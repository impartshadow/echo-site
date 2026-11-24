# Violation Decay Case Study

Generated: 2026-11-24T09:06:05.312001+00:00

## Claim
platform-action-precheck cooled from 3 to 0 weekly hits; live-state-claim-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 72
- Distinct contracts in log: 24
- Distinct failure modes: 14
- Eligible contracts: 10
- Cooled contracts: 7
- Hotter contracts: 2

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `platform-action-precheck` | 3 | 3 | 0 | -3 | -100.0% |
| `term-lookup-before-ask-gate` | 3 | 3 | 0 | -3 | -100.0% |
| `completion-artifact` | 6 | 3 | 1 | -2 | -66.7% |
| `propguard-provenance-detector` | 7 | 4 | 3 | -1 | -25.0% |
| `deferred-first-step-gate` | 1 | 1 | 0 | -1 | -100.0% |
| `identity-attribution-evidence-gate` | 1 | 1 | 0 | -1 | -100.0% |
| `third-party-state-claim-verification-guard` | 1 | 1 | 0 | -1 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `live-state-claim-guard` | 6 | 1 | 4 | +3 | +300.0% |
| `factual-claim-verification` | 11 | 3 | 5 | +2 | +66.7% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
