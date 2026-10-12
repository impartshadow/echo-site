# Violation Decay Case Study

Generated: 2026-10-12T09:07:48.956167+00:00

## Claim
state-assertion-grounding cooled from 7 to 1 weekly hits.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 183
- Distinct contracts in log: 60
- Distinct failure modes: 22
- Eligible contracts: 48
- Cooled contracts: 47
- Hotter contracts: 0

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `state-assertion-grounding` | 12 | 7 | 1 | -6 | -85.7% |
| `stale-state-assertion-guard` | 10 | 7 | 1 | -6 | -85.7% |
| `cleanup-claim-mechanism-gate` | 9 | 6 | 1 | -5 | -83.3% |
| `factual-claim-verification` | 9 | 5 | 0 | -5 | -100.0% |
| `dox-guard` | 8 | 6 | 1 | -5 | -83.3% |
| `terminal-state-evidence-gate` | 6 | 5 | 0 | -5 | -100.0% |
| `continuation-ambiguity-guard` | 5 | 5 | 0 | -5 | -100.0% |
| `pressure-framing-guard` | 9 | 5 | 1 | -4 | -80.0% |
| `completion-artifact` | 4 | 4 | 0 | -4 | -100.0% |
| `ownership-ask-execution-gate` | 4 | 4 | 0 | -4 | -100.0% |
| `platform-message-id-claim-guard` | 4 | 4 | 0 | -4 | -100.0% |
| `privacy-exposure-taxonomy` | 4 | 4 | 0 | -4 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| n/a | 0 | 0 | 0 | 0 | n/a |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
