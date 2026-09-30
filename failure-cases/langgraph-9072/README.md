# langgraph#9072 — sibling ParentCommand coalescing candidate

Repro from https://github.com/langchain-ai/langgraph/issues/9072#issuecomment-5914500115
pinned: langgraph 1.2.9, langgraph-prebuilt 1.1.0, langchain 1.3.14, langchain-core 1.4.9.

- `patch9072.py` — runner-boundary candidate: collect sibling `ParentCommand`s in `_panic_or_proceed` and raise one coalesced command (shared graph required, >1 non-None resume raises, gotos normalized, updates concatenated as `_update_as_tuples()`).
- `patch_toolnode.py` — restores `parent_command = output` for the first Send-list PARENT command so `update`/`resume` survive the ToolNode rebuild.
- `repro_both.py` / `repro_both_async.py` — the reporter's repro with both patches applied (sync / ainvoke).

Results (20 runs each): unpatched drops one sibling on both paths; runner patch alone restores both workers but the Send path still lacks ToolMessages; both patches: `(('c1','c2'),('x','y'))` on both paths, sync and async, nothing dropped. ToolMessage order still flips between runs because `done` is a set.
Not covered: in-flight sibling cancellation, deterministic write order, upstream suite.
