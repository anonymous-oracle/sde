# Curriculum Validation Report

## Source Inventory

| Key | Path | Lines | Bytes | SHA1 |
| --- | --- | ---: | ---: | --- |
| textbooks | /Users/Suhas.KS/textbooks.md | 97 | 4537 | 53f97401689270cd82353b5e6585fff6bff3a539 |
| analysis | /Users/Suhas.KS/CurriculumSpine2.txt | 239 | 48929 | 0db16171cdf13beeb7f457ef600250ac679335a7 |
| dense | /Users/Suhas.KS/curriculum-spine.md | 2 | 40579 | 08c597cc68c09854fa5c9377b589a94e0cb10655 |
| structured | /Users/Suhas.KS/curriculum-spine2.md | 435 | 22328 | 3aeb5eb529ea5efe23b8a6a9ea3a2748207ef533 |
| master | /Users/Suhas.KS/master-curriculum.md | 773 | 116373 | bbd527857811bb5066746c3e2c47124dbc8f7c36 |

## Source Relationships

- `CurriculumSpine2.txt` appears verbatim as the first `239` lines of `master-curriculum.md`.
- `textbooks.md` appears verbatim as the final `97` lines of `master-curriculum.md`.
- `curriculum-spine2.md` section beginning with `# UNIFIED MATHEMATICAL AND TECHNICAL CURRICULUM ARCHITECTURE REFERENCE` begins at line `244` of `master-curriculum.md`.

## Artifact Coverage

- Lossless archive path: `/Users/Suhas.KS/sde/curriculum_artifacts/curriculum_lossless_archive.md`
- Pure dump path: `/Users/Suhas.KS/sde/curriculum_artifacts/curriculum_pure_dump.md`
- Omission ledger path: `/Users/Suhas.KS/sde/curriculum_artifacts/curriculum_omission_ledger.csv`
- Lossless archive preservation rule: every source file is embedded verbatim in a fenced block.
- Pure dump rule: bibliography, deconstructions, module spine, and supplementary taxonomy are included; audit and policy lines are excluded by rule.

## Pure Dump Inclusion Summary

- Included line rows: `468`
- Excluded line rows: `1076`
- Partially normalized line rows: `2`

## Anchor Verification

| Anchor | In Lossless Archive | In Pure Dump |
| --- | --- | --- |
| Audit Checkpoint 1 | yes | no |
| Audit Checkpoint 2 | yes | no |
| Audit Checkpoint 3 | yes | no |
| Audit Checkpoint 4 | yes | no |
| Audit Checkpoint 5 | yes | no |
| Operational Execution Strategy | yes | no |
| Hall & Knight | yes | yes |
| Tattersall | yes | yes |
| Apostol | yes | yes |
| Rosen | yes | yes |
| Grimaldi | yes | yes |
| aima-python | yes | yes |
| OpenFst Toolkit | yes | yes |
| Karhunen- | yes | yes |
| BigQuery ML | yes | yes |
| PANCE | yes | yes |
| Pathology: The Big Picture | yes | yes |

## Regression Check Against Prior Derived Dump

- Prior derived dump `curriculum-load.md` has SHA1 `2f6da535ff266a696b1a5bcf6428dd87dec2ddc9` and line count `992`.
- Sentinel `Operational Execution Strategy`: prior dump `no`, lossless archive `yes`, pure dump `no`.
- Sentinel `Audit Checkpoint 1`: prior dump `no`, lossless archive `yes`, pure dump `no`.
- Sentinel `The rapid evolution of artificial intelligence`: prior dump `no`, lossless archive `yes`, pure dump `no`.
- Sentinel `The development of Automatic Speech Recognition`: prior dump `no`, lossless archive `yes`, pure dump `yes`.

## Verdict

- Lossless archive status: PASS. All original source files are preserved verbatim.
- Pure dump status: DERIVED VIEW. It intentionally excludes audit/process/policy material and normalizes the dense supplementary source.