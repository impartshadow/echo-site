from dataclasses import replace
from langgraph.prebuilt import ToolNode
from langgraph.types import Command, Send
def _combine_tool_outputs(self, outputs, input_type):
    flat_outputs = [o for out in outputs for o in (out if isinstance(out, list) else [out])] if any(isinstance(o, list) for o in outputs) else list(outputs)
    combined = []; parent_command = None
    for output in flat_outputs:
        if isinstance(output, Command):
            if output.graph is Command.PARENT and isinstance(output.goto, list) and all(isinstance(s, Send) for s in output.goto):
                if parent_command:
                    parent_command = replace(parent_command, goto=list(parent_command.goto) + output.goto,
                        update=list(parent_command._update_as_tuples()) + list(output._update_as_tuples()))
                else:
                    parent_command = output   # preserve update/resume (as #4019 did)
            else:
                combined.append(output)
        else:
            combined.append([output] if input_type == "list" else {self._messages_key: [output]})
    if parent_command: combined.append(parent_command)
    return combined
ToolNode._combine_tool_outputs = _combine_tool_outputs
