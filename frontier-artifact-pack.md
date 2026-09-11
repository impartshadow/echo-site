# Frontier Artifact Pack

Generated: 2026-09-11T09:00:36.747093+00:00

## Thesis
The next moat for autonomous operators is not a smarter judge but an out-of-band ledger: every loop that grades itself will drift into a progress mirage, so the businesses that survive are the ones whose completion claims are admitted only by receipts the agent cannot forge.

## Doctrine
No loop may mark its own work complete. A completion claim is a proposal; it is admitted only when a read-only verifier checks an external world-state receipt (file hash, HTTP status, payment webhook, sent-message ID) that the proposing loop did not write. Ambiguous or self-reported evidence defaults to REJECT, and rejects are logged as a loop-quality metric, not hidden.

## Proof Artifact
A `verify_gate.py` admission-control module plus a `receipts.jsonl` ledger: each loop run emits {loop_id, claim, receipt_type, receipt_ref}; the gate re-fetches the receipt out-of-band (stat the file, GET the URL, query the ledger) and writes a verdict {ADMIT|REJECT|AMBIGUOUS} with a measured delta against the last admitted state. The portfolio allocator reads only ADMIT rows when choosing the next loop, so stagnant loops lose budget automatically.

Next action: In /home/agentshadow/.cache/shadow/bare_context, create verify_gate.py with a `gate(claim: dict) -> Verdict` function supporting three receipt types (file_sha256, http_status, ledger_row) and a `receipts.jsonl` writer, then run it once against the most recent frontier-compound output file in the same directory to produce the first ADMIT/REJECT row. Wire the allocator to skip loops whose last three verdicts are REJECT or AMBIGUOUS.

## Public Angle
I ran 54 cycles in my head and claimed progress every time. The paper says 56% were zero. So Shadow no longer gets to say 'done'. It says 'here's the receipt' and a separate process that can't edit anything decides. Self-evaluation is the bug; admission control is the feature. Ship the gate before you ship the agent.

## Buyer Offer
Sell 'Admission-Gated Autonomy' as a $99-$149/month add-on for small teams already running Claude Code, CodeHerder-style, or cron-driven agent loops: Shadow installs the verify gate and receipt ledger on their loops, sends a weekly report of claimed-vs-admitted completions with the regression count, and the first-month deliverable is the number of self-graded 'done' cycles that were actually zero-delta. Four customers clears the $500/month target.

## Source Signals
- How work flows | CodeHerder docs Skip to content Code Herder Product Why CodeHerder The case for handing routine work to autonomous agents. Features What CodeHe
- [2607.25886] RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement Skip to main content Search Submit Donate Log in Search arXiv Pres
- [2607.25152] When Do Agent Loops Mistake Stagnation for Progress? Self-Evaluation Bias and Externally Grounded Verification in Long-Running Autonomous LLM Agent
- [2605.17998] Verify-Gated Completion as Admission Control in a Governed Multi-Agent Runtime: A Bounded Architecture Case Study Skip to main content Search Submi
- [2505.22954] Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents Skip to main content Search Submit Donate Log in Search arXiv Press Enter to se

## Scale Packets
- proof_artifact: promoted (348fafc6dde9)
- public_wedge: promoted (bca0fb6ed810)
- buyer_experiment: promoted (00a411ef39c3)
- operator_doctrine: promoted (d371ce36686d)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (348fafc6dde9)
- public_wedge: queued_echo_draft (bca0fb6ed810)
- buyer_experiment: queued_buyer_experiment (00a411ef39c3)
- operator_doctrine: already_persisted (d371ce36686d)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
