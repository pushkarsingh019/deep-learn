# Mathematics, Proofs, and Code

## Moving baseline

“From scratch” begins at the lowest dependency not supported by current evidence. **No evidence means no assumed prerequisite.** As learning records accumulate, the starting point moves forward.

Before any source equation or formal definition, complete the ordinary-language on-ramp and obtain technical-depth consent. A direct request to understand a particular equation, proof, or implementation counts as consent for that item while the rules below still apply.

## Notation bridge

**Every symbol is introduced before it appears in an equation.** Preserve the anchor source’s notation, but introduce it through this sequence:

1. State the relationship in words.
2. Use a concrete numerical, geometric, or code example.
3. Introduce one source symbol: say how to read it aloud, what it refers to here, and its units, type, domain, or tensor shape.
4. Show the smallest expression containing that symbol and read the expression back into words.
5. Add one term at a time until the source equation has been reconstructed.
6. Translate the finished equation into words and code or behavior, then vary a value or assumption.

Keep notation explanations beside first use. Use a table only when comparing several symbols that the learner already understands. A dense end-of-lesson symbol table cannot repair notation introduced too early.

When a prerequisite would displace the current conceptual idea, create one linked prerequisite lesson and return afterward.

Completion: the learner can read the notation aloud, explain every term, reconstruct the equation’s logic, and connect it to a concrete case.

## Proof reconstruction

1. Explain what the claim says and why anyone needs it.
2. Audit every definition, symbol, lemma, and inference against the moving baseline.
3. Establish missing prerequisites through small examples.
4. Give the proof strategy without formal details.
5. Let the learner predict important moves; respond with progressively stronger hints.
6. After the attempt, record the complete source-faithful proof and justify each move in plain language.

Completion: the learner can explain the strategy, justify the key transitions, and read the source proof.

## Co-programming

1. Reduce the concept to the smallest behavior worth implementing.
2. Ask the learner to predict behavior and decompose the problem.
3. Give an editable code block for their attempt.
4. Preserve mistakes; use questions and progressively stronger hints to expose the missing model.
5. Add tests, debugging, and changed constraints after the core mechanism works.
6. Move into an IDE, repository, or notebook when execution becomes essential or the learner requests it.

Completion: the learner can reconstruct and explain the mechanism, including why the tests establish the intended behavior.
