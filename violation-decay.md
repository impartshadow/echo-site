# Violation Decay Case Study

Generated: 2026-07-06T08:20:56.169448+00:00

## Claim
patterned-stop cooled from 192 to 2 weekly hits; platform-action-precheck is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 2047
- Distinct contracts in log: 55
- Distinct failure modes: 21
- Eligible contracts: 42
- Cooled contracts: 33
- Hotter contracts: 7

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `patterned-stop` | 235 | 192 | 2 | -190 | -99.0% |
| `persistent-correction` | 343 | 191 | 46 | -145 | -75.9% |
| `loop-tripwire` | 81 | 81 | 0 | -81 | -100.0% |
| `factual-claim-verification` | 119 | 75 | 13 | -62 | -82.7% |
| `web-tool-invocation-rewriter` | 57 | 57 | 0 | -57 | -100.0% |
| `completion-artifact` | 125 | 59 | 11 | -48 | -81.4% |
| `partial-evidence-flag` | 228 | 90 | 49 | -41 | -45.6% |
| `anticipation-phase-gate` | 42 | 41 | 0 | -41 | -100.0% |
| `dox-guard` | 89 | 35 | 9 | -26 | -74.3% |
| `harness-scaffolding-leak-guard` | 16 | 16 | 0 | -16 | -100.0% |
| `live-state-claim-guard` | 35 | 17 | 2 | -15 | -88.2% |
| `loop-name-validation-guard` | 34 | 21 | 9 | -12 | -57.1% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `platform-action-precheck` | 68 | 7 | 26 | +19 | +271.4% |
| `state-assertion-grounding` | 71 | 13 | 21 | +8 | +61.5% |
| `behavioral-haiku-guard` | 45 | 13 | 17 | +4 | +30.8% |
| `commit-hash-verification` | 63 | 17 | 19 | +2 | +11.8% |
| `balar-clarification` | 19 | 6 | 7 | +1 | +16.7% |
| `state-io-consolidation-guard` | 15 | 4 | 5 | +1 | +25.0% |
| `we-built-attribution` | 4 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
