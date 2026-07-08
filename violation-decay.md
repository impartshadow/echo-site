# Violation Decay Case Study

Generated: 2026-07-08T08:19:28.818461+00:00

## Claim
patterned-stop cooled from 152 to 0 weekly hits; platform-action-precheck is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 1900
- Distinct contracts in log: 55
- Distinct failure modes: 21
- Eligible contracts: 43
- Cooled contracts: 33
- Hotter contracts: 6

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `patterned-stop` | 189 | 152 | 0 | -152 | -100.0% |
| `persistent-correction` | 347 | 199 | 55 | -144 | -72.4% |
| `loop-tripwire` | 68 | 68 | 0 | -68 | -100.0% |
| `factual-claim-verification` | 119 | 70 | 20 | -50 | -71.4% |
| `dox-guard` | 87 | 49 | 3 | -46 | -93.9% |
| `web-tool-invocation-rewriter` | 44 | 44 | 0 | -44 | -100.0% |
| `anticipation-phase-gate` | 42 | 41 | 0 | -41 | -100.0% |
| `completion-artifact` | 99 | 43 | 9 | -34 | -79.1% |
| `live-state-claim-guard` | 35 | 17 | 1 | -16 | -94.1% |
| `loop-name-validation-guard` | 34 | 21 | 5 | -16 | -76.2% |
| `harness-scaffolding-leak-guard` | 14 | 14 | 0 | -14 | -100.0% |
| `partial-evidence-flag` | 211 | 70 | 60 | -10 | -14.3% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `platform-action-precheck` | 70 | 13 | 31 | +18 | +138.5% |
| `state-assertion-grounding` | 73 | 13 | 18 | +5 | +38.5% |
| `stale-state-assertion-guard` | 42 | 11 | 16 | +5 | +45.5% |
| `commit-hash-verification` | 59 | 22 | 24 | +2 | +9.1% |
| `api-first-routing-guard` | 11 | 5 | 6 | +1 | +20.0% |
| `we-built-attribution` | 4 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
