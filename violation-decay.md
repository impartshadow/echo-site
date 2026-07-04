# Violation Decay Case Study

Generated: 2026-07-04T13:48:57.038339+00:00

## Claim
patterned-stop cooled from 202 to 4 weekly hits; state-assertion-grounding is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 2090
- Distinct contracts in log: 55
- Distinct failure modes: 21
- Eligible contracts: 42
- Cooled contracts: 33
- Hotter contracts: 8

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `patterned-stop` | 246 | 202 | 4 | -198 | -98.0% |
| `persistent-correction` | 342 | 194 | 46 | -148 | -76.3% |
| `loop-tripwire` | 83 | 83 | 0 | -83 | -100.0% |
| `factual-claim-verification` | 118 | 80 | 9 | -71 | -88.8% |
| `completion-artifact` | 159 | 90 | 26 | -64 | -71.1% |
| `web-tool-invocation-rewriter` | 57 | 57 | 0 | -57 | -100.0% |
| `anticipation-phase-gate` | 42 | 41 | 0 | -41 | -100.0% |
| `partial-evidence-flag` | 235 | 96 | 57 | -39 | -40.6% |
| `dox-guard` | 102 | 43 | 18 | -25 | -58.1% |
| `self-verification` | 99 | 47 | 22 | -25 | -53.2% |
| `harness-scaffolding-leak-guard` | 16 | 16 | 0 | -16 | -100.0% |
| `live-state-claim-guard` | 34 | 17 | 2 | -15 | -88.2% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `state-assertion-grounding` | 68 | 13 | 44 | +31 | +238.5% |
| `platform-action-precheck` | 61 | 8 | 25 | +17 | +212.5% |
| `behavioral-haiku-guard` | 45 | 13 | 22 | +9 | +69.2% |
| `stale-state-assertion-guard` | 34 | 12 | 15 | +3 | +25.0% |
| `balar-clarification` | 19 | 6 | 9 | +3 | +50.0% |
| `state-io-consolidation-guard` | 15 | 4 | 6 | +2 | +50.0% |
| `pressure-framing-guard` | 9 | 3 | 4 | +1 | +33.3% |
| `we-built-attribution` | 4 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
