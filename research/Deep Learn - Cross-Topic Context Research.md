---
type: research
status: draft
---

# Deep Learn — Cross-Topic Context Research

## Question

How should `deep-learn` use an Obsidian vault to carry relevant knowledge about the learner across topics without a centralized `Learner Model.md`, excessive structure, or indiscriminate full-vault reading?

## Recommendation

Use an **open, evidence-first, just-in-time learner context**:

- learning records remain the durable evidence;
- MOCs remain the global summaries and entry points;
- wikilinks and backlinks carry relationships;
- the agent retrieves a small relevant subgraph for the current learning decision;
- the agent exposes the assumptions it derives so the learner can correct them;
- no permanent global mastery score or hidden learner profile is maintained.

This combines the strongest ideas from open learner models, adaptive educational systems, research on prior knowledge and transfer, and graph-based retrieval without importing their heavier machinery.

## What the research says

### 1. A learner model should be evidence-based, dynamic, and inspectable

Open learner model research treats the model as a changing representation inferred from learning interactions. Bull and Kay distinguish models that are merely inspectable from models the learner can edit, challenge, add evidence to, or negotiate with the system. They argue that exposing the evidence and uncertainty can support accuracy, reflection, planning, control, and trust.

They also describe a useful alternative to aggressively compressing a learner into scores: keep long-term evidence and interpret it when needed. A model only needs enough structure to support the adaptation being performed.

**Implication for `deep-learn`:** learning records and preserved answer attempts should be the evidence store. The agent should derive temporary context from them and show the links behind its assumptions. The learner can answer “too obvious,” dispute a claimed connection, or demonstrate that earlier knowledge is stale.

Source: Susan Bull and Judy Kay, [“SMILI☺: A Framework for Interfaces to Learning Data in Open Learner Models” (2016)](https://doi.org/10.1007/s40593-015-0090-8), especially pp. 294–308. [Open PDF](https://link.springer.com/content/pdf/10.1007/s40593-015-0090-8.pdf).

### 2. One scalar mastery level is too crude

Adaptive-system research distinguishes a single scalar level such as “beginner” from an overlay model that tracks knowledge across domain elements. A scalar averages away uneven knowledge. Overlay models are more useful, but depend on a predefined expert domain model and can still mistake misconceptions for simple missing knowledge. Rich “bug models” can represent misconceptions, but are difficult to build and have mainly been practical in constrained problem-solving domains.

**Implication:** a multi-topic vault should not assign one expertise level to a topic or pretend to maintain a complete ontology of everything the learner knows. Preserve specific evidence about concepts, derivations, implementations, and misconceptions. Diagnose the relevant mental model during the current lesson.

Source: Peter Brusilovsky and Eva Millán, [“User Models for Adaptive Hypermedia and Adaptive Educational Systems” (2007)](https://sites.pitt.edu/~peterb/papers/1_BrusilovskyMillan.pdf), §1.2.1.

### 3. Prior knowledge helps and distorts

The National Academies reports that prior knowledge can lower attentional demands, help learners identify relevant information, and support new learning. It can also bias attention and cause an old schema to be applied where it does not fit. Experts’ useful knowledge is organized around concepts and conditionalized by when it applies, rather than stored as disconnected facts.

**Implication:** cross-topic links should be treated as hypotheses, not proof. A useful connection states the structural relationship and its boundary: prerequisite, analogy, contrast, or application. The agent should probe a critical connection when the evidence is weak rather than silently assuming transfer.

Sources:

- National Academies, [*How People Learn II*, Chapter 5: “Knowledge and Reasoning” (2018)](https://www.nationalacademies.org/read/24783/chapter/7), especially Conclusions 5-1, 5-3, and 5-4.
- National Research Council, [*How People Learn*, Chapter 1 (2000)](https://www.nationalacademies.org/read/9853/chapter/3), especially the sections on organized, conditionalized knowledge and transfer.

### 4. The vault already has the necessary graph primitives

Obsidian internal links create a knowledge network, backlinks expose linked and unlinked mentions, properties provide searchable structured data, and search can combine full text, properties, tags, files, sections, and blocks. The CLI can query links, backlinks, properties, and search results when Obsidian is available.

**Implication:** a separate global learner-model document would duplicate the graph. Minimal note properties support discovery; prose around wikilinks supplies the meaning of each relationship.

Sources: Obsidian’s official documentation for [internal links](https://help.obsidian.md/links), [backlinks](https://help.obsidian.md/backlinks), [properties](https://help.obsidian.md/properties), [search](https://help.obsidian.md/search), and the [CLI](https://help.obsidian.md/cli).

### 5. Reading the entire vault is not a sound retrieval strategy

Experiments on long-context language models found that access to a long context did not guarantee robust use of information: performance varied with the position of relevant evidence and could degrade in the presence of additional context. Model capabilities continue to change, but the result is a warning against treating “fits in the context window” as equivalent to “will be used well.”

**Implication:** progressively retrieve relevant evidence instead of loading every MOC and learning record.

Source: Nelson Liu et al., [“Lost in the Middle: How Language Models Use Long Contexts” (2024)](https://arxiv.org/abs/2307.03172).

### 6. Local and global retrieval solve different problems

GraphRAG research distinguishes local retrieval of specific records from global questions requiring sense-making across a corpus. Its proposed global method uses hierarchical community summaries, while local retrieval follows entities and relationships. The experiments concern corpus question-answering rather than education, so the implementation should not be copied uncritically.

**Implication:** topic MOCs can serve as human-visible global summaries. For a new topic, scan MOCs first; then use lexical search and one-hop link expansion to retrieve detailed learning records. A full GraphRAG index is unnecessary at the current scale.

Source: Darren Edge et al., [“From Local to Global: A Graph RAG Approach to Query-Focused Summarization” (2024/2025)](https://arxiv.org/abs/2404.16130).

## Approaches considered

### Option A — Central `Learner Model.md`

A manually maintained summary of all knowledge, weaknesses, and preferences.

- **Strength:** one obvious place to read.
- **Weaknesses:** becomes stale, duplicates records and links, compresses away evidence, and lets an unverified summary become authoritative.
- **Verdict:** reject.

### Option B — Read every MOC and learning record

- **Strength:** maximal nominal coverage.
- **Weaknesses:** attention dilution, irrelevant context, poor scaling, and false confidence that all loaded text influenced the decision.
- **Verdict:** reject.

### Option C — Follow wikilinks only

- **Strength:** simple and native to Obsidian.
- **Weaknesses:** misses relevant but not-yet-linked topics; a bare link does not explain whether the relation is a prerequisite, analogy, contrast, or coincidence.
- **Verdict:** use as one retrieval signal, not the entire method.

### Option D — Formal mastery scores or knowledge tracing

- **Strength:** effective in systems with predefined atomic skills and repeated structured observations.
- **Weaknesses:** requires a trustworthy domain decomposition and enough comparable trials. Open-ended essays, source reading, and cross-domain programming provide neither. Numeric precision would be misleading.
- **Verdict:** reject for the default vault model.

### Option E — Embeddings or full GraphRAG

- **Strength:** can discover semantically related notes and support corpus-level questions at large scale.
- **Weaknesses:** adds an opaque derived index, maintenance, and false-positive conceptual similarities. The vault is currently too small to justify it.
- **Verdict:** reconsider only after native search and links measurably fail.

### Option F — Hybrid evidence retrieval

Use MOCs for a global pass, search for cold-start discovery, links/backlinks for local expansion, and learning records as the evidence of what the learner knows.

- **Strength:** transparent, native to Obsidian, scalable enough, and resistant to a single stale summary.
- **Verdict:** recommended.

## Recommended retrieval procedure

### 1. Frame the present learning decision

Extract from the current source and MOC:

- the concept being taught;
- required prerequisites;
- likely analogies or contrasts;
- the kind of adaptation needed: skip basics, introduce an analogy, test a prerequisite, or revisit a misconception.

Retrieval is performed for this decision, rather than to answer the unbounded question “What does the learner know?”

### 2. Run a global MOC pass

Find notes with `type: moc`. Inspect titles, topics, statuses, mission summaries, and main wikilinks. Select MOCs plausibly related by mechanism or prerequisite, not merely by shared vocabulary.

This is a metadata-and-summary pass; it does not load every lesson.

### 3. Run a local evidence pass

For the strongest candidates:

1. search MOCs and learning records for the current concepts and important synonyms;
2. inspect outgoing links and backlinks one hop from the best matches;
3. retrieve the smallest set of records that can establish a prerequisite, analogy, contrast, or misconception;
4. follow a second hop only when the first hop contains an explicit reason to do so.

Use Obsidian CLI when available and filesystem search otherwise.

### 4. Rank by evidence, not note existence

Use this order:

1. completed capstone or reconstruction evidence;
2. a learning record backed by a preserved answer or implementation;
3. a learning record of user-declared prior experience;
4. an answer still under revision;
5. a lesson that was merely created or read.

A lesson note proves exposure, not understanding. If evidence is old, contradicted, or weak, treat the prior knowledge as uncertain.

### 5. Expose the derived context

When a prior topic changes the lesson, state the assumption and cite its note or block, for example:

> This lesson assumes you can reason about reverse-mode differentiation based on [[Autodiff - LR 0003 - Tracing a backward pass]]. If that no longer feels solid, revise this assumption before continuing.

The learner can confirm it, challenge it, or say the material is too obvious. A correction updates or supersedes the underlying learning record rather than being hidden in agent state.

### 6. Create meaningful links only when used

When a connection materially helps learning, write a sentence that explains the relation and add the wikilink in the current MOC or lesson. Backlinks provide reverse discovery automatically.

Good:

> Multi-head attention repeats the query–key–value interaction across learned subspaces; compare the role of subspaces in [[Representation Learning - Basis Changes]].

Weak:

> Related: [[Representation Learning]].

The first link records why the connection exists. The second only creates graph density.

### 7. Preserve uncertainty and revision

Learning records should distinguish demonstrated understanding from stated prior experience and support supersession when later evidence contradicts them. The agent reports a relevant assumption as supported, tentative, or contradicted—not as a percentage mastery score.

## Minimal properties

MOCs need only the already agreed properties:

```yaml
---
type: moc
topic: attention mechanisms
status: active
---
```

Learning records can remain equally small:

```yaml
---
type: learning-record
moc: "[[Attention Mechanisms MOC]]"
evidence: demonstrated
status: active
---
```

Use `evidence: stated` for prior knowledge reported by the learner. Use `status: superseded` when later evidence replaces a record. Concepts and relationships remain in prose and wikilinks unless native search demonstrably becomes inadequate.

## Completion criterion for cross-topic retrieval

The retrieval step is complete when the agent can answer all four questions with linked evidence or explicitly say that no evidence exists:

1. Which prior knowledge can safely be reused?
2. Which prerequisite is uncertain enough to probe?
3. Which prior misconception could interfere?
4. Which cross-topic connection materially improves this lesson?

If none is relevant, the correct outcome is to add no cross-topic context.

## Scaling path

1. **Now:** properties + search + wikilinks/backlinks + runtime evidence retrieval.
2. **As the vault grows:** use MOCs as global summaries and optionally run a user-requested synthesis pass to repair missing links.
3. **Only after observed retrieval failures:** evaluate embeddings or a graph index against real missed connections before adopting it.

## Research limits

Open learner model and knowledge-tracing studies usually operate in bounded curricula with structured interaction data. GraphRAG studies corpus question-answering, not pedagogy. Applying them to an open-ended personal learning vault is a design synthesis, not a directly validated learning intervention. The transparency and correction loop are therefore essential safeguards.
