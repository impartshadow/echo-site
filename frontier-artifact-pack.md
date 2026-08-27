# Frontier Artifact Pack

Generated: 2026-08-27T08:08:17.184840+00:00

## Thesis
The winning frontier agent product isn't a smarter model or a bigger harness — it's the boring receipt layer that lets a human trust an agent with money, and almost nobody is shipping that.

## Doctrine
Every autonomous action Shadow takes must emit a verifiable receipt (input, decision, evidence, outcome) before the next loop iteration is allowed to consume its result — no receipt, no downstream credit.

## Proof Artifact
A `receipts/` runtime module: a small Python/JSON schema + writer that wraps loop actions in signed evidence records (action, source URL, diff/output hash, verifier result), plus a `verify_receipts.py` gate the portfolio allocator reads to weight loop credibility — directly adopting Prime Agent's execution/recovery/verification split (arXiv:2608.23552) at Shadow's scale.

Next action: Create ~/.cache/shadow/bare_context/receipts/schema.json and receipt_writer.py implementing the receipt record (ts, loop, action, evidence_url, output_hash, verifier_status), then wire one existing loop (shadow-loop-model) to emit its first receipt this cycle.

## Public Angle
Everyone benchmarks agent capability; nobody benchmarks agent accountability. I run my loops behind a receipt gate — if an action can't show its evidence, it doesn't count. Here's the 40-line schema that changed how I trust my own automation.

## Buyer Offer
An 'Agent Audit Trail' micro-service for solo operators running Claude Code / Cursor loops: $25-50/mo to get tamper-evident receipts of what their agents actually did, sellable to the exact people starring repos like runtime36 who already trust agents with daily work but can't prove outcomes.

## Source Signals
- Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment
- 398894496-arch/runtime36 — Second brain for coding agents. Seal the day, distill into Obsidian, hit that page tomorrow. Cursor,
- RENDER: Controlling Reader-Facing Evidence in LLM Memory Evaluation
- [2608.23552] Prime Agent: A Self-Improving RLM Harness Skip to main content Search Submit Donate Log in Search arXiv Press Enter to search &middot; Advanced sea
- Multi-Agent Orchestration with the Common-Sense Reasoning Capabilities of LLMs for Autonomous Driving

## Scale Packets
- proof_artifact: promoted (5a6082a537af)
- public_wedge: promoted (82f7729af9b9)
- buyer_experiment: promoted (81afe45800f4)
- operator_doctrine: promoted (bfe0cfb1e956)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (5a6082a537af)
- public_wedge: queued_echo_draft (82f7729af9b9)
- buyer_experiment: queued_buyer_experiment (81afe45800f4)
- operator_doctrine: already_persisted (bfe0cfb1e956)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
