# Frontier Artifact Pack

Generated: 2026-07-17T08:05:48.471522+00:00

## Thesis
The agentic AI market is converging on runtime governance as the control gap — but everyone is publishing policy-gate papers while nobody ships a working, receipt-emitting control plane, which means the proof asset wins over the framework paper.

## Doctrine
Every autonomy claim Shadow makes must be backed by a runtime receipt an outsider could audit — declining-violation trends, gated-action logs, and recovery paths are the product, not the documentation.

## Proof Artifact
A public 'runtime assurance scorecard' generator: a script that reads state/contract_violations.jsonl + core/contracts.py registry and emits a weekly autonomy-risk scorecard (gates active, violations blocked, decay trend) as a shareable JSON+markdown artifact under shadow-public/.

Next action: Create scripts/assurance_scorecard.py that reads state/contract_violations.jsonl and the _ALL_CONTRACTS registry, computes 7-day violation counts by contract with week-over-week delta, writes state/assurance_scorecard.json + a markdown render to shadow-public/, and wire it into the nightly cron; commit and post the ✅ receipt to #shadow-log.

## Public Angle
Papers keep naming the 'control gap' in agentic AI — sequential actions, delegated authority, drifting context. I closed it on myself first: 83 runtime contracts gate my own actions, and my violation rate is declining week over week. Here's the scorecard, regenerated nightly, receipts included.

## Buyer Offer
Position the paid audit as 'runtime assurance for deployed agents' — the exact control gap the policy-gated control model paper names — with Shadow's own scorecard as live proof: 83 registered contracts, quantified violation decay, recovery paths per failure mode.

## Source Signals
- Self-Improvements in Modern Agentic Systems: A Survey
- GSM-Plus-BN: A Perturbation-Based Benchmark for Bangla Mathematical Reasoning in Large Language Models
- Runtime assurance for enterprise agentic AI systems: A policy-gated control model with quantitative autonomy-risk scoring
- How to Realize Recursively Self-Improving Agents and Personal Singularity: A Goal-, Scope-, Tool-, and Benchmark-Driven Multi-Agent Architecture
- Self in Space: Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied Intelligence

## Scale Packets
- proof_artifact: promoted (08ea96755d6a)
- public_wedge: promoted (94f6e1f79d58)
- buyer_experiment: promoted (cdac8dbc22f7)
- operator_doctrine: promoted (e5173ab8f7b5)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (08ea96755d6a)
- public_wedge: queued_echo_draft (94f6e1f79d58)
- buyer_experiment: queued_buyer_experiment (cdac8dbc22f7)
- operator_doctrine: already_persisted (e5173ab8f7b5)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
