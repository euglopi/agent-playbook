---
name: git-branching-quiz
description: Run a ~5-minute interactive quiz teaching git branching — trunk-based vs dev/staging/production, feature branches, worktrees, releases, hotfixes — when the user says "quiz me on branching", "quiz me on dev/prod/feature branches and worktrees", "branching quiz", or asks to practice git flow. One question at a time, adaptive, grounded in the current project's verified setup.
---

# Git branching quiz

A short interactive quiz for a non-engineer building real software with coding agents.
The goal is understanding the learner can explain to someone else, not vocabulary.
Read the project's branching and contribution guide when available before using real
project facts. Otherwise label the examples below hypothetical.

## How to run it

- **One question at a time**, using the host's clickable-question control when it
  exists (AskUserQuestion), otherwise short numbered options. Never dump all
  questions at once.
- After each answer: say right or wrong in 1 line, then the *why* in 2-3 plain
  sentences, then the next question. Wrong answers are the valuable ones — follow a
  wrong answer with 1 easier question on the same idea before moving on.
- ~8 questions, ~5 minutes. End with a 3-line summary: what the learner got solid, what to
  re-ask next time, and 1 thing to watch for in real work this week.
- Vary the questions between runs; the bank below is a starting set, not a script.
  Keep every question concrete — name real branches, real commands, verified project
  facts — never abstract definitions.

## Establish ground truth before the quiz

- Verify whether the project is **trunk-based**: 1 permanent branch (often `main`),
  short feature branches and reviewed merges back. Check whether merging deploys
  automatically, requires a separate release, or has no deployment at all. Never
  present the example as the project's live setup without that evidence.
- The **dev/staging/production reference model**: 3 permanent branches mirroring 3
  deployed environments; releases are deliberate merges up; hotfixes merge back down
  to every lower branch (the step teams forget).
- The honest tradeoff : pick dev/staging/prod when a release
  needs human sign-off or a rehearsal is worth the delay; pick trunk-based when
  releasing is boring enough to do 28 times a day. **A develop branch nothing
  deploys, and a staging branch nobody tests, buy the delay without the safety.**
- A **worktree** is a second working copy of the same repository in its own folder,
  so parallel sessions cannot overwrite each other's uncommitted files. Policy: one
  worktree per simultaneously active piece of work; create when work starts
  (using the project's supported worktree command), write only inside it, then keep it for follow-up.
  Remove it only when the user requests cleanup, using the project's guarded
  owner-release command or the Codex app's archive control.
- A **squash-merge** lands a whole branch as 1 commit on the target, so history
  reads one change per topic and any change reverts cleanly.

## Question bank (sample shapes)

1. In a hypothetical project where merging the permanent branch triggers deployment,
   what happens when a PR is squash-merged? (it deploys automatically; distinguish
   this example from the current project's verified release process)
2. You and another session both need to change code today. Why does each get its
   own worktree instead of sharing the checkout? (uncommitted files; a branch
   switch or reset in a shared copy destroys the other's work)
3. In the dev/staging/production model, a bug is found on production and hotfixed
   there. What's the step teams forget? (merge the fix back down, or it resurrects)
4. A feature branch should start from which commit, and why? (fresh origin/main —
   or dev in that model — so the PR contains only your change)
5. When is a dev branch WORSE than no dev branch? (when nothing deploys it —
   delay without safety)
6. What does a squash-merge buy on a busy repo? (1 commit per topic; clean revert)
7. Your PR is green but main moved since the checks ran. Merge? (no — a stale
   green describes a base that no longer exists; re-run against current main)
8. When its PR merges, what happens to the feature branch and its worktree?
   (follow the project's retention policy; keep work and previews until explicit cleanup
   is authorized, then verify backup, ownership and release before removal)
