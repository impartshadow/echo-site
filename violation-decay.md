# Violation Decay Case Study

Generated: 2026-07-15T08:16:21.578363+00:00

## Claim
patterned-stop cooled from 25 to 0 weekly hits; partial-evidence-flag is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1418
- Distinct contracts in log: 52
- Distinct failure modes: 21
- Eligible contracts: 44
- Cooled contracts: 30
- Hotter contracts: 9

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `patterned-stop` | 38 | 25 | 0 | -25 | -100.0% |
| `loop-name-validation-guard` | 39 | 21 | 5 | -16 | -76.2% |
| `dox-guard` | 45 | 14 | 0 | -14 | -100.0% |
| `dangerous-path-guard` | 10 | 9 | 0 | -9 | -100.0% |
| `behavioral-haiku-guard` | 52 | 13 | 6 | -7 | -53.8% |
| `concurrence-grounding` | 21 | 12 | 5 | -7 | -58.3% |
| `commit-hash-verification` | 53 | 16 | 10 | -6 | -37.5% |
| `balar-clarification` | 19 | 6 | 0 | -6 | -100.0% |
| `cl-stop_editing_github_inbound_check` | 8 | 7 | 1 | -6 | -85.7% |
| `cl-stop_editing_gmail_summary_py` | 8 | 7 | 1 | -6 | -85.7% |
| `api-first-routing-guard` | 11 | 5 | 0 | -5 | -100.0% |
| `personal-token-send-guard` | 5 | 5 | 0 | -5 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 234 | 38 | 92 | +54 | +142.1% |
| `factual-claim-verification` | 87 | 12 | 37 | +25 | +208.3% |
| `stale-state-assertion-guard` | 58 | 5 | 27 | +22 | +440.0% |
| `state-assertion-grounding` | 101 | 13 | 28 | +15 | +115.4% |
| `completion-artifact` | 100 | 24 | 39 | +15 | +62.5% |
| `persistent-correction` | 208 | 47 | 56 | +9 | +19.1% |
| `self-verification` | 75 | 13 | 21 | +8 | +61.5% |
| `live-state-claim-guard` | 26 | 5 | 6 | +1 | +20.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
