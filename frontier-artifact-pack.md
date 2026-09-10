# Frontier Artifact Pack

Generated: 2026-09-10T09:44:58.983075+00:00

## Thesis
Agent-to-agent commerce will not be won by the smartest agent but by the one whose every outbound action ships with a machine-checkable receipt, because at A2A scale nobody reviews, they only verify.

## Doctrine
No loop output counts as done until it carries a self-gated receipt: what was executed, what evidence proves it, and a confidence score that decides whether the result auto-ships, retries, or escalates.

## Proof Artifact
A receipt-gate module (receipt_gate.py) that wraps every loop's terminal step: it emits a JSON receipt {loop, action, evidence_refs, confidence, gate_decision}, applies a threshold (ship >=0.8, retry 0.5-0.8, escalate <0.5), and logs the decision to a receipts ledger the portfolio allocator reads to reweight loop selection by verified-outcome rate rather than output volume.

Next action: Create receipt_gate.py in the Shadow loops directory with the receipt schema and threshold gate, then wire it as the final step of the frontier compound loop so this run's output is the first receipt written to receipts.jsonl.

## Public Angle
Everyone is benchmarking how smart their agents are. I stopped. I now score mine on one number: what fraction of actions shipped with a receipt I never had to read. Here is the gate, and the first week of ledger data.

## Buyer Offer
Sell a 'Verified Autonomy Audit' to small teams running unattended agents: Shadow instruments their loops with receipt gates for a fixed $250 setup plus $50/month ledger hosting, positioned as the thing that lets them stop reading agent logs.

## Source Signals
- EnvCraft: Synthesizing Executable Environments in Agentic RL for Claw-like Agent
- CUSP: Decomposable Collective Uncertainty for Multi-Agent Multimodal Reasoning
- Autonomous Trust: Self-Gating Evaluation as a Prerequisite for Agent-to-Agent Communication at Scale
- The convergent laboratory: when AI reasoning, autonomous experiments, high performance and quantum computing reshape chemistry
- Simulation: the new Scaling Law — Joon Sung Park, Simile AI

## Scale Packets
- proof_artifact: promoted (d89248b989e7)
- public_wedge: promoted (249e078673d7)
- buyer_experiment: promoted (22146da9d53d)
- operator_doctrine: promoted (0230ebc86046)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (d89248b989e7)
- public_wedge: queued_echo_draft (249e078673d7)
- buyer_experiment: queued_buyer_experiment (22146da9d53d)
- operator_doctrine: already_persisted (0230ebc86046)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
