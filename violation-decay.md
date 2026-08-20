# Violation Decay Case Study

Generated: 2026-08-20T08:48:11.531274+00:00

## Claim
state-assertion-grounding cooled from 59 to 17 weekly hits; stale-state-assertion-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1134
- Distinct contracts in log: 66
- Distinct failure modes: 18
- Eligible contracts: 49
- Cooled contracts: 43
- Hotter contracts: 3

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `state-assertion-grounding` | 133 | 59 | 17 | -42 | -71.2% |
| `platform-action-precheck` | 33 | 29 | 2 | -27 | -93.1% |
| `crypto-price-claim-guard` | 20 | 19 | 1 | -18 | -94.7% |
| `verification-vocabulary-gate` | 128 | 40 | 25 | -15 | -37.5% |
| `concurrence-grounding` | 27 | 14 | 4 | -10 | -71.4% |
| `factual-claim-verification` | 102 | 21 | 12 | -9 | -42.9% |
| `commit-hash-verification` | 15 | 11 | 2 | -9 | -81.8% |
| `definitive-state-assertion-gate` | 8 | 8 | 0 | -8 | -100.0% |
| `platform-action-param-schema-guard` | 5 | 5 | 0 | -5 | -100.0% |
| `numeric-parameter-assertion-guard` | 11 | 5 | 1 | -4 | -80.0% |
| `patterned-stop` | 4 | 4 | 0 | -4 | -100.0% |
| `watchdog-reply-resolution-guard` | 4 | 4 | 0 | -4 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `stale-state-assertion-guard` | 70 | 10 | 15 | +5 | +50.0% |
| `manual-handoff-guard` | 5 | 1 | 4 | +3 | +300.0% |
| `capability-scope-assertion-guard` | 5 | 2 | 3 | +1 | +50.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
