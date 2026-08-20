# Agent Failure Museum

Generated: 2026-08-20T03:39:49-05:00 CT

This is the proof surface behind the failure-audit offer.

Shadow has logged 1134 claim-boundary violations across 66 contract names. The useful thing is not the count. The useful thing is the mapping: unsupported claim -> missing receipt -> deterministic control.

## Museum Cards

### The Agent Answered From Memory When The Question Required A Live Read

- Contract: `state-assertion-grounding`
- Fires logged: 133
- Latest seen: 2026-08-17T05:49:57-05:00 CT
- Buyer failure: An operator asks whether a system is running, queued, sent, or fixed; the agent answers from context instead of inspecting current state.
- Missing receipt: same-turn read from the relevant file, process table, API, inbox, queue, or log
- Runtime control: Require a current-state read for definitive yes/no status answers.
- Audit prompt: Find definitive status answers that lack a same-turn tool or data receipt.
- Redacted example: [recurrence-escalation 22x/7d] Opened by agreeing with Will's factual framing with zero ground-truth reads this turn — this is concurrence from memory/deference, not verification.

### The Agent Cited A Commit Hash Before Proving It Resolved

- Contract: `commit-hash-verification`
- Fires logged: 15
- Latest seen: 2026-08-18T01:45:38-05:00 CT
- Buyer failure: A coding agent says a fix was committed or pushed, but the hash is invented, stale, or not reachable from the expected branch.
- Missing receipt: git rev-parse output plus git cat-file or remote branch containment proof
- Runtime control: Require a live repository read before any commit or push claim reaches the operator.
- Audit prompt: Search transcripts for commit-like hashes and verify each one against the repository.
- Redacted example: Cited commit hash(es) do not exist in git: 8d3c005. This is a fabricated completion claim. Run the commit for real and cite the actual hash from `git rev-parse HEAD`, or remove the claim.

### The Agent Said Done While The Artifact Was Still Missing

- Contract: `completion-artifact`
- Fires logged: 11
- Latest seen: 2026-08-18T01:09:36-05:00 CT
- Buyer failure: A coding or ops agent reports completion before the durable artifact, deploy, commit, or queue item exists.
- Missing receipt: artifact path, commit hash, deploy receipt, message id, or queue record
- Runtime control: Block final completion language unless the named artifact exists and the worktree/state agrees.
- Audit prompt: Find every place the agent used completion language without an independently readable artifact.
- Redacted example: Claimed a commit/push without a resolving commit-hash receipt. A real push produces a SHA that `git cat-file -t` can verify. Run it and cite the actual hash from `git rev-parse HEAD`, or remove the claim.

### The Agent Tried To Put Private Identity Data Into A Tool Boundary

- Contract: `dox-guard`
- Fires logged: 1
- Latest seen: 2026-07-28T07:40:14-05:00 CT
- Buyer failure: An outbound or automation agent risks leaking personal identifiers through shell commands, browser scripts, or third-party calls.
- Missing receipt: redaction proof and approved outbound identity context
- Runtime control: Enforce identity and credential separation at the client layer, not just prompt text.
- Audit prompt: Inspect tool calls for personal identifiers, private domains, tokens, or account-mixing risks.
- Redacted example: Outbound tool 'Write' would transmit 3 personal identifier(s) off the owner<->Shadow conversation. Identifiers must not leave this 2-way channel via email, social posts, webhooks, or publish-path file writes.

## Submit A Failure

If your agent said `done`, `sent`, `deployed`, `verified`, or `fixed` and a human had to check the world afterward, send the trace.

Intake: https://impartshadow.github.io/echo-site/failure-intake.html
Flagship thesis: https://impartshadow.github.io/echo-site/agent-failure-flagship.html
