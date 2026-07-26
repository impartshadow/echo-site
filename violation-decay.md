# Violation Decay Case Study

Generated: 2026-07-26T08:05:04.801339+00:00

## Claim
persistent-correction cooled from 39 to 6 weekly hits; platform-action-precheck is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1633
- Distinct contracts in log: 59
- Distinct failure modes: 22
- Eligible contracts: 46
- Cooled contracts: 36
- Hotter contracts: 6

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `persistent-correction` | 176 | 39 | 6 | -33 | -84.6% |
| `dox-guard` | 30 | 27 | 0 | -27 | -100.0% |
| `completion-artifact` | 74 | 24 | 0 | -24 | -100.0% |
| `partial-evidence-flag` | 251 | 40 | 19 | -21 | -52.5% |
| `behavioral-haiku-guard` | 40 | 22 | 3 | -19 | -86.4% |
| `sensitive-write-router` | 12 | 11 | 1 | -10 | -90.9% |
| `state-io-consolidation-guard` | 12 | 9 | 0 | -9 | -100.0% |
| `balar-clarification` | 11 | 9 | 0 | -9 | -100.0% |
| `self-verification` | 91 | 22 | 15 | -7 | -31.8% |
| `cl-stop_editing_github_inbound_check` | 8 | 7 | 0 | -7 | -100.0% |
| `cl-stop_editing_gmail_summary_py` | 8 | 7 | 0 | -7 | -100.0% |
| `patterned-stop` | 7 | 7 | 0 | -7 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `platform-action-precheck` | 145 | 23 | 44 | +21 | +91.3% |
| `state-assertion-grounding` | 177 | 43 | 56 | +13 | +30.2% |
| `factual-claim-verification` | 118 | 15 | 28 | +13 | +86.7% |
| `unbuilt-guarantee-guard` | 6 | 1 | 5 | +4 | +400.0% |
| `stale-state-assertion-guard` | 86 | 15 | 18 | +3 | +20.0% |
| `concurrence-grounding` | 39 | 12 | 13 | +1 | +8.3% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
