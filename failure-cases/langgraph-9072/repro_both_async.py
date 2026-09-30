import asyncio
import patch9072, patch_toolnode
import collections
from typing import Annotated

from langchain.agents import create_agent
from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.tools import InjectedToolCallId, tool
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode
from langgraph.types import Command, Send

# Instrumentation only: how many tool outputs does ToolNode combine per call?
combine_sizes = collections.Counter()
_combine = ToolNode._combine_tool_outputs


def _spy(self, outputs, input_type):
    combine_sizes[len(outputs)] += 1
    return _combine(self, outputs, input_type)


ToolNode._combine_tool_outputs = _spy


class FakeModel(GenericFakeChatModel):
    def bind_tools(self, tools, **kwargs):
        return self


def make_handoff(dest: str, goto_as_send: bool):
    @tool(f"delegate_{dest}", description=f"hand off to {dest}")
    def handoff(task: str, tool_call_id: Annotated[str, InjectedToolCallId]):
        tm = ToolMessage(content="forwarded", name=f"delegate_{dest}", tool_call_id=tool_call_id)
        goto = [Send(dest, {"messages": [HumanMessage(content=task)]})] if goto_as_send else dest
        return Command(goto=goto, update={"messages": [tm]}, graph=Command.PARENT)

    return handoff


def make_worker(name: str, visited: list):
    def worker(state: MessagesState):
        visited.append(name)
        return {"messages": [HumanMessage(content=f"reply from {name}", name=name)]}

    return worker


def run_once(goto_as_send: bool):
    visited = []
    llm = FakeModel(messages=iter([
        AIMessage(content="", tool_calls=[  # two sibling handoffs in the same turn
            {"name": "delegate_x", "args": {"task": "t1"}, "id": "c1"},
            {"name": "delegate_y", "args": {"task": "t2"}, "id": "c2"},
        ]),
        AIMessage(content="done"),
    ]))
    tools = [make_handoff("x", goto_as_send), make_handoff("y", goto_as_send)]
    builder = StateGraph(MessagesState)
    builder.add_node("sup", create_agent(llm, tools=tools, name="sup"), destinations=("x", "y"))
    builder.add_edge(START, "sup")
    for name in ("x", "y"):
        builder.add_node(name, make_worker(name, visited))
        builder.add_edge(name, "sup")
    out = asyncio.run(builder.compile().ainvoke({"messages": [HumanMessage(content="hi")]}))
    tool_messages = tuple(m.tool_call_id for m in out["messages"] if isinstance(m, ToolMessage))
    return tool_messages, tuple(sorted(visited))


for goto_as_send in (False, True):
    label = "goto=[Send(...)]" if goto_as_send else "goto='node'     "
    print(label, dict(collections.Counter(run_once(goto_as_send) for _ in range(20))))
print("len(outputs) per ToolNode._combine_tool_outputs call:", dict(combine_sizes))
