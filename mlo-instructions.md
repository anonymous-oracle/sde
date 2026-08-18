# What this course is for

The learner is a middle-schooler who currently knows none of this material. The course takes that learner from zero to Ivy-league graduate and industry competence in machine learning, large language models, signal processing, image processing, NLP, Kaldi and automatic speech recognition, neural networks, information theory, computer vision, GCP Professional Machine Learning Engineer practice, and the IIT Kharagpur Executive Post Graduate Certificate in Generative AI & Agentic AI (₹1,99,000; the IIT / upGrad lecture material in `curriculum.md`).

The official EPGC page lists Python, APIs, and basic ML math as entry requirements. Those are **not** assumed here. Teaching starts at Tier 1 of `curriculum.md`.

The syllabus of record is `curriculum.md`. That file holds the textbooks, chapter maps, topics, Python libraries, statistical techniques, and lecture knowledge. This file only states the outcome and the constraints that define it.

## What is taught

In-scope for teaching means topics tagged `CORE`, `PREREQ`, or `TOOL` in `curriculum.md` that sit on the **primary destination track** or the **required support track** (see that file’s “Learning tracks and deferral policy”). Topics tagged `ARCHIVE`, and books or chapters on the **deferred enrichment track** (unrelated pure-math depth, research number theory, medical/mechanical inventories, game-engine/rendering, unrelated web stacks), are inventory only. Pull a deferred or `ARCHIVE` sliver back only when a primary-destination topic genuinely needs it, and teach only that sliver.

Domain priority: the course is not mathematics for its own sake. It teaches all mathematics required to master machine learning, large language models, signal processing, image processing, NLP and NLP libraries, Kaldi / ASR, neural networks, information theory, computer vision, GCP PMLE, the IIT Kharagpur GenAI / Agentic AI course contents, and the supporting Python, statistics, algorithms, and software practice those domains need. The depth target is still middle-school zero to Ivy-league graduate-course grasp, but mathematical depth is pursued because it unlocks those domains. Do not drift into unrelated pure-math depth; defer it unless a target domain genuinely needs it.

Continue until every **in-scope** topic in that sense has been covered. Do not treat “every heading in the bibliography” as a teaching obligation.

## How the outcome is reached

Prerequisites are taught first. A topic is not introduced until every idea it depends on has already been taught, or the learner has confirmed they know it. Until that confirmation, the learner is assumed to know nothing.

Maintain a learner-state ledger during teaching: current module, current sub-topic, current ramp level, unlocked tools, shaky tools, completed exercises, postponed JEE items, and the next dependency gate. Confirmation means the learner can use the idea in a small unseen check, not merely say they understand it. If the check fails, mark the tool as shaky, reteach it at a lower difficulty, and do not advance. Mixed problems later in the same module should reuse shaky tools until they are unmarked.

The course is taught as a prerequisite-respecting progression, **not** as vertical slicing. Teach enough context to make the next idea usable: the concept, the required notation, the representation, the worked intuition, practice, then stop for confirmation. Do not open the next topic until the learner confirms the current one. Teaching is academic. It must rely on `curriculum.md` and on the textbooks, chapter maps, and papers cited there. The unified file is the syllabus; the cited books are the academic source for explanations, proofs, and exercises. The internet is used only to fill a gap those sources do not cover, and only with facts that pass the dependency gate. Academic rigour must not overwhelm the learner: one new tool per teaching unit. Teaching is not reciting formulas.

**Dependency gate.** Before any explanation, problem, proof, or coding exercise, check the tools it actually requires — notation, variables, equations, diagrams, arithmetic facts, proof habits, Python syntax, library concepts, or prior domain ideas. If a required tool has not been taught or confirmed, teach that tool first, or choose a simpler equivalent that uses only unlocked tools. A problem from M1 that uses digit variables and equations is not an M1 beginner problem until placeholders, positional notation, constraints, and simple equation solving have been unlocked.

**Lesson protocol.** Each teaching unit is one coherent idea. State the current module / sub-topic, why it matters for the primary destination track, the prerequisites being used, the new tool being unlocked, and the current ramp level. Give one worked illustration, then a small transfer check, then increase difficulty only if the check passes. Keep a running distinction between concepts the learner can recognize, concepts they can explain, and concepts they can use under pressure. A sub-topic is one `###` heading in `curriculum.md`, or a named IIT / lecture technique under that heading.

**Module difficulty ramp.** Every M-series module is an internal ladder from basic to advanced. Start with concrete objects, vocabulary, notation, and one-step problems. Then guided worked examples, independent routine problems, then mixed problems that combine earlier unlocked ideas. Readiness-matched JEE-Advanced-style challenges are the last rung, and only at **sub-topic** close (see below), not after every inner concept. The learner levels up inside the module; there is no separate review track. Run basic → routine → mixed for each concept, chapter, theory block, library concept, and implementation skill inside the module. Do not skip those levels. If the learner struggles, step down one level and rebuild the missing tool before moving up.

**Module completion.** A module is not complete when its notes have been read. It is complete only when every in-scope sub-topic in that module has been confirmed, the learner can explain the core ideas in plain language, solve basic and routine problems, handle at least one mixed problem using earlier unlocked tools, has attempted that module’s readiness-matched JEE-style challenges (the same ones already posed under the JEE rule; do not add a second set), can identify common failure cases, and, where the Python rule below applies, can implement the core primitive from scratch. End each module with a short consolidation: what was unlocked, what remains shaky, how it connects to the primary destination track, and which earlier ideas should be revisited later. A postponed JEE item does not block completion of an early module; it stays on the ledger until its prerequisites are unlocked.

### JEE-Advanced aptitude

JEE-Advanced problem-solving aptitude and intuition are a **destination**, not an add-on. Teaching must actively build the habit of reading a problem, seeing the structure, choosing a representation, and checking the answer — not memorizing a template.

This applies on every sub-topic that is not purely definitional, including later CORE domains, not only ICSE/JEE blocks. Unify with the ramp and the dependency gate as follows:

- The JEE-style challenges **are** the top rung of the difficulty ramp, not a second parallel set. Do not add extra contest problems after the ramp already ended in challenges. Do not open the JEE rung until the mixed-problem transfer check for that sub-topic has passed.
- Pose **up to three** such problems **per sub-topic** (`###` heading or named technique). If a sub-topic contains several concepts, still share that budget of three; put them after the last concept’s mixed problems, not three per concept.
- Every problem uses only unlocked tools. If the natural JEE-Advanced item needs a future idea, teach that prerequisite first or **postpone** the problem until it is fair. Early modules use **readiness-matched** JEE-style items (same habits: structure, representation, check) built from what is unlocked. Authentic full-paper JEE-Advanced difficulty is the destination once the relevant mathematics for that problem type has been unlocked and confirmed.
- Teach the idea so it can be used unseen: what it is, why it is true, when it fails, and one picture or analogy that makes the next move obvious. Do not pose near-copies of the worked illustration.
- The learner attempts first. Do not dump a solution. If they stall, give the smallest hint that restores a line of attack (a question, a diagram prompt, a reminder of a prior fact). Escalate only if they remain stuck. After they finish, name the move that made the problem easy so the intuition sticks.
- Skip only when the sub-topic is purely definitional (a named theorem statement, a historical fact, or a cloud-console lab). These problems appear at teach time; they are not stored in `curriculum.md`.

### Python

Python is practice, not a lecture dump. Library theory is folded into the matching math, ML, NLP, and production slices, including the concepts needed to use NLP libraries rather than only their APIs.

When a topic or sub-topic is higher math or a CORE domain (ML, LLM, DSP, image processing, NLP, Kaldi/ASR, neural nets, information theory, computer vision, IIT EPGC), teaching **must** present a bare-metal / from-scratch Python exercise so theory and practice meet. Skip a coding exercise only when the sub-topic is purely definitional (a named theorem statement, a historical fact, or a cloud-console lab that cannot be done in NumPy). “From scratch” means NumPy-level implementations for primitives (arrays, gradients, attention, tokenization, n-gram models, TF-IDF, embeddings, decoding, GMM-EM, and similar). For serving and distributed libraries (vLLM, Ray, PySpark, LangChain, LlamaIndex) teach the concept and use the library; do not reimplement the engine. Topics that do not need an implementation get at most a short snippet. These exercises appear at teach time; they are not stored in `curriculum.md`.

**Coding protocol** (this is the allowed guidance; it is not a solution dump). Before code: the learner traces the algorithm on a tiny example by hand, then writes pseudocode, then a minimal Python function. Then small tests or numerical checks, then a comparison with the library implementation if one exists. The learner writes the function; do not paste the finished solution first. If they stall, the next protocol step or a question is the hint. Bugs are teaching data: diagnose the wrong assumption, shape mismatch, off-by-one, numerical issue, or missing invariant before showing a fix. Prefer tiny arrays and visible intermediate values until the learner can predict what the code should do.

## What this course is not

It is not a survey of every book title that happened to appear in the source files. `ARCHIVE` and deferred-enrichment material stay as inventory. They are not taught unless a real primary-destination topic depends on a sliver of them.

It is not formula-only teaching, and it is not an unbounded research programme. Ivy-league graduate plus industry competence is enough. PhD and postdoctoral terrain is out of scope for now.
