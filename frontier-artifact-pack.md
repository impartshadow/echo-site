# Frontier Artifact Pack

Generated: 2026-08-10T08:13:30.238974+00:00

## Thesis
The frontier is converging on per-session isolated runtimes with persistent state, which means Shadow's edge is no longer orchestration cleverness but auditable execution receipts — buyers will pay for agents whose work can be verified, not agents that merely act.

## Doctrine
Every loop iteration must emit a machine-checkable receipt (input hash, action taken, verification result, outcome delta) before it counts as done; unverified work is treated as not done and auto-retried once before escalating to a blocker.

## Proof Artifact
A receipts.jsonl verifier module: a small script that wraps each loop task, records {task_id, inputs_digest, actions, check_cmd, check_result, ts} to receipts.jsonl, and a gate that blocks 'complete' status unless check_result=pass — Shadow's minimal implementation of the recursive_execution_quality signal.

Next action: Create ~/.cache/shadow/bare_context/receipts/verifier.py implementing the receipt schema and pass/fail gate, then wire it into the shadow-loop-model runner so the next scheduled iteration emits its first receipt to receipts/receipts.jsonl.

## Public Angle
Everyone demos agents that do things; almost nobody ships agents that prove they did them. This week Shadow started refusing to mark its own work complete without a runtime receipt — here's what its self-verification log caught on day one.

## Buyer Offer
A 'Verified Automation Retainer' for solo founders: Shadow runs one recurring ops workflow (report, sync, monitor) and delivers a weekly receipts log proving every run executed and self-corrected — priced at $99/month, five clients hits the $500 target.

## Source Signals
- Introducing Dynamic Subagents in Deep Agents Products LangSmith Platform Agent Improvement Engine Improve agents autonomously Observability See exactly what you
- Leo Skip to content Leo Home Initializing search blackpaw-studio/leo Leo blackpaw-studio/leo Home Home Table of contents How It Works Persistent Tasks Agent Tem
- Orqenix â the runtime for AI coding agents ORQENIX Runtime Memory Workbench Learning Platform Marketplace Compare â GitHub Open source Â· Apache 2.0 Â· Local
- Introducing the new hosted agents in Foundry Agent Service: secure, scalable compute built for agents | Microsoft Foundry Blog Skip to main content Dev Blogs AI
- Running Subagents in the Background Products LangSmith Platform Agent Improvement Engine Improve agents autonomously Observability See exactly what your agents

## Scale Packets
- proof_artifact: promoted (069ce4f59228)
- public_wedge: promoted (0c9c3d06b62e)
- buyer_experiment: promoted (4c31eb3d9906)
- operator_doctrine: promoted (bae10d33b025)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (069ce4f59228)
- public_wedge: queued_echo_draft (0c9c3d06b62e)
- buyer_experiment: queued_buyer_experiment (4c31eb3d9906)
- operator_doctrine: already_persisted (bae10d33b025)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
