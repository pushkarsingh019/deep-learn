# Review

Use this branch when the learner says they answered, revised, or found a question too obvious.

## Review loop

1. Read every `awaiting response` item in the active checkpoint. Preserve each learner answer exactly.
2. Compare the response with the anchor source and the mental model the task was designed to expose.
3. Add feedback beneath the attempt:
   - what is correct and why;
   - the earliest point where the reasoning or implementation diverges;
   - what that reveals about the underlying model;
   - one actionable revision direction.
4. When the gap is ambiguous, add a targeted diagnostic question that distinguishes plausible misconceptions. Increase difficulty only as evidence supports it.
5. Add a revision area beneath the feedback. Repeat until the answer demonstrates the intended idea, then mark that question `resolved`.
6. If the learner says **too obvious**, remove that exact question from the evaluation. Attach no additional status or inference to the phrase.
7. Update the lesson, MOC checkpoint link/status, and provisional drafts to reflect the evidence.

Completion: every submitted answer has source-grounded feedback, unresolved gaps have diagnostic next actions, and learner-authored attempts remain intact.

## Learning records

Create a learning record only when the learner:

- demonstrates non-trivial understanding;
- states meaningful prior knowledge;
- corrects a misconception; or
- changes the mission because of learning.

Use `evidence: demonstrated` or `evidence: stated`. Link demonstrated records to the exact lesson heading or block that contains the evidence. Number records per topic by incrementing the highest existing `<Topic> - LR NNNN` note. When later evidence contradicts a record, mark it `superseded` and link its replacement.

Coverage alone is not learning evidence. Each record states what is now known and why it changes future teaching.

## Glossary

When a checkpoint or revision shows the learner can use a term correctly in their own words, promote it to the topic glossary. Compressing the concept into a tight definition is itself evidence of understanding, so co-author the entry from the learner's phrasing rather than the source's. Add a term only after such evidence exists; keep it out of the glossary while it is merely introduced. Pick one canonical term per concept and list competing words as aliases to avoid. When later evidence sharpens or corrects a definition, revise the entry in place so every future lesson inherits the current language.

## Teaching notes

When the learner states how they want to be taught—pace, example-first, notation tolerance, session length—record it in `Teaching Notes.md`. This note holds pedagogical preferences only; knowledge evidence still belongs in learning records.
