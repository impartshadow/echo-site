# Violation Decay Case Study

Generated: 2026-08-17T08:16:34.242081+00:00

## Claim
platform-action-precheck cooled from 64 to 2 weekly hits; capability-scope-assertion-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1404
- Distinct contracts in log: 71
- Distinct failure modes: 21
- Eligible contracts: 52
- Cooled contracts: 49
- Hotter contracts: 1

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `platform-action-precheck` | 68 | 64 | 2 | -62 | -96.9% |
| `state-assertion-grounding` | 171 | 80 | 23 | -57 | -71.2% |
| `partial-evidence-flag` | 47 | 47 | 0 | -47 | -100.0% |
| `scope-coverage-guard` | 41 | 41 | 0 | -41 | -100.0% |
| `self-verification` | 30 | 30 | 0 | -30 | -100.0% |
| `verification-vocabulary-gate` | 147 | 53 | 29 | -24 | -45.3% |
| `persistent-correction` | 21 | 21 | 0 | -21 | -100.0% |
| `definitive-state-assertion-gate` | 20 | 20 | 0 | -20 | -100.0% |
| `factual-claim-verification` | 128 | 44 | 25 | -19 | -43.2% |
| `terminal-state-evidence-gate` | 39 | 15 | 0 | -15 | -100.0% |
| `commit-hash-verification` | 14 | 11 | 1 | -10 | -90.9% |
| `concurrence-grounding` | 32 | 16 | 7 | -9 | -56.2% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `capability-scope-assertion-guard` | 5 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
