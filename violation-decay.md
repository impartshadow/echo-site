# Violation Decay Case Study

Generated: 2026-07-14T08:54:27.349376+00:00

## Claim
patterned-stop cooled from 29 to 0 weekly hits; partial-evidence-flag is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1487
- Distinct contracts in log: 52
- Distinct failure modes: 21
- Eligible contracts: 44
- Cooled contracts: 31
- Hotter contracts: 9

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `patterned-stop` | 43 | 29 | 0 | -29 | -100.0% |
| `dox-guard` | 56 | 24 | 1 | -23 | -95.8% |
| `loop-name-validation-guard` | 38 | 21 | 4 | -17 | -81.0% |
| `dangerous-path-guard` | 15 | 12 | 0 | -12 | -100.0% |
| `commit-hash-verification` | 61 | 21 | 13 | -8 | -38.1% |
| `concurrence-grounding` | 21 | 12 | 5 | -7 | -58.3% |
| `identity-hash-guard` | 7 | 7 | 0 | -7 | -100.0% |
| `behavioral-haiku-guard` | 52 | 13 | 7 | -6 | -46.2% |
| `balar-clarification` | 19 | 6 | 0 | -6 | -100.0% |
| `cl-stop_editing_github_inbound_check` | 8 | 7 | 1 | -6 | -85.7% |
| `cl-stop_editing_gmail_summary_py` | 8 | 7 | 1 | -6 | -85.7% |
| `api-first-routing-guard` | 11 | 5 | 0 | -5 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 245 | 48 | 97 | +49 | +102.1% |
| `factual-claim-verification` | 87 | 13 | 39 | +26 | +200.0% |
| `stale-state-assertion-guard` | 59 | 5 | 31 | +26 | +520.0% |
| `state-assertion-grounding` | 99 | 13 | 28 | +15 | +115.4% |
| `completion-artifact` | 106 | 29 | 40 | +11 | +37.9% |
| `persistent-correction` | 217 | 55 | 61 | +6 | +10.9% |
| `continuation-ambiguity-guard` | 8 | 2 | 4 | +2 | +100.0% |
| `high-stakes-pre-critique` | 23 | 5 | 6 | +1 | +20.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
