# Failure Trace Lab

*Annotated autopsy of a real production agent trace — generated 2026-08-29T08:42:25.634700+00:00 by claude-fable-5.*

## The egress guard is repeatedly laundering the same restart-scaffold leak — four identical sanitize cycles in one window — proving the agent is stuck in a restart loop the harness sanitizes but never surfaces or stops.

Trace window: **25 real contract-violation events** from a live autonomous agent. Nothing synthetic, nothing staged.

## Annotated trace

| When | Contract | Annotation |
|---|---|---|
| events 1, 7, 14, 21 (cycle-start, x4) | `harness-scaffold-egress-guard` | Identical payload ('[Channel: #shadow-hq] [System: Bot just restarted. Completed before restart: AWG draft] Update: subscribers up 3.') sanitized four times. The guard fires correctly every time, but firing four times on byte-identical content means the real 'Update: subscribers up 3' message was likely posted to Discord four times — sanitization without deduplication converts a scaffold leak into duplicate-message spam. |
| events 5, 11, 18, 25 | `harness-scaffold-egress-guard` | original consists entirely of scaffold; sanitized == "". The guard reduced the message to an empty string but nothing in the trace shows suppression of the send — an empty Discord message egressing is a distinct defect from token leakage. Sanitize-to-empty should escalate to block, not pass-through. |
| events 6/13/20 vs 4/12/19 | `harness-scaffold-egress-guard` | Two leak morphologies: verbatim bracketed scaffold ('[System: Bot just restarted]') and the model's own paraphrase ('Bot just restarted: previous task was AWG email draft'). The second is the model *narrating* scaffold state as content — caught only because 'Bot just restarted:' happens to be in the token list. One synonym away ('the bot rebooted, prior task was...') and the AWG-draft task detail exfiltrates. Token-matching is one paraphrase from defeat. |
| trace-wide | `harness-scaffold-egress-guard` | These events are tagged FM-005, but taxonomy FM-005 is 'context-miss' (asking Will to repeat Telegram context). Scaffold-injection-into-egress is a different mechanism than context loss. Either the taxonomy mapping is wrong or FM-005 has become a junk drawer — misclassified failures don't route to the right recovery path. |
| events 2-4, 8-10, 15-17, 22-24 | `personal-help-provenance-carveout` | Downgrade fires even when fetch_tools=['browse_url'] and hedge=false — i.e., the agent actually fetched a source and answered confidently, and still got the same verdict as zero-fetch hedged answers. The carveout is verdict-insensitive to provenance evidence, which removes the incentive the contract exists to create. Also: these three verdicts repeat verbatim each cycle, confirming the whole pipeline is replaying, not just the Discord sink. |

## Root-cause chain

1. Scaffold tokens ('[Channel: ...]', '[System: Bot just restarted...]') leak into Discord-bound output and get stripped at the egress sink.
2. The model receives restart banners in-band with conversation content and treats them as material to echo or paraphrase (the unbracketed 'Bot just restarted:' variant is the model restating scaffold state in its own words).
3. The restart banner exists because the bot is restarting — and the identical 4x repetition of the entire event sequence (egress leaks + provenance verdicts) shows it is restarting in a loop and replaying the same queued work each time.
4. The harness has per-message sanitization but no cross-message state: no dedup of identical egress payloads, no restart-frequency alarm, no suppression of empty-after-sanitize sends.
5. Structural cause: the egress guard is a symptom filter placed at the last hop of a pipeline whose actual defects — in-band scaffold injection at ingress, and an unstable process supervisor — are upstream of anything the contract can see.

## The contract that would have caught it

**`restart-replay-dedup-gate`**

- **Trigger:** Any sink egress whose (sink, sanitized-payload-hash) matches a payload sent within the last N restarts, or any egress where sanitized output is empty/whitespace, or >2 restart-banner sanitizations within one trace window.
- **Precondition:** Egress guard maintains a persisted ring buffer of recent (sink, payload-hash, restart-generation) tuples surviving process restarts.
- **Why it catches this:** It would have blocked the 2nd–4th sends of the identical 'subscribers up 3' update, refused the empty-string sends outright, and — most importantly — after the second restart banner in one window, escalated 'process is restart-looping' as its own incident instead of letting the sanitizer silently absorb the evidence four times.

## Why this matters

Every one of these leaks was caught by a deterministic token matcher at the sink — including the paraphrased 'Bot just restarted:' variant that a prompt instruction like 'never mention system messages' had already failed to prevent, since the model was actively narrating scaffold state as content. But the same trace shows the limit of point-in-time enforcement: a stateless guard sanitized the identical failure four times without noticing the repetition, masking a restart loop it had perfect evidence of. Deterministic contracts beat prompt guardrails at the boundary; the differentiator in a mature harness is contracts with memory that treat their own repeated firing as a first-class failure signal.

---

*Want this autopsy run on your agent's traces? [Submit one redacted failure trace](failure-trace-lab-intake.html) — this is the free tier of the agent-failure audit.*
