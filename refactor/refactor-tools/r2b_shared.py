"""The shared rule text each companion carries in its own §0 (D6: every part self-contained).

The main course's §0.4 Suite Teaching Contract and §0.5 Lab Safety are copied, after the main course's own R2b
rules ran, into each companion as one subsection. Only the section references change, so that each one still
lands on the same text (the learner preferences have their own number in each part). These copies are the one
sanctioned repeat under D7: they are rules for teaching the course, not course topics (D11 reading, RD-10).
"""
import re

from r2b_common import CUR


def contract_lines(cur):
    s = cur.heading("0.4 Suite Teaching Contract")
    e = cur.heading("1. The Phase Plan")
    while cur.L[e - 1].strip() == "":
        e -= 1
    return cur.L[s:e]


def contract_copy(files, prefs_no, copy_no):
    """the §0.4 + §0.5 text, retargeted for a companion whose preferences are §0.<prefs_no>"""
    src = contract_lines(files[CUR])
    out = [f"### 0.{copy_no} Suite Teaching Contract and Lab Safety (same text in every part)", "",
           "The main course's §0.4 and §0.5, copied whole so that this companion can be taught on its own terms. "
           "The rule numbers stay the main course's (0.4.1…0.4.9, and the five Lab Safety rules), so \"main course "
           "§0.4.3\" and rule 0.4.3 here are the same rule. The **progress ledger** named below is the tutor's "
           "running record beside the inline boxes (main course §0.1): each ID's mastery state, the misconception "
           "register, the errata list, the recorded overrides and wrong predictions, and the exact resume point. "
           "The inline `- [ ]` boxes stay authoritative.", ""]
    for l in src:
        if l.startswith("### 0.4 Suite Teaching Contract"):
            out.append("**Suite Teaching Contract (main course §0.4).**")
            continue
        if l.startswith("### 0.5 Lab Safety"):
            out.append("**Lab Safety (main course §0.5).**")
            continue
        l = l.replace("(§0.2)", f"(§0.{prefs_no} here)").replace("per §0.2.", f"per §0.{prefs_no}.")
        l = l.replace("in §0.2 rule out", f"in §0.{prefs_no} rule out")
        l = l.replace("(§0.3)", "(main course §0.3)").replace("by the owner in §0.3.", "by the owner in main course "
                                                                                          "§0.3.")
        l = l.replace("the Lab Reality paragraph above", "the main course's Lab Reality paragraph")
        l = l.replace("this main course on order", "the main course on order")
        if re.search(r"§0\.[235](?![.\d])", l.replace(f"§0.{prefs_no} ", "").replace(f"§0.{prefs_no}.", "")
                     .replace(f"§0.{prefs_no})", "")) and "main course §0" not in l:
            raise SystemExit(f"contract copy: unretargeted section reference in {l[:120]!r}")
        out.append(l)
    return out



_PN = re.compile(r"(\b(?:[Aa]n?|[Tt]he|(?i:today's|each|every|one)) )?`Curriculum`('s)?( ?)")
_ADJ = re.compile(r"\*{0,2}(module|section|anchor|IDs?|mapping|pairing|depth|spine|slot|session)\b")
_ID = re.compile(r"\*{0,2}(?:[A-D]\d|[MUS]\d|V-[A-Z])")
_PART = re.compile(r"(?:Part|Phase) ")
_PREP = {"from", "in", "to", "of", "with", "by", "on", "at", "for", "via", "into", "per", "under", "name", "names"}


def _pn(m):
    """one backticked `Curriculum` (with its article) -> the main course, by what follows it"""
    art, poss, sp = m.group(1) or "", m.group(2), m.group(3)
    before, after = m.string[:m.start()], m.string[m.end():]
    low = art.strip().lower()
    if poss:
        out = "the main course's" + sp
    elif sp and _ADJ.match(after):
        prev = before.split()[-1].lower() if before.split() else ""
        det = "the " if prev in _PREP or not prev else ""        # "security-relevant main-course section"
        out = ("a " if low in ("a", "an") else art or det) + "main-course "
    elif sp and _ID.match(after):
        return art                       # the ID is the stitch tag; "the A7 module", "(A7"
    elif sp and _PART.match(after):
        out = "the main course's "
    elif after.startswith(")") and before.endswith("("):
        out = "main course"
    else:
        out = ("the " if low in ("", "the", "a", "an") else art) + "main course" + sp
    b = before.rstrip("* ")
    if b == "" or re.search(r"(?:[.!?|]|^-|^\d+\.|^>)$", b):
        out = out[0].upper() + out[1:]
    return out


def parent_name(f, rule):
    """every remaining backticked `Curriculum` in a companion becomes the main course (D11); IDs stay bare"""
    f.rx(rule, "anchor-rewrite", _PN.pattern, _pn, "D11: the file-style parent name becomes 'the main course'; "
         "IDs stay as stitch tags", mn=0)
