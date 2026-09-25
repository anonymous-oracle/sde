"""R9 The architect's practice (learner decision D20, 2026-09-25).

D20: the learner said "the course should be such that it trains the learner to think like a bleeding edge FDE and
software systems architect and become one too." An audit against that aim found the knowledge taught (architecture
documentation and ATAM in A7, reliability and postmortems in C7, cost in B4, discovery and delivery in the Forward
Deployed Engineer companion) but not the practice that turns knowledge into judgment. Each missing piece goes to one
owner, so nothing is taught twice:

  - how an architect decides, forecasts, shapes teams and strategy, keeps current and reaches the role becomes main
    course B6, with its academic pass B6.D (decision analysis, real options, calibration) and problem set;
  - public postmortems become C7's case library, since C7 owns incidents;
  - the habits that make it thinking rather than reading (the judgment turn, the decision journal, failure recall,
    the frontier turn, design reviews) become rule 0.4.12 of the course guide (authored/guide/course-guide.md);
  - the course's aim is stated once, in the guide's head and the main course's "Why this order".

cur(f, fr)   main-course edits; run after r8_fde and before r7_guide.
build(files, pri)
"""
import os
import re

from r2b_common import CUR, PRI

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "authored")
MODULES = {"B6": "B6. "}   # the academic plan's new module (r5_acad.MODULES and r8_fde.MODULES hold the rest)
EV = ("D20 (2026-09-25): the learner asked that the course train them to think like, and become, a frontier Forward "
      "Deployed Engineer and software systems architect; the practice that was missing goes to one owner each.")


def fragments():
    out, key = {}, None
    for l in open(os.path.join(SRC, "practice", "main-course.md"), encoding="utf-8").read().split("\n"):
        m = re.match(r"^@@@ (\S+)$", l)
        if m:
            key = m.group(1)
            out[key] = []
        elif key:
            out[key].append(l)
    for v in out.values():
        while v and not v[0].strip():
            v.pop(0)
        while v and not v[-1].strip():
            v.pop()
    return out


def cur(f, fr):
    ev = EV + " The architect's practice becomes B6, the last module of Track B, taught in blocks across the phases."
    f.ins_after("PR-1", "> **Readings:** Sandhu, Coyne, Feinstein and Youman,", fr["b6"], ev)
    f.ins_after("PR-2", "Phase 8  Agentic Architect (GA) once ADK/agent material is solid", [
        "Phase 9  The architecture review board: B6.C, the course's last capstone, after D5's capstones and the PCA"], ev)
    f.rep("PR-2", "anchor-rewrite", "it is sat once D5's capstones pass, and the Forward Deployed Engineer companion's "
          "§15 prepares it.", "it is sat once D5's capstones pass, and the Forward Deployed Engineer companion's §15 "
          "prepares it. The certifications are milestones and evidence on the way, not the aim: the course trains you "
          "to think and work as a software systems architect and a Forward Deployed Engineer at the frontier, and to "
          "become one. B6 teaches that practice, every module exercises it (rule 0.4.12), and B6.C, the review board, "
          "is its final examination.", EV + " The course's aim is stated once in the main course, where its order is "
          "explained.")
    f.ins_after("PR-3", "Proving reliability: load tests against the SLO", fr["c7-cases"], EV + " Public postmortems "
                "join C7, which owns incidents; B6.5 teaches how to read them.")
    f.ins_after("PR-4", "| Systems engineering, reliability and delivery |", fr["align-row"], EV + " B6.D's pass needs "
                "its row in the alignment table (rule 0.4.10.4).")
    f.ins_after("PR-5", "- **B5-P4** · proof ·", fr["problems"], ev)
    f.ins_after("PR-5", "- **B5-P4** — Expected:", fr["keys"], ev)


def pri_ids(pri):
    pri.rep("PR-6", "anchor-rewrite", "`A1…A11, B1…B5, C1…C7, D1…D4` — Curriculum module IDs.",
            "`A1…A11, B1…B6, C1…C7, D1…D5` — Curriculum module IDs.", EV + " The notation line's ID ranges follow "
            "the main course (D5 was added by D19, B6 by D20).")


def build(files):
    cur(files[CUR], fragments())
    pri_ids(files[PRI])
