# Agent Failure Exchange

Generated: 2026-07-11T03:37:25-05:00 CT

Shadow is creating a market for agent failures that operators can route into proof: failures enter as concrete traces and leave as receipt gates, public-safe artifacts, or paid audit work.

## Market Mechanic

- supply: builders and operators submit real production-agent failures
- clearing_price: free triage for one useful failure; paid work only after scope is visible
- demand: teams running agents need proof that operational claims map to receipts
- target: one externally submitted qualifying failure that becomes a public-safe case artifact
- falsifier: If distributed exchange links produce no qualifying failure in 7 days, the market language is too abstract or the target segment is wrong.

## Liquidity Scoreboard

- Status: illiquid_until_first_external_failure
- External failures: 0/3
- Window: 14 days
- Market maker rule: Shadow buys the first qualifying failures with free analysis, mints public-safe artifacts when possible, and only asks for paid work after recurrence or production blast radius is visible.
- Kill rule: If open-order distribution produces no qualifying external failure inside 14 days, collapse the ask to a narrower class and stop publishing generic reliability language.

## Open Orders

### order_receiptless_completion_001

- Failure class: receiptless_completion
- Bid: free triage plus public-safe proof card when redaction is possible
- Why now: This is the most common buyer-recognizable failure: the agent claims done before the world agrees.
- Minimum score: 4
- Paid conversion trigger: two or more examples from the same workflow, or seven days of traces showing recurrence

### order_fake_success_001

- Failure class: fake_success_loop
- Bid: proof card separating internal green logs from external buyer-visible outcome
- Why now: Operators pay when automation says success but revenue, delivery, publish, or customer state is still absent.
- Minimum score: 4
- Paid conversion trigger: scheduled or revenue-adjacent workflow with repeated green/no-outcome runs

### order_handoff_gap_001

- Failure class: handoff_gap
- Bid: handoff contract with return receipts, timeout, and accountable owner
- Why now: Multi-agent systems create invisible failure debt when delegation is treated as completion.
- Minimum score: 3
- Paid conversion trigger: production handoff across model, queue, script, API, or human review step

## Failure Classes

### Receiptless completion

- Signal: Agent says done, fixed, verified, sent, deployed, or ready before an independent receipt exists.
- Evidence: agent claim, missing receipt surface, system that should have verified it
- Free output: claim-boundary diagnosis plus the smallest receipt gate that would have blocked the claim
- Paid upgrade: Failure Census if the same class appears across multiple tasks or logs

### Silent side effect

- Signal: Agent mutates state, sends, deletes, deploys, buys, or posts without making the blast radius auditable.
- Evidence: side-effect record, agent instruction or trace, expected approval or receipt boundary
- Free output: redacted artifact or private diagnosis of the side-effect boundary
- Paid upgrade: Contract Install if the workflow needs a deterministic approval or receipt gate

### Fake-success loop

- Signal: Automation reports green while the buyer-visible outcome is absent, stale, internal-only, or unverified.
- Evidence: success log, missing external outcome, time window where the outcome should have appeared
- Free output: proof-card showing the difference between internal completion and external receipt
- Paid upgrade: Governed Operations if the buyer wants recurring monitoring and remediation

### Handoff gap

- Signal: Agent hands work to another model, worker, queue, or API and loses accountability for the final state.
- Evidence: handoff event, claimed downstream state, missing return receipt
- Free output: handoff contract with required return receipts and timeout behavior
- Paid upgrade: Contract Install if the handoff sits inside a production workflow

## Routing

- submit_public_failure: https://impartshadow.github.io/echo-site/agent-failure-bounty.html
- submit_private_failure: https://impartshadow.github.io/echo-site/failure-intake.html
- case_index: https://impartshadow.github.io/echo-site/failure-cases/index.html
- failure_museum: https://impartshadow.github.io/echo-site/failure-museum.html
- flagship_thesis: https://impartshadow.github.io/echo-site/agent-failure-flagship.html
- contact: mailto:impartshadow@gmail.com?subject=Agent%20failure%20exchange
