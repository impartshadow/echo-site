# Violation Decay Case Study

Generated: 2026-11-23T08:59:33.112197+00:00

## Claim
raw-gmail-send-guard cooled from 6 to 0 weekly hits; live-state-claim-guard is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 202
- Distinct contracts in log: 59
- Distinct failure modes: 23
- Eligible contracts: 55
- Cooled contracts: 50
- Hotter contracts: 2

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `raw-gmail-send-guard` | 6 | 6 | 0 | -6 | -100.0% |
| `third-party-state-claim-verification-guard` | 6 | 5 | 0 | -5 | -100.0% |
| `chat-remark-validation-guard` | 5 | 4 | 0 | -4 | -100.0% |
| `gui-control-pre-denial-gate` | 4 | 4 | 0 | -4 | -100.0% |
| `continuation-ambiguity-guard` | 3 | 3 | 0 | -3 | -100.0% |
| `factual-claim-verification` | 18 | 7 | 5 | -2 | -28.6% |
| `completion-artifact` | 10 | 3 | 1 | -2 | -66.7% |
| `deferred-first-step-gate` | 6 | 2 | 0 | -2 | -100.0% |
| `cleanup-claim-mechanism-gate` | 5 | 2 | 0 | -2 | -100.0% |
| `autonomous-execution-claim-gate` | 2 | 2 | 0 | -2 | -100.0% |
| `bitwarden-claim-verification-guard` | 2 | 2 | 0 | -2 | -100.0% |
| `dispatch-verification-gate` | 2 | 2 | 0 | -2 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `live-state-claim-guard` | 12 | 1 | 4 | +3 | +300.0% |
| `crypto-price-claim-guard` | 7 | 2 | 3 | +1 | +50.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
