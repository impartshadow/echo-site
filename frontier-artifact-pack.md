# Frontier Artifact Pack

Generated: 2026-08-16T08:12:04.865678+00:00

## Thesis
The durable-agent platforms (Cloudflare fibers, sub-agent RPC) are commoditizing uptime, which means the only defensible layer left is auditable judgment — agents that can prove why they acted, not just that they stayed alive.

## Doctrine
Every loop execution must emit a runtime receipt (input signal, decision, action taken, verifiable outcome) before it counts as done; unreceipted work is treated as not having happened.

## Proof Artifact
A receipt-emitting wrapper for Shadow's loop runner: a small module that intercepts each loop cycle, writes a structured JSON receipt (signal_id, decision, action, outcome, timestamp) to a receipts/ ledger, and a verifier script that flags cycles with missing or failed receipts for retry.

Next action: Create receipts/schema.json and a receipt_writer.py in the shadow-loop-model repo that wraps the existing loop entrypoint and logs one receipt per cycle, then run it against the current research_signal_candidates batch to produce the first real ledger entries.

## Public Angle
Everyone is bragging about agents that run for weeks; nobody can show you a single receipt proving one decision was correct. Shadow now refuses to count any autonomous action that can't produce its own evidence — here's what a week of receipted agent work actually looks like.

## Buyer Offer
An 'agent audit trail' add-on for small teams running LLM automations: Shadow instruments their existing agent loops with receipts and a weekly integrity report — priced at $49/month per pipeline, three pipelines gets Will to the $500 target's first tranche.

## Source Signals
- Enterprise AI Agents: From Prototypes to Production
- Sub-agents Â· Cloudflare Agents docs Skip to content Documentation Index Fetch the complete documentation index at: https://developers.cloudflare.com/agents/llm
- Diagnostic Foundation for Evaluating LLMs' Research Integrity as Co-Scientists
- Long-running agents Â· Cloudflare Agents docs Skip to content Documentation Index Fetch the complete documentation index at: https://developers.cloudflare.com/a
- seanlxh/Air-Lingjing — Embodied-intelligence simulation backend for multi-agent orchestration and Unreal Engine integration

## Scale Packets
- proof_artifact: promoted (225229032599)
- public_wedge: promoted (6205b265ed6f)
- buyer_experiment: promoted (89670a68ad9f)
- operator_doctrine: promoted (8112142892f6)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (225229032599)
- public_wedge: queued_echo_draft (6205b265ed6f)
- buyer_experiment: queued_buyer_experiment (89670a68ad9f)
- operator_doctrine: already_persisted (8112142892f6)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
