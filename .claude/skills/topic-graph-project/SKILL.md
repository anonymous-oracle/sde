---
name: topic-graph-project
description: >
  Resume and run Suhas's curriculum topic-graph project (NPTEL/OCW/university course lists, ≤3-word topic filter with an
  n-gram language model and the local DeepSeek-R1 gatekeeper, MIT OCW corpus expansion, curriculum packs). Use when the
  user says "continue the topic graph / curriculum / OCW expansion / R1 service work", points at
  HANDOFF_curriculum_coverage.md, or asks to start, check or resume any step of that pipeline. Works together with /crew.
---

# Topic-graph project: how to resume and work

## 1. Start (read-only, do this before anything else)
1. Read `/Users/suhas/sde/HANDOFF_curriculum_coverage.md` fully (§0 goals, §1 state, §6 open items, §9 last session's scripts and decisions). Older detail: `ocw-courses/recovery/handoff_archive_20261110/`.
2. Check state, change nothing:
   ```
   BASE=/Users/suhas/sde/ocw-courses/recovery/topic_lm_20261110
   OCW=/Users/suhas/sde/ocw-courses/recovery/ocw_expansion_20261110
   pgrep -fl 'ollama|supervisor|queue_server|zipfetch|claude -p' || echo none-running
   ls -l $BASE/out/llmq/DOWN.flag      # 0 bytes = clear; non-empty blocks the supervisor
   ls $OCW; git -C ~/sde status --short
   ```
3. Report back what is running, what is half-done, and which open item comes next. Ask which to start unless the user said.

## 2. Work method
- Use `/crew`: master plans, briefs, reviews; workers are `claude-haiku-5-5` at `--effort medium`, no advisor, unless the user changes it. Brief says "Commit: NONE". Review worker output yourself before reporting (spot-check 3-5 claims against files/logs, never trust a report alone).
- Worker launch: `env -i`, allowlist `Bash(python3 -I:*)` plus read-only helpers; run all Python as `python3 -I -B` (no `__pycache__`); never `Bash(env:*)`. Workers have no network except the exception a brief grants (OCW work: ONLY `ocw.mit.edu`, generic User-Agent `course-list-research/1.0`, one request at a time, ≥0.5-1 s apart, exponential back-off with Retry-After; loopback 127.0.0.1 for local tests). Redirects to other hosts are not followed.
- Worker Bash calls time out after 10 min: long jobs must be resumable (checkpoint file, `--budget-seconds 480`, rerun until `DONE`).
- The crew skill text says "no git", this project adds: nothing is committed without Suhas's explicit yes; exclude the large untracked trees (`ocw-courses/recovery/graph_cloudgenai_20261110/`, `nptel/builds/full/graph/`).

## 3. Standing rules (Suhas's)
Ask before deleting ANY file (the only standing authorisation: a batch's raw downloaded OCW files after they are processed and verified, §9.4 of the handoff; never anything else; never `rmtree`). Ask before any commit. Stdlib Python only, no pip, no OCR, public/legal sources only. Never invent topics, sources, course codes, levels, assignments or capstones. Additive curriculum changes only. Never modify originals in `~/sde/nptel/`. Write new versions as new files and back up before replacing. **Do not touch any topics file until he says so.** Graph work always on a new copy; junk is retyped (`phrase`/`non_topic`), never dropped. R1 is the final gatekeeper for uncertain topics (reasoning on, one phrase per request, tool definitions on disk with sha256, all calls through the queue, ≤7.6 GB RAM).
Graph source of truth: `~/nptel-ocw.zip` (latest) or its plain copy `ocw-courses/recovery/graph_cloudgenai_20261110/expanded/`.

## 4. Pieces and where they live (details in handoff §3 and §9)
- R1 service: `python3 -I -B $BASE/code/llmq/supervisor.py start|stop|status` (Ollama 127.0.0.1:11500, queue 11600, cap 7600 MB, model `hf.co/bartowski/deepseek-ai_DeepSeek-R1-0528-Qwen3-8B-GGUF:Q6_K`, num_ctx 4096 ladder). Client: `$BASE/code/llmq/llmq.py` (`generate`, `build_raw_prompt`). Never a bare `ollama serve`. Start it only when R1 is needed, stop it after.
- LM / features / scorer: `$BASE/code/{tok,build_lm,eval_lm,w2_*,w3_*}.py`, outputs `$BASE/out/{lm,features,filter}`; gold labels `$BASE/out/gold_labels.tsv`. W3 scorer and W6 tools (`$BASE/tools/`) are unreviewed.
- OCW expansion: `$OCW/{probe,listing,zipfetch,zipfetch_test}.py`, lists `course_list.tsv`, `missing_courses.tsv`, `diff_*.tsv`, reports `ACCESS_REPORT.md`, `ZIPS_REPORT.md`. `zipfetch.py` was never run live: review before use.

## 5. OCW content fetch (when asked to run it)
Batches of 15 courses ascending by zip size: fetch kept members with explicit `Range: bytes=a-b` reads of each zip's central directory (the server answers suffix `bytes=-N` with HTTP 501; a 200 reply to a Range ⇒ STOP, never download a whole zip), keep text-like files only (never audio/video/images), convert (`pdftotext -layout`, Office via zipfile+xml, no OCR), write `processed/<slug>/docs.jsonl` in the corpus schema, verify, delete that batch's raw files (guarded function, dry-run first, log `batch_deleted.tsv`), append `BATCH_LEDGER.tsv`, next batch. Pass the live range test (small zip + 699 MB `6-007…` zip) and a loopback self-test before any bulk run. Suhas's caution: a course listing EECS/Math is not necessarily relevant, so add a relevance filter before widening the list or adding topics.

## 6. Lessons already paid for
- `DOWN.flag` empty = clear; do not ask to delete it. A worker once deleted `__pycache__` against the rule: forbid deletions in briefs and use `-B`.
- Watchdog kill test needs a loaded model (cap forced low with `LLMQ_MEM_CAP_MB`); memory reads 5.0-5.3 GB steady, 7.0-7.2 GB seen at cold load: cold loads are untested.
- Always end by updating the handoff (state, new script paths, decisions) and keep a backup copy of the previous handoff in the archive folder.
