# Violation Decay Case Study

Generated: 2026-08-19T08:22:36.253931+00:00

## Claim
platform-action-precheck cooled from 48 to 2 weekly hits; capability-scope-assertion-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1339
- Distinct contracts in log: 71
- Distinct failure modes: 20
- Eligible contracts: 51
- Cooled contracts: 46
- Hotter contracts: 1

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `platform-action-precheck` | 52 | 48 | 2 | -46 | -95.8% |
| `state-assertion-grounding` | 154 | 64 | 19 | -45 | -70.3% |
| `partial-evidence-flag` | 26 | 26 | 0 | -26 | -100.0% |
| `verification-vocabulary-gate` | 149 | 51 | 29 | -22 | -43.1% |
| `definitive-state-assertion-gate` | 18 | 18 | 0 | -18 | -100.0% |
| `scope-coverage-guard` | 17 | 17 | 0 | -17 | -100.0% |
| `self-verification` | 16 | 16 | 0 | -16 | -100.0% |
| `factual-claim-verification` | 120 | 35 | 21 | -14 | -40.0% |
| `persistent-correction` | 13 | 13 | 0 | -13 | -100.0% |
| `terminal-state-evidence-gate` | 39 | 13 | 2 | -11 | -84.6% |
| `concurrence-grounding` | 30 | 14 | 5 | -9 | -64.3% |
| `commit-hash-verification` | 15 | 11 | 2 | -9 | -81.8% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `capability-scope-assertion-guard` | 5 | 2 | 3 | +1 | +50.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
