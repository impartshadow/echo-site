# Violation Decay Case Study

Generated: 2026-08-09T08:18:20.120994+00:00

## Claim
partial-evidence-flag cooled from 94 to 0 weekly hits; factual-claim-verification is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1433
- Distinct contracts in log: 67
- Distinct failure modes: 20
- Eligible contracts: 46
- Cooled contracts: 38
- Hotter contracts: 2

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 154 | 94 | 0 | -94 | -100.0% |
| `persistent-correction` | 84 | 56 | 0 | -56 | -100.0% |
| `scope-coverage-guard` | 43 | 43 | 0 | -43 | -100.0% |
| `completion-artifact` | 52 | 39 | 6 | -33 | -84.6% |
| `self-verification` | 55 | 21 | 0 | -21 | -100.0% |
| `definitive-state-assertion-gate` | 20 | 20 | 0 | -20 | -100.0% |
| `verification-vocabulary-gate` | 110 | 53 | 34 | -19 | -35.8% |
| `state-assertion-grounding` | 184 | 30 | 16 | -14 | -46.7% |
| `platform-action-precheck` | 98 | 13 | 0 | -13 | -100.0% |
| `sensitive-write-router` | 12 | 11 | 0 | -11 | -100.0% |
| `terminal-state-evidence-gate` | 39 | 15 | 5 | -10 | -66.7% |
| `dangerous-path-guard` | 10 | 10 | 0 | -10 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `factual-claim-verification` | 136 | 38 | 40 | +2 | +5.3% |
| `unbuilt-guarantee-guard` | 9 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
