"""R8 The Forward Deployed Engineer companion, the suite's seventh part (learner decision D19, 2026-09-25).

D19: the learner asked to "ingest fde-ccdvf-course-meta-prompt.md and integrate it into the course/ directory. Not just
adding it, modify it such that there should not be any repeating content and the curriculum stays unified. Update the
course guide accordingly." The brief is a tutor meta prompt: a learner profile, teaching rules, the FDE role, the
CCDV-F exam, a stage plan A–N and a progress log. It is split by owner, so nothing is taught or stated twice:

  - its teaching rules join the course guide's rules (rule 0.2 preferences, rule 0.4.1 rhythm, rule 0.4.9 languages,
    rule 0.5 Lab Safety) as journaled edits to the main course's rule text, before r7_guide moves that text out;
  - its stage items that the course already teaches stay with their owners; the few from-scratch builds and
    checkpoints they lacked are added to those owners (A2, A3, A4, C4; the Go companion's GO-21);
  - what the course did not teach becomes main course D5 (the parent module, with its academic pass D5.D and problem
    set) and the Forward Deployed Engineer companion (refactor/authored/fde-companion.md), whose §1 maps every brief
    item to its owner;
  - its module IDs A1…E7 and exam domains D1–D8 collide with main-course IDs and are not kept (the domains are CF1…CF8);
  - its progress log is the ledger delta of rule 0.4.8, not a section of a course file.

cur(f)             main-course edits; run after r6 and before r7_guide, so the guide receives the edited rules.
go_edits(go)       the GO-21 raw-socket builds.
build(files, go, root) both, and the companion itself, journaled as one new-content insert.
"""
import os
import re

from r2b_common import CUR, F

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "authored")
FDEF = "fde-companion.md"
MODULES = {"D5": "D5. "}   # the academic plan's new module (r5_acad.MODULES holds the rest)
EV = ("D19 (2026-09-25): the learner asked to ingest the Forward Deployed Engineer and CCDV-F brief into the course "
      "with no repeated content and one unified curriculum; each item goes to its owner.")


def fragments():
    out, key = {}, None
    for l in open(os.path.join(SRC, "fde", "main-course.md"), encoding="utf-8").read().split("\n"):
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


def rules(f):
    """the brief's teaching rules, merged into the rules the guide will hold (rules 0.2, 0.4.1, 0.4.2, 0.4.9, 0.5)"""
    ev = EV + " The brief's teaching rules that the rules did not already hold are added to them once."
    f.ins_after("FDE-1", "**say so plainly rather than forcing a silent, possibly-wrong mapping** — this was well "
                "received when done for the SQL companion.", [
        "- **Build it by hand, then use the library** (the learner's brief of 2026-09-25). A concept that can be "
        "built at toy size is taught in three passes: a small toy built by hand, just enough to show how it works; "
        "then the real library, naming what it handles that the toy did not (edge cases, performance, security, "
        "standards); then the library in production code. Hand-written cryptography is the exception: built only to "
        "learn, never used for real (Lab Safety, rule 0.5).",
        "- **Languages in order: Python, then Go, then TypeScript** (rule 0.4.9). Assume no prior knowledge of code, "
        "of mathematics beyond school level, of networking or of AI.",
        "- **Tone: warm and direct; no emoji, no cheerleading.** When something is hard, say \"this trips most "
        "people up\", never \"anyone can do this\". Praise only specific, earned things; say plainly and kindly when "
        "code or reasoning is wrong or weak, and what to do about it.",
        "- **Stop when it is understood.** When the learner explains a concept back correctly or applies it to a new "
        "case, say so plainly, summarize what was covered, and move on; do not keep probing past understanding.",
        "- **No time boxes.** Modules and phases have no fixed durations; the learner advances by passing "
        "checkpoints."], ev)
    f.rep("FDE-2", "anchor-rewrite", "(the learner preferences in §0.2 rule out separate calibrating questions).",
          "(the learner preferences in §0.2 rule out separate calibrating questions). A new topic's first check is "
          "the calibrating one, woven into its first teaching turn: predict an output, or give a best guess.", ev +
          " The brief's \"diagnose with one calibrating question\" yields to the woven checks of §0.2 and becomes "
          "the first of them.")
    f.rep("FDE-3", "anchor-rewrite", "→ Go implementation (Go companion) → attacker/crypto (cyber).",
          "→ Go implementation (Go companion) → Claude application (Forward Deployed Engineer companion) → "
          "attacker/crypto (cyber).", ev)
    f.rep("FDE-4", "anchor-rewrite", "and its later modules bind where they are first used. Four rules:",
          "and its later modules bind where they are first used. TypeScript is the third language, after Python and "
          "Go: the Forward Deployed Engineer companion's FDE-01 teaches it when D5 begins, for Claude clients and MCP "
          "servers; rule 1 binds it as it binds Go, and that companion's §0 gives its lab acceptance. Four rules:", ev)
    f.rep("FDE-5", "anchor-rewrite", "crypto through vetted libraries only.", "crypto through vetted libraries "
          "only; cryptography written by hand (a JWT signer, a hash, a TLS toy) is built only to learn, is never "
          "deployed, and the tutor says so each time it is built.", ev)
    f.rep("FDE-5", "anchor-rewrite", "with a budget alert set before the first apply.", "with a budget alert set "
          "before the first apply. Model API calls are replayed from recorded responses first; a live call runs only "
          "inside a workspace whose spend limit is set before the first call.", ev)
    f.rep("FDE-5", "anchor-rewrite", "never put a password, key or real customer data in a query, a prompt or a "
          "course file.", "never put a password, key or real customer data in a query, a prompt or a course file; an "
          "API key lives in an environment variable or a secret manager, never in code, a client or a transcript.", ev)


def cur(f, fr):
    rules(f)
    ev = EV + " The brief's from-scratch builds and checkpoints join the modules that already teach their concepts."
    f.ins_after("FDE-6", "Calculus intuition: derivatives as \"rate of change,\" gradients, why gradient descent trains "
                "ML models", [
        "Built by hand in Python, then checked against the library (the three passes, rule 0.2): matrix "
        "multiplication as three nested loops, checked against NumPy; a gradient-descent minimizer for a function of "
        "one and then two variables; softmax with a temperature, and sampling from it",
        "Checkpoint (A2.C): compute a softmax and one gradient-descent step by hand, then verify both in code"], ev)
    f.rep("FDE-7", "anchor-rewrite", "Python: variables, control flow, functions, data structures (list/dict/set/tuple), "
          "OOP basics, virtual environments, package management (pip)", "Python: variables, control flow, functions, "
          "data structures (list/dict/set/tuple), OOP basics, modules and imports, exceptions and reading a "
          "traceback, virtual environments, package management (pip)", ev)
    f.ins_after("FDE-7", "Git fundamentals (deep dive lives in A11)", [
        "Testing, built by hand first (rule 0.2): a tiny test runner that finds `test_` functions, runs them and "
        "reports each pass or failure with its traceback; then pytest",
        "Checkpoint (A3.C): a tested command-line program in Python, pushed to a Git host"], ev)
    f.ins_after("FDE-8", "Sorting/searching intuition (enough to reason about algorithmic choices", [
        "Built by hand, then checked against the library (rule 0.2): binary search and merge sort, tested against "
        "`bisect` and `sorted` on random inputs; A4.D1 and A4.D2 prove them"], ev)
    f.ins_after("FDE-9", "Concepts: build → test → package → deploy pipeline stages, artifact repositories", [
        "Built by hand first (rule 0.2): a minimal CI script that, on each push, checks out the commit, runs the "
        "linters and the tests, and fails on the first non-zero exit — before a hosted pipeline"], ev)
    # Track D: D5 and the certification
    ev = EV + " What the course did not teach becomes main course D5, taught through the new companion."
    f.rep("FDE-10", "anchor-rewrite", "Required for PMLE, AIP-C01, and Agentic Architect specifically",
          "Required for PMLE, AIP-C01, Agentic Architect and CCDV-F (D5) specifically", ev)
    f.ins_after("FDE-11", "Hoffmann et al., \"Training Compute-Optimal Large Language Models\" (2022); Ouyang et al.",
                fr["d4-note"] + [""] + fr["d5"], ev)
    f.rep("FDE-12", "anchor-rewrite", "D4 `[local]` RAG and agent prototypes, `[credit ~$X]` timeboxed model API calls "
          "`(verify)`.", "D4 `[local]` RAG and agent prototypes, `[credit ~$X]` timeboxed model API calls `(verify)` · "
          "D5 `[local]` builds and recorded-response fixtures, `[credit ~$X]` Claude API calls inside a workspace "
          "spend limit, `[free-tier]` Cloud Run for the capstones `(verify)`.", ev)
    f.rep("FDE-13", "anchor-rewrite", "just learning new names and new console layouts for concepts you already own.",
          "just learning new names and new console layouts for concepts you already own. CCDV-F, Anthropic's Claude "
          "Certified Developer – Foundations, is the one certification outside the cloud providers: it is sat once "
          "D5's capstones pass, and the Forward Deployed Engineer companion's §15 prepares it.", ev)
    f.rep("FDE-14", "anchor-rewrite", "D4 (D4.D1–D4.D5) |", "D4 (D4.D1–D4.D5); D5 (D5.D1–D5.D3) |", ev)
    f.rep("FDE-14", "anchor-rewrite", "Stanford CS 336 Language Modeling from Scratch |", "Stanford CS 336 Language "
          "Modeling from Scratch · Stanford CS 276 Information Retrieval and Web Search `(verify)` |", ev)
    f.rep("FDE-14", "anchor-rewrite", "Huyen, *Designing Machine Learning Systems* (2022) |", "Huyen, *Designing "
          "Machine Learning Systems* (2022) · Manning, Raghavan and Schütze, *Introduction to Information Retrieval* "
          "(2008) |", ev)
    f.ins_after("FDE-15", "- **D4-P5** · design ·", fr["problems"], ev)
    f.ins_after("FDE-15", "- **D4-P5** — Expected:", fr["keys"], ev)


def go_edits(go):
    ev = EV + " The brief's raw-socket builds belong to GO-21, which teaches the Go HTTP they lead up to."
    go.rep("FDE-16", "anchor-rewrite", "| GO-21 | `net/http` server and client,", "| GO-21 | `net` (`Listen`, "
           "`Dial`, `Conn`), `net/http` server and client,", ev)
    go.rep("FDE-16", "anchor-rewrite", "- **Build lab `[local]`:** the `shop.example` orders API skeleton",
           "- **Build lab `[local]`:** first, from scratch (rule 0.2): an echo server on `net.Listen` and `net.Conn`, "
           "then a minimal HTTP/1.1 server and client over raw TCP (the request line, headers, `Content-Length`, one "
           "response per connection), each with a Python `socket` twin; then the same endpoint on `net/http`, with a "
           "one-page written comparison of what the library handles that the toy did not (persistent connections, "
           "chunked bodies, timeouts, header limits, HTTP/2). Then the `shop.example` orders API skeleton", ev)


def assemble(root):
    src = open(os.path.join(SRC, FDEF), encoding="utf-8").read().split("\n")
    if any("@@" in l for l in src):
        raise SystemExit("r8_fde: a marker is left in the Forward Deployed Engineer companion")
    g = F(FDEF, [])
    g.ins("FDE-0", 0, src, EV + " The whole file is new, authored for R8 from the brief as material only; its rules "
          "went to the course guide and its stage items to their owners (its §1 maps each one).")
    return g


def build(files, go, root):
    cur(files[CUR], fragments())
    go_edits(go)
    return assemble(root)
