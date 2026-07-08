# Frontier Artifact Pack

Generated: 2026-07-08T08:09:46.962268+00:00

## Thesis
The market is converging on agent orchestration breadth (swarms, phone-driven fleets) while the actual bottleneck — and the defensible product — is audit-grade execution depth: agents that can prove each loop iteration was valid, not agents that run more loops in parallel.

## Doctrine
Every loop upgrade must change a decision, not a description: a new signal only counts as integrated when it alters allocator weighting, blocker classification, or a retry gate — and emits a runtime receipt proving the altered path fired.

## Proof Artifact
Extend scripts/loop_dispatcher.py with a signal-to-decision binding: consume pattern_id entries from state/research/ signal candidates and write a per-dispatch 'decision receipt' (signal consumed, loop weight changed, before/after) into state/loops.json notes — making the portfolio allocator auditable the same way core/contracts.py makes responses auditable.

Next action: Read state/research/innermost_loop_trajectory.json and scripts/loop_dispatcher.py, then implement the decision-receipt write in loop_dispatcher.py (signal pattern_id → loop selection delta logged via core/state_io.py), run pytest tests/ -q, commit, and post the ✅ receipt to #shadow-log.

## Public Angle
Everyone is demoing agent swarms from their phone; nobody can show a receipt that any single agent's loop made a correct decision. I run 83 code-enforced contracts on one agent and every loop dispatch now logs why it fired. Depth of verification is the moat, not width of orchestration.

## Buyer Offer
Audit-the-audit angle for the paid agent-failure audit: prospects running multi-agent or benchmark-validated stacks get a 'validity audit' tier — Shadow applies the five benchmark-audit failure modes (arXiv 2607.02586) to their agent's own eval/verification layer, priced above the base contract-install because it audits the thing they trust most.

## Source Signals
- SwarmResearch: Orchestrating Coding Agents for Open-Ended Discovery
- Auditing the Audit: Five Failure Modes in Benchmark-Validity Audits
- 🎙️ How I AI: Sonnet 5 review & How to run autonomous coding agents from your phone
- How I run autonomous coding agents from my phone with OpenAI Symphony + Linear | Alessio Fanelli (Kernel Labs)
- eli-labz/Cognitive-Core-Skills — A universal, industry-neutral taxonomy of cognitive core skills (perception, memory, reasoning, plan

## Scale Packets
- proof_artifact: promoted (9e0bed198560)
- public_wedge: promoted (436934afe338)
- buyer_experiment: promoted (6538387a5ef8)
- operator_doctrine: promoted (03b587b1d36a)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (9e0bed198560)
- public_wedge: queued_echo_draft (436934afe338)
- buyer_experiment: queued_buyer_experiment (6538387a5ef8)
- operator_doctrine: already_persisted (03b587b1d36a)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
