---
name: deep-learn
description: Build durable, first-principles understanding of a source or topic in a persistent Obsidian vault.
argument-hint: "Topic, source, or action: continue, answered, deeper, or capstone"
---

# Deep Learn

Run a source-grounded, file-first learning process. The durable interaction happens in Obsidian; chat points to the current note and next action.

The leading word is **on-ramp**: build the motivating problem and core intuition in ordinary language before formal machinery. An on-ramp is complete only when the learner can explain the central relationship without borrowing unexplained source notation.

## Every invocation

1. Read [CONFIG.md](CONFIG.md), resolve `vault_root`, and verify it is writable. Read `Teaching Notes.md` for durable learner preferences and honor them. Write every learning artifact beneath that root. Completion: the vault, target topic, and recorded preferences are known.
2. Route from the request and vault state:
   - new source/topic or continue → [CURRICULUM.md](CURRICULUM.md)
   - author or revise a lesson → [LESSONS.md](LESSONS.md)
   - mathematics, a proof, or programming → also [MATH-AND-CODE.md](MATH-AND-CODE.md)
   - answered questions or “too obvious” → [REVIEW.md](REVIEW.md)
   - prior learning may change the baseline → [CONTEXT.md](CONTEXT.md)
   - capstone → [CAPSTONE.md](CAPSTONE.md)
   - create or edit any note → [FORMATS.md](FORMATS.md) and the installed `obsidian-markdown` guidance
   Completion: every applicable branch is loaded before editing.
3. Perform the routed work. Preserve learner writing and source notation. Completion: the requested learning action exists in its durable note.
4. Reconcile the MOC so **Now**, lesson states, links, and records match reality. Completion: opening the MOC immediately reveals what to read or answer next.
5. Open the active note in Obsidian when available; otherwise report its absolute path. Keep chat to a brief summary and one next action.

## Hard gates

- The source survey is backstage legwork; the learner-facing entry point is the current idea.
- No evidence means no assumed prerequisite. Teach from ordinary language until the vault demonstrates a higher baseline.
- Before technical-depth consent, keep source equations, formal definitions, proof machinery, and function-space notation out of the lesson. A direct request for one of these counts as consent for that request.
- Every technical term and symbol is explained before use.
- One lesson develops one conceptual idea through coherent prose, not a repeated courseware template.
- The first active lesson is authored fully. Until its checkpoint supplies evidence, the next two lessons remain outline-only.
- Treat a supplied source as the anchor; verify factual and historical claims from it or another primary source.
- Lessons speak the topic glossary's language; a term enters the glossary only once the learner has demonstrated it.
- Use Markdown and meaningful wikilinks. Add a visual only when it makes a hard relationship easier to reason about.
