# Violation Decay Case Study

Generated: 2026-08-16T08:24:57.457180+00:00

## Claim
platform-action-precheck cooled from 69 to 0 weekly hits.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1277
- Distinct contracts in log: 68
- Distinct failure modes: 21
- Eligible contracts: 51
- Cooled contracts: 42
- Hotter contracts: 0

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `platform-action-precheck` | 71 | 69 | 0 | -69 | -100.0% |
| `state-assertion-grounding` | 168 | 81 | 14 | -67 | -82.7% |
| `partial-evidence-flag` | 57 | 57 | 0 | -57 | -100.0% |
| `scope-coverage-guard` | 43 | 43 | 0 | -43 | -100.0% |
| `self-verification` | 32 | 32 | 0 | -32 | -100.0% |
| `verification-vocabulary-gate` | 138 | 53 | 28 | -25 | -47.2% |
| `persistent-correction` | 23 | 23 | 0 | -23 | -100.0% |
| `definitive-state-assertion-gate` | 20 | 20 | 0 | -20 | -100.0% |
| `factual-claim-verification` | 125 | 46 | 27 | -19 | -41.3% |
| `terminal-state-evidence-gate` | 39 | 15 | 0 | -15 | -100.0% |
| `commit-hash-verification` | 14 | 11 | 1 | -10 | -90.9% |
| `concurrence-grounding` | 33 | 16 | 7 | -9 | -56.2% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| n/a | 0 | 0 | 0 | 0 | n/a |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
