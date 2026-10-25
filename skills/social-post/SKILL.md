---
name: social-post
description: Draft a social post for the user about AI engineering, working with
  coding agents, or a lesson learned from a build. Use for X, LinkedIn, or any
  similar short public post. Invoke before writing the first draft, not after.
---

# Drafting concise social posts

An opinionated house-style example for short posts about lessons from AI engineering.
Apply it when the user chooses this style; their approved voice and platform needs
control. Drafting does not authorize publication.

Front-load concision. Revise against the requested meaning and evidence, not a
fixed number of rounds.

## Skeleton

Keep this order. It survived every round:

1. Credit, if the idea built on someone else's work.
2. What it was supposed to do.
3. What went wrong, in 1 sentence.
4. `Reason:` the cause, in 1 sentence.
5. `The fix:` what was done, in 1 sentence.
6. `N things proved:` then the principles, 1 short paragraph each.
7. A line pointing at the attached evidence.
8. The ask.

Blank line between every block. No headers, no bullet characters, no numbered
lists in the post itself.

## Opening and credit

- Fold the credit and what it achieves into 1 sentence, not 2 blocks.
  Shape: "Thanks to X for the Y that makes Z do W."
- Name the platform when the handle is from a different one than the post.
  "@author on X" when the post is going to LinkedIn (replace with the actual source).
- Bold only the single key phrase in that sentence. Nothing else in the whole
  post is bold.

## Wording

- Pick the accurate word over the dramatic one. "Worked initially" beat
  "worked great." "Partway into a coding session" beat "deep into a long
  session."
- Label a block with a bare noun and a colon. "Reason:" not "The reason was
  simple." State the reason; never announce that it is simple. Simplicity
  shows in the sentence length, not in a claim about it.
- Cut quantifiers that carry nothing. "Later" beat "Hours later."
- Prefer the construction without a pronoun. "2 things proved" beat "2 things
  it proves."
- Never write as "I", "me", "we", or "our". State what was done.
- Cut the second supporting detail when the first already lands.
- Cut any context the following lines already imply.
- Numbers are numerals. Always.
- No em dashes.

## Closing ask

- Ask directly. Delete any lead-in such as "Curious what others think."
- Compress to the shortest true form. "Drop your tips for simplifying AI
  engineering" beat "Drop your tips for making complex engineering work
  easier with AI."
- The ask invites others to share what makes working with AI on complex
  engineering easier. It is not about getting more out of AI.

## The attached evidence

When the post makes a claim that a screenshot supports, attach the relevant
evidence and reference it in 1 line. Name the actual tool or model only when known.

What makes a useful evidence attachment:

- **The coding agent's own unedited words**, first person. It is a receipt, so it must
  not look rewritten.
- **A plain-language header** that states the exact question the post raises.
  Example: "Why the reminder worked when the instruction alone did not."
- **The failure admitted in the first clause**, before any claim of success.
  Example: "The rule was already there and I still drifted." Use a real quotation
  only when the evidence actually contains it.
- **A concrete true-or-false contrast** at the end that proves the principle,
  rather than restating it.
- **3 sentences.** Long enough to prove the mechanism, short enough to read
  inside an image.

Useful asymmetry: author-specific rules can stay out of the post body while an
approved public example appears in the evidence image. A screenshot has the same
privacy and publication boundary as the post. Include only details approved for
that audience; redact unrelated private content, mark redactions and retain the
original privately. Preserve the meaning of any quoted evidence.

## Formatting traps

- Inspect how the destination renders filenames such as `CLAUDE.md`. If a filename
  becomes an unintended link, use a plain-text form such as "CLAUDE md".
- At most 1 emoji, on the payoff line only.
- Use the link format native to the destination platform.
