"""R12 Tutor corrections from the A5 session (learner decision D24, 2026-09-30).

D24: the learner asked that the corrections the tutor received in the session of 2026-09-30 (A5 networking: DNS
migration, DOS-02, NT-03) be applied to the course. Each had the same shape: a default lower in the priority order of
rule 0.4 (a turn "as long as one concept needs", "one gcloud line", a check that may be re-asked) had beaten the
learner's own instruction. The fixes put the learner's instruction into the rule the default came from, so the rules no
longer conflict:

  - rule 0.2 records the preferences: short turns with full rigour, no text-drawn diagrams, no assumed terms, the
    learner writes the GCP commands, a parked check is not re-asked word for word;
  - rule 0.4.1 (length, the stuck reply), 0.4.6 (the term scan), 0.4.7 (check test; confirm, do not answer) and 0.4.8
    (coverage strip) gain the mechanics; rule 0.5.4 gains the workplace-safety details and the question of which
    project is the learner's own;
  - one error in a part: NT-03 of the cybersecurity companion named VPC Service Controls as a DNS-tunnel defence (E4);
  - the guide's own rules (authored/guide/course-guide.md) gain Lens-1 as a command the learner builds, the lens
    layout, the retro-lens backlog, recalled figures flagged, the actor table (0.4.11.6) and the pre-reply pass (0.4.13).
The session's ledger delta (mastery states, misconception register, backlog, open questions) is the learner's own record
and is not course text.

cur(f)   main-course rule text; run after r11_gcplab and before r7_guide moves the rules to the guide.
build(files)
"""
from r2b_common import CUR, SEC

EV = ("D24 (2026-09-30): the learner asked that the tutor corrections of the A5 session be applied to the course; "
      "each puts the learner's instruction into the rule whose default had overridden it.")


def cur(f):
    f.ins_after("TF-1", "has broad access: each mapping also says where to look in it (Lens-W), read-only "
                "(rule 0.5.4).", [
        "- **Short turns, full rigour** (the learner's instruction of 2026-09-30, given twice). A concept is taught "
        "across several short turns; rigour is kept by never dropping the \"why\", not by lengthening a turn (rule "
        "0.4.1).",
        "- **No text-drawn diagrams** (2026-09-30; replaces the earlier request for fenced text diagrams). Use tables, "
        "numbered steps and prose; fenced blocks hold commands and code only.",
        "- **Never assume a term is known** (2026-09-30). A technical term is defined in one line the first time it "
        "appears unless it is `taught` on the ledger (rule 0.4.6).",
        "- **The learner writes the GCP commands** (2026-09-30). For every GCP topic the tutor teaches the command "
        "grammar and the `--help` path, the learner builds the command, and the tutor confirms or corrects it "
        "(rule 0.4.11.1).",
        "- **A parked check is never re-asked word for word** (2026-09-30). An unanswered check is reworded and made "
        "smaller, and only after the layer beneath it is settled (rule 0.4.1)."], EV)
    f.rep("TF-2", "anchor-rewrite", "- One concept per turn, at full depth.",
          "- One concept at a time, at full depth, across short turns.", EV)
    f.rep("TF-3", "anchor-rewrite", "A turn may be as long as one concept needs.",
          "A turn stays short: about 120 to 200 words of teaching plus at most one table or worked example. A concept "
          "that needs more is split (\"part 1 of 2\") and nothing is dropped; the why arrives in the next part.", EV)
    f.rep("TF-4", "anchor-rewrite", "give a foothold when the learner is genuinely stuck.",
          "give a foothold when the learner is genuinely stuck. A reply that does not answer the open check is the "
          "learner's real question: answer it first, park the check on the ledger, and ask it again once, reworded "
          "and smaller, after the layer beneath it is settled.", EV)
    f.rep("TF-5", "anchor-rewrite", "fix the check; don't mark the learner shaky.",
          "fix the check; don't mark the learner shaky. Before sending, scan the draft for every technical noun: one "
          "that is not `taught` on the ledger is defined in one line or removed. A learner who answers quickly is not "
          "thereby known to know a term.", EV)
    f.rep("TF-6", "anchor-rewrite", "and is never answered by the tutor in the same turn.",
          "and is never answered by the tutor in the same turn: after the learner answers, the tutor confirms and "
          "sharpens, and does not add the model answer. Before it is sent a check is tested: one holding \"and\", "
          "\"then\" or a second question mark is split across turns.", EV)
    f.rep("TF-7", "anchor-rewrite", "(6) naming the exact resume point and any open question, verbatim.",
          "(6) naming the exact resume point and any open question, verbatim. A one-line coverage strip of the "
          "module's bound IDs and their states opens each new concept and the close, so the learner can see what is "
          "covered and what is pending.", EV)
    f.rep("TF-8", "anchor-rewrite", "A project the employer sanctions for learning counts as the learner's own only "
          "when the learner names it in chat.",
          "A project the employer sanctions for learning counts as the learner's own only when the learner names it "
          "in chat. Every workplace session starts with `gcloud config list`, to confirm which account and project "
          "the commands will touch. Before the first Lens-2 build the tutor asks once which project is the learner's "
          "own and records the answer in the ledger; until then builds stay `[local]` or `[plan-only]`. A pasted "
          "workplace name or output is met plainly: rule 0.5.3 forbids it, with no \"this time\" exemption.", EV)


def sec(f):
    """E4: NT-03 named VPC Service Controls, a later control (rule 0.4.6) that guards Google APIs, not DNS or HTTPS to
    the internet"""
    ev = EV + " Error E4 of the session: VPC Service Controls was named as a DNS-tunnel defence."
    f.rep("TF-9", "anchor-rewrite", "Egress allowlists; DNS logging/monitoring; VPC-SC; DLP on egress paths; alert unusual "
          "DNS volume.", "Egress allowlists (VPC firewall egress rules); DNS logging/monitoring; DLP on egress paths; "
          "alert unusual DNS volume. VPC Service Controls (NT-06) is not a control here: it guards Google APIs, not "
          "DNS or HTTPS to the internet.", ev)
    f.rep("TF-10", "anchor-rewrite", "Lens-1: Cloud DNS logging; VPC-SC; Cloud NAT logs. Lens-2: conceptual tunneling",
          "Lens-1: Cloud DNS logging; VPC firewall egress rules; Cloud NAT logs. Lens-2: conceptual tunneling", ev)


def build(files):
    cur(files[CUR])
    sec(files[SEC])
