# Violation Decay Case Study

Generated: 2026-08-21T08:14:58.610648+00:00

## Claim
state-assertion-grounding cooled from 47 to 16 weekly hits; stale-state-assertion-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1082
- Distinct contracts in log: 63
- Distinct failure modes: 18
- Eligible contracts: 47
- Cooled contracts: 40
- Hotter contracts: 3

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `state-assertion-grounding` | 121 | 47 | 16 | -31 | -66.0% |
| `platform-action-precheck` | 26 | 22 | 2 | -20 | -90.9% |
| `crypto-price-claim-guard` | 20 | 19 | 1 | -18 | -94.7% |
| `commit-hash-verification` | 15 | 11 | 2 | -9 | -81.8% |
| `factual-claim-verification` | 99 | 18 | 13 | -5 | -27.8% |
| `concurrence-grounding` | 20 | 7 | 2 | -5 | -71.4% |
| `definitive-state-assertion-gate` | 5 | 5 | 0 | -5 | -100.0% |
| `platform-action-param-schema-guard` | 5 | 5 | 0 | -5 | -100.0% |
| `numeric-parameter-assertion-guard` | 11 | 5 | 1 | -4 | -80.0% |
| `patterned-stop` | 4 | 4 | 0 | -4 | -100.0% |
| `watchdog-reply-resolution-guard` | 4 | 4 | 0 | -4 | -100.0% |
| `verification-vocabulary-gate` | 113 | 26 | 23 | -3 | -11.5% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `stale-state-assertion-guard` | 69 | 9 | 14 | +5 | +55.6% |
| `manual-handoff-guard` | 5 | 1 | 4 | +3 | +300.0% |
| `capability-scope-assertion-guard` | 5 | 2 | 3 | +1 | +50.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
