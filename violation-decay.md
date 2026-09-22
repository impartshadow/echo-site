# Violation Decay Case Study

Generated: 2026-09-22T08:08:36.737814+00:00

## Claim
fleet-state-claim-grounding-gate cooled from 24 to 0 weekly hits; terminal-state-evidence-gate is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 389
- Distinct contracts in log: 61
- Distinct failure modes: 19
- Eligible contracts: 28
- Cooled contracts: 17
- Hotter contracts: 7

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `fleet-state-claim-grounding-gate` | 25 | 24 | 0 | -24 | -100.0% |
| `stale-state-assertion-guard` | 41 | 18 | 7 | -11 | -61.1% |
| `factual-claim-verification` | 39 | 16 | 7 | -9 | -56.2% |
| `personal-help-provenance-carveout` | 9 | 9 | 0 | -9 | -100.0% |
| `verification-vocabulary-gate` | 21 | 8 | 0 | -8 | -100.0% |
| `state-assertion-grounding` | 33 | 11 | 7 | -4 | -36.4% |
| `privacy-exposure-taxonomy` | 22 | 7 | 4 | -3 | -42.9% |
| `canonical-source-guard` | 2 | 2 | 0 | -2 | -100.0% |
| `numeric-parameter-assertion-guard` | 2 | 2 | 0 | -2 | -100.0% |
| `unbuilt-guarantee-guard` | 10 | 4 | 3 | -1 | -25.0% |
| `third-party-outbound-authorization-gate` | 3 | 2 | 1 | -1 | -50.0% |
| `action-deferral-guard` | 1 | 1 | 0 | -1 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `terminal-state-evidence-gate` | 14 | 2 | 5 | +3 | +150.0% |
| `cleanup-claim-mechanism-gate` | 9 | 2 | 4 | +2 | +100.0% |
| `live-state-claim-guard` | 4 | 1 | 3 | +2 | +200.0% |
| `pressure-framing-guard` | 10 | 4 | 5 | +1 | +25.0% |
| `completion-artifact` | 9 | 3 | 4 | +1 | +33.3% |
| `commit-hash-verification` | 3 | 1 | 2 | +1 | +100.0% |
| `manual-handoff-guard` | 3 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
