# Frontier Artifact Pack

Generated: 2026-08-24T08:20:11.525213+00:00

## Thesis
Subagent hierarchies are being sold as team-org charts, but the real scarcity is not delegation depth — it's the receipt layer that proves a delegated run actually changed state, so the winning runtime is the one that can refuse to report success without evidence.

## Doctrine
No loop output counts as delivered unless it carries a verifiable receipt: a file path, a diff, a URL, or an external side effect. Narrative summaries are logged as attempts, not outcomes, and attempts do not earn budget in the portfolio allocator.

## Proof Artifact
`receipts.py` — a shared verifier module every Shadow loop calls before writing its outcome record. It takes a claimed outcome plus a list of evidence pointers, verifies each pointer resolves (file exists and mtime is within the run window, URL returns 2xx, or command exit code is 0), and writes `receipts/<loop>/<run_id>.json` with `{status: verified|unverified, evidence[], claim}`. Unverified runs get status downgraded automatically and are excluded from the loop's success rate.

Next action: Write `receipts.py` into the Shadow repo with the verify function and JSON writer, then retrofit the single highest-frequency existing loop to call it and emit its first receipt file, so tomorrow's run produces real verified/unverified counts.

## Public Angle
Everyone's shipping agent org charts. Nobody's shipping agent receipts. My loops can't tell me they succeeded — they have to show me the file they touched, or the run gets logged as a miss. Here's what a week of that looks like.

## Buyer Offer
"Receipted automation" for small operators already running AI workflows: a fixed monthly retainer where every automated run ships a machine-checkable receipt instead of a Slack summary — priced at $99–$149/mo, sold on the pain of not knowing whether your agents actually did anything last week.

## Source Signals
- Subagents | Cursor Docs Skip to main content Cursor Logo Docs API Learn Help Search docs... ⌘K Sign in Download Command Palette Search for a command to run... G
- Andrej Karpathy on X: &quot;I packaged up the &quot;autoresearch&quot; project into a new self-contained minimal repo if people would like to play over the week
- Minsi.AI on X: &quot;OpenAI 编程助手 Codex 0.105.0 刚上线。 被不少用户称为史上最大单次更新。 最炸的一个点：语音听写进终端 在终端里按住空格键直接说话。 Codex 实时把语音转成指令。 写代码第一次有点“对着电脑说话就能干活”的感觉了。 更关键的是：子代理系统全面重构 AI

## Scale Packets
- proof_artifact: promoted (2e9b92f0451a)
- public_wedge: promoted (c8240e2e22fd)
- buyer_experiment: promoted (4d98ae46cb9f)
- operator_doctrine: promoted (b5df92de25ff)

## Latest Promotions
- proof_artifact: delegated_to_improvement_queue (2e9b92f0451a)
- public_wedge: queued_echo_draft (c8240e2e22fd)
- buyer_experiment: queued_buyer_experiment (4d98ae46cb9f)
- operator_doctrine: already_persisted (b5df92de25ff)

## Receipts
- State: `state/revenue/frontier_artifact_pack.json`
- Markdown: `docs/frontier-artifact-pack.md`
- Public HTML: `docs/frontier-artifact-pack.html`
- Public JSON: `docs/frontier-artifact-pack.json`
- Current synthesis: `state/frontier_compound_current.json`
- Flywheel: `state/revenue/frontier_scale_flywheel.json`
- Execution ledger: `state/revenue/frontier_scale_execution.jsonl`
