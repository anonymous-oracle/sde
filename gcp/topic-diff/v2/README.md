# Fresh topic diff (v2)

This diff compares `gcp/unified-curriculum.md` (4,894 lines, eleven regions) against the gcp-lite topic files. It ran after the integration. The master grep-checked every "missing" verdict, and the verified gaps and false misses below reflect those verdicts. Covered verdicts were not re-checked, so some hidden gaps may remain.

## Regions

| Region | File | Curriculum lines | Topics | Covered | Partial | Missing (worker) | Out of scope |
|---|---|---|---|---|---|---|---|
| v01 | [f01_mission_graph_single_track.md](f01_mission_graph_single_track.md) | 1-385 | 607 | 461 | 107 | 37 | 2 |
| v02 | [f02_reference_maps_atlases_policies.md](f02_reference_maps_atlases_policies.md) | 386-882 | 488 | 374 | 102 | 4 | 8 |
| v03 | [f03_source_registry_atlases_1.md](f03_source_registry_atlases_1.md) | 883-1300 | 338 | 268 | 36 | 34 | 0 |
| v04 | [f04_atlases_2_audit.md](f04_atlases_2_audit.md) | 1301-1733 | 262 | 162 | 78 | 22 | 0 |
| v05r | [f05_master_bibliography_textbooks_1.md](f05_master_bibliography_textbooks_1.md) | 1734-2115 | 483 | 348 | 90 | 45 | 0 |
| v05b | [f05b_textbook_deconstructions_1.md](f05b_textbook_deconstructions_1.md) | 2116-2489 | 497 | 326 | 121 | 36 | 14 |
| v06 | [f06_textbooks_2.md](f06_textbooks_2.md) | 2490-2863 | 338 | 282 | 41 | 7 | 8 |
| v07 | [f07_teaching_spine.md](f07_teaching_spine.md) | 2864-3406 | 349 | 311 | 28 | 6 | 4 |
| v08 | [f08_libraries_stats_archive.md](f08_libraries_stats_archive.md) | 3407-3847 | 270 | 195 | 44 | 23 | 8 |
| v09 | [f09_nasiko_go_spines.md](f09_nasiko_go_spines.md) | 3848-4327 | 331 | 280 | 28 | 0 | 23 |
| v10 | [f10_tools_design_phases_glossary.md](f10_tools_design_phases_glossary.md) | 4328-4894 | 265 | 237 | 19 | 0 | 9 |
| Total | | 1-4894 | 4228 | 3244 | 694 | 214 | 76 |

Counts are read from each file's Counts line. The v05b and v08 Counts lines use a different format and were read as written: v05b "covered 326 · partial 121 · missing 36 · out of scope 14 (total 497)", v08 "covered 195 | partial 44 | missing 23 | out of scope 8 | total 270". No Counts line had placeholders, so no value is n/a. The "Missing (worker)" column is the workers' count before master verification; the verified list is under "Verified gaps by part".

## Verified gaps by part

### part01
- Divisibility rules (v06)
- Place value (v05b)

### part03
- Trust-region methods (v04); Line search (Armijo, Wolfe) with trust regions (v02; merges with v04 trust-region)
- Subgradients (v04)
- Mirror descent (v04)
- ADMM (v04)
- Practical significance and effect size (v01)
- Multilinear forms; complexification (v03)
- Voting and apportionment (v03); Voting methods and fair division (v05r; filed at part04, merged here)
- Multi-objective least squares (v03)
- Burnside's lemma and orbit counting (v03)
- Derivative-free optimization; nonlinear least squares (Gauss-Newton, LM); Frank-Wolfe; alternating minimization (v05r)
- Combinatorial and non-stationary bandits (v05r)
- Sampling without replacement and the hypergeometric distribution (v05b)
- Bertrand's paradox (v05b)
- Location-scale families (v05b)

### part03b
- Quadric surfaces (v07)
- Numerical quadrature rules (trapezoid, Simpson) (v01; partial at part03b:17)
- Direction fields; phase-plane analysis (v03)
- Equicontinuity (v03)
- Potential theory and harmonic functions (v03)
- Boundary value problems and Sturm–Liouville theory (v03)
- Real-number foundations: uniqueness of the reals as complete ordered field; perfect sets (v05b)
- Series: summation by parts; Cauchy product and rearrangements (v05b)
- Rectifiable curves; differentiation under the integral; partitions of unity (v05b)

### part03c
- Bandpass sampling and oversampling; Karhunen-Loeve expansion (v05r)
- Sparse FFT; DSP tricks (frequency translation, interpolation) (v05b)

### part04
- Domain-expert validation of outputs (v01)
- Power of a point (v03)

### part08
- Differential testing against a reference implementation (v01)
- Approximation algorithms (v02)
- Arithmetic coding and stream codes (v05r)
- Augmenting data structures (order-statistic and interval trees) (v05b)
- Bipartite matching algorithms (Hopcroft-Karp, augmenting paths) (v05b; Hungarian at part03:176)

### part09
- HTTP redirection status codes (v03)
- WebDAV and publishing with PUT (v03)

### part11
- gRPC security (TLS, per-call credentials) (v03)
- Transaction script, active record and data mapper (v03)
- Architecture reconstruction (v03)

### part12
- SQL join types: outer, semi and anti joins (v01; join algorithms exist at part12:88) [verify]
- Database process model (v03)
- Optimistic offline concurrency / optimistic locking (v03)

### part14
- Security assurance and Common Criteria (v03)
- OAuth dynamic client registration (v03)
- Secure development lifecycle (v03)
- Host header validation (v02)
- Cache-Control no-store for sensitive responses (v02; caching headers at part09:75)

### part18
- Init containers (v03; sidecars partial at part23:54)

### part19
- Data contracts between producers and consumers (v01)
- Data versioning tools (DVC/lakeFS) (v01; partial at part19b:71)
- Reinforcement learning and psychology or neuroscience (v06)
- Reinforcement learning case studies (games, control) (v06)
- Hierarchical forecast reconciliation (v04)
- Causal inference g-methods: effect modification, selection/measurement bias, g-formula, g-estimation, causal survival, time-varying treatments (v05r); Target trial emulation (v04); Causal mediation analysis (v04)
- ICA; GAMs; online learning and regret; algorithmic stability; structural risk minimization; convex learning problems (v05r)
- Judgmental forecasting; dynamic regression (v05r)
- ML design patterns catalogue (v05r)
- Reproducing kernel Hilbert spaces (v05b; kernel trick at part19:57)
- RBMs and DBN pretraining (v05b)

### part19b
- Epsilon removal in weighted automata (v07)
- OpenFst library and composition simulation (v07)
- Gestalt grouping (v06)
- Algorithm evaluation and error analysis for multi-view geometry (v06)
- Camera calibration with a calibration target (v01; only autocalibration at part19b:62)
- Character error rate (v01)
- ASR system fusion (ROVER) (v05r)
- Acoustic echo cancellation and beamforming (v05b)
- Chomsky hierarchy for language modelling; combinatory categorial grammar (v05b)

### part20
- Multimodal evaluation (v01)
- RL with verifiable rewards (RLVR) and format rewards (v05r)

### part22
- Industry capstone: business problem to deployed solution (v07)
- Safety regression testing on model or prompt change (v01; red-team exists)

### part30
- Credit and income tax (v05r)
- Volumetric, translucent and non-photorealistic rendering (v05b)

## Graduate-depth candidates (not recommended for the core)

From the curriculum's IIT/IISc cross-check (§17.1.17), both items below are marked single-sourced and unverified; algebra, topology and differential geometry are listed in the ARCHIVE atlas row; decision pending with the user.

- GRAD-17.1.17 | (v08, institutional cross-check, single-sourced) polynomial hierarchy; space-bounded computation; circuit complexity; PCP and interactive proofs; I/O and DMA; superscalar/VLIW; register allocation; representation theory; fundamental group and homology; Lp spaces; Frenet-Serret curves; surfaces/fundamental forms/geodesics/Gauss-Bonnet; compactness and Löwenheim-Skolem; Gödel incompleteness; Ramsey theory; extremal graph theory; design theory; hardness assumptions; PDE existence/uniqueness; Sobolev; PDE maximum principle; Green's functions
- ARCHIVE? | Abstract algebra and Galois theory; point-set and algebraic topology; differential geometry (v04; unified-curriculum line 557 marks these ARCHIVE)

## False misses

- Flash attention (v07) -> part20:37
- Structure from motion and SLAM (v07) -> part19:170, part19b:61
- Section formula (v06) -> part01:77
- Top-k retrieval and WAND (v06) -> part19b:77
- v04: histogram equalization part19b:67; sequence-discriminative part19b:27; speaker adaptation part19b:25; PLP part19b:18; i-vectors part19b:43; state clustering part19b:31; flash attention part20:37; paged attention part22:138; FLOP accounting part20:49, part22:154; GSPO part19:148; grammar-constrained decoding part21:99; model abuse part19:205 (partial)
- v08: ELIZA part22
- v01: benchmark crossover part08:129; transformations of RVs part03:76; statistical power part03:112; missing data part19:71; GIN/GiST/BRIN part12:80; robust/stochastic opt part03:181; corners/descriptors part19:171; RANSAC part19:172; DNN-HMM part19b:26; accent/noise part19b:35; scaling laws part20:49; catastrophic forgetting part20:69; token budgets part22:64; CFG part20:158; watermark part19b:50; datasheets part20:79; LLM routing part21:75; evaluator-optimizer part22:14; prompt leak part14:245; threat models part14; ADMM (dup of v04); PQ/IVF part20:179
- v03: matrix computation complexity part03:142/part08:124; functional limits part03b:50; inter-service comms part11:26; database per service part11:13; architecture risk part11:158; partial-only: vector-valued functions part03b:10, derived data part11:138, long-running ops part23:186, infra testing part18:93, multilinear part19b:61; quadric surfaces dup of v07
- v05r: BFGS part03:178; Gram-Schmidt part03:146 (signal space partial, part03c:50); Kelly/gambling part30:12; uniform convergence partial part03b:56 + VC part19:75; quantization/pruning part20 (4 hits); pixel connectivity partial part03:35
- v05b: countable sets part03:21; connected sets part03b:54; gamma part03b:29; inverse matrices part03:145; errors-in-variables part19:79; speech coding part19b:17; portfolio/Kelly part30:12; partition function part19:85; dependency parsing part19:127; algorithm-independent ML partial (bias-variance part19:48); shares and dividends = ARCHIVE (M18), out of scope; Counts line format nonstandard

## Partials

- v01: 107 partial rows; see the "Partial in this range" section of [f01_mission_graph_single_track.md](f01_mission_graph_single_track.md).
- v02: 102 partial rows; see the "Partial in this range" section of [f02_reference_maps_atlases_policies.md](f02_reference_maps_atlases_policies.md).
- v03: 36 partial rows; see the "Partial in this range" section of [f03_source_registry_atlases_1.md](f03_source_registry_atlases_1.md).
- v04: 78 partial rows; see the "Partial in this range" section of [f04_atlases_2_audit.md](f04_atlases_2_audit.md).
- v05r: 90 partial rows; see the "Partial in this range" section of [f05_master_bibliography_textbooks_1.md](f05_master_bibliography_textbooks_1.md).
- v05b: 121 partial rows; see the "Partial in this range" section of [f05b_textbook_deconstructions_1.md](f05b_textbook_deconstructions_1.md).
- v06: 41 partial rows; see the "Partial in this range" section of [f06_textbooks_2.md](f06_textbooks_2.md).
- v07: 28 partial rows; see the "Partial in this range" section of [f07_teaching_spine.md](f07_teaching_spine.md).
- v08: 44 partial rows; see the "Partial in this range" section of [f08_libraries_stats_archive.md](f08_libraries_stats_archive.md).
- v09: 28 partial rows; see the "Partial in this range" section of [f09_nasiko_go_spines.md](f09_nasiko_go_spines.md).
- v10: 19 partial rows; see the "Partial in this range" section of [f10_tools_design_phases_glossary.md](f10_tools_design_phases_glossary.md).

## Next step

The verified gaps await the user's approval before any topic file is edited.
