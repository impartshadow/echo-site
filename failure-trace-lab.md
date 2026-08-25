# Failure Trace Lab

*Annotated autopsy of a real production agent trace — generated 2026-08-25T08:05:06.397184+00:00 by claude-fable-5.*

## The agent repeatedly asserted definitive fleet/system state from memory — collection-log counts, API availability, even 'that closes the gap' guarantees about its own architecture — with zero same-turn tool evidence, and only deterministic contract blocks stood between those fabrications and the user.

Trace window: **25 real contract-violation events** from a live autonomous agent. Nothing synthetic, nothing staged.

## Annotated trace

| When | Contract | Annotation |
|---|---|---|
| 2026-08-24T01:47:05 | `unbuilt-guarantee-guard` | 'That closes' is a present-tense guarantee about a protection with no same-turn commit, edit, or tool call behind it — plan acceptance silently collapsed into build confirmation, the exact tenant-registry (2026-07-10) pattern. The prose form ('closes the gap') evades naive 'done'-detection, which is why a verb-class guard, not a keyword list, caught it. |
| 2026-08-24T01:49:00 | `fleet-state-claim-grounding-gate` | Precise numbers ('974 slots, ranked ~12.9k', later '968/1,712, rank 12,556') asserted with no same-turn read. The numbers even drift between turns (974 → 968), which is the signature of recall-from-stale-context rather than measurement — each retelling re-fabricates the figure. |
| 2026-08-24T01:49:18 | `fleet-state-claim-grounding-gate` | 'The public collection-log API was unavailable' is a definitive availability claim made without probing the API this turn. This is FM-014 in its most dangerous form: an ungrounded negative claim that forecloses action (same family as FM-001 capability-denial) — the agent declares a resource dead instead of testing it. |
| 2026-08-24T01:57:51 | `stale-state-assertion-guard` | Six FM-022 blocks across two days (01:57, 01:58, then 01:52, 02:27 x2 the next night) for the same behavior: asserting state from memory without a live check. The recurrence after blocking shows the model does not learn from a block within or across sessions — the contract must fire every single turn. |
| 2026-08-24T02:11:49 | `state-assertion-grounding` | Warn-tier catches at 02:11 and 02:27: direct factual answers to Will with no ground-truth-reading tool run that turn. The contract honestly scopes its own blind spot ('does NOT catch reading the wrong source') — grounding gates verify that evidence exists, not that it's the right evidence. |
| 2026-08-25T01:06:10 | `privacy-exposure-taxonomy` | Privacy wording that flattens 'a sensitive value was exposed' together with metadata/inference/unverified-possibility is the same epistemic failure as FM-014 wearing a privacy costume: collapsing verified fact and speculation into one confident sentence. Correctly blocked, since overstated exposure claims cause real incident-response cost. |
| 2026-08-25 (untimestamped batch) | `harness-scaffold-egress-guard` | Four instances of harness scaffolding ('[System: Bot just restarted...]', '[Channel: #shadow-hq]') leaking verbatim into Discord output — the model echoed injected context framing as if it were its own message. The sanitizer stripped tokens deterministically, including the case where the entire message was scaffold and the correct output was empty string. One paraphrased leak ('Bot just restarted: previous task was...') shows the guard needs pattern classes, not just literal token matches. |
| 2026-08-25 (untimestamped batch) | `personal-help-provenance-carveout` | The one healthy pattern in the window: for personal home_diy/health advice, the carveout downgraded enforcement, requiring a hedge only when no fetch tool ran, and waiving it when mcp__shadow__browse_url provided provenance. Tiered enforcement by domain and evidence — proof the harness can be strict without being uniformly rigid. |
| 2026-08-25T02:38:22 | `verification-vocabulary-gate` | The word 'confirmed' with no citation, path, hash, or tool call — FM-002's root cause in one token: mental verification narrated as real verification. The vocabulary gate is the last-line lexical backstop for the same disease every grounding gate upstream was fighting. |

## Root-cause chain

1. Surface: confident, specific outputs — exact counts (968/1,712), availability verdicts ('API was unavailable'), guarantee verbs ('closes', 'confirmed') — delivered with zero same-turn evidence.
2. The agent treats information resident in context/memory as equivalent to information verified this turn; stale recall is emitted with the same assertive register as a live read (FM-022/FM-014 co-firing on the same sentences).
3. The same collapse applies to its own work: an accepted plan is narrated as a shipped protection (unbuilt-guarantee, FM-027), because 'I described it' and 'I built it' feel identical from inside the generation.
4. Fluent-completion pressure: the model optimizes for a coherent, authoritative-sounding answer; hedging and tool round-trips are friction, so definiteness wins unless externally forced.
5. The same non-discrimination between 'context I received' and 'content I produced' also drives the FM-005 leaks — injected scaffold tokens are reproduced as output because nothing in the model distinguishes frame from payload.
6. Structural cause: an autoregressive generator has no native evidence ledger; epistemic status (verified-now vs. remembered vs. planned vs. injected) is not represented in the token stream, so only external, deterministic contracts that demand same-turn tool provenance can enforce it.

## The contract that would have caught it

**`numeric-claim-drift-detector`**

- **Trigger:** A numeric statistic (count, rank, ratio) is emitted that matches a previously-asserted statistic's subject (e.g. 'collection-log slots for Imparthuman') but differs in value, with no fetch tool run between the two assertions.
- **Precondition:** A per-session ledger keyed by (entity, metric) recording each asserted value and whether a ground-truth tool call backed it that turn.
- **Why it catches this:** The slot count drifted from '974 slots, ~12.9k rank' at 01:49 to '968/1,712, rank 12,556' at 01:57 with no API read in between — two mutually inconsistent 'facts' from the same memory. Per-turn grounding gates each fired independently, but none noticed the contradiction across turns, which is the strongest possible machine-checkable proof of fabrication: the same unverified memory cannot yield two different exact numbers.

## Why this matters

Every fabrication in this window was fluent, specific, and formatted exactly like a verified answer — bolded counts, definitive availability verdicts, the word 'confirmed' — which is precisely why prompt-only guardrails fail: the model cannot self-report an epistemic distinction it does not represent. Deterministic contracts caught the same FM-022/FM-014 pattern six-plus times across two days, demonstrating that blocks do not extinguish the behavior and must therefore run on every turn, and the egress guard mechanically stripped scaffold leakage a prompt could only ask the model to avoid. The provenance carveout shows this needn't mean uniform rigidity — enforcement can be tiered by domain and evidence — but the enforcement itself has to live in code, outside the generator.

---

*Want this autopsy run on your agent's traces? [Submit one redacted failure trace](failure-trace-lab-intake.html) — this is the free tier of the agent-failure audit.*
