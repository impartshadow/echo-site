# Violation Decay Case Study

Generated: 2026-11-28T09:20:45.514746+00:00

## Claim
completion-artifact cooled from 3 to 1 weekly hits; factual-claim-verification is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 60
- Distinct contracts in log: 20
- Distinct failure modes: 14
- Eligible contracts: 4
- Cooled contracts: 3
- Hotter contracts: 1

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `completion-artifact` | 5 | 3 | 1 | -2 | -66.7% |
| `platform-action-precheck` | 2 | 2 | 0 | -2 | -100.0% |
| `propguard-provenance-detector` | 7 | 4 | 3 | -1 | -25.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `factual-claim-verification` | 9 | 1 | 5 | +4 | +400.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
