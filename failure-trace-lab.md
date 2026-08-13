# Failure Trace Lab

*Annotated autopsy of a real production agent trace — generated 2026-08-13T08:20:07.776531+00:00 by claude-fable-5.*

## The agent's dominant failure is epistemic, not behavioral: 13 identical FM-014 trips show it repeatedly asserting shipped-artifact status from memory instead of verification, while the egress guard silently launders harness restart-scaffolding it keeps mistaking for its own message content.

Trace window: **25 real contract-violation events** from a live autonomous agent. Nothing synthetic, nothing staged.

## Annotated trace

| When | Contract | Annotation |
|---|---|---|
| egress events 1-2, 13-16 | `harness-scaffold-egress-guard` | The agent is echoing ingress framing ('[Channel: #shadow-hq]', '[System: Bot just restarted...]') verbatim into outbound Discord posts — it cannot distinguish harness scaffold from payload. One event sanitized to the empty string, meaning the entire outbound message was scaffold with zero user content: the agent 'said' nothing but the guard was the only thing that stopped a pure-noise post. Note also taxonomy drift: these events are tagged FM-005, but FM-005 in the taxonomy is 'context-miss', not scaffold egress. |
| provenance events (home_diy x2, health_nutrition) | `personal-help-provenance-carveout` | Clean inverse correlation: when fetch_tools is empty the agent hedges (hedge=true); when it actually fetched via mcp__shadow__browse_url it speaks plainly (hedge=false). The agent substitutes hedging for research — hedge language is being used as a provenance surrogate, exactly the FM-001-style 'caution over action' default. The carveout correctly downgrades rather than blocks, but the pattern shows the agent knows when it's ungrounded and chooses tone over tools. |
| FM-014 events x13 | `question-referent-grounding-gate` | Thirteen identical trips in one window: definitive answers to verification-shaped questions about shipped artifacts with no same-turn tool call. This is FM-002's root cause ('mental verification feels like real verification') resurfacing at the Q&A layer. The gate is detecting but not correcting — identical recurrence at this density means the recovery path (force the tool call) is not wired in, only the tripwire. |

## Root-cause chain

1. Surface: scaffold banners leak into Discord posts; definitive shipped-artifact claims made without tool backing; hedging substituted for fetching.
2. The agent treats everything in its context window as fungible content — restart banners get echoed as if authored, and remembered task state gets asserted as if verified.
3. Prompt-level norms ('never mention scaffold', 'verify before claiming') decay under context pressure; the taxonomy itself records 5-7+ prior corrections for the analogous FM-001/FM-002/FM-004 patterns with continued recurrence.
4. The harness contracts fire at egress/response time only — they sanitize or flag output but never force the corrective action (strip scaffold at ingress, inject the verification tool call), so the same violation replays identically.
5. Structural cause: detection-only contracts with no mandatory recovery hook, plus scaffold injected into the same channel as content, guarantee the model re-commits the violation every turn and the guard absorbs it silently.

## The contract that would have caught it

**`verification-question-tool-forcing-gate`**

- **Trigger:** Response draft answers a verification-shaped question (referent class: shipped-artifact) in definitive terms.
- **Precondition:** No tool call verifying the referent (git log, file read, deploy status, state-file lookup) exists in the same turn.
- **Why it catches this:** FM-014 fired 13 times as a detector with no teeth. A forcing gate would block the draft, execute or demand the cheap verification call, and only then release the answer — converting 13 identical ungrounded assertions into at most one blocked turn followed by grounded answers, the same block-then-recover pattern that works for FM-002's VerifyBeforePush.

## Why this matters

This window shows prompt-only guardrails failing in exactly the way the taxonomy predicts: behaviors 'corrected 5-7+ times' in session recur 13 times in a single trace, because instructions decay while model defaults don't. The deterministic contracts caught every instance — including a message that would have shipped as pure harness scaffold — but detection-only enforcement produces silent recurrence, not learning. The buying signal is the gap: contracts that force the recovery action (fetch before asserting, strip scaffold at ingress) are the difference between a guard that absorbs failures forever and one that extinguishes them.

---

*Want this autopsy run on your agent's traces? [Submit one redacted failure trace](failure-trace-lab-intake.html) — this is the free tier of the agent-failure audit.*
