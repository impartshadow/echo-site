# Violation Decay Case Study

Generated: 2026-10-11T07:57:38.544797+00:00

## Claim
state-assertion-grounding cooled from 7 to 0 weekly hits.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 199
- Distinct contracts in log: 61
- Distinct failure modes: 22
- Eligible contracts: 47
- Cooled contracts: 46
- Hotter contracts: 0

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `state-assertion-grounding` | 11 | 7 | 0 | -7 | -100.0% |
| `factual-claim-verification` | 14 | 6 | 0 | -6 | -100.0% |
| `dox-guard` | 8 | 6 | 1 | -5 | -83.3% |
| `continuation-ambiguity-guard` | 5 | 5 | 0 | -5 | -100.0% |
| `personal-token-send-guard` | 5 | 5 | 0 | -5 | -100.0% |
| `stale-state-assertion-guard` | 12 | 5 | 1 | -4 | -80.0% |
| `cleanup-claim-mechanism-gate` | 9 | 6 | 2 | -4 | -66.7% |
| `pressure-framing-guard` | 8 | 5 | 1 | -4 | -80.0% |
| `terminal-state-evidence-gate` | 6 | 5 | 1 | -4 | -80.0% |
| `vendor-availability-external-fetch-required` | 6 | 4 | 0 | -4 | -100.0% |
| `ownership-ask-execution-gate` | 4 | 4 | 0 | -4 | -100.0% |
| `platform-message-id-claim-guard` | 4 | 4 | 0 | -4 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| n/a | 0 | 0 | 0 | 0 | n/a |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
