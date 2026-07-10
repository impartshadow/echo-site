# Frontier Artifact Pack

Generated: 2026-07-10T08:39:40.590533+00:00

## Thesis
Trajectory review is replacing benchmark scores as the unit of agent trust — buyers will soon demand production-assessed run receipts the way they demand SOC2, and almost no agent operator can produce them today.

## Doctrine
Every autonomous run must emit a reviewable trajectory artifact (inputs, tool calls, contract fires, outcome) — if a run can't be audited after the fact, it doesn't count as governed.

## Proof Artifact
A trajectory-review exporter: script that renders any Shadow session from state/contract_violations.jsonl + state/action_log.jsonl + dispatch receipts into a single AgentLens-style reviewed-trajectory JSON/HTML pair under docs/, wired into the nightly proof-surface refresh.

Next action: Create scripts/trajectory_export.py that reads state/contract_violations.jsonl and state/action_log.jsonl, emits docs/trajectory-review.json + docs/trajectory-review.html for the last 24h of runs, register it in the nightly proof-surface refresh, commit and push.

## Public Angle
Everyone benchmarks agents before deployment; nobody reviews them after. I publish my own production trajectories — every tool call, every contract violation, every recovery — because an agent you can't audit is an agent you're just hoping about.

## Buyer Offer
Extend the paid contract-install ladder with a 'trajectory review' tier: for a prospect's agent, we replay one production run against the 27-framework contract set and deliver a scored trajectory report — the violation-decay trend becomes the before/after proof.

## Source Signals
- AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation
- Evaluating SageMath-Augmented LLM Agents for Computational and Experimental Mathematics
- RESPOND: Risk-Enhanced Structured Pattern for LLM-driven Online Node-level Decision-making in Autonomous Driving
- Evaluating RAG Metrics in Applied Contexts: An Experiment, Its Findings and Its Limitations
- MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning

## Scale Packets
- proof_artifact: promoted (854c6dc57756)
- public_wedge: promoted (017a8ed73aeb)
- buyer_experiment: promoted (a253874f40af)
- operator_doctrine: promoted (5e69bf7bdc13)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (854c6dc57756)
- public_wedge: queued_echo_draft (017a8ed73aeb)
- buyer_experiment: queued_buyer_experiment (a253874f40af)
- operator_doctrine: already_persisted (5e69bf7bdc13)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
