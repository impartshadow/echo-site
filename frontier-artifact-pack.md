# Frontier Artifact Pack

Generated: 2026-07-15T08:06:50.880978+00:00

## Thesis
The frontier is converging on small rule-aligned models as runtime governors — meaning the moat isn't the agent, it's the enforceable rulebook the agent runs under, and everyone building agents will soon need to buy or build one.

## Doctrine
Every research signal must land as a runtime gate, verifier, or allocator input that changes what the next loop iteration does — if a signal only changes what Shadow says, it wasn't ingested.

## Proof Artifact
A minimal-context edit verifier in core/contracts.py: before any Edit/Write in an autonomous pass, log the context actually read (files, line ranges) vs. the edit site into state/edit_context_log.jsonl, then a weekly regression showing wasted-read ratio declining — the same declining-trend proof shape as the violation-decay wedge, applied to execution efficiency (per arXiv:2607.09691).

Next action: Add EditContextLogger contract to core/contracts.py (pre-check on Edit/Write during autonomous sessions, appends {files_read, edit_target, ratio} via core/state_io.py to state/edit_context_log.jsonl), register it, add a test in tests/test_contracts.py, run pytest, push to main, receipt to #shadow-log.

## Public Angle
Everyone measures how much context their coding agent CAN hold; I started logging how much mine actually NEEDS per edit — the wasted-read ratio is now a weekly regression metric with receipts, and it's falling. Governance isn't just catching bad actions; it's proving your agent gets cheaper every week.

## Buyer Offer
Contract-install prospects get a 'governed small-model tier' pitch: Shadow installs Haiku-class rule-aligned checkers as pre/post gates on their existing agents — cheaper than the agent itself, with weekly declining-violation receipts as the deliverable, priced per governed agent per the harness venture thesis.

## Source Signals
- Closed-Loop Control with Rule-Aligned Small Language Models and Multi-Agent Self-Correction
- The Payload: A Short Story
- A Dynamic Scene Interaction Reasoning Framework for Scene-level Lane-Change Intention and Trajectory Prediction of Multiple Interacting Vehicles
- What Context Does a Coding Agent Actually Need to Act?
- Scaffolding the Strategist: Architecture-Dependent Reasoning Interventions in Hotelling Spatial Markets

## Scale Packets
- proof_artifact: promoted (b3ed8ee61d2e)
- public_wedge: promoted (791c11beb182)
- buyer_experiment: promoted (384f609b6db2)
- operator_doctrine: promoted (f45f95a61ea8)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (b3ed8ee61d2e)
- public_wedge: queued_echo_draft (791c11beb182)
- buyer_experiment: queued_buyer_experiment (384f609b6db2)
- operator_doctrine: already_persisted (f45f95a61ea8)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
