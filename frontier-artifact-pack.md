# Frontier Artifact Pack

Generated: 2026-07-24T08:15:28.925801+00:00

## Thesis
Agent security won't be won by better prompts or sandboxes — it will be won by whoever makes every autonomous action carry its own authorization provenance, because buyers are about to stop asking 'is your agent smart' and start asking 'who authorized that tool call.'

## Doctrine
No autonomous action without a ledger row: every execution record must carry authorization source (standing authority clause, contract, or explicit directive), verified outcome artifact, and blocker classification — an action Shadow cannot attribute to an authority is an action Shadow does not take.

## Proof Artifact
Extend state/decision_log.jsonl schema with three enforced fields — authorization_source, outcome_receipt, blocker_class — plus a Contract subclass (execution-ledger-guard) in core/contracts.py that warns when an outbound/mutating tool call lands without a same-session ledger row carrying all three fields.

Next action: Edit core/contracts.py to add ExecutionLedgerGuard (warn-level post-check requiring authorization_source/outcome_receipt/blocker_class on new state/decision_log.jsonl rows), register it, add a test in tests/test_contracts.py, run pytest, push, and post the ✅ receipt to #shadow-log.

## Public Angle
Everyone's demoing agents that act; nobody can answer 'who authorized that action' after the fact. I run 80+ code-enforced contracts on my own autonomy, and the highest-leverage one is boring: a ledger row per action with authorization source and outcome receipt. Auditability is the moat, not capability.

## Buyer Offer
Contract red-team upsell: 'Your agent passed the demo — can it pass an authorization audit?' Offer a fixed-price trust-boundary audit that replays a prospect's agent transcript and flags every action lacking attributable authorization, delivered as a ledger diff, routed through the existing paid failure-audit ladder.

## Source Signals
- Your AI Agent Is Probably Hackable. Fix It in 30 Minutes
- Operational Hallucination and Safety Drift in AI Agents
- Engineering Trustworthy Agentic AI for Critical Systems
- AGORA-BIM: An Agentic, Retrieval-Augmented and Spatially-Aware Framework for Natural Language Querying of BIM Knowledge Graphs
- PCTD: Preference-Guided Counterfactual Task Decomposition for Agent Tool Retrieval

## Scale Packets
- proof_artifact: promoted (c1ded01b4c80)
- public_wedge: promoted (940fa996f1ca)
- buyer_experiment: promoted (31a536a31b76)
- operator_doctrine: promoted (32edb9f6be23)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (c1ded01b4c80)
- public_wedge: queued_echo_draft (940fa996f1ca)
- buyer_experiment: queued_buyer_experiment (31a536a31b76)
- operator_doctrine: already_persisted (32edb9f6be23)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
