#!/usr/bin/env python3
"""R2b: make the five course files self-contained (learner decisions D5–D11).

Usage:  r2b_build.py ROOT [--from-r2]      (ROOT = the refactor workspace)

1. Reads the R2 output of the five course files from outputs/r2b/in/, a frozen snapshot checked against
   outputs/r2b/in.sha256 (the R2 output as committed at the end of R2). With --from-r2 it first re-runs the R2
   pipeline (r2_build.main) and refreshes the snapshot; that needs the legacy file gcp-curriculum.md, which decision
   D8 deletes after R2b, so --from-r2 works only on a checkout from before that deletion.
2. (--from-r2 only) Snapshots the R2 output of the five course files to outputs/r2b/in/.
3. Applies the R2b rules, file by file:
     G0  R2's in-file D3 archive moves to refactor/records/<file> (D6: no bookkeeping in course files)
     G1  provenance lines move to records
     G2  "(was …)" notes move to records
     G3  "Refactor note" labels become plain dated notes; conflict IDs leave the text
     G4  "Refactor-authored" / "added by the refactor" leads leave the text
     G8  N-tags (the withdrawn Track N, D5) in module stitch headers map to main-course anchors
   then the per-file rules in r2b_cur / r2b_pri / r2b_sql / r2b_dp / r2b_sec (file names, the file-style parent
   name, Northstar pointers, material dependencies) and the new content they insert (D9 gap fills).
4. (R2c, D12) r2c_go adds the Go Language Companion as a sixth part, rule 0.4.9 in the main course, and the
   tie-ins in the other parts (see r2c_go.py).
5. (R2c-bis, D13) r2c_gcp adds the few topics the legacy GCP notes held and no part taught (see r2c_gcp.py).
6. (R4, D16) r4_cur withdraws the reserved tracks M, U and S and rebinds every anchor to them (see r4_cur.py).
7. Writes work/, refactor/records/, outputs/r2b/journal.jsonl, and deletes work/northstar-reference-app.md (D5).

Deterministic and idempotent: every run starts again from the frozen R2 snapshot.
"""
import hashlib
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import r2_build  # noqa: E402
from r2b_common import JOURNAL, RECORDS, COURSE, F, DATE, CUR, PRI, SQL, DPC, SEC  # noqa: E402
import r2b_cur  # noqa: E402
import r2b_pri  # noqa: E402
import r2b_sql  # noqa: E402
import r2b_dp  # noqa: E402
import r2b_sec  # noqa: E402
import r2c_go  # noqa: E402
import r2c_gcp  # noqa: E402
import r4_cur  # noqa: E402
import r5_acad  # noqa: E402

# Track N section → the main-course anchor that holds the same subject (D5 + D11). Used only for stitch headers;
# body pointers are rewritten by hand in the per-file rules, because each needs its material present.
N_ANCHOR = [
    (r"N0\.4", "S2"), (r"N0", "B5"), (r"N1\.2", "C1"), (r"N2\.6", "C4"), (r"N2\.\d", "V-STOR"),
    (r"N3\.4", "B2"), (r"N3\.(?:0|x)", "A7"), (r"N4\.(?:5|6|7|10)", "A7"), (r"N4\.\d+", "A10"),
    (r"N5(?:\.\d|\.x)?", "A8"), (r"N6\.\d+", "V-NET"), (r"N7\.(?:\d|x)", "Phase 4 Security"),
    (r"N8\.1\.5", "A7"), (r"N8\.1", "A9"), (r"N8(?:\.0|\.C)?", "S2"), (r"N9\.2", "C2"), (r"N9\.\d", "V-STOR"),
    (r"N9b(?:\.1)?", "V-DATA"), (r"N9c(?:\.1)?", "D3"), (r"N9c\.\d", "D4"), (r"N10\.3", "B4"),
    (r"N10(?:\.0)?", "C6"), (r"N11b?", "S11"),
]


def n_anchor(tok):
    for pat, a in N_ANCHOR:
        if re.fullmatch(pat, tok):
            return a
    raise SystemExit(f"no main-course anchor for N-tag {tok!r}")


NTOK = re.compile(r"(?<![\w-])N\d+(?:\.\d+)*[a-z]?(?:\.[\dx]+)*(?![\w-])")


def remap_stitch(l):
    m = re.match(r"^(#### .*? — stitch: )(.*)$", l)
    if not m or not NTOK.search(m.group(2)):
        return l
    parts, out = [p.strip() for p in m.group(2).split(" · ")], []
    for p in parts:
        sub = []
        for q in [x.strip() for x in re.split(r"\s\+\s|\s/\s", p)]:
            q = NTOK.sub(lambda t: n_anchor(t.group(0)), q)
            if q not in sub:
                sub.append(q)
        p2 = " + ".join(sub)
        if p2 not in out and not any(p2 == x for x in out):
            out.append(p2)
    # drop a part that only repeats an anchor already named in an earlier part
    flat, final = set(), []
    for p in out:
        toks = set(x.strip() for x in p.split(" + "))
        if toks <= flat:
            continue
        flat |= toks
        final.append(p)
    return m.group(1) + " · ".join(final)


def generic(f):
    ev6 = "D6: course files carry no refactor bookkeeping; the text moves to refactor/records (D3 kept)"
    f.cut_archive(ev6)
    f.drop("G1", lambda l: bool(re.match(r"^\s*- \*\*Provenance\*\*|^\*Provenance \(", l)), ev6, mn=0)
    f.rx("G2", "move", r" ?\*\(was [^)]*\)\*| ?\(was E-[A-Z]{2}\d\)", "", ev6, mn=0)
    f.rx("G3", "anchor-rewrite", r"> \*\*Refactor note \([^)]*\):\*\* ", "> **Note:** ", ev6, mn=0)
    f.rx("G4", "anchor-rewrite", r"\*Refactor-authored \([^)]*\)\.\* ?|\*Refactor-authored section \([^)]*\)\.\* ?|"
         r" ?\*\((?:added by the refactor|Legend added by the refactor)[^)]*\)\.?\*| ?\*\(Legend added by the refactor, C-\d\d\.\)\*",
         "", ev6, mn=0)
    # conflict IDs: parentheticals holding only IDs, then "C-nn: " / ", C-nn" inside other parentheses
    cid = r"(?:C-\d{2}|C-NEW-\d{2})"
    f.rx("G5", "anchor-rewrite", r" ?\(" + cid + r"(?:(?:, ?| / |/| \+ |; ?)" + cid + r")*\)", "", ev6, mn=0)
    f.rx("G5", "anchor-rewrite", cid + r"(?:/" + cid + r")*: ", "", ev6, mn=0)
    f.rx("G5", "anchor-rewrite", r"(?:, |; )" + cid + r"(?:(?:, |/)" + cid + r")*(?=[)\]])", "", ev6, mn=0)
    # G9 the learner preferences: same text in every part; only the file tokens change (D6, D11)
    ev9 = "D6 + D11: the preference text stays; only its file names and the file-style parent name change"
    f.rx("G9", "anchor-rewrite", r"^(### 0\.\d Learner teaching preferences) \(binding; copied unchanged from "
         r"session-progress-ledger\.md §5, invariant 4\)$", r"\1 (binding)", ev9, mn=1, mx=1)
    f.rep("G9", "anchor-rewrite", "overlaps a `Curriculum` module, **teach it once", "overlaps a main-course module, "
          "**teach it once", ev9)
    f.rep("G9", "anchor-rewrite", "don't exist in `Curriculum` (as `sql-databases-companion.md` does), **say so",
          "don't exist in the main course (as the SQL companion's did before its IDs were rebound), **say so", ev9)
    # G10 each companion's register slice: "§0.3" alone would name the companion's own §0.3 (a different section)
    f.rx("G10", "anchor-rewrite", r"slice of it, and on a conflict §0\.3 wins\.",
         "slice of it, and on a conflict the main course's register wins.", "D6: a section reference must land on "
         "the material it names inside the part that carries it", mn=0, mx=1)
    ev5 = "D5 (no Track N) + D11 (course IDs stay as stitch tags): N-tag → the main-course anchor of the same subject"
    for i, l in enumerate(list(f.L)):
        new = remap_stitch(l)
        if new != l:
            f.block("G8", "anchor-rewrite", i, i + 1, [new], ev5)


GO_MARK = "## Journaled build edits (written by r2b_build.py; do not edit below this line)"


def write_records(root):
    rd = os.path.join(root, "records")
    os.makedirs(rd, exist_ok=True)
    for fn in COURSE:
        out = [f"# Records for {fn} (R2b, R2c and R4 build edits, {DATE})", "",
               "Refactor bookkeeping only, not course material. Decision D6 keeps provenance, the D3 archive and "
               "every line the build changed or removed (R2b; the R2c Go tie-ins; R4, rules R4-*) out of the course "
               "files; decision D3 keeps them here, verbatim. Each entry names the build journal number "
               "(outputs/r2b/journal.jsonl), the rule and the class.", ""]
        for n, rule, what, lines in RECORDS[fn]:
            out += [f"**J{n}** · {rule} · {what}", "", "````text"] + lines + ["````", ""]
        open(os.path.join(rd, fn), "w", encoding="utf-8").write("\n".join(out))
    # the Go companion's records file is hand-kept above the marker (R2c-bis, D13); the build owns what follows it
    gp = os.path.join(rd, r4_cur.GOF)
    head = open(gp, encoding="utf-8").read().split(GO_MARK)[0].rstrip("\n")
    out = [head, "", GO_MARK, "",
           "Journaled edits the build applies to the Go companion after it is assembled from its authored source "
           "(R4 onward). Each entry names the journal number (outputs/r2b/journal.jsonl), the rule and the class, "
           "and keeps the line as the authored source has it.", ""]
    for n, rule, what, lines in RECORDS.get(r4_cur.GOF, []):
        out += [f"**J{n}** · {rule} · {what}", "", "````text"] + lines + ["````", ""]
    open(gp, "w", encoding="utf-8").write("\n".join(out))


def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    from_r2 = "--from-r2" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    root = os.path.abspath(args[0] if args else ".")
    work = os.path.join(root, "work")
    snap = os.path.join(root, "outputs", "r2b", "in")
    sums = os.path.join(root, "outputs", "r2b", "in.sha256")
    if from_r2:
        sys.argv = [sys.argv[0], root]
        r2_build.main()
        os.makedirs(snap, exist_ok=True)
        for fn in COURSE:
            shutil.copyfile(os.path.join(work, fn), os.path.join(snap, fn))
        with open(sums, "w", encoding="utf-8") as fh:
            fh.writelines(f"{sha256(os.path.join(snap, fn))}  {fn}\n" for fn in COURSE)
    want = dict(reversed(l.split()) for l in open(sums, encoding="utf-8") if l.strip())
    for fn in COURSE:
        if sha256(os.path.join(snap, fn)) != want.get(fn):
            raise SystemExit(f"r2b_build: frozen R2 snapshot {fn} does not match outputs/r2b/in.sha256")
    files = {fn: F(fn, open(os.path.join(snap, fn), encoding="utf-8").read().split("\n")) for fn in COURSE}
    for fn in COURSE:
        generic(files[fn])
    r2b_cur.build(files[CUR], files)
    r2c_go.cur(files[CUR])   # D12: before the companions copy the contract, so rule 0.4.9 is in every copy
    r2c_gcp.cur(files[CUR])  # D13: the final gap-fill from the legacy GCP notes (material only)
    r5_acad.cur_contract(files[CUR])  # D17: rule 0.4.10 before the companions copy the contract
    r2b_pri.build(files[PRI], files)
    r2b_sql.build(files[SQL], files, root)
    r2b_dp.build(files[DPC], files)
    r2b_sec.build(files[SEC], files)
    go = r2c_go.build(files, root)   # D12: the Go Language Companion and its tie-ins
    r4_cur.build(files, go)          # R4 (D16): no Track M, U or S; every anchor rebound, material re-homed
    r5_acad.build(files, go, root)   # R5 (D17): the academic pass of every part
    for fn, f in list(files.items()) + [(go.n, go)]:
        open(os.path.join(work, fn), "w", encoding="utf-8").write("\n".join(f.L))
    ns = os.path.join(work, "northstar-reference-app.md")
    if os.path.exists(ns):
        os.remove(ns)
    write_records(root)
    with open(os.path.join(root, "outputs", "r2b", "journal.jsonl"), "w", encoding="utf-8") as fh:
        for k, j in enumerate(JOURNAL, 1):
            fh.write(json.dumps({"n": k, **j}, ensure_ascii=False, sort_keys=True) + "\n")
    by = {}
    for j in JOURNAL:
        by[(j["file"], j["cls"])] = by.get((j["file"], j["cls"]), 0) + 1
    print(f"r2b_build: {len(JOURNAL)} journaled edits · " +
          " · ".join(f"{fn.split('-')[0].split('.')[0]}:{c}={k}" for (fn, c), k in sorted(by.items())))


if __name__ == "__main__":
    main()
