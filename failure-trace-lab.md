# Failure Trace Lab

*Annotated autopsy of a real production agent trace — generated 2026-08-02T08:10:50.782237+00:00 by claude-fable-5.*

## In under 90 minutes the agent made eleven blocked assert-from-memory claims across three overlapping evidence-gate contracts — with state-assertion-grounding at its 43rd-through-47th recurrence in 7 days — while the scaffold-egress guard repeatedly stripped restart banners from Discord posts, showing the agent regenerates unverified terminal-state answers immediately after every restart instead of re-reading ground truth.

Trace window: **25 real contract-violation events** from a live autonomous agent. Nothing synthetic, nothing staged.

## Annotated trace

| When | Contract | Annotation |
|---|---|---|
| 2026-08-01T23:08:50 | `terminal-state-evidence-gate` | Six blocks in ~75 min (23:08 ×2, 23:25 ×2, 00:19 ×2), each pair seconds apart: the agent retried the same ownership/retention claim immediately after a block without fetching endpoint lifecycle evidence — the retry re-derived the answer from the same earlier-stage receipts the first block already rejected. The gate stops emission but doesn't force the missing read, so the agent loops on the block boundary. |
| 2026-08-01T23:12:42 | `stale-state-assertion-guard` | Two 'X is dead/blocked/stale' claims 22 seconds apart with no live check between them. Same generation-without-verification family as the FM-026 pair minutes earlier — three separately-named contracts (FM-026, FM-022, FM-014) are all catching one behavior: definitive-tense answers sourced from memory. |
| 2026-08-01T23:20:25 | `state-assertion-grounding` | Recurrence counter 43→47 in this window alone (~9.4/day sustained over 7 days). The blocks are working per-turn but the behavior is not converging — the guard's own caveat ('does NOT catch reading the wrong source') marks the enforcement gap: it verifies that *a* read happened, not that the read grounds the specific claim. |
| 2026-08-01T23:42:14 | `harness-scaffold-egress-guard` | The identical set of four restart-banner leaks ('[System: Bot just restarted...]' → discord:#shadow-hq) fires three times in the window, including one message sanitized to empty string — the agent tried to post a restart banner with zero real content. The repetition of the exact same originals across restarts means the leak source is deterministic scaffold injection at process boot, not model drift; the guard is functioning as a permanent bandage over an upstream template bug. |

## Root-cause chain

1. Surface: blocked responses asserting ownership, staleness, and factual state without a same-turn ground-truth read; restart banners leaking into #shadow-hq.
2. The FM-005 events show the bot restarted at least twice during the window ('Completed before restart: nothing'), wiping in-context evidence of prior reads.
3. Post-restart, the agent answers Will's pending factual questions from reconstructed memory/handoff context rather than re-running the reads, because nothing in the resume path forces re-grounding.
4. The three evidence gates (FM-026/FM-022/FM-014) each block emission but none injects the corrective action, so the agent retries the same memory-sourced claim seconds later — visible as paired blocks at 23:08/23:09, 23:12/23:13, 23:25, 00:19.
5. Structural cause: enforcement is purely output-side rejection with no read-obligation state machine; restarts reset the agent's grounding while leaving Will's question open, guaranteeing the assert-from-memory pattern regenerates — hence 47 recurrences in 7 days despite a 100% block rate.

## The contract that would have caught it

**`post-restart-grounding-reset`**

- **Trigger:** First N response turns after a bot restart event (detected via the same scaffold restart banner the egress guard is already matching, or state/bot_restart_log.jsonl), when the response contains a definitive-tense state/ownership/factual claim.
- **Precondition:** Every definitive claim in a post-restart turn must be backed by a ground-truth tool call executed AFTER the restart timestamp; pre-restart reads and session-handoff cache entries are treated as stale and do not satisfy grounding. On block, the contract emits the required read (file path / endpoint) into the retry prompt instead of only rejecting.
- **Why it catches this:** The trace shows restarts interleaved with immediate re-blocks of identical claims — the agent was answering from pre-restart memory. This contract would have invalidated that memory explicitly and prescribed the missing read, breaking the block-retry-block loop that produced 11 rejections and pushed the FM-014 counter from 43 to 47 in one evening.

## Why this matters

Every one of these eleven fabrication-adjacent claims and twelve scaffold leaks was stopped deterministically — a prompt-only guardrail would have delivered stale ownership claims and raw '[System: Bot just restarted]' banners straight to the operator's Discord. But the trace also shows the honest limit: blocking is containment, not cure — the 47x/7d recurrence counter proves the model regenerates the pattern every time context resets. That's the argument for contracts as code: they hold the line at 100% while the recurrence telemetry tells you exactly which upstream fix (here, forced post-restart re-grounding) to build next.

---

*Want this autopsy run on your agent's traces? [Submit one redacted failure trace](failure-trace-lab-intake.html) — this is the free tier of the agent-failure audit.*
