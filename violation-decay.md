# Violation Decay Case Study

Generated: 2026-11-01T09:03:23.659269+00:00

## Claim
raw-gmail-send-guard cooled from 6 to 0 weekly hits; platform-action-precheck is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 153
- Distinct contracts in log: 55
- Distinct failure modes: 23
- Eligible contracts: 34
- Cooled contracts: 32
- Hotter contracts: 1

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `raw-gmail-send-guard` | 6 | 6 | 0 | -6 | -100.0% |
| `third-party-state-claim-verification-guard` | 6 | 5 | 1 | -4 | -80.0% |
| `chat-remark-validation-guard` | 5 | 4 | 0 | -4 | -100.0% |
| `gui-control-pre-denial-gate` | 4 | 4 | 0 | -4 | -100.0% |
| `pressure-framing-guard` | 4 | 3 | 0 | -3 | -100.0% |
| `stale-state-assertion-guard` | 11 | 2 | 0 | -2 | -100.0% |
| `deferred-first-step-gate` | 7 | 3 | 1 | -2 | -66.7% |
| `runtime-activation-claim-gate` | 5 | 2 | 0 | -2 | -100.0% |
| `cleanup-claim-mechanism-gate` | 3 | 2 | 0 | -2 | -100.0% |
| `bitwarden-claim-verification-guard` | 2 | 2 | 0 | -2 | -100.0% |
| `dox-guard` | 2 | 2 | 0 | -2 | -100.0% |
| `unbuilt-guarantee-guard` | 2 | 2 | 0 | -2 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `platform-action-precheck` | 4 | 1 | 3 | +2 | +200.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
