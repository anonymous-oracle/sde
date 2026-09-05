# Textbook Research Audit Log

Companion to §17.1 of `unified-curriculum.md`. One row per candidate textbook
considered, in batch order, so every compiled entry is traceable from module to
source to file location. Statuses use the §17.1.1 contract: `confirmed`,
`single-sourced, unverified`, `candidate`, `rejected`.

Research baseline and access date for all rows below: **2026-09-04**.

Excluded hosts (never fetched, cited, or linked, regardless of search rank):
Scribd, Library Genesis, Z-Library, Sci-Hub, Internet Archive full-text or
borrow copies, epdf.pub, PDF Drive, dokumen.pub, and any other unauthorized
scan or mirror.

## Batch B0 — closing the open M1-M28 gaps

| Modules | Candidate | Sources fetched | Outcome | Compiled entry | Gap effect |
|---|---|---|---|---|---|
| `M27`, `M28`, `MML-2` | OpenStax *Calculus Volume 3* (2016) | OpenStax preface `SRC-MATH-024`; LibreTexts vectors-in-space chapter and navigation `SRC-MATH-025` | `confirmed` | `TB-MATH-012` | closes dot/cross products, lines and planes in space, distance formulas; triple products still open |
| `M5-M8`, `M22`, `M25`, `M26`, `MML-1` | OpenStax *Intermediate Algebra 2e* (2020) | OpenStax preface `SRC-MATH-026`; LibreTexts workbench `SRC-MATH-027`; determinant section `SRC-MATH-029` | `confirmed` | `TB-MATH-013` | closes inequalities and polynomial/rational work; contributes conics, binomial theorem, determinants |
| `M17`, `M23`, `M20` | Corral, *Elementary Trigonometry* v1.2 (2020) | Author site `SRC-MATH-030`; LibreTexts `SRC-MATH-031` | `confirmed` | `TB-MATH-014` | closes the dedicated-trigonometry gap; contributes polar/complex representation |
| `M14`, `M15`, `M16` | Africk, *Elementary College Geometry*, 2021 ed. | Open Textbook Library `SRC-MATH-032`; LibreTexts `SRC-MATH-033`; CUNY repository `SRC-MATH-034` | `confirmed` | `TB-MATH-015` | closes the applied synthetic-geometry gap; rigorous tier still open |
| `M3`, `M19`, `M21`, `PROOF-DISCRETE` | Sundstrom, *Mathematical Reasoning: Writing and Proof* | GVSU ScholarWorks `SRC-MATH-035`; AIMath `SRC-MATH-036` | `confirmed` on contents; version string unsettled between the two sources (v3 2020 vs v2.1 2022) | `TB-MATH-016` | closes the second-confirmed-proof-text gap; digital logic still open |
| `M3`, `M21`, `M22`, `PROOF-DISCRETE` | Levin, *Discrete Mathematics: An Open Introduction*, 4th ed. (2024) | Author site `SRC-MATH-037`; Open Textbook Library `SRC-MATH-038` | `single-sourced, unverified` — the library record's listed contents still follow the 3rd-edition ordering, so the two do not corroborate | `TB-MATH-017` | does not clear a gap |
| `M1`, `M2`, `M4`, `M16`, `M18`, `MML-0` | OpenStax *Contemporary Mathematics* (2023) | LibreTexts `SRC-MATH-039`; OpenStax money-management chapter `SRC-MATH-040` | `confirmed` | `TB-MATH-018` | closes the second foundational-arithmetic gap and the commercial-arithmetic content gap |
| `M21`, `M22` | Keller and Trotter, *Applied Combinatorics* (2017) | Open Textbook Library `SRC-MATH-041`; author site `SRC-MATH-042` (scope only, no ToC) | `single-sourced, unverified` | `TB-MATH-019` | multinomial gap stays open |
| `M5-M8`, `M20`, `M23-M25` | OpenStax *Algebra and Trigonometry 2e* (2021), already recorded | Existing `SRC-MATH-019`; new LibreTexts workbench `SRC-MATH-028` | promoted `single-sourced, unverified` to `confirmed` | `TB-MATH-007`, logged as `CORR-003` | contributes to closing `M5-M8`, `M20`, `M24-M25` |
| `M14-M16` | Hartshorne-tier and olympiad synthetic geometry | not established | `rejected` for this pass | none | rigorous-geometry `GAP:` retained |
| `M24`, `M25` | Tewani, *JEE Advanced Coordinate Geometry* | Existing `SRC-MATH-023`, publisher metadata only | remains `candidate` | `TB-MATH-011` | JEE-technique `GAP:` retained |

### B0 result

Closed: `M1`/`M2`/`M4`/`MML-0`, `M5-M8`/`MML-1`, `M17`/`M23`, `M26`.
Partially closed with a narrowed note: `M3`, `M14-M16`, `M18`, `M20`,
`M24-M25`, `M27-M28`.
Still fully open: multinomial expansions for `M22`.

## Batch B1 — calculus and real analysis (`M29-M34`, `M38`, `MML-4`, `MML-12`, `MATH-CALC-NUM`)

| Modules | Candidate | Sources fetched | Outcome | Compiled entry | Gap effect |
|---|---|---|---|---|---|
| `M29-M33`, `MML-4` | OpenStax *Calculus Volume 1* (2016) | OpenStax preface `SRC-CALC-001`; LibreTexts combined navigation `SRC-CALC-003` | `confirmed` | `TB-CALC-001` | closes the applied tier for limits, derivatives, and integration |
| `M32-M34`, `MML-4` | OpenStax *Calculus Volume 2* (2016) | OpenStax preface `SRC-CALC-002`; LibreTexts `SRC-CALC-003` | `confirmed` | `TB-CALC-002` | closes integration technique and series; sole confirmed source for `M34` |
| `M29-M33`, `M38`, `MML-12` | Spivak, *Calculus*, 4th ed. (2008) | Publish or Perish publisher page `SRC-CALC-004`; Google Books `SRC-CALC-005` | `confirmed` | `TB-CALC-003` | closes the rigorous tier for single-variable calculus |
| `M38`, `MML-12` | Rudin, *Principles of Mathematical Analysis*, 3rd ed. | UW-Madison catalog contents note `SRC-CALC-006`; McGraw-Hill India `SRC-CALC-007` | `confirmed` | `TB-CALC-004` | closes `M38` at the stated undergraduate ceiling |
| `M29`, `M38`, `MML-12` | Abbott, *Understanding Analysis*, 2nd ed. (2015) | Springer ToC `SRC-CALC-008`; Google Books `SRC-CALC-009` (metadata only) | `single-sourced, unverified` | `TB-CALC-005` | does not clear a gap |
| `M29-M34` | Apostol, *Calculus, Volume 1*, 2nd ed. | Google Books ToC `SRC-CALC-010`; Wiley `SRC-CALC-011` (edition identity only, contents PDF not machine-readable) | `single-sourced, unverified` | `TB-CALC-006` | does not clear a gap; resolves the Apostol mis-citation as `CORR-005` |
| `M29-M33` | Stewart and Thomas calculus editions | not pursued | `rejected` for this pass | none | none; two confirmed applied records already in place |
| all | Course-hosted and mirror PDFs of Rudin, Spivak, Apostol surfaced by search (lehman.edu, cs.mcgill.ca, neocities, theswissbay, pdfcoffee, studylib, dokumen.pub) | not fetched | excluded as unauthorized scans of in-copyright works | none | none |

### B1 result

Closed: `M29`, `M30`, `M31`, `M32`, `M33`, `M38`, `MML-12`, and the calculus slice of `MATH-CALC-NUM`.
Narrowed notes retained: parametric differentiation for `M30`, Jacobians and Hessians for `MML-4`.
Still open: `M34` has one confirmed source; the engineering-mathematics batch owns the deeper differential-equations treatment.

## Batch B2 — engineering mathematics and numerics (`M35`, `M36`, `M37`, `MML-10`)

| Modules | Candidate | Sources fetched | Outcome | Compiled entry | Gap effect |
|---|---|---|---|---|---|
| `M35`, `M36`, `M37`, `MML-10` | Kreyszig, *Advanced Engineering Mathematics*, 10th ed. | Wiley companion-site contents `SRC-ENG-001`; Google Books `SRC-ENG-002` | `confirmed` | `TB-ENG-001` | sole confirmed source for `M35` and `M36`; contributes to closing `M37` |
| `M37`, `MML-10`, `MML-12` | Trefethen and Bau, *Numerical Linear Algebra* (1997) | SIAM chapter listing `SRC-ENG-003`; Google Books `SRC-ENG-004` | `confirmed` | `TB-ENG-002` | closes the rigorous numerics tier and the floating-point/conditioning half of `MML-10` |
| `M34`, `M35`, `M37` | Boyce, DiPrima, Meade, *Elementary Differential Equations and BVP*, 11th ed. | Google Books `SRC-ENG-005`; Wiley product page returned 404 | `single-sourced, unverified` | `TB-ENG-003` | does not clear the `M35` gap |
| `M35`, `M36` | Grewal, *Higher Engineering Mathematics* | searched; no exact edition tied to two legitimate contents sources | `rejected` for this pass | none | `M35`/`M36` second-source gaps retained |
| `M37` | Burden and Faires, *Numerical Analysis* | not fetched | left as an unresearched candidate | none | none |
| `M39` | Golub and Van Loan, *Matrix Computations* | deferred | deferred to the optimization and spectral batch | none | none |

### B2 result

Closed: `M37`, `MML-10`, and the numerics slice of `MATH-CALC-NUM`.
Still open: `M35` and `M36` each rest on one confirmed source; the z-transform is deferred to the signals batch.

## Batch B3 — probability, statistics, information theory (`M40`, `MML-5`, `MML-6`, `MML-8`, `PROB-STAT-INFO`)

| Modules | Candidate | Sources fetched | Outcome | Compiled entry | Gap effect |
|---|---|---|---|---|---|
| `MML-5`, `M40` | Grinstead and Snell, *Introduction to Probability*, 2nd ed. (2006, AMS) | Open Textbook Library `SRC-PROB-001`; LibreTexts `SRC-PROB-002` | `confirmed` | `TB-PROB-001` | closes `MML-5` |
| `M40`, `MML-6` | OpenStax *Introductory Statistics 2e* (2023) | OpenStax preface `SRC-PROB-003`; LibreTexts `SRC-PROB-004` | `confirmed`; the two sources swap the regression and ANOVA chapter order | `TB-PROB-002` | closes the applied statistics tier |
| `M40`, `MML-6` | Casella and Berger, *Statistical Inference*, 2nd ed. | Routledge/Chapman and Hall `SRC-PROB-005`; Google Books/CRC `SRC-PROB-006` | `confirmed`; second listing scrambles chapter order | `TB-PROB-003` | closes the rigorous inference tier |
| `M40`, `MML-6`, `MML-9` | Wasserman, *All of Statistics* (2004) | Springer ToC `SRC-PROB-007`; Google Books `SRC-PROB-008` (metadata only) | `single-sourced, unverified` | `TB-PROB-004` | bootstrap/jackknife gap stays open |
| `M40`, `MML-8` | Jaynes, *Probability Theory: The Logic of Science* (2003) | Cambridge ToC `SRC-PROB-009`; Google Books `SRC-PROB-010` (metadata only) | `single-sourced, unverified` | `TB-PROB-005` | none |
| `MML-8`, `M40` | Cover and Thomas, *Elements of Information Theory*, 2nd ed. | Google Books ToC `SRC-PROB-011`; Wiley `SRC-PROB-012` (edition identity; contents PDF 403) | `single-sourced, unverified` | `TB-PROB-006` | `MML-8` gap stays open |
| `MML-8` | MacKay, *Information Theory, Inference, and Learning Algorithms* | author site inference.org.uk returned 403 to both WebFetch and the browser | `rejected` for this pass | none | `MML-8` remains the batch's largest gap |
| `MML-5` | DeGroot and Schervish; Ross; Blitzstein and Hwang | not fetched | left as unresearched candidates | none | none |
| `M40` | Durrett, *Probability: Theory and Examples* | deferred | beyond the declared rigor ceiling | none | none |

### B3 result

Closed: `MML-5`, `MML-6` core, and the probability and inference slices of `M40` and `PROB-STAT-INFO`.
Still open: `MML-8` has no confirmed source at all; Fisher information, Cramer-Rao, MCMC, and the bootstrap each rest on one record.

## Batch B4 — optimization and spectral methods (`M39`, `MML-7`, `MATH-LA`)

| Modules | Candidate | Sources fetched | Outcome | Compiled entry | Gap effect |
|---|---|---|---|---|---|
| `M39`, `M37`, `MML-3`, `MML-10` | Golub and Van Loan, *Matrix Computations*, 4th ed. (2013) | SIAM/JHU contents listing `SRC-OPT-001`; Google Books `SRC-OPT-002` | `confirmed` | `TB-OPT-001` | closes the spectral and decomposition half of `M39` |
| `MML-7`, `M39` | Nocedal and Wright, *Numerical Optimization*, 2nd ed. | Springer ToC `SRC-OPT-003`; Google Books `SRC-OPT-004` exposes only the first three chapters | `single-sourced, unverified` | `TB-OPT-002` | `MML-7` gap stays open |
| `MML-7`, `M39` | Boyd and Vandenberghe, *Convex Optimization* (2004) | Cambridge chapter listing `SRC-OPT-005` (reached via the browser after WebFetch and the Cambridge core page both failed to expose contents); Stanford author site `SRC-OPT-006` exposes no ToC | `single-sourced, unverified` | `TB-OPT-003` | `MML-7` gap stays open |
| `M39` | Luenberger, *Optimization by Vector Space Methods* | not edition-verified | `rejected` for this pass | none | `M39` Hilbert-space gap recorded |
| `MML-7` | Bertsekas, *Nonlinear Programming*; Beck, *First-Order Methods in Optimization* | not fetched | left as unresearched candidates | none | none |

### B4 result

Closed: `M39` spectral content, and the spectral slice of `MATH-LA`.
Still open and significant: `MML-7` has no confirmed source for convexity, Lagrange/KKT, gradient descent variants, or adaptive optimizers. `M39` abstract Hilbert space is unverified.

## Batch B5 — signals, image processing, vision (`M41`, `M42`, `MML-11`)

| Modules | Candidate | Sources fetched | Outcome | Compiled entry | Gap effect |
|---|---|---|---|---|---|
| `M41`, `MML-11` | Downey, *Think DSP* (2012) | author HTML edition `SRC-DSP-003`; Open Textbook Library `SRC-DSP-004` | `confirmed` | `TB-DSP-002` | closes the applied DSP tier |
| `M41`, `M36` | Oppenheim and Schafer, *Discrete-Time Signal Processing*, 3rd ed. | Pearson International Edition contents PDF `SRC-DSP-001` (read as PDF pages after text extraction failed); Google Books `SRC-DSP-002` partial and reordered | `single-sourced, unverified` | `TB-DSP-001` | rigorous DSP gap stays open |
| `M42`, `ML-9` | Hartley and Zisserman, *Multiple View Geometry*, 2nd ed. | Oxford VGG authors' contents PDF `SRC-CV-003` (read as PDF pages); Cambridge `SRC-CV-004` | `confirmed` | `TB-CV-002` | closes the multi-view geometry slice |
| `M42`, `MML-11` | Gonzalez and Woods, *Digital Image Processing*, 4th ed. | authors' companion-site detailed contents `SRC-CV-001` (read as PDF pages); Pearson catalog `SRC-CV-002` | `single-sourced, unverified` — the second source conflicts on chapter order rather than corroborating | `TB-CV-001` | `M42` core gap stays open |
| `M42`, `ML-9` | Szeliski, *Computer Vision*, 2nd ed. (2022) | Springer ToC `SRC-CV-005`; author site `SRC-CV-006` and Google Books expose no ToC | `single-sourced, unverified` | `TB-CV-003` | none |
| `M41` | Proakis and Manolakis; Lyons; Lathi; Oppenheim and Willsky; Proakis and Salehi | not fetched | left as unresearched candidates | none | none |
| `M42` | Forsyth and Ponce | not fetched | left as an unresearched candidate | none | none |

### B5 result

Closed: the applied DSP tier for `M41` and `MML-11`, and the multi-view geometry slice of `M42`.
Still open and significant: the core image-processing content of `M42` has no corroborated source; the rigorous DSP tier for `M41` has none; cepstral analysis has none.

## Batch B6 — speech, ASR, automata (`M43`, `M44`)

| Modules | Candidate | Sources fetched | Outcome | Compiled entry | Gap effect |
|---|---|---|---|---|---|
| `M43` | Yu and Deng, *Automatic Speech Recognition: A Deep Learning Approach* (2014) | Springer ToC `SRC-SPCH-001`; Google Books `SRC-SPCH-002` (no ToC) | `single-sourced, unverified` | `TB-SPCH-001` | `M43` gap stays open |
| `M43`, `M45`, `ML-8` | Jurafsky and Martin, *Speech and Language Processing*, 3rd ed. draft | Stanford author draft site `SRC-NLP-001`; Google Books 2nd ed. `SRC-NLP-002` | `single-sourced, unverified`; a living draft, so exact-edition verification is not achievable | `TB-NLP-001` | none |
| `M44`, `PROOF-DISCRETE` | Hopcroft, Motwani, Ullman, 3rd ed. | Google Books partial `SRC-AUT-001`; Pearson catalog `SRC-AUT-002` (no ToC); Ullman's Stanford page refused connection | `single-sourced, unverified` | `TB-AUT-001` | `M44` gap stays open |
| `M43` | Rabiner and Juang; Huang, Acero, Hon; Quatieri | no legitimate edition-matched ToC reached | `rejected` for this pass | none | `M43` remains without any confirmed source |
| `M44` | Sipser; Mohri/Pereira/Riley WFST literature | not fetched; the WFST literature is papers and project documentation, not textbooks | left as candidates / out of contract | none | `M44` WFST content has no textbook record at any level |

### B6 result

Nothing closed. `M43` and `M44` are the weakest modules in the audit: no confirmed textbook at either tier, and weighted finite-state transducers have no textbook record at all. Both modules currently rest on official OpenFst and Kaldi documentation, which is legitimate primary material but cannot satisfy the textbook contract.

## Batch B7 — classical machine learning (`ML-1`-`ML-7`, `ML-10`, `ML-11`, `ML-CORE`)

| Modules | Candidate | Sources fetched | Outcome | Compiled entry | Gap effect |
|---|---|---|---|---|---|
| `ML-1`, `ML-3`-`ML-6`, `ML-11` | James, Witten, Hastie, Tibshirani, *ISL* 2nd ed. (2021) | Springer chapter listing `SRC-ML-003`; statlearning.com author site `SRC-ML-004` | `confirmed`; the author site lists topics rather than numbered chapters, so the match is on sequence | `TB-ML-002` | closes `ML-4`, `ML-5`, and most of `ML-3` |
| `ML-3`-`ML-6` | Hastie, Tibshirani, Friedman, *ESL* 2nd ed. (2009) | Springer ToC `SRC-ML-001`; author frameset `SRC-ML-002` exposes no chapter list; Google Books record for the ISBN returned no ToC | `single-sourced, unverified` | `TB-ML-001` | none |
| `ML-CORE` | Bishop, *PRML*; Murphy *PML1*; Duda/Hart/Stork; Geron; Shalev-Shwartz & Ben-David; Hyndman & Athanasopoulos | bishopbook.com now serves the newer Bishop & Bishop volume; MIT Press exposes no ToC for Murphy; the rest not fetched | `rejected` / unresearched | none | `ML-2`, `ML-10`, `ML-11` gaps remain wide open |

## Batch B8 — deep learning and sequence models (folded DL Modules 1-7, `M45`, `ML-14`)

| Modules | Candidate | Sources fetched | Outcome | Compiled entry | Gap effect |
|---|---|---|---|---|---|
| folded DL Modules 1-7, `ML-14` | Goodfellow, Bengio, Courville, *Deep Learning* (2016) | author site ToC `SRC-DL-001`; MIT Press `SRC-DL-002` states the same part-and-topic sequence in prose | `confirmed` | `TB-DL-001` | closes DL Module 1; single-source coverage for Modules 2-7 |
| folded DL Modules 2-7, `M45` | Prince, *Understanding Deep Learning* (2023) | MIT Press metadata `SRC-DL-003`; author notebooks `SRC-DL-004` | `single-sourced, unverified`; chapter titles inferred from numbered exercise notebooks | `TB-DL-002` | none |
| folded DL Modules 2-7, `M45`, `ML-7` | Zhang, Lipton, Li, Smola, *Dive into Deep Learning* (2023) | d2l.ai author ToC `SRC-DL-005`; the Cambridge catalog page returned HTTP 500 | `single-sourced, unverified` | `TB-DL-003` | none |
| folded DL Modules 1-7, `M45` | Bishop and Bishop, *Deep Learning: Foundations and Concepts* (2024) | Springer `SRC-DL-006`; author site `SRC-DL-007`; neither exposes a chapter list | `candidate` | `TB-DL-004` | none |

## Batch B9 — NLP, IR, GenAI, RAG, agents (`ML-8`, folded IIT Modules 7-13, `GENAI-RAG-AGENTS`)

| Modules | Candidate | Sources fetched | Outcome | Compiled entry | Gap effect |
|---|---|---|---|---|---|
| `ML-7`, `ML-8`, folded IIT Module 8 | Manning, Raghavan, Schuetze, *Introduction to Information Retrieval* (2008) | Stanford author site ToC `SRC-IR-001`; Cambridge chapter listing `SRC-IR-002` (reached via the browser) | `confirmed` | `TB-IR-001` | closes the classical IR half of `ML-7` and `ML-8` |
| `GENAI-RAG-AGENTS` | Russell and Norvig, *AIMA* 4th ed. | Berkeley contents page refused connection from both WebFetch and the browser | `rejected` for this pass | none | none |
| `ML-8` | Manning and Schuetze *FSNLP*; Tunstall et al. *NLP with Transformers* | not fetched | unresearched candidates | none | `ML-8` LLM gap remains |

## Batch B10 — RL, bandits, causality (`ML-12`, `MML-9`)

| Modules | Candidate | Sources fetched | Outcome | Compiled entry | Gap effect |
|---|---|---|---|---|---|
| `ML-12`, `MML-9` | Lattimore and Szepesvari, *Bandit Algorithms* (2020) | Cambridge ToC `SRC-RL-003`; Google Books full chapter listing `SRC-RL-004` | `confirmed` | `TB-RL-002` | closes the bandit half of `ML-12` and `MML-9` |
| `ML-12`, `MML-9` | Sutton and Barto, 2nd ed. (2018) | author site `SRC-RL-001` (reached via the browser after a WebFetch certificate error); MIT Press part description `SRC-RL-002` | `single-sourced, unverified`; neither source exposes a chapter list | `TB-RL-001` | RL half of `ML-12` stays open |
| `ML-12`, `MML-9` | Hernan and Robins, *Causal Inference: What If* | the Harvard book URL now redirects to a staff profile | `rejected` for this pass | none | causal gap stays fully open |
| `MML-9` | Pearl, *Causality*; Pearl/Glymour/Jewell primer; banditalgs.com | not fetched; banditalgs.com presented an expired certificate | unresearched / rejected | none | none |

## Batch B11 — production ML and MLOps (`M46`, `ML-13`, `MLSYS-1`-`MLSYS-9`, `ML-SYS-MLOPS`)

| Modules | Candidate | Sources fetched | Outcome | Compiled entry | Gap effect |
|---|---|---|---|---|---|
| `M46`, `MLSYS-1`-`MLSYS-9` | Huyen, *Designing Machine Learning Systems* (2022) | O'Reilly ToC `SRC-MLSYS-001` (reached via the browser after a 403); Google Books `SRC-MLSYS-002` exposes no ToC | `single-sourced, unverified`; the publisher listing truncates after Ch. 9 | `TB-MLSYS-001` | no gap closed |
| `MLSYS-2`, `MLSYS-4`, `MLSYS-6`-`MLSYS-8` | already-`confirmed` §17.1.4 records: Kleppmann, the two Google SRE volumes, Anderson | reused, not re-researched | reused | `TB-DIST-001`, `TB-OPS-001`, `TB-OPS-002`, `TB-SEC-001` | covers the systems, operations and security substrate |
| `M46` | Lakshmanan, Robinson, Munn, *Machine Learning Design Patterns* | O'Reilly returned 403; not retried in the browser before the batch closed | unresearched candidate | none | strongest untried lead for this area |
| `ML-13` | Burkov; Ameisen | not fetched | unresearched candidates | none | `ML-13` gap remains |

### B7-B11 result

Closed: `ML-4`, `ML-5`, most of `ML-3`, the classical IR half of `ML-7` and `ML-8`, folded DL Module 1, and the bandit half of `ML-12` and `MML-9`.
Single-confirmed-source coverage: folded DL Modules 2-7 and `ML-14`, all resting on `TB-DL-001` alone.
No confirmed source at all: `ML-2`, `ML-10`, `ML-11` forecasting, `M45`, every folded IIT module from 7 to 13, the RL and causal halves of `ML-12`, `MML-9` causal content, `ML-13`, and `M46`.

## Audit-log scope note

`TB-MATH-001` to `TB-MATH-006` and `TB-MATH-008` to `TB-MATH-010` predate this pass; they were compiled by the earlier session recorded in §17.1.3 and are not re-litigated here. `TB-MATH-007` appears in the B0 table because this pass changed its status. Every textbook record created or changed by this pass has a row above.

## Verification run (2026-09-04)

| Check | Result |
|---|---|
| No excluded or unauthorized host cited anywhere in the file | clean |
| Every `SRC-*` referenced is defined in §17.1.2 | 157 defined, 0 dangling |
| Every `TB-*` referenced is defined in an atlas table | 79 defined, 0 dangling |
| Every row marked `confirmed` names at least two distinct `SRC-*` ids | 0 violations |
| Every in-scope identifier (`M1`-`M46`, `MML-0`-`MML-12`, `ML-1`-`ML-14`, `MLSYS-1`-`MLSYS-9`) appears in an audit table | all 82 covered |
| §18.2 losslessness: strip each marked region plus its preceding blank line | byte-identical to the pre-audit section |
| Compiled entries use chapter ranges plus paraphrased nouns, no verbatim ToC | spot-checked; no numbered mirror lists |
| Diff is additive apart from the deliberately flagged §17.1 history paragraph, the §18.1 diff rule, and the `TB-MATH-007` status change (`CORR-003`) | confirmed |

## Batch B12 — fanout.sh appraisal and the leads it surfaced

Prompted by a user request to evaluate whether `fanout.sh` resources could close
any open gap. The site was first checked for security and link hygiene, then
browsed only through its own published public surfaces: `robots.txt`,
`llms.txt`, `sitemap.md`, `roadmap.md`, and public `.md` representations. Its
`robots.txt` explicitly allows `ClaudeBot` and `Claude-User`, and its `llms.txt`
states that public pages may be summarized and cited. **No paywalled lesson
content was fetched, and no access control was bypassed or probed.**

### Security and link assessment

| Check | Result |
|---|---|
| Real TLS chain, verified out-of-band via certificate transparency | Let's Encrypt and Google Trust Services; current and valid |
| Certificate presented locally | A Zscaler interception certificate. This workstation sits behind a corporate TLS-inspecting proxy, so the locally observed chain is not the site's own; the true chain was confirmed independently |
| Security headers | HSTS two years, `nosniff`, `X-Frame-Options: SAMEORIGIN`, `strict-origin-when-cross-origin` referrer policy, permissions policy denying camera, microphone and geolocation |
| Hosting | Cloudflare fronting Railway; no forms on public pages |
| Outbound links | All HTTPS. Destinations are arXiv, YouTube, Amazon, and author or publisher sites. Zero hits against the excluded-host list |
| Privacy | Public pages load Google Ads, Meta and X advertising pixels plus an `unpkg.com` script. Not a vulnerability, but visits are tracked by three ad networks |
| Authority | Solo-authored commercial platform; course content paywalled and therefore unverifiable |

### Records

| Modules | Candidate | Sources fetched | Outcome | Compiled entry | Gap effect |
|---|---|---|---|---|---|
| `M45`, folded IIT Module 9, `ML-8`, `ML-14` | Raschka, *Build a Large Language Model (From Scratch)* (Manning, 2024) | O'Reilly full ToC `SRC-DL-009`, recovered by expanding the publisher's own collapsed contents listing; Google Books full ToC `SRC-DL-010`; Manning edition identity `SRC-DL-008`; surfaced via `SRC-REC-001` | `confirmed` — the two ToC sources agree chapter for chapter and appendix for appendix | `TB-DL-005` | closes `M45` attention and GPT-from-scratch, and folded IIT Module 9 LoRA. Both previously had **no textbook record at any evidence level** |
| `M45` modern primitives, folded IIT Modules 9 and 12-13 | Kumaresan, *Under The Hood* (Leanpub, 2026) | Leanpub scope and structure `SRC-DL-011`; surfaced via `SRC-REC-001` | `candidate` — self-published, no independent record | `TB-DL-006` | clears nothing; named as the only known candidate for the modern-architecture gap |
| n/a | fanout.sh itself | `robots.txt`, `llms.txt`, `sitemap.md`, `roadmap.md`, `/ai/resources.md`, `/system/resources.md`, public overview stubs | admitted as a selection signal only | `SRC-REC-001`, logged as `CORR-006` | cannot clear any `GAP:`; not added as a curriculum resource or teaching source |
| various | Goodfellow, Bishop, Axler on fanout's shelf | already held | corroboration only | existing records | none; already `confirmed` or handled |
| n/a | Bertrand Russell, *Principles of Mathematics*, which fanout tags as an ML "foundation" text | not pursued | `rejected` | none | a 1903 philosophy-of-mathematics work; not a proof or foundations textbook for this curriculum |
| n/a | Math Academy, Khan Academy, MIT OCW links on the same shelf | not pursued as textbooks | out of contract | none | platforms and courses, not textbook editions |

### Curriculum-coverage finding

The user also asked whether fanout covers topics this file does not. Its course
bodies are paywalled, but its public `roadmap.md` publishes the full topic tree
for all three tracks. Diffing that tree against this file by word-boundary
search produced one real, coherent finding, now logged as a cross-cutting `GAP:`
row in §17.1.12.1.

Verified absent from `unified-curriculum.md`, zero hits each: RMSNorm, rotary
position embeddings, SwiGLU, grouped-query attention, mixture-of-experts as a
taught mechanism, flash attention, paged attention, continuous batching,
speculative decoding, group-relative and sequence-level policy optimization,
empirical risk minimization, and PAC learning. Proximal policy optimization
appears once, inside a table, rather than as taught content.

Already covered and therefore **not** gaps: quantization, distillation, pruning,
decoding strategies, and the model-family landscape.

Out of scope, noted only: fanout's system-design track covers probabilistic and
streaming structures (HyperLogLog, count-min sketch, reservoir sampling, top-K
heavy hitters) absent from this file. These fall under the frozen
software/systems scope of §17.1 and were not researched.

### B12 result

Closed: `M45` 2017-2020 core, folded IIT Module 9 LoRA, the `ML-8` LLM half, and
`ML-14` attention primitives — all via one `confirmed` record.
Opened: one cross-cutting `GAP:` for the modern transformer architecture and
inference layer, with `TB-DL-006` as its only candidate.
