# Write a clear task brief

A useful brief gives the agent a finish line and the facts that shape it. Leave routine implementation choices to the agent; spell out decisions that would change the product or widen the work.

## Include what changes the answer

1. **Outcome:** what a person should be able to do when the task is finished.
2. **Current behavior:** what happens today and how to reproduce the problem.
3. **Sources:** where the approved requirements and relevant code live.
4. **Scope:** what may change, what must stay, and where the work should be delivered.
5. **Evidence:** which results would prove the outcome, including realistic failures.
6. **Limits:** any spending, access, publication or destructive-action boundaries.

Ask the agent to inspect the project before proposing a solution. A screenshot shows appearance; it does not prove that an interaction works. A file name suggests a purpose; it does not establish what the code does.

## Example brief

```text
Help people retry a failed search without losing the results they already have.

Read the project's instructions and approved search requirements first. Inspect
the current search flow and reproduce the failure before changing it.

While a new search loads, keep the last successful results visible and show
that an update is in progress. If the request fails, retain those results,
explain the failure and provide a retry action. Never show results from a
different signed-in account. An older response must not replace a newer one.

Use the project's existing controls and visual treatment. Keep unrelated
search features outside this task. Ask before changing an unresolved product
decision; continue any work that does not depend on that answer.

Verify slow requests, failed requests, rapid changes, retry, account changes,
and keyboard use. Show evidence from the running app and describe any paths
you could not test.

Deliver a local working change for review. Do not publish, deploy, spend money
or change access permissions. Report the changed behavior, evidence and any
remaining limits when finished.
```

Replace the delivery boundary with the permission you actually intend to give. A request to review should stay a review; a request to ship needs an agreed destination and a way to verify it.

## When the brief needs a question

Ask when two reasonable readings would produce different outcomes. Resolve facts from the project when possible. Do not turn a routine coding choice into a product question, or quietly treat an unanswered product question as approval.
