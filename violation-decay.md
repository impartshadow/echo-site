# Violation Decay Case Study

Generated: 2026-07-10T08:49:10.674414+00:00

## Claim
patterned-stop cooled from 151 to 0 weekly hits; partial-evidence-flag is the hottest remaining governance gap.

This is not a generic benchmark. It is a trend read over Shadow's production
contract-violation log: `state/contract_violations.jsonl`.

## Totals
- Violations logged: 2080
- Distinct contracts in log: 57
- Distinct failure modes: 21
- Eligible contracts: 43
- Cooled contracts: 31
- Hotter contracts: 8

## Cooled Guardrails
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `patterned-stop` | 177 | 151 | 0 | -151 | -100.0% |
| `persistent-correction` | 365 | 196 | 89 | -107 | -54.6% |
| `loop-tripwire` | 64 | 64 | 0 | -64 | -100.0% |
| `dox-guard` | 87 | 49 | 1 | -48 | -98.0% |
| `web-tool-invocation-rewriter` | 43 | 43 | 0 | -43 | -100.0% |
| `anticipation-phase-gate` | 42 | 41 | 0 | -41 | -100.0% |
| `loop-name-validation-guard` | 36 | 21 | 7 | -14 | -66.7% |
| `factual-claim-verification` | 138 | 61 | 49 | -12 | -19.7% |
| `live-state-claim-guard` | 40 | 17 | 6 | -11 | -64.7% |
| `dangerous-path-guard` | 18 | 11 | 1 | -10 | -90.9% |
| `identity-hash-guard` | 8 | 8 | 0 | -8 | -100.0% |
| `behavioral-haiku-guard` | 51 | 13 | 9 | -4 | -30.8% |

## Remaining Hot Spots
| Contract | Total | First 7d | Recent 7d | Delta | Change |
|---|---:|---:|---:|---:|---:|
| `partial-evidence-flag` | 280 | 77 | 128 | +51 | +66.2% |
| `stale-state-assertion-guard` | 63 | 7 | 40 | +33 | +471.4% |
| `platform-action-precheck` | 77 | 13 | 34 | +21 | +161.5% |
| `state-assertion-grounding` | 88 | 13 | 28 | +15 | +115.4% |
| `commit-hash-verification` | 67 | 21 | 32 | +11 | +52.4% |
| `continuation-ambiguity-guard` | 8 | 2 | 4 | +2 | +100.0% |
| `we-built-attribution` | 5 | 1 | 3 | +2 | +200.0% |
| `high-stakes-pre-critique` | 26 | 9 | 10 | +1 | +11.1% |

## Buyer Use
This is the case-study metric behind the Fabricated-Completion Audit:
mine a live agent's logs, identify unverified completion claims, install
deterministic contracts, then measure whether the same failure family cools.
