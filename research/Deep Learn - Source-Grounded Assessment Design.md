---
type: research
status: draft
---

# Deep Learn — Source-Grounded Assessment Design

## Question

How can `deep-learn` create a capstone from an original paper, textbook, or codebase without making the assessment circular or allowing one faulty up-front map to compromise the learning experience?

## Finding

A single “competency map” should **not** be load-bearing. Assessment research supports maintaining an explicit account of the intended domain, but treats that account as revisable and treats every assessment as an uncertain inference from limited evidence—not as proof that a complete mental model has been captured.

The safer design separates three things:

1. a factual inventory of the source;
2. the learner’s adaptive path through it;
3. a fresh assessment argument created from the source at capstone time.

## What the research says

### 1. Assessment is inference, not direct access to understanding

The National Research Council describes assessment as reasoning from a small set of observed performances to claims about knowledge that cannot be observed directly. Its “assessment triangle” requires three coordinated elements: a model of cognition in the domain, observations that can expose relevant thinking, and a method for interpreting those observations. It also stresses that the elements usually require repeated refinement.

**Implication:** no source map can guarantee a sound capstone. The skill should preserve uncertainty and seek converging evidence from essays, explanations, debugging, and implementation rather than treating one answer as decisive.

Source: [National Research Council, *Knowing What Students Know*, Chapter 2 (2001)](https://www.nationalacademies.org/read/10019/chapter/4), especially the sections “Reasoning from Evidence” and “The Assessment Triangle.”

### 2. The two main validity failures match the concern

The *Standards for Educational and Psychological Testing* names two central threats:

- **construct underrepresentation**: the assessment omits important aspects of what it claims to measure;
- **construct-irrelevant variance**: performance depends on something outside the intended target.

For `deep-learn`, a bad source map can cause underrepresentation. An essay whose result mostly reflects prose fluency, or a coding task dominated by setup syntax, can introduce irrelevant difficulty.

The Standards also says validity belongs to a particular interpretation and use, rather than to a test in the abstract. Here the intended interpretation is narrow: “this response is evidence about the learner’s understanding of the included portion of this source.”

Source: [AERA, APA, and NCME, *Standards for Educational and Psychological Testing* (2014)](https://www.testingstandards.net/uploads/7/6/6/4/76643089/9780935302356.pdf), pp. 11–15.

### 3. Source coverage and cognitive demand both matter

The Standards recommends checking whether assessment content samples the intended domain and whether each task’s cognitive demand matches the intended learning. For a delivered curriculum, it says the assessed domain should be limited to material learners had an opportunity to learn.

**Implication:** deferred and skipped material should be removed by source location and concept—not merely by deleting lesson titles. The capstone must also test derivation, causal explanation, or reconstruction when those are the intended depths; factual recall is not an adequate substitute.

Source: [*Standards* (2014)](https://www.testingstandards.net/uploads/7/6/6/4/76643089/9780935302356.pdf), pp. 14–15 and 75–80.

### 4. Specifications are useful precisely because they are revisable

The Standards calls for content specifications, but explicitly notes an interplay between defining a domain and developing tasks: specifications may need refinement as development proceeds. It recommends performance tasks when the target is an applied process and analytic scoring when diagnosis across several dimensions is important.

**Implication:** keep a source-grounded ledger, but treat every conceptual decomposition as a hypothesis. Revise it when teaching, learner answers, or capstone design exposes a missing dependency.

Source: [*Standards* (2014)](https://www.testingstandards.net/uploads/7/6/6/4/76643089/9780935302356.pdf), pp. 75–80.

### 5. Claims, evidence, and tasks should be designed together

Evidence-Centered Design asks:

1. What knowledge or skill is the assessment meant to reveal?
2. What observable features of the learner’s work would support that inference?
3. What task would elicit those features?

Its task models describe families of tasks, not one memorized question. Multiple task forms can probe the same understanding under changed conditions.

**Implication:** each capstone prompt should be justified by a small source-grounded claim → evidence → task chain. A second attempt should use a new task from the same family rather than repeat the old prompt.

Source: Robert Mislevy, Russell Almond, and Janice Lukas, [“A Brief Introduction to Evidence-Centered Design” (ETS/CRESST, 2003)](https://files.eric.ed.gov/fulltext/ED483399.pdf), pp. 4–12.

### 6. Deep understanding should support novel reasoning

The National Academies’ synthesis on learning distinguishes accumulated information from organized knowledge that can be used flexibly for inference and unfamiliar problems. It also recommends deep-reasoning prompts such as why, how, what-if, and what-if-not, while warning that explanations can hide missing specifics behind an overly simple story.

**Implication:** capstones should include changed assumptions, counterexamples, debugging, or transfer—not paraphrases of lesson questions. Evaluation should inspect both the broad explanation and the source’s important technical particulars.

Source: National Academies of Sciences, Engineering, and Medicine, [*How People Learn II*, Chapters 5 and 7 (2018)](https://www.nationalacademies.org/read/24783/chapter/7) and [assessment section](https://www.nationalacademies.org/read/24783/chapter/9).

## Design options

### Option A — Static competency map

Create one conceptual map at intake and use it for curriculum and assessment.

- **Benefit:** simple and coherent.
- **Failure:** one omission contaminates teaching, scope tracking, and assessment simultaneously.
- **Verdict:** reject as the sole source of truth.

### Option B — Fresh capstone directly from the source

At the end, reread the source and generate questions while consulting a list of skipped lessons.

- **Benefit:** less lesson-circular.
- **Failure:** skipped lesson titles may not map cleanly to source sections; a fresh unstructured pass can still omit major ideas or test incidental details.
- **Verdict:** safer than Option A, but insufficient by itself.

### Option C — Source ledger plus a fresh assessment argument

Maintain a factual, cited source ledger during learning. At capstone time, derive claims and tasks afresh from in-scope source anchors, then audit the result.

- **Benefit:** no single conceptual map controls everything; provenance and omissions are inspectable; the curriculum remains adaptive.
- **Cost:** requires an explicit capstone audit.
- **Verdict:** recommended.

### Option D — External or author-provided assessment

Prefer exercises, tests, replication targets, unresolved examples, or implementation requirements supplied by the original source when they genuinely test the desired depth. Supplement them where coverage is weak.

- **Benefit:** strongest break from model-generated circularity.
- **Failure:** many sources have no assessment, and available exercises may emphasize chapter order or routine manipulation.
- **Verdict:** use opportunistically inside Option C, not as the only method.

## Recommended design

### During source intake

Create two MOC sections:

#### Source ledger

A factual index with precise anchors:

- textbook: chapters, sections, central derivations, exercises;
- paper: sections, claims, figures, equations, algorithms, experiments, limitations;
- codebase: modules, public interfaces, execution paths, tests, and important symbols.

This inventory says **what is present**, not what mastery must look like. Every item points back to the source.

#### Learning path

Arrange concepts by dependency and mark each `planned`, `in progress`, `learned`, `deferred`, or `skipped`. Each lesson links to its source-ledger anchors. This path may change freely as understanding develops.

### Before the capstone

1. Reopen and rescan the original source.
2. Build the assessment scope from source anchors linked to `learned` lessons.
3. Show the learner only a concise included/excluded scope summary and ask for confirmation.
4. Prefer suitable author-provided exercises or repository tests where available.
5. For each generated prompt, privately define:
   - the source-grounded claim about understanding;
   - observable evidence that would support or weaken it;
   - a task capable of eliciting that evidence.
6. Select one or two synthesis essays and, where appropriate, one implementation task that jointly sample the included source.

### Audit before revealing prompts

For every prompt and scoring criterion, verify:

- **Provenance:** it traces to exact original-source anchors.
- **Scope:** it uses learned material and excludes deferred/skipped material.
- **Coverage:** the small prompt set samples the central in-scope mechanisms rather than an easy corner.
- **Depth:** its cognitive demand matches the intended first-principles depth.
- **Transfer:** it changes an example, condition, constraint, or failure mode from the lessons.
- **Relevance:** success depends on target understanding rather than prose polish, memorized wording, or incidental syntax.
- **Diagnostic power:** plausible wrong answers expose distinguishable missing mental models.

If an audit fails, revise the prompt before showing it.

### Evaluate with converging evidence

Use an analytic, source-specific rubric rather than one opaque score. Typical dimensions may include:

- motivation and problem framing;
- causal or mathematical mechanism;
- assumptions and limitations;
- derivation or reconstruction;
- behavior under changed conditions;
- implementation decomposition, correctness, and tests.

Report each inference as `strong evidence`, `partial evidence`, or `insufficient evidence`. Explain the observed evidence and plausible alternative explanation. Weak dimensions generate targeted lessons and a new task form.

## Why this is safer

The design has no all-powerful “competency map.” A factual source ledger protects provenance; an adaptive learning path tracks opportunity to learn; and a fresh claim → evidence → task argument controls each assessment. Independent source rescanning and an explicit audit provide redundancy. If one representation is weak, another can expose and correct it before the capstone reaches the learner.

## Remaining limitation

The same agent may still interpret the source imperfectly across all passes. No prompt structure removes that risk. For unusually important or difficult material, the strongest additional safeguards are:

- author-provided assessment artifacts;
- executable tests or empirical reproduction;
- comparison with an authoritative external syllabus or expert review;
- a separate evaluator reviewing source coverage and capstone tasks when available.
