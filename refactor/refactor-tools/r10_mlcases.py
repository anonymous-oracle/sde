"""R10 ML system-design case studies (learner decision D21, 2026-09-25).

D21: the learner asked that the 309 case-study material of the old GCP curriculum be ingested — "only copy and
integrate material related to those case studies and nothing else". That material is the source's case-study atlas
(its Part 9c: the method, the gap table of concepts the cases need, four reference builds and ten family design packs
with worked company examples) and its Appendix M (the 309-entry index). Production ML system design had no owner in
the course (D1 names the families as literacy, D3 owns the MLOps lifecycle), so each piece goes to one owner:

  - the method, the ten families, three of the builds and the concepts the cases need become main course D6, with its
    academic pass D6.D (inverse propensity scoring, bandit regret, decision-shaped losses, causal effects and lifetime
    value) and problem set;
  - the fourth build, retrieval-augmented generation, stays with the Forward Deployed Engineer companion's FDE-25 and
    FDE-CAP1, which already build it; D6.F5 only reads its cases;
  - the index becomes main course Appendix M, deduplicated (309 entries, 299 distinct), each heading mapped to its
    family;
  - left out as not case-study material: the source's classical-model zoo (D1 owns classical models) and its PMLE
    product depth (D3 and the PMLE part own it).

cur(f, fr)   main-course edits; run after r9_practice and before r7_guide.
build(files)
"""
import os
import re

from r2b_common import CUR, PRI

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "authored")
MODULES = {"D6": "D6. "}   # the academic plan's new module (r5_acad, r8_fde and r9_practice hold the rest)
EV = ("D21 (2026-09-25): the learner asked that the 309 ML system-design case studies of the old GCP curriculum be "
      "ingested and integrated, and nothing else from it; production ML system design becomes D6 and the index "
      "Appendix M.")


def fragments():
    out, key = {}, None
    for l in open(os.path.join(SRC, "mlcases", "main-course.md"), encoding="utf-8").read().split("\n"):
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
    ev = EV + " D6 follows D5 in Track D and is taught after D3."
    f.ins_after("ML-1", "> **Readings:** Manning, Raghavan and Schütze, *Introduction to Information Retrieval* (2008), "
                "chapters 6, 8 and 11;", fr["d6"], ev)
    f.rep("ML-2", "anchor-rewrite", "and uplift measurement (why a lift claim needs a control group)",
          "and uplift measurement (why a lift claim needs a control group); each family is designed end to end in D6",
          EV + " D1 keeps the families as literacy and points to their owner.")
    f.rep("ML-3", "anchor-rewrite", "`[free-tier]` Cloud Run for the capstones `(verify)`.",
          "`[free-tier]` Cloud Run for the capstones `(verify)` · D6 `[local]` the three builds on toy data, "
          "`[free-tier]` Cloud Run and the BigQuery sandbox `(verify)`.", EV + " D6's labs carry Lab Reality tags "
          "(rule 0.5).")
    f.ins_after("ML-4", "Heavy 2026 emphasis on GenAI: Vertex AI Studio, Model Garden, RAG architectures", [
        "Framing a business problem as an ML problem, and the design questions in every domain, draw on D6's families "
        "and builds; the platform products themselves are taught here and in D3"], EV + " The PMLE part points to D6 "
        "for problem framing and design.")
    f.rep("ML-5", "anchor-rewrite", "Stanford CS 276 Information Retrieval and Web Search `(verify)` |",
          "Stanford CS 276 Information Retrieval and Web Search `(verify)`" + fr["align-add"][0] + " |",
          EV + " D6.D's pass names its course in the alignment table (rule 0.4.10.4).")
    f.rep("ML-5", "anchor-rewrite", "D5 (D5.D1–D5.D3) |", "D5 (D5.D1–D5.D3); D6 (D6.D1–D6.D4) |", EV)
    f.ins_after("ML-6", "- **D5-P7** · derive ·", fr["problems"], ev)
    f.ins_after("ML-6", "- **D5-P7** — Expected:", fr["keys"], ev)
    f.ins_after("ML-7", "- **D6-P8** — Expected:", [""] + fr["appendix-head"] + [""] + fr["appendix-body"],
                EV + " The index is the main course's last appendix; its headings map to D6's families.")


def pri_ids(pri):
    pri.rep("ML-8", "anchor-rewrite", "`A1…A11, B1…B6, C1…C7, D1…D5` — Curriculum module IDs.",
            "`A1…A11, B1…B6, C1…C7, D1…D6` — Curriculum module IDs.", EV + " The notation line's ID ranges follow "
            "the main course.")


def build(files):
    cur(files[CUR], fragments())
    pri_ids(files[PRI])
