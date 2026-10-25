---
name: model-effort
description: Proactively advise, decompose, route and tier every new or substantive task. Safety, authorization and explicit spending limits are hard boundaries; verified quality decides first, verified completion speed decides second, and model/token cost is ignored. Owns task decomposition, mechanism choice, model, thinking level and parallel-agent routing. Runs inline before any new job and is also invokable as /model-effort.
---

# Route for the best verified result, then the fastest route to it

## The objective, in this order, and it is lexicographic

0. **Safety, authorization and spending limits are hard boundaries.** They do not trade
   against anything and they are not part of the optimization.
1. **Verified quality decides first.** Choose the path most likely to produce the correct,
   complete, evidenced and safe result. A material quality gain beats any speed gain.
2. **Verified completion speed decides second.** Among paths with materially equal quality,
   take the fastest to a *verified* answer, not to a first draft.
3. **Model and token cost do not count.** Never lower the model or effort to save money. A
   lower or faster tier is right only when it preserves materially equal quality and
   finishes sooner. A saved note about conserving tokens or plan allowance is capability
   history and cannot lower a tier.

Act on the pick yourself and keep clear choices with the agent: route the work accordingly;
never run everything on the session default and mention the better option afterward.
Explicit limits on outside spending remain hard boundaries under item 0. Use the strongest tier that materially
improves the result, never the deepest setting by ritual: when a lighter setting produces
materially equal quality faster, the faster setting wins. Escalate on evidence, not on nerves:
move up when evidence conflicts, a test exposes a wrong assumption, the work is broad or
high-stakes, or a route failed because the reasoning was too thin. Never downgrade if it
could materially reduce correctness, coverage, judgment or verification; for irreversible,
production or correctness-critical work, the downside of a weak answer justifies the
strongest tier that materially improves verified quality.

## When this runs

- **Proactively, before every new or substantive task**, inline, without being asked. Skip
  it only on trivial or conversational turns; a short question about a substantial future
  build still requires assessing that build before naming its pair.
- **A new pasted work prompt or bundle:** read its framing, choose the tier, then start the
  authorized work in the same turn when the current setting fits; when it does not, name the
  change and wait. A go already in the message, a plain question or a live emergency does
  not trigger the wait; follow-up messages inside an authorized build never re-open it.
- **An attached task brief:** when the user's intent to execute it is clear, read the
  instructions addressed to the agent separately from quoted examples and source material,
  choose the tier and proceed within that authorized scope. An attachment alone does not
  grant execution or publication permission; resolve unclear intent before acting.
- **Completion authorization persists**: apply the latest scoped user instruction,
  including a later resumption of paused work, through testing, release and live
  verification; preserve it and every hold when handing work to a helper or saving a
  continuation; never ask for another go at a phase boundary; on a tool refusal use its
  permitted review route with the original context or another permitted safe route, never
  a bypass. A running worker or review-ready result does not finish the parent task:
  continue into acceptance, authorized release, live checks and independent final review,
  and before a final reply apply the completion and real-boundary check; a host-required
  yield needs saved next steps and tested event delivery. The completion boundary is described in [the shared rules](../../guides/operating-principles.md).
- **On demand** via `/model-effort`, optionally naming the task; bare or proactive, it
  evaluates the current or next task in play, asking 1 short question only if genuinely ambiguous.
- For an authorized build, "Resolve ordinary obstacles within authorized scope" in
  [the shared rules](../../guides/operating-principles.md) applies: a failed hosting route or an
  unfinished capacity check stays with the current coding agent; a rule update does not end
  the active build.

## Before announcing any pair

Complete the [selection procedure](#the-selection-procedure) before naming a job's model and
effort, including in
progress messages and advice about a future build. Never fill the pair from the current
session, a default or the easiest part of the job. An initial update may cover the bounded
assessment itself; it never presents that pair as the recommendation for the unassessed
build or claims an unobserved setting is already set.

Keep the report short, never the evidence check incomplete. Keep a brief decision summary
in the existing task notes (working notes for a small task):
the requested finish; material open questions and the checks that cannot settle them; the
current official sources and supported candidate pairs; the strongest alternative and why the
chosen model **and effort** fit better. Write it before the recommendation; it is a concise
conclusion with evidence, not a transcript of private reasoning. If a needed source is
unavailable, name the missing evidence and label the pick provisional.

For mixed work, assess the lead's unresolved decisions separately from settled helper jobs.
Proposed tests are not proof that unknown causes or missing requirements are covered; an
independent review does not by itself establish equal quality on a lighter lead. For 1 pair
across a batch, choose for the hardest material judgment the lead still owns. When advisory
work proposes implementation, name the implementation's pair in that first answer, as its own
job. Tier the work requested now; advice never authorizes implementation or adds an
unrequested later phase.

## Read Anthropic's guidance for every Claude recommendation

Before each recommendation of a Claude model and effort, including a Design handoff, a
revised recommendation in the same conversation, and the final recommendation after a
consultation or review loop with another agent (Codex, Design, another session), read the
current official
[model-selection guidance](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model),
[model comparison](https://platform.claude.com/docs/en/models/overview) and
[effort guidance](https://platform.claude.com/docs/en/build-with-claude/effort), plus the
candidate model's own prompting and effort guidance. A remembered ladder, local table, earlier
recommendation or visible picker alone does not satisfy this. When a back-and-forth with
another agent ends in an agreed proposal, the reply reporting the agreement re-reads these
pages against the agreed scope and names a checked pair for the implementation; a pair carried
from an earlier round is never restated as the recommendation. Then judge the task: what is
settled, what choices remain, how much context must stay consistent, how long the work runs,
what a mistake affects, which checks catch it. Model-specific guidance overrides a generic
effort table; never carry an effort from an older model to a newer one by name; a provider
default is a starting point, not proof. Select model and effort together using the
objective above. Never claim that a quality gain or equal quality was measured without
actual task results; generic provider guidance supports a provisional task judgment, not a
measured claim of equal quality or faster completion.

Confirm both exact labels in the receiving product's current controls or official product
documentation; Claude Design, Claude Code, chat and the API expose different choices, and
availability is not suitability. Always give model and effort together, even in a short
correction or a repeated handoff. Cite the official basis briefly and keep Anthropic's guidance distinct from the
task judgment. If official guidance cannot be reached, say so and label the pick provisional.

### Claude Design: establish the recommendation's evidence limit up front

Before the first Design pair, distinguish visual exploration, whole-journey interaction work
and bounded changes to an approved design; identify the consequential choices still open and
the dependencies between screens. Screen count, a long prompt, sensitive subject matter or the
word "design" does not establish harder reasoning; a prototype of checkout is not a payment
operation; approved content reduces uncertainty without settling every interaction,
narrow-screen state or handoff.

Compare the strongest credible alternative on the same full assignment, including the
candidate's default and, where relevant, a higher supported effort. State the model's
expected benefit separately from the reason for its effort. Never choose High merely because
the model is stronger, or Max merely because quality comes first; never require a failed
lower-effort run before choosing deeper reasoning that the unresolved work and model-specific
guidance justify. Explain any departure from the
provider's starting advice without quoting only the passage favouring the preferred model.

Keep 3 kinds of evidence separate: product controls establish available labels, not quality
or any mapping between Design's effort control and API settings (never change shared settings
or interrupt a running Design request to inspect availability; name an unconfirmed pair);
provider guidance supports an expected fit, and general coding or reasoning benchmarks, API
effort advice and "most capable" claims do not establish better visual taste, fewer missed
screens, faster accepted completion or the best effort inside Claude Design; comparable
completed Design work supports a bounded
outcome claim, where a successful export, 1 model's screenshots, a second model's opinion or a
test of this skill proves nothing about model performance.

Ordinary Design recommendations need no fresh trials: recommend from the nature of the work
and current guidance, with outcome evidence when available, and say in the first answer
whether the pick rests on guidance or on tested advantage; never turn missing trials into a
blocker or repeatedly demand evaluations. When both alternatives have a
substantial task-specific case that could change the finished result or completion time,
present both exact pairs, the practical tradeoff and the preferred choice, and let the user
choose before starting the affected Design work; do not change an existing Design request
while that choice is pending. Mere uncertainty, both models being capable, or absent trials
does not trigger this; clear choices remain the agent's own recommendation. Never call a
defensible alternative wrong merely because it was later replaced; name the actual
assessment defect and what remains unknown. For a
requested proof of superiority, use the matched-input method in
[selection evidence](references/selection-evidence.md#claude-design-comparison-checks); a
comparison that cannot run within access, scope or spending limits is reported as the exact
missing comparison, never a simulated win; never send new Design work, restart a project or
substitute Claude Code or API outputs for Design results without the appropriate
authorization.

## The selection procedure

For leads, helpers, reviews and consultations. Task-shape examples elsewhere are illustrations,
never automatic assignments.

1. **Reconstruct the requested finish before naming a model.** Read the request history,
   approved constraints and task evidence; include diagnosis, shared uses, implementation,
   independent review and delivery when requested. Distinguish settled work from open causes
   and decisions: a clear symptom is not a known cause, and tests for 1 proposed fix do not
   establish the whole problem is understood. Trace related effects without expanding
   permission to change them.
2. **Identify where judgment can change the result.** Competing causes, interacting
   requirements, evidence gaps, memory across dependent steps, harm from a wrong answer, what
   the named checks cannot catch. Assess each meaningful phase; if the user wants 1 setting for
   the whole job, choose for the hardest material judgment that remains; otherwise assign
   bounded work independently when
   the handoff and review preserve quality. A routine release is not difficult reasoning
   because publishing takes long.
3. **Compare supported model-and-effort pairs, not brand roles.** Read current official
   selection and model-specific effort guidance and confirm the receiving host's options (the
   OpenAI Docs skill for OpenAI when available, otherwise current
   [official OpenAI documentation](https://developers.openai.com/); the per-recommendation
   source rule above for Claude; official sources for any other provider).
   Model roles are shorthand, not evidence. A confirmed
   access or rate limit that prevents completion is a feasibility constraint, not an
   allowance preference: choose a suitable permitted route or name the dependency. Compare
   the credible alternative, including more effort on the same model. A comparison with an
   unnamed model cannot name a winning model; recover its run identity or limit the
   conclusion to the tested effort on that unidentified model. Name the task-specific
   advantage expected. Where official pages differ, distinguish model-specific guidance from
   illustrative tables and examples, apply the guidance for the actual receiving product, and
   name unresolved conflicts rather than selecting whichever example supports the first pick.
   A provider's cost advice never changes the quality-first objective.
4. **Challenge the first pick before showing it.** What known fact most favours the
   alternative? Would the choice hold if the user asked "are you sure?" or named the other
   model? Resolve omitted scope and conflicting guidance now, without automatic peer
   consultation or exhaustive benchmarking for a small task.
5. **Finish the decision record before announcing the pair.** For a consequential, disputed or
   phase-split choice, or a deliberate comparison, keep in the task notes: requested finish;
   open uncertainty and checks; selected pair and credible alternative; evidence basis and
   source date; expected benefit and limitations; what evidence would change the pick.
   Routine work gets a short rationale in working notes. Distinguish provider guidance,
   task judgment and observed comparative results. Explain the reason to the user when a
   setting needs changing, a choice is challenged or the recommendation changes; never
   print a worksheet for every task. Inspecting a picker proves availability, not
   capability or the running setting.

A settled build with focused checks is a good candidate for a faster pair, not proof of equal
quality; an unresolved, consequential interaction is a reason to consider stronger reasoning,
not proof the deepest pair wins. Without a task-specific comparison, make the best-supported
choice, name the residual uncertainty, and never invent speed percentages, guarantees or
superiority. Missing tools, credentials, devices or sources need those inputs; more reasoning
cannot supply them.

### When a recommendation is challenged

Recheck the recorded scope, evidence and strongest alternative, reconstructing what was known
at the first recommendation from the request history rather than facts learned later. A
challenge alone is not new evidence. Keep the pick when its basis holds; change it when new
facts, changed scope, current guidance or a specific flaw in the original assessment
materially changes the choice, naming the exact delta and why it matters. If a relevant fact
was already known but omitted or underweighted, say the original assessment was incomplete,
never that scope expanded. Correct a bad choice rather than defending it, and never
manufacture certainty to keep it. A planned phase change is not a reversal: name the phase
and its now-bounded work. A failed attempt gets diagnosis first: reasoning failure, missing
context, weak checks, tooling, permissions or external waiting. A final success after helpers
and review does not prove the initial model was optimal or that another would have failed.

### Keep the guidance accurate through use

Use [selection evidence and review cases](references/selection-evidence.md) when a choice is
challenged, misses its expected outcome, or new models or effort guidance change a relevant
comparison; capture outcomes there from authorized task evidence and run representative
comparisons on demand. Reconcile
conflicting selection instructions in place; maintain evidence by task type and exact version,
never a permanent universal winner. This is event-driven, never authorization for paid
schedules or unattended model runs. Head-to-head comparisons use the matched-input and
outcome method in that file; an ordinary recommendation implies no comparison run.

## Classify by what bounds the task

These shapes guide decomposition after the procedure; they do not override its evidence.

- **Reasoning-bound** (unresolved alternatives, conflicting evidence, tricky code; a wrong turn
  costs rework): consider a stronger pair when it is expected to reduce material reasoning
  errors.
- **Mechanical, well-specified, bounded** (simple edits, routine changes, formatting, a clear
  spec, bulk file reads): the host's fastest model that preserves materially equal quality,
  light through standard reasoning; equal quality and faster completion are a task judgment
  unless a comparison supports them.
- **Mixed** (the common case: a little judgment around much mechanical work): keep the
  reasoning and orchestration in the main loop at the tier the hard part needs; delegate
  independently briefable mechanical work when execution plus review shortens accepted
  completion without losing quality. Split it up front so the hardest 10% does not slow the
  rest.
- **Throughput-bound** (API batches, scraping, builds, large file ops, external waits): a
  larger model does not shorten the wait. Assess planning, batching and retry decisions
  separately; run settled independent slices as processes capped by service limits.
- **Multiple agents** help with independently briefable reasoning or mechanical work when
  execution plus review shortens accepted completion without losing quality; dependent steps
  stay ordered, 1 writer per artifact; pure throughput gets processes, not reasoning agents.

## Then pick the mechanism, a separate call

Classification informs selection; it does not pick the pair or where the work runs. 4
mechanisms, in neutral words so the rules work on any host; only the host table names tools.

- **current task**: the session in conversation with the user. Owns the plan, the acceptance
  judgment, the cross-piece check and the report, and delegates none of those; helpers run
  checks and hand back evidence, the lead decides what is true. Default for anything needing
  context already held.
- **internal worker**: help inside a session that reports back and the user never sees. For
  mechanical, self-contained, completely briefable work: a config change, a doc edit, a rename
  sweep, bulk reading, a wiring pass, a verify-and-delete. Its own context protects the lead's.
- **visible durable task**: a separate job needing its own visible conversation, independent
  decisions or later resumption. Risk calls for judgment and review, not automatically a new
  task; preserve useful lead context and host creation permissions.
- **non-reasoning throughput**: work that waits instead of thinking: downloads, builds, bulk
  fetches, repeated commands. Never a reasoning agent.

Defaulting to the visible option because it is visible pins every delegated job to the
parent's tier on hosts that copy it, mechanical ones included. Never split 1 tightly coupled
change across tasks to parallelize it (shared decisions drift and the merge costs more than
the serial build saved); never open a visible task for work you could brief completely to a
faster internal worker with materially equal quality. When a mechanism cannot carry the control a job needs, assess
another permitted mechanism; an unavailable control does not make the strongest available
setting suitable. Preserve context, quality and authorization; when the needed pair cannot
be supplied safely, report the limit and follow the task-start and existing-authorization
rules. Say which mechanism was chosen and why, so the user can push back.

### Own the route and settings

A "new task" or delegation request authorizes a helper instead when a helper fits the work better:
a bounded build with settled behaviour and clear checks, with the current task keeping
acceptance and release. A separate visible task fits an ongoing conversation, substantial
independent decisions or a long investigation resumed separately. Publishing alone does not
need a separate task. State the route and proceed; keep a later explicit requirement for a
visible conversation, all scope, holds and host limits; never relocate active work merely
to match this route preference.

Select the delegated work's model and effort from the work, not the parent's setting, through
the permitted launch or follow-up controls. For a Codex visible task whose creation cannot
select the chosen model, complete the two-step launch below before substantive work; never
hand the user a setting change the parent can make. Never broaden creation permissions: a
generic delegation request does not name a particular model. A follow-up setting applies to a
later turn, never a running one. Report an accepted
setting separately from observed work.

### Host table, the only place mechanisms are named

The table records example host controls from the source setup, not a promise that
your product exposes them. Use only controls present and permitted in the current
tool list. Verify current behavior and authorization before relying on any entry.

| Neutral name | Claude Code | Codex |
|---|---|---|
| **current task** | This session. Both controls are the user's (`/model`, `/effort`). It cannot change its own. | The current task. Same: it cannot change its own. |
| **internal worker** | Use the installed helper definition or launch controls for `model` and `effort`; support depends on the version and mechanism. Do not assume a control exists from this table. | `spawn_agent` may expose `model` and `reasoning_effort`. Use only supported history options; some hosts require `fork_turns="none"` for overrides. A full-history worker may inherit both. |
| **visible durable task** | Use the current host's supported launch mechanism. A CLI launch may expose `--model` and `--effort`; an app task control may differ. Verify its actual behavior. | `create_thread` may expose effort and allow a model only when the user named one. Follow the current tool contract and creation permissions. |
| **non-reasoning throughput** | Background processes and batched tool calls. The controls change nothing. | Batched calls (`functions.exec`) and long-running commands (`exec_command` with `write_stdin`). Neither is a reasoning helper. |

**When a setting comes out wrong:**

| Question | Claude Code | Codex |
|---|---|---|
| Can it change its own setting mid-job? | No, for any of them. | No, for any of them. |
| Can the parent fix a worker after launch? | Only through a supported later-turn control. If replacement is necessary and authorized, save progress, stop the exact worker and its child writers safely, then resume or replace without losing work. | Only through a supported later-turn control. Otherwise preserve progress and stop the exact worker and child writers before authorized replacement. Never interrupt unrelated work. |
| Can the parent fix a visible task later? | Depends on the host mechanism. Use a supported setting or resume control when permitted; an ordinary message does not change the setting. Ask the user only when the host exposes no suitable control. | A host may expose later-turn controls such as `send_message_to_thread`. Verify permission and tool support; no change retunes a running turn. |
| Does a visible task start on its own? | A supported background CLI launch can start immediately; an app launch may wait for a user action. Observe the actual working state. | Some launchers start without a click after setup. Observe the actual working state; creation alone does not prove execution. |
| How risky actions are gated | Permission settings and hooks. | Its own sandbox and approval flow. |

Some Codex hosts can copy a Codex task's history with `fork_thread`. Inspect the
current tool's supported source kinds and launch behavior. Do not assume it exposes
model controls or retunes a turn; use a supported follow-up control only when authorized.

### When the user has to set the controls

Never let a turn run at the wrong model or effort without telling the user what to set, using
the fastest quality-safe fix the host allows.

- **Claude Code**: inspect the permitted launch controls. A requested visible task started by
  a chip inherits the parent's settings, so its title opens with the selected model and
  effort; when
  that pair differs from the inherited one the user sets it before clicking; a chip is never
  replaced by a manual copy-and-paste handoff. When permitted controls can set the pair, use
  them and observe work starting; ask the user only when required.
- **Codex**: the running task cannot change itself. For a user-requested new visible task,
  start at once when the launch controls or a suitable inherited setting supply the chosen
  pair; otherwise use a
  setup-only first turn (read the brief, no substantive decisions or changes, obtain the real
  ID), then the permitted follow-up control to set the pair and start, observing accepted
  settings and active work. Ask the user only if no permitted control can supply the setting;
  never create an unsolicited visible task or claim a running turn was retuned.

### Explicit design-build routing

Follow the user's explicit choice of current-task or separate-task execution.
Carry the selected model and effort through permitted controls, preserve design
approval and publication boundaries, and keep the parent responsible for review
and delivery. Do not infer a local shortcut's meaning in a different installation.

### Finish a two-step task launch

Only when the host's model-setting restrictions require it. Never set a launch model the host
does not permit or pass a temporary client ID to a tool that needs a real thread ID.

1. **Prepare the whole handoff before creation**: the full brief, intended model and effort,
   parent thread ID and exact start message together. The setup message permits reading and
   acknowledging the brief and 1 readiness message to the parent (with real thread ID and
   working directory when available, saying it awaits the parent's start), and nothing else.
2. **Resolve identity, not just a title.** Save the creation result and use its real thread ID
   when returned. A temporary client ID means creation is not yet resolved to a usable ID; it
   does not prove setup is still in progress later. A recency-limited task list may omit a
   ready task, and absence from it proves nothing.
3. **Recover a missing ID with direct evidence**: the child's readiness message or the host's
   creation status; failing those, a supported read-only source that links the exact temporary
   ID to a real thread ID (a narrowly filtered application log), then read that thread and
   match its brief, directory and setup response before sending anything. Never guess from a
   similar title, a broad log dump or a nearby unrelated error; never repeatedly poll the
   same incomplete listing or create a duplicate as a retry.
4. **Send the start message immediately when ready**, applying the intended pair through the
   supported follow-up control and lifting only the setup hold; every product, publication
   and spending hold stays. Existing authorization covers this step.
5. **Observe the start before reporting it**: a direct status read or bounded wait on the real
   thread ID; "running" only with an active work turn or task-specific evidence, never a
   receipt acknowledgement or successful message submission alone. Record created, awaiting
   parent start, start requested, active, failed. If blocked, name the observed failure and
   recovery step; never claim the app is still preparing a working copy without evidence.

Complete the handshake in the launch turn when possible; if an external boundary prevents it,
keep the exact IDs and remaining start message, report that boundary, and resume before
unrelated work in the next active turn. No paid recurring monitor, no implied background
ownership when nothing is running.

### Consulting the peer coding platform

The agent holding the task is the `current coding agent`; the other platform is the `peer
coding consultant` (Codex for Claude Code, Claude Code for Codex). A consultation supplies a
second judgment while the current coding agent keeps ownership, integration and the final
answer. Share only task-relevant material that the user and host permit that
recipient to receive; local file access alone does not authorize external sharing.
Not automatic: a
second opinion is worth nothing with nothing to disagree about, and routine agreement destroys
the signal. 4 triggers, after direct evidence checks: the decision is expensive or dangerous to
reverse; only the other platform can prove a fact about its own controls; a disputed or
important judgment is about to become a lasting shared rule, not merely a document edit; the
evidence still conflicts, is
incomplete, or a lead catches itself confident without evidence. Only a lead consults; it
may assign exactly 1 worker to carry a fixed question, which returns the answer and its
evidence, and the lead still decides what is true and what gets written down. The
consultation's model and effort follow this skill's objective: judgment questions get the
strongest useful reasoning the path accepts; plain capability lookups get light reasoning.
Agreement between 2 models is not evidence. Use the receiving platform's installed,
authorized consultation route. Establish the authentication and billing route before
calling it; never copy credentials into prompts or assume a subscription covers API use.

## Then shape the run: critical path first, without manufacturing work

Tier and mechanism decide how well and where; this decides how much runs at once, which is
where the speed priority is cashed in.

- **Safe independent work runs in parallel by default.** Before a serial plan, list the nodes
  whose prerequisites are satisfied; if 2 or more can run now without sharing an unsettled
  decision, file, branch, production resource or safety gate, start them immediately at
  the right tier and name each owner in the reply; never wait for the current chain to
  finish, offer the split as an optional later idea, or wait for the user to ask whether
  parallel work is possible. Repeat whenever scope, dependencies or capacity change. A
  negative check goes in working notes unless it is surprising or changes the
  recommendation. Parallel work must still materially shorten the checked finish after
  briefing, coordination and merge cost.
- **Build the smallest useful dependency graph** once a job has 3 or more meaningful parts or
  any real dependency: per node, the result, prerequisites, owner, files or resources it may
  touch, completion check and merge order.
- **Staff the longest chain first**, then fill capacity with the highest-value independent
  work ready now; launch the next ready node the moment an agent finishes, since idle capacity
  is lost wall-clock.
- **Never create agents to fill slots.** Keep work together when it shares 1 design decision,
  edits the same files, changes the same production resource, depends closely on earlier
  judgment, or when briefing plus coordination plus merging exceeds doing it in 1 place.
  Merge cost is charged in the same currency as the saving.
- **Split breadth, never judgment**: 1 fast pass to enumerate, then parallel over the items;
  an unsettled plan is a serial node by construction.
- **1 writer per file or resource**; where overlap is unavoidable, 1 writer and 1 read-only
  reviewer; parallel mutation of 1 tree needs isolated copies.
- **Verification lives inside each branch**; a step waits for every prior result only when it
  genuinely needs them all (deduplicating across the set, exiting early on zero, comparing
  findings).
- **Production, security, migration, spending or irreversible work gets a separate strong
  review as its own node after implementation**, never a second writer on the same change.
- **Match the loop to the work**: a known list, a pipeline; unknown size, loop until 2
  consecutive rounds return nothing new; a blocked step, run everything independent of it.
- **Separate external waiting from decisions about it**: processes for settled waits and
  repeated commands; planning, batching, retries and diagnosis assessed as reasoning work.
- **Saturation is a live fact**: discover the host's current concurrency cap from its own
  documentation or behaviour before fanning out, and scale to that cap and the item count;
  never carry a figure across hosts or versions.

## Models and effort ladder

3 descriptive model roles, never permanent mappings; named examples illustrate formatting or
dated evidence and do not select a model for the next task: **`fast`** (clear, repeatable,
high-volume work with a concrete definition of done), **`balanced`** (everyday work needing
solid reasoning and tool use), **`frontier`** (ambiguous, difficult, high-value work: new
design direction, hard diagnosis, security, production data, migrations, concurrency,
high-value review, final integration). First choose a platform-neutral reasoning role, then
translate it: **`light`** (trivial, tightly bounded or waiting-heavy work where deeper
thought adds nothing), **`standard`** (clear routine work where checks make simple mistakes
easy to catch), **`deep`** (work with unresolved alternatives where a wrong turn would cause
meaningful rework), **`deepest useful`** (the hardest correctness-critical work, only when
more thought can materially improve correctness, coverage or judgment). Never carry any 1
tool's level name into universal guidance; a newly adopted tool gets its own translation
without changing the shared roles.

Discover, never hard-code: resolve a role into a model from the current host's callable tool
metadata, configuration and official guidance; never copy a ladder across hosts, quote
pricing without the provider's current source, or leave retired aliases in saved settings.
Per-host lists and quirks live in `../../guides/model-and-cost-routing.md` with the date each
was checked. The 1 exception: a user-facing pair names today's full selectable model label,
variant or suffix included, and the exact effort label, nothing else.

## Apply it yourself

The procedure decides the pair; these are candidate execution shapes. A recommended tier that
matches the current task means proceed here while still assessing worthwhile worker
assignments. Mechanical or bulk work: a `fast` pair and an internal worker when fully
briefable and checks preserve quality. Reasoning-heavy or correctness-critical work: a
`frontier` pair with effort justified by the unresolved reasoning, downside and checks. Mixed
work: hard decisions and integration on the strongest appropriate lead, well-defined
implementation and verification on faster workers. A hard decision that arises while the
current task runs on a lower tier goes to a stronger worker only when its subproblem can be
briefed completely; pervasive context-heavy reasoning stays in the current task.
Waiting-bound work: processes for settled
waits, separate pairs for unresolved planning or recovery. Production, security, migration,
spending or irreversible work: a separate strong review node after implementation. If a host
exposes no permitted override, report the exact limit, assess whether the configured setting
is suitable, use another permitted route when it preserves context and quality, otherwise
follow the task-start and existing-authorization rules above rather than silently treating
the default as the chosen pair; ask for a user-only change only when required; never claim a
change without an accepted tool control.

Verification of this skill exercises the selection on the realistic cases in
[selection evidence and review cases](references/selection-evidence.md): scope coverage,
evidence, justified stability and revisions, respect for authorization; never whether the
answer repeats a hard-coded model label. The supported pairs and best mechanism can differ
across hosts; the user outcome and selection criteria must not.

## Report

Name the pair as [the shared rules](../../guides/operating-principles.md) explain: once per batch, in
the intro line
above the jobs, the full selectable model label and exact effort label, each in inline code,
separated by 1 space. After routing, state the classification, the chosen mechanism, every
safe independent track started in parallel and its owner, and which launch control was used;
if a host rule prevented an override, say so. The displayed pair does not prove which setting
is running; accepted host controls establish that. Advice you act on, not a question you wait
on.
