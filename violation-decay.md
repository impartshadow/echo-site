# Violation Decay Case Study

Generated: 2026-07-27T08:00:35.801133+00:00

## Claim
persistent-correction cooled from 45 to 1 weekly hits; state-assertion-grounding is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1663
- Distinct contracts in log: 61
- Distinct failure modes: 22
- Eligible contracts: 46
- Cooled contracts: 40
- Hotter contracts: 5

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `persistent-correction` | 174 | 45 | 1 | -44 | -97.8% |
| `partial-evidence-flag` | 250 | 48 | 5 | -43 | -89.6% |
| `dox-guard` | 28 | 27 | 0 | -27 | -100.0% |
| `behavioral-haiku-guard` | 39 | 24 | 0 | -24 | -100.0% |
| `completion-artifact` | 76 | 24 | 3 | -21 | -87.5% |
| `self-verification` | 91 | 22 | 4 | -18 | -81.8% |
| `sensitive-write-router` | 12 | 11 | 1 | -10 | -90.9% |
| `balar-clarification` | 10 | 10 | 0 | -10 | -100.0% |
| `state-io-consolidation-guard` | 12 | 9 | 0 | -9 | -100.0% |
| `cl-stop_editing_github_inbound_check` | 8 | 7 | 0 | -7 | -100.0% |
| `cl-stop_editing_gmail_summary_py` | 8 | 7 | 0 | -7 | -100.0% |
| `patterned-stop` | 7 | 7 | 0 | -7 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `state-assertion-grounding` | 192 | 43 | 61 | +18 | +41.9% |
| `platform-action-precheck` | 145 | 23 | 29 | +6 | +26.1% |
| `factual-claim-verification` | 121 | 15 | 21 | +6 | +40.0% |
| `concurrence-grounding` | 42 | 12 | 14 | +2 | +16.7% |
| `unbuilt-guarantee-guard` | 6 | 1 | 3 | +2 | +200.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
