"""R11 Every concept on GCP, hands on, with the workplace tour (learner decision D23, 2026-09-29).

D23: the learner asked that every valid or related concept be mapped to GCP and taught hands on, and said they have a
workplace GCP account with broad credentials and access that they can browse to understand. The course already gave
each concept a GCP lens (rule 0.4.11.1) and kept the workplace console read-only (rule 0.5.4). D23 tightens both:

  - a learner preference (rule 0.2): every concept with an honest GCP counterpart, in any of the seven parts, is shown
    on GCP and done hands on; a concept with none says so in one line instead of forcing a mapping;
  - the lens rule (authored/guide/course-guide.md, rule 0.4.11.1) gains the workplace tour, Lens-W: where the concept
    lives in the learner's workplace account and what to look for there, read-only;
  - Lab Safety (rule 0.5.4) spells out what browsing allows: the learner said "browse", and the account belongs to the
    employer, so building stays in the learner's own project and the workplace account is looked at, never changed,
    unless the learner names an employer-sanctioned sandbox project in chat;
  - the main course's Lab Reality paragraph describes the account as the learner now does.

cur(f)   main-course rule text; run after r10_mlcases and before r7_guide moves the rules to the guide.
build(files)
"""
from r2b_common import CUR

EV = ("D23 (2026-09-29): the learner asked that every related concept be mapped to GCP and taught hands on, and "
      "said their workplace GCP account, with broad access, is there to browse and understand.")


def cur(f):
    f.ins_after("GL-1", "Modules and phases have no fixed durations; the learner advances by passing checkpoints.", [
        "- **Every concept on GCP, hands on** (the learner's brief of 2026-09-29). Every concept with an honest GCP "
        "counterpart, in any part (theory, SQL, patterns, Go, security, the Forward Deployed Engineer work and D6's "
        "cases included), is shown on GCP and done hands on in the learner's own project, not only named "
        "(rule 0.4.11.1). A concept with no honest counterpart, such as a proof or a data structure, says so in one "
        "line rather than forcing a mapping. The learner learns well by browsing their workplace GCP account, which "
        "has broad access: each mapping also says where to look in it (Lens-W), read-only (rule 0.5.4)."],
        EV + " The brief joins the learner's preferences once.")
    f.rep("GL-2", "anchor-rewrite", "4. **The workplace console is read-only:** look, never create or change.",
          "4. **The workplace account is browsed, never changed.** The learner's workplace GCP account has broad "
          "access; it is for looking. Console pages and read-only commands (`list`, `describe`, `get-iam-policy`, "
          "`gcloud logging read`, a BigQuery dry run) are allowed. Nothing there is created, changed, started, "
          "stopped or deleted; no query runs that bills the employer beyond a dry run; no workplace credential is "
          "used by a lab or pasted into a session; and no workplace data, resource names or secrets enter a prompt, "
          "a note or a course file (rule 0.5.3). Building happens in the learner's own project under rule 0.5.2. A "
          "project the employer sanctions for learning counts as the learner's own only when the learner names it "
          "in chat.", EV + " Browsing is spelled out so broad access is not read as leave to change things.")
    f.rep("GL-3", "anchor-rewrite", "a workplace GCP account you can look in but not touch,",
          "a workplace GCP account with broad access that you browse but never change,", EV)
    f.rep("GL-3", "anchor-rewrite", "and use your workplace console read-only, as a museum, never to create or change "
          "anything there.", "and use your workplace console read-only, as a museum, never to create or change "
          "anything there: every concept's GCP lens says where to look in it (Lens-W, rule 0.4.11).", EV)


def build(files):
    cur(files[CUR])
