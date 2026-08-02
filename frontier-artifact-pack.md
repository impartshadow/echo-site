# Frontier Artifact Pack

Generated: 2026-08-02T08:01:00.084776+00:00

## Thesis
The orchestration-research wave (OrchBench, attention allocation) is optimizing plans nobody can audit — the market gap isn't smarter routing, it's routing with receipts, and Shadow already owns that lane.

## Doctrine
Every model/task routing decision gets logged as a machine-readable receipt (task class, model chosen, observed outcome) so routing improves from evidence, not defaults — ungoverned optimization is just drift with better PR.

## Proof Artifact
core/model_router.py — an observed-strength routing table (task class → model) backed by state/model_routing_ledger.jsonl, seeded from existing routing rules (Codex for code, Sonnet for voice, Haiku for judging, Gemini chain) and updated by logged outcomes; wire it into core/claude_client.py as the single decision point.

Next action: Create core/model_router.py with the seeded routing table + ledger writes via core/state_io.py, add tests/test_model_router.py, run pytest, commit and push, post receipt to #shadow-log.

## Public Angle
Everyone benchmarks orchestration in simulation (OrchBench dropped this week). I log every routing decision my own agent makes in production — model, task, outcome — and the ledger disagrees with the benchmarks more often than you'd think. Simulated plan quality is a map; the receipt ledger is the territory.

## Buyer Offer
Contract-install upsell: 'Your agent picks models by vibes — I install a routing ledger that shows which model earned each task, with per-task receipts. OrchBench evaluates plans in simulation; this governs them in production.'

## Source Signals
- Data and Environment Curation for Post-Training LLMs — Mahesh Sathiamoorthy, Bespoke Labs
- daly2211/autoretrieval — AI agent autonomously optimizing RAG retrieval pipelines against your own documents
- Focus Is All You Need: Adaptive Goal-aware Attention Orchestration for Multi-Agent Graph Systems
- OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation
- Welcome to July 31, 2026

## Scale Packets
- proof_artifact: promoted (857a08f32c11)
- public_wedge: promoted (b97b2262c757)
- buyer_experiment: promoted (7c88f6784d02)
- operator_doctrine: promoted (d4cac5425507)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (857a08f32c11)
- public_wedge: queued_echo_draft (b97b2262c757)
- buyer_experiment: queued_buyer_experiment (7c88f6784d02)
- operator_doctrine: already_persisted (d4cac5425507)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
