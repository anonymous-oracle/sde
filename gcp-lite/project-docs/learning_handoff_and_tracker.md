# Learning Handoff and Pending Tracker (combined)

**Learner:** suhass149 · **Course:** the GCP Lite curriculum (index: `Consolidated_Topic_Index_GCP.md`, 3,749 lines, 20 sections, 229 topic groups, 2,805 topic lines) · **Tutor skill:** `learn-SKILL.md` (both are in the Project "GCP Lite") · **Generated:** Thursday 8 October 2026

This file has two parts.

- **Part A: Handoff.** Read this first. It says how to resume, the rules the tutor must follow, exactly where the course stands, and what to do next.
- **Part B: The full Pending Tracker.** The complete record (overrides, progress report, error log, misconceptions, errata, heuristics, the practical track, prerequisite register, all 229 groups, billing queue, open verifications, log). Part A summarises it; Part B is the detail and wins in a disagreement of detail.

---

# PART A. HANDOFF

## A1. How to resume in a fresh session

1. Open the Project "GCP Lite" (it holds the index and the `learn` skill) and make sure this file is in it, or attach this file to the chat.
2. Start with a message like this (copy and paste):

> /learn Resume the course. Read the handoff file first (Part A), then Part B section 2 (overrides), section 10 (resume point) and section 4.1 (error log). Do not re-teach anything marked taught. Continue Python classes where the handoff says, with one check per turn. Do not give me ready-made code to paste.

3. The tutor's chat memory does not persist. Everything the tutor needs is in this file. At the end of each session, ask for the updated file and replace this one.

## A2. The tutoring contract (binding, in the learner's words where possible)

| Rule | What it means in practice |
|---|---|
| One check per turn | Exactly one focused question. Never answered by the tutor in the same turn. The check must be answerable from what has been taught. |
| Diagnose through checks woven into the explanation | No separate probing round. |
| **Elaborate explanations** (said twice: "your explanations are not elaborate"; "I wasted 55 minutes on this concept") | Teach the mechanism step by step with a worked example before the check. After a check is missed twice, re-teach the whole idea once with a single self-test. |
| Correction format | Confirm what is right, then sharpen the mechanism. No false praise, no emoji. |
| Reworded, smaller check after a miss | Never the same check word for word. |
| **Top rungs use only taught material** | "How the hell would I know about mod arithmetic? Follow the curriculum order." |
| **No ready-made code to paste** (all coding, Python and Go) | "I need to learn to code in golang, do not give me ready snippets to simply paste and run." Describe the task in words. Show syntax only as a pattern with blanks. Never a runnable solution. Review the learner's own code line by line. |
| **Follow the index order** | The learner's list (cloud, systems design, maths, SQL, middleware, Go, "etc.") was examples, not the whole scope. "I only asked you to pause that, not pick from a few example topics I listed." |
| Python, then Go, then TypeScript | Standing order, back in force. |
| Reflection rung | Dropped for Page arithmetic only. Normal elsewhere unless the learner says otherwise. |
| Numbers carry units; recalled facts are tagged `(verify)` | |
| No time boxes | Progress is by passing checks. The learner is time-conscious: avoid detours, say when a topic is running long. |
| Billing and trial | Personal GCP account only for labs. The workplace account is browse-only (`list`, `describe`, `get-iam-policy`). The $300 trial credit (3-month expiry) is reserved for demanding labs; no billing account exists yet. The learner writes every cloud command; the tutor teaches grammar and the `--help` path. |
| Ten-rung ramp | anchor, vocabulary, representation, core move, worked illustration, then basic unseen check, routine variation, mixed transfer, top rung, reflection. |
| Mastery states and recall | taught, in progress, shaky, sliced, unverified. Recalls at about 1, 3, 7 and 21 sessions. |

## A3. How this learner works (patterns seen so far)

- Strong at: multi-step arithmetic, estimation, hand conversion, building a program from a task description, predicting short code outputs after a worked example.
- Characteristic misses (full list in B 4.1 and 4.2):
  - Dropping the rounding rule (floor/ceiling) in counting problems.
  - Reading a signed range as unsigned; off-by-one on counts (largest value taken as the count).
  - Importing the rules of one language into another (Python floor division applied to Go).
  - Padding-rule confusion (whose size decides the offset).
  - Python: thinking a method call triggers a class-attribute fallback (the lookup is of the *name*); describing a class-attribute change as a "broadcast".
- Loose vocabulary, corrected in place: "overloading" for "overlong", "fill rate" for "fill factor", "class objects" for "instances".
- Often answers with a result and no reasoning, and sometimes skips the requested one-sentence explanation. Ask for the reason as the whole check when it matters.
- Reacts badly to: terse explanations, unexplained jargon, material not yet taught, being handed code, long detours on one topic.
- Prefers: step-by-step reasoning with a worked parallel example, then trying it on their own.

## A4. Where the course stands

**Nothing has yet reached the mastery bar** (no academic pass, no from-scratch code exercise, no cold recall).

### Taught (engineering pass, L1 to L2)

| Area | What | Status |
|---|---|---|
| Computer Organization, Number systems | binary, hex, positional notation, base conversion, addition, overflow, two's complement, sign extension, bitwise ops, masks | taught; code exercises and academic pass pending |
| Computer Organization, Storage units | KB vs KiB, 1.024 gap compounding, powers of two by feel, estimation, GCP lens (Compute Engine disks are GiB) | taught; lab pending (billing queue) |
| Computer Organization, Character encoding | ASCII, Unicode, UTF-8 header bits, overlong, self-synchronization, mojibake | taught; from-scratch codec pending |
| Computer Organization, Data layout | endianness, network byte order taught. **Alignment and padding paused mid-topic** | in progress (open check below) |
| Computer Organization slices | Boolean logic, half adder, cache hit rate / average latency / speedup, latency numbers | sliced |
| Databases, Page arithmetic | 8 KiB pages, fill factor, rows per page (floor), pages (ceiling) | sliced |
| GCP, Cloud Shell | `gcloud` grammar, `--help`, `--filter`, `--format=json`, read-only verbs; budgets only notify; straight-line forecast | touched |
| Go (slice, out of order) | toolchain, packages vs modules, `go.mod`, `:=`/`var`, zero values, no implicit conversion, integer division truncates toward zero, `%` takes the dividend's sign, `for`/`if` | sliced; to be recalled when the Go groups are reached |
| **Python core language (current)** | interpreter/REPL; operators (`/`, `//`, `%`, `**`); indentation; truthiness; `range`; functions (params vs args, `return` vs `None`, scope, hints, defaults); lists, slicing (shallow copy); names, references, objects, `is` vs `==`; dicts (hash tables), tuples, sets; mutable default arguments; recursion (base case, frames, depth limit); **classes** (`__init__`, `self`, attributes, methods, shared references, `self.count += 1` as read-rebind, class vs instance attributes, lookup order instance then class, shadowing, mutable class attribute, the Bag fix); **special methods** (`__str__` default, `__eq__` default is identity) | in progress |

### Evidence by building (learner's own files, all reviewed line by line)

Go: two-line program; divisible-by-3 loop (1 to 20). Python: divisible-by-3 loop; divisibility function with zero guard; word counter; recursive digit sum; Rectangle; Counter; Tag; Bag fix; Money with `__eq__`.

### Open checks right now

1. **Money:** the learner's `__eq__` is correct (`self.cents == value.cents`) and the first output was reported as False, but the one-sentence reason was not given. The reason to elicit: the default `==` compares identity (it is the same test as `is`), and two separately built objects are different objects. Ask it as a short cold question.
2. **Alignment total size** (paused Data layout): for `u8 a; u16 b; u32 c; u8 d` the offsets are 0, 2, 4, 8 (learner got these). The total size under "round up to a multiple of the largest field" is still unanswered. Do not record the answer in advance.
3. Noted, not yet taught: `value.cents` fails with `AttributeError` when `==` compares a Money to a non-Money. This leads naturally into `isinstance` and returning `NotImplemented`.

### Cold-retry queue (error log items to re-test later, in new wording)

1. Page arithmetic: rows per page needs a floor.
2. Signed 32-bit counter overflow time (signed range, not unsigned).
3. Count of 8-bit values where x + x overflows (method: plug candidates back into the condition).
4. UTF-8 count of valid 2-byte sequences (count = largest − smallest + 1).
5. Little-endian: which byte sits at the lowest address.
6. Alignment: whose size decides the padding; the total-size rule.
7. Go: −9 / 4 truncates toward zero; `%` follows the dividend; contrast with Python `//` and `%`.
8. Python: mutable default argument (unseen variants).
9. Python: Tag prediction (class attribute changed after `__init__` copied it).
10. Python: Bag (`append` runs on whatever the name `items` resolved to).
11. Python: why default `==` gave False (Money).

## A5. What to do next (in this order)

1. Close the two open checks above (Money reason; alignment total size). Each is one short question, not a re-teach.
2. Finish Python classes: `__str__` practice (the learner writes one), comparing against other types (`isinstance`, `NotImplemented`), then a short mixed check on class vs instance attributes and `==` vs `is`.
3. Python, index order, remaining: modules, packages and imports; exceptions, `try`/`finally`, context managers, reading a traceback; Environment and tooling (virtual environments, pip, lock files, a hand-built test runner, pytest); Python runtime model (call by sharing, reference counting and the cycle collector, the GIL and free-threaded build, `asyncio`, big integers, `str` vs `bytes`, `Decimal`, late-binding closures, the mutable-default trap formalised); Python for data and services (NumPy, pandas, Matplotlib, FastAPI).
4. Then, in index order within Programming Languages & Language Theory: Shell and working with APIs from code; the Go groups (recall the slice first, not a restart); TypeScript, Node and the web client; Wire formats; Language theory; Exercises.
5. Then the rest of the index in order. Where a strict dependency appears, teach the prerequisite at that moment (register in B section 6): floating point (IEEE 754) is first, at the first surprising float result and at `Decimal`; also modular arithmetic, concurrency basics, TCP/HTTP.
6. Return to the paused Computer Organization (Data layout, then Error detection, the rest of Digital logic and Machine organization) when the learner says, or in index order.
7. Billing and credit labs stay parked until the non-credit, non-trial, read-only sections are done. Then run the queue (B section 8) in one go.

## A6. Pending, at a glance

Group-level counts from the section-by-section tracker (B section 7). A group marked "in progress / partly" may contain taught topics; counts below are groups, not topic lines. The 2,805 topic lines are all listed in the index.

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

**Taught at topic level:** Number systems, Storage units, Character encoding (3 topics, 12 topic lines, about 0.4% of the lines). Partly taught: Data layout, Boolean logic, Combinational circuits, The memory hierarchy, Latency numbers, Page arithmetic, Python (in progress), Go (a slice).

**Not started (everything else):** all of School-level foundations (the formal walk and exit audit were never done; items were used as tools), Mathematics, Problem solving, Data structures and algorithms, Networking, Operating systems, Software architecture, most of Databases/SQL, Distributed systems, Security, Software delivery, Cloud core, Architect's practice, DevOps/SRE, Machine learning, Generative AI, Cloud providers (GCP/AWS/Azure and certifications), and the ML case studies. The exact group names for each are in B section 7.

## A7. Waiting on billing (parked; details in B section 8)

1. Billing account and trial-clock question (can an account exist without starting the $300 trial?).
2. A real budget (the walk-through is done; the budget itself is not created).
3. Storage units disk lab (Compute Engine disks, GiB).
4. Latency numbers lab (two VMs, ping/iperf3, same-zone vs cross-zone vs cross-region).
5. Candidate new labs, to confirm when each topic arrives (B 8.2).
6. Open verifications (B section 9), including AWS and Azure exam codes.

## A8. Study aids and where they are

| Item | Location |
|---|---|
| Curriculum map with Playground (mind map, interactive tools) | https://claude.ai/artifact/9ukLuALUU1S9EYsX9qX9hn |
| Index (the source of truth for order) | Project "GCP Lite": `Consolidated_Topic_Index_GCP.md` |
| Tutor skill | Project "GCP Lite": `learn-SKILL.md` (the `/learn` command) |
| This file | Project "GCP Lite" (if saved) and the downloaded copy |
| Learner code files (Go and Python) | The learner's own machine and Cloud Shell; the tutor only sees what is uploaded |

## A9. Tutor errata to avoid repeating (full list in B 4.3)

- Do not state an answer in the same turn that asks the check (it happened at least twice).
- One question per check (several checks held two).
- Do not use a concept in a top rung before it is taught (modular congruence).
- Do not substitute the learner's example list for the scope.
- Do not paste a runnable program (the Go hello-world was pasted once before the rule).
- Do not blur whose size decides padding; state it in one sentence and give the byte-by-byte example.
- A mutable-default check that follows its own explanation is weak evidence; use unseen variants.

---

# PART B. THE FULL PENDING TRACKER

(Verbatim copy of `pending_tracker.md` as of 8 October 2026. Section numbers below refer to this part.)

---

# Pending Tracker

Renamed from `billing_pending_queue.md` and expanded on 6 October 2026. Created 3 October 2026.

This is the learner's full curriculum record: what has been taught, what is in progress, what is pending, what is waiting on billing, and the dependencies to teach just in time. It replaces the billing-only queue; the billing queue is kept intact as section 8.

**How to carry this file between sessions:** the tutor's chat memory does not persist and the tutor cannot write to the project folder. At the start of every session, upload this file (or add it to the project) so the tutor can read it, and re-upload the updated copy at the end. The curriculum index (`Consolidated_Topic_Index_GCP.md`) must be uploaded alongside it.

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

- The index holds 20 sections (19 domains plus the ML case-study appendix), 229 topic groups and 2,805 topic lines.
- Marked taught: 3 topics, 12 topic lines (Number systems, Storage units, Character encoding), all at L1 and L2 (intuition and undergraduate core), engineering pass only. About 0.4% of the lines.
- In progress: Data layout (endianness and network byte order taught; alignment and padding paused mid-topic).
- Partly taught (named slices): Boolean logic, Combinational circuits, The memory hierarchy, Latency numbers (all in Computer Organization); Page arithmetic (in Databases, Pre-SQL foundations).
- Nothing has reached the mastery bar yet. No topic has an academic pass, a from-scratch code exercise, or a cold recall result.
- Parked in the billing queue: billing account, a real budget, the Storage units disk lab, the Latency numbers two-VM lab.
- Study so far: 46 numbered teaching parts plus checks, one hands-on session in Cloud Shell (read-only commands in the personal project).
- Programming Languages & Language Theory (started 6 Oct 2026, index order): a Go slice taught out of order (section 3.5, to be recalled when the Go groups are reached); Python core language in progress (section 3.6): variables to recursion, then classes, class versus instance attributes, special methods `__str__` and `__eq__`. Python 3.12.3 confirmed in Cloud Shell.
- Last refreshed 8 Oct 2026 (handoff generated).

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

### Standing rules and preferences (from the index method and this chat)

- Personal account only. The workplace account is browse-only: `list`, `describe`, `get-iam-policy` and other read-only commands.
- The $300 trial credit (3-month expiry) is reserved for demanding labs. Do not start it for light labs.
- No billing account exists. Creating one may prompt the trial; whether it can be created without starting the trial clock is open (section 8, item 1).
- Before anything paid is created: a budget alert exists, and the project shown in the Cloud Shell prompt is the personal one.
- Paid resources for a lab are deleted the same day, and the deletion is confirmed with a read-only command.
- The learner writes every cloud command. The tutor teaches the grammar (product, resource group, verb, name, flags) and the `--help` path only.
- Checks: one thing at a time; answerable from what was taught; never answered by the tutor in the same turn; a missed check is reworded and made smaller, never repeated word for word.
- Numbers always carry units. Recalled figures are flagged `(verify)` until checked in a primary source.
- No time boxes: progress is by passing checks. The learner is time-conscious, so avoid detours and say so when a topic is running long.
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
- A curriculum map (published page) and a Playground of six tools exist as study aids. They are not evidence of mastery.

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

### 3.6 Programming Languages & Language Theory: Python, core language (in progress, taught in index order from 6 Oct 2026)

**Python** · `[~]` in progress · setup: Python 3.12.3 in Cloud Shell (`python3` and `python` both work there)
- Taught and passed unaided: how Python runs (interpreter, file versus REPL); names, values and types; `/`, `//`, `%`, `**` (floor division, remainder takes the divisor's sign; cross-checked against Go: −9 % 4 is 3 in Python, −1 in Go); `if`/`elif`/`else`, `for`, `while`, `range` (end-exclusive), truthiness; functions (parameters versus arguments, `return` versus `None`, local scope, type hints and defaults as labels); lists (indexing, negative indices, slicing); dicts as hash tables (lookup, `get`, `in`, insertion order, hashable keys); tuples and sets (unpacking, `|`, `&`, `-`, `^`); recursion (base case, frames, call stack, depth limit; digit-sum built unaided).
- Taught with a hint or weak evidence: references, shallow copy and the nested-list prediction (passed unaided); mutable default arguments (first answer correct but weak because the explanation came just before; rebinding versus mutation re-taught; two unseen variants then passed).
- Evidence by building: divisible-by-3 loop (1 to 21), divisibility function, word counter, recursive digit sum.
- Classes (8 Oct): `__init__`, `self`, attributes, methods; objects shared through references (`b = a`); `self.count += 1` as read then rebind; class versus instance attributes, lookup order (instance, then class), shadowing by assignment through an instance; a mutable class attribute mutated through `n.items.append(1)`. Evidence: Rectangle and Counter predictions correct unaided; Tag prediction wrong first (said `m.prefix` is "x" after `Tag.prefix = "y"`, because `__init__` copied the value into the instance; then explained with a "broadcast" picture); Bag predicted correctly but reasoned that `append` triggers the class fallback (wrong: the lookup is of the name `items`); Bag fix (`self.items = []` in `__init__`) written correctly, without output or a prose explanation of the change. Bag mechanism restated in own words: instance attribute looked up first, then `append` on it (correct for the found case; the not-found fall-through to the class was supplied by the tutor). Special methods taught (`__str__` default repr, `__eq__` default is identity). Money check: `__eq__` written correctly (`self.cents == value.cents`), first output reported False, but the one-sentence reason (default `==` is identity) was not stated, and the file shows only the final version. Noted: `value.cents` raises `AttributeError` when compared to a non-Money object; not yet taught.
- Noted in review: an input that is negative never reaches `num // 10 == 0` in the digit sum, because floor division moves away from zero, so it would recurse forever. The task said non-negative; the point links back to floor versus truncation.
- Pending in this group, in index order: special methods and the rest of classes (`__str__`, `__eq__`); modules, packages and imports; exceptions, `try`/`finally`, context managers, reading a traceback; then Environment and tooling (virtual environments, pip, lock files, a hand-built test runner, pytest); Python runtime model (call by sharing, reference counting and the cycle collector, the GIL and free-threaded build, `asyncio`, arbitrary-precision `int`, `str` versus `bytes`, `Decimal`, late-binding closures); Python for data and services (NumPy, pandas, Matplotlib, FastAPI).
- Dependency noted, not yet reached: floating point (IEEE 754) at the first surprising float result and at `Decimal`.

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
| 9 | Terminology | "Overloading" for "overlong"; "fill rate" for "fill factor"; "GiB is lower" for "fewer GiB for the same bytes" | Loose vocabulary | Corrected in place |
| 10 | Python classes, Tag | Predicted `m.prefix` is "x" after `Tag.prefix = "y"` where `__init__` set `self.prefix` | Missed that `__init__` copies the value into the instance, so the later class change is not seen | Corrected; later described as a broadcast (wording imprecise) |
| 11 | Python classes, Bag | Said `append` triggers the fallback to the class attribute | Confused the lookup of a name with the method call on the result | Corrected; fix written; retry due |

### 4.2 Misconception register

- Pad every struct field to the largest field's size. **Open, repeated three times.**
- `append` (a method call) makes Python fall back to the class attribute. Actual: the name `items` is looked up (instance, then class) and `append` then runs on whatever object that lookup returned. **Open; fix written correctly, mechanism not yet stated in the learner's words.**
- Class attribute changes "broadcast" to all instances. Actual: only instances that have no own attribute of that name see the change. Corrected.
- The largest value of a range is its count (off by one). Corrected; watch in any counting problem.
- Integer division floors (Go truncates toward zero; Python floors). Corrected; check again when Python's `//` is taught.
- A GiB is "lower" than a GB. A GiB is larger, so the same bytes give a smaller GiB count. Corrected.
- The little-endian reader begins from the most significant end. Corrected.

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

### 4.4 Predictions (predict, run, explain the gap)

- GiB count lower than 500 for a decimal 500 GB disk: right.
- Which cache improvement lowers average latency more (higher hit rate beats a faster cache): right.
- Little-endian value for network bytes 0A 00 00 01: wrong at first, right after a smaller step.
- No Brier-scored decision journal yet.

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

## 6. Just-in-time prerequisite register

When the left-hand topic starts, teach the right-hand prerequisite first (at the depth needed, then resume). Items marked "taught" need only a short recall.

| When this arrives | Teach first | Source and status |
|---|---|---|
| Go numeric types; any float in SQL or JSON | Floating point (IEEE 754: sign, exponent, mantissa; rounding) | Mathematics, Numerical computing; also a stated prerequisite of Programming Languages and Databases. **Not taught; pull forward.** |
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

- [~] Python (21 lines) · in progress: see 3.6
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

Everything that needs a billing account or trial credit is parked here. Finish the free and read-only parts first, then work through this section in one go, with the demanding labs lined up so the 3-month credit is used well.

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

**Paused here:** Computer Organization & Data Representation, Data layout, Alignment and padding. One open check: the total size, under the round-up rule, of `u8 a; u16 b; u32 c; u8 d` (offsets already correct: 0, 2, 4, 8).

**Also in progress (since 6 Oct 2026, updated 8 Oct):** Programming Languages & Language Theory, Python, core language. Classes taught (8 Oct) through class versus instance attributes and the Bag fix. Next: the Money reason (default `==` is identity) as a quick cold check, `__str__` practice, comparing against other types, then modules, packages and imports, then exceptions.

**Next session starts with:**
1. Upload this file and the curriculum index.
2. Continue Python, core language, in order. Setup: Python in Cloud Shell (version not yet checked).
3. Check the setup for later sections when reached (Docker, Go version).

**Recalls due:** none scheduled until sessions pass. The first round (1 session later) covers: binary to hex, the XOR rule, storage unit gap, UTF-8 header bits, rows per page.

## 11. Log

- 3 Oct 2026: billing queue created. Items 1 to 4 pending.
- 6 Oct 2026: renamed to Pending Tracker and expanded into the full curriculum record: progress report, records, practical track, just-in-time prerequisites, all 20 sections and 229 groups, billing queue with new candidate labs, open verifications, resume point. Override recorded: pause Computer Organization at alignment and padding; practical track first; strict dependencies taught just in time. Teaching feedback recorded: more elaborate explanations; one self-test rule instead of repeated corrections.
- 6 Oct 2026 (later): practical track started at Go, toolchain and program structure. Learner ran the hello program in Cloud Shell, which shows Go is installed there (version not yet checked). Override 6 recorded: no pasteable code from the tutor.
- 6 Oct 2026 (later): learner corrected the plan: only Computer Organization was paused; the focus list was examples, not the whole scope; Python must come before Go. Override 2 withdrawn, override 7 added, section 3.5 records the Go slice taught so far, current plan set to Programming Languages from its first group (Python). Go: divisible-by-3 loop passed unaided.
- 8 Oct 2026: Python core language taught through recursion (section 3.6): variables and operators, control flow, functions, lists, dicts, tuples, sets, mutable defaults, recursion; Python 3.12.3 confirmed in Cloud Shell. A check on mutable defaults was weak evidence because the explanation preceded it; two unseen variants passed.
- 8 Oct 2026 (later): Python classes taught and recorded in section 3.6 (Rectangle, Counter, Tag, Bag); errors 10 and 11 logged; misconception register updated.
- 8 Oct 2026 (later): Bag mechanism confirmed; special methods (`__str__`, `__eq__`) taught; Money `__eq__` check passed on code. Handoff document generated.
