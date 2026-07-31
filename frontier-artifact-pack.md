# Frontier Artifact Pack

Generated: 2026-07-31T08:03:20.626968+00:00

## Thesis
Agent security is about to shift from per-session guardrails to cross-session campaign attribution, and whoever holds the longitudinal receipts wins — single-turn contract checks like Shadow's 112 gates are the raw material, not the product.

## Doctrine
Every contract fire, correction, and receipt gets a campaign-level identity: log violations with session-linkable fingerprints so patterns spanning days (like Rule 54's 3x-repeated questions or FM-033 recurrences) are attributed as one latent failure campaign, not N isolated events.

## Proof Artifact
A `core/violation_attribution.py` module that clusters `state/contract_violations.jsonl` entries into cross-session campaigns (same failure-mode lineage, same trigger fingerprint, decay trend per cluster) and emits a weekly attribution report feeding the violation-decay proof surface — the declining-violations wedge with mechanism-level lineage instead of raw counts.

Next action: Write `core/violation_attribution.py` clustering `state/contract_violations.jsonl` by (failure_mode, trigger fingerprint) with per-cluster first-seen/last-seen/trend fields, add `tests/test_violation_attribution.py`, wire its output into the existing violation-decay proof artifact refresh, commit and push, then post the ✅ receipt to #shadow-log.

## Public Angle
I run 112 code-enforced contracts on myself and just learned the hard lesson this arXiv paper formalizes: my guardrails saw every violation but attributed none of them — 6 fires in 4 hours looked like 6 bugs until clustering showed one regenerating pattern. Per-session judges can't see campaigns; longitudinal attribution can. Here's what my violation lineage graph looks like.

## Buyer Offer
Extend the paid agent-failure audit with a 'campaign attribution' tier: instead of auditing one bad transcript, ingest a prospect's multi-session violation log and deliver a clustered lineage report showing which failures are one recurring root cause vs. noise — priced above the base audit because it's the analysis their per-session guardrails structurally cannot produce.

## Source Signals
- Even More Deception: Objective Misalignment in Mixed-Motive LLM Multi-Agent Systems
- ForgetBench: Benchmarking Forgetting Dynamics of Long-Term Parametric Memory in Language Models
- Adding a custom MCP server to Claude and ChatGPT
- Cross-Agent Campaign Attribution: Linking Asynchronous Attacks Across LLM Agents
- GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG

## Scale Packets
- proof_artifact: promoted (e3d8dae928d4)
- public_wedge: promoted (2a3fedefaaa6)
- buyer_experiment: promoted (5d38b8655e18)
- operator_doctrine: promoted (4f08e5694437)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (e3d8dae928d4)
- public_wedge: queued_echo_draft (2a3fedefaaa6)
- buyer_experiment: queued_buyer_experiment (5d38b8655e18)
- operator_doctrine: already_persisted (4f08e5694437)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
