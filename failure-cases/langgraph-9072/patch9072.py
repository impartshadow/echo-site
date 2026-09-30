"""Bounded candidate: coalesce sibling ParentCommands raised in one superstep."""
from dataclasses import replace
import langgraph.pregel._runner as runner
from langgraph.errors import GraphInterrupt, ParentCommand
from langgraph.types import Command, Send

class ParentCommandConflict(Exception):
    pass

def coalesce_parent_commands(excs):
    cmds = [e.args[0] for e in excs]
    if len(cmds) == 1:
        return excs[0]
    graphs = {c.graph for c in cmds}
    if len(graphs) != 1:
        raise ParentCommandConflict(f"sibling Command.PARENT targets differ: {graphs}")
    resumes = [c.resume for c in cmds if c.resume is not None]
    if len(resumes) > 1:
        raise ParentCommandConflict("multiple sibling tools returned non-None resume")
    gotos = []
    for c in cmds:
        g = c.goto
        if g is None or g == ():
            continue
        gotos.extend(list(g) if isinstance(g, (list, tuple)) else [g])
    update = [t for c in cmds for t in c._update_as_tuples()]  # ordered, duplicate keys kept
    merged = Command(graph=cmds[0].graph, goto=gotos, update=update or None,
                     resume=resumes[0] if resumes else None)
    return ParentCommand(merged)

_orig = runner._panic_or_proceed
_exception = runner._exception

def _panic_or_proceed(futs, *, timeout_exc_cls=TimeoutError, panic=True,
                      handled_exception_ids=None, handled_futures=None):
    done = set(); inflight = set()
    for fut in futs:
        if fut.cancelled(): continue
        (done if fut.done() else inflight).add(fut)
    interrupts = []; parents = []
    while done:
        fut = done.pop()
        if exc := _exception(fut):
            if fut in (handled_futures or set()): continue
            if id(exc) in (handled_exception_ids or set()): continue
            while inflight: inflight.pop().cancel()
            if panic:
                if isinstance(exc, GraphInterrupt): interrupts.append(exc)
                elif isinstance(exc, ParentCommand): parents.append(exc)   # NEW
                elif fut not in runner.SKIP_RERAISE_SET: raise exc
    if interrupts:
        raise GraphInterrupt(tuple(i for exc in interrupts for i in exc.args[0]))
    if parents:
        raise coalesce_parent_commands(parents)                           # NEW
    if inflight:
        while inflight: inflight.pop().cancel()
        raise timeout_exc_cls("Timed out")

runner._panic_or_proceed = _panic_or_proceed
