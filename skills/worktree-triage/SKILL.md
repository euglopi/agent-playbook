---
name: worktree-triage
description: Review local working folders and branches, find unfinished or unbacked-up work, identify owners and preview holds, and recommend safe completion or cleanup using the project's supported lifecycle tools. Use on demand or when starting or finishing related work.
---

# Worktree triage

## Purpose and boundaries

Find what needs preserving, finishing, holding or releasing. Run locally: remote
pull requests cannot reveal uncommitted files, unpushed commits or local previews.
This is an on-demand review skill, not a scheduler or authority to delete folders.

Free local programs may produce a daily inventory, save recovery copies and retry
explicitly approved cleanup. Those checks do not replace the owner decision.
Recurring AI reviews or other paid recurring work require separate authorization;
this skill does not create them.

Read the project's agent instructions and owning lifecycle guide before choosing
commands. Check OPEN observations tagged `worktree-triage` in the available
observation log. Preserve explicit review, preview and publication holds.

## Gather the evidence

1. Prefer the project's installed **read-only inventory or inspect command**.
   Confirm its repository identity, installation profile and freshness. Distinct
   projects may use separate profiles and private state. A folder admitted
   to one profile is not admitted to another. Read the installed policy for exact
   allowed external paths and protected previews; never broaden it to a naming
   wildcard during review.
2. Reconcile inventory against the host's live task list and relevant task history.
   Record the exact owner title and ID, current activity, completed delivery,
   acceptance status and any explicit hold or release. A partial task list cannot
   prove the owner is gone. A stopped chat, absent process or old timestamp cannot
   prove abandonment. If ownership is unresolved, retain the folder with that
   specific uncertainty.
3. Include the shared checkout, external linked folders, detached folders, native
   app folders and missing registrations in the inventory. Distinguish where a
   folder lives from which repository owns it. A path or branch name alone proves
   neither owner nor completion.
4. Inspect modified tracked files, untracked files, unpushed commits and required
   ignored files. Do not discard a file merely because its name looks generated.
   Separate reproducible dependencies from source, private inputs and review
   artifacts. Confirm recovery exists before calling local work protected.
5. Identify previews and other users of each folder, including saved service
   configurations. A preview hold persists while its process is stopped. Preserve
   its original address and serving checkout until its owner releases that need.
6. Refresh the actual integration reference before comparing committed work.
   Establish the project's integration branch rather than assuming `main`.
   Map open and merged pull requests to their exact head commit and account for
   truncated result lists. If fresh remote evidence is unavailable, mark the
   comparison stale and retain affected folders.

If installed inventory is unavailable, use read-only Git inspection as a fallback:
`git worktree list --porcelain -z`, per-folder `git status --porcelain=v1 -z
--untracked-files=all`, and branch/ref inspection. Parse NUL-separated output with
path-safe code, not whitespace splitting. Record errors as unknowns rather than
zero changes. Missing setup does not authorize improvised removal.

## Distinguish saved work from work already included

Ahead/behind counts are clues about commits, not permission to remove anything.
A branch with `ahead=0` has no commits outside the compared integration history,
but its folder may hold unsaved files, ignored inputs or an active preview.
Being behind alone is not a reason to update an otherwise unused checkout.

A squash merge combines several commits into 1 new commit. The original branch
may therefore remain ahead, fail an ancestry check, and show `git cherry` plus
signs even when its changes reached the integration branch. Conversely, a merged
pull request does not prove later commits on that branch have landed.

Use the pull request's exact merged head and the current integration history as
landing evidence. For uncertain branches, inspect the changes they authored from
the merge base, then compare those specific files with the integration branch and
trace their later history. Raw file or added/deleted-line counts cannot tell
superseded work from missing behavior. A nonempty difference deserves reading;
an empty difference describes tracked content only. Preserve untracked material,
ownership and previews independently of this comparison.

Do not force-delete a branch to bypass a failed ancestry check. Do not treat a
content comparison as a substitute for delivery, acceptance and owner release.
The installed guarded helper owns the exact proof required for external cleanup.

## Reach an owner decision

Give every reviewed folder a concrete next step:

- **Unfinished or uncertain:** name the work, owner and missing evidence. Keep the
  folder and record a specific hold, including for dirty or unmerged work.
- **Delivery or review still open:** retain the folder with the exact remaining
  check, preview or approval. Merged code is not completed acceptance.
- **Delivered and accepted:** keep the folder and local branch for follow-up,
  with no automatic expiry. Record a retention hold. Only the user's explicit cleanup
  request for the folder or an approved batch permits an owner release; completion
  alone does not. All owners must release a shared folder before removal.
- **Already released:** report whether the guarded helper completed removal or
  which safety check still keeps the folder. Do not work around that check.

A review of another owner's folder does not authorize acting as that owner. Resolve
ownership through the host and existing user authorization. For the current task's
own authorized work, record the hold through supported tools. Record a release
only within an explicit user cleanup request, without asking to repeat that request. Registration or resumed work must revoke an
older release before work continues. A hold is not automatic permission to later
release the folder when a timer expires.

## Cleanup and recovery routes

For external folders, use the project's installed guarded lifecycle commands.
They must enforce repository identity, admitted paths, owner decisions, current
landing evidence, preview/process holds and private recovery before removal.
Keep profiles separate. If no supported helper exists, retain the folder and
recommend the missing setup instead of copying an ad hoc deletion loop.

For native Codex folders, use `list_artifacts` and the owning chat's supported
`archive_worktree` action only for user-requested cleanup after delivery and
acceptance. Keep completed folders available until then. Attach only the current
chat's exact managed folder when needed. Preserve required ignored material
privately outside it first. Informational register/hold records do not grant a
script permission to remove a native folder. If the app protects it, retain that
specific hold. Never rewrite native app state or use raw Git removal or pruning
as a replacement for the app's archive action.

An interrupted removal, leftover directory or missing registration goes through
the installed helper's recovery/resume inspection. Do not prune registrations or
delete leftover directories to make an error disappear. Branch deletion likewise
requires its supported, authorized route and recoverable saved state; this skill
contains no bulk deletion command.

## Report and improve

Lead with the recommendation: which work needs completion, which folders remain
held and why, and which explicit releases can use the supported cleanup route.
Name the actual owner, remaining step and recovery evidence. Keep uncertainty
visible; do not label clean, merged, old or ownerless folders disposable.

After a run, correct demonstrated gaps in this skill within authorized scope and
record reusable observations under the project's observation rules. Do not add
new recurring jobs merely to keep the skill exercised.
