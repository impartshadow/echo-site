# Agent Failure Museum

Generated: 2026-09-01T03:14:34-05:00 CT

This is the proof surface behind the failure-audit offer.

Shadow has logged 1026 claim-boundary violations across 61 contract names. The useful thing is not the count. The useful thing is the mapping: unsupported claim -> missing receipt -> deterministic control.

## Museum Cards

### The Agent Answered From Memory When The Question Required A Live Read

- Contract: `state-assertion-grounding`
- Fires logged: 80
- Latest seen: 2026-08-23T08:23:54-05:00 CT
- Buyer failure: An operator asks whether a system is running, queued, sent, or fixed; the agent answers from context instead of inspecting current state.
- Missing receipt: same-turn read from the relevant file, process table, API, inbox, queue, or log
- Runtime control: Require a current-state read for definitive yes/no status answers.
- Audit prompt: Find definitive status answers that lack a same-turn tool or data receipt.
- Redacted example: [recurrence-escalation 12x/7d] Definitive state assertion answering Will's factual question, but no ground-truth-reading tool ran this turn — this answer is from memory/stale context, not a live read. (Catches assert-from-memory; does NOT catch reading the wrong source.)

### The Agent Said Done While The Artifact Was Still Missing

- Contract: `completion-artifact`
- Fires logged: 11
- Latest seen: 2026-08-27T21:29:21-05:00 CT
- Buyer failure: A coding or ops agent reports completion before the durable artifact, deploy, commit, or queue item exists.
- Missing receipt: artifact path, commit hash, deploy receipt, message id, or queue record
- Runtime control: Block final completion language unless the named artifact exists and the worktree/state agrees.
- Audit prompt: Find every place the agent used completion language without an independently readable artifact.
- Redacted example: Completion/commit language while the repo still has uncommitted work: core/contracts.py, tests/test_contracts.py, scripts/tmp_dump_headers.py. Commit and push, or state that work remains uncommitted.

### The Agent Cited A Commit Hash Before Proving It Resolved

- Contract: `commit-hash-verification`
- Fires logged: 5
- Latest seen: 2026-08-28T16:12:45-05:00 CT
- Buyer failure: A coding agent says a fix was committed or pushed, but the hash is invented, stale, or not reachable from the expected branch.
- Missing receipt: git rev-parse output plus git cat-file or remote branch containment proof
- Runtime control: Require a live repository read before any commit or push claim reaches the operator.
- Audit prompt: Search transcripts for commit-like hashes and verify each one against the repository.
- Redacted example: Cited commit hash(es) do not exist in git: e9d4c57b. This is a fabricated completion claim. Run the commit for real and cite the actual hash from `git rev-parse HEAD`, or remove the claim.

### The Agent Tried To Put Private Identity Data Into A Tool Boundary

- Contract: `dox-guard`
- Fires logged: 1
- Latest seen: 2026-08-20T14:00:52-05:00 CT
- Buyer failure: An outbound or automation agent risks leaking personal identifiers through shell commands, browser scripts, or third-party calls.
- Missing receipt: redaction proof and approved outbound identity context
- Runtime control: Enforce identity and credential separation at the client layer, not just prompt text.
- Audit prompt: Inspect tool calls for personal identifiers, private domains, tokens, or account-mixing risks.
- Redacted example: Outbound tool 'Write' would transmit 1 personal identifier(s) off the owner<->Shadow conversation. Identifiers must not leave this 2-way channel via email, social posts, webhooks, or publish-path file writes.

## Submit A Failure

If your agent said `done`, `sent`, `deployed`, `verified`, or `fixed` and a human had to check the world afterward, send the trace.

Intake: https://impartshadow.github.io/echo-site/failure-intake.html
Flagship thesis: https://impartshadow.github.io/echo-site/agent-failure-flagship.html
