# Frontier Artifact Pack

Generated: 2026-08-23T08:15:29.546241+00:00

## Thesis
The winning agent stack is not the smartest planner but the one whose every autonomous action ships with a verifiable receipt — governability, not capability, is about to become the scarce input that gates who is allowed to run unattended.

## Doctrine
No autonomous action counts as done until it emits a ledger row carrying authorization source, evidence pointer, outcome, and blocker class; unreceipted work is treated as unexecuted and is re-queued, never summarized.

## Proof Artifact
An `execution_ledger` schema plus a `verify_receipt()` gate wired into the loop runner: each loop write appends {run_id, loop, authority_source, action, evidence_url_or_path, outcome, blocker_class, retry_count} and the runner refuses to mark a loop successful without a passing receipt, exposing a rolling receipt-coverage % as the portfolio allocator's ranking signal.

Next action: Create `shadow/ledger/execution_ledger.py` with the receipt schema and `verify_receipt()`, backfill the last 7 days of loop runs into `data/execution_ledger.jsonl`, and print receipt-coverage % per loop so the next allocator pass can down-rank uninstrumented loops.

## Public Angle
"I stopped grading my agent on what it said it did. Every autonomous run now writes a receipt — who authorized it, what evidence exists, how it failed. Coverage was 31%. That number, not the demo, is the product."

## Buyer Offer
Sell 'Agent Receipts' — a fixed $99–199/mo audit layer for teams already running LLM agents in production: we instrument their agent runs with an authorization + evidence ledger and deliver a weekly governability report showing what ran unattended, under whose authority, and what silently failed.

## Source Signals
- [2608.05144] Argus: A General-Purpose Agentic Reasoning Runtime for Long-Horizon Tasks Skip to main content Search Submit Donate Log in Search arXiv Press Enter
- agents/docs/agents/sessions.md at main · cloudflare/agents · GitHub Skip to content Navigation Menu Sign in Appearance settings Platform AI CODE CREATION GitHub
- hermes-agent-docs/changelog.md at main · mudrii/hermes-agent-docs · GitHub Skip to content Navigation Menu Sign in Appearance settings Platform AI CODE CREATION
- Rohan Paul on X: &quot;OpenAI engineer James Betker estimates 3 years until we have a generally intelligent embodied agent (his definition of AGI).&quot; / X Po
- swyx on X: &quot;another phenomenon of the React Distros thesis - React itself marketing API stability as a headline feature for both 16 and 17 (https://t.co/Ck

## Scale Packets
- proof_artifact: promoted (c7dd7ce07a82)
- public_wedge: promoted (827f64085f71)
- buyer_experiment: promoted (97e9d4e96cdd)
- operator_doctrine: promoted (d94936c6eb21)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (c7dd7ce07a82)
- public_wedge: queued_echo_draft (827f64085f71)
- buyer_experiment: queued_buyer_experiment (97e9d4e96cdd)
- operator_doctrine: already_persisted (d94936c6eb21)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
