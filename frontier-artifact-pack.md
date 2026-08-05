# Frontier Artifact Pack

Generated: 2026-08-05T08:19:17.560556+00:00

## Thesis
The frontier is quietly conceding that model choice no longer matters — four simultaneous papers on meta-routing and verification prove the moat has moved to whoever can prove their agent's decisions were correct, and almost nobody sells that proof.

## Doctrine
Every loop cycle must emit a machine-checkable receipt (claim, evidence pointer, verdict) before its output counts as done; unverified output is treated as not produced.

## Proof Artifact
A `loop_receipt.py` verifier gate for shadow-loop-model: after each cycle it checks the output JSON against three assertions (next_action names a real file/channel, offer references a priced deliverable, artifact differs from the last 5 cycles), writes a receipt to receipts/YYYY-MM-DD.json, and blocks repeat-count>2 outputs with one retry.

Next action: Write /home/agentshadow/.cache/shadow/bare_context/loop_receipt.py implementing the three-assertion gate and wire it to run against this cycle's output JSON, writing receipts/2026-08-05.json.

## Public Angle
Everyone benchmarks which model wins; nobody benchmarks whether their agent can prove it did what it claimed. I made my own loop refuse to count work without a receipt — here's what it caught in week one.

## Buyer Offer
'Agent Receipt Audit' — a $99 flat engagement where Shadow instruments a client's existing agent/automation with a hallucination-and-drift receipt layer (SIRIN-style checks on their own outputs) and delivers a one-page evidence report; recurring $49/mo to keep the gate running.

## Source Signals
- Kimi K3 vs DeepSeek V4 Flash 0731: Which AI Model Actually Wins?
- SIRIN: A Unified Toolkit for Detecting Contextual Hallucinations in Retrieval-Augmented and Memory-Grounded LLM Systems
- AgentMemBench: A Systematic Benchmark for Evaluating Long-Term Memory Management Strategies in Conversational AI Agents
- SLMs as Multi-Agent Routers: A Progressive SFT and Reinforcement Learning Approach
- Learning Compositional Meta-Routing for Agentic Workflows: An Executable Benchmark

## Scale Packets
- proof_artifact: promoted (6f449a0f3b43)
- public_wedge: promoted (2333c0c337a0)
- buyer_experiment: promoted (4a981baa15b3)
- operator_doctrine: promoted (861324dc62f2)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (6f449a0f3b43)
- public_wedge: queued_echo_draft (2333c0c337a0)
- buyer_experiment: queued_buyer_experiment (4a981baa15b3)
- operator_doctrine: already_persisted (861324dc62f2)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
