# Note Formats

Keep the vault flat. Formats provide a small durable frame, not a prose template.

## Topic MOC — `<Topic> MOC.md`

The MOC is the learner’s front door. It contains **one short source summary** and links to a separate `<Topic> - Source Map.md` for dense coverage.

```md
---
type: moc
topic: <topic>
status: active
---

# <Topic>

## Now
**Read:** [[<Topic> - <Current idea>]]
**Answer:** [[<Topic> - <Current idea>#Checkpoint]]
**Waiting for:** <one concrete learner action>

## Mission
<Why this source matters and what the learner ultimately wants to reconstruct or judge.>

## Learning path
### 1. <Current phase>
- **active** — [[<Topic> - <Current idea>]]
- **outline** — [[<Topic> - <Next idea>]]

### 2. <Later phase>
- <A short conceptual destination, without prewriting every lesson>

## Source
<One short source summary.>

- Anchor: [[<source file>]] or [external source](url)
- Coverage: [[<Topic> - Source Map]]
- Additional primary resources only when needed

## Language
- [[<Topic> Glossary]]

## Learning records
- [[<Topic> - LR 0001 - <Insight>]]

## Connections
<Only links whose relationship is explained in prose.>
```

Keep **Now** near the top and source inventory out of the MOC.

## Source map — `<Topic> - Source Map.md`

```md
---
type: source-map
moc: "[[<Topic> MOC]]"
status: active
---

# <Topic> source map

Topic map: [[<Topic> MOC]]

## <Conceptual phase or source region>
- <Exact source anchor> — <what is present and why it may matter>
```

This note may be dense. It supports curriculum and capstone audits; it is not the starting lesson.

## Lesson — `<Topic> - <Concept>.md`

```md
---
type: lesson
moc: "[[<Topic> MOC]]"
status: active
---

# <Concept-specific title>

Topic map: [[<Topic> MOC]]

<Use a small number of descriptive headings chosen for this idea. Write a connected explanation rather than copying generic lesson sections.>

## Checkpoint

### Q1 — <Question about the idea itself>
**Status:** awaiting response

**Your answer — attempt 1:**

<!-- Write your answer above this line. -->

^checkpoint-q1

## Source
- [[<source>#page=<n>|<precise anchor>]] — <what it supports>
```

During review, append `**Agent feedback:**` and `**Your revision — attempt 2:**` beneath the preserved attempt.

## Outline draft — `<Topic> - <Future concept>.md`

```md
---
type: lesson
moc: "[[<Topic> MOC]]"
status: outline
---

# <Future concept>

## Purpose
<The single idea this may teach.>

## Depends on
- <Evidence that must exist before authoring>

## Source anchors
- <Exact source locations>
```

## Learning record — `<Topic> - LR NNNN - <Insight>.md`

```md
---
type: learning-record
moc: "[[<Topic> MOC]]"
evidence: demonstrated
status: active
---

# <Insight>

<What the learner demonstrated and why it changes future teaching.>

Evidence: [[<Topic> - <Concept>#^checkpoint-q1]]
```

Use `evidence: stated` for disclosed prior knowledge. Supersede a contradicted record by linking its replacement.

## Glossary — `<Topic> Glossary.md`

The canonical language of the topic. Lessons draw their terms from here; a term is added only once the learner has demonstrated it.

```md
---
type: glossary
moc: "[[<Topic> MOC]]"
status: active
---

# <Topic> glossary

Topic map: [[<Topic> MOC]]

**<Term>**: <One or two sentences defining what the term is, in the learner's own words.>
_Aliases to avoid_: <competing words for the same concept>
Evidence: [[<Topic> - <Concept>#^checkpoint-q1]]
```

Prefer the glossary's own terms inside later definitions. Group under subheadings only when natural clusters emerge. Revise a definition in place as understanding deepens.

## Teaching notes — `Teaching Notes.md`

Durable learner preferences about how to teach, read at the start of every invocation. Pedagogical only; knowledge evidence belongs in learning records.

```md
---
type: teaching-notes
status: active
---

# Teaching notes

- <A stated preference: pace, example-first, notation tolerance, session length, format.>
```

One shared note across the vault. Record a preference when the learner states it; revise when it changes.
