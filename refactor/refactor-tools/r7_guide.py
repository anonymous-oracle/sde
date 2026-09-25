"""R7 The course guide (learner decision D18, 2026-09-25).

D18: the learner asked for "a new .md file which stores the literal course outline, ToCs, etc which has references to
the course files", as the tutor's guide to teaching the whole course, with "necessary instructions and rules to manage
the other course files accordingly", and asked that no overlap or repeated information remain in any course file.

D18 reverses one part of D6 (each part self-contained): the rules had been copied whole into every part's §0 ("same
text in every part"), so that any part could be read alone. They now live once, in COURSE-GUIDE.md, and every part
refers to them as "rule 0.x":
  - the main course's §0.1–§0.5 (the parts and the stitch rule, the learner's preferences, the ownership register,
    the Suite Teaching Contract, Lab Safety) move to the guide, and Part X (whose overrides and session shape are
    rules 0.4.1 and 0.4.2) leaves the main course;
  - each companion loses its copy of the preferences and of the contract and Lab Safety, and its standing instruction,
    stitching rules and session outline give way to a short §0 that keeps only what is particular to that part
    (authored/guide/parts.md); the generic rules those sections restated join the contract as rule 0.4.11;
  - the five per-part slices of the overlap register (§2.1) merge into the one register, rule 0.3, with rows that
    said the same thing folded together (authored/guide/course-guide.md);
  - the cybersecurity companion's §0.5 alignment checklist folds into its Appendix U, which already held the same
    courses, so the security alignment is kept in one place.
Every line removed from a part goes to records/ (D3). The guide's §5 outline is generated from the built parts, so it
cannot drift from them. Within the guide the moved rules are rewritten only where a section reference changed meaning.
"""
import os
import re

from r2b_common import CUR, PRI, SQL, DPC, SEC, F, RECORDS, fence_mask

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "authored", "guide")
GUIDE = "COURSE-GUIDE.md"
EV = ("D18 (2026-09-25): the learner asked for one guide file holding the course outline and the rules for teaching and "
      "managing the course, and for no repeated information in any course file; the rules move to the guide once and "
      "each part keeps only what is particular to it.")


def fragments(name):
    out, key = {}, None
    for l in open(os.path.join(SRC, name), encoding="utf-8").read().split("\n"):
        m = re.match(r"^@@@ (\S+)$", l)
        if m:
            key = m.group(1)
            if key in out:
                raise SystemExit(f"r7_guide: duplicate fragment {key} in {name}")
            out[key] = []
        elif key:
            out[key].append(l)
    for v in out.values():
        while v and not v[0].strip():
            v.pop(0)
        while v and not v[-1].strip():
            v.pop()
    return out


def section(f, prefix):
    """(start, end) of the section whose heading starts with prefix"""
    h = f.heading(prefix)
    return h, f.section_end(h)


def trim_tail(f, s, e):
    """end index e moved back over trailing blank and --- lines, so a removed block keeps the separators after it"""
    while e > s and f.L[e - 1].strip() in ("", "---"):
        e -= 1
    return e


# ---------------------------------------------------------------------------------------------- the main course
def cur(f, fr):
    s, e = f.heading("0.1 The course parts"), f.heading("0.6 University")
    rules = {}
    for key, prefix in (("prefs", "0.2 Learner teaching preferences"), ("contract", "0.4 Suite Teaching Contract"),
                        ("safety", "0.5 Lab Safety")):
        a, b = section(f, prefix)
        rules[key] = f.L[a:trim_tail(f, a, b)]
    f.block("R7-1", "move", s, e, fr["cur-note"] + [""], EV, what="rules 0.1–0.5 moved to the course guide")
    a, b = section(f, "PART X")
    f.block("R7-1", "move", a, b, [], EV + " Part X restated rules 0.4.1 (overrides) and 0.4.2 (the session shape); "
            "its opening pointer (\"we start with A1\") is the guide's §1 fresh-start rule.",
            what="Part X moved out (its content is rules 0.4.1, 0.4.2 and the guide's §1)")
    f.rx("R7-1", "anchor-rewrite", r"§0\.([1-5](?:\.\d+)*)\b", r"rule 0.\1", EV, mn=1)
    return rules


# ---------------------------------------------------------------------------------------------- the companions
PARTS = [  # file key, fragment, notation heading, new notation heading
    (PRI, "pri-s0", "0.4 Notation", "### 0.3 Notation"),
    (SQL, "sql-s0", "0.4 Notation", "### 0.3 Notation"),
    (DPC, "dp-s0", "0.4 Notation", "### 0.3 Notation"),
    (SEC, "sec-s0", "0.4 Notation", "### 0.3 Notation"),
    (None, "go-s0", "0.4 Notation and the unlock list", "### 0.3 Notation and the unlock list"),
]


def companion(f, frag, note_head, new_head):
    # the new §0 replaces the heading, the standing instruction, the stitching rules and the session outline
    s, n = f.heading("0. Read this first"), f.heading(note_head)
    f.block("R7-2", "move", s, n, frag + [""], EV, what="§0.1–§0.3 replaced by the part's own §0 (generic rules are "
            "in the course guide)")
    f.line("R7-2", "anchor-rewrite", "### " + note_head, new_head, EV + " Renumbered after §0.1–§0.3 were replaced.")
    # everything after the notation section up to the next top-level section: the copied preferences, contract and
    # Lab Safety (and, in the cybersecurity companion, the alignment checklist that Appendix U already holds)
    a = f.section_end(f.heading(new_head[4:]))
    b = f.heading("1. ")
    b = trim_tail(f, a, b)
    f.block("R7-2", "move", a, b, [], EV, what="copied preferences, contract and Lab Safety moved out")
    a, b = section(f, "2.1 Overlap register")
    f.block("R7-3", "move", a, trim_tail(f, a, b), [], EV + " The slice is merged into rule 0.3, the one register.",
            what="overlap-register slice moved to rule 0.3")


def refs(files, go):
    pri, sql, dp, sec = files[PRI], files[SQL], files[DPC], files[SEC]
    ev = EV + " A reference to a section that moved is rewritten to name where the material is now."
    pri.rep("R7-4", "anchor-rewrite", "(rule 5, §0.2)", "(rule 2 of §0.2)", ev)
    sql.rep("R7-4", "anchor-rewrite", "(§0.2 rule 1)", "(rule 0.1)", ev)
    sql.rep("R7-4", "anchor-rewrite", "(the storefront OLTP data of §0.4)", "(the storefront OLTP data of §0.3)", ev)
    sql.rep("R7-4", "anchor-rewrite", "(Lab Safety, §0.6)", "(Lab Safety, rule 0.5)", ev)
    sql.rep("R7-4", "anchor-rewrite", "(§0.2 rule 5)", "(rule 0.4.11)", ev)
    # SQL §2.1 left with the register slice; §2.2 and §2.3 move up one
    sql.rx("R7-4", "anchor-rewrite", r"^### 2\.2 ", "### 2.1 ", ev, mn=1, mx=1)
    sql.rx("R7-4", "anchor-rewrite", r"^### 2\.3 ", "### 2.2 ", ev, mn=1, mx=1)
    sql.rx("R7-4", "anchor-rewrite", r"§2\.2\b", "§2.1", ev, mn=1)
    sql.rx("R7-4", "anchor-rewrite", r"§2\.3\b", "§2.2", ev, mn=1)
    sec.rep("R7-4", "anchor-rewrite", "the suite overlap register (the main course §0.3)",
            "the suite overlap register (rule 0.3)", ev)
    sec.rep("R7-4", "anchor-rewrite", "Stanford CS255 alignment: see §0.5.", "Stanford CS255 alignment: see Appendix U.",
            ev)
    sec.rep("R7-4", "anchor-rewrite", "DOS-02, §0.2.10", "DOS-02, rule 0.5", ev)
    sec.rep("R7-4", "anchor-rewrite", "(main course §0.6 and §0.5 here)", "(main course §0.6 and Appendix U)", ev)
    sec.ins_after("R7-4", "| MIT 6.1600 | Security definitions;", [
        "| CSA CCM v4.x | Cloud control framework | §8 checklist (not a control dump) |",
        "| OWASP Top 10:2025 · MITRE ATT&CK Cloud | Web application risks; cloud attacker techniques | WA-*, AU-*, "
        "CL-*, WL-*, IR-*; §9 |"], EV + " The §0.5 coverage checklist and Appendix U mapped the same courses; the two "
        "rows only §0.5 had join Appendix U, which becomes the one security index.")
    go.rep("R7-4", "anchor-rewrite", "(rule 8 of §0.2)", "(rule 7 of §0.2)", ev)
    # the sibling lists in the title blocks repeat the parts list, which is the guide's §2
    dp.rep("R7-4", "anchor-rewrite", " Sibling to the System Design Primer companion and the SQL & Databases companion.",
           "", EV + " The parts are listed once, in the guide's §2.")
    go.rep("R7-4", "anchor-rewrite", " Sibling to the System Design Primer companion, the SQL & Databases companion, "
           "the Design Patterns companion and the Cloud Cybersecurity companion.", "", EV + " The parts are listed "
           "once, in the guide's §2.")


# ---------------------------------------------------------------------------------------------- the outline
CARD = re.compile(r"^#### (\S+(?:[–-]\S+)?) · (.+?)(?: — stitch:.*)?$")
CARD_SECTIONS = {PRI: ("3.", "4."), SQL: ("4.",), SEC: ("3.",), "go": ("3.", "4.", "5.", "6.", "7.", "8."),
                 "fde": tuple(f"{n}." for n in range(4, 15))}
NO_CHILDREN = re.compile(r"^(Appendix K|Appendix P)\b")
CERT_PARTS = ("PART V ", "PART VI ", "PART VII ")


def cert_title(l):
    m = re.match(r"^\d+\. (.+?\((?:[A-Z][A-Za-z0-9-]*)\))", l)
    return m.group(1) if m else re.split(r" — | \(", l.split(". ", 1)[1])[0]


def outline(name, key, lines):
    out, mask = [], fence_mask(lines)
    top, cards, hide = "", [], False

    def flush():
        if cards:
            out.append("    - " + " · ".join(cards))
            cards.clear()
    for i, l in enumerate(lines):
        if mask[i]:
            continue
        m = re.match(r"^(#{2,4}) (.+?)\s*$", l)
        if m:
            lv, t = len(m.group(1)), m.group(2)
            if lv == 2:
                flush()
                top, hide = t, bool(NO_CHILDREN.match(t))
                out.append(f"- **{t}**")
            elif lv == 3 and not hide:
                flush()
                out.append(f"  - {t}")
            elif lv == 4 and not hide and top.startswith(CARD_SECTIONS.get(key, ())):
                c = CARD.match(l)
                if c:
                    cards.append(f"**{c.group(1)}** {c.group(2)}")
            continue
        if top.startswith(CERT_PARTS) and re.match(r"^\d+\. ", l):
            nxt = next((x for x in lines[i + 1:i + 4] if x.strip()), "")
            if nxt.startswith("- [ ]") and nxt.rstrip().endswith("passed"):
                out.append(f"  - {cert_title(l)}")
    flush()
    return out


# ---------------------------------------------------------------------------------------------- the guide
def guide(files, go, fde, rules, fr):
    g = F(GUIDE, [])
    RECORDS.setdefault(GUIDE, [])
    prefs = list(rules["prefs"])
    contract = list(rules["contract"])
    safety = list(rules["safety"])
    reg = open(os.path.join(SRC, "register.md"), encoding="utf-8").read().rstrip("\n").split("\n")
    L = (fr["head"] + [""] + fr["s1"] + [""] + fr["s2"] + ["", "## 3. The rules (rules 0.1–0.5)", ""]
         + fr["r0.1"] + [""] + prefs + [""] + fr["r0.3"] + [""] + reg + [""] + contract + [""] + fr["r0.4.11"]
         + [""] + safety + [""] + fr["s4"] + [""] + fr["s5"] + [""])
    g.L = L
    ev = EV + " Moved rule text is rewritten only where it named a section that is now a rule, or a copy that is gone."
    g.rep("R7-5", "anchor-rewrite", "per each companion's own §0.2 stitching rules", "per the stitch rule (rule 0.1)",
          ev)
    g.rep("R7-5", "anchor-rewrite", "One contract for every part; each companion carries the same contract in its own "
          "§0 and adds its session detail.", "One contract for every part; each part's §0 adds only what is "
          "particular to that part.", ev)
    g.rep("R7-5", "anchor-rewrite", "(3) this main course on order", "(3) the main course on order", ev)
    g.rep("R7-5", "anchor-rewrite", "One rule set for every file; it unifies the cybersecurity companion's rule 10, "
          "the SQL companion's rule 10 and the Lab Reality paragraph above.", "One rule set for every part. The "
          "main course's Lab Reality paragraph (its §0) sets the budget these rules protect.", ev)
    lo, hi = g.L.index("## 3. The rules (rules 0.1–0.5)"), g.L.index(fr["s4"][0])   # the moved rules only
    g.rx("R7-5", "anchor-rewrite", r"(?<!main course )§0\.([1-5](?:\.\d+)*)\b", r"rule 0.\1", ev, lo=lo, hi=hi, mn=1)
    parts = [(CUR, CUR, "The main course"), (PRI, PRI, "The System Design Primer Companion"),
             (SQL, SQL, "The SQL & Databases Companion"), (DPC, DPC, "The Design Patterns Companion"),
             (SEC, SEC, "The Cloud Cybersecurity Companion"), (go.n, "go", "The Go Language Companion"),
             (fde.n, "fde", "The Forward Deployed Engineer Companion")]
    for k, (fn, key, title) in enumerate(parts, 1):
        src = {"go": go.L, "fde": fde.L}.get(key) or files[fn].L
        g.L += [f"### 5.{k} {title} — `{fn}`", ""] + outline(fn, key, src) + [""]
    while g.L and not g.L[-1].strip():
        g.L.pop()
    g.L.append("")
    return g


def dedupe(files):
    """R7-6: the SQL bank's per-card gate lines only repeated the gate their level states once, under its heading"""
    sql = files[SQL]
    ev = (EV + " Each of these card lines repeated, word for word, the gate its level already states once under the "
          "level heading; the stitch-partner half is stated once in the bank's introduction.")
    sql.drop("R7-6", lambda l: re.fullmatch(r"- \*\*Prereq gate:\*\* (?:Level \d+ gate above; stitch partners from "
                                           r"§2 as tagged|matching PQ unlocked)", l) is not None, ev, mn=100, mx=100)
    sql.rep("R7-6", "new-content", "**Bank ≠ dump** (rule 0.4.11): issue **one** item at the ledger rung;",
            "**Gates** are stated once per level, under its heading; a card's stitch partners are the §2 rows its tags "
            "name. **Bank ≠ dump** (rule 0.4.11): issue **one** item at the ledger rung;", ev)


def build(files, go, fde):
    fr = fragments("course-guide.md")
    fp = fragments("parts.md")
    rules = cur(files[CUR], fp)
    for fn, key, note, new in PARTS:
        companion(go if fn is None else files[fn], fp[key], note, new)
    refs(files, go)
    dedupe(files)
    return guide(files, go, fde, rules, fr)
