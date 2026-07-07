# Contract Install Blueprint

A buyer should be able to see the before/after diff behind Shadow's $2,000 Contract Install before the first call: observed failure, installed gate, forced after-state, regression test, and CTA.

Generated: 2026-07-07T09:01:22.064423+00:00
Source model: `claude-fable-5`
Runtime contracts: 163
Violation rows scanned: 4384

## Conversion Path

- Free-triage entries route one real failure trace to the intake page.
- Census entries route seven days of traces to a $400 failure census.
- Install entries route one production workflow to a $2,000 deterministic contract install.
- Retainer path is governed operations after the first workflow has receipt-backed controls.

## Blueprints

### cib-001 · action-deferral-guard

- Failure mode: FM-011 — Deferral Instead of Execution
- Gate type: post
- Trigger: Outbound response contains proposal phrases such as 'want me to', 'should I', or 'shall I' while standing authority covers the action.
- Observed fires: 117
- Install estimate: 3.0h
- Tier: free-triage
- CTA: [Diagnose one failure free](https://impartshadow.github.io/echo-site/failure-intake.html)

```text
if standing_authority_applies(turn) and proposal_phrase(response):
    block(response)
    inject('execute directly; remove permission-seeking')
    regenerate()
```

### cib-002 · commit-hash-verification

- Failure mode: FM-027 — Fabricated Completion Claims
- Gate type: post
- Trigger: Outbound completion language contains a hex commit token near words like commit, pushed, shipped, landed, SHA, or HEAD.
- Observed fires: 92
- Install estimate: 2.0h
- Tier: census
- CTA: [Request the $400 failure census](mailto:impartshadow@gmail.com?subject=Census:%20cib-002)

```text
for sha in commit_like_tokens(response):
    if git_cat_file(sha) != 'commit':
        block(response)
        require('rerun git rev-parse HEAD or remove receipt')
```

### cib-003 · stale-state-assertion-guard

- Failure mode: FM-022 — Claims Without Same-Turn Verification
- Gate type: post
- Trigger: Definitive state language appears in a status answer without a same-turn file, process, API, or browser read in the trace.
- Observed fires: 61
- Install estimate: 5.0h
- Tier: install
- CTA: [Scope the $2,000 contract install](mailto:impartshadow@gmail.com?subject=Contract%20Install:%20cib-003)

```text
if definitive_state_claim(response):
    if not same_turn_evidence(trace):
        warn_or_block(response)
        require('read authoritative state before claiming')
```

### cib-004 · partial-evidence-flag

- Failure mode: FM-026 — Thin Evidence With Definitive Framing
- Gate type: post
- Trigger: A numerical, revenue, subscriber, or public-platform claim appears without an explicit source citation or live check.
- Observed fires: 474
- Install estimate: 4.0h
- Tier: census
- CTA: [Request the $400 failure census](mailto:impartshadow@gmail.com?subject=Census:%20cib-004)

```text
if factual_claim(response) and evidence_count(response) < threshold:
    require_source_or_hedge(response)
    downgrade_confidence_or_block()
```

### cib-005 · dox-guard

- Failure mode: FM-023 — Personal Data Egress
- Gate type: pre
- Trigger: Outbound shell, email, browser, or API action contains protected personal identifiers or unsanctioned recipient data.
- Observed fires: 112
- Install estimate: 6.0h
- Tier: install
- CTA: [Scope the $2,000 contract install](mailto:impartshadow@gmail.com?subject=Contract%20Install:%20cib-005)

```text
if outbound_tool(tool) and contains_protected_identifier(payload):
    block(tool_call)
    route_to_sanitized_client_or_redact()
```

### cib-006 · platform-action-precheck

- Failure mode: FM-012 — Manual Handoff Before Automation
- Gate type: pre
- Trigger: A response includes manual UI instructions for email, calendar, publishing, browser auth, or deploy checks with no programmatic attempt in the turn.
- Observed fires: 110
- Install estimate: 3.5h
- Tier: free-triage
- CTA: [Diagnose one failure free](https://impartshadow.github.io/echo-site/failure-intake.html)

```text
if manual_instruction(response) and platform_tool_available(context):
    block(response)
    require('attempt automation path before handoff')
```

## Before / After: Installed Contract Packet

This is the shape of the $2,000 deliverable: one production workflow, the observed failure before the install, the deterministic gate, the after behavior, and the regression test.

- the observed failure before the install
- the exact deterministic contract added
- the after behavior the agent is forced into
- the regression test proving the bad path blocks
- the implementation diff, acceptance criteria, and rollout plan

### ba-commit-receipt · commit-hash-verification

Sample workflow: agent completion report after a git push to main · FM-027 · 92 observed fires.

Buyer pain: The operator cannot tell whether the shipped commit exists without auditing the repo manually.

| Phase | Behavior | Outcome |
|---|---|---|
| before | agent reports 'Pushed fix as `28404c9`' — hash reconstructed from memory, not from git output | operator acts on a receipt that does not resolve; trust burns on the next audit |
| after | post-check resolves every cited sha with `git cat-file -t`; unresolvable hash blocks the response | only literal `git rev-parse HEAD` output ships; every receipt is one-command verifiable |

- Trigger: outbound completion language contains a hex commit token near words like commit, pushed, shipped, landed, SHA, or HEAD
- Precondition: every cited commit token must resolve via `git cat-file -t <sha>` == 'commit' in the repo the receipt names
- Block behavior: response is blocked; agent must rerun `git rev-parse HEAD` and paste literal stdout, or remove the receipt claim
- Regression test: `tests/test_contracts.py::TestCommitHashVerificationContract`
- Receipt boundary: A completion claim is not allowed to leave the agent until the cited commit resolves in the named repository.
- Installed artifacts:
  - post-send contract that extracts commit-like tokens from completion claims
  - same-repo git resolver for each cited token
  - regression test proving fabricated hashes block before the operator sees them
- Implementation diff:
  - add a post-response verifier around completion messages
  - extract repo-scoped commit tokens before the message is emitted
  - block or rewrite any receipt that cannot be resolved by the local git backend
- Acceptance criteria:
  - fabricated commit ids are never visible to the operator
  - valid commit ids pass only after an independent git lookup
  - completion reports name the command or artifact that produced the receipt
- Rollout plan:
  - run in warn mode against seven days of historical traces
  - promote to block mode for completion-report surfaces
  - review false positives after 48 hours and narrow token extraction if needed
- [Scope the $2,000 contract install](mailto:impartshadow@gmail.com?subject=Contract%20Install:%20cib-002)

### ba-state-receipt · stale-state-assertion-guard

Sample workflow: status answer about whether a bot, queue, publish job, or external account is working · FM-022 · 61 observed fires.

Buyer pain: Leadership hears a confident status answer that came from stale context, not the system of record.

| Phase | Behavior | Outcome |
|---|---|---|
| before | agent says 'the bot is running' from session memory | operator discovers later that the process was stale, crashed, or never restarted |
| after | agent must read `ps`, service logs, state ledger, or platform API before asserting status | answer includes a current receipt or explicitly says the live check failed |

- Trigger: definitive state language appears in a factual status answer
- Precondition: the same turn must include a read from the authoritative file, process, API, browser, or ledger
- Block behavior: answer is blocked or downgraded until the agent performs a current read and cites the receipt
- Regression test: `tests/test_contracts.py::TestStateAssertionGroundingContract`
- Receipt boundary: A live-state answer must carry a same-turn read from the system of record or explicitly say the check did not succeed.
- Installed artifacts:
  - state-claim detector keyed to live operational nouns
  - evidence trace check for same-turn reads
  - status-answer template that names the receipt instead of relying on memory
- Implementation diff:
  - classify status answers that name live operational state
  - require same-turn reads from configured authoritative sources
  - downgrade unsupported claims to uncertainty or block them before send
- Acceptance criteria:
  - status answers cite a current process, file, API, browser, or ledger receipt
  - stale memory alone cannot produce 'running', 'sent', 'live', or 'verified'
  - failed checks produce a precise failure result instead of a confident status claim
- Rollout plan:
  - map each workflow noun to an authoritative source
  - run warn mode until source coverage is complete
  - promote high-blast status classes to block mode
- [Scope the $2,000 contract install](mailto:impartshadow@gmail.com?subject=Contract%20Install:%20cib-003)

### ba-platform-action · platform-action-precheck

Sample workflow: agent tells an operator how to send, publish, deploy, or inspect a platform manually · FM-012 · 110 observed fires.

Buyer pain: The agent hands work back to humans while the tool/API path was available.

| Phase | Behavior | Outcome |
|---|---|---|
| before | agent replies with UI steps: 'go to the dashboard and click publish' | operator becomes the automation layer; the agent preserves no execution receipt |
| after | agent attempts the sanctioned tool path and reports the real API/browser/shell result | manual work appears only after a logged failed attempt or a hard blocker |

- Trigger: manual UI instructions for an action class with an available programmatic path
- Precondition: agent must attempt the API, MCP, browser, shell, or sanctioned automation path first
- Block behavior: manual handoff is blocked unless the attempted programmatic path produced a documented failure
- Regression test: `tests/test_contracts.py::TestPlatformActionPrecheckContract`
- Receipt boundary: A manual instruction cannot leave the agent until the sanctioned automation path has produced a receipt or a hard blocker.
- Installed artifacts:
  - action-class router for email, calendar, publishing, browser, and deploy checks
  - tool-attempt receipt requirement before any manual escalation
  - allowlist for auth, legal, spend, and irreversible high-blast blockers
- Implementation diff:
  - detect manual handoff language for platform action classes
  - route eligible actions to sanctioned API, MCP, browser, shell, or deploy tools
  - allow manual escalation only after a logged attempt or hard-blocker match
- Acceptance criteria:
  - available automation paths are attempted before UI instructions appear
  - manual handoffs include the failed tool result or hard-blocker class
  - authorized low-risk actions produce execution receipts instead of homework
- Rollout plan:
  - start with email, calendar, publishing, browser, and deploy checks
  - log attempted path, result, and blocker class for each escalation
  - expand action classes only after the first workflow stabilizes
- [Scope the $2,000 contract install](mailto:impartshadow@gmail.com?subject=Contract%20Install:%20cib-006)

### Machine Contract Anchor

- Primary trigger: outbound completion language contains a hex commit token near words like commit, pushed, shipped, landed, SHA, or HEAD
- Primary precondition: every cited commit token must resolve via `git cat-file -t <sha>` == 'commit' in the repo the receipt names
- Primary block behavior: response is blocked; agent must rerun `git rev-parse HEAD` and paste literal stdout, or remove the receipt claim
- Primary regression test: `tests/test_contracts.py::TestCommitHashVerificationContract`

## What Not To Build

- No new runtime contracts in this artifact.
- No all-107-contract dump; use installable gates with observed evidence.
- No interactive configurator; static JSON, HTML, and Markdown are enough.
- No buyer-specific customization in public; customization is the paid product.
- No new distribution apparatus; route through existing intake and proof surfaces.
- No direct Stripe links.
