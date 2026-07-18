# Violation Decay Case Study

Generated: 2026-07-18T08:31:04.210475+00:00

## Claim
patterned-stop cooled from 17 to 0 weekly hits; state-assertion-grounding is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1501
- Distinct contracts in log: 57
- Distinct failure modes: 23
- Eligible contracts: 44
- Cooled contracts: 33
- Hotter contracts: 9

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `patterned-stop` | 24 | 17 | 0 | -17 | -100.0% |
| `behavioral-haiku-guard` | 50 | 14 | 2 | -12 | -85.7% |
| `commit-hash-verification` | 46 | 11 | 0 | -11 | -100.0% |
| `live-state-claim-guard` | 25 | 13 | 2 | -11 | -84.6% |
| `completion-artifact` | 87 | 13 | 4 | -9 | -69.2% |
| `loop-name-validation-guard` | 39 | 16 | 8 | -8 | -50.0% |
| `cl-stop_editing_github_inbound_check` | 8 | 7 | 0 | -7 | -100.0% |
| `cl-stop_editing_gmail_summary_py` | 8 | 7 | 0 | -7 | -100.0% |
| `dox-guard` | 36 | 6 | 0 | -6 | -100.0% |
| `balar-clarification` | 17 | 6 | 0 | -6 | -100.0% |
| `cl-channel_shadow_hq_system_bot` | 6 | 6 | 0 | -6 | -100.0% |
| `cl-if_title_seems_relevant_can` | 6 | 6 | 0 | -6 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `state-assertion-grounding` | 121 | 9 | 38 | +29 | +322.2% |
| `platform-action-precheck` | 109 | 11 | 39 | +28 | +254.5% |
| `partial-evidence-flag` | 247 | 21 | 47 | +26 | +123.8% |
| `self-verification` | 87 | 12 | 29 | +17 | +141.7% |
| `stale-state-assertion-guard` | 72 | 5 | 16 | +11 | +220.0% |
| `factual-claim-verification` | 94 | 11 | 18 | +7 | +63.6% |
| `dangerous-path-guard` | 17 | 6 | 10 | +4 | +66.7% |
| `canonical-source-guard` | 4 | 1 | 3 | +2 | +200.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
