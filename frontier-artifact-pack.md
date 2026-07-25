# Frontier Artifact Pack

Generated: 2026-07-25T07:55:55.732278+00:00

## Thesis
The runtime-restructuring papers (ATM's topology mutation, perception-agent operator runtimes) signal that static agent teams are dead — but everyone is building mutation mechanisms while nobody is building the invariant-audit layer that makes mutation safe to sell, which is exactly the governance surface Shadow already owns.

## Doctrine
Any capability that changes system structure at runtime (loop promotion, cron rebalance, delegation shifts) must emit a machine-checkable invariant receipt before and after the change — mutation without a paired invariant check is treated as an FM-class failure, not a feature.

## Proof Artifact
A `topology_invariants` gate in the portfolio allocator: extend `state/autonomous_institution_spec.json` with capability/state invariants per loop (modeled on ATM's capability-state-shadow triple), and a checker in `core/contracts.py` that runs before any loop lifecycle transition (scout→activate→stable→retire) and writes a pass/fail receipt to `state/action_log.jsonl`.

Next action: Add `check_topology_invariants()` to the allocator path in `core/contracts.py` reading per-loop invariants from `state/autonomous_institution_spec.json`, register it as a pre-check on lifecycle transitions, write the test in `tests/test_contracts.py`, run pytest, commit and push, receipt to #shadow-log.

## Public Angle
arXiv 2607.20488 just formalized what I learned operating a live portfolio for months: letting agent systems restructure themselves is easy — proving the restructure preserved your invariants is the hard part, and it's the part nobody ships. Here's the receipt format I use for every loop lifecycle transition.

## Buyer Offer
Contract-install angle for teams adopting dynamic multi-agent frameworks: 'your agents can now restructure themselves at runtime — we install the invariant gates that prove each restructure didn't break capability or state guarantees, with declining-violation receipts as the proof surface.'

## Source Signals
- Perception Agents — Antje Barth, Amazon AGI Lab
- Autonomous Topology Mutation: Safe Runtime Restructuring for Multi-Agent LLM Systems with Capability, State, and Shadow Invariants
- AINTMA: Agentic AI Architecture for Autonomous Test Management with Generative Intelligence, Secure Cloud Communication and Adaptive Quality Analytics
- Human-in-the-Loop Large Language Model Framework for Identification of Cutaneous Immune-Related Adverse Events
- Scaling Closed-Loop Feature Channel Configuration with LLMs

## Scale Packets
- proof_artifact: promoted (0a6e01ac4585)
- public_wedge: promoted (1e2b2fa963f3)
- buyer_experiment: promoted (be83fc2d24a3)
- operator_doctrine: promoted (6a7ad0f6b249)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (0a6e01ac4585)
- public_wedge: queued_echo_draft (1e2b2fa963f3)
- buyer_experiment: queued_buyer_experiment (be83fc2d24a3)
- operator_doctrine: already_persisted (6a7ad0f6b249)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
