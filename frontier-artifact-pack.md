# Frontier Artifact Pack

Generated: 2026-08-13T08:10:10.487238+00:00

## Thesis
Everyone is shipping agents that do more work autonomously; almost no one is shipping the receipts layer that lets a buyer trust an agent enough to pay it monthly — trust infrastructure, not capability, is the actual bottleneck to agent revenue.

## Doctrine
Every autonomous run must emit a verifiable receipt (inputs, decisions, evidence, cost) as a first-class artifact; capability without an audit trail is a demo, capability with one is a product.

## Proof Artifact
A run-receipt spec and generator: a script that wraps any Shadow loop execution and emits a signed JSON+markdown receipt (goal, actions taken, evidence links, tokens/cost, outcome delta) suitable for sending to a paying client as proof-of-work.

Next action: Create ~/.cache/shadow/receipts/receipt_schema.json and a wrapper script shadow_receipt.sh that captures loop name, timestamp, actions, and outputs into a per-run receipt file, then retrofit it onto the next scheduled loop execution.

## Public Angle
AWS just told you agents will work for days without intervention. Nobody asked the obvious question: when it's done, how do you know what it actually did? We've been running autonomous loops for months — the unlock wasn't longer autonomy, it was receipts. Post the schema.

## Buyer Offer
A $99/month 'autonomous ops with receipts' retainer: Shadow runs a recurring operational task (monitoring, triage, reporting) for a small team and delivers weekly receipts proving what ran, what it found, and what it cost — pitched at teams burned by black-box AI tools like the AWS frontier agents they can't audit.

## Source Signals
- Ronin on X: &quot;Do you understand what just got open sourced??? an agent that improves other agents. autonomously. NO human in the loop [ literally how it hel
- Arc — AI-forward coordination substrate ΛRC AI-forward coordination substrate Docs, Stories, Tasks, Status is a byproduct of Intent . click to copy curl -fsSL h
- Amazon launches frontier AI agents that work autonomously like teammates News AWS AWS unveils frontier agents, a new class of AI agents that work as an extensio
- J.B. on X: &quot;&amp;gt; be openai &amp;gt; hire thousands of engineers &amp;gt; build AI that codes &amp;gt; AI gets good at coding &amp;gt; give AI the abili
- Rohan Paul on X: &quot;The prompt era is ending. That&#x27;s too linear, too bottlenecked by humans. We are entering the loop machine of AI agents. The value is

## Scale Packets
- proof_artifact: promoted (a61aceb30cd3)
- public_wedge: promoted (6489c1ef7b1c)
- buyer_experiment: promoted (9cd8acec08de)
- operator_doctrine: promoted (32cef08393a0)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (a61aceb30cd3)
- public_wedge: queued_echo_draft (6489c1ef7b1c)
- buyer_experiment: queued_buyer_experiment (9cd8acec08de)
- operator_doctrine: already_persisted (32cef08393a0)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
