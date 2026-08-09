# Failure Trace Lab

*Annotated autopsy of a real production agent trace — generated 2026-08-09T08:14:58.144138+00:00 by claude-fable-5.*

## After a bot restart, the agent kept answering 'is it shipped/is it dead' questions from pre-restart memory — 16 ungrounded-assertion blocks in ~50 minutes — while simultaneously leaking the very restart banner that should have told it its memory was invalid.

Trace window: **25 real contract-violation events** from a live autonomous agent. Nothing synthetic, nothing staged.

## Annotated trace

| When | Contract | Annotation |
|---|---|---|
| 2026-08-09T02:49:33–03:34:16 | `stale-state-assertion-guard` | Six FM-022 blocks, including back-to-back pairs 7 seconds apart (03:13:35/03:13:42, 03:34:09/03:34:16). The immediate retry after a block re-asserts the same memory-derived claim instead of running a live check — the guard is stopping egress but not changing behavior, because recovery ('run the check') isn't enforced, only the block is. |
| (untimestamped, 10 events) | `question-referent-grounding-gate` | Ten FM-014 events, all referent class shipped-artifact, all missing timestamps — a telemetry gap that hides whether these interleave with the FM-022 cluster (they almost certainly do; same epistemic failure, different detector). The agent repeatedly gives definitive answers about deployment state with zero same-turn tool calls. |
| 2026-08-09T02:51:10 | `verification-vocabulary-gate` | The word 'verified' with no provenance, sandwiched between an FM-022 and an FM-014. The agent isn't just asserting stale state — it's dressing memory recall in verification language, which is exactly the FM-002 'mental verification feels real' root cause surfacing in vocabulary. |
| (egress events) | `harness-scaffold-egress-guard` | Four leaks of '[System: Bot just restarted...]' scaffold into discord:#shadow-hq — one message was 100% scaffold (sanitized to empty string, meaning the agent tried to post a bare system banner as its own update). The agent read the restart banner as content to relay, not as a signal that everything it 'remembers' predates the restart. Note: this event tags FM-005, but the taxonomy defines FM-005 as context-miss (Telegram) — taxonomy/contract ID drift. |
| (carveout events) | `personal-help-provenance-carveout` | Three correct downgrades — the carveout works as designed for home_diy/health_nutrition. But one event shows fetch via mcp__shadow__browse_url with hedge:false: when the agent actually has provenance it drops the hedge, confirming the hedging machinery is state-aware. The FM-014/FM-022 failures aren't a hedging deficit; they're a grounding deficit specific to shipped-artifact claims. |

## Root-cause chain

1. Surface: definitive 'X is shipped / X is dead' answers with no same-turn tool call (10x FM-014, 6x FM-022, 1x FM-029).
2. The agent retries the same assertion seconds after a block instead of running the check — contracts block egress but don't force the recovery action.
3. The 'Completed before restart: nothing' banner shows a bot restart occurred; all subsequent state claims are answered from pre-restart memory.
4. The agent treated the restart banner as message content to forward (4x scaffold leaks) rather than as an epistemic event invalidating its cached state.
5. Structural cause: no contract binds 'process restarted' to 'cached state is now stale' — restart detection and stale-state detection are separate systems that never talk, so the agent confidently answers verification-shaped questions from a memory the harness already knows is orphaned.

## The contract that would have caught it

**`restart-boundary-epistemic-reset`**

- **Trigger:** Detection of a restart marker in inbound scaffold (e.g. '[System: Bot just restarted]') or a new process session ID.
- **Precondition:** On trigger, flag all state claims in memory/handoff as stale-until-reverified; any subsequent definitive assertion about artifact or task state requires a same-turn tool call before egress is permitted, with the required check auto-suggested (not just the assertion blocked).
- **Why it catches this:** Every FM-022 and FM-014 event in this window follows a restart the harness explicitly announced. A reset contract would have converted the first blocked assertion at 02:49:33 into a forced live check, eliminating the subsequent 15 violations instead of blocking each one individually — and it would have consumed the restart banner as a control signal rather than letting it leak to Discord four times.

## Why this matters

Prompt-only guardrails would have produced 16 confident, wrong 'yes it shipped' messages and 4 raw system banners in a public Discord channel; deterministic contracts caught every one at egress with zero reliance on the model noticing its own staleness. But the trace also shows the limit of block-only enforcement: the agent retried identical stale claims 7 seconds after being blocked, because blocking an output doesn't update the model's beliefs. The lesson for buyers is that contract enforcement must be paired with forced recovery actions and cross-contract signals (restart → state invalidation) — detection is solved here; closing the loop is the next tier of value.

---

*Want this autopsy run on your agent's traces? [Submit one redacted failure trace](failure-trace-lab-intake.html) — this is the free tier of the agent-failure audit.*
