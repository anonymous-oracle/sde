"""Shared framework for the R2 repair pipeline: the journaled Doc editor, constants and shared text.

Imported by r2_build.py and the per-file builders (r2_cur.py, r2_sql.py, r2_sec.py, r2_dp.py). JOURNAL is a single
module-level list, so every builder appends to the same journal.
"""
import re

DATE = "2026-09-24"
CUR = "Curriculum.md"
PRI = "system-design-primer-companion.md"
SQL = "sql-databases-companion.md"
DPC = "design-patterns-companion.md"
SEC = "cloud-cybersecurity-companion.md"
LED = "session-progress-ledger.md"
SKL = "learn-SKILL.md"
COMPANIONS = [PRI, SQL, DPC, SEC]
ARCHIVE_HEAD = "## Pre-refactor text archive (D3)"

JOURNAL = []


def note(cid, text):
    """a refactor-authored note line; the label makes authored text impossible to mistake for source text"""
    return f"> **Refactor note ({DATE}, {cid}):** {text}"


def fence_mask(lines):
    inside, mask = False, []
    for l in lines:
        s = l.lstrip()
        if s.startswith("```") or s.startswith("~~~"):
            mask.append(True)
            inside = not inside
        else:
            mask.append(inside)
    return mask


class Doc:
    def __init__(self, fname, lines):
        self.f = fname
        self.L = list(lines)
        self.archive = []  # (cid, what, [lines])

    # ---- lookup ----
    def find(self, needle, regex=False, start=0, end=None, expect=1):
        end = len(self.L) if end is None else end
        pat = re.compile(needle) if regex else None
        hits = [i for i in range(start, end)
                if (pat.search(self.L[i]) if regex else needle in self.L[i])]
        if expect is not None and len(hits) != expect:
            raise SystemExit(f"[{self.f}] expected {expect} match(es) for {needle!r}, got {len(hits)}: "
                             f"{[h + 1 for h in hits][:10]}")
        return hits

    def one(self, needle, **kw):
        return self.find(needle, expect=1, **kw)[0]

    def heading(self, title_prefix):
        return self.one("^#{1,6} " + re.escape(title_prefix), regex=True)

    def section_end(self, i):
        """exclusive end of the markdown section whose heading is at i"""
        lv = len(re.match(r"^(#+)", self.L[i]).group(1))
        for j in range(i + 1, len(self.L)):
            m = re.match(r"^(#+) ", self.L[j])
            if m and len(m.group(1)) <= lv:
                return j
        return len(self.L)

    # ---- journaled edits ----
    def _j(self, cid, cls, before, after, evidence, note_=""):
        JOURNAL.append(dict(file=self.f, cid=cid, cls=cls, before=before, after=after, evidence=evidence,
                            note=note_))

    def sub(self, cid, cls, pat, repl, evidence, start=0, end=None, expect_min=1, expect_max=None,
            skip_fence=True, only=None):
        """regex substitution line by line; journals each changed line. `only`: predicate on the line text"""
        rx = re.compile(pat)
        end = len(self.L) if end is None else end
        mask = fence_mask(self.L)
        n_hits = 0
        for i in range(start, end):
            if skip_fence and mask[i]:
                continue
            if only and not only(self.L[i]):
                continue
            new, k = rx.subn(repl, self.L[i])
            if k and new != self.L[i]:
                self._j(cid, cls, [self.L[i]], [new], evidence)
                self.L[i] = new
                n_hits += k
        if n_hits < expect_min or (expect_max is not None and n_hits > expect_max):
            raise SystemExit(f"[{self.f}] {cid}: {pat!r} matched {n_hits}, expected {expect_min}..{expect_max}")
        return n_hits

    def replace_line(self, cid, cls, i, new, evidence, archive=True, what=""):
        old = self.L[i]
        new = new if isinstance(new, list) else [new]
        if archive:
            self.archive.append((cid, what or "replaced line", [old]))
        self.L[i:i + 1] = new
        self._j(cid, cls, [old], new, evidence)

    def replace_block(self, cid, cls, s, e, new, evidence, archive=True, what=""):
        old = self.L[s:e]
        if archive:
            self.archive.append((cid, what or "replaced block", old))
        self.L[s:e] = new
        self._j(cid, cls, old, new, evidence)

    def insert(self, cid, cls, i, new, evidence):
        """insert new lines before index i"""
        self.L[i:i] = new
        self._j(cid, cls, [], new, evidence, note_=f"inserted before line {i + 1}")

    def insert_after(self, cid, cls, i, new, evidence):
        self.insert(cid, cls, i + 1, new, evidence)

    def move(self, cid, s, e, dest_before, evidence, prefix=(), suffix=()):
        """move lines [s, e) so they sit immediately before the line that is at dest_before now"""
        block = self.L[s:e]
        dest_text = self.L[dest_before]
        del self.L[s:e]
        d = self.L.index(dest_text) if dest_before >= e else dest_before
        self.L[d:d] = list(prefix) + block + list(suffix)
        self._j(cid, "move", block, list(prefix) + block + list(suffix), evidence,
                note_=f"moved {len(block)} lines to before {dest_text[:60]!r}")

    def finish(self):
        if self.archive:
            out = ["", "---", "", ARCHIVE_HEAD, "",
                   f"*Refactor-authored section ({DATE}).* Decision D3 says content may be re-arranged but never "
                   "removed. Each block below is the exact pre-refactor text (after the §5 ID renames) of a line "
                   "that R2 corrected or regenerated. It is kept for provenance only and is **not authoritative**; "
                   "the live text above wins. Tooling excludes this section from ID and anchor checks.", ""]
            for k, (cid, what, lines) in enumerate(self.archive, 1):
                out += [f"**D3-{k:02d}** · {cid} · {what}", "", "```text"] + lines + ["```", ""]
            self.L += out
        return self.L


# ------------------------------------------------------------------------------------------------ shared text
PREFS_HEAD = "Learner teaching preferences (binding; copied unchanged from session-progress-ledger.md §5, invariant 4)"


def ledger_prefs(ledger_lines):
    s = next(i for i, l in enumerate(ledger_lines) if l.startswith("## 5. Standing teaching preferences"))
    out = []
    for l in ledger_lines[s + 1:]:
        if l.startswith("## ") or l.strip() == "---":
            break
        if l.startswith("- "):
            out.append(l)
    assert len(out) == 4, out
    return out


C29_POINTER = ("When other companions bind to the same session, the Suite Session Protocol in `Curriculum` §0.4 "
               "governs.")


