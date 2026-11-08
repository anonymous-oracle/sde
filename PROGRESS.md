# PROGRESS: architecture unification (runbook /workspace/sde/cloud_curriculum_unification_runbook.md)

Environment: workspace /workspace/cloud; outputs /workspace/sde/out/ (originals in /workspace/sde untouched).
Merge patch appended to srclib.py (backup srclib_pre_merge.py.bak). Formula checks in verify/v_b*.py.

| Batch | Status | Checks after batch |
|---|---|---|
| B1 U14.1-U14.5 | done | build check: 232 cells, cited 173 (MCA:W2 atoms pending U14.6); chk_assign units 137 bad 0; NAT dump read; verify/v_b1.py all pass |
| B2 U14.6-U14.9 | done | build check: cited 192, no arch MISS; chk_assign units 141 bad 0; NAT dump read; verify/v_b2.py all pass |
| B3 U14.10-U14.13 | done | build check: cited 202, missing 114 (baseline), no arch MISS with -o; chk_assign units 145 bad 0; NAT dump read; verify/v_b3.py all pass (one script expectation corrected: FR-FCFS example 17 -> 9) |
| B4 U14.14-U14.16 | done | build check: cited 217, missing 114 (baseline), no arch MISS with -o; chk_assign units 148 bad 0; NAT dump read; verify/v_b4.py all pass (MSI/MESI model checker 6/11, 8/14 states; litmus enumerator; CDG checker) |
| B5 U14.17-U14.20 | done | build check: cited 230 (MCA:W12 QoS atoms pending U14.21), no other arch MISS with -o; chk_assign units 152 bad 0; NAT dump read; verify/v_b5.py all pass (SIMT, coalescing, systolic simulator, quantiser) |
| B6 U14.21, U14.22, U13.7, section 5 pointers | done | build check: cells cited 232/232, missing 114 (baseline, no architecture MISS); chk_assign units 154 bad 0; verify/v_b6.py all pass (UCP partition, fairness metrics, WRR, CV^2f/DVFS, SECDED (72,64) fault injection, FIT/MTTF, TMR, cache-channel model); pointer edits to U4.1, U9.16, U9.9, U11.8, U11.9, U12.3 appended to Gap-fills (no text moved or deleted) |
| B7 front matter, assembler, index, acceptance | done | front_cloud.md and assemble_cloud.py edited per section 8; build check cited 232/232 uncited 0; chk_assign units 154 bad 0; assemble: units 161 domains 14 with assignments 154; index regenerated (14/161/154/17 bridges/7 capstones/232 cells/19 courses); no dangling U refs; 154 collapsed keys; NAT dump 154 lines read; overlap greps done (U14.9 and U14.16 ownership wording corrected to U3.11/U10.6 and U3.2/U3.3/U3.10); D1-D13 diff = six pointer sentences only |

## D15 (dbms.txt) addition, 2026-11-05
| Batch | Status | Checks |
|---|---|---|
| D1 U15.1-U15.6 | done | verify/v_d1.py, ra.py pass |
| D2 U15.7-U15.13 | done | verify/v_d2.py, dbx.py pass |
| D3-D5 U15.14-U15.23 | done | verify/v_d3-v_d5b.py, bpt.py pass |
| D6 U15.24-U15.27, U13.8 | done | verify/v_d6.py, v_d7.py pass; assign/20_D15e.txt |
| Assembly | done | cells 306, cited 306, uncited 0; chk_assign units 181 bad 0; dangling refs none; 15 domains, 189 units, 181 assignments, 20 bridges, 8 capstones |
Edits: pointers in U10.1 and U9.17; front_cloud.md (counts, standing instruction 10, stage 7, tooling numbering fixed); assemble_cloud.py (ORDER, HANDLED, App A note, E.1, F, D.3 item 9); gen_index.py writes index_cloud.md.

## D16 (design patterns and System Design Primer) addition, 2026-11-06
| Batch | Status | Checks |
|---|---|---|
| Sources | done | cloned primer (ae9bbd7) and python-patterns (a8e4090); `design_src/mk_src4.py` writes `src4.txt` (54 cells: SDP, PYP, GOF) and `table.json`; `srclib_design.py` and a patch in `srclib.py` |
| U16.1-U16.7 (OO bridge, GoF and python-patterns, OO exercises) | done | `units/22_D16a.md`; coverage passes |
| U16.8-U16.13 (estimation, scalability, availability, data tier, caching, asynchronism) | done | `units/23_D16b.md`; `verify/v_e1.py` to `v_e4.py` pass |
| U16.14-U16.16 (worked designs, scaling story, reading lists) | done | `units/24_D16c.md`; `verify/v_e5.py` passes; min-hash figure corrected to 0.795 |
| Assignments A16.1-A16.16 | done | `assign/21_D16a.txt` to `23_D16c.txt`; chk_assign units 197 bad 0; NAT dump read, all 16 recomputed |
| Capstone U13.9 | done | in `units/14_D12_D13.md`; D13 Aim says nine |
| Assembly | done | cells 360, cited 360, uncited 0; no dangling U-references; 16 domains, 206 units, 197 assignments, 21 bridges, 9 capstones, 25 courses |
Edits: pointers added to U2.4, U3.11, U4.8, U6.7, U9.5, U9.13, U9.15, U9.16, U10.6, U11.6, U14.9, U15.20; `front_cloud.md` (counts, standing instruction 11, stage 9, capstones); `assemble_cloud.py` (ORDER with D16 after D12, Part D renamed, Appendix A licence note, D.1, D.3 item 10, E.1 rows, F rows); `gen_index.py`.

## Data-analytics extension (data-analytics.txt), 2026-11-06
| Batch | Status | Checks |
|---|---|---|
| Sources | done | src5.txt, srclib_data.py (92 cells), srclib.py _OFF5; 452 cells, uncited 0 |
| D17 to D21 units | done | units/25_D17.md to 29_D21.md; assign/24 to 28; verify/v_f1.py to v_f5.py |
| DBMS mapped to D15, BDC duplicate | done | src lines extended, no new unit |
| U13.10 capstone | done | units/14_D12_D13.md |
| Assembly | done | 21 domains, 265 units, 255 assignments, 30 bridges, 10 capstones, 33 courses |

## Second follow-up: R to Python, algorithms and data structures on demand, 2026-11-06
| Batch | Status | Checks |
|---|---|---|
| U21.3 rewritten (scientific Python) and assign/27_D21.txt | done | verify/v_f6.py, v_f6b.py; chk_assign bad 0 |
| U19.15 to U19.17 with PyMC, Bambi, ArviZ | done | verify/v_f7.py (all parts run); figures recorded in the units |
| Front matter, assembler, HANDLED, Appendix D items 11 to 13, E.1 | done | no R-code remains; names kept only where the text says what replaces them |
| D17 entry map, Bridge-for lines, U17.15 to U17.17, 37 pointer sentences | done | verify/v_f8.py; assign/24_D17.txt now 17 units |
| Assembly | done | build check uncited 0 (27 known CSP misses); chk_assign units 258 bad 0; 21 domains, 268 units, 258 assignments, 46 bridges, 10 capstones, 452 cells, 33 courses; no dangling references |

## Software engineering, Go on demand, and the unification pass, 2026-11-06
| Batch | Status | Checks |
|---|---|---|
| Source ingest | done | src6.txt (87 lines), srclib_se.py (ISE, SEM; 26 cells), srclib.py _OFF6; 478 cells, uncited 0 |
| D22 units U22.1 to U22.14 and assign/29_D22.txt | done | units/30_D22.md; verify/v_g1.py to v_g3.py (+ .out); 4 flagged phrases fixed by quoting the source spelling; two wrong claims found on re-read and corrected (delay ratio at load 0.95 is about 4, not 10; basis-path wording) |
| D23 Go units U23.1 to U23.8 and assign/30_D23.txt | done | units/31_D23.md; `go/` module (11 packages, 35 tests), `go/verify.sh` output in verify/v_go.out; gofmt and go vet clean; go test -race passes; race demo (build tag racedemo) reports a data race; Dockerfile not built (no daemon) |
| Go track lines | done | 29 existing units (D4, D9, D10, D11, D12, D13, D15, D16) each name the U23 unit to enter and the result to reproduce |
| Unification and de-duplication | done | 21 edits (probability U21.6, birthday U5.1, Bloom U3.1, universal hashing U17.5, consistent hashing U9.5, shortest paths and MST D17, flows U17.14, MMU/TLB U4.1, 2PL/WAL/precedence D15, relational engine D15 and U13.8, UML U22.9, sketches U20.2/U20.3); Appendix G register; coverage re-run after each batch |
| Assembly | done | build check uncited 0 (27 known CSP misses only); chk_assign units 280 bad 0; no dangling references; 23 domains, 290 units, 280 assignments, 55 bridges, 10 capstones, 478 cells, 35 courses |

## ML curriculum merged into the cloud curriculum (Part G), 2026-11-06
| Batch | Status | Checks |
|---|---|---|
| Plan: ID scheme, demand map, dedupe policy | done | idmap.py, demand.py (86 cloud units, 196 links), ledger2.py |
| Import of 160 ML units and 153 assignments | done | ml_import.py -> units_ml/D24..D41.md, D13_add.md, assign_ml/, merge_ledger.json; 76 atoms removed (owner named), 37 kept on purpose |
| Wiring | done | cloud_wire.py (idempotent): 86 On demand (Part G) lines, 7 stale-wording fixes, D13 aim; 95 Part G units start with "Bridge for" |
| Assembly | done | assemble_cloud.py, assemble_ml.py, front_cloud.md; 8 parts, 41 domains, 450 units, 433 assignments, 17 capstones, 150 bridges, 79 courses, 1,042 cells |
| Index files | done | gen_index.py -> index_cloud.md, unified_curriculum_index.md (old to new map) |
| Audit | done | audit.py -> merge_audit_report.md; 63 checks, 63 pass. First run found 3 real ledger weakenings (handshake lemma, Euler's formula, Cauchy-Schwarz); restored. With the source files supplied: mlcheck.py (564 cells, 4,150 atoms, 44 flagged, all prose or source typos, 0 technical) and verify_keys.py (all 153 numeric keys recomputed; A40.1 key corrected to 170.67) |
| Old ML file | done | unified_curriculum.md now carries a SUPERSEDED banner, text unchanged |

## Final sweep of the merge (answer keys)

| Step | Status | Notes |
|---|---|---|
| Q1/Q2 keys (306) | done | read one by one against their options; one fix (A35.5 Q2 option D reworded so it is plainly false) |
| Q3 keys (153) | done | recomputed independently (verify_keys.py, 127) plus the audit script (26); one fix earlier (A40.1 = 170.67) |
| Q4 outlines (153) | done | read against their questions; no defects |
| Q5 predictions (153) | done | checkable numeric claims run with reference code (q5_reference_checks.py) or recomputed by hand; four keys corrected: A32.12 (water level 1.469, noise level = 1/gain now stated), A28.1 (error about 1e-12 to 1e-11), A28.8 (smallest eigenvalue at rounding level about 1e-15), A28.11 (OMP success about 85 percent) |
| Counts | fixed | the programming questions number 153, not 148 (front_cloud.md, H.1, audit limits, old unified_curriculum.md) |
| Audit | 63 of 63 pass | with the six KEY_FIXES in H.1 and checked by the assignment-identity check |

## Fold by subject (second pass, 2026-11-06)

User instruction: "Fold by subject but in addition, ensure that all topics still remain in the file. The only requirement here is that the cloud curriculum file is the primary curriculum and the other file is taught on demand but is folded by subject."

| Step | Status | Notes |
|---|---|---|
| Subject map | done | pre-calculus and discrete mathematics into D21 (U21.7-U21.18); approximation and complexity into D17 (U17.18-U17.24); linear algebra into D18 (U18.14-U18.24); probability and statistics into D19 (U19.18-U19.32); calculus, differential equations, numerics, complex analysis into new D24; optimization D25; ML foundations to ML systems D26-D33 at the start of Part E. Cloud IDs unchanged; 7 parts, 33 domains. |
| fold.py | done | runs on the audited first-merge document (F_doc.md); fold_core.py (parser, id map), fold_struct.py (ladders, layout), fold_rw.py (explicit rewrites), fold_text.py (generic wording rules) |
| Reading ladders | done | D17, D18, D19, D21 print compact cloud units beside the merged units that go deeper; the ladder is printed in each domain introduction |
| Fold audit | 41 of 41 pass | audit_fold.py: units paired by title, text identical up to identifiers and listed rewording, derived id map equals the formula, no word lost, all references resolve, old to final end-to-end with the old titles, indexes consistent |
| Indexes | done | gen_index_x.py -> index_cloud.md, unified_curriculum_index.md (old to final map) |
| Size | unchanged | about 2.1 MB: the overlap between a cloud unit and a merged unit is under 50 % at most; folding moves and renumbers, it does not delete. An earlier estimate of 25-35 % smaller was wrong. |
