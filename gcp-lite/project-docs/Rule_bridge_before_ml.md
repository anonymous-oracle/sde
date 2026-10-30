# Standing rules for the Math of ML strand: bridge right before the ML topic; derive the formula

Set 29 Oct 2026 by the learner.

1. "How about teaching the required bridge right before the ML topic. That way we will be doing both. In fact record create a single file for this rule so that it can stick to the session."
2. "Also, wherever appropriate, teach how a formula is derived too. In fact record create a single file for this rule so that it can stick to the session." (Both go in this one file.)

Background (28 Oct): asked whether a bridge covering all topics was needed now, the learner had just been unable to choose a technique for a line through two points. That is the gap a bridge fills, and it is the gap the matrix places right before its first ML use.

**Scope:** the Math of ML strand (`gcp-lite/ml-math/ml_math_strand.md`, which holds the bridge matrix, the units and the record). Read this file at the start of every session in the strand and after any compaction, together with `index/00_learning_method.md`. Where this file and the strand doc differ, this file wins.

## Rule A: the school bridge comes right before the ML topic

1. **Just in time, never up front.** Immediately before each ML concept, teach only the Class 9 to 12 topics that concept consumes. Do not teach the school stack ahead of its use.
2. **One stretch, fixed order:** bridge, then the ML concept, then the build, then the academic pass, then the ramp. Bridge and concept sit in the same stretch of turns so the learner does both together.
3. **Name the consumer first.** Open every bridge with one line saying which ML idea will use it, so the topic is learned as a tool.
4. **Teach the bridge JEE style:** the menu of techniques, how to choose between them (look at the structure first), one named habit, and a second route. The block's Rung-9 problem fuses the bridge topic with the ML idea.
5. **Probe, do not pre-test.** A topic the learner handles fluently is not re-taught. When a gap shows, teach the missing link in full, then resume.
6. **Mid-concept gap:** stop, teach just that link, return to the same point. Log it in the strand doc's record and in the error log by cause (conceptual, misread, slip, strategic).
7. **The matrix is a default, not a cage.** If a school topic is needed earlier than the matrix says, teach it then and update the matrix.

## Rule B: derive the formula, wherever appropriate

1. **When to derive.** A formula is derived the first time it is used when (a) its derivation fits in one or two short turns and teaches a reusable idea (slope from a constant rate; the dot product from the law of cosines), or (b) it is the central result of the unit (normal equations, the logistic gradient, the PCA objective).
2. **When not to.** A definition or a notation is not derived; say it is a definition and why it was chosen. A result whose proof needs a topic not yet taught is stated, with the missing piece and the unit where it will be proved named aloud and logged in the strand record as "stated, proof deferred". A deferred result is never presented as derived.
3. **How.** (a) Say the question the formula answers. (b) State the assumptions that carry it. (c) Give every step with its reason. (d) Check it by a special case or by units and, where possible, by a second route. (e) Name the habit used.
4. **Who does what.** A new formula is derived by the tutor in narrated steps, because the learner has nothing yet to discover; the learner takes the last step when it is small. The check that follows asks the learner to use the formula or explain one step, and the derivation never contains that check's answer. At the reflection rung, or in a later recall, the learner re-derives it cold.
5. **In the build.** The from-scratch exercise implements the derived formula and is checked against a hand computation or the library.
6. **Errata.** A formula given without its derivation, where the rule says to derive it, is logged as a tutor's error. First instance: the slope and intercept formulas on 28 Oct were stated without derivation; derived on 29 Oct.

## Rule C: unchanged from the method

Short turns, one check per turn with expected answers written first, no ready-made code, one exercise per 3 to 5 concepts judged on functional logic, an unanswered check reworded and made smaller, stop when it is understood.

## Rules in action so far

- Block 1a. ML concept M1: a model is a rule with adjustable numbers (weight w, bias b); signed error = actual − predicted; different pairs of points give different lines. Bridge taught right before the next ML step: a line through two points (slope as rise over run, intercept b = y₁ − w·x₁, choosing a technique by the x-gap, simultaneous equations as the always-works fallback).
- 29 Oct: the slope and intercept formulas were derived from a constant rate (rise = w × run), with a check against the first table. This closed the errata item in Rule B.6.
- 30 Oct: the lines bridge closed. Then ML concept M2 opened: three pairs of rows give three lines (A, B, C), each fitting two rows exactly and missing the third; a single score is needed to choose among lines. First candidate score: the sum of signed errors.

## State (30 Oct 2026)

- Passed, M1: w = 3 and b = 10 from an exact table, with b given unasked. Rows-1-and-2 line predicted 21 at area 3 (simultaneous equations; second route by rate of change shown). Rows-1-and-3 line misses area 2 by one (signed error +1; the learner gave the size, the sign was supplied).
- Passed, lines bridge: slope with a non-unit gap and a negative sign, direction predicted before computing (line through (1, 9) and (4, 3): −2, it falls). The earlier check on (2, 7) and (6, 19), reworded to give the rise and run, was passed (3). Intercept b = y₁ − w·x₁ shown on that line (b = 1). Lines bridge: taught, L2 engineering pass; the cold retry of an unseen line with non-integer slope is still due.
- Error log: sign omitted on a signed error (slip, 28 Oct). No misconceptions registered.
- Table in use (areas 1, 2, 3; prices 13, 17, 19): line A from rows 1 and 2 has w = 4, b = 9, errors 0, 0, −2; line B from rows 1 and 3 has w = 3, b = 10, errors 0, +1, 0; line C from rows 2 and 3 has w = 2, b = 13, errors −2, 0, 0. For later: the least-squares line is w = 3, b = 31/3 (about 10.33), errors −1/3, +2/3, −1/3, sum of squared errors 2/3, against 1 for line B.
- **Open check (M2):** give three signed errors, not all zero, whose sum is 0. Expected: any such triple, for example +1, −1, 0. Expected wrong: a triple that does not sum to 0, or "impossible". Purpose: the plain sum of signed errors cannot tell a perfect line from a bad one, because errors cancel.
- Next: absolute errors against squared errors as the score; squared error as the choice (smooth, differentiable, and its minimum is found in closed form); the sum of squared errors for lines A, B, C; then Unit 3 for the exact minimizer.
