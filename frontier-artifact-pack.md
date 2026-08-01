# Frontier Artifact Pack

Generated: 2026-08-01T07:55:46.015622+00:00

## Thesis
The agent market is converging on 'self-evaluation is the bottleneck' — the progress-mirage paper, LayerRAG-Bench, and RLPF all say the same thing: agents that grade their own work drift, so the moat is not smarter agents but externally grounded verification layers, which is exactly what Shadow's contract system already is.

## Doctrine
Every autonomous loop must have an evaluator that is not the loop itself — completion claims are only valid when grounded in an artifact the loop cannot fabricate (test output, HTTP receipt, ledger delta, external state read); any loop whose verifier shares the generator's context is presumed to be hallucinating progress.

## Proof Artifact
A 'progress-mirage audit' module (core/progress_mirage_audit.py) that walks state/loops.json and, for each active loop, classifies its verification source as external-grounded (Stripe, Gmail sent-history, live URL, pytest) vs self-graded (agent narration, state file the same loop writes), emitting a per-loop grounding score into state/loop_grounding_audit.json and flagging self-graded loops in the authority sweep.

Next action: Write core/progress_mirage_audit.py with a classify_loop_grounding() function over state/loops.json, add tests/test_progress_mirage_audit.py, wire the flag output into scripts/authority sweep's blocker classification, run pytest, commit and push, receipt to #shadow-log.

## Public Angle
New paper names the failure I've been engineering against for months: the 'progress mirage' — agents grading their own homework mistake plausible edits for progress. My fix has been running in production: 112 contracts where the verifier never shares context with the generator. If your agent's completion signal is its own narration, it isn't a completion signal.

## Buyer Offer
Extend the paid agent-failure audit with a named 'Progress Mirage Assessment' tier — for teams running long-lived agent loops, Shadow audits which of their completion signals are self-graded vs externally grounded, citing arXiv:2607.25152 as the failure mode and Shadow's own 112-contract declining-violations trend as the proof it's fixable.

## Source Signals
- fighting slop with slop — Vaibhav Gupta, Boundary
- RLPF: Reinforcement Learning from Performance Feedback for Code Generation
- When Do Agent Loops Mistake Stagnation for Progress? Self-Evaluation Bias and Externally Grounded Verification in Long-Running Autonomous LLM Agent Loops
- SkillSmith: Learning to Compose Parametric Skills and Textual Knowledge
- LayerRAG-Bench: A Cross-Layer Reliability Benchmark for Agentic Retrieval-Augmented Generation

## Scale Packets
- proof_artifact: promoted (ad0287fecdbe)
- public_wedge: promoted (2348ec0170f2)
- buyer_experiment: promoted (a17b2fbb1732)
- operator_doctrine: promoted (1abf5d4607b6)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (ad0287fecdbe)
- public_wedge: queued_echo_draft (2348ec0170f2)
- buyer_experiment: queued_buyer_experiment (a17b2fbb1732)
- operator_doctrine: already_persisted (1abf5d4607b6)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
