# Violation Decay Case Study

Generated: 2026-07-11T08:49:53.821451+00:00

## Claim
patterned-stop cooled from 58 to 0 weekly hits; partial-evidence-flag is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1664
- Distinct contracts in log: 54
- Distinct failure modes: 21
- Eligible contracts: 46
- Cooled contracts: 32
- Hotter contracts: 12

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `patterned-stop` | 81 | 58 | 0 | -58 | -100.0% |
| `dox-guard` | 75 | 39 | 1 | -38 | -97.4% |
| `anticipation-phase-gate` | 23 | 22 | 0 | -22 | -100.0% |
| `loop-tripwire` | 22 | 22 | 0 | -22 | -100.0% |
| `loop-name-validation-guard` | 36 | 21 | 7 | -14 | -66.7% |
| `web-tool-invocation-rewriter` | 13 | 13 | 0 | -13 | -100.0% |
| `dangerous-path-guard` | 15 | 12 | 1 | -11 | -91.7% |
| `persistent-correction` | 262 | 95 | 85 | -10 | -10.5% |
| `live-state-claim-guard` | 37 | 14 | 6 | -8 | -57.1% |
| `concurrence-grounding` | 18 | 12 | 5 | -7 | -58.3% |
| `identity-hash-guard` | 7 | 7 | 0 | -7 | -100.0% |
| `balar-clarification` | 19 | 6 | 0 | -6 | -100.0% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 249 | 52 | 121 | +69 | +132.7% |
| `factual-claim-verification` | 89 | 13 | 48 | +35 | +269.2% |
| `stale-state-assertion-guard` | 60 | 5 | 38 | +33 | +660.0% |
| `platform-action-precheck` | 79 | 13 | 29 | +16 | +123.1% |
| `state-assertion-grounding` | 91 | 13 | 28 | +15 | +115.4% |
| `commit-hash-verification` | 61 | 21 | 32 | +11 | +52.4% |
| `self-verification` | 75 | 17 | 24 | +7 | +41.2% |
| `completion-artifact` | 120 | 37 | 43 | +6 | +16.2% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
