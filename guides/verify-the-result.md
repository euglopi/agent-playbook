# Verify the result

A change is finished when it works in the place and role the task requires. A successful code check, a merged change and a working live feature are different milestones.

## Match the evidence to the promise

| Promise | Useful evidence |
| --- | --- |
| A calculation is correct | Known inputs and expected results, including boundaries |
| A bug is fixed | The original failure reproduced, then the same case passing |
| A control works | The real interaction exercised in the running app |
| An error can be recovered from | A failed action followed by a successful retry without losing work |
| A change is live | The intended address shows and performs the new behavior |
| Access stays private | The relevant account and permission boundaries exercised |

Use focused checks that could catch a real mistake. A test that repeats the implementation without an independent expected result adds little confidence.

## Follow the full path

Start where a person starts. Enter realistic information, take the intended action, and inspect the result. Include the next step: saving is not enough if the saved item cannot be reopened.

For a visible change, inspect the actual rendered screen at the sizes the product supports. Try keyboard use, long text, loading, failure and recovery where they apply. A still image cannot establish those behaviors.

For data or access changes, use a safe test account or a scoped record. A check must not send real messages, spend money or destroy data without authorization. Prepare a real recovery path before overwriting important information.

## Check the cause and its other uses

When a shared function or assumption caused the bug, find its other uses. Separate a demonstrated defect from a possible exposure. Fix within the agreed scope and explain any wider work that needs a separate decision.

## Close with an honest result

Say what now works, where it works, and what evidence supports it. Name anything unfinished and who owns the next step. Do not call a preview live, a passing test a complete user journey, or a saved plan a running task.

Keep detailed evidence with the task so another person can reproduce the result. Save the lesson in the project rule or guide that owns it when it will help prevent the same failure.
