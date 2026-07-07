# Violation Decay Case Study

Generated: 2026-07-07T09:03:53.715460+00:00

## Claim
patterned-stop cooled from 174 to 0 weekly hits; platform-action-precheck is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 2019
- Distinct contracts in log: 54
- Distinct failure modes: 21
- Eligible contracts: 44
- Cooled contracts: 34
- Hotter contracts: 8

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `patterned-stop` | 217 | 174 | 0 | -174 | -100.0% |
| `persistent-correction` | 352 | 191 | 55 | -136 | -71.2% |
| `loop-tripwire` | 76 | 76 | 0 | -76 | -100.0% |
| `factual-claim-verification` | 123 | 73 | 17 | -56 | -76.7% |
| `web-tool-invocation-rewriter` | 52 | 52 | 0 | -52 | -100.0% |
| `anticipation-phase-gate` | 42 | 41 | 0 | -41 | -100.0% |
| `completion-artifact` | 107 | 41 | 11 | -30 | -73.2% |
| `dox-guard` | 89 | 35 | 9 | -26 | -74.3% |
| `partial-evidence-flag` | 239 | 85 | 61 | -24 | -28.2% |
| `live-state-claim-guard` | 35 | 17 | 1 | -16 | -94.1% |
| `harness-scaffolding-leak-guard` | 15 | 15 | 0 | -15 | -100.0% |
| `loop-name-validation-guard` | 34 | 21 | 8 | -13 | -61.9% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `platform-action-precheck` | 72 | 6 | 29 | +23 | +383.3% |
| `commit-hash-verification` | 60 | 10 | 23 | +13 | +130.0% |
| `state-assertion-grounding` | 72 | 13 | 20 | +7 | +53.8% |
| `stale-state-assertion-guard` | 43 | 11 | 16 | +5 | +45.5% |
| `behavioral-haiku-guard` | 46 | 13 | 14 | +1 | +7.7% |
| `balar-clarification` | 19 | 6 | 7 | +1 | +16.7% |
| `api-first-routing-guard` | 11 | 5 | 6 | +1 | +20.0% |
| `we-built-attribution` | 4 | 1 | 2 | +1 | +100.0% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
