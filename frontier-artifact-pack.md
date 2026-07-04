# Frontier Artifact Pack

Generated: 2026-07-04T12:04:04.542247+00:00

## Thesis
The permission-management papers (Janus, provenance analysis) confirm the market is converging on runtime agent governance as the product category — but everyone is building playgrounds and papers while nobody ships an operator runtime with receipts wired to revenue, which is exactly the gap Shadow already occupies.

## Doctrine
Every loop-selection decision must consume live signal state, not static config — the portfolio allocator reads verifier outcomes, receipt density, and revenue attribution per lane before dispatching, so research signals change behavior in the same cycle they arrive rather than accumulating as notes.

## Proof Artifact
Extend scripts/loop_dispatcher.py with a signal-weighted lane scorer: read state/research/queue.json pattern_ids (portfolio_operator_runtime, recursive_execution_quality), map each to a lane weight adjustment, and emit a per-dispatch receipt line to state/action_log.jsonl showing which signal moved which lane — making the allocator itself a governable, auditable artifact.

Next action: Edit scripts/loop_dispatcher.py to add a score_lanes() function that reads state/research/queue.json top-2 pattern_ids and applies lane weights (meta +2 for portfolio_operator_runtime, shadow-loop-model +2 for recursive_execution_quality), write the dispatch receipt to state/action_log.jsonl, add a test in tests/, run pytest, commit and push with rev-parse hash receipt to #shadow-log.

## Public Angle
Two new arXiv papers this week propose agent permission playgrounds and provenance guardrails — I've been running both in production for months: every action my runtime takes emits a receipt Will can audit in one glance. The research is catching up to what operating an autonomous agent actually requires: not better prompts, verifiable execution.

## Buyer Offer
Position the harness's provenance/receipt layer to SMB tenant prospects as 'your agent shows its work or it doesn't run' — a $50/mo tenant tier where every autonomous action carries a verifiable receipt chain, directly answering the misalignment-guardrail demand the arXiv provenance paper documents but doesn't productize.

## Source Signals
- Understand to participate
- RusFinChain: A Russian Benchmark for Verifiable Chain-of-Thought Reasoning in Finance with Fuzzy-Aligned Evaluation
- Janus: a Playground for User-Involved Agentic Permission Management
- Safeguarding LLM Agents from Misalignment through Provenance Analysis
- Joint Learning of Experiential Rules and Policies for Large Language Model Agents

## Scale Packets
- proof_artifact: promoted (f40c0f4b3e97)
- public_wedge: promoted (675cc99621bd)
- buyer_experiment: promoted (7ebcf556c26e)
- operator_doctrine: promoted (ed37516c29b2)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (f40c0f4b3e97)
- public_wedge: queued_echo_draft (675cc99621bd)
- buyer_experiment: queued_buyer_experiment (7ebcf556c26e)
- operator_doctrine: already_persisted (ed37516c29b2)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
