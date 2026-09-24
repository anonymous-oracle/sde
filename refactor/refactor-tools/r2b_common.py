"""Shared framework for R2b (the self-contained rework; learner decisions D5–D11).

R2b edits the five course files that R2 wrote to work/. Every edit is journaled (outputs/r2b/journal.jsonl) with a
class, a rule ID, evidence, and the before/after lines. D3 (no content loss) is kept by records: every line R2b
changes or removes is copied verbatim into refactor/records/<file> before it changes, and R2's in-file D3 archive
moves there whole. d3_check.py --stage r2b proves that every line of the R2 output survives in work/ or in records/.
"""
import re

DATE = "2026-09-24"
CUR = "Curriculum.md"
PRI = "system-design-primer-companion.md"
SQL = "sql-databases-companion.md"
DPC = "design-patterns-companion.md"
SEC = "cloud-cybersecurity-companion.md"
COURSE = [CUR, PRI, SQL, DPC, SEC]
ARCHIVE_HEAD = "## Pre-refactor text archive (D3)"

JOURNAL = []
RECORDS = {f: [] for f in COURSE}   # file -> [(journal n, rule, what, [lines])]


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


class F:
    """one course file under R2b edit"""

    def __init__(self, name, lines):
        self.n = name
        self.L = list(lines)

    # ------------------------------------------------------------------ journal + records
    def _j(self, rule, cls, before, after, ev, what=""):
        JOURNAL.append(dict(file=self.n, rule=rule, cls=cls, before=before, after=after, evidence=ev, note=what))
        if before:
            RECORDS[self.n].append((len(JOURNAL), rule, what or cls, list(before)))

    # ------------------------------------------------------------------ lookup
    def idx(self, needle, start=0, regex=False):
        hits = [i for i in range(start, len(self.L))
                if (re.search(needle, self.L[i]) if regex else needle in self.L[i])]
        if len(hits) != 1:
            raise SystemExit(f"[{self.n}] expected 1 line for {needle!r}, got {len(hits)}: {[h + 1 for h in hits][:8]}")
        return hits[0]

    def heading(self, prefix):
        return self.idx("^#{1,6} " + re.escape(prefix), regex=True)

    def section_end(self, i):
        lv = len(re.match(r"^(#+)", self.L[i]).group(1))
        mask = fence_mask(self.L)
        for j in range(i + 1, len(self.L)):
            m = re.match(r"^(#+) ", self.L[j])
            if m and not mask[j] and len(m.group(1)) <= lv:
                return j
        return len(self.L)

    # ------------------------------------------------------------------ edits
    def cut_archive(self, ev):
        try:
            i = self.L.index(ARCHIVE_HEAD)
        except ValueError:
            return
        s = i
        while s > 0 and self.L[s - 1].strip() in ("", "---"):
            s -= 1
        block = self.L[s:]
        del self.L[s:]
        self._j("G0", "move", block, [], ev, what="R2 in-file D3 archive, moved out whole")

    def rx(self, rule, cls, pat, repl, ev, lo=0, hi=None, fence=False, mn=1, mx=None, only=None):
        r = re.compile(pat)
        hi = len(self.L) if hi is None else hi
        mask = fence_mask(self.L)
        n = 0
        for i in range(lo, hi):
            if mask[i] and not fence:
                continue
            if only and not only(self.L[i]):
                continue
            new, k = r.subn(repl, self.L[i])
            if k and new != self.L[i]:
                self._j(rule, cls, [self.L[i]], [new], ev)
                self.L[i] = new
                n += k
        if n < mn or (mx is not None and n > mx):
            raise SystemExit(f"[{self.n}] {rule}: {pat!r} matched {n}, expected {mn}..{mx}")
        return n

    def drop(self, rule, pred, ev, mn=1, mx=None):
        mask = fence_mask(self.L)
        keep, gone = [], []
        for i, l in enumerate(self.L):
            (gone if (not mask[i] and pred(l)) else keep).append(l)
        if len(gone) < mn or (mx is not None and len(gone) > mx):
            raise SystemExit(f"[{self.n}] {rule}: dropped {len(gone)}, expected {mn}..{mx}")
        for g in gone:
            self._j(rule, "move", [g], [], ev, what="line moved out of the course file")
        self.L = keep
        return len(gone)

    def rep(self, rule, cls, old, new, ev, n=1, fence=False):
        """exact substring replacement; `old` must occur exactly n times (outside fences unless fence=True)"""
        mask = fence_mask(self.L)
        hits = [(i, self.L[i].count(old)) for i in range(len(self.L))
                if old in self.L[i] and (fence or not mask[i])]
        tot = sum(c for _, c in hits)
        if tot != n:
            raise SystemExit(f"[{self.n}] {rule}: {old[:70]!r} occurs {tot}×, expected {n}: "
                             f"{[i + 1 for i, _ in hits][:8]}")
        for i, _ in hits:
            b = self.L[i]
            self.L[i] = b.replace(old, new)
            self._j(rule, cls, [b], [self.L[i]], ev)

    def line(self, rule, cls, needle, new, ev, regex=False):
        """replace the one line containing needle with new (a str, a list, or [] to remove it)"""
        i = self.idx(needle, regex=regex)
        new = [new] if isinstance(new, str) else list(new)
        b = self.L[i]
        self.L[i:i + 1] = new
        self._j(rule, cls, [b], new, ev)

    def block(self, rule, cls, s, e, new, ev, what=""):
        b = self.L[s:e]
        self.L[s:e] = list(new)
        self._j(rule, cls, b, list(new), ev, what=what)

    def ins(self, rule, i, new, ev, cls="new-content"):
        """insert lines before index i"""
        self.L[i:i] = list(new)
        self._j(rule, cls, [], list(new), ev, what=f"inserted before line {i + 1}")

    def ins_after(self, rule, needle, new, ev, cls="new-content", regex=False):
        self.ins(rule, self.idx(needle, regex=regex) + 1, new, ev, cls)

    def ins_section_end(self, rule, heading_prefix, new, ev, cls="new-content"):
        """append lines at the end of the section whose heading starts with heading_prefix"""
        h = self.heading(heading_prefix)
        e = self.section_end(h)
        while e > h + 1 and self.L[e - 1].strip() in ("", "---"):
            e -= 1
        self.ins(rule, e, [""] + list(new), ev, cls)
