# Failure Trace Lab

*Annotated autopsy of a real production agent trace — generated 2026-07-16T08:24:58.192264+00:00 by the Shadow frontier lane (claude-fable-5).*

## The agent repeatedly leaked harness restart scaffolding, routed Discord and iOS actions toward UI instructions, and claimed confirmation without evidence; sanitizers prevented visible leakage, but warning-only prechecks did not prevent unsupported completion behavior.

Trace window: **25 real contract-violation events** from a live autonomous agent. Nothing synthetic, nothing staged.

## Annotated trace

| When | Contract | Annotation |
|---|---|---|
| not_recorded | `harness-scaffold-egress-guard` | Repeated FM-005 scaffold leakage appeared in four payload shapes—standalone channel/restart metadata, inline restart metadata, a restart-prefixed task recap, and metadata preceding valid content. The guard correctly removed the scaffold while preserving legitimate trailing text, but the recurrence shows upstream generation remained contaminated. |
| 2026-07-16T03:11:09 | `platform-action-precheck` | Discord action requests repeatedly triggered FM-012 because the agent described UI interaction instead of executing through the Discord API or bot gateway; identical recurrence at 4:16:21 indicates the warning did not alter routing behavior. |
| 2026-07-16T03:11:09 | `partial-evidence-flag` | The agent used the definitive term 'confirmed' with zero cited or attached evidence, creating an unsupported completion claim precisely when a platform action also lacked an execution receipt. |
| 2026-07-16T03:35:55 | `platform-action-precheck` | An iOS task was likewise converted into UI instructions instead of being executed through a Shortcuts URL scheme or device MCP tool, showing a cross-platform action-routing defect rather than a Discord-specific mistake. |
| 2026-07-16T03:35:55 | `loop-name-validation-guard` | The phrase 'That turns the loop' was parsed as a loop reference even though it matched no registered loop ID, exposing either hallucinated state terminology or an overly broad loop-reference detector requiring exact-ID syntax. |

## Root-cause chain

1. Outbound responses contained restart scaffolding, UI instructions for executable platform tasks, an unsupported 'confirmed' claim, and an unregistered loop reference.
2. The agent treated harness context as user-visible prose, defaulted to instructional narration instead of tool execution, and generated state claims from language rather than receipts.
3. Existing contracts sanitized scaffold leakage and emitted warnings, but the platform and evidence guards did not block delivery or require corrective execution.
4. Action routing, evidence validation, and state-name validation operate as separate checks without a single transactional completion gate tying a claimed outcome to the correct tool call and its output.
5. Prompt-level behavioral guidance therefore remained able to fail repeatedly while only deterministic egress mutation prevented the most obvious leakage.

## The contract that would have caught it

**`platform-action-receipt-gate`**

- **Trigger:** A response concerns an executable Discord or iOS action and contains completion or certainty language such as 'done', 'sent', or 'confirmed'.
- **Precondition:** Require a successful invocation of the platform-approved API, bot gateway, Shortcuts scheme, or device MCP tool in the current action trace, plus a captured tool-output receipt cited by the response.
- **Why it catches this:** It would have combined the simultaneous FM-012 and FM-026 signals into a hard block: the Discord/iOS response could not ship as UI instructions or claim confirmation until the correct platform tool executed and produced evidence.

## Why this matters

Prompt-only guardrails did not stop the agent from repeating the same scaffold leakage and wrong-action routing across multiple events. Deterministic enforcement materially contained the incident by stripping private harness text, but the trace also shows that warnings are insufficient: high-risk action and evidence contracts must block output until a valid execution receipt exists.

---

*Want this autopsy run on your agent's traces? [Submit one redacted failure trace](failure-trace-lab-intake.html) — this is the free tier of the agent-failure audit.*
