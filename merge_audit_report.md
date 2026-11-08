# Audit of the merge and of the fold by subject

The merge of the machine-learning curriculum into the cloud curriculum was audited in two steps. **Part 1** is the audit of the first merge (63 checks), run on the document before the fold; in it the merged units carry the identifiers of the first merge (a separate Part G, domains D24 to D41, units U24.x to U41.x), which Part 3 maps to the final ones. **Part 2** is the audit of the fold by subject (41 checks), run on the final document and both index files. Part 4 lists what the audits do not cover.

# Part 1. Audit of the first merge (before the fold)


Audited file: `unified_cloud_curriculum.md` (2,116,432 characters). Run by `audit.py` on the assembled document, its two index files and the work files. **Result: 63 checks: 63 pass, 0 fail, 0 warnings (details in merge_audit_report.md).**

## 1. Counts and structure

| Check | Result | Detail |
|---|---|---|
| units in the merged document | **PASS** | 450 (290 cloud + 160 Part G) |
| domains | **PASS** | 41 domains, all distinct |
| parts | **PASS** | 8 parts: PART A. FOUN; PART B. CRYP; PART C. DIST; PART D. DATA; PART E. BIG ; PART F. COMP; PART G. MATH; PART H. CAPS |
| assignments with keys | **PASS** | 433 assignments, 433 collapsed keys (280 cloud + 153 Part G) |
| capstones U13.1 to U13.17, none with an assignment | **PASS** | 17 capstones |
| bridge and called-on units (first line "Bridge for") | **PASS** | 150 = 55 cloud + 95 Part G |
| cloud units present, unchanged order and identifiers | **PASS** | all 290 cloud unit identifiers present |
| Part G units present | **PASS** | 160 identifiers present |
| unit numbers contiguous inside each domain | **PASS** | yes (D33 starts at U33.0 by design) |
| every unit sits in the domain its identifier names | **PASS** | yes |

## 2. Identifier and reference integrity

| Check | Result | Detail |
|---|---|---|
| dangling unit references in units and domain intros | **PASS** | 0 dangling |
| dangling unit references in the appendices | **PASS** | 0 dangling |
| domain references resolve in the appendices (old-identifier map excluded) | **PASS** | lines that explain the old numbering ("D0 to D18", "D0→D24") are excluded |
| domain references resolve | **PASS** | 0 unresolved |
| assignment references resolve to an assignment | **PASS** | 0 unresolved |
| each assignment sits inside the unit with the same number | **PASS** | 433 assignments; 0 misplaced |

## 3. Old to new identifier map (Part G)

| Check | Result | Detail |
|---|---|---|
| all 160 old units mapped, injectively | **PASS** | 160 old -> 160 distinct new |
| map equals the stated scheme (D0-D17 -> D24-D41, +24; U18.n -> U13.(10+n)) | **PASS** | yes |
| unit titles identical after renumbering | **PASS** | 0 differ |
| the 153 old assignments are the 153 Part G assignments | **PASS** | 153 = 153; capstones carry none |
| domain titles identical after renumbering | **PASS** | 0 differ [] |

## 4. Retention: nothing from the old curriculum is lost except what the ledger lists

| Check | Result | Detail |
|---|---|---|
| every old atom is present in the new unit or listed in the removal ledger (H.4) | **PASS** | 2707 atoms checked; 0 lost |
| U33.12 (cut to its increment) names its cloud owners | **PASS** | U19.11 and U19.13 named; FP-growth and PrefixSpan kept |
| lines added to Part G units are only the generated first lines (Bridge for / On demand / Shares ground / Not repeated / Builds on) | **PASS** | 0 other added lines |

## 5. Removal ledger re-verified against the owners in the assembled document

| Check | Result | Detail |
|---|---|---|
| every owner named in the ledger is a cloud unit | **PASS** | 35 distinct owners |
| removed [P]/[D] atoms checked for proof status against the whole owner unit | **PASS** | 13 tagged atoms; definitions ([Def]) are not proof claims |

## 6. On-demand wiring

| Check | Result | Detail |
|---|---|---|
| every cloud unit in the demand map carries an On demand (Part G) line naming all its Part G units | **PASS** | 86 cloud units, 196 links; 0 problems [] |
| no cloud unit has a pointer that is not in the map | **PASS** | 0 stray |
| each called-on Part G unit starts with Bridge for: naming exactly its cloud callers | **PASS** | 95 units; 0 problems [] |
| every Part G unit has a first line of the expected kind | **PASS** | Bridge for / On demand / Integration |
| Part G units that no cloud unit calls on (entered through their domain chain) | **PASS** | 58 of 153 non-capstone units: U25.3, U26.4, U27.4, U27.5, U29.9, U30.6, U31.2, U31.3, U31.4, U32.1, U32.4, U32.11, U32.15, U32.17, U33.0, U33.13, U33.14, U34.1, U34.2, U34.3, U34.5, U34.6, U35.3, U35.5, U35.6, U35.7, U35.8, U36.1, U36.2, U36.4, U36.5, U36.6, U36.7, U36.9, U36.10, U37.1, U37.2, U37.3, U37.4, U37.5, U37.6, U37.7, U37.8, U38.1, U38.2, U38.4, U38.5, U38.7, U38.9, U38.10, U38.11, U38.12, U38.13, U38.14, U |
| domains of Part G with no direct cloud caller at all | **PASS** | D37 (0/8 called) |
| every "Builds on" target is an earlier Part G unit | **PASS** | yes |

## 7. Cloud units: only the intended edits

| Check | Result | Detail |
|---|---|---|
| pointer lines added to cloud units | **PASS** | 86 lines |
| all other cloud-unit edits are the planned ones (7 stale-wording fixes and the D13 aim) | **PASS** | 8 changed lines: 13_D11.md: Aim: the data-processing half of the big // 13_D11.md: Bridge for: U11.9 (machine learning on t // 13_D11.md: - **Gap-fills:** *[inferred: Hastie–Tibs // 14_D12_D13.md: - **Gap-fills:** *[inferred: the platfor // 14_D12_D13.md: Aim: ten integrating projects, each one  // 26_D18.md: - **Gap-fills:** *[inferred: Strang Chap // 26_D18.md: - **Gap-fills:** *[inferred: Candès and  // 29_D21.md: |
| cloud word-level coverage unchanged: 478 cells, all cited, 27 known residual flags | **PASS** | cells total 478; required 478; cited 478; uncited 0; shown 27 of 284 |
| cloud assignment checker | **PASS** | units 280 bad 0 |

## 8. Assignments (433)

| Check | Result | Detail |
|---|---|---|
| all 433 assignments have Q1-Q5, five keys, a numeric Q3 key, one collapsed block and the standard header | **PASS** | 433 blocks; problems: [] |
| the 153 Part G assignments are identical to the old ones apart from renumbering and the corrections listed in H.1 | **PASS** | 153 identical; 0 differ [] |
| every MCQ/MSQ key letter is an option of its question | **PASS** | 0 problems [] |
| all 153 Part G numeric keys recomputed: 26 by the audit script from the key text, the other 127 by verify_keys.py with an independently written computation per question | **PASS** | 26 + 127 of 127 keys recomputed independently and equal within the stated tolerance; mismatches []; no independent value written for [] |

## 9. Source coverage of Part G

| Check | Result | Detail |
|---|---|---|
| Part G cells: 564 registered, 564 cited | **PASS** | 564 registered, 564 cited |
| Appendix B Part G matrix equals the old matrix with identifiers mapped (cell by cell) | **PASS** | 564 cells; 0 differ [] |
| the matrix equals the Sources lines of the units | **PASS** | yes |
| every Part G content unit prints a Sources line | **PASS** | 0 missing [] |
| Appendix A lists all 44 Part G courses with the DM collision resolved | **PASS** | 44 rows |
| word-level coverage of the 564 Part G cells (nptel.txt and iit-genai.md): every source atom found in the units that cite its cell, removed atoms counted through their cloud owner | **PASS** | cells 564; atoms 4150; flagged 44 (generic prose 37, source typos 7, technical 0); outline atoms not covered 659; whole-course fallback cells 4. Flagged atoms are generic prose and source misspellings (reviewed one by one); none is an untaught technical term |

## 10. Duplicates still present after the merge

| Check | Result | Detail |
|---|---|---|
| atoms of Part G units that a cloud owner still states at the same or a stronger proof status (containment >= 0.8) | **PASS** | 0 remain |
| same-subject unit pairs with similarity >= 0.25 (declared in G.2 and H.5, compact versus full) | **PASS** | 39 pairs; highest 0.47 (U24.5 vs U18.1); lowest listed 0.25 |
| every pair above is covered by a G.2 row (the Part G unit lies in a listed range) | **PASS** | 27 G.2 rows; see H.5 for the 39 pairs |

## 11. Stale wording and figures

| Check | Result | Detail |
|---|---|---|
| stale phrases from before the merge | **PASS** | {'the earlier machine-learning': 4} |
| front-matter figures agree with the computed counts | **PASS** | {'Eight parts, 41 domains': True, 'One per content unit (433': True, 'seventeen capstones': True, '79 source courses': True, '1,042 source cells': True, 'U13.1 to U13.17': True} |
| mentions of unified_curriculum.md are all in the merge notes | **PASS** | 6 mentions; Direction.** This document is primary. `; e earlier machine-learning curriculum (`; neither is a prohibition). The earlier `; ruction this curriculum is primary and `; the earlier file: done (2026-11-06).** ` |
| no Part G text still claims to be printed first in the document | **PASS** | ok |
| no residual "R " or R-language revival from the old D0 (none expected) | **PASS** |  |

## 12. Index files

| Check | Result | Detail |
|---|---|---|
| index_cloud.md lists exactly the 450 units of the document, in document order | **PASS** | 450 units listed; order equal: True |
| index_cloud.md lists all 41 domains in document order | **PASS** | 41 domains |
| index_cloud.md marks every bridge and every capstone | **PASS** | 150 bridges, 17 capstones |
| unified_curriculum_index.md maps all 160 old units to the new identifiers | **PASS** | 160 mappings, equal to the ledger map |

## 13. Part G unit structure

| Check | Result | Detail |
|---|---|---|
| every Part G unit still has each of Topics, Results and Build that it had in the old file, non-empty | **PASS** | 0 problems [] |
| no field was left empty by a removal | **PASS** | 0 empty [] |
| no stray punctuation left by a removal ("; ;", ";;", "..") | **PASS** | 0 units [] |
| merged document size | **PASS** | 2,116,432 characters, 19,116 lines, 450 units |

# Part 2. Audit of the fold by subject


Folded document `X_final.md` against the audited merged document `F_doc.md`. 41 fold checks: 41 pass, 0 fail


## Fold 1. Counts and structure

- **PASS**: unit counts equal (450 before and after) (450 -> 450)
- **PASS**: 33 domains D1-D33, each once, 7 parts (33 domains, 7 parts)
- **PASS**: every unit sits in the domain that its identifier names ([])
- **PASS**: unit numbers contiguous inside each domain (D26 starts at U26.0) ([])
- **PASS**: 433 assignments before and after, 433 collapsed key blocks (433 -> 433; key blocks 433)
- **PASS**: every assignment id equals its unit id
- **PASS**: 17 capstones U13.1-U13.17, all in D13, no assignment (17)

## Fold 2. The fold lost nothing and changed nothing but identifiers and wording

- **PASS**: unit titles are unique in both documents, so a unit can be paired by title (450 / 450 distinct titles)
- **PASS**: every unit (text, results, assignment and key) is identical before and after, up to identifiers and the listed rewording (450 identical, 0 differ [])
- **PASS**: the identifier map derived from the title pairing equals the stated scheme (offsets per old domain) ([])
- **PASS**: each old (first-pass) domain lands in exactly one final domain ({})
- **PASS**: every unit and assignment identifier inside a unit is the image of the old one under the derived map (token by token, in order) (450 units exact; differ [])
- **PASS**: the 290 cloud units are unchanged apart from identifiers in pointer sentences and the Part G wording of those pointers (290 cloud units, identifiers unchanged, text differences [])
- **PASS**: no word is lost: the multiset of words over all unit bodies is contained in the folded one (216110 words before, 216110 after; lost {})

## Fold 3. Old curriculum to final: end-to-end

- **PASS**: H.2 has one row for each of the 160 old units (160 rows)
- **PASS**: each H.2 row names a final unit whose title is the old unit title ([])
- **PASS**: the 160 final identifiers are all different and 153 of them have an assignment, 7 are capstones
- **PASS**: cloud unit identifiers never appear as targets of an old unit (no collision), except the capstones in D13

## Fold 4. References and wording

- **PASS**: every unit identifier in the document resolves to a unit (H.2 old column excluded) ([])
- **PASS**: every assignment identifier resolves to an assignment ([])
- **PASS**: every domain identifier is D1-D33 ([])
- **PASS**: the old "Part G" survives only as the capstone Part and in the note that its numbering is retired ([])
- **PASS**: no "Part H", "On demand (Part G)", "Eight parts", "41 domains", "18 domains" or "D24 to D41" wording
- **PASS**: no stale statement that the merged units are a separate block ("printed after D14", "never read as a block" as for a Part)
- **PASS**: the reading ladder printed in D17, D18, D19 and D21 is the order in which the units are printed ([('D17', True), ('D18', True), ('D19', True), ('D21', True)])
- **PASS**: a unit that "Builds on" another unit of its own domain is printed after it ([])
- **PASS**: every merged unit (153 plus 7 capstones) carries its Bridge for / On demand / Integration line ([])

## Fold 5. Coverage, domain map, ledger

- **PASS**: Appendix B has the same number of cell entries before and after (1,042) (1042 -> 1042)
- **PASS**: every source cell is cited by the images of the units that cited it before (1042 of 1042 entries agree)
- **PASS**: the domain map in the front matter lists all 33 domains with their true unit ranges (33 rows, 33 ranges correct)
- **PASS**: the removal ledger H.4 still lists 76 removed atoms with identifiers that resolve (76 rows)
- **PASS**: H.3 lists 86 cloud units with their on-demand targets, all merged units (86 rows)
- **PASS**: the On demand lines of cloud units name 196 units, all existing merged units (86 lines, 196 links)

## Fold 6. Size

- **PASS**: the folded document is within 1 % of the size of the document before the fold (folding does not delete) (2116432 -> 2123025 bytes (+0.31 %))

## Fold 7. Index files

- **PASS**: index_cloud.md lists the 450 units once each, in the order they are printed (450 lines)
- **PASS**: index_cloud.md titles equal the unit titles of the document
- **PASS**: index_cloud.md marks 150 bridges, 153 merged units and 17 capstones (150 bridges, 153 merged, 17 capstones)
- **PASS**: index_cloud.md has the 33 domain headings and 7 part headings of the document
- **PASS**: unified_curriculum_index.md maps all 160 old units to final units with the same title (160 entries, 160 correct)
- **PASS**: the old-to-final map of the ML index equals H.2 of the document
- **PASS**: both index files contain no "Part G" except the capstone Part and the retired-numbering note, and no D34-D41

# Part 3. First-merge identifiers to final identifiers (to read Part 1)

Units keep their order inside each first-merge domain; the offsets are those of Appendix H.2 of the document. Cloud identifiers and the capstones U13.11 to U13.17 did not change.

| First-merge domain | First-merge units | Final units |
|---|---|---|
| D24 Pre-calculus Bridge | U24.1–U24.5 | U21.7–U21.11 |
| D25 Discrete Mathematics | U25.1–U25.7 | U21.12–U21.18 |
| D26 Single-Variable Calculus and Real Analysis | U26.1–U26.5 | U24.1–U24.5 |
| D27 Multivariable and Vector Calculus | U27.1–U27.5 | U24.6–U24.10 |
| D28 Linear Algebra | U28.1–U28.11 | U18.14–U18.24 |
| D29 Probability and Stochastic Models | U29.1–U29.9 | U19.18–U19.26 |
| D30 Statistics and Statistical Inference | U30.1–U30.6 | U19.27–U19.32 |
| D31 Differential Equations, Dynamical Systems, Numerical Methods, Complex Analysis and Transforms | U31.1–U31.7 | U24.11–U24.17 |
| D32 Optimization | U32.1–U32.17 | U25.1–U25.17 |
| D33 Machine Learning Foundations | U33.0–U33.14 | U26.0–U26.14 |
| D34 Sequential Decision Making | U34.1–U34.6 | U27.1–U27.6 |
| D35 Deep Learning Foundations | U35.1–U35.8 | U28.1–U28.8 |
| D36 NLP, the Transformer and Large Language Models | U36.1–U36.10 | U29.1–U29.10 |
| D37 Deep Generative Models | U37.1–U37.8 | U30.1–U30.8 |
| D38 Retrieval-Augmented Generation and Agentic Systems | U38.1–U38.15 | U31.1–U31.15 |
| D39 Evaluation, Safety and Responsible AI | U39.1–U39.6 | U32.1–U32.6 |
| D40 ML Systems, Efficiency and Distributed and Federated Learning | U40.1–U40.6 | U33.1–U33.6 |
| D41 Approximation Algorithms and Computational Complexity | U41.1–U41.7 | U17.18–U17.24 |

# Part 4. Remaining limits

- The fold changes where a unit stands and what it is numbered, not what it says. Pairs of same-subject units (a compact cloud unit beside the full merged unit, Appendix G.2) are still two units: merging their prose would mean rewriting cloud units, which are source-cited and were left untouched on purpose. Hence the document stays at about 2.1 MB; the word-level overlap between a cloud unit and a merged unit is under 50 % at most (largest 0.47) and nearly always under 35 %.
- The reading ladders and the subject map were chosen by judgement (for example calculus and optimization are domains of their own, not folded into cloud domains that have a different aim); the audit checks that the ladders are the printed order and that prerequisites named in a "Builds on" line come first, not that the order is the best one.
- The multiple-choice, multiple-select and derivation keys of the merged assignments were read and checked by hand, one by one (not by a program); the 153 numerical keys were recomputed by program; the checkable numeric predictions of the 153 programming questions were run with reference code, but no complete reference solution of each programming task was written.
- The word-level source check (section 9 of Part 1) counts a source atom as covered when 75 % of its content stems occur in the citing units; it detects omissions, not weak teaching. About-text atoms (audience, prerequisites, industry, instructor biography) are not required content. It was run before the fold; the fold audit shows that every unit body is unchanged, so the result carries over.
- Cloud-side assignments and coverage are those of the earlier audit (build check and assignment checker re-run: unchanged).
