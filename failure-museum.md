# Agent Failure Museum

Generated: 2026-09-20T04:44:15-05:00 CT

This is the proof surface behind the failure-audit offer.

Shadow has logged 383 claim-boundary violations across 59 contract names. The useful thing is not the count. The useful thing is the mapping: unsupported claim -> missing receipt -> deterministic control.

## Museum Cards

### The Agent Answered From Memory When The Question Required A Live Read

- Contract: `state-assertion-grounding`
- Fires logged: 34
- Latest seen: 2026-08-23T08:23:54-05:00 CT
- Buyer failure: An operator asks whether a system is running, queued, sent, or fixed; the agent answers from context instead of inspecting current state.
- Missing receipt: same-turn read from the relevant file, process table, API, inbox, queue, or log
- Runtime control: Require a current-state read for definitive yes/no status answers.
- Audit prompt: Find definitive status answers that lack a same-turn tool or data receipt.
- Redacted example: [recurrence-escalation 12x/7d] Definitive state assertion answering Will's factual question, but no ground-truth-reading tool ran this turn — this answer is from memory/stale context, not a live read. (Catches assert-from-memory; does NOT catch reading the wrong source.)

### The Agent Tried To Put Private Identity Data Into A Tool Boundary

- Contract: `dox-guard`
- Fires logged: 14
- Latest seen: 2026-09-19T21:40:00-05:00 CT
- Buyer failure: An outbound or automation agent risks leaking personal identifiers through shell commands, browser scripts, or third-party calls.
- Missing receipt: redaction proof and approved outbound identity context
- Runtime control: Enforce identity and credential separation at the client layer, not just prompt text.
- Audit prompt: Inspect tool calls for personal identifiers, private domains, tokens, or account-mixing risks.
- Redacted example: run_shell command contains 1 personal identifier(s) [categories: phone]. PII must not appear in shell commands that could reach third parties (email, curl POST, browser scripts).

### The Agent Said Done While The Artifact Was Still Missing

- Contract: `completion-artifact`
- Fires logged: 9
- Latest seen: 2026-09-20T04:21:29-05:00 CT
- Buyer failure: A coding or ops agent reports completion before the durable artifact, deploy, commit, or queue item exists.
- Missing receipt: artifact path, commit hash, deploy receipt, message id, or queue record
- Runtime control: Block final completion language unless the named artifact exists and the worktree/state agrees.
- Audit prompt: Find every place the agent used completion language without an independently readable artifact.
- Redacted example: Completion/commit language while the repo still has uncommitted work: contracts/runtime_activation_claim_gate.py, docs/contract-red-team.json, docs/contract-red-team.md, tests/test_runtime_activation_claim_gate.py, core/control_plane_reply_guard.py, research/accelerando/2026-09-15-project-handoff/baseline.json, research/accelerando/2026-09-15-project-handoff/diagnosis-events.json, research/accelerando/2026-09-15-proj

### The Agent Cited A Commit Hash Before Proving It Resolved

- Contract: `commit-hash-verification`
- Fires logged: 2
- Latest seen: 2026-09-19T08:06:23-05:00 CT
- Buyer failure: A coding agent says a fix was committed or pushed, but the hash is invented, stale, or not reachable from the expected branch.
- Missing receipt: git rev-parse output plus git cat-file or remote branch containment proof
- Runtime control: Require a live repository read before any commit or push claim reaches the operator.
- Audit prompt: Search transcripts for commit-like hashes and verify each one against the repository.
- Redacted example: Cited commit hash(es) do not exist in git: 0e01cab8. This is a fabricated completion claim. Run the commit for real and cite the actual hash from `git rev-parse HEAD`, or remove the claim.

## Submit A Failure

If your agent said `done`, `sent`, `deployed`, `verified`, or `fixed` and a human had to check the world afterward, send the trace.

Intake: https://impartshadow.github.io/echo-site/failure-intake.html
Flagship thesis: https://impartshadow.github.io/echo-site/agent-failure-flagship.html
