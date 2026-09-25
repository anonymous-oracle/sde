Authored text of the course guide (decision D18, 2026-09-25). r7_guide.py assembles COURSE-GUIDE.md from the "@@@ key"
sections below, the rules it moves out of the main course (rules 0.2, 0.4.1–0.4.10 and 0.5), and an outline it
generates from the six built parts. Text above the first key is not used.

@@@ head
# Course Guide — how to teach the Consolidated Cloud Mastery course

For the tutor. Read this file first, at the start of every session, before any course file. The course has six parts, one file each. The parts hold the material; this guide holds everything about *how* the course is taught and kept, and holds it once:

- §1 — how every session starts, and where to find things;
- §2 — the six course files: what each owns, its IDs, and where its keys are;
- §3 — the rules every part follows (rules 0.1–0.5). A reference to "rule 0.x" in any part means a rule in this section;
- §4 — how to manage the course files, so that nothing is taught or written twice;
- §5 — the outline of all six parts, generated from their headings.

The learner reads the parts. The tutor reads this guide as well.

@@@ s1
## 1. Start of every session

1. **Read this guide** (§1–§4). Use §5 to find a module without opening a whole part.
2. **Find the resume point.** Check, in this order: the resume point named at the last session's close (rule 0.4.8), which the learner may paste in; then the ticked `- [ ]` boxes in the parts; then the phase plan in the main course (§1 of the main course). If nothing is ticked and no ledger is given, the course is a fresh start and begins at A1.
3. **Anchor the session.** Open the main course at the module. In each companion's §2 stitch table, find the rows for that module. Those rows list the companion IDs that are taught in the same session (rule 0.1).
4. **Open only what is bound.** In each part, read its §0, then only the blocks for today's IDs. Search by ID (`SD-10`, `SL-06`, `GO-17`, `AU-03`). Never reload a whole part. Open keys, rubrics and reference solutions only after the learner has attempted the item.
5. **Teach** by the Suite Session Protocol (rule 0.4.2), within the contract (rule 0.4), the learner's preferences (rule 0.2) and Lab Safety (rule 0.5).
6. **Close** by rule 0.4.8: tick the boxes in every part, and emit the ledger delta and the exact resume point.

Where to find things:

| You need | Look in |
|---|---|
| What to teach next, and in what order | Main course §1 (the phase plan) and its Parts I–IV (Tracks A–D); Parts V–VII for the certification tracks |
| The companion IDs that ride with a main-course module | Each companion's §2 stitch table (the SQL companion also has §2.1, the engine-slice pairing, and §2.2, the parallel calendar) |
| Who teaches a shared concept, and who only adds to it | Rule 0.3 (the ownership register) |
| A module's check key, a problem key or a rubric | The keys section of the part that owns the item (§2 below) |
| Whether the learner may skip a block | The part's skip-tests (§2 below); rule 0.4.1 |
| The order inside a companion | The companion's dependency gate or prerequisite map (§2 below) |
| Which university course or textbook a pass follows | Main course §0.6 |
| Lab tags and what may be run | Rule 0.5 |

**The progress ledger** is the tutor's running record, kept beside the boxes (rule 0.1). The boxes remain authoritative. The ledger is not a file in the course folder: the learner removed that file on 2026-09-25. It is carried as the delta block emitted at each close (rule 0.4.8). The learner keeps it between sessions and gives it back at the start of the next one.

@@@ s2
## 2. The course files

All six files sit in this folder. The main course is the only parent (rule 0.1); every companion binds its modules to main-course IDs.

| File | Part | Owns | IDs | Keys, rubrics, skip-tests and order |
|---|---|---|---|---|
| `Curriculum.md` | The Consolidated Cloud Mastery Curriculum (the **main course**) | Order and phases, certification timing, Lab Reality, Tracks A–D (fundamentals, cloud core, the DevOps spine, ML/AI), the GCP, AWS and Azure certification parts, the cross-provider map, the university alignment table (§0.6) | `A1`…`A11`, `B1`…`B5`, `C1`…`C7`, `D1`…`D4`; academic blocks `A4.D6` and the like; problems `A4-P3`; Part V categories `V-COMP`…`V-OPS` | Appendix P (problem sets), Appendix K (keys); the phase plan in §1 |
| `system-design-primer-companion.md` | The System Design Primer Companion — GCP-Native Edition | The system-design layer: trade-offs, numbers, interview framing, GCP resources; the primer's problems; Terraform labs TF-1…TF-7; the primer's reference tables | `SD-nn`, `SX-nn`, `P01`–`P08`, `O01`–`O07`, `Q01`–`Q23`, `TF-n`, `SDA.n`, `SDA-Pn` | §4.1–§4.3 (prerequisites and readiness tiers), §4.5 (the ladder), §8.12 (academic keys) |
| `sql-databases-companion.md` | The SQL & Databases Companion — GCP-Native Edition | SQL, relational theory, the engine slices DB-1…DB-10, data design, operating databases (Cloud SQL), analytics engines, the lab kit and query ladder | `PQ-nn`, `RT-nn`, `SL-nn`, `CS-nn`, `DD-nn`, `OD-nn`, `AN-nn`, `DB-n`, `SQL-E…`, `SQL-Z0.n`, `TD-n`, `PX-n`, `TX-n`, `BH-n`, `DT-n`, `SCH-n`, `SQL-CAPn`, `TF-DBn`, `DBT.n`, `DBT-Pn` | §5 (skip tests and tiers), Appendix K (keys, including the academic keys); the lab kit in §3 computes the goldens |
| `design-patterns-companion.md` | Design Patterns, SOLID & Clean Architecture — A Companion Curriculum | OOP design theory, SOLID and GRASP, the 23 GoF patterns with a Go kata each, architecture styles and DDD, anti-patterns | `F-nn`, `PR-nn`, `DP-nn`, `ARCH-nn`, `AP-nn`, `DPE-nn`, `DPA.n`, `DPA-Pn` | §10 (dependency gate), §12 (skip-tests), Appendix K (keys, kata solutions, exercise and academic keys) |
| `cloud-cybersecurity-companion.md` | The Cloud Cybersecurity Companion | Attack mechanics and defences, applied cryptography, network and cloud security, detection and response, AI-application threats, privacy and compliance literacy | `PQ-S-nn`, `TH`, `CR`, `AU`, `AB`, `DOS`, `WA`, `CL`, `NT`, `CK`, `WL`, `IR`, `AI`, `SC`, `PV`, `CM` modules; `SEC-E…`, `CR-E…`, `SEC-Z0.n`, `SEC-CAPn`, `CRA.n`, `CRA-Pn` | §4 (skip tests and tiers), Appendix K (keys); Appendix U (university index) |
| `go-language-companion.md` | The Go Language Companion — Syntax, Semantics, Runtime and Contrasts | The implementation language (rule 0.4.9): Go's grammar, semantics, runtime and toolchain, contrasted with Python, Java, C and JavaScript; authentication and payment integration built in Go | `GO-nn`, `GO-Em.n`, `GO-Pnn`, `GO-CAPn`, `GOT.n`, `GOT-Pn` | §0.3 (the unlock list), §12 (dependency gate), §10.1 (keys), §10.2 (rubrics), §14.11 (academic keys) |

Within a part, a module card carries its own fields: `- [ ]` box, content, GCP lens, lab with its Lab Reality tag, and check. Each part's §0 names the fields that are particular to it.

@@@ r0.1
### 0.1 The course parts and the stitch rule

The course is one course in six parts (§2). The main course is the **only parent**. It owns order, certification timing and Lab Reality, and every companion binds its modules to the main course's IDs. A module ID from any part may be used as a stitch tag in any other part.

**The stitch rule.** Each companion's §2 lists what it binds to each main-course module. When a module is taught, every bound companion ID is taught in the same session, once, by its owner (rule 0.3), in the layer order of rule 0.4.2. It is one story, never a separate pass, and never taught twice. A companion ID with no main-course anchor is a defect: say so plainly (rule 0.2) rather than guess a mapping.

**Progress** lives in the inline `- [ ]` boxes of the six parts, which are authoritative. The tutor also keeps a **progress ledger**, a running record beside the boxes. It holds each ID's mastery state (rule 0.4.5), the misconception register, the errata list, the recorded overrides and wrong predictions, and the exact resume point (rule 0.4.8). §1 says where the ledger is kept.

@@@ r0.3
### 0.3 Suite overlap and ownership register

When two parts touch the same concept, the **owner** teaches it and the others only **add**. Later sessions recall it in one line. This is the only register; no part keeps its own copy. A concept that appears in two parts and is missing here is a defect: add its row here before teaching it (§4).

@@@ r0.4.11
**0.4.11 Conventions every part shares.**

1. **GCP lens, three depths.** Every concept gets its GCP lens the moment it is taught. **Lens-1** names the resource, says why it is the answer, and shows one `gcloud`, console or Terraform line; it is used throughout Phases 0–3. **Lens-2** touches it inside Lab Reality: free tier, a slice of the credit, a local emulator or fixture, or `terraform plan`. **Lens-3** designs with it at certification depth, with its trade-offs and limits, from Phase 4 on. Each part's §0 names its own Lens-2 default and Lens-3 exams.
2. **Bank ≠ dump.** An exercise bank is a bank of specifications, not a worksheet. Issue **one** item, at the rung the ledger says is next, and let the learner attempt it first. Escalate hints one notch at a time: *what structure do you see* → a smaller case → the smallest unlocked hint. Only then open the key. A mixed-transfer item names its two earlier tools on one line before it runs (rule 0.4.3).
3. **Inline tracking.** Tick the `- [ ]` box, or the learner says "done" in chat. No other tracker, log or research file is created; the ledger (rule 0.1) is the only record beside the boxes.
4. **Honesty flags.** `(verify)` marks a detail that changes often or was not confirmed when written; check it against live documentation before it is relied on for an exam or production. `(checked on …)` marks a behaviour that was run on that release. **Modern note** marks where industry has moved past the source. A part may add its own flags in its §0.
5. **Read economically.** Each session reads this guide, then each bound part's §0 and §2, then only the blocks bound to today's module (§1). Material is never copied from one file into another (§4).

@@@ s4
## 4. Managing the course files

These rules keep the six parts free of repeated material. They bind the tutor, and anyone else who edits the course.

1. **One home for everything.** A concept is taught in the part and module that owns it (rule 0.3). Any other part names it by ID and adds only its own layer, or recalls it in one line. Rules, the session protocol, the learner's preferences and Lab Safety live only in this guide; a part's §0 holds only what is particular to that part. The university and textbook alignment lives only in main course §0.6, with the cybersecurity companion's Appendix U as its security index.
2. **Refer; never copy.** A part refers to another part by the part's name and an ID or section: "the SQL companion's OD-11", "main course §0.6". It never repeats their text, and never names or links a course file (a lab's own files, such as the SQL lab kit's, are named where they are used). Only this guide names the course files (§2).
3. **Search before adding.** Before adding material, search all six parts for the concept, by name and by ID. If it is already taught, add to its owner or add a one-line recall; never write a second explanation. A new concept goes into the module that owns its subject, with a row in rule 0.3 if a second part touches it. Never create a new part, list or appendix to hold additions.
4. **What the tutor may change while teaching.** Tick `- [ ]` boxes. Everything else waits for the learner's instruction. An error found in a part is corrected openly in the next turn and logged in the ledger's errata list (rule 0.4.7); the fix to the file is made only when the learner asks for it.
5. **Every check and problem keeps its key with its owner.** The key has an expected answer and at least one expected wrong answer (rule 0.4.7), and sits in the owning part's keys section (§2). A new problem is numbered on from the end of its set, and the set's range line is updated with it.
6. **Honesty flags travel with the fact.** A new fact that was not checked carries `(verify)` (rule 0.4.11). A fact that was run carries the release it was run on.
7. **The files are built.** The six parts and this guide are generated by the build in the refactor workspace beside this folder (`../refactor`), from its frozen inputs, authored sources and journaled rules. An edit made only in this folder is overwritten by the next build, and so are ticked boxes. A lasting change to material is made in the workspace and rebuilt. After a rebuild, re-tick the boxes from the ledger. §5 of this guide is regenerated from the parts' headings, so it is never edited by hand.

@@@ s5
## 5. Course outline

Generated from the six parts' headings and module cards at build time. Each entry is a section of the named file, in teaching-document order. The order of *teaching* is the main course's phase plan (§1 of the main course) with each companion riding its bound modules (rule 0.1). A companion's own order is its dependency gate or prerequisite map (§2).
