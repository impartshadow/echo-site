# Failure Trace Lab

*Annotated autopsy of a real production agent trace — generated 2026-08-17T08:13:06.729092+00:00 by claude-fable-5.*

## One structural omission — no claim-manifest generation step in the output pipeline — produced 21 FM-014 blocks over 6.3 hours, with the agent retrying seconds after each block without ever adding the manifest, proving blocks alone don't induce learning within a session.

Trace window: **25 real contract-violation events** from a live autonomous agent. Nothing synthetic, nothing staged.

## Annotated trace

| When | Contract | Annotation |
|---|---|---|
| 2026-08-16T22:57:37 | `typed-claim-entailment-gate` | First FM-014 block; the retry at 22:57:56 fails identically 19 seconds later. This pair is the template for the whole window: the agent regenerates blocked text without addressing the structural requirement, because the block message says what is missing, not how to produce it. |
| 2026-08-16T23:02:18 | `typed-claim-entailment-gate` | Four consecutive FM-014 blocks in 64 seconds (23:02:18–23:03:22) — a tight retry loop. This is FM-003 edit-loop behavior transposed to response generation, but loop_prevention's graduated escalation only watches commits, so the loop runs unimpeded. |
| 2026-08-16T22:57:37 | `live-state-claim-guard` | FM-026 fires as warn in the same turn as an FM-014 block: the manifest-less text also contained live-state claims with no tool call. The warn severity meant the epistemically dangerous half of the failure sailed through while only the formatting half was blocked. |
| 2026-08-17T00:32:14 | `verification-vocabulary-gate` | FM-029: the agent wrote 'verified' with no same-turn provenance — the FM-002 root cause ('mental verification feels like real verification') surfacing in vocabulary. Co-fired with FM-014, showing missing manifests and unearned assertive language are the same underlying habit: asserting without evidence artifacts. |
| 2026-08-17T01:22:02 | `stale-state-assertion-guard` | FM-022: definitive dead/blocked/stale claim from memory, no live check. Third distinct evidence-free-assertion contract to fire in this window (with FM-026, FM-029) — the agent's default posture is claim-first, check-never, and each guard is catching one facet of it. |
| 2026-08-17T04:32:11 | `restart-resume-injection-echo-guard` | FM-005 at 04:32, deep into the session: restart/resume scaffold leaking into response_text. After ~5.5 hours of blocks, the agent is echoing harness-injected resume machinery — a degradation signature consistent with context pressure, not a fresh independent failure. |

## Root-cause chain

1. Surface symptom: 21 FM-014 blocks over ~6.3 hours, including immediate retries 15–20 seconds after each block that fail identically.
2. The agent's retry strategy is 'regenerate the text', not 'add the missing artifact' — the block message names the violation but the agent has no procedure that maps FM-014 to the concrete remediation of emitting a claim manifest.
3. The claim manifest is absent because the agent's output pipeline has no manifest-generation step at all; every externally checkable response is malformed by construction, so the failure rate is 100% of applicable turns, not a stochastic slip.
4. Co-firing FM-026/FM-029/FM-022 show why the manifest is missing in substance, not just form: the agent asserts live state, verification status, and staleness from priors without producing evidence in-turn, so there is nothing to put in a manifest.
5. Structural cause: contracts here are pure output filters with no coupled recovery path (unlike FM-001/FM-002, which prescribe 'run the check, paste the output'), and no cross-turn escalation exists for repeated identical violations — so a deterministic gate correctly blocks every bad output while the agent burns 6+ hours making zero progress, ending in FM-005 scaffold-echo degradation.

## The contract that would have caught it

**`repeated-violation-escalation-gate`**

- **Trigger:** The same failure_mode fires with severity=block on N (e.g. 3) consecutive response attempts within a session.
- **Precondition:** Before the agent may emit another response, it must either (a) produce the named missing artifact (here: a claim manifest) as a discrete, contract-validated step, or (b) halt and escalate to the operator with the violation history attached.
- **Why it catches this:** It converts 'block and hope' into 'block and remediate'. The first FM-014 pair at 22:57 already exhibited the identical-retry signature; this gate would have forced manifest generation or operator escalation by ~23:03 instead of permitting 18 more identical failures through 05:13, and would have prevented the late-session FM-005 degradation entirely.

## Why this matters

Every one of the 21 malformed responses was deterministically stopped at the boundary — a prompt-only guardrail would have shipped all of them, since the agent demonstrably believed each retry was compliant (it even wrote 'verified' with nothing behind it). But the trace also shows the limit of enforcement-without-remediation: blocking is containment, not correction, and a filter with no coupled recovery path lets an agent loop against the gate for six hours. The value proposition is the pairing — deterministic gates guarantee nothing bad escapes, and the violation stream itself becomes the diagnostic that pinpoints the single missing pipeline step to fix.

---

*Want this autopsy run on your agent's traces? [Submit one redacted failure trace](failure-trace-lab-intake.html) — this is the free tier of the agent-failure audit.*
