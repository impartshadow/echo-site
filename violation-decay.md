# Violation Decay Case Study

Generated: 2026-08-15T08:15:56.475953+00:00

## Claim
platform-action-precheck cooled from 64 to 0 weekly hits; stale-state-assertion-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1247
- Distinct contracts in log: 69
- Distinct failure modes: 21
- Eligible contracts: 50
- Cooled contracts: 40
- Hotter contracts: 3

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `platform-action-precheck` | 85 | 64 | 0 | -64 | -100.0% |
| `partial-evidence-flag` | 63 | 63 | 0 | -63 | -100.0% |
| `state-assertion-grounding` | 170 | 73 | 22 | -51 | -69.9% |
| `scope-coverage-guard` | 43 | 43 | 0 | -43 | -100.0% |
| `self-verification` | 34 | 34 | 0 | -34 | -100.0% |
| `persistent-correction` | 29 | 29 | 0 | -29 | -100.0% |
| `definitive-state-assertion-gate` | 20 | 20 | 0 | -20 | -100.0% |
| `verification-vocabulary-gate` | 132 | 53 | 36 | -17 | -32.1% |
| `terminal-state-evidence-gate` | 39 | 15 | 3 | -12 | -80.0% |
| `commit-hash-verification` | 14 | 11 | 1 | -10 | -90.9% |
| `sensitive-write-router` | 11 | 10 | 0 | -10 | -100.0% |
| `dangerous-path-guard` | 10 | 10 | 0 | -10 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `stale-state-assertion-guard` | 85 | 29 | 35 | +6 | +20.7% |
| `factual-claim-verification` | 121 | 39 | 40 | +1 | +2.6% |
| `blocker-surfacing-gate` | 5 | 2 | 3 | +1 | +50.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
