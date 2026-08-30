# Frontier Artifact Pack

Generated: 2026-08-30T08:06:33.884117+00:00

## Thesis
The moat is shifting from smarter models to harnesses that keep agents inside long-running worlds — whoever owns the observe→act→verify loop for a legacy ecosystem owns the ecosystem, and DCS-Harness proves hobbyists are already shipping it before vendors.

## Doctrine
Every Shadow loop action must emit a runtime receipt: the intended state change, the verification probe that confirmed it, and a retry gate if the probe fails — unverified actions count as failures, not outputs.

## Proof Artifact
Ship a receipt-verifier module (shadow/verify_receipt.py) that wraps loop task execution: records intent, runs a post-action probe (file diff, HTTP check, or metric read), writes pass/fail receipts to a receipts.jsonl ledger, and gates one automatic retry on failure.

Next action: Create shadow/verify_receipt.py and receipts.jsonl in the working directory, wire the receipt wrapper around the existing research_signal_candidates processing step, and record the first pass/fail receipt on the next loop run.

## Public Angle
Everyone benchmarks agent intelligence; almost nobody benchmarks whether the agent's action actually changed the world. We started logging receipts for every autonomous action our system takes — here's what the failure rate taught us about 'working' agents.

## Buyer Offer
Position a 'verified automation' tier for small operators: Shadow runs a recurring back-office loop (reporting, monitoring, content ops) where every run comes with a machine-checked receipt log the client can audit — priced at $99/mo, five clients hits the $500 target.

## Source Signals
- Agents Don't Paginate: First-Chunk Selection for LLM Tool Responses
- Prime Agent: A Self-Improving RLM Harness | Seth Karten Home Research Canonical page Agent Harnesses · Technical Report Prime Agent: A Self-Improving RLM Harnes
- Distributed Training using an Intelligent Network
- yuriak/DCS-Harness — An agent-native workspace for autonomous DCS mission direction
- Carer-Healthcare-AI/Hospilot — Open-source agentic AI operating layer for hospital operations — multi-agent orchestration over FHIR

## Scale Packets
- proof_artifact: promoted (cdbbab792cad)
- public_wedge: promoted (8dbade1443b6)
- buyer_experiment: promoted (ef6fbbee0e31)
- operator_doctrine: promoted (f84e09845891)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (cdbbab792cad)
- public_wedge: queued_echo_draft (8dbade1443b6)
- buyer_experiment: queued_buyer_experiment (ef6fbbee0e31)
- operator_doctrine: already_persisted (f84e09845891)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
