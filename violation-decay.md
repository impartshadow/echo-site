# Violation Decay Case Study

Generated: 2026-07-24T08:25:24.781076+00:00

## Claim
dox-guard cooled from 28 to 0 weekly hits; platform-action-precheck is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1637
- Distinct contracts in log: 57
- Distinct failure modes: 21
- Eligible contracts: 45
- Cooled contracts: 35
- Hotter contracts: 9

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `dox-guard` | 31 | 28 | 0 | -28 | -100.0% |
| `completion-artifact` | 75 | 22 | 3 | -19 | -86.4% |
| `persistent-correction` | 182 | 39 | 21 | -18 | -46.2% |
| `behavioral-haiku-guard` | 43 | 22 | 6 | -16 | -72.7% |
| `sensitive-write-router` | 11 | 11 | 0 | -11 | -100.0% |
| `state-io-consolidation-guard` | 13 | 9 | 0 | -9 | -100.0% |
| `balar-clarification` | 12 | 8 | 0 | -8 | -100.0% |
| `cl-stop_editing_github_inbound_check` | 8 | 7 | 0 | -7 | -100.0% |
| `cl-stop_editing_gmail_summary_py` | 8 | 7 | 0 | -7 | -100.0% |
| `patterned-stop` | 7 | 7 | 0 | -7 | -100.0% |
| `api-first-routing-guard` | 6 | 6 | 0 | -6 | -100.0% |
| `personal-token-send-guard` | 5 | 5 | 0 | -5 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `platform-action-precheck` | 146 | 20 | 64 | +44 | +220.0% |
| `state-assertion-grounding` | 170 | 37 | 76 | +39 | +105.4% |
| `factual-claim-verification` | 118 | 15 | 44 | +29 | +193.3% |
| `self-verification` | 93 | 13 | 30 | +17 | +130.8% |
| `partial-evidence-flag` | 253 | 38 | 52 | +14 | +36.8% |
| `stale-state-assertion-guard` | 83 | 15 | 27 | +12 | +80.0% |
| `concurrence-grounding` | 38 | 12 | 15 | +3 | +25.0% |
| `pressure-framing-guard` | 16 | 3 | 6 | +3 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
