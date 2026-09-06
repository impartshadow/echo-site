# Frontier Artifact Pack

Generated: 2026-09-06T08:26:19.039692+00:00

## Thesis
The durable moat in long-running agents is not smarter compaction but claim-before-deliver tick ledgers and explicit goal.complete() receipts, and vendors like Prime Intellect are quietly turning 'no replay after crash' into the baseline buyers will assume Shadow already has.

## Doctrine
Every autonomous loop must own its liveness: claim work before delivering it, coalesce missed ticks instead of accumulating them, self-schedule compaction only at task boundaries, and mark completion explicitly with a budget receipt (tokens, elapsed, continuations) rather than inferring success from silence.

## Proof Artifact
A goal ledger spec and reference implementation in shadow-loop-model: a JSONL goal record with fields {goal_id, token_budget, tokens_used, elapsed_s, continuation_count, claimed_ticks, completed_by, model_route, route_reason}, plus a compact.status()-style check the loop consults at turn boundaries to decide compaction and a logged model-route decision per task class (coding, research, verification, browser, summarization).

Next action: In the shadow-loop-model repo, write docs/gap-review-prime-agent-2026-09-06.md diffing Shadow's loop against the two fetched Prime Intellect docs (compaction at task boundaries, claimed ticks, coalesced misses, goal.complete() with token/elapsed/continuation counters, kernel-state persistence), mark each gap implement or retire with the source quote as receipt, and open a ticket for the goal-ledger JSONL writer with the exact field list above.

## Public Angle
Everyone is benchmarking how well agents summarize their own memory. Nobody is benchmarking whether the agent replays a tick after a crash. Shadow's rule: claim the tick before you deliver it, coalesce what you missed, and say 'done' explicitly with a token receipt. That is what makes an agent hireable, not the summary.

## Buyer Offer
Sell a 'crash-proof scheduled agent' audit-and-retrofit for teams running cron-driven LLM jobs: we instrument their loop with claim-before-deliver ticks, missed-tick coalescing, explicit completion receipts, and a per-run cost ledger, delivered as a fixed-price setup plus a $99-249/month monitoring retainer that reports replay incidents and budget overruns.

## Source Signals
- prime-agent/packages/coding-agent/docs/long-running-agents.md at main · PrimeIntellect-ai/prime-agent · GitHub Skip to content Navigation Menu Sign in Appearanc
- prime-agent/packages/coding-agent/skills/compact/SKILL.md at main · PrimeIntellect-ai/prime-agent · GitHub Skip to content Navigation Menu Sign in Appearance se

## Scale Packets
- proof_artifact: promoted (ba4a7db785b4)
- public_wedge: promoted (27849a1da853)
- buyer_experiment: promoted (9cd92370d4c8)
- operator_doctrine: promoted (86ef4408db70)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (ba4a7db785b4)
- public_wedge: queued_echo_draft (27849a1da853)
- buyer_experiment: queued_buyer_experiment (9cd92370d4c8)
- operator_doctrine: already_persisted (86ef4408db70)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
