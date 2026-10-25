# Agent Playbook

Reusable skills and practical guides for working with AI agents: clear tasks, evidence-based decisions, useful reviews and verified results.

**[Browse the complete skills and guides catalog](CATALOG.md).** It includes full skill instructions and supporting references, shared guides, and links to tools maintained by their original publishers.

## Start here

| When you need to… | Start with |
| --- | --- |
| Give an agent a task it can finish without guessing your intent | [Write a clear task brief](guides/task-brief.md) |
| Find the cause of a bug | [Systematic debugging](skills/systematic-debugging/SKILL.md) |
| Understand conflicting or bloated agent instructions | [Context audit](skills/context-audit/SKILL.md) |
| Choose a model, reasoning level and work method | [Model and effort selection](skills/model-effort/SKILL.md) |
| Review follow-up work before acting | [Follow-up audit](skills/loop-audit/SKILL.md) |
| Create readable reports and presentations | [Presentation rules](skills/presentation-rules/SKILL.md) and [report rules](skills/report-rules/SKILL.md) |
| Publish social content with working links and the right format | [Social publishing](guides/social-publishing.md) |
| Decide whether a change is ready to use | [Verify the result](guides/verify-the-result.md) |

## Use a skill

A skill is a folder with an instruction file named `SKILL.md`. Keep the whole collection together so links to shared guides and supporting files continue to work.

```sh
git clone https://github.com/euglopi/agent-playbook.git
```

Open the checkout in your coding assistant and ask it to read the skill you need, for example:

```text
Read skills/systematic-debugging/SKILL.md and its relevant references.
Use that method to investigate this bug: [describe the failure and how to reproduce it].
Keep the work within my project's existing permissions and the scope of this request.
```

Use the full checkout path if your project is in another folder. Some skills require browser access, repository tools or project-specific inputs. Read those requirements before running them. The collection does not install tools, grant permissions or start background jobs.

For third-party skills, follow the publisher's setup instructions linked in the [catalog](CATALOG.md#skills-maintained-by-other-publishers).

## The working principles

- Describe the result a person needs, not just the file to edit.
- Let the agent decide routine implementation details within the agreed scope.
- Keep product choices, spending and access boundaries explicit.
- Test the path a person will actually use, including failures and recovery.
- Keep evidence of what works and say plainly what remains unknown.
- Save useful lessons where the next task will find them.

## Suggest an improvement

[Open an issue](https://github.com/euglopi/agent-playbook/issues) with the skill or guide, the situation where it fell short, and a concrete example. Remove private project details before sharing. Proposed edits are welcome through pull requests; see [contribution guidance](CONTRIBUTING.md).

## License

Original material is under [MIT](LICENSE). Included adaptations retain the licenses and credits listed in [THIRD_PARTY.md](THIRD_PARTY.md). Linked external skills remain under their publishers' terms.
