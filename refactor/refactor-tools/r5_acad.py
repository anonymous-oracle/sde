"""R5 Academic depth (learner decision D17, 2026-09-24).

D17: the learner asked that the main course and its five companions become "a full practical cloud+system
architecture design course with all undergraduate pre-requisites taught in academic depth and thoroughness".
D17 supersedes the part of D16 that left the declined tracks' rigorous passes in records only: the rigour now lives
inside the existing modules, as each module's academic pass (its "D" teaching blocks, rule 0.4.10). No Track M, U or
S returns and no new module ID is created (D16 stands for that). Nothing is taken from the legacy GCP notes (D16).

The text is authored in authored/academic/<part>.md, split into "@@@ <key>" sections, and applied here through
journaled edits only: every insertion is in the journal, and every replaced line goes to records/ (D3).
"""
import os
import re

from r2b_common import CUR, PRI, SQL, SEC, DPC, RECORDS

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "authored", "academic")
EV = ("D17 (2026-09-24): the learner asked for \"a full practical cloud+system architecture design course with all "
      "undergraduate pre-requisites taught in academic depth and thoroughness\"; the academic pass is taught inside "
      "the existing module (rule 0.4.10), from named textbooks and university courses checked by web search that day.")
MODULES = {"A1": "A1. ", "A2": "A2. ", "A3": "A3. ", "A4": "A4. ", "A5": "A5. ", "A6": "A6. ", "A7": "A7. ",
           "A8": "A8. ", "A9": "A9. ", "A10": "A10. ", "A11": "A11. ", "B2": "B2. ", "B3": "B3. ", "B4": "B4. ",
           "B5": "B5. ", "C2": "C2. ", "C6": "C6. ", "C7": "C7. ", "D1": "D1. ", "D2": "D2. "}


def fragments(name):
    """{key: [lines]} from authored/academic/<name>.md; each section is stripped of blank edge lines"""
    out, key = {}, None
    for l in open(os.path.join(SRC, name), encoding="utf-8").read().split("\n"):
        m = re.match(r"^@@@ (\S+)$", l)
        if m:
            key = m.group(1)
            if key in out:
                raise SystemExit(f"r5_acad: duplicate fragment {key} in {name}")
            out[key] = []
        elif key:
            out[key].append(l)
    for k, v in out.items():
        while v and not v[0].strip():
            v.pop(0)
        while v and not v[-1].strip():
            v.pop()
    return out


def cur_contract(f):
    """rule 0.4.10 joins §0.4 before the companions copy the contract, so every part carries it"""
    fr = fragments("main-course.md")
    f.ins("R5-1", f.heading("0.5 Lab Safety"), fr["rule-0.4.10"] + [""], EV)


def cur(f):
    fr = fragments("main-course.md")
    f.ins("R5-2", f.heading("1. The Phase Plan"), fr["s0.6"] + [""], EV + " §0.6 is the university and textbook "
          "alignment table the §0.3 papers row already promised.")
    f.rep("R5-2", "anchor-rewrite", "A9 deepening and the university alignment appendix cite the same papers",
          "A9's academic pass (A9.D) and the university and textbook alignment table (§0.6) cite the same papers",
          EV + " The row named an appendix that did not exist; it now names the table that does.")
    f.ins_after("R5-3", "> **Note:** First-pass scope: this intuition pass is the first pass and is complete as "
                "written.", fr["A2-note"], EV)
    f.ins_after("R5-3", "> **Note:** First-pass scope: A4 stays at engineering-practical depth.", fr["A4-note"], EV)
    for key, head in MODULES.items():
        f.ins_section_end("R5-4", head, fr[key], EV + f" The academic pass of {key}.")
    f.ins("R5-5", len(f.L), [""] + fr["appendix-P"] + [""] + fr["appendix-K"], EV + " The problem sets and their "
          "keys (rule 0.4.7: an expected answer and at least one expected wrong answer each).")


def pri(f):
    fr = fragments("primer.md")
    f.ins("R5-6", len(f.L), [""] + fr["section"], EV + " The primer's academic pass: the mathematics under the SD "
          "cards (queueing, tails, hashing, load balancing, caching, quorums, CAP).")


def pri_c40(f):
    fr = fragments("primer.md")
    ev = ("C-40: the primer's GCP details came from a January 2026 knowledge cutoff; the volatile ones were checked by "
          "web search on 2026-09-24 and the results are dated in place. Every `verify` flag is kept (invariant 7).")
    f.ins_after("R5-15", "- **GCP mappings come from my own knowledge (cutoff January 2026)", fr["c40-note"], ev)
    f.ins_after("R5-15", "- **GCP lens:** **Memorystore** (Redis, Redis Cluster, Memcached, Valkey", fr["c40-memcached"], ev)


def sql(f):
    fr, fk = fragments("sql.md"), fragments("sql-keys.md")
    f.ins("R5-7", f.heading("Appendix K"), fr["section"] + [""], EV + " The SQL companion's academic pass: the "
          "proof layer of its RT and CS cards (main course A8.D1).")
    f.ins("R5-7", f.heading("Appendix V"), fk["keys"] + [""], EV + " Keys for DBT-P1…DBT-P14 (rule 0.4.7).")
    ev = ("C-56 and C-NEW-02: the goldens' pins (seed v1, PostgreSQL 15.x, UTC, C collation) were stated only in prose; "
          "run_ex.py now asserts them, and the kit was re-verified in place from the course text (goldens unchanged).")
    f.ins("R5-14", f.idx("    return p.returncode, p.stdout, p.stderr") + 1, fr["run-ex-pins"], ev)
    f.ins("R5-14", f.idx('    mods = sys.argv[1].split(",")'), fr["run-ex-call"], ev)
    f.ins("R5-14", f.heading("3.2 Bring-up") , fr["s3.1-note"] + [""], ev)
    f.ins_after("R5-14", "4. Smoke: `SELECT lab.chk('SELECT 1');`", fr["s3.2-note"], ev)


def sec(f):
    fr = fragments("cyber.md")
    f.ins_after("R5-8", "| Berkeley CS161 | CR foundations, NT, DOS, WA, AU |", fr["align-row"], EV + " §0.5 names "
                "the courses the academic pass is aligned with.")
    f.ins_after("R5-8", "| CMU 95-746 |", fr["u-row"], EV)
    f.ins("R5-8", f.heading("Appendix K"), fr["section"] + [""], EV + " The Cloud Cybersecurity companion's academic "
          "pass: cryptography with definitions and proofs (main course A10.D3).")
    f.ins("R5-8", f.heading("Appendix N"), fr["keys"] + [""], EV + " Keys for CRA-P1…CRA-P10 (rule 0.4.7).")


def gof(f):
    fr = fragments("go.md")
    RECORDS.setdefault(f.n, [])
    f.ins("R5-9", len(f.L), [""] + fr["section"], EV + " The Go Language Companion's academic pass: the language's "
          "specification, type system, CSP, memory model, scheduler and garbage collector; every quoted output was "
          "run on Go 1.27.1 offline.")


def by_id(lines):
    """{"DP-01": "text", …} from "ID: text" lines"""
    out = {}
    for l in lines:
        k, t = l.split(": ", 1)
        out[k] = t
    return out


def kata(n, name):
    """the text of katas/dpNN/<name>, checked on Go 1.27.1 offline (gofmt, go vet, go test, go test -race)"""
    return open(os.path.join(SRC, "katas", f"dp{n:02d}", name), encoding="utf-8").read().rstrip("\n").split("\n")


def dp(f):
    fr = fragments("patterns.md")
    named, lens, tasks = by_id(fr["named"]), by_id(fr["lens"]), by_id(fr["kata-tasks"])
    names = {}
    for n in range(1, 24):
        k = f"DP-{n:02d}"
        h = f.idx(f"**{k} · ")
        names[k] = re.match(r"^\*\*DP-\d\d · (.+?) \[", f.L[h]).group(1)
        e = next(i for i in range(h, len(f.L)) if f.L[i].startswith("- **Real-world example:**"))
        f.ins("R5-10", e + 1, [f"- **Named real examples:** {named[k]}", f"- **GCP lens:** {lens[k]}"],
              EV + " C-59: every pattern names real systems that use it and its Google Cloud form.")
    for k, t in by_id(fr["arch-checks"]).items():
        h = f.idx(f"**{k} · ")
        e = h
        while f.L[e].strip():
            e += 1
        f.ins("R5-11", e, [f"- **Check:** {t}"], EV + f" C-61: {k} had no check of its own.")
    for fam in ("grasp-checks", "ap-checks"):
        for k, t in by_id(fr[fam]).items():
            name = re.escape(k)
            f.ins_after("R5-11", rf"^- \*\*{name} [^*]+:\*\*", [f"  - **Check:** {t}"], EV + f" C-61: {k} had "
                        "no check of its own; the section's shared check becomes its integration check.", regex=True)
    for old in ("**Check:** a `PaymentValidator`", "**Check:** a `UserManager`"):
        f.rep("R5-11", "relabel", old, old.replace("**Check:**", "**Integration check:**"), EV + " C-61: the "
              "shared check now follows one check per item, so it is labelled as the section's integration check.")
    f.ins_after("R5-12", "7. AP-01…10 — taught last", fr["gate-line"], EV + " The gate places the academic "
                "additions (§12–§15).")
    out = ["", "---", ""] + fr["sections"] + [""]
    for n in range(1, 24):
        k = f"DP-{n:02d}"
        out += [f"### 13.{n} Kata for {k} · {names[k]}", "", f"**Task.** {tasks[k]}", "",
                "Given test:", "", "```go"] + kata(n, "kata_test.go") + ["```", ""]
    out += fr["s14"] + [""] + fr["s15"] + ["", "---", ""] + fr["appendix-k"] + [""]
    for n in range(1, 24):
        k = f"DP-{n:02d}"
        out += [f"#### K-kata 13.{n} · {k} {names[k]} — reference solution", "", "```go"] + \
            kata(n, "kata.go") + ["```", ""]
    out += fr["keys-tail"]
    f.ins("R5-13", len(f.L), out, EV + " C-64 (skip-tests, one per section), the Go katas (one per pattern; Go "
          "replaces the suite standard's Python, recorded as a deviation under D12), the exercise bank, the academic "
          "pass (§15) and Appendix K with a key for every check and problem (rule 0.4.7).")


def build(files, go, root):
    cur(files[CUR])
    pri(files[PRI])
    pri_c40(files[PRI])
    sql(files[SQL])
    sec(files[SEC])
    dp(files[DPC])
    gof(go)


LED = "session-progress-ledger.md"
STATES = ("not-started", "in-progress", "taught", "mastered", "shaky", "unverified", "sliced")   # rule 0.4.5


def prefs(lines):
    """the earlier ledger's §5 bullets, verbatim (D2 keeps them)"""
    s = next(i for i, l in enumerate(lines) if l.startswith("## 5. "))
    e = next(i for i in range(s + 1, len(lines)) if lines[i].strip() == "---")
    return [l for l in lines[s + 1:e] if l.startswith("- ")]


def led(root):
    """C-23, C-66 (D2): the ledger is regenerated as a clean template with the §14 YAML block. The earlier ledger is
    read from its frozen copy beside the R2 snapshot; every line of it goes to records/ (D3)."""
    from r2b_common import F
    old = open(os.path.join(root, "outputs", "r2b", "in", LED), encoding="utf-8").read().split("\n")
    f = F(LED, old)
    RECORDS.setdefault(LED, [])
    p, new = prefs(old), []
    for l in fragments("ledger.md")["ledger"]:
        if l == "@@@PREFS@@@":
            new += p
        elif l == "@@@PREFS-YAML@@@":
            new += ["    - '" + x[2:].replace("'", "''") + "'" for x in p]
        else:
            new.append(l)
    f.block("R5-16", "regenerate", 0, len(old), new + [""],
            "D2 (fresh start): the ledger is regenerated as a clean template, nothing carried over as done, the §5 "
            "preferences kept verbatim. C-66: the §14 schema (one fenced YAML block, validated by verify.py against "
            "the ID registry and the DAG). C-23: the A4, A5, A6 and A7 checkpoints are listed, all not-started.")
    return f
