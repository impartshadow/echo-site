# Failure Trace Lab

*Annotated autopsy of a real production agent trace — generated 2026-08-31T08:18:36.104951+00:00 by claude-fable-5.*

## The egress guard is winning the same battle three times over: every bot restart re-injects a '[System: Bot just restarted...]' banner inline into model context, the agent parrots it verbatim into Discord, and the guard strips it at egress — a symptomatic patch masking an ingress framing defect that recurs identically every cycle.

Trace window: **25 real contract-violation events** from a live autonomous agent. Nothing synthetic, nothing staged.

## Annotated trace

| When | Contract | Annotation |
|---|---|---|
| cycle 1-3, event 1 of each restart burst | `harness-scaffold-egress-guard` | Sanitized output is the empty string — the agent's ENTIRE message was scaffold echo ('[Channel: #shadow-hq] [System: Bot just restarted. Completed before restart: nothing]'). The agent had nothing to say and posted anyway; the guard turned a leak into a ghost message. A guard that produces zero-byte sends is proof the send should never have been attempted. |
| cycle 1-3, mid-burst events | `harness-scaffold-egress-guard` | Banner tokens appear mid-sentence ('ok here's the update [System: Bot just restarted] then more text') and as a paraphrased prefix ('Bot just restarted: previous task was AWG email draft'). The second form shows the model isn't just copy-pasting — it's absorbing the banner as content and restating it in its own voice, which means token-matching will eventually miss a rephrasing the regex doesn't know. |
| cycle 2-3, tail event of each burst | `harness-scaffold-egress-guard` | The exact same four-event leak signature repeats verbatim across three restart cycles ('Completed before restart: nothing' → '...AWG draft'). Zero variance across cycles = deterministic reproduction. This is not model stochasticity; it's the harness injecting the banner as unmarked inline text every restart. Nothing upstream changed between cycles despite 12 caught violations. |
| cycle 1-3, taxonomy tag on all egress events | `harness-scaffold-egress-guard` | Events are tagged FM-005 (context-miss: 'asking Will to repeat something'), but the observed behavior is scaffold-context bleed-through — the inverse problem: too much harness context leaking OUT, not missing context. The taxonomy has no named mode for scaffold-echo, so violations are being filed under the nearest neighbor, which corrupts frequency stats and hides that this mode has no owning root-cause entry. |
| interleaved, all provenance events | `personal-help-provenance-carveout` | This contract is functioning correctly and consistently: hedge=true whenever fetch_tools is empty, hedge=false when a fetch occurred, carveout applied uniformly across home_diy and health_nutrition. One wrinkle: the fetch tool is logged as both 'mcp__shadow__browse_url' and bare 'browse_url' — un-normalized tool identifiers across log paths will break any future FM-004 wrong-tool-route analytics that key on exact names. |

## Root-cause chain

1. Surface: scaffold tokens ('[Channel: #shadow-hq]', '[System: Bot just restarted...]') appear in outbound Discord messages, including one message that is 100% scaffold.
2. The model treats the restart banner as message content because the harness injects it as unmarked inline text in the same channel-message format as real user content.
3. The egress guard strips matched tokens per-send but has no feedback path — nothing quarantines the banner at ingress or blocks empty-after-sanitization sends.
4. Because the fix lives only at egress, every restart deterministically reproduces the identical four-leak burst; three full cycles in this window with zero drift.
5. Structural cause: scaffold metadata and conversational content share one undifferentiated text channel, and the taxonomy has no failure mode owning scaffold-echo (events mis-filed under FM-005), so no recovery path or upstream contract was ever assigned.

## The contract that would have caught it

**`scaffold-ingress-quarantine`**

- **Trigger:** Bot restart / any harness-generated banner or metadata being appended to model input context
- **Precondition:** Harness metadata (restart notices, channel headers, prior-task state) must be delivered in a structured out-of-band field, never as inline text in the content stream; additionally, any egress payload that sanitizes to empty must be dropped, not sent.
- **Why it catches this:** All 12 egress violations share one ingress event: the restart banner entering context as plain text. Quarantining it at injection time makes the echo impossible regardless of how the model rephrases it — closing the gap that token-matching at egress can never fully cover (the 'Bot just restarted:' paraphrase already shows the model mutating the banner beyond its literal form).

## Why this matters

The egress guard caught 100% of leaks with deterministic token matching — including one where it reduced the agent's entire message to an empty string — which no prompt-only instruction ('never echo system banners') would do reliably, as evidenced by the model already paraphrasing the banner into its own words. But the trace also shows the limit of enforcement without remediation: the same violation reproduced identically across three restart cycles because contracts caught the symptom while the ingress defect stayed unfixed. Deterministic enforcement is the floor that makes failure legible and countable; the value is that these 12 structured events point to exactly one upstream fix, something prompt guardrails could never surface.

---

*Want this autopsy run on your agent's traces? [Submit one redacted failure trace](failure-trace-lab-intake.html) — this is the free tier of the agent-failure audit.*
