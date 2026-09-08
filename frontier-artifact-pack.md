# Frontier Artifact Pack

Generated: 2026-09-08T08:22:13.422726+00:00

## Thesis
The moat is no longer prompts or models but the receipt trail: whoever can prove what their agents did, why, and what it cost will be the only ones allowed to run unattended for paying customers.

## Doctrine
Every loop run must emit a machine-checkable receipt (inputs, decision, model used, verifier result, cost) before its output counts; unreceipted work is treated as a draft, never as done.

## Proof Artifact
A loop_receipt.json schema plus a tiny verifier script that gates loop outputs: it checks the receipt exists, the claimed artifact path exists, a verifier ran, and the model/route decision was logged with the observed reason, then writes pass/fail to a receipts ledger.

Next action: Create /home/agentshadow/.cache/shadow/bare_context/loop_receipt.schema.json and verify_receipt.py, then run verify_receipt.py against post_output.json in the same directory to produce the first receipt entry in receipts.jsonl.

## Public Angle
Markdown repos with zero runtime code are getting starred because prompts are cheap to share. Receipts are not. I'm publishing my agent's run receipts for a week: what it did, what it verified, what it cost. Judge the loop, not the prompt.

## Buyer Offer
A $99/month 'Agent Receipts' audit feed for small teams running unattended agents (Claude Code, OpenClaw, AutoAgent-style loops): Shadow ingests their run logs, produces daily receipts with pass/fail verification and cost per outcome, and flags runs that changed things without evidence.

## Source Signals
- Alex Prompter on X: &quot;Some of the most starred repos on GitHub right now contain zero runtime code. They&#x27;re markdown files, skill configs, and prompt c
- Andrej Karpathy Releases Document on AI Agent Architecture Replacing Manual Prompting with Self-Improving Loops / X Trending Log in Sign up Trending Andrej Karp
- Andrej Karpathy on X: &quot;https://t.co/Lb6T42n5jl&quot; / X Post Log in Sign up Post Andrej Karpathy @karpathy 2025 LLM Year in Review 2025 has been a strong
- Ronin on X: &quot;Do you understand what just got open sourced??? an agent that improves other agents. autonomously. NO human in the loop [ literally how it hel
- Karpathy&#x27;s LLM Knowledge Bases Turn Raw Files into Evolving Wikis / X Trending Log in Sign up Trending Karpathy&#x27;s LLM Knowledge Bases Turn Raw Files i

## Scale Packets
- proof_artifact: promoted (2bda7fdb7038)
- public_wedge: promoted (0e6f1c1072b8)
- buyer_experiment: promoted (2813df01cbd1)
- operator_doctrine: promoted (3023da44f84f)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (2bda7fdb7038)
- public_wedge: queued_echo_draft (0e6f1c1072b8)
- buyer_experiment: queued_buyer_experiment (2813df01cbd1)
- operator_doctrine: already_persisted (3023da44f84f)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
