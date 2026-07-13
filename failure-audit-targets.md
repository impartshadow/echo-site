# Failure-Audit Target Map

Generated: 2026-07-13T03:30:58-05:00 CT

Goal: Get one real submitted production-agent failure trace.

Intake: https://impartshadow.github.io/echo-site/failure-intake.html
Flagship: https://impartshadow.github.io/echo-site/agent-failure-flagship.html
Museum: https://impartshadow.github.io/echo-site/failure-museum.html

## Targets

### Patrick Thompson / CrewAI

- Score: 95
- Status: sent
- Hook: Crew-style delegation and task-completion boundaries.
- Ask: Send one real CrewAI failure where a crew claimed completion, retried a side effect, or crossed a delegation boundary without the receipt a buyer would need.

### Jacob Lee / LangGraph.js

- Score: 94
- Status: sent
- Hook: Graph node/tool boundaries where success can outrun the surrounding receipt.
- Ask: Send one LangGraph-style failure where a node, tool call, or side-effect boundary reported success before the workflow had a receipt.

### Scott Condron / W&B Weave

- Score: 92
- Status: sent
- Hook: Trace observability adjacent to the point where operational claims still need receipts.
- Ask: Send one Weave-adjacent failure where the trace showed the sequence but the operational claim still needed proof: done, sent, deployed, verified, or safe to proceed.

### Guillaume Noziere / Patronus AI

- Score: 90
- Status: sent
- Hook: Evaluator/judge output that identifies a problem after the action has already crossed the boundary.
- Ask: Send one agent failure where a post-hoc eval identified the issue, but the same class could recur because no runtime gate existed.

### Ameya Bhatawdekar / Braintrust

- Score: 89
- Status: sent
- Hook: Evaluation traces that reveal what happened but not what should have blocked it.
- Ask: Send one failure where the trace showed what happened, but a human still had to decide which boundary should have blocked it.
