# Violation Decay Case Study

Generated: 2026-07-16T08:29:09.221370+00:00

## Claim
patterned-stop cooled from 18 to 0 weekly hits; partial-evidence-flag is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1374
- Distinct contracts in log: 52
- Distinct failure modes: 21
- Eligible contracts: 43
- Cooled contracts: 27
- Hotter contracts: 12

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `patterned-stop` | 27 | 18 | 0 | -18 | -100.0% |
| `loop-name-validation-guard` | 42 | 21 | 7 | -14 | -66.7% |
| `behavioral-haiku-guard` | 49 | 11 | 3 | -8 | -72.7% |
| `dox-guard` | 39 | 8 | 0 | -8 | -100.0% |
| `live-state-claim-guard` | 25 | 13 | 7 | -6 | -46.2% |
| `concurrence-grounding` | 22 | 12 | 6 | -6 | -50.0% |
| `balar-clarification` | 19 | 6 | 0 | -6 | -100.0% |
| `cl-stop_editing_github_inbound_check` | 8 | 7 | 1 | -6 | -85.7% |
| `cl-stop_editing_gmail_summary_py` | 8 | 7 | 1 | -6 | -85.7% |
| `cl-channel_shadow_hq_system_bot` | 6 | 6 | 0 | -6 | -100.0% |
| `cl-if_title_seems_relevant_can` | 6 | 6 | 0 | -6 | -100.0% |
| `cl-stop_just_cold_including_stripe` | 6 | 6 | 0 | -6 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 222 | 21 | 93 | +72 | +342.9% |
| `persistent-correction` | 189 | 23 | 56 | +33 | +143.5% |
| `stale-state-assertion-guard` | 61 | 5 | 30 | +25 | +500.0% |
| `state-assertion-grounding` | 99 | 9 | 30 | +21 | +233.3% |
| `completion-artifact` | 88 | 12 | 31 | +19 | +158.3% |
| `factual-claim-verification` | 85 | 12 | 31 | +19 | +158.3% |
| `platform-action-precheck` | 91 | 14 | 22 | +8 | +57.1% |
| `self-verification` | 74 | 13 | 19 | +6 | +46.2% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
