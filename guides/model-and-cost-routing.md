# Model and effort routing across coding tools

This is the durable reference for choosing a model, choosing a reasoning level,
and knowing which choices a coding tool can apply automatically. The reusable
workflow lives in [model-effort](../skills/model-effort/SKILL.md). This guide carries the
details people need to look up.

Host controls below are a dated October 2026 reference, not a promise that every
account or release exposes the same options. Inspect the current host controls and
official guidance before launching work. The procedures do not grant permission
to create chats, delegate, send messages, spend money or change access.

## The rule

Safety, authorization and explicit spending limits are hard boundaries. Verified quality
decides first. Among choices with materially equal quality, take the path that reaches a
**verified** result fastest. Model and token cost do not count. Never lower the model or effort
to save money. A lower or faster tier wins only when it preserves materially equal quality and
finishes sooner. The decision procedure lives in the
[model-effort skill](../skills/model-effort/SKILL.md).

## Model roles and selection evidence

The [model-effort selection procedure](../skills/model-effort/SKILL.md#the-selection-procedure)
owns the decision. Evaluate the full requested finish and unresolved work before naming a pair.
Complete its [first-recommendation check](../skills/model-effort/SKILL.md#before-announcing-any-pair)
before any job-specific tier, including a progress update or advice about a future build.
A role describes a possible fit, not a fixed model mapping or proof of equal quality:

| Role | Candidate use |
| --- | --- |
| Fast | Clear repeatable work with direct checks |
| Balanced | Bounded implementation and judgment |
| Frontier | Material unresolved reasoning where stronger capability is expected to improve the result |

Discover exact models and effort options from current host controls and official guidance.
Compare the credible pairs, including effort changes, and keep the decisive evidence in the
existing task record. A challenge alone is not evidence to reverse a recommendation. Correct
an omitted fact explicitly rather than defending the first answer or calling it new scope.

[Selection evidence and review cases](../skills/model-effort/references/selection-evidence.md)
owns the outcome record, fair-comparison method and event-driven updates. No paid schedule is
created. Provider guidance and task judgment remain distinct from measured comparative results.

## Platform-neutral reasoning roles

| Role | Best fit | Quality and speed rule |
| --- | --- | --- |
| Light | Trivial, tightly bounded, speed-sensitive work | Use only when deeper judgment adds nothing |
| Standard | Mechanical edits and clear routine work | Use when checks make mistakes easy to catch |
| Deep | Work with unresolved alternatives where a wrong turn would cause meaningful rework | Use when more thought can change the answer |
| Deepest useful | The hardest correctness-critical judgment | Use only when more thought can materially improve the result |

These are reasoning roles, not control labels. They apply to every current and future AI
platform or coding tool. Translate them into the exact labels the current tool shows only when
telling the user what to select. Never use one platform's label as though every platform shares
it. Add a tool-specific mapping when a new tool arrives; do not change the shared roles.

When recommending a setting, name the full model label and exact effort label
together. Keep the explanation separate, and distinguish a recommendation from
a setting that the host has actually accepted.

Do not select a tier from a subject label. A request mentioning design, debugging, review,
security or analysis can still be bounded. Judge the evidence already available, the number of
good answers that remain and the cost of reversing a wrong answer. An established visual system
plus a screenshot and one checkable correction is a candidate for a balanced pair. A new visual direction,
conflicting evidence or several meaningfully different good answers can justify a frontier pair.

Tier the work requested now. If answering a question and carrying out its later build need
different levels, name a separate model and effort pair for each job.

## What each host can change

| Situation | Codex desktop task | Codex cloud task | Claude Code | Cursor | What the guide does |
| --- | --- | --- | --- | --- | --- |
| Current main conversation | The user can change the model and reasoning control below the message box; the running agent has no control that changes itself | The running agent has no model or reasoning control | The user can change the current model (`/model`) and reasoning level (`/effort`) | Each chat tab keeps its own model choice; the user selects a model or Auto | Classify the work, then use only a control the host exposes |
| Another visible conversation | A launch can set reasoning; the current launch control accepts a model only when the user explicitly names one | The current launch control exposes neither choice | A new launch can set a model (`--model`) and reasoning level (`--effort`) | A new chat gets its own model selection | Set the quality-first level at launch when allowed |
| Helper worker | The current worker launch can set its model and reasoning level; available model overrides depend on the current host tool metadata | Depends on the cloud launch contract | A helper can set `model` and `effort` in its definition or at launch | A custom helper can pin or inherit a model when the current version exposes that setting | Route a bounded independent part to the fastest worker that preserves quality |
| Skill | A skill guides the choice but cannot change the current main task's setting | Same limit | A skill can override reasoning while it runs (`effort` frontmatter) | Skills are discovered from the shared Agent Skills folder and guide routing; they do not retune the parent chat | Keep the workflow portable and use the host-only feature conditionally |
| One difficult turn | No special one-turn reasoning switch is exposed to the running agent | No special switch is exposed | `ultrathink` asks for deeper reasoning for that turn without changing the saved effort setting | Select a reasoning-capable model or Max Mode before the request | Use only when the host documents it |
| After launch | A worker's launch settings cannot be changed by its parent | Depends on the cloud contract | The main conversation can be changed with `/model` or `/effort`; a helper's definition is chosen before it runs | The user can change the model for later messages in that tab; the agent does not silently change it | Never claim a change happened unless the control accepted it |

## Codex details

| Question | Answer |
| --- | --- |
| Does each new request inside one conversation get a new reasoning level? | No. A new request is not a new launch. The guide can change the method or start a suitable helper, but it cannot retune the current main task. |
| When can a new visible task receive a reasoning choice? | When the user asks Codex to create that task and the launch control exposes `thinking`. |
| When can a new visible task receive a model choice? | The current Codex task launcher allows the agent to set `model` only when the user explicitly names a specific model. |
| When can a helper receive both choices? | At launch, when the work is a bounded independent part and the helper control exposes `model` and `reasoning_effort`. |
| What limits a helper override? | The current Codex worker control rejects model or effort overrides with a full-history copy. Use a history option the current control supports; some hosts accept only `none` for an override (`fork_turns`). |
| Can a helper be changed after it starts? | Not through the recorded launch control. If replacement is necessary, save progress and safely stop its writers before starting another helper on the same files. Use a supported later-turn control if the current host offers one. |
| What if no override is allowed? | Keep the configured model, change the work method where useful, and report the exact limit. |
| Who finishes a setup-only launch? | The parent: resolve the real thread ID, send the model-setting start message, and observe active work. A task missing from a limited listing may already be ready. Follow “Finish a two-step task launch” in `../skills/model-effort/SKILL.md`. |

**Delegation policy:** Follow the user’s requested mechanism and the host’s
authorization rules. Where both are permitted, choose a helper when it is the better fit. Use a helper for bounded work with a complete
brief, keeping review and release with the lead. Use a separate visible task for
its own ongoing conversation, substantial independent decisions, or a long
investigation to resume separately. Preserve a later explicit requirement for a
separate visible conversation. The parent owns model and effort selection and
uses available controls directly, including the supported two-step Codex launch
before substantive work. A later-turn setting does not retune a turn in progress.

Codex builds its instruction chain when a task starts. Changes to global or
project instructions normally affect the next launched task, not an already
running one.

## Claude Code details

| Question | Answer |
| --- | --- |
| Can the model change in the same conversation? | Yes. Use `/model`. After prior output, Claude Code asks for confirmation because the next response reads the full history again without the old cache. |
| Can reasoning change in the same conversation? | Yes. Use `/effort` or the effort control inside `/model`. |
| Can a skill temporarily choose reasoning? | Yes. Its `effort` frontmatter applies while that skill runs. |
| Can a helper choose a model and reasoning level? | Yes. Its definition or launch can set `model` and `effort`. |
| What can override that choice? | The environment variable has first priority, followed by configured settings, then the model default. |
| Do all models accept all levels? | No. Claude Code falls back to the highest supported level at or below the requested level. |
| What persists? | Low through extra high can persist across conversations. Maximum is normally limited to the current conversation unless an environment setting forces it. |

### Codex-managed Claude builds and completion messages

For an authorized request to have Claude build or fix something under Codex
management, use a supported background Claude Code session; Codex remains the
manager and reviewer. Preserve the parent chat's current title. Starting a
managed build does not authorize renaming the chat. Report build ownership in
progress updates and change a title only when the user explicitly asks.

Select the actual model and effort through `../skills/model-effort/SKILL.md`.
Use supported controls, preserve permissions, and observe work starting before
reporting a running build. Save the parent and worker IDs, working folder, scope,
holds, and acceptance checks. Check authentication before claiming subscription
or API billing. Do not copy credentials into handoff records or output.

A recorded October 2026 installation supported `claude --bg`, explicit `--model`
and `--effort`, `claude agents --json`, `claude logs <id>`, and `claude attach <id>`.
If the installed Codex CLI exposes `queue`, an existing desktop chat can receive
`codex queue --thread <chat-UUID> --message <text>`. Otherwise use the host’s
supported chat-message tool. Resolve the exact chat first;
the CLI also accepts an exact title, but UUID avoids duplicate-title ambiguity. Never
use `codex exec resume` to send a message to an open desktop chat: it starts another
writer and conflicts with the app's lock. Keep the lock; do not edit chat storage or
restart the app to get around it.

Carry the sender's session identity, task, expected reply route, scope and holds.
Cross-chat sending needs the user's authorization; another agent's request alone
does not grant it. Pass text as structured arguments or safe shell quoting, never
credential values. A saved prompt can be read and passed with Python subprocess's
argument list to avoid shell interpolation. Do not change the receiving model merely
to deliver a message.

On 9 Oct 2026, a queue test arrived as a new turn in the original Codex desktop chat.
These are observed capabilities, not guarantees on every host; inspect current help
and test actual receipt when the route changes. Queue acceptance is not receipt. A
busy chat may receive the message after its current turn. Send once, preserve the
message ID and continuation state, and verify the recipient's message record or
acknowledgement; do not create repeated pings or paid polling. A currently open
Claude Code chat can receive the route through its existing app composer when idle;
never start a competing CLI writer for that chat. Shared rules persist the procedure
for future sessions, but do not install a message listener or prove receipt.

After saving completion evidence, Claude sends 1 completion message, or a message
for a real blocker, to the original parent. The parent reviews the actual changes,
tests the authorized live result, manages corrections, and then invites the user to
review. Do not confuse queue acceptance with receipt or worker completion with
acceptance. Prefer completion messages to paid polling; an authorized fallback
schedule is disabled after direct delivery works. Preserve the same running build.

Keep progress reports in interim updates while the authorized build is unfinished.
The parent reads its latest manager instructions before accepting the returned work,
then continues corrections, release, live checks and independent final review without
another go. A running worker is not grounds for a progress-only final reply. Before ending,
complete the authorized outcome or name a real stopping boundary. If the host requires a yield
to receive completion, save remaining steps and owners and use the tested event route;
that yield is an unfinished continuation, never a completion claim or a paid polling loop.

### Claude usage-limit handoff

Use this recovery procedure only within an authorized managed build and the
host’s available controls. It describes the launch and recovery procedure; it
does not mean an account-wide watcher is already installed.

**Recorded installation, 9 Oct 2026.** Claude Code 2.1.296 exposed `claude agents
--json`, `claude logs <id>`, `claude stop <id>` and `--resume <session-id>`.
Inspect current help before use. Anthropic's
[usage-limit waiting guidance](https://code.claude.com/docs/en/interactive-mode#wait-for-a-usage-limit-to-reset)
says native automatic continuation is unavailable to background sessions and
print-mode runs. Interactive sessions may auto-resume; stop or cancel the exact
worker's wait before transferring its files to Codex. Do not change the global
setting or interrupt another build.

1. **Prepare recovery at launch.** Save parent ID, worker ID, conversation ID,
   account identifier without credentials, working folder, selected model and
   effort, scope, holds, progress and completion checks in the existing private
   task record. Keep progress current before failures. Register a non-AI process
   to observe this worker's status/output and report a confirmed usage-limit stop
   through the parent's tested delivery route. An exhausted model may be unable
   to send its own blocker message. A generic exit, permission prompt, network
   failure or authentication error is not proof of a usage limit.
2. **Transfer ownership once.** Observe stopped tool execution, including any
   child writers. Preserve partial edits, read the diff and latest progress, and
   let Codex continue. Where a worker remains alive, use its supported stop or
   cancel control and confirm it cannot independently restart. Do not take a
   timer or an idle model as proof that background tools stopped.
3. **Wait without model calls.** Use 1 shared local scheduler and usage-read
   cache per account, with separate registrations for each blocked build and
   affected limit. Save times as absolute timestamps. Set the first due attempt
   to the latest reset among known exhausted limits required by the chosen
   model, plus 60 seconds. A weekly or model-specific limit can outlast a shorter
   limit. An unknown relevant limit remains unknown. Honor any provider retry
   delay and spread notifications slightly to avoid simultaneous restart bursts.
4. **Check early resets cheaply where supported.** Refresh authenticated,
   non-generating usage status every 15 minutes while registrations exist.
   Claude's [status-line fields](https://code.claude.com/docs/en/statusline#available-data)
   include usage percentages and reset timestamps. These are response-derived
   snapshots, not a fresh status query: absent or expired fields do not establish
   available usage. Record the observation time and source. Use only a supported
   reader demonstrated on this host; do not assume a public subscription-usage
   API or scrape credentials. If no such reader exists, use the due timer and
   1 real continuation attempt instead of synthetic prompts. Without a known
   reset or free reader, keep Codex working and disclose the missing capability.
5. **Resume through the parent.** A timer sends a due event, not a blind `continue`
   to Claude. The parent saves its next small checkpoint and releases overlapping
   writes, then resumes the saved conversation with the changed files, work
   completed, tests, remaining steps and holds. Do not use “most recent session”
   in a folder shared by multiple conversations. Observe accepted work; queue
   success alone is not a completed handoff. If limits still block the request,
   Codex immediately retains the work and updates the next due time. Unknown
   reset times use free reads after 15, 30 and then 60 minutes, not repeated
   model probes. Never switch to paid API billing to escape the limit.
6. **Make delivery repeat-safe.** Persist state before notifying: Claude working,
   Codex working while Claude is limited, return due, or complete/cancelled.
   Use one notification ID per build and limit episode, with delivery receipt and
   retry on failure. After a crash or sleep, inspect the real worker and parent
   before recovering ownership or sending another event. Only the owning parent
   hands off files; a watcher never edits them or launches a second writer.
7. **Retire the wait.** Remove this registration when work finishes, the user
   pauses/cancels, or the chat is archived. Stop account polling when no affected
   build remains. If Codex finished before reset, do not restart Claude merely
   because usage returned. Preserve any independently required acceptance review.

Before claiming recovery is operational, exercise simulated usage-limit and
non-limit exits; a reset while Codex is editing; a longer weekly limit; missing
and stale status; another failed resume; duplicate delivery; sleep/restart; and
completion or pause before the timer fires. Test actual receipt in the intended
parent through a harmless event. Keep the existing model selection and billing
route. Do not exhaust real usage or start real builds just to test the watcher.

## Claude Design details

Read Anthropic's current model and effort guidance for every recommendation, then judge the
individual design task, following `../skills/model-effort/SKILL.md`. Inspect the actual Design
picker for the supported pair; API effort names and product labels need not match.

Use the skill's [Design evidence check](../skills/model-effort/SKILL.md#claude-design-establish-the-recommendations-evidence-limit-up-front)
before the first recommendation. Separate available controls, provider guidance and comparable
Design outcomes. Give the expected model benefit and effort rationale separately; without a
relevant comparison, present a task-specific starting choice rather than a proven winner.
Fresh comparisons are not required for ordinary recommendations. If both alternatives have
a substantial task-specific case, explain the tradeoff and preferred pair, then let the user
choose before starting the affected Design work.

Observed in Claude Design on 23 Sep 2026: the picker offers Opus 5.5, Fable 5.1, Sonnet 5 and
Haiku 4.5. For Opus 5.5, effort choices are Low, Medium (Default), High, Extra and Max. This is
an availability snapshot, not a standing recommendation. Always name both model and effort;
neither "Design (High)" nor "Design (Max)" is a complete recommendation.

## Cursor details

| Question | Answer |
| --- | --- |
| How are project rules loaded? | Project `AGENTS.md` and `.cursor/rules/` files carry project-specific instructions. If your setup also maintains a copied global rule, refresh it from its source before use and verify that Cursor reads it. The copy process is your setup, not a built-in promise. |
| How are personal skills loaded? | Inspect the current host's documented skill locations. A shared `~/.agents/skills/` folder can avoid separate copies when each installed tool supports it. |
| Can the model change in the same chat? | Yes, the user can use the model picker. Cursor CLI also provides `/model`. Each chat tab keeps its own selection. |
| Can the running agent change its own model? | Do not assume so. Use the visible picker or a documented launch setting and verify what actually ran. |
| What does Auto do? | Cursor chooses a premium model for the immediate task and current reliability. Use a manual choice when exact cost or model identity matters. |
| What does Max Mode do? | It expands available context on supported models and consumes more usage. Reserve it for unusually large or difficult work. |
| Can helpers choose a model? | Current Cursor versions support model selection for custom helpers. Treat built-in helper routing as host-controlled unless the actual setting is visible and verified. |
| What about background agents? | They use paid API-priced model usage and require a spending limit. They cannot read local-only global rule links, so rely on committed project instructions. Apply the large-cost comparison before launching them. |

## When a launch control permits a choice

All of these must be true:

1. The current host exposes the model or reasoning field for that kind of launch.
2. The selected model supports the requested reasoning level.
3. A higher-priority company, environment, or account setting does not lock it.
4. The launch shape meets the tool's rules, such as Codex's limited-history rule
   for an overridden helper.
5. Delegation itself is appropriate: the work is bounded, can be explained
   completely, and will not collide with another task.

## Task routing table

These are candidate work shapes, not automatic choices; apply the selection procedure first.

| Work shape | Model role | Reasoning | Execution choice |
| --- | --- | --- | --- |
| Existing visual rules plus a screenshot or fixed target with one checkable answer | Balanced | Standard through deep | Apply the approved pattern and check the result |
| New visual direction, conflicting evidence, or several strong answers | Frontier | Deep through deepest useful | Keep the connected reasoning together |
| Hard diagnosis or unclear requirements | Frontier | Deep through deepest useful | Keep the connected reasoning together |
| Clear routine edit | Fast | Light or standard | Use checks to catch simple mistakes |
| A small hard decision plus much routine work | Frontier for the decision; faster workers for routine parts | Match each part | Split only independent parts |
| Builds, downloads, scraping, or large file movement | Fastest quality-safe | Light or standard | Improve batching and safe parallel work; more thinking rarely makes waiting faster |
| Production writes, money, access, or irreversible work | Strongest level needed for correctness | Deep through deepest useful | Do not trade verified quality for speed |

## Large cost or speed differences

Before an expensive, slow, long-running, or unattended job, compare the viable
paths. Show speed, money, and quality before starting. Stop for the user when an
equivalent path is about 3 times faster, about 2 times cheaper on a meaningful
base, or saves about $100 or more.

## Keep one maintained source

Keep portable rules, skills and guides in a versioned collection. Keep account
settings and private working notes separate. Do not assume a desktop chat, a
cloud agent and an uploaded project file share storage or editing rights.

| Material | Suggested home |
| --- | --- |
| Reusable routing workflow | [model-effort](../skills/model-effort/SKILL.md) |
| Model comparison evidence and review cases | [selection evidence](../skills/model-effort/references/selection-evidence.md) |
| Cross-tool control reference | This guide |
| Project behavior and permissions | That project's instructions and approved decisions |
| Account settings, credentials and private task notes | Private storage outside the public collection |

For each tool, verify which source it reads and whether it can edit that source.
A copied or uploaded guide can drift; name its maintained source and refresh it
before relying on it. A cloud tool cannot read a local path just because another
tool on the same account can. Inspect connector permissions instead of assuming
all GitHub connections are read-only or can write.

## Official references

| Topic | Source |
| --- | --- |
| Codex model roles and reasoning | <https://learn.chatgpt.com/docs/models.md> |
| Codex instruction loading | <https://learn.chatgpt.com/docs/agent-configuration/agents-md.md> |
| Claude Code model and effort controls | <https://code.claude.com/docs/en/model-config> |
| Claude Code commands | <https://code.claude.com/docs/en/commands> |
| Claude Code helper models | <https://code.claude.com/docs/en/sub-agents> |
| Claude Code portable skills | <https://code.claude.com/docs/en/slash-commands> |
| Cursor rules and `AGENTS.md` | <https://docs.cursor.com/context/rules-for-ai> |
| Cursor CLI project instructions | <https://docs.cursor.com/en/cli/using> |
| Cursor models and Max Mode | <https://docs.cursor.com/advanced/models> |
| Cursor helper model settings | <https://cursor.com/docs/subagents#model-configuration> |
| Cursor background-agent pricing | <https://docs.cursor.com/account/pricing> |
| ChatGPT Work and Codex separation | <https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex> |
| ChatGPT GitHub connection | <https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt> |
