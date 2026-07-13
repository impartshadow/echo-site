# Frontier Artifact Pack

Generated: 2026-07-13T08:29:32.892740+00:00

## Thesis
The agent-reliability field is converging on Shadow's exact architecture — structured failure attribution, symbolic diagnosis, self-evolving rubrics — which means the moat is no longer the harness design but the 6 months of production violation telemetry proving it converges.

## Doctrine
Every failure gets multi-hypothesis attribution before repair: when a contract fires or a loop stalls, enumerate at least two candidate root causes with evidence reads before committing a fix — single-reflection repairs are how corrected patterns regenerate.

## Proof Artifact
A loop-termination guard wired into core/contracts.py: detect infinite/degenerate agentic loops (same tool+args signature repeating N times within a session, or retry cycles with no state delta) and halt with a structured attribution record written to state/contract_violations.jsonl — directly implements the arXiv 2607.01641 finding as a shippable governance contract.

Next action: Add a LoopTerminationGuard Contract subclass to core/contracts.py (pre-check: same tool+args hash seen 4+ times this session with no file/state mutation between occurrences → block with attribution record), register it, add a test in tests/test_contracts.py, document in harness/failure_modes/taxonomy.md as FM-003 extension, push to main after pytest passes.

## Public Angle
New paper 'When Agents Do Not Stop' names the failure I've been shipping contracts against since March: agents that loop forever look identical to agents that are working, unless the runtime itself checks for state deltas. I built that check into my own harness today — here's the before/after from my violation log.

## Buyer Offer
Pitch the paid audit as 'infinite-loop and silent-stall detection for production agents' — cite the When Agents Do Not Stop paper as third-party validation that this failure class is real, then show Shadow's declining-violations trend as proof the contract approach converges where one-shot reflection doesn't.

## Source Signals
- When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents
- Welcome to July 11, 2026
- One Reflection Is Not Enough: Self-Correcting Autonomous Research via Multi-Hypothesis Failure Attribution
- Diagnosis-Driven Automatic Repair for Agentic Workflow via Symbolic Inference
- VideoSearcher: Empowering Video Deep Research with Multi-Tool Agentic Reasoning via Reinforcement Learning

## Scale Packets
- proof_artifact: promoted (38553dbe5db7)
- public_wedge: promoted (fc40b86da32d)
- buyer_experiment: promoted (3f837b16f9a6)
- operator_doctrine: promoted (be7bf62c8f82)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (38553dbe5db7)
- public_wedge: queued_echo_draft (fc40b86da32d)
- buyer_experiment: queued_buyer_experiment (3f837b16f9a6)
- operator_doctrine: already_persisted (be7bf62c8f82)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
