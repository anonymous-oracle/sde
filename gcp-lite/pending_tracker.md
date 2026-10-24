# Pending Tracker

Learner: suhass149 · Course: the GCP Lite curriculum (index: `Consolidated_Topic_Index_GCP.md`, 3,749 lines, 20 sections, 229 topic groups, 2,805 topic lines) · Tutor skill: `learn`

Renamed from `billing_pending_queue.md` and expanded on 6 October 2026. Created 3 October 2026. Dedicated copy created 8 October 2026 from Part B of `progress.md`. **Refreshed 24 October 2026** for a move to a new chat: concepts 14 to 36 are now recorded (sections 3.6 and 3.7), errors 13 to 22 are logged, the cold-retry queue is extended, and the index is now also split into 29 parts (`gcp-lite/index/00_index_map.md`). Companion file: `gcp-lite/SESSION_HANDOFF_2026-10-24.md`.

**Scope of this file (learner's instruction, 11 Oct 2026):** it logs concepts that are intentionally paused, yet to be taught, or blocked on a prerequisite. Do not update it every turn; update it at the close of a sub-topic or when something is paused, blocked or newly pending. What has been taught is recorded in the handoff and in sections 3.6 and 3.7.

This is the learner's full curriculum record: what has been taught, what is in progress, what is pending, what is waiting on billing, and the dependencies to teach just in time. The billing queue is kept intact as section 8.

**Status marks used below:** `[x]` taught · `[~]` in progress or partly taught (a named slice) · `[ ]` not started · `$` waits on billing or trial credit.

## Contents

1. Snapshot
2. Instructions and overrides in force
3. Progress report: what has been taught
4. Records: error log, misconceptions, errata, predictions, decisions, heuristics
5. The practical track: what we do next
6. Just-in-time prerequisite register
7. Section-by-section tracker (all 20 sections, 229 groups)
8. Billing and credit queue
9. Open verifications
10. Resume point
11. Log

## 1. Snapshot

- The index holds 20 sections (19 domains plus the ML case-study appendix), 229 topic groups and 2,805 topic lines. It is also cut into 29 parts (rules file plus topic list each); the current part is **05** (Python and shell).
- Marked taught at topic level: Number systems, Storage units, Character encoding (Computer Organization), all at L1 and L2, engineering pass only; and in Python: the whole Core language group and the Environment and tooling group through `parametrize` (see 3.6). Nothing has reached the mastery bar: no academic pass, no cold recall result.
- Paused: Data layout, at alignment and padding (override 8). Do not raise.
- Partly taught (named slices): Boolean logic, Combinational circuits, The memory hierarchy, Latency numbers (Computer Organization); Page arithmetic (Databases, Pre-SQL foundations); a Go toolchain slice (3.5).
- Python runtime model started: reference counting, reference cycles and the cycle collector, and call by sharing are taught (concepts 34 to 36). The exercise for that sub-topic (`language-theory/exercise-36/memory.py`) is submitted and the review is open.
- Parked in the billing queue: billing account, a real budget, the Storage units disk lab, the Latency numbers two-VM lab.
- The tutor numbers concepts consecutively from 11 Oct 2026 (concept-14 onward). Concept-36 (call by sharing) is the last closed. The next new concept is 37.
- Last refreshed 24 Oct 2026.

## 2. Instructions and overrides in force

Precedence: the learner's explicit instruction in the current chat wins, then the learner's preferences, then the index method.

### Overrides (recorded in the learner's words where possible)

1. **6 Oct 2026: pause Computer Organization and start the practical track.** *(Clarified later the same day, see 7: the list was examples, not the whole scope.)* "Right now, I want to focus on learning cloud, software systems design, required mathematics for it, SQL databases, from the scratch middleware implementations, coding concepts in golang, etc." The index order is suspended for those areas. If a strict dependency arises, teach the prerequisite topic at that point and note it (section 6). The rest of the index resumes afterwards, in index order. The paused topic is Data layout, at alignment and padding.
2. **WITHDRAWN (6 Oct, later): Python, then Go, then TypeScript stays in force.** The earlier note below was an overreading of the focus list.
   Original note: **Python, then Go, then TypeScript (standing preference) versus Go now.** The learner asked for Go. Recorded as an override: Go is taught first; confirm at the start of Go that Python is deferred, and check programming basics at that point (what a variable, function and loop are) before assuming them.
3. **Reflection rung dropped for Page arithmetic only** ("I cannot afford to spend so much time on a single topic"). Scope: that one topic. Not extended to others unless the learner says so.
4. **Top rungs rely only on what has been taught** (said after a top rung used modular congruence notation before it was taught). In force for every topic.
5. **More elaborate explanations** (said twice during Data layout: "your explanations are not elaborate", and that 55 minutes were lost on alignment). In force: teach the mechanism with a byte-by-byte or step-by-step worked example before the check; when a check is missed twice, stop correcting separately and re-teach the whole idea once, with one test the learner can run on their own answer.
6. **No ready-made code to paste (6 Oct 2026, Go).** "I need to learn to code in golang, do not give me ready snippets to simply paste and run." In force for all coding: the tutor describes the task in words, may show syntax only as a pattern with placeholders (never a runnable program or solution), and reviews the learner's own code line by line. The learner types everything. The first hello-world program was shown in full before this instruction; it is not repeated.
7. **Follow the index order; the focus list was examples (6 Oct 2026, later).** "I only asked you to pause that, not pick from a few example topics I listed." In force: after the paused Computer Organization, teach the index sections in their own order and each section from its first group. The areas the learner named (cloud, systems design, the maths they need, SQL, middleware, Go) are where the course is heading, not a filter. Strict dependencies are still taught just in time and noted. Mathematics and Problem Solving come before Programming Languages in the index; the maths is taught as each topic needs it (section 6), and Problem Solving habits run through everything.

8. **Keep Computer Organization (alignment and padding) paused (8 Oct 2026, resume).** "Keep the pause on that until we finish other parts of the curriculum or until I tell you to teach them or if there is a rigid requirement of it as a prerequisite." In force: do not raise the alignment total-size check or any other paused Computer Organization item unless the learner asks or a strict prerequisite demands it (then note it in section 6 and the log). Continue Programming Languages & Language Theory.
9. **Exercise rule (24 Oct 2026).** The learner asked for exercises with guidance to write real code after a few concepts, not endless checks. In force for the whole course: one small exercise per sub-topic of 3 to 5 concepts, one key idea each, never two exercises for one concept; elaborate exercises only at the top rung of a topic group; the tutor never gives a runnable solution; the learner predicts first, builds, runs and reports. Revised 24 Oct 2026: predictions and exercises are never mixed. A prediction is read and answered with one reason, never run or typed; an exercise is written by the learner from a task in words, with no snippet to copy. Concepts between exercises get predictions only. The full rule is in the Project doc "Exercise Rules".
10. **Subagents and the tracker's scope (11 Oct 2026).** "You may utilise haiku 5.5 subagents and assign reasoning tiers to them based on the task complexity within this chat. Use subagents to minimise token costs whenever appropriate. But you will be responsible for ensuring that the concepts are taught properly." Also: "the pending tracker is for logging in concepts that are intentionally paused or yet to be taught or paused because a pre-requisite is needed. Do not keep updating it every time needlessly." In force: bulk work may go to Haiku subagents; teaching stays in the main chat; this file is updated sparingly.
11. **Number the concepts (11 Oct 2026).** "Start numbering the concepts please. You need not stop." In force: concepts are numbered consecutively; the tutor continues without waiting between concepts when a check has been passed.
12. **Teaching-contract breach, 22 Oct 2026.** After a check whose worked example had already shown its answer (concept-26), the learner said: "I hope you are aware about the teaching guidelines. If not re-ingest all project files and chat files for a refresher. I mean all files." In force: never put a check's answer in the explanation that precedes it; re-ingest everything when asked or after a compaction. Predictions are written before anything is run; a missing prediction or reason is asked for again.

### Standing rules and preferences (from the index method and this chat)

- One check per turn. Exactly one focused question, never answered by the tutor in the same turn, answerable from what has been taught.
- Correction format: confirm what is right, then sharpen the mechanism. No false praise, no emoji.
- Personal account only. The workplace account is browse-only: `list`, `describe`, `get-iam-policy` and other read-only commands.
- The $300 trial credit (3-month expiry) is reserved for demanding labs. Do not start it for light labs.
- No billing account exists. Creating one may prompt the trial; whether it can be created without starting the trial clock is open (section 8, item 1).
- Before anything paid is created: a budget alert exists, and the project shown in the Cloud Shell prompt is the personal one.
- Paid resources for a lab are deleted the same day, and the deletion is confirmed with a read-only command.
- The learner writes every cloud command. The tutor teaches the grammar (product, resource group, verb, name, flags) and the `--help` path only.
- A missed check is reworded and made smaller, never repeated word for word.
- Numbers always carry units. Recalled figures are flagged `(verify)` until checked in a primary source.
- No time boxes: progress is by passing checks. The learner is time-conscious, so avoid detours and say so when a topic is running long.
- Ten-rung ramp: anchor, vocabulary, representation, core move, worked illustration, then basic unseen check, routine variation, mixed transfer, top rung, reflection.
- Mastery states and recall: taught, in progress, shaky, sliced, unverified. Recalls at about 1, 3, 7 and 21 sessions.
- Tone: warm and direct, no emoji, no false praise.

## 3. Progress report: what has been taught

All topics below are at engineering pass, L1 to L2, unless stated. "Guided" means a hint or nudge was needed, which keeps the cold retry on the list.

### 3.1 Computer Organization & Data Representation, Data representation

**Number systems** · `[x]` taught · parts 1 to 5, 8, 9 and 24 to 37 · code evidence pending
- Bits and bytes; why base 2. Place values; binary to decimal and back. Pattern count 2^n; unsigned range 0 to 2^n − 1.
- Hexadecimal; one hex digit is 4 bits; hex to binary and binary to hex; both unseen checks passed.
- Positional notation in any base (value = sum of digit × base^position). Base conversion by repeated division; read remainders bottom-up; why it terminates; step count = floor(log2 x) + 1.
- Binary addition with carries; overflow as wraparound (kept result = true sum minus a multiple of 2^n).
- Two's complement: negative top place value; negation by flip and add 1; range −2^(n−1) to 2^(n−1) − 1; wraparound at the top; sign extension; signed overflow when the carry into the sign column differs from the carry out.
- Bitwise AND, OR, XOR; masks; XOR as a toggle and its own inverse; x AND (x − 1) clears the lowest set bit; power-of-two test.
- Evidence: mixed transfer (signed 32-bit millisecond counter overflows after about 24.9 days): guided. Top rung (count of 8-bit signed x where x + x overflows, 128 of 256): guided. Reflection (one-sentence heuristic): passed with a prompt.
- Pending in this topic: code exercises (base conversion, two's-complement encode/decode and overflow detection, sign extension), the academic pass (prove one adder serves signed and unsigned values; derive the overflow condition from the carries), the 1/3/7/21-session recalls.
- Not yet taught and needed later: modular arithmetic as a formal tool (index: Mathematics, Proof and discrete mathematics). Only a preview ("remainder after dividing by 2^n") was given.

**Storage units** · `[x]` taught · parts 10 to 13 and 15 to 17 · lens depth 1 · lab and code pending `$`
- Binary versus decimal prefixes (KB/KiB, MB/MiB, GB/GiB); the gap per step is a factor 1.024, compounding: 2.4%, 4.86%, 7.37%.
- Powers of two by feel: 2^10 ≈ 10^3, 2^20 ≈ 10^6, 2^30 ≈ 10^9, 2^40 ≈ 10^12, with the drift quantified.
- Estimation: split into coefficient and power of ten. Worked and unseen: 10 million pastes of 1.27 KB (12.7 GB); 360 million 7-byte short codes (2.52 GB). Disk sold as 500 GB reads 465.66 GiB.
- GCP lens, depth 1: Compute Engine counts disk size in binary GB (GiB) and labels it GB (checked on Google's pricing page); a disk created at 100 holds 100 × 2^30 = 107,374,182,400 bytes. Other products not verified.
- Pending: the disk lab `$` (section 8, item 3); "by hand and in code" version of storage arithmetic; academic pass.

**Character encoding** · `[x]` taught · part 14, the unnumbered UTF-8 introduction, and parts 38 to 43 · code evidence pending
- ASCII (7 bits, 128 codes). Unicode code points. UTF-8 as a variable-length prefix code: header bits 0, 110, 1110, 11110, continuation 10; ASCII-compatible.
- Encoding and decoding 2-byte and 3-byte characters by hand; byte count versus character count; the code point ranges per length; overlong encodings (and why they are a security problem); self-synchronization; wrong-encoding reads (mojibake, Latin-1 shows one character per byte).
- Evidence: mixed transfer (10 million names, 120 MB) passed unaided; top rung (1,920 valid 2-byte sequences) guided.
- Pending: from-scratch encoder/decoder in code rejecting overlong and invalid sequences; 4-byte encode/decode by hand was introduced but not drilled; academic pass.

**Data layout** · `[~]` in progress · parts 44 to 46
- Endianness and network byte order: **taught, guided.** Big versus little endian, byte-level layouts, 16- and 32-bit examples, network order is big-endian, the misread 0x0A000001 → 0x0100000A, `ntohl`/`ntohs`. The learner explained the mechanism back correctly.
- Alignment and padding: **in progress, paused.** The learner now applies the two-step test (next free offset; move to the first offset divisible by this field's own size) correctly for offsets. Open: the total-size rule (round up to a multiple of the largest field) on an unseen struct. See section 4 for the misconception register entry.
- Open check: for `u8 a; u16 b; u32 c; u8 d`, offsets were given correctly (0, 2, 4, 8); the total size under rule 3 is still to be answered. The answer is not recorded here.
- Natural return point: Go struct layout and `unsafe.Sizeof` (Go, memory group), or sooner if asked.

**Error detection** · `[ ]` next in index order (parity, CRC as polynomial division over GF(2), detection versus authentication). Needs polynomial arithmetic over GF(2), which is not yet taught.

### 3.2 Computer Organization, Digital logic and Machine organization (partly taught)

**Boolean logic** · `[~]` sliced · parts 6 and 7
- Taught: AND, OR, NOT, XOR and truth tables; the same logic reappears in the carry of binary addition (XOR for the sum digit, AND for the carry).
- Pending: Boolean algebra laws (identity, complement, distributive, De Morgan); sum-of-products and product-of-sums; NAND/NOR functional completeness; Karnaugh maps up to four variables; the IAM policy and firewall rule readings of the same logic.

**Combinational circuits** · `[~]` sliced · parts 7 and 8
- Taught: the half adder idea (sum = XOR, carry = AND); carry rippling across columns (why a simple adder slows with width).
- Pending: full adder; n-bit ripple-carry adder with its O(n) delay; carry-lookahead (O(log n)); multiplexers and decoders; the from-scratch gates-to-adder exercise.

**The memory hierarchy** · `[~]` sliced · parts 19 to 21
- Taught: cache hit and miss; hit rate; average latency = hit rate × cache latency + miss rate × slow-source latency (a simplified model); speedup = old time ÷ new time; misses dominate the average; a cache 100× faster gave only about 9× at a 90% hit rate; the 50% and 90% comparison; improving hit rate beats improving cache speed in the worked case.
- Pending: SRAM/DRAM/flash/disk; locality; cache organization (direct-mapped, set-associative, fully associative; tag, index, offset); write-through versus write-back; the three Cs; AMAT level by level (the full formula was not given); virtual memory and the TLB from the hardware side.

**Latency numbers** · `[~]` sliced · parts 18 to 21 · lab pending `$`
- Taught: ns, µs, ms and their 1,000× steps; four reference figures (memory about 100 ns, SSD random 4 KB read about 150 µs, data-centre round trip about 500 µs, disk seek about 10 ms; all `(verify)`); converting to a common unit before comparing (SSD about 1,500× slower than memory); why caching tiers exist (the full-scan example: 47,620 pages with a 90% hit rate took about 719 ms in the model).
- Pending: the rest of the reference table (L1, mispredict, L2, mutex, compress, 1 Gbps transfers, sequential reads, intercontinental round trip); transfer rates; same-zone, cross-zone and cross-region latency; the ping/iperf3 lab `$` (section 8, item 4).

**Not started in Computer Organization:** Sequential logic; Instruction set architecture; Performance laws (Amdahl, Little, Iron law); Parallel hardware and cache coherence; Performance engineering; Error detection; the section's exercises and capstone (RV32I machine with a cache model).

### 3.3 Databases, Pre-SQL foundations (one slice)

**Page arithmetic** · `[~]` sliced · parts 22 and 23, plus a mixed transfer and a top rung · taught early from an earlier version of the plan
- Taught: an 8 KiB page (8,192 bytes); usable bytes = page × fill factor; rows per page = floor(usable ÷ row size); pages needed = ceiling(rows ÷ rows per page); table size = pages × 8 KiB; overhead against raw data; the smallest whole-number fill factor for a target rows-per-page, rounded up.
- Worked results: 200 B rows at 90% fill give 36 rows per page, 27,778 pages for 1,000,000 rows (about 217 MiB, 14% over raw); 300 B rows at 80% give 21 rows per page, 47,620 pages; 22 rows per page needs 81%, cutting pages to 45,455 (4.5% fewer) at the cost of 300 bytes less free space per page.
- Reflection rung skipped by override. The one-line decision record was drafted ("I pick 81% because it cuts pages by 4.5%; I accept less free space per page for updates"). The update/fragmentation cost was explained, not yet taught in depth.
- Pending in this section: the other six Pre-SQL lines (relations as sets and bags, three-valued logic, types and encodings, files for loading, tooling with `psql` and Postgres in Docker, driver hygiene), then the whole section from its start.

### 3.4 Touched in passing, never formally taught

These come from School-level foundations and were used as tools. The section's own walk (and exit audit) has not been done, and "prerequisites verified through woven checks" has only covered what appeared.

- Exponents and powers of two; percentages and ratios; unit conversion between ns, µs, ms and s; significant figures and standard form; weighted averages; floor and ceiling rounding; counting inclusive ranges (the fencepost rule, b − a + 1); basic inequalities; solving for a smaller case; comparing candidates by plugging them back.
- Straight-line forecasting (budgets): spend so far ÷ days elapsed × days in month.
- GCP: Cloud Shell, the command grammar, `gcloud projects list` with `--filter` and `--format=json`, finding filter keys from the JSON.
- A curriculum map (published page) and a Playground of six tools exist as study aids: https://claude.ai/artifact/9ukLuALUU1S9EYsX9qX9hn. They are not evidence of mastery.

### 3.5 Programming Languages & Language Theory: Go slice, taught out of order

Taught on 6 Oct 2026 before the index order was restored (override 7). Kept on record as a slice. The Go groups will be reached in place after Python and Shell; this slice then becomes recall and does not need re-teaching from zero.

**Go, toolchain and program structure** · `[~]` sliced · taught in this order
- The `go` command as a toolchain; `go <verb> <flags> <what>`; a compiled language. The smallest program (package main, import, func main) was shown in full once, before the no-pasteable-code rule.
- Packages (a directory, one package, import path versus package name, exported versus package-private names, `internal/`); modules (`go.mod`, module path, import path = module path + directory, `go.sum`, the proxy, versions and `/v2`, `go get`, `go mod tidy`); the standard library lives outside `go.mod`; compiler rules (unused imports and variables are errors, no import cycles, init order, naming). Not verified by any exercise.
- Variables: `:=`, `var`, zero values, no implicit conversions, `float64(x)`. Integer division truncates toward zero; `%` takes the dividend's sign; the identity (a / b) * b + a % b = a.
- Control flow: `for` (three shapes), `if`, conditions must be bool.
- Evidence: two-line program (unaided; compile-time constant `6*7` noted); divisible-by-3 loop 1 to 20 (unaided; formatting looks gofmt-clean); integer division −9 / 4 (first attempt wrong, applied Python floor division; guided pass); −9 % 4 (unaided).
- Not yet done in this group: minimal version selection derivation, the `go` line and `GOTOOLCHAIN`, `gofmt -l` and `go vet` run by the learner, constants and `iota`, `range`, `switch`, labels, per-iteration loop variables; Go version in Cloud Shell not yet checked.
- Setup: Go runs in Cloud Shell (the learner ran a program there).
- Dependencies noted: IEEE 754 floats (floating point not yet taught).

### 3.6 Programming Languages & Language Theory: Python (in progress; index part 05)

**Python** · `[~]` in progress · setup: Python 3.12.3 in Cloud Shell; the learner also runs Python locally in `/Users/suhas/sde` (the `.ml-venv` there is git-ignored).

**Numbering.** Concepts 1 to 13 are the learner's own numbering of the first stretch (folders `concept-1` to `concept-13` in `language-theory/`: the Go slice, then Python core and classes). Concepts 14 onward are numbered by the tutor from 11 Oct 2026. Concept-36 is the last closed.

**Against the index bullets (part 05, group Python):**

| Index bullet | State | Notes |
|---|---|---|
| Core: variables, expressions and control flow | taught | 8 Oct; passed unaided |
| Core: functions, arguments and return values; recursion | taught | 8 Oct; digit-sum built unaided; mutable-default argument taught (two unseen variants passed) |
| Core: list, dict, set, tuple; the dict as a hash table | taught | 8 Oct |
| Core: classes and object-oriented basics | taught | `__init__`, `self`, class versus instance attributes, lookup order, `__str__`, `__eq__` (identity by default), `isinstance`, `NotImplemented` and the fallback; concepts 14 and 15 |
| Core: modules, packages and imports | taught | concepts 16 to 19 and the shop exercise |
| Core: exceptions, `try`/`finally`, context managers; reading a traceback | taught | concepts 20 to 24 |
| Environment: virtual environments; pip; lock files | taught | concepts 25 and 26 |
| Environment: a hand-built test runner, then pytest (fixtures, parametrisation, assert rewriting) | partly taught | runner built (27 to 31); pytest basics (32) and `parametrize` (33) taught; **fixtures not taught**; assert rewriting only seen in a failure report, not formally taught |
| Runtime: call by sharing; names as references; reference counting plus a cycle collector | taught | concepts 34 to 36; exercise submitted, review open |
| Runtime: the GIL and the free-threaded build; `asyncio` | not started | |
| Runtime: arbitrary-precision `int`; floor division and modulo with negative operands | not started as a topic | `//` and `%` were taught on 8 Oct (floor, remainder takes the divisor's sign, contrasted with Go); concept-37 is planned as the negative-operand prediction |
| Runtime: `str` versus `bytes`; `decimal.Decimal` | not started | IEEE 754 floating point is a prerequisite to pull forward |
| Runtime: late-binding closures; the mutable-default trap | not started (closures); the mutable-default trap was taught on 8 Oct and is to be formalised | |
| Data and services: NumPy, pandas, Matplotlib, FastAPI | not started | |

**Evidence by building (learner's own files, all reviewed):** `concept-1` Go hello and `6*7`; `concept-3` divisible-by-3 loop; `concept-4` divisibility in Go and Python; `concept-5` word counter; `concept-6` digit sum; `concept-9` Rectangle; `concept-10` Counter; `concept-11/12/13` Bag, Money `__eq__`, Money `__str__`; `concept-14` Money `isinstance`/`NotImplemented`; `concept-15-mixed` Cart tags; `concept-16` and `concept-17` import caching and the `__name__` guard; `concept-16-19/python` the `shop` package; `concept-30` and `concept-31` hand-built test runners; `concept-32/test_items.py` and `concept-33/test_items.py` pytest and `parametrize`; `concept-34/main.py` reference counts; `exercise-36/memory.py` (review open). All of this is committed on branch `gcp` (latest commit `22a742b`).

**Still to check on earlier material:** Money `__str__` with negative cents (floor division gives a negative dollar count and a positive remainder); not yet asked.

### 3.7 Concepts 14 to 36 (tutor numbering), with the result of each check

"Passed" means the check was answered correctly with its mechanism. Errors are numbered in 4.1. Dates and results for 14 to 36 were reconstructed from the chat transcript on 24 Oct; the learner's folder history is the check if one looks off.

| # | Date | Concept | Result |
|---|---|---|---|
| 14 | 9 to 11 Oct | `==` across types: `isinstance`, returning `NotImplemented`, the reflected attempt, the fallback to identity | Code correct; no prediction given once (asked to predict from now on); generalised "always False" (error 13); `x is y` check passed |
| 15 | 11 Oct | Mutable class attribute versus instance attribute; `is` (Cart tags) | Passed; the name-lookup mechanism stated correctly, closing error 11 on evidence |
| 16 | 14 Oct | Modules and `import`: the first import runs the file, later imports hit the cache | Passed |
| 17 | 14 Oct | `__name__` and the main guard | Passed |
| 18 | 14 Oct | Packages and dotted imports; `__init__.py` runs once; the cache is keyed by full dotted name | Passed |
| 19 | 14 Oct | Where Python looks for modules (`sys.path`); shadowing by a local `json.py` | Passed; omitted that the shadowing file's top-level code runs first |
| 16 to 19 exercise | 24 Oct | The `shop` package: `__init__.py`, `cart.py` with a guard, `main.py` | Built by the learner. Run 1 predicted and run correctly (`Shop initialised`, `Inside Cart`, `991`). Run 2 omitted at first; the retry predicted `Inside Cart` then `6` correctly, with the reason (only an import runs `__init__.py`). Style note: spaces around `==` in the guard |
| 20 | 14 Oct | Exceptions and `try`/`except`; the frame is discarded and the search moves up the stack | Output correct; the reason lacked the unwinding step |
| 21 | 15 Oct | Which `except` catches which; operands are evaluated before `//` (`10 // d[k]`) | Passed with the exact mechanism |
| 22 | 16 Oct | `finally`: runs as the frame unwinds, before the caller's `except` | Passed with the exact mechanism |
| 23 | 16 Oct | Context managers and `with` | Wrong first (put `out` after `caught`, no reason; error 14); after a smaller check, correct and explained. `__exit__` returning `True` swallows the exception: told, not drilled |
| 24 | 17 Oct | Reading a traceback | Function names right (`c`, `b`, `a`); missed the `<module>` frame and the line number (error 15); smaller check passed (line 2) |
| 25 | 22 Oct | Virtual environments: `PATH`, the venv's `pip`, `site-packages` | `pip` choice right; `deactivate` wrongly said to remove the environment (error 16) |
| 26 | 22 Oct | `pip freeze`, requirements files, pinning | The first check leaked its answer in the worked example (tutor error; the learner objected); retry in new wording passed: pinning one package does not pin its dependencies |
| 27 | 22 Oct | `assert` and what a test is | `test_a pass` and `test_b fail` right; `test_c` wrongly called a fail (error 17); the retry reasoning was correct |
| 28 | 22 Oct | The general `Exception` and clause order | Passed; the order trap (a general clause first makes the specific clause dead code) taught |
| 29 | 22 Oct | Finding the tests automatically: the `test_` prefix and `callable` | Passed |
| 30 | 22 to 23 Oct | Build your own test runner (no code from the tutor) | Built `runner.py`; the first send had only output (no code, no prediction); on review the structure was right, one gap fixed (`except Exception as e` so any crash counts as an error, shown by `test_e`) |
| 31 | 23 Oct | `finally` inside the runner (mixed transfer) | Prediction written first and matched; missed the spec: the same text for every test instead of `done <name>` (error 18, open) |
| 32 | 23 Oct | pytest versus the hand-built runner | Counts right (2 passes, 2 fails); the learner then ran it: `.FF.`, so pytest is verified in the record; `>` versus `E` in the failure body explained |
| 33 | 23 to 24 Oct | `parametrize` | Per-test results right; progress line given as `..F` for six cases (error 19) |
| 34 | 24 Oct | Reference counting; a container holds one reference per slot | Lines 3 and 4 wrong first (error 20); the retry passed; counts 1, 2, 4, 3, 1 correct |
| 35 | 24 Oct | Reference cycles and the cycle collector | "Everything goes" after `del a, b` (error 21); after re-teaching, the one-sentence answer was correct |
| 36 | 24 Oct | Call by sharing: mutation through a parameter is visible, rebinding is local, strings can only be rebound | `{"n": 5}` right; `t` wrongly said to become `"hi!"` (error 22); the second answer was correct with the reason |
| 34 to 36 exercise | 24 Oct | Run the collector, then two independent objects (A), then a real cycle (B) | `memory.py` submitted; **review open** (see 10) |

## 4. Records

### 4.1 Error log (the learner's errors, by cause, with cold retries)

Cold retries are due after about 1, 3 and 7 sessions, unseen variants only. None has been attempted yet.

| # | Topic | What happened | Cause | State |
|---|---|---|---|---|
| 1 | Page arithmetic | Gave 36.864 rows per page | Ignored the whole-number constraint (floor) | Closed on evidence (two later variants correct); retry due |
| 2 | Number systems, mixed transfer | Signed 32-bit counter: 46.3 days instead of 24.9 | Read a signed range as unsigned; used the 2^10 ≈ 10^3 shortcut where three significant figures needed exact values | Guided pass; retry due |
| 3 | Number systems, top rung | Count of overflowing x + x: answered 7, then 126 as a boundary | No method; did not plug a candidate back into the condition | Guided pass; retry due |
| 4 | Character encoding, top rung | Counted valid 2-byte UTF-8 sequences as the largest value (2,047 − 128) | Largest value taken for a count; missing the +1 | Guided pass; retry due |
| 5 | Data layout, endianness | Said the little-endian reader "reads 01 first" | Mixed up which byte lands at the lowest address | Corrected; later explained correctly |
| 6 | Data layout, alignment | Padded every field up to the largest field's size; padded before the first field; compared the previous field's size instead of testing the next start offset | Rule restated several times without a single self-test | Offsets now correct; total size open; retry due |
| 8 | Go, integer division | Said −9 ÷ 4 is −3 | Applied Python-style floor division instead of truncation toward zero | Guided pass; retry due |
| 9 | Terminology | "Overloading" for "overlong"; "fill rate" for "fill factor"; "GiB is lower" for "fewer GiB for the same bytes"; "class objects" for "instances" | Loose vocabulary | Corrected in place |
| 10 | Python classes, Tag | Predicted `m.prefix` is "x" after `Tag.prefix = "y"` where `__init__` set `self.prefix` | Missed that `__init__` copies the value into the instance, so the later class change is not seen | Corrected; later described as a broadcast (wording imprecise) |
| 11 | Python classes, Bag | Said `append` triggers the fallback to the class attribute | Confused the lookup of a name with the method call on the result | Corrected; fix written; retry due |
| 12 | Python classes, Money | Reported the first `==` output as False without the reason | Result given with no reasoning; reason (default `==` is identity) not yet stated | Closed 8 Oct: learner said default `==` compares the object's own identifier; vocabulary sharpened (identity, same test as `is`); retry due |
| 13 | Python concept-14, `Blank` | Generalised "always False" from the one Money case | Reasoned from a single observed case; the fallback gives True for the same object | Corrected; `x is y` check passed |
| 14 | Python concept-23, `with` | Put `out` after `caught`, with no reason | Treated `__exit__` as running after the handler | Corrected after a smaller check; retry due |
| 15 | Python concept-24, traceback | Missed the `<module>` frame and the line number | Read function names only | Smaller check passed (line 2); retry due |
| 16 | Python concept-25, `deactivate` | Said it removes the `.venv` environment | Confused a `PATH` change with deleting the directory | Corrected; retry due |
| 17 | Python concept-27, tests | Called `test_c` (division by zero) a fail | `ZeroDivisionError` is not `AssertionError`, so the runner's `except` does not match | Corrected; the later runner counts errors with `except Exception`; retry due |
| 18 | Python concept-31, runner | Printed the same text for every test instead of `done <name>` | Spec detail not read; the prediction matched the learner's own code | **Open**: not changed in the file yet |
| 19 | Python concept-33, `parametrize` | Progress line `..F` for six cases | Stopped after three characters; pytest prints one per collected case | Corrected (`..F..F`); retry due |
| 20 | Python concept-34, reference counts | Counted `c = [a, a]` as one reference | A container holds one reference per slot | Corrected; retry passed |
| 21 | Python concept-35, cycles | "Everything goes" after `del a, b` | Believed deleting the names frees the objects; missed the references the lists hold to each other | Corrected; later answer correct; the exercise is the cold test |
| 22 | Python concept-36, strings | Said `t` becomes `"hi!"` | Strings are immutable; `+` builds a new string and repoints only the local name | Corrected the same turn; second answer correct |

Pattern across 14 to 36: the learner often reports a result with no prediction or no reason, and the tutor has had to ask again (concepts 14, 23, 30, 31, 33, 36). Ask for the reason as the whole check when it matters.

(Error number 7 was struck from the log: it depended on congruence notation that had not been taught; see errata.)

### 4.2 Misconception register

- Pad every struct field to the largest field's size. **Open, repeated three times. Paused.**
- `append` (a method call) makes Python fall back to the class attribute. Actual: the name `items` is looked up (instance, then class) and `append` then runs on whatever object that lookup returned. Closed on evidence at concept-15.
- Class attribute changes "broadcast" to all instances. Actual: only instances with no own attribute of that name see the change. Corrected.
- The largest value of a range is its count (off by one). Corrected; watch in any counting problem.
- Integer division floors (Go truncates toward zero; Python floors). Corrected; to be tested again at concept-37.
- A GiB is "lower" than a GB. Corrected.
- The little-endian reader begins from the most significant end. Corrected.
- `==` returning `NotImplemented` always ends in `False`. Actual: the fallback is identity, so the same object gives `True`. Corrected.
- `__exit__` runs after the outer handler. Actual: it runs on leaving the `with` block, while the exception is still in flight. Corrected.
- `deactivate` deletes the virtual environment. Actual: it only removes the venv's `bin/` from `PATH`. Corrected.
- A failing test is any failing test. Actual: the type matters (`AssertionError` is a fail; any other exception is an error in the learner's runner; pytest folds both into `F`). Corrected.
- Deleting names frees objects. Actual: objects are freed when their reference count reaches zero; two lists that refer to each other keep each other alive until the cycle collector runs. **Corrected; the exercise is the cold test.**
- A container counts as one reference. Actual: one per slot. Corrected.
- Strings can be changed in place through a parameter. Actual: strings are immutable; `+` makes a new object. Corrected.

### 4.3 Errata (the tutor's errors)

- Part 10: the check asked the learner to read back a number already printed in the same turn.
- Several checks held two questions (parts 16 and 41, and others), against the one-question rule.
- The top rung for Number systems depended on congruence notation and modular equations, which were not taught. The attempt was struck from the error log, and the problem was replaced.
- Said the index has "twelve domains"; it has 19 plus an appendix (20 sections).
- An earlier version of the index (with IDs like A1, SD-36, PQ-08) was used for the first stretch. IDs are retired; progress is recorded by topic name.
- The alignment rule was first worded so that "rule 2" blurred whose size decides padding; it took five rewordings to land on a self-test.
- Read the learner's list of focus areas as the whole scope, skipped Python and the first group of Programming Languages, and started Go. Corrected by override 7.
- Showed a complete working program to paste before the no-pasteable-code rule was set (it ran and printed hello, so the first Go step was a copy, not a build).
- The curriculum map page footer carried a wrong date (5 October); the session date is 6 October 2026.
- Standing cautions: do not state an answer in the same turn that asks the check; one question per check; do not use a concept in a top rung before it is taught; a mutable-default check that follows its own explanation is weak evidence, so use unseen variants.
- 22 Oct (concept-26): the worked example contained the answer to the check that followed it. The learner flagged it ("the answer was already in it"). The check was rewritten in new wording and passed; everything was re-read.
- 24 Oct (concepts 34 to 36): prediction checks were written as complete runnable snippets with "run to confirm", which put copy-and-run back into the course and mixed a prediction with an exercise. The learner objected; the Exercise Rule was split into predictions (read-only) and exercises (written from words). Recorded as override 9.
- 24 Oct: the first review of the shop exercise asked for files that were already in the learner's folder, because the folder was not yet connected; later the tutor said `memory.py` could not be found before the folder was connected. Both were resolved by connecting `/Users/suhas/sde`.
- 24 Oct: asked the learner which of "6 0 2" was a prediction and which a result; the learner pointed out the file already held part of that. The tutor then ran the file; the lesson is to run the code itself first and ask only for what the code cannot show (the prediction).

### 4.4 Predictions (predict, run, explain the gap)

- GiB count lower than 500 for a decimal 500 GB disk: right.
- Which cache improvement lowers average latency more (higher hit rate beats a faster cache): right.
- Little-endian value for network bytes 0A 00 00 01: wrong at first, right after a smaller step.
- Python Rectangle and Counter output predictions: right. Tag: wrong first. Bag: right outcome, wrong reason.
- No Brier-scored decision journal yet.
- Python concepts 14 to 36: see 3.7. Predictions skipped or without a reason on 14, 23, 30, 31 and 36; the exercises for concepts 16 to 19 and 34 to 36 are the first where a prediction is requested in writing before the run.

### 4.5 Decision journal

- Fill factor 81% over 80% for 300 B rows on 8 KiB pages: fewer pages (45,455 against 47,620, about 4.5%), accepted cost less free space per page (1,592 B against 1,892 B). Journal entry drafted; no confidence recorded.

### 4.6 Heuristics catalogue (named by the learner or discovered while solving)

1. Plug the candidate back into the condition before answering.
2. A second independent route (different method, or an approximation) before trusting a number.
3. Count a valid set as total minus invalid, and check range counts with b − a + 1.
4. Convert to one unit before comparing.
5. Find where a condition flips (the edges), then count the interval between them.
6. Turn a bit operation into arithmetic modulo 2^n (named, but the modular arithmetic itself is not yet taught).
7. Use the shortcut for the estimate and the exact value for the final digits.

### 4.7 Frontier list (asked about, parked)

- AWS and Azure certifications (in the index under Cloud Providers; Google Cloud first).
- Why encoding matters in production pipelines beyond mojibake (BigQuery strings) `(verify)`.
- Hand-checking the cost of the 81% decision on updates (heap pages and HOT updates, in Databases).

### 4.8 Cold-retry queue (new wording, unseen variants only)

1. Page arithmetic: rows per page needs a floor.
2. Signed 32-bit counter overflow time (signed range, not unsigned).
3. Count of 8-bit values where x + x overflows (method: plug candidates back into the condition).
4. UTF-8 count of valid 2-byte sequences (count = largest − smallest + 1).
5. Little-endian: which byte sits at the lowest address.
6. Alignment: whose size decides the padding; the total-size rule. **Paused; do not raise.**
7. Go: −9 / 4 truncates toward zero; `%` follows the dividend; contrast with Python `//` and `%` (links to concept-37).
8. Python: mutable default argument (unseen variants).
9. Python: Tag prediction (class attribute changed after `__init__` copied it).
10. Python: Bag (`append` runs on whatever the name `items` resolved to).
11. Python: why default `==` gave False (Money); the fallback after `NotImplemented`.
12. Python: the order of `__exit__` and the outer handler.
13. Python: a traceback lists `<module>` first and the last frame shows the raising line.
14. Python: what `deactivate` changes.
15. Python: test outcome by exception type (fail versus error), and clause order.
16. Python: pytest prints one character per collected case (`parametrize`).
17. Python: reference counts, one per slot.
18. Python: cycles; deleting names versus references held inside objects.
19. Python: strings are immutable; rebinding versus mutating a parameter.

## 5. The practical track: what we do next

**Focus areas (learner's list, 6 Oct 2026):** A. cloud; B. software systems design; C. the mathematics those need; D. SQL databases; E. middleware implemented from scratch; F. Go. "Etc." is open: add areas here as they come up.

**CURRENT PLAN (replaces the proposed order below, 6 Oct 2026 later):** teach Programming Languages & Language Theory from its first group, in index order: Python; Shell and working with APIs from code; the seven Go groups; TypeScript; Wire formats; Language theory; Exercises. Then continue through the index in order (Data Structures, Networking, Operating Systems, Software Architecture, Databases, Distributed Systems, Security, Delivery, Cloud Core and so on), with Mathematics and Problem Solving taught just in time and strict dependencies noted in section 6. The Go slice already taught (section 3.5) is recalled in place when its group arrives.

*(The proposed order below is kept for reference only. It was superseded because it picked Go from the learner's examples.)*

**How it works:** teach a focus topic in the order below. When a strict dependency appears, stop, teach the prerequisite at that point (section 6 lists the known ones), note it in the log, then return. Anything not listed in the six areas stays in index order and waits.

### Superseded proposed order (kept for reference)

1. **Go, first stretch:** toolchain and program structure; then composite data, functions, errors and text. Setup check first: what Cloud Shell offers (Go, editor) or a local install.
2. **Go, memory and types** (structs, pointers, interfaces, generics). Alignment and padding resume here as Go struct layout.
3. **Networking for middleware, just in time:** TCP, then HTTP/1.1. Then **Go: a raw-TCP echo server and a minimal HTTP/1.1 server and client, from scratch.** (Middleware, step 1.)
4. **SQL, first stretch** (local, free): the rest of Pre-SQL foundations, relational theory, the SQL language, using Postgres in Docker (teach the minimum Docker needed at that point).
5. **Go concurrency**, then **Go HTTP services with `net/http`** and **middleware chains** (recover, request ID, logging, authentication, rate limit), plus the token bucket. (Middleware, step 2.)
6. **Go `database/sql`** against the local Postgres; transactions and retries.
7. **From-scratch middleware set:** layer-7 reverse proxy (round-robin, least-connections, health checks); consistent hashing with virtual nodes; circuit breaker, retry with jittered backoff and bulkhead; a distributed rate limiter; an API gateway edge with graceful shutdown. (Middleware, step 3.)
8. **Cloud:** Cloud Computing Core (service models, virtualization and containers, well-architected, FinOps, IAM concepts), then Google Cloud groups: read-only console and `gcloud list/describe` first; paid and credit labs parked (section 8).
9. **Systems design:** Software Architecture groups and Distributed Systems groups, with the math pieces taught as they arise (section 6).
10. **SQL, second stretch:** storage and access methods, query processing, transactions, recovery and replication, data modelling, operating databases; the page-arithmetic slice continues in storage and access methods.

### Area A. Cloud
- Sections: Cloud Computing Core (6 groups); Cloud Providers, the nine Google Cloud groups. AWS, Azure and certifications are parked.
- Free or read-only first: concepts, console browsing, `gcloud` list/describe in the personal project, Terraform plan-only, local emulators. Paid labs: section 8.
- Prerequisites to check at the start (index): OS virtualization, namespaces and cgroups; availability arithmetic; access-control models and OAuth/OIDC; networking (VPC, subnets, CIDR, DNS, TLS, load balancing); databases and distributed-systems vocabulary; Bash, JSON and `jq`.
- Capstone: see the section tracker (Cloud Computing Core and Cloud Providers).

### Area B. Software systems design
- Sections: Software Architecture, APIs, Design Patterns & Clean Architecture; Distributed Systems & Large-Scale System Design (system design method, design techniques, caching, queues, partitioning, replication, consensus, availability).
- Prerequisites to check: networking (TCP, DNS, load balancing, latency numbers), databases (transactions, isolation, replication, indexes), concurrency, probability, queueing, partial orders, hashing.
- Cross-domain capstone for the systems domains: one production service on Google Cloud (credit lab).

### Area C. Required mathematics (just in time, not the whole domain)
- Needed for the above (from the prerequisite lines): sets, relations, functions, bags; propositional and predicate logic; counting and induction; partial orders; conditional probability, expected value, indicator variables; the birthday bound, balls into bins, order statistics; the exponential distribution; percentiles and histograms; Little's law and utilization; availability arithmetic (series and parallel); floating point (IEEE 754); modular arithmetic and hashing; logarithms and exponents.
- Parked until needed: linear algebra, calculus and optimization, information theory, signals and sequences, decision mathematics, most of statistics.

### Area D. SQL databases
- Section: Databases, SQL, Relational Theory & Data Modelling: all 12 groups, in the order listed in section 7.
- Local first: Postgres in Docker with volumes and health checks (free). Managed Cloud SQL: credit lab.
- Prerequisites to check: sets, relations and bags; three-valued logic; binary search, sorting, hashing and trees (B-trees); the storage hierarchy with page and row arithmetic (partly taught); integers versus floats and encodings; files, CSV and JSON; a language with a database driver (Go); virtual memory and `fsync`; concurrency (locks, deadlock).

### Area E. Middleware from scratch
- Where the index puts it: Go, HTTP services with `net/http` (echo server and a minimal HTTP/1.1 server over raw TCP first; middleware chains and their order); Networking exercises (a layer-7 reverse proxy with round-robin and least-connections balancing and health checks; consistent hashing with virtual nodes); Software Architecture exercises (dependency-injection container; in-process event bus; circuit breaker, retry with jittered backoff and a bulkhead; decorator as middleware); Distributed Systems exercises (a distributed rate limiter; outbox relay with idempotent consumers); DevOps (NGINX and API gateways); Security (rate-limit algorithms: token bucket, leaky bucket, fixed and sliding windows).
- Strict dependencies: Go basics, interfaces and function values, goroutines and `context`, HTTP semantics, TCP sockets, testing with `httptest`.

### Area F. Go
- Groups, in order: toolchain and program structure; composite data, functions, errors and text; memory, types with behaviour and generics; the everyday standard library; concurrency; engineering (testing, benchmarks, HTTP services, `database/sql`); cross-language contrasts.
- Index acceptance for Go code: `gofmt -l` prints nothing; `go vet ./...` clean; tests pass under `go test -race`; no silently dropped error; every goroutine has a way to stop. Each Go group ends with one involved problem the learner writes alone; the tutor never writes the solution.
- Strict dependencies: computer literacy and the terminal; data representation including floating point (taught except floating point); induction; sets, relations and functions.

### Area G. Rust track (file added to the Project on 16 Oct 2026; yet to be taught)
- File: `Rust_Track_AI_Infrastructure.md` (21 projects, P1 to P21, ending in an AI serving platform capstone).
- Its own rule: start only after the first two or three Go groups (toolchain, composite data, memory and types) are mastered, so the two syntaxes do not settle together. Prerequisites: Python basics, the terminal and Git, binary/hex/two's complement/UTF-8, Big-O.
- Status: not started. Waits behind Python, Shell, and the first Go groups. Where it differs from the main curriculum, the Rust file governs the Rust track.

## 6. Just-in-time prerequisite register

When the left-hand topic starts, teach the right-hand prerequisite first (at the depth needed, then resume). Items marked "taught" need only a short recall.

| When this arrives | Teach first | Source and status |
|---|---|---|
| Go numeric types; any float in SQL or JSON | Floating point (IEEE 754: sign, exponent, mantissa; rounding) | Mathematics, Numerical computing; also a stated prerequisite of Programming Languages and Databases. **Not taught; pull forward (first surprising float result in Python, and at `Decimal`).** |
| Go strings, runes, `range` over strings | UTF-8 and code points | Taught |
| Go `encoding/binary`, wire formats, TCP headers | Endianness and network byte order | Taught (guided) |
| Go structs, `unsafe.Sizeof`, memory layout | Alignment and padding | **In progress, paused** |
| Go interfaces, generics | A few type-system basics (nominal versus structural typing, parametric polymorphism) | Software Architecture prerequisites; teach the minimum when reached |
| Go concurrency (goroutines, channels, mutexes, `sync/atomic`) | Threads and processes basics; locks and deadlock; happens-before in outline; atomic instructions in outline | Operating Systems (Processes and threads, Concurrency); Computer Organization (atomic instructions). **Not taught.** |
| Go `net/http`, echo server, raw TCP | TCP (connections, ports, streams), sockets in outline | Networking, Transport. **Not taught.** |
| HTTP/1.1 server from scratch, middleware | HTTP messages, methods, status codes, headers, connection reuse; HTTP semantics | Networking, HTTP and the web. **Not taught.** |
| TLS in Go, `crypto/tls`, cloud load balancers | TLS mechanics in outline; certificates | Networking, TLS mechanics. **Not taught.** |
| Rate-limiter middleware | Token bucket, leaky bucket, fixed and sliding windows; time and clocks; queueing basics (utilization) | Security (API abuse); Distributed Systems; Mathematics (Queueing). **Not taught.** |
| Reverse proxy and load balancer from scratch | Load-balancing algorithms; health checks; idle timeouts; DNS in outline | Networking, Middleboxes, proxies and load balancing. **Not taught.** |
| Consistent hashing with virtual nodes | Hash functions; modular arithmetic; balls into bins in outline | Data Structures (Hashing); Mathematics (number theory, probability). **Modular arithmetic not taught.** |
| Circuit breaker, retry with jitter, bulkhead | Exponential backoff; retry budgets; simple probability of independent failures | Software Architecture (Distributed application patterns); Mathematics (Probability). **Not taught.** |
| SQL, Pre-SQL foundations | Sets, relations, functions and bags; propositional and predicate logic; three-valued logic | Mathematics (Proof and discrete maths); Databases. **Not taught.** |
| SQL: Postgres in Docker, `psql` | Minimum Docker (images, containers, volumes, health checks); the terminal | DevOps (Docker); Computer literacy. **Not taught.** |
| SQL: indexes and B-trees; sorting and joins | Binary search; B-tree intuition; sorting and hashing; Big-O | Data Structures (Analysis, Trees and heaps, Sorting). **Not taught.** |
| SQL: storage and access methods | Page arithmetic (taught slice); virtual memory and `fsync` in outline | Databases; Operating Systems (Persistence). Slice taught. |
| SQL: transactions and concurrency control | Locks, deadlock, isolation vocabulary; concurrency basics | Operating Systems; Databases. **Not taught.** |
| Go `database/sql` | Go interfaces and `context`; connection pools; transactions | Go groups; Databases. **Not taught.** |
| Cloud: virtualization and containers | Virtual memory, page tables and privileged instructions in outline; namespaces and cgroups | Operating Systems (Virtual memory, Isolation); Computer Organization (VM and the TLB). **Not taught.** |
| Cloud: availability and SLAs | Probability of independent events; series versus parallel availability; "nines" arithmetic | Mathematics (Probability); Cloud economics. **Not taught.** |
| Cloud: IAM | Access-control models; OAuth 2.0 and OIDC tokens | Security (Access-control models, Authentication and sessions). **Not taught.** |
| Cloud: VPC, subnets, firewall rules, routing | CIDR notation (binary, powers of two, masks: taught); IP addressing and routing basics | Networking (Addressing). Binary side taught; the rest **not taught.** |
| Cloud: command line at depth | Bash scripting, JSON and `jq` | Programming Languages (Shell group). **Not taught.** |
| Distributed systems and system design | Percentiles and histograms; Little's law; order statistics; the birthday bound; partial orders; consistent hashing | Mathematics (Statistics, Queueing, Probability, Discrete); Data Structures. **Not taught.** |
| Software architecture, API design | OOP foundations; preconditions and postconditions; state machines and graphs; HTTP semantics | Programming Languages and Software Architecture groups. **Not taught.** |
| Security of any middleware (auth, sessions) | Hashing and password storage in outline; JWT structure | Security. **Not taught.** |
| The Go testing and benchmark groups | Statistics of repeated measurement (mean, variance, distributions) | Mathematics (Statistics). **Not taught.** |

## 7. Section-by-section tracker

One line per topic group, in index order. Tags show which practical focus area a group belongs to (GO, MIDDLEWARE, SQL, CLOUD, DESIGN, MATH) or that it is a PREREQ to teach just in time. Untagged groups wait in index order.

### Group-level counts at a glance (as of 8 Oct 2026)

| # | Section | Taught | In progress / partly | Not started | Groups |
|---|---|---|---|---|---|
| 7.1 | School-level foundations | 0 | 0 | 16 | 16 |
| 7.2 | Computer Organization & Data Representation | 0 | 3 | 1 | 4 |
| 7.3 | Mathematics, Probability, Statistics, Queueing & Performance Modelling | 0 | 0 | 11 | 11 |
| 7.4 | Problem Solving, Reasoning & Research Method | 0 | 0 | 9 | 9 |
| 7.5 | Programming Languages & Language Theory | 0 | 2 | 11 | 13 |
| 7.6 | Data Structures, Algorithms & Computational Complexity | 0 | 0 | 11 | 11 |
| 7.7 | Computer Networking & Web Protocols | 0 | 0 | 12 | 12 |
| 7.8 | Operating Systems & Linux | 0 | 0 | 9 | 9 |
| 7.9 | Software Architecture, APIs, Design Patterns & Clean Architecture | 0 | 0 | 15 | 15 |
| 7.10 | Databases, SQL, Relational Theory & Data Modelling | 0 | 1 | 11 | 12 |
| 7.11 | Distributed Systems & Large-Scale System Design | 0 | 0 | 14 | 14 |
| 7.12 | Security, Cryptography, Privacy & Compliance | 0 | 0 | 19 | 19 |
| 7.13 | Software Delivery & Version Control | 0 | 0 | 4 | 4 |
| 7.14 | Cloud Computing Core: Virtualization, Well-Architected, Economics & IAM | 0 | 0 | 6 | 6 |
| 7.15 | The Architect's Practice: Decisions, Strategy & Career | 0 | 0 | 10 | 10 |
| 7.16 | DevOps & SRE: Docker, Kubernetes, NGINX, CI/CD, Infrastructure as Code, Observability | 0 | 0 | 8 | 8 |
| 7.17 | Machine Learning, MLOps & Production ML System Design | 0 | 0 | 9 | 9 |
| 7.18 | Generative AI, LLMs, Agents & Claude Applications | 0 | 0 | 15 | 15 |
| 7.19 | Cloud Providers: Google Cloud, AWS, Azure & Certifications | 0 | 0 | 20 | 20 |
| 7.20 | Published ML System-Design Case Studies | 0 | 0 | 12 | 12 |
| | **Total** | **0** | **6** | **223** | **229** |

Counts are groups, not topic lines. A group marked in progress or partly may contain taught topics. Taught at topic level: Number systems, Storage units, Character encoding (3 topics, 12 topic lines, about 0.4% of 2,805).

### 7.1 School-level foundations

16 groups, 39 topic lines.

- **Depth bar:** fast, error-free work on unseen multi-step problems in every group of this domain, with each rule justified rather than recalled. These are the roots every prerequisite chain ends in, so a gap here is closed before anything built on it.
- **Capstone:** a timed mixed set spanning every group, and a one-page explanation of a quantitative decision written for a non-expert.

- [ ] Arithmetic and number sense (4 lines)
- [ ] Units and dimensional reasoning (3 lines)
- [ ] Algebra (3 lines)
- [ ] Functions and graphs (3 lines)
- [ ] Exponents, roots and logarithms (3 lines)
- [ ] Sequences, series and notation (2 lines)
- [ ] Geometry, trigonometry and vectors (4 lines)
- [ ] Probability and data (3 lines)
- [ ] Sets and logic in words (2 lines)
- [ ] Proof habits (2 lines)
- [ ] Pre-calculus and calculus intuition (1 lines)
- [ ] Electricity and signals (1 lines)
- [ ] Computer literacy (2 lines)
- [ ] Technical reading and writing (2 lines)
- [ ] Technical communication (2 lines)
- [ ] Everyday economics (2 lines)

### 7.2 Computer Organization & Data Representation

4 groups, 79 topic lines.

- **Prerequisites (as written):** arithmetic and number sense; units; exponents and logarithms; sets and logic; electricity and signals.
- **Depth bar:** an undergraduate computer-architecture course with its labs: every representation encoded and decoded by hand, every performance law derived and used with numbers, every hardware effect measured on a real machine.
- **Capstone:** a simulated RV32I machine with a cache model, running a small recursive program and reporting cycles per instruction, hit rates and average memory access time against predictions written beforehand.

- [~] Data representation (19 lines) · in progress
- [~] Digital logic (14 lines) · partly taught
- [~] Machine organization (31 lines) · partly taught
- [ ] Exercises (15 lines)

### 7.3 Mathematics, Probability, Statistics, Queueing & Performance Modelling

11 groups, 159 topic lines.

- **Prerequisites (as written):** the school-level foundations from arithmetic through calculus intuition.
- **Depth bar:** the mathematics, probability and statistics expected at graduate entry in computer science: each theorem proved or its proof sketched, each formula derived, each method run by hand and then in code on real data.
- **Capstone:** a capacity and experiment report for a service you run: a queueing model predicting latency under load, a load test that confirms or refutes it, and an A/B analysis with power, intervals and a written conclusion, defended orally.

- [ ] Proof and discrete mathematics (31 lines) · MATH (just in time)
- [ ] Probability (28 lines) · MATH (just in time)
- [ ] Statistics and experimental design (17 lines) · MATH (just in time)
- [ ] Queueing and performance modelling (16 lines) · MATH (just in time)
- [ ] Linear algebra (9 lines)
- [ ] Calculus and optimization (18 lines)
- [ ] Numerical computing (7 lines) · MATH (floating point pulled forward)
- [ ] Information theory (6 lines)
- [ ] Signals and sequences (6 lines)
- [ ] Decision mathematics (2 lines)
- [ ] Exercises (19 lines)

### 7.4 Problem Solving, Reasoning & Research Method

9 groups, 66 topic lines.

- **Prerequisites (as written):** school algebra, geometry, functions and graphs, units, probability and sequences; proof techniques (direct proof, contradiction, cases, induction); counting; expected value and conditional probability; convex functions.
- **Depth bar:** contest-level problem solving and research-level reading: unseen problems solved under time and then by a second method; papers read critically and their claims tested.
- **Capstone:** a full-length timed contest paper scored and post-mortemed by error cause, and a short research report extending one published result to a new setting.

- [ ] Problem-solving strategy (11 lines)
- [ ] Contest mathematics toolkit (8 lines)
- [ ] Physical and quantitative intuition (7 lines)
- [ ] Speed and accuracy under time (5 lines)
- [ ] Proof craft and mathematical maturity (5 lines)
- [ ] Research method (7 lines)
- [ ] Systems thinking (5 lines)
- [ ] Learning science and deliberate practice (6 lines)
- [ ] Exercises (12 lines)

### 7.5 Programming Languages & Language Theory

13 groups, 356 topic lines.

- **Prerequisites (as written):** computer literacy and the terminal; data representation (binary, two's complement, UTF-8, floating point); proof by induction; sets, relations and functions.
- **Depth bar:** production fluency in Python and Go (idiomatic, tested, race-free, profiled code) together with a programming-languages course: semantics, type soundness, and a working interpreter and type checker.
- **Capstone:** a production-grade Go service with a command-line client, tests, benchmarks, profiling and graceful shutdown; and an interpreter with a type checker for a small language of your own design.

- [~] Python (21 lines) · in progress: core language and environment taught; runtime model started (reference counting, cycles, call by sharing); see 3.6 and 3.7 · index part 05
- [ ] Shell and working with APIs from code (10 lines) · PREREQ (cloud CLI: Bash, JSON, jq)
- [~] Go — toolchain and program structure (29 lines) · sliced: see 3.5 · GO
- [ ] Go — composite data, functions, errors and text (30 lines) · GO
- [ ] Go — memory, types with behaviour and generics (30 lines) · GO
- [ ] Go — the everyday standard library (23 lines) · GO
- [ ] Go — concurrency (35 lines) · GO
- [ ] Go — engineering (86 lines) · GO + MIDDLEWARE
- [ ] Go — cross-language contrasts (6 lines) · GO
- [ ] TypeScript, Node and the web client (11 lines)
- [ ] Wire formats (4 lines) · PREREQ (middleware: JSON, protobuf)
- [ ] Language theory (33 lines)
- [ ] Exercises (38 lines)

### 7.6 Data Structures, Algorithms & Computational Complexity

11 groups, 81 topic lines.

- **Prerequisites (as written):** a first programming language (Python, then Go); proof by induction and invariants; logarithms and exponents; sums and recurrences; probability with indicator variables and expectation; discrete maths (relations, graphs, counting).
- **Depth bar:** a top-university algorithms course: correctness proved by invariant, exchange argument or induction; recurrences solved; lower bounds and reductions shown; every implementation benchmarked against its predicted complexity.
- **Capstone:** a library of the core structures and algorithms with property-based tests and benchmarks confirming each asymptotic claim, and a timed set of unseen hard problems, each solved and proved.

- [ ] Analysis (13 lines) · PREREQ (SQL / design)
- [ ] Linear structures and techniques (6 lines)
- [ ] Hashing (5 lines) · PREREQ (SQL / design)
- [ ] Trees and heaps (8 lines) · PREREQ (SQL / design)
- [ ] Sorting, searching and strings (8 lines)
- [ ] Graph algorithms (8 lines)
- [ ] Greedy algorithms and dynamic programming (4 lines)
- [ ] Randomized and probabilistic structures (5 lines)
- [ ] Computability and complexity (6 lines)
- [ ] Algorithms at scale (4 lines)
- [ ] Exercises (14 lines)

### 7.7 Computer Networking & Web Protocols

12 groups, 99 topic lines.

- **Prerequisites (as written):** binary and powers of two; bit operations; queueing basics (delay grows with utilization); graph shortest paths (Dijkstra, Bellman–Ford); tries; the latency numbers of the memory and network hierarchy.
- **Depth bar:** a top-university networking course with its socket and protocol labs: each protocol mechanism traced on the wire with packet capture, each performance formula derived and checked under emulated loss and delay.
- **Capstone:** a service on Google Cloud reached through your own DNS records, TLS, reverse proxy and CDN, with its latency budget predicted, measured hop by hop, then broken and repaired under injected loss.

- [ ] Architecture principles (5 lines) · PREREQ (cloud / middleware)
- [ ] Addressing and the link layer (5 lines) · PREREQ (cloud / middleware)
- [ ] Routing (6 lines)
- [ ] Transport (23 lines) · PREREQ (cloud / middleware)
- [ ] DNS (7 lines) · PREREQ (cloud / middleware)
- [ ] HTTP and the web (14 lines) · PREREQ (cloud / middleware)
- [ ] TLS mechanics (2 lines) · PREREQ (cloud / middleware)
- [ ] Middleboxes, proxies and load balancing (14 lines) · PREREQ (cloud / middleware)
- [ ] Private connectivity (3 lines) · PREREQ (cloud / middleware)
- [ ] Data-centre networks (3 lines)
- [ ] Measurement (4 lines)
- [ ] Exercises (13 lines)

### 7.8 Operating Systems & Linux

9 groups, 70 topic lines.

- **Prerequisites (as written):** computer organization (ISA, the memory hierarchy, TLB, cache coherence and atomic instructions); a programming language with threads; data structures (queues, trees, hash tables); basic probability.
- **Depth bar:** a graduate operating-systems course with kernel labs: each mechanism explained down to its data structures and system calls, built at toy size, and observed on a live Linux system with tracing tools.
- **Capstone:** a minimal container runtime and a concurrent network server, each tuned from measurements (system-call traces, scheduler and memory counters, flame graphs), with every finding written as hypothesis, evidence and fix.

- [ ] Linux practice (8 lines) · PREREQ (cloud / Go / SQL)
- [ ] Processes and threads (7 lines) · PREREQ (cloud / Go / SQL)
- [ ] CPU scheduling (6 lines)
- [ ] Virtual memory (8 lines) · PREREQ (cloud / Go / SQL)
- [ ] Concurrency (10 lines) · PREREQ (cloud / Go / SQL)
- [ ] Persistence (7 lines)
- [ ] Isolation (4 lines) · PREREQ (cloud / Go / SQL)
- [ ] I/O models and performance (5 lines)
- [ ] Exercises (15 lines)

### 7.9 Software Architecture, APIs, Design Patterns & Clean Architecture

15 groups, 149 topic lines.

- **Prerequisites (as written):** a programming language with classes or interfaces (Python, Go); type systems (nominal and structural typing, parametric and subtype polymorphism); HTTP semantics; preconditions, postconditions and invariants; graphs and state machines.
- **Depth bar:** a graduate software-architecture and design course plus staff-level design review: every principle and pattern implemented, critiqued in real code and justified against quality-attribute scenarios.
- **Capstone:** a modular service designed from quality-attribute scenarios, documented with C4 views and decision records, built with ports and adapters and tests, then changed by a new requirement to measure how modifiable it really is.

- [ ] Architecture fundamentals (20 lines) · DESIGN
- [ ] API design (20 lines) · DESIGN
- [ ] Object-oriented foundations (5 lines) · DESIGN
- [ ] Design principles (13 lines) · DESIGN
- [ ] Design by contract and behavioural subtyping (3 lines) · DESIGN
- [ ] Gang of Four patterns (30 lines) · DESIGN
- [ ] Application architecture (7 lines) · DESIGN
- [ ] Domain-driven design (5 lines) · DESIGN
- [ ] Distributed application patterns (4 lines) · DESIGN
- [ ] Anti-patterns (7 lines) · DESIGN
- [ ] Quality attributes and evaluation (5 lines) · DESIGN
- [ ] Architecture documentation (5 lines) · DESIGN
- [ ] Formal methods (4 lines)
- [ ] Software testing at depth (5 lines)
- [ ] Exercises (16 lines)

### 7.10 Databases, SQL, Relational Theory & Data Modelling

12 groups, 153 topic lines.

- **Prerequisites (as written):** sets, relations, functions and bags; propositional and predicate logic; binary search, sorting, hashing and trees; the storage hierarchy with page and row arithmetic; integer versus floating-point arithmetic and encodings; files, CSV and JSON; a programming language with a database driver; operating-system virtual memory and fsync; concurrency (locks, deadlock).
- **Depth bar:** a top-university database-systems course with its internals labs plus production PostgreSQL practice: each theorem proved, each plan predicted before EXPLAIN, each operational procedure rehearsed.
- **Capstone:** a production schema for a transactional product taken from requirements through normalization, migrations, indexing and an isolation-anomaly test suite to backups with a timed restore, deployed on Cloud SQL with a connection budget.

- [~] Pre-SQL foundations (7 lines) · SQL · partly taught
- [ ] Relational theory (26 lines) · SQL
- [ ] The SQL language (15 lines) · SQL
- [ ] Storage and access methods (16 lines) · SQL
- [ ] Query processing (18 lines) · SQL
- [ ] Transactions and concurrency control (11 lines) · SQL
- [ ] Recovery and replication (11 lines) · SQL
- [ ] Data modelling and design (12 lines) · SQL
- [ ] Operating databases (8 lines) · SQL
- [ ] NoSQL and choosing a store (7 lines) · SQL
- [ ] Analytics and other engines (6 lines) · SQL
- [ ] Exercises (16 lines) · SQL (exercises)

### 7.11 Distributed Systems & Large-Scale System Design

14 groups, 98 topic lines.

- **Prerequisites (as written):** networking (TCP, DNS, load balancing, latency numbers); databases (transactions, isolation, replication, indexes); concurrency (locks, happens-before, memory models); probability (order statistics, balls into bins, the birthday bound); queueing (Little's law, utilization); partial orders; hashing and consistent hashing basics.
- **Depth bar:** a graduate distributed-systems course with replication and consensus labs plus staff-level system-design interviews: impossibility results proved, protocols implemented and tested under injected faults, designs sized with numbers.
- **Capstone:** a replicated, partitioned key-value store with consensus and a client library, tested under partitions, crashes and clock skew with a linearizability checker, and its design written up and defended with capacity numbers.

- [ ] Foundations (20 lines) · DESIGN
- [ ] Consensus and coordination (6 lines) · DESIGN
- [ ] Replication (7 lines) · DESIGN
- [ ] Availability (4 lines) · DESIGN
- [ ] Partitioning (5 lines) · DESIGN
- [ ] Distributed transactions (5 lines) · DESIGN
- [ ] Caching at scale (6 lines) · DESIGN
- [ ] Asynchronism and flow control (5 lines) · DESIGN
- [ ] Stream and batch processing (7 lines) · DESIGN
- [ ] Performance at scale (5 lines) · DESIGN
- [ ] Testing and verification (3 lines) · DESIGN
- [ ] System design method (4 lines) · DESIGN
- [ ] Design techniques (10 lines) · DESIGN
- [ ] Exercises (11 lines) · DESIGN (exercises)

### 7.12 Security, Cryptography, Privacy & Compliance

19 groups, 209 topic lines.

- **Prerequisites (as written):** number theory (modular arithmetic, Euler's theorem, discrete logarithms); probability (the birthday bound, negligible advantage); networking (HTTP, cookies, TLS, DNS, BGP); operating-system isolation (namespaces, cgroups, capabilities); databases (SQL, row-level security); distributed systems (consensus, replication); an HTTP service in a programming language.
- **Depth bar:** a top-university computer-security and applied-cryptography course with attack labs plus a cloud-security professional exam: every attack reproduced on your own fixtures, every defence explained by the property it restores, every primitive's security notion stated.
- **Capstone:** a threat-modelled application on Google Cloud with least-privilege IAM, managed secrets, perimeter controls, audit logging and detections, attacked by your own scripted tests and closed with an incident-response exercise and written report.

- [ ] Principles and economics (6 lines)
- [ ] Threat modelling (8 lines)
- [ ] Access-control models (6 lines) · PREREQ (cloud IAM / middleware)
- [ ] Cryptography (55 lines)
- [ ] Authentication and sessions (14 lines) · PREREQ (cloud IAM / middleware)
- [ ] Authorization flaws (5 lines)
- [ ] API abuse (8 lines) · PREREQ (cloud IAM / middleware)
- [ ] Denial of service (9 lines)
- [ ] Web application security (14 lines)
- [ ] Cloud-specific attacks (7 lines)
- [ ] Network security and zero trust (9 lines)
- [ ] Containers and Kubernetes security (6 lines)
- [ ] Supply chain (6 lines)
- [ ] Detection and incident response (6 lines)
- [ ] AI and LLM application threats (19 lines)
- [ ] Isolation classes (2 lines)
- [ ] Privacy (7 lines)
- [ ] Compliance (2 lines)
- [ ] Exercises (20 lines)

### 7.13 Software Delivery & Version Control

4 groups, 34 topic lines.

- **Prerequisites (as written):** the shell; hashing and Merkle structures; directed acyclic graphs and lowest common ancestors; queueing intuition (batch size and waiting time).
- **Depth bar:** Git understood as data structures, and delivery practised at the level of a team that owns its production releases.
- **Capstone:** a repository with branch protection, signed commits and CI, carrying one change through review, release, a failed rollout and a rollback.

- [ ] Git (18 lines) · PREREQ (Go modules, labs)
- [ ] Delivery models (5 lines)
- [ ] The profession (3 lines)
- [ ] Exercises (8 lines)

### 7.14 Cloud Computing Core: Virtualization, Well-Architected, Economics & IAM

6 groups, 48 topic lines.

- **Prerequisites (as written):** operating systems (virtual memory, page tables, the TLB, privileged instructions, namespaces and cgroups); probability (means and standard deviations of sums, the exponential distribution); availability arithmetic; access-control models; OAuth and OIDC tokens.
- **Depth bar:** cloud architecture at professional-certification depth together with the virtualization mechanisms beneath it: every service model explained down to the isolation it rests on, every cost claim computed.
- **Capstone:** a well-architected review of a workload you built: a pillar-by-pillar assessment, an IAM model with no basic roles, a cost model checked against the bill, and a remediation plan carried out.

- [ ] What cloud computing is (7 lines) · CLOUD
- [ ] Virtualization and containers (6 lines) · CLOUD
- [ ] Architecture patterns and well-architected frameworks (9 lines) · CLOUD
- [ ] Cloud economics and FinOps (8 lines) · CLOUD
- [ ] Cloud IAM concepts (9 lines) · CLOUD
- [ ] Exercises (9 lines) · CLOUD (exercises)

### 7.15 The Architect's Practice: Decisions, Strategy & Career

10 groups, 43 topic lines.

- **Prerequisites (as written):** architecture documentation (decision records, C4 views, quality-attribute scenarios); cost modelling; expected value and probability; delivery practices (canaries, feature flags, expand/contract migrations); SLOs and postmortems; technical reading and writing.
- **Depth bar:** staff and principal engineer practice: decisions written, reviewed and revisited against outcomes; strategy defended to engineers and to executives.
- **Capstone:** a technical strategy and migration plan for a realistic system, with decision records, a premortem, a build-or-buy analysis and a review held under adversarial questions.

- [ ] Making decisions (5 lines)
- [ ] Decision theory (6 lines)
- [ ] Build, buy, rent or adopt (4 lines)
- [ ] Evolutionary architecture and migration (3 lines)
- [ ] Sociotechnical architecture (3 lines)
- [ ] Strategy, writing and review (6 lines)
- [ ] Learning from failure (1 lines)
- [ ] Keeping current (2 lines)
- [ ] The road to the role (4 lines)
- [ ] Exercises (9 lines)

### 7.16 DevOps & SRE: Docker, Kubernetes, NGINX, CI/CD, Infrastructure as Code, Observability

8 groups, 109 topic lines.

- **Prerequisites (as written):** Linux (processes, namespaces, cgroups, capabilities, seccomp, file systems); networking (HTTP, TLS, load balancing, DNS); Git; Raft and replicated key-value stores; bin packing and DAGs; queueing (Little's law); percentiles and histograms; availability arithmetic.
- **Depth bar:** SRE practice at the level of owning an on-call service: every component deployed from your own manifests and pipelines, every alert tied to an SLO, every failure mode drilled.
- **Capstone:** a service on GKE or Cloud Run deployed by Terraform through a CI/CD pipeline with progressive delivery, SLOs with burn-rate alerts, dashboards and traces, and a game-day failure written up as a blameless postmortem.

- [ ] Docker (17 lines) · PREREQ (local Postgres)
- [ ] Kubernetes (24 lines)
- [ ] NGINX and API gateways (8 lines) · MIDDLEWARE
- [ ] CI/CD (11 lines)
- [ ] Infrastructure as code (14 lines)
- [ ] Observability (7 lines) · CLOUD (operations)
- [ ] Site reliability engineering (10 lines)
- [ ] Exercises (18 lines)

### 7.17 Machine Learning, MLOps & Production ML System Design

9 groups, 141 topic lines.

- **Prerequisites (as written):** sets and propositional logic; coordinate geometry and lines; linear algebra (vectors, matrices, transposes, determinants, cosine similarity, eigen-decomposition, PCA); multivariable calculus and the chain rule; convex optimization and gradient descent; probability (joint, marginal and conditional), Bayes' rule, distributions, maximum likelihood, hypothesis tests and sample size; information theory (entropy, cross-entropy, KL divergence); numerical stability (log-sum-exp, stable softmax); Python with NumPy, pandas and Matplotlib; SQL including window functions and as-of joins; graph search; queues and Little's law; cloud data services (warehouse, object storage, pub/sub).
- **Depth bar:** a graduate machine-learning course (losses, gradients and generalization derived) plus production ML system design: every model built from scratch at toy size before the library, every pipeline monitored.
- **Capstone:** an end-to-end ML system: the problem framed with its metric, point-in-time-correct features, a model evaluated with ablations, a served endpoint with drift monitoring, and an online experiment measuring its effect.

- [ ] Foundations of AI (3 lines)
- [ ] Classical machine learning (28 lines)
- [ ] Deep learning (11 lines)
- [ ] Natural language processing foundations (5 lines)
- [ ] Machine learning in Python (3 lines)
- [ ] Specialised learning areas (10 lines)
- [ ] Applied problem families (45 lines)
- [ ] MLOps (16 lines)
- [ ] Exercises (20 lines)

### 7.18 Generative AI, LLMs, Agents & Claude Applications

15 groups, 277 topic lines.

- **Prerequisites (as written):** probability (joint, marginal and conditional) and the chain rule of probability; cross-entropy, maximum likelihood and perplexity; linear algebra (matrix multiplication, transposes, projections) and cosine similarity; backpropagation, gradient descent and neural-network training; classical NLP, word embeddings and recurrent sequence models; ranking measures (recall@k, MRR, nDCG); binomial proportions, confidence intervals and paired tests; Python with NumPy and PyTorch, Go and TypeScript; HTTP, JSON Schema, JSON-RPC 2.0 and Server-Sent Events; OAuth 2.0 with PKCE; containers; queues, idempotency, retries with backoff, sagas and rate limiting; prompt-injection, jailbreak and AI-application threats; observability and SLOs.
- **Depth bar:** a graduate course on large language models (the transformer derived, training and inference costs computed) plus production LLM engineering: every application measured by an evaluation suite before and after each change.
- **Capstone:** an agentic retrieval application over your own documents with tools, guardrails, an evaluation suite gating regressions, cost and latency budgets and a red-team pass, deployed on Google Cloud.

- [ ] How LLMs work (38 lines)
- [ ] Fine-tuning and adaptation (8 lines)
- [ ] Multimodal models (4 lines)
- [ ] Embeddings and retrieval (24 lines)
- [ ] Retrieval-augmented generation (28 lines)
- [ ] Model APIs (24 lines)
- [ ] Prompt, context and output engineering (17 lines)
- [ ] Tools and the Model Context Protocol (5 lines)
- [ ] Agents and workflows (43 lines)
- [ ] Claude Code (6 lines)
- [ ] Security and safety of LLM applications (9 lines)
- [ ] Evaluation, testing and debugging (21 lines)
- [ ] Application architecture and LLMOps (18 lines)
- [ ] The forward-deployed engineer's craft (3 lines)
- [ ] Exercises (29 lines)

### 7.19 Cloud Providers: Google Cloud, AWS, Azure & Certifications

20 groups, 311 topic lines.

- **Prerequisites (as written):** cloud computing concepts (service and deployment models, shared responsibility, well-architected pillars, FinOps, IAM models); virtualization and containers; networking (VPCs, subnets, routing, BGP, DNS, TLS, load balancing, CDNs); databases (relational, key-value, wide-column, document, warehouse) and their consistency models; distributed systems (replication, sharding, queues, consensus); security (cryptography, identity, zero trust); DevOps (CI/CD, IaC, observability, SRE); Bash scripting, JSON and jq; machine learning and LLM applications.
- **Depth bar:** professional-certification depth on Google Cloud first, then on AWS and Azure by mapping each service and teaching what differs; every command is built by the learner.
- **Capstone:** one multi-tier production workload built on Google Cloud end to end from the command line and Terraform, then ported to AWS and Azure, with a written comparison of identity, networking, operations and cost.

- [ ] Google Cloud — compute (10 lines) · CLOUD
- [ ] Google Cloud — storage and databases (17 lines) · CLOUD
- [ ] Google Cloud — networking (15 lines) · CLOUD
- [ ] Google Cloud — data and analytics (8 lines) · CLOUD
- [ ] Google Cloud — AI and ML (8 lines) · CLOUD
- [ ] Google Cloud — security (13 lines) · CLOUD
- [ ] Google Cloud — operations, DevOps and cost (5 lines) · CLOUD
- [ ] Google Cloud — command line (82 lines) · CLOUD
- [ ] Google Cloud — mapping system-design components (9 lines) · CLOUD
- [ ] AWS (7 lines)
- [ ] AWS command line (23 lines)
- [ ] Azure (7 lines)
- [ ] Azure command line (19 lines)
- [ ] AWS and Azure — what differs at depth (8 lines)
- [ ] Cross-provider concept map (39 lines)
- [ ] Certifications — Google Cloud (12 lines)
- [ ] Certifications — AWS (6 lines)
- [ ] Certifications — Microsoft Azure (5 lines)
- [ ] Certifications — Anthropic (1 lines)
- [ ] Exercises (17 lines)

### 7.20 Published ML System-Design Case Studies

12 groups, 284 topic lines.

- **Prerequisites (as written):** the case-study method; leakage and point-in-time correctness; the applied problem families (recommendation, search and ads, forecasting, fraud, language, vision, speech, marketing, availability, ML platforms); evaluation metrics and online experiments; MLOps serving and monitoring.

- [ ] Recommend / personalize / feed (58 lines)
- [ ] Search / rank / ads (35 lines)
- [ ] Forecast / ETA / demand (23 lines)
- [ ] Fraud / trust & safety (21 lines)
- [ ] LLM / genAI apps (19 lines)
- [ ] NLP / text / support (7 lines)
- [ ] CV / video / OCR (6 lines)
- [ ] Speech / audio (3 lines)
- [ ] Marketing / churn / CLV / notify (14 lines)
- [ ] Availability / inventory (3 lines)
- [ ] ML platform / infra (2 lines)
- [ ] Other (pricing, classification, routing, dimensions and more) (93 lines)

## 8. Billing and credit queue

Everything that needs a billing account or trial credit is parked here. Finish the free and read-only parts first, then work through this section in one go, with the demanding labs lined up so the 3-month credit is used well. Billing and credit labs stay parked until the non-credit, non-trial, read-only sections are done.

### 8.1 Items carried over unchanged from the billing queue (created 3 Oct 2026)

#### Item 1. Billing account and the trial-clock question
- Status: not started. Blocks items 2 to 4 and every paid lab below.
- Verify first (console and Google's documentation): can a billing account be created without starting the trial; what the trial prompt says; where the credit balance and expiry are shown.

#### Item 2. Create a budget for real
- Where: console, Billing, Budgets & alerts (menu path to verify).
- Choose: scope (one project), a monthly amount you are comfortable with, thresholds (for example 50%, 90%, 100%), actual versus forecasted basis, who is notified.
- Reminder: a budget only notifies. It never stops spending.
- Practised in theory already: straight-line forecast = spend so far ÷ days elapsed × days in month (check: $5 in 10 days gives $15, which is 1.5× a $10 budget).
- Verify: whether trial credit counts toward a budget; how Google actually computes forecast alerts.

#### Item 3. Storage units lab: a Compute Engine disk
- Goal: see that the size you type is in binary GB (GiB), then convert it to bytes by hand.
- Steps: create one minimum-size disk in your own project (confirm the minimum size and disk type at the time); read the size back with a `describe` command you write; compute bytes = size × 2^30; compare with the same number × 10^9; delete the disk; confirm it is gone with a `list` command.
- Already taught: 100 × 2^30 = 107,374,182,400 bytes; a disk created at 500 holds about 536.87 decimal GB.
- Cost tag: credit, estimated at a fraction of a cent for minutes of a minimum-size disk (verify on the pricing page before creating).
- Not yet verified: how Cloud Storage and other products define GB.

#### Item 4. Latency numbers lab: ping and iperf3
- Goal: measure round-trip time and throughput between two small VMs in the same zone, then in different zones, and compare with the reference table.
- Reference figures taught (they drift, so verify when doing the lab): memory read about 100 ns; SSD random 4 KB read about 150 µs; same-data-centre round trip about 500 µs; HDD seek about 10 ms.
- Explain any gap between the measured numbers and the table in writing.
- Delete both VMs the same day and confirm with a `list` command.
- Cost tag: credit, estimate to confirm.

### 8.2 New items from the practical track (candidates; confirm each when its topic arrives)

Cost tags follow the index: free tier, credit with an estimate, plan only, paper, or local. Prefer local and plan-only versions first.

| Area | Lab | Cost tag | Notes |
|---|---|---|---|
| Cloud | Cloud Run deployment of the learner's own Go service (TLS terminated at the front end) | credit, estimate to confirm | Needs billing; first real deployment; set the budget first |
| Cloud | Compute Engine VM for NGINX / reverse-proxy experiments | credit, estimate to confirm | Local NGINX in Docker first (free) |
| Cloud | Global Application Load Balancer with Cloud CDN, Cloud Armor and IAP built resource by resource from the command line | credit; likely the costliest single lab | Strong candidate for the demanding-lab credit; tear down the same day |
| Cloud | Cloud Storage buckets, IAM roles, signed access | free tier or credit, to confirm | Confirm how GB is defined in its billing (open verification) |
| Cloud | Terraform plan-only versions of the above | plan only (free) | Do these before any apply |
| SQL | Cloud SQL (managed Postgres): create, connect with the Go connector and IAM database authentication, a read replica, a failover | credit; HA and replicas are costlier | Local Postgres in Docker comes first (free); this is the managed counterpart |
| SQL | Backup and point-in-time recovery on Cloud SQL | credit | After recovery and replication are taught |
| Design | One production service on Google Cloud as the systems capstone | credit | The cross-domain capstone for the systems domains; line up before using the credit |
| Middleware | Deploy the from-scratch gateway or proxy behind a managed load balancer for comparison | credit | Local first; compare with the managed equivalent |
| Go | Build and run on Cloud Shell or Cloud Build | free tier or credit, to confirm | Cloud Shell itself is free to use; confirm any build costs |

### 8.3 Run order, when ready

1. Resolve the open verifications (section 9).
2. Create the billing account only when the demanding labs are lined up (the trial clock may start).
3. Create the budget alert and confirm the Cloud Shell prompt shows the personal project.
4. Run the light labs (items 3 and 4, then the smaller new items), tearing everything down the same day.
5. Run the demanding labs together while the credit lasts.
6. Check the billing page the next day for stray charges.

## 9. Open verifications

- Trial and billing account relationship (can the account exist without starting the trial).
- Whether trial credit counts toward budgets; how Google computes forecast alerts.
- Minimum disk size and type for the Compute Engine lab; the unit definition for products other than Compute Engine.
- Exact console menu paths: Billing, Budgets & alerts; Compute Engine, Disks.
- What Cloud Shell provides for Go and Docker (versions, persistence of the home directory, any usage limits), before the Go and SQL stretches.
- Latency reference figures (drift over time) before the latency lab.
- Exam codes and domains for the AWS and Azure certifications before booking anything.

## 10. Resume point

**The open item right now (24 Oct 2026): the exercise for concepts 34 to 36.** The learner submitted `language-theory/exercise-36/memory.py` (on branch `gcp`): three `gc.collect()` calls and three printed lines, no `A` or `B` labels, and the first call printed although the task said to ignore it. Part A uses two independent lists; Part B builds a two-list cycle. The learner sent "6 / 0 / 2". The tutor ran the file: the second and third lines match (0 and 2); the first differed (the start-up call counts leftover objects and was never meant to be read).
- **Question already asked, not yet answered:** before running, what did the learner expect lines 2 and 3 to print, and the one reason for each? Do not state the expected values first.
- Then: review line by line; confirm what is right; sharpen the mechanism (independent objects are freed the moment their count reaches zero; only a cycle needs the collector; `gc.collect()` returns the number of unreachable objects it found); name the two deviations (labels, the first call printed). A miss gets one smaller, reworded retry, not a second exercise.
- Then close the sub-topic, add a short log line, and teach concept 37 as a read-only prediction.

**Paused or blocked (do not raise unless the learner asks or a prerequisite demands it):**
1. Alignment and padding (Data layout), and the rest of Computer Organization (Error detection, the remainder of Digital logic and Machine organization, exercises). Override 8.
2. Billing and credit labs (section 8). The Rust track waits behind the first Go groups.
3. Blocked on a prerequisite: `Decimal` and any float surprise need IEEE 754 (pull forward at `Decimal`); consistent hashing needs modular arithmetic; Go concurrency needs threads and locks; `net/http` needs TCP and HTTP.

**Yet to be taught, in index order (Python, part 05):**
1. Concept 37: floor division and modulo with negative operands (link to Go −9 / 4 and the digit-sum recursion on negative input; Money `__str__` with negative cents).
2. The GIL and the free-threaded build; `asyncio`.
3. Arbitrary-precision `int`; `str` versus `bytes`; `Decimal` (IEEE 754 first).
4. Late-binding closures; the mutable-default trap formalised.
5. pytest fixtures and assert rewriting (not yet taught).
6. Python for data and services: NumPy, pandas, Matplotlib, FastAPI.
7. Then Shell and working with APIs from code (part 05); the Go groups (part 06; recall the slice first); TypeScript, wire formats, language theory and the Programming exercises (part 07); then the rest of the index in order.

**Small loose ends:** the runner's `finally` message (error 18, `done <name>`); `__exit__` returning `True`; Money `__str__` with negative cents.

**Recalls due:** none scheduled formally. The retry queue in 4.8 holds the unseen variants to use.

**How to resume in a fresh session:** attach `gcp-lite/SESSION_HANDOFF_2026-10-24.md`, this file, and (or connect) `/Users/suhas/sde`; the Project "GCP Lite" holds the split index under `index/`. Start with: "/learn Resume the course. Read the handoff first, then the index map and progress file. Open only part 05. Review my `exercise-36/memory.py` (branch `gcp`). One check per turn. No ready-made code. Do not reveal answers." Replace this file with the updated copy when a sub-topic closes.

## 11. Log

- 3 Oct 2026: billing queue created. Items 1 to 4 pending.
- 6 Oct 2026: renamed to Pending Tracker and expanded into the full curriculum record: progress report, records, practical track, just-in-time prerequisites, all 20 sections and 229 groups, billing queue with new candidate labs, open verifications, resume point. Override recorded: pause Computer Organization at alignment and padding; practical track first; strict dependencies taught just in time. Teaching feedback recorded: more elaborate explanations; one self-test rule instead of repeated corrections.
- 6 Oct 2026 (later): practical track started at Go, toolchain and program structure. Learner ran the hello program in Cloud Shell, which shows Go is installed there (version not yet checked). Override 6 recorded: no pasteable code from the tutor.
- 6 Oct 2026 (later): learner corrected the plan: only Computer Organization was paused; the focus list was examples, not the whole scope; Python must come before Go. Override 2 withdrawn, override 7 added, section 3.5 records the Go slice taught so far, current plan set to Programming Languages from its first group (Python). Go: divisible-by-3 loop passed unaided.
- 8 Oct 2026: Python core language taught through recursion (section 3.6): variables and operators, control flow, functions, lists, dicts, tuples, sets, mutable defaults, recursion; Python 3.12.3 confirmed in Cloud Shell. A check on mutable defaults was weak evidence because the explanation preceded it; two unseen variants passed.
- 8 Oct 2026 (later): Python classes taught and recorded in section 3.6 (Rectangle, Counter, Tag, Bag); errors 10 and 11 logged; misconception register updated.
- 8 Oct 2026 (later): Bag mechanism confirmed; special methods (`__str__`, `__eq__`) taught; Money `__eq__` check passed on code. Handoff document generated.
- 8 Oct 2026 (resume): dedicated tracker file created in this chat from the handoff (Part B), with error 12 added (Money reason open), the cold-retry queue added as 4.8, and group counts added at the top of section 7. Session resumes with the Money reason check.
- 8 Oct 2026 (resume, later): Money reason closed (learner: default `==` compares the object's own identifier). Override 8 recorded: alignment and all paused Computer Organization items stay paused until the learner asks or a strict prerequisite requires them. Continuing Python classes with `__str__` practice.
- 9 Oct 2026: concept-13 finished (learner's numbering): `__str__` practice. Money `__str__` written unaided (f-string, `//` for dollars, `%` for leftover cents), output `12 dollars 34 cents`, correct. Not yet checked: negative cents (floor division gives a negative dollar count and a positive remainder). Learner asked for a sub-topic title for the concepts going forward: "Special methods, part 2: comparing objects across types" (concept-14 onward: `AttributeError` when `==` meets a non-Money, `isinstance`, `NotImplemented`, reflected comparison).
- 11 Oct 2026: Money default `==` explained (identity); concept-14 to 15 passed (`isinstance`, `NotImplemented`, the fallback, class attribute versus instance attribute with `is`). Overrides 10 (subagents; tracker scope) and 11 (number the concepts) recorded.
- 14 Oct 2026: concepts 16 to 19 (modules, import caching, the main guard, packages, `sys.path`, shadowing) passed; 14 to 17 Oct: concepts 20 to 24 (exceptions, which `except` matches, `finally`, `with`, tracebacks); `with` order missed first (error 14), traceback frame and line missed first (error 15).
- 22 Oct 2026: concepts 25 and 26 (virtual environments, pip freeze, pinning); the concept-26 check leaked its answer and was rewritten (override 12, errata). Concepts 27 to 29 (`assert`, clause order, test discovery); `test_c` misclassified (error 17).
- 22 to 23 Oct 2026: concept 30 (the learner built `runner.py`) and concept 31 (`finally` in the runner; message not as specified, error 18); concept 32 (pytest, `.FF.` verified) and concept 33 (`parametrize`; progress line cut short, error 19).
- 24 Oct 2026: the Exercise Rule written; the shop exercise (concepts 16 to 19) reviewed and passed; concepts 34 to 36 (reference counting, cycles, call by sharing); errors 20 to 22. The Exercise Rule revised (predictions and exercises never mixed). Exercise for 34 to 36 set; `memory.py` submitted, review open.
- 24 Oct 2026: the learner connected `/Users/suhas/sde` (device "macbookair-lan"); all Project files and the folder re-ingested after a compaction. The topic index was cut into 29 parts with an index map and a progress file (Project `index/`, repo `gcp-lite/index/`); the repo's pending changes were committed on `gcp` (`22a742b`) and `gcp-lite/` added on `master` (uncommitted). Session handoff and this refreshed tracker written.
