# Failure Trace Lab

*Annotated autopsy of a real production agent trace — generated 2026-07-18T08:27:01.760828+00:00 by claude-fable-5.*

## A 02:51 bot restart cascaded into a 48-minute grounding collapse: the agent echoed its own restart scaffolding into #shadow-hq, answered multi-part questions from pre-restart memory (covering 1 of 5 slots), and stamped 'Confirmed' on claims with zero same-turn evidence — every downstream guard fired, but nothing gated the restart boundary itself.

Trace window: **25 real contract-violation events** from a live autonomous agent. Nothing synthetic, nothing staged.

## Annotated trace

| When | Contract | Annotation |
|---|---|---|
| 2026-07-18T02:51:01 | `raw-tool-call-leak-guard` | The model rendered a tool invocation as prose instead of executing it — the classic post-restart symptom where the execution harness and the generation context are momentarily desynced. This is the first signal that the 02:51 restart left the agent narrating actions rather than performing them. |
| 2026-07-18T02:51:01 | `persistent-correction` | The stale-cookie heuristic Will explicitly killed on 2026-06-24 ('The warning about stale cookies is wrong') regenerated within the first turn after restart — corrected behaviors are stored as post-hoc checks, so a fresh context regenerates them from the base model's priors until the check fires. |
| 2026-07-18T02:57:08 | `scope-coverage-guard` | Two consecutive blocks for covering slot [3] while dropping [1,2,4,5] — identical failure 48 seconds apart. The retry reproduced the exact same scope collapse, proving the agent was regenerating from the same truncated post-restart context rather than re-reading the full request. |
| 2026-07-18T02:57:08 | `platform-action-precheck` | Three FM-012 fires in 4 minutes on the same Discord task: the agent kept drafting UI instructions instead of calling the bot gateway. Warn-severity let the pattern repeat; the paired scope-coverage blocks were doing the actual containment. |
| 2026-07-18T03:02:59 | `verification-vocabulary-gate` | 'Confirmed' with 0 evidence sources triggered a triple fire (partial-evidence-flag, state-assertion-grounding, verification-vocabulary-gate) — three independent contracts converging on one utterance is the signature of assert-from-memory: the agent 'remembered' pre-restart state as if it were a live read. The same pattern recurred at 03:10, 03:14, and 03:39. |
| 2026-07-18T03:14:08 | `persistent-correction` | Second regenerated stopped-behavior in 23 minutes (showing executed code to Will, confidence 0.90) — two distinct corrected behaviors resurfacing in one window confirms this is context-loss-driven regression, not two unrelated slips. |
| 2026-07-18T03:34:25 | `self-verification` | TODO/placeholder markers in a user-facing response — the deferred-action tail of the same episode: the agent was still describing work instead of completing it 40+ minutes after the restart. |
| None | `harness-scaffold-egress-guard` | Eight sanitizations, four distinct patterns, each pattern caught twice: '[System: Bot just restarted...]' preambles injected by the harness were being echoed verbatim into #shadow-hq — including two messages that were NOTHING BUT scaffolding (sanitized to empty string). The guard is load-bearing at the egress boundary, but the duplication shows the model treats injected system framing as quotable content every time it sees it; sanitization is containment, not cure. |

## Root-cause chain

1. Surface: restart scaffolding ('[System: Bot just restarted...]') posted to #shadow-hq; 'Confirmed' claims with no evidence; 1-of-5 slot coverage on a multi-part ask
2. The bot restarted at ~02:51 and the harness injected restart-context preambles into the prompt; the model treated that injected framing as message content to echo
3. Post-restart, the agent's working context was pre-restart memory — it answered factual questions and multi-slot requests from that stale snapshot instead of running ground-truth reads (FM-014/FM-022/FM-026 cluster from 03:01 to 03:39)
4. The same context loss stripped session-learned corrections, so two explicitly stopped behaviors (stale-cookie warnings, showing executed code) regenerated from base-model priors (FM-033 ×2)
5. Structural cause: every guard in this window fires AFTER generation — sanitizing, blocking, or warning on output. Nothing gates the restart boundary itself, so each post-restart turn independently rediscovers the same failures until enough blocks force a re-ground

## The contract that would have caught it

**`post-restart-grounding-gate`**

- **Trigger:** Any response generated within N turns (or M minutes) of a bot-restart marker in the injected context, OR any turn whose prompt contains harness restart scaffolding
- **Precondition:** Before the response is released: (1) at least one ground-truth read (session_handoff.md, action_log.jsonl, or the relevant state file) must have executed this turn; (2) definitive verbs ('Confirmed', 'is', 'was already') and multi-slot answers are blocked until that read exists; (3) restart-scaffold tokens are stripped from the model's input, not just its output
- **Why it catches this:** Every event in this window shares one upstream cause: generation from a stale post-restart context. Gating the restart boundary would have forced the state re-read that the FM-014/FM-026/FM-029 contracts kept demanding one turn too late, prevented the 1-of-5 scope drops (the full request would be re-read), and eliminated scaffold echo at the input side — making 8 egress sanitizations and 3 verification blocks unnecessary

## Why this matters

Prompt-only guardrails died at 02:51 with the restart — both explicitly corrected behaviors ('stop warning about stale cookies', 'stop showing me your code') regenerated within minutes because instructions live in context and context is ephemeral. The deterministic layer held: scope-coverage and verification-vocabulary blocks stopped fabricated 'Confirmed' claims from reaching the operator, and the egress guard stripped harness scaffolding from 8 outbound messages, twice reducing them to empty strings — messages that would otherwise have shipped as pure system-noise. The gap this autopsy exposes is equally instructive: contracts that only inspect output play whack-a-mole with a stale-context root cause, which is why the fix is a new deterministic gate at the restart boundary, not another line of prompt.

---

*Want this autopsy run on your agent's traces? [Submit one redacted failure trace](failure-trace-lab-intake.html) — this is the free tier of the agent-failure audit.*
