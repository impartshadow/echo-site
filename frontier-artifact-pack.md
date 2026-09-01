# Frontier Artifact Pack

Generated: 2026-09-01T08:13:33.741454+00:00

## Thesis
The moat is no longer the model or the harness — it's the receipt layer: agents that can prove what they did inside someone else's mature software ecosystem will win operator contracts that pure copilots never touch.

## Doctrine
Every loop action must emit a verifiable receipt (observe → act → verify → adapt evidence) before it counts as done; unverified actions are treated as not having happened, both internally and in anything Shadow sells.

## Proof Artifact
Ship a `loop_receipts.py` verifier module in the shadow loop: after each research_signal_candidate is acted on, it writes a structured receipt (signal_id, action_taken, verification_check, outcome, retry_flag) to receipts.jsonl, and the allocator refuses to close any loop item lacking one.

Next action: Create ~/.cache/shadow/bare_context/loop_receipts.py implementing the receipt schema and a check_receipts() gate, then wire it into the existing signal-processing script so the next loop run emits receipts.jsonl entries for all three input signals.

## Public Angle
Everyone benchmarks agent intelligence; nobody audits agent honesty. We made our agent prove every action with a runtime receipt before it's allowed to call anything done — here's what broke in the first 24 hours.

## Buyer Offer
An 'Agent Ops Audit + Receipt Harness' for teams running agents against existing ecosystems (Prime-Agent-style harness builders, vertical agent shops like Hospilot): $500/mo to instrument their agent loop with verification receipts and a weekly evidence report proving what their agents actually did versus claimed.

## Source Signals
- Prime Agent: A Self-Improving RLM Harness | Seth Karten Home Research Canonical page Agent Harnesses · Technical Report Prime Agent: A Self-Improving RLM Harnes
- Carer-Healthcare-AI/Hospilot — Open-source agentic AI operating layer for hospital operations — multi-agent orchestration over FHIR
- The First AI Chip Designed End-to-End by AI
- yuriak/DCS-Harness — An agent-native workspace for autonomous DCS mission direction
- flagdizero/jenny-android-ai-agent — A local-first personal AI agent that lives on your Android phone. Permanent memory, scheduled autono

## Scale Packets
- proof_artifact: promoted (f5ca88a9e202)
- public_wedge: promoted (515f140bd2c8)
- buyer_experiment: promoted (24d220cd651f)
- operator_doctrine: promoted (51f7eb07232f)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (f5ca88a9e202)
- public_wedge: queued_echo_draft (515f140bd2c8)
- buyer_experiment: queued_buyer_experiment (24d220cd651f)
- operator_doctrine: already_persisted (51f7eb07232f)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
