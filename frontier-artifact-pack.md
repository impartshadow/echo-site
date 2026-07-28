# Frontier Artifact Pack

Generated: 2026-07-28T08:04:21.269770+00:00

## Thesis
The frontier is quietly conceding that agent capability is now bottlenecked by verifiable execution memory — not model quality — so the winners will be operators who can prove what their agents did, not describe what they can do.

## Doctrine
Every retained skill or workflow must carry its own receipt: if a loop learns a procedure (FlowEvo-style), the procedure is only 'real' once it has an execution record with a verifiable outcome — persist the receipt with the skill, never the skill alone.

## Proof Artifact
A skill-receipt ledger: extend core/loop_runtime_receipts.py so any repeated procedure Shadow executes ≥2x gets registered in state/skill_ledger.jsonl with {procedure_id, first_run, last_verified_outcome, receipt_ref, failure_count} — turning transient loop wins into governed, reusable, evidence-backed skills.

Next action: Add SkillLedger to core/loop_runtime_receipts.py writing via core/state_io.py to state/skill_ledger.jsonl, wire it into the existing receipt emit path, add tests/test_skill_ledger.py, run pytest, commit and push, receipt to #shadow-log.

## Public Angle
Everyone is publishing self-evolving-agent papers this week; nobody ships the boring half — my agent doesn't 'learn skills', it earns them: a procedure only enters the ledger after it has produced a verified outcome twice, and I can show you the receipts.

## Buyer Offer
Pitch prospects a 'procedure audit': most agent stacks re-derive the same workflow every run and can't prove any past run succeeded — Shadow installs a receipt-backed skill ledger so their agent's learned procedures are inspectable, reusable, and auditable (contract-install ladder upsell).

## Source Signals
- The Best Doctor May Soon Be AI
- AgentKVShift: Efficient KV Cache Reuse for Agentic Memory Systems
- Agentic Evaluation of Copyright Law Compliance
- Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings
- Encoding Invisible Causation for Bridge Diagnostic Agents: Triple-Guided Retrieval-Augmented Fine-Tuning with QLoRA

## Scale Packets
- proof_artifact: promoted (44f77c0f10e9)
- public_wedge: promoted (2171e17e0641)
- buyer_experiment: promoted (992854cc3e43)
- operator_doctrine: promoted (b063fd13a686)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (44f77c0f10e9)
- public_wedge: queued_echo_draft (2171e17e0641)
- buyer_experiment: queued_buyer_experiment (992854cc3e43)
- operator_doctrine: already_persisted (b063fd13a686)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
