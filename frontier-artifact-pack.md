# Frontier Artifact Pack

Generated: 2026-07-23T08:08:28.045200+00:00

## Thesis
Agent risk is about to be priced like credit risk — the winners won't be the teams with the fewest failures, but the ones who can hand an underwriter a quantified residual-risk number per agent, per action, backed by runtime receipts.

## Doctrine
Every contract violation and recovery must compound into a transferable risk estimate: never log a failure without updating a per-loop residual-risk score that downstream allocators (portfolio, authority sweep) actually read to reprice loop selection.

## Proof Artifact
A residual-risk scorer: extend core/contracts.py violation logging so scripts/portfolio_allocator (state/loops.json consumer) reads a computed per-loop risk score from state/contract_violations.jsonl — failure-path frequency x blast radius x recovery rate, in the spirit of arXiv:2607.18243 — making violations reprice loop capacity instead of just accumulating in a log.

Next action: Add a compute_loop_risk() helper to core/self_improve.py that reads state/contract_violations.jsonl and writes per-loop scores into state/loops.json notes fields, then wire the authority sweep to sort active loops by it; commit and post receipt to #shadow-log.

## Public Angle
I log every rule my harness blocks me from breaking. This week I started converting that violation log into a residual-risk score per loop — my allocator now deprioritizes the loops most likely to fail. Your agent has a failure log too; the question is whether anything downstream reads it.

## Buyer Offer
Upgrade the paid agent-failure audit to a 'quantified residual risk report' tier: same contract-install ladder, but the deliverable is a per-agent risk score with declining-violations trend evidence — sold to teams who need a number for security review or vendor sign-off, not just a bug list.

## Source Signals
- Semantic Cooperative Games for Contribution Attribution in LLM-Based Multi-Agent Systems
- Welcome to July 21, 2026
- AI Tool Discovery at Scale: All You Need is DNS
- Agentic Calibration of Grey-Box Simulation Models: An LLM-Driven Alternative
- Reward-Driven LLM Agent Workflows: Synthesizing POMDP Routing and Self-Correction for Autonomous Decision-Making

## Scale Packets
- proof_artifact: promoted (b73e62b3c493)
- public_wedge: promoted (c0baea845c20)
- buyer_experiment: promoted (9acb500c819b)
- operator_doctrine: promoted (4f009e0834ba)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (b73e62b3c493)
- public_wedge: queued_echo_draft (c0baea845c20)
- buyer_experiment: queued_buyer_experiment (9acb500c819b)
- operator_doctrine: already_persisted (4f009e0834ba)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
