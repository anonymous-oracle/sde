"""R2 repairs for `cloud-cybersecurity-companion.md` (C-01, C-03, C-04, C-10…C-17, §6.2, §6.3, invariant 4).

- Module headers: the stitch is regenerated from BIND (§6.2 primary · secondaries), plus the old parent's numbered
  sections in N-form (C-03) and the non-anchor references the header already carried. A `Provenance:` line under
  each header records what was rebound or removed (pseudo-anchors are deleted, never reverse-engineered; C-10).
- §2 is regenerated from BIND (C-13, C-14, C-15 resolved by construction); the old table goes to the D3 archive.
- Prose: numbered sections x.y → Nx.y (C-03); pseudo-anchors rewritten by content (explicit list).
"""
import re

from r2_common import C29_POINTER, DATE, PREFS_HEAD, note

# §6.2: module → (primary, [secondary anchors])
BIND = {}


def _b(ids, primary, sec=()):
    for i in ids:
        BIND[i] = (primary, list(sec))


def _r(prefix, a, b):
    return [f"{prefix}-{n:02d}" for n in range(a, b + 1)]


_b(["PQ-S-01"], "A10", ["A1 recall"])
_b(["PQ-S-02", "PQ-S-05", "PQ-S-06"], "A10")
_b(["PQ-S-03"], "B1")
_b(["PQ-S-04"], "A5 HTTP/TLS (preview)", ["A10"])
_b(_r("TH", 1, 3), "A10", ["S6"])
_b(["TH-04"], "A7", ["A10"])
_b(["TH-05"], "Phase 4 Security (SecOps)")
_b(["TH-06"], "A9")
_b(_r("CR", 1, 10) + ["CR-13"], "A10")
_b(["CR-11", "CR-12"], "A5 TLS", ["A10"])
_b(["CR-19"], "A10", ["after CR-11/CR-12"])
_b(["CR-14", "CR-15", "CR-17", "CR-18", "CR-20"], "Phase 4 Security")
_b(["CR-16"], "A10", ["SC-01"])
_b(_r("AU", 1, 4), "A10", ["A5 HTTP cookie mechanics (recall)"])
_b(_r("AU", 5, 7), "A7", ["A10 federation/SSO"])
_b(_r("AU", 8, 10), "A10")
_b(_r("AU", 11, 13), "A7", ["A10"])
_b(["AU-14"], "B5")
_b(_r("AB", 1, 5), "A7", ["V-NET (Armor, Lens-3)"])
_b(_r("AB", 6, 8), "A7", ["B4"])
_b(["DOS-01"], "A5 load balancing")
_b(["DOS-02"], "A5 DNS/UDP")
_b(["DOS-03"], "A10")
_b(["DOS-04"], "Phase 4 Networking (Prop Lock)")
_b(["DOS-05"], "A10", ["A5 HTTP (recall)"])
_b(["DOS-06"], "A6")
_b(["DOS-07"], "B4")
_b(["DOS-08"], "A9", ["SD-26 (recall)"])
_b(["WA-01", "WA-02", "WA-03", "WA-04", "WA-06", "WA-07", "WA-08", "WA-12"], "A10")
_b(["WA-05"], "A10", ["A8 (SQL SL-13 owns the SQL mechanics)"])
_b(["WA-09"], "C6")
_b(["WA-10"], "A6 + U1", ["A10"])
_b(["WA-11"], "V-NET (Armor)")
_b(_r("CL", 1, 5), "B5", ["Phase 4 Security (Lens-3)"])
_b(["CL-06"], "A9", ["B5", "N8.1"])
_b(["CL-07"], "V-NET")
_b(["CL-08"], "B2", ["A7"])
_b(["NT-01", "NT-02", "NT-07"], "A5 NAT/firewalls/proxies")
_b(["NT-03", "NT-04"], "A5 DNS")
_b(["NT-05"], "A5 VPN")
_b(["NT-06"], "Phase 4 Security (Prop Lock)")
_b(["NT-08"], "A5 TLS")
_b(["CK-01", "CK-02", "CK-04"], "C1", ["B2"])
_b(["CK-03", "CK-05", "CK-06"], "C2")
_b(["WL-01"], "C1")
_b(["WL-02", "WL-03", "WL-05", "WL-06"], "C4", ["A11"])
_b(["WL-04"], "Phase 4 Security")
_b(["IR-01", "IR-02", "IR-04"], "C6", ["Phase 4 Security (SecOps)"])
_b(["IR-03", "IR-05", "IR-06", "IR-07", "IR-08"], "C7", ["Phase 4 Security"])
_b(_r("AI", 1, 5), "D4")
_b(["SC-01"], "A10")
_b(["SC-02"], "B2")
_b(["SC-03"], "Phase 4 Security")
_b(_r("PV", 1, 4), "Phase 4 Security", ["B1"])
_b(["PV-05"], "U7", ["A10"])
_b(["CM-01", "CM-02"], "Phase 4 Security", ["B1"])

# C-11: phantom checkpoint → existing card, chosen by content ([resolved-by-default])
PHANTOM = {
    "E-NT1": ("SEC-E4.21", "subdomain takeover via a dangling CNAME: the DNS card behind NT-03/NT-04, taught at A5 DNS"),
    "E-NT3": ("SEC-E10.7", "Shared VPC trust creep: the network-segmentation card for the Network Engineer track"),
    "E-AU3": ("SEC-E3.5", "JWT algorithm confusion (AU-05): the A7 JWT/OAuth awareness row, paired with CR-E4"),
    "E-CL1": ("SEC-Z0.5", "the shared-responsibility quiz (old Z0.5), as the prompt suggests"),
    "E-CL3": ("SEC-E3.1", "IAM privilege-escalation path (CL-03): the B5 IAM-abuse row"),
    "E-CK1": ("SEC-E6.5", "poisoned base image (`FROM node:latest`; WL-01): the C1 Docker row"),
    "E-CK2": ("SEC-E6.8", "RBAC wildcard on secrets (CK-03): the C2 RBAC row"),
    "E-DD2": ("SEC-E4.16", "Adaptive Protection meaning (DOS-04): the Phase 4 networking + Cloud Armor row"),
    "E-AB1": ("SEC-E4.3", "rate-limit design (AB-01): the Phase 4 networking + Cloud Armor row"),
}

PSEUDO_RE = re.compile(r"A10/B5\.\d+(?: owner labs| literacy)?|A5/Phase4-Net\.\d+|Phase4-Sec\.\d+(?: owner product| recall)?|"
                       r"A5 TLS / Phase 4 Armor|B5 IAM|A5\.2")
NUM_SET = {"0.4", "1.2", "2.3", "3.0", "3.4", "3.x", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7", "4.8", "4.9", "4.10",
           "5", "5.3", "5.x", "6.11", "6.12", "6.13", "6.14", "6.15", "6.16", "6.x", "7.1", "7.2", "7.3", "7.4",
           "7.5", "7.6", "7.7", "7.8", "7.9", "8", "8.1", "9.1", "9.2", "9b", "9c", "9c.2", "10", "10.0", "10.3"}
FOREIGN_LABEL = {"T.SysTheory": "§6.1 → A8 + A9 (+ U5)", "F1": "§6.1 → A3 + A6", "D2": "§6.1 → C4",
                 "D8": "C-53 D0…D8 → C1–C5 by content", "B4": "C-04: B4 is FinOps in `Curriculum`",
                 "Part 2": "the old parent's data part; §6.1 → A8 + N2.x"}
PROSE_NUM = re.compile(r"(?<![\w.§/$-])(Part [025]|\d{1,2}[bc]?(?:\.(?:\d{1,2}|x))?(?:–\d{1,2}\.\d{1,2})?)(?![\w.%/+])")


def nform(tok):
    if tok.startswith("Part "):
        return "N" + tok[5:]
    if "–" in tok:
        a, b = tok.split("–")
        return f"N{a}–N{b}"
    return "N" + tok


def header_stitch(mid, old):
    prim, sec = BIND[mid]
    anchors, keep, nf, removed, foreign = [prim] + sec, [], [], [], []
    for tok in [t.strip() for t in old.split(" · ")]:
        m = PSEUDO_RE.fullmatch(tok)
        if m:
            removed.append(tok)
        elif tok in FOREIGN_LABEL:
            foreign.append(tok)
        elif tok in NUM_SET:
            nf.append(nform(tok))
        elif tok in ("B5", "A5", "A10", "A7"):
            if not any(a.startswith(tok) for a in anchors):
                keep.append(tok)
        else:
            keep.append(tok)
    for n in nf:
        if n not in anchors:
            anchors.append(n)
    new = " · ".join(anchors + keep)
    prov = []
    if nf:
        prov.append("old numbered sections kept in N-form (" + ", ".join(nf) + "; C-03)")
    if foreign:
        prov.append("foreign labels rebound: " + "; ".join(f"`{f}` ({FOREIGN_LABEL[f]})" for f in foreign))
    if removed:
        prov.append("corrupted pseudo-anchors removed, not reverse-engineered: " + ", ".join(f"`{r}`" for r in removed)
                    + " (C-10)")
    prov.append(f"primary anchor per the §6.2 crosswalk: {prim}")
    return new, "- **Provenance** *(refactor, 2026-09-24)*: " + "; ".join(prov) + "."


def pairs(d, cid, needle, reps, evidence, cls="anchor-rewrite", what="", **kw):
    i = d.one(needle, **kw)
    new = d.L[i]
    for old, rep in reps:
        assert old in new, (cid, old, new[:120])
        new = new.replace(old, rep)
    d.replace_line(cid, cls, i, new, evidence, archive=(cls != "anchor-rewrite"), what=what)


ANCHOR_ORDER = ["A1", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "B1", "B2", "B4", "B5", "C1", "C2", "C4", "C6", "C7", "D4", "U7",
                "V-NET", "Phase 4 Networking", "Phase 4 Security"]
CHECKPOINTS = {
    "A5": "SEC-E4.21 (was E-NT1), CR-E12", "A7": "SEC-E3.5 (was E-AU3), CR-E4", "A10": "CR-E1…CR-E8, SEC-Z0.*",
    "B1": "SEC-Z0.5 (was E-CL1)", "B5": "SEC-E3.1 (was E-CL3)", "C1": "SEC-E6.5 (was E-CK1)",
    "C2": "SEC-E6.8 (was E-CK2)", "V-NET": "SEC-E4.3 (was E-AB1)",
    "Phase 4 Networking": "SEC-E4.16 (was E-DD2)", "Phase 4 Security": "CR-E9…CR-E15, SEC-CAP1",
}


def akey(primary):
    for a in ANCHOR_ORDER:
        if primary == a or primary.startswith(a + " "):
            return a
    raise KeyError(primary)


def stitch_table(old_rows):
    by = {}
    for mid, (prim, sec) in BIND.items():
        by.setdefault(akey(prim), []).append((mid, prim))
    also = {}
    for mid, (prim, sec) in BIND.items():
        for s in sec:
            for a in ANCHOR_ORDER:
                if s == a or s.startswith(a + " "):
                    rest = s[len(a):].strip()
                    also.setdefault(a, []).append(mid if not rest else f"{mid} {rest}" if rest.startswith("(")
                                                  else f"{mid} ({rest})")
    rows = ["| `Curriculum` anchor | Taught here (primary, §6.2) | Also in this session (secondary) | Checkpoint |",
            "|---|---|---|---|"]
    for a in ANCHOR_ORDER:
        if a not in by and a not in also:
            continue
        prim = ", ".join(m + ("" if p == a else f" {p[len(a):].strip()}" if p[len(a):].strip().startswith("(")
                              else f" ({p[len(a):].strip()})") for m, p in by.get(a, []))
        if a == "A5":
            prim += " — CR-11/CR-12 at mechanism level plus the minimal public-key intuition bridge (C-14)"
        if a == "A10":
            prim += " — formalizes the A5 bridge in one recall line (C-14)"
        rows.append(f"| **{a}** | {prim or '—'} | {', '.join(also.get(a, [])) or '—'} | {CHECKPOINTS.get(a, '—')} |")
    for r in old_rows:  # cert-track rows are kept; their checkpoints get the C-11 mapping
        if re.match(r"\| \*\*(Cloud Security Engineer|Cloud Network Engineer|Security Operations|GenAI|AWS Security)", r):
            r = r.replace("E-NT3", "SEC-E10.7 (was E-NT3)").replace("A5 revisit", "A5 recall")
            r = r.replace("`gcp.md` provider tables", "`Curriculum` Part VIII tables")
            rows.append(r)
    return rows


def build_sec(d, prefs):
    E1 = "C-01: `Curriculum` is the only parent (§3.1); `gcp.md` was its file name"
    E62 = "§6.2 crosswalk; C-03 (x.y → Nx.y); C-10 (pseudo-anchors deleted)"

    # ---------- title / intro ----------
    pairs(d, "C-10", "# The Cloud Cybersecurity Companion — Standalone Edition",
          [(" — Standalone Edition", "")], "C-10: one title (line 1 said Standalone Edition, the footers GCP-Native "
          "Edition)", cls="correction", what="title")
    pairs(d, "C-01", "**Companion to [`gcp.md`](./gcp.md)**", [("[`gcp.md`](./gcp.md)", "[`Curriculum`](./Curriculum.md)")],
          E1)
    pairs(d, "C-17", "This file is **standalone**. It does not depend on other companion files.",
          [("This file is **standalone**. It does not depend on other companion files.",
            "This file has **self-contained content**; ownership is shared per the suite overlap register "
            "(`Curriculum` §0.3)."), ("matching sections of `gcp.md`", "matching sections of `Curriculum`")],
          "C-17: it overlaps primer SD-35/SD-08/SD-10/11/SD-26/SD-29/Q22 and SQL SL-13/OD-04/CS-07", cls="correction",
          what="intro \"standalone\" line")
    pairs(d, "C-01", "**Does not own:** non-security tracks in `gcp.md`",
          [("in `gcp.md` (", "in `Curriculum` ("), ("stay in `gcp.md` only", "stay in `Curriculum` only")], E1)
    for needle in ["## 0. Read this first — how this file complements `gcp.md`",
                   "**This file is a complement to `gcp.md`, not a second roadmap.",
                   "Why: `gcp.md` owns the *roadmap spine*", "2. **Ownership split.** *`gcp.md` owns:*",
                   "4. **GCP lens at three depths**", "11. **User can override** skip/jump.",
                   "1. **Anchor** — name the `gcp.md` section"]:
        pairs(d, "C-01", needle, [("`gcp.md`", "`Curriculum`")], E1)
    pairs(d, "C-55", "3. **Same teaching discipline.**",
          [("before its `gcp.md` section has been covered", "before its `Curriculum` section has been covered "
            "(suite-wide rule: `Curriculum` §0.4.6)")], E1 + "; C-55")
    i = d.one("7. **Close** — tick boxes; note unlocked / shaky / postponed.")
    d.insert_after("C-29", "append", i, ["", C29_POINTER], "C-29 pointer")
    i = d.one("- `gcp.md` IDs: `A5`, `A7`, `A10`, `B1`, `B5`, `C1`, `C2`, `Phase4-Sec`, `Phase4-Net`")
    d.replace_line("C-03", "correction", i,
                   "- `Curriculum` IDs: module IDs (`A5`, `A7`, `A10`, `B1`, `B5`, `C1`, `C2` …), Part V category IDs "
                   "(`V-NET`, `V-SEC` …), `Phase 4 Networking` / `Phase 4 Security`, the reserved tracks (`M`, `U`, "
                   "`S`), and cert names (PCA, Cloud Security Engineer, …). `Nx.y` = a section of "
                   "`northstar-reference-app.md`; it carries the old parent's number and meaning (C-03). The old "
                   "pseudo-anchors (`Phase4-Sec.n`, `A5/Phase4-Net.n`, `A10/B5.n`) are gone (C-10).",
                   E62, what="§0.4 notation, anchor legend")
    i = d.one("| OWASP Top 10:2025 · ATT&CK Cloud | WA, AU, CL, WL, IR |")
    d.insert_after("INV-4", "new-content", i, ["", "### 0.6 " + PREFS_HEAD, ""] + prefs,
                   "invariant 4: ledger §5 preferences copied unchanged")

    # ---------- §2 (regenerated) ----------
    pairs(d, "C-01", "## 2. Stitch table — teach these with `gcp.md`", [("`gcp.md`", "`Curriculum`")], E1)
    t0 = d.one("| `gcp.md` section | Companion modules (same session) | Checkpoint |")
    t1 = next(j for j in range(t0, len(d.L)) if not d.L[j].startswith("|"))
    old = d.L[t0:t1]
    intro = [f"*Generated from the §6.2 crosswalk ({DATE}; C-11, C-12, C-13, C-14, C-15).* Every concept module "
             "appears once as primary; secondary anchors are previews, recalls or Lens-3 passes. The nine old "
             "checkpoint IDs that were never defined (shown below as 'was E-…') are mapped to existing cards by content "
             "(`crosswalk.md` §3; `[resolved-by-default]`). VPC-SC is NT-06 (C-12). The pre-refactor table is kept in "
             "the D3 archive.", ""]
    d.replace_block("§6.2", "regenerate", t0, t1, intro + stitch_table(old[2:]), E62 + "; C-11 mapping",
                    what="§2 stitch table (pre-refactor)")

    # ---------- §2.1 ----------
    reg = [("| `gcp.md` B1 |", "| `Curriculum` B1 |"),
           ("| `gcp.md` A5/A10 |", "| `Curriculum` A5 (mechanics) / A10 (formal; C-21) |"),
           ("| `gcp.md` B5 |", "| `Curriculum` B5 |"), ("| `gcp.md` Phase 4 Security |", "| `Curriculum` Phase 4 Security |"),
           ("| `gcp.md` Phase 4 Net |", "| `Curriculum` V-NET / Phase 4 Networking |"),
           ("| `gcp.md` C1/C2 |", "| `Curriculum` C1/C2 |"), ("| `gcp.md` A7 |", "| `Curriculum` A7 |")]
    for o, r in reg:
        pairs(d, "C-01", o, [(o, r)], E1)
    i = d.one("| Idea | Owner | This file adds |")
    d.insert("§7", "append", i, [note("§7", "the suite-wide register is `Curriculum` §0.3; this table is the security "
             "slice of it, and on a conflict §0.3 wins."), ""], "§7 register → Curriculum §0.3")

    # ---------- module headers + provenance ----------
    n = 0
    for i in range(len(d.L)):
        m = re.match(r"^(#### ([A-Z]{2,3}(?:-S)?-\d{2}) · .*? — stitch: )(.*)$", d.L[i])
        if m and m.group(2) in BIND:
            new, prov = header_stitch(m.group(2), m.group(3))
            d.replace_line("§6.2", "anchor-rewrite", i, m.group(1) + new, E62, archive=False)
            d.L.insert(i + 1, prov)
            d._j("C-03", "append", [], [prov], "C-03/§6.2: Provenance field", note_=f"inserted before line {i + 2}")
            n += 1
    assert n == len(BIND), (n, len(BIND))

    # ---------- C-10 prose fixes ----------
    pairs(d, "C-10", "as assumed props before their gcp.md gcp.md sections (7.3 / 7.5)",
          [("their gcp.md gcp.md sections (7.3 / 7.5)", "their Northstar sections (N7.3 / N7.5)")],
          "C-10: doubled word; C-03 N-form")
    pairs(d, "C-10", "**Pairing rule with A10 / B5 / API auth patterns & 7.3:**",
          [("**Pairing rule with A10 / B5 / API auth patterns & 7.3:** A10 / B5 / API auth patterns owns",
            "**Pairing rule with A7 (API auth patterns) + A10 & N7.3:** A7 (API auth patterns) + A10 own"),
           ("GCP KMS / CMEK (Phase 4 Security) owns CMEK", "Phase 4 Security (N7.3) owns CMEK")],
          "C-10: pseudo-anchor `A10 / B5 / API auth patterns` rewritten by content (A7 lists API authentication "
          "patterns; A10 authentication)")
    pairs(d, "C-10", "*Equal scale to AU/AB/CL. Roadmap A10 / B5 / API auth patterns owns",
          [("Roadmap A10 / B5 / API auth patterns owns", "`Curriculum` A7 (API auth patterns) + A10 own"),
           ("GCP KMS / CMEK (Phase 4 Security) owns CMEK *product* spine",
            "Phase 4 Security (N7.3) owns the CMEK *product* spine")], "C-10 pseudo-anchor")
    s = d.one("**Recommended CR session bundles (when spine allows):**")
    assert d.L[s + 1].startswith("1. CR-01…04") and d.L[s + 5].startswith("5. CR-16…19")
    d.replace_block("C-14", "correction", s + 1, s + 6, [
        "1. CR-11 + CR-12 on the `Curriculum` A5 TLS day, at mechanism level, with the minimal public-key intuition "
        "bridge (what a key pair does, what a signature proves, why DH gives a shared secret) — CR-E12.",
        "2. CR-01…04 + CR-E1…E5 at A10 (channel vs object encryption distinction; recalls the A5 bridge in one line).",
        "3. CR-05…07 + CR-13 at A10 (password/KDF day; the A7 API-auth product labs are recalled, N4.3).",
        "4. CR-08…10 + CR-19 at A10 (DH, public-key encryption, signatures formally; PQC after CR-11/CR-12).",
        "5. CR-14…15 + CR-20 at Phase 4 Security (KMS + key IR; N7.8).",
        "6. CR-16 at A10; CR-17…18 at Phase 4 Security, with Confidential Computing literacy + N9c privacy (survey "
        "depth)."], "C-14: A5 = CR-11/12 mechanism + bridge; A10 = CR-01…10, CR-13 at full depth; the old bundles "
        "put CR-01…04 and CR-08…12 on the A5 TLS day", what="§3.3.1 CR session bundles")
    pairs(d, "C-10", "- **GCP lens:** Lens-1: Memorystore + CDN TTLs (A5 TLS / Phase 4 Armor).",
          [("(A5 TLS / Phase 4 Armor)", "(V-STOR + V-NET)")], "C-10 pseudo-anchor, by content")
    pairs(d, "C-01", "Skip a companion family only by passing its skip-test. gcp.md still owns product labs",
          [("gcp.md still owns product labs", "`Curriculum` and Northstar still own product labs")], E1)
    pairs(d, "C-10", "- **Map to GCP:** A5 TLS / Phase 4 Armor / 6.11 path",
          [("A5 TLS / Phase 4 Armor / 6.11 path", "A5 TLS / N6.11 path")], "C-10; C-03")
    pairs(d, "C-10", "- **Map to GCP:** A5 TLS / Phase 4 Armor FinOps",
          [("A5 TLS / Phase 4 Armor FinOps", "V-NET (Armor) + B4 FinOps")], "C-10 by content (LB + Armor cost)")
    for needle in ["- **Map to GCP:** A5 TLS / Phase 4 Armor, CR-12, CR-17", "- **Map to GCP:** CR-12, A5 TLS / Phase 4 Armor",
                   "- **Map to GCP:** CR-11, A5 TLS / Phase 4 Armor"]:
        pairs(d, "C-10", needle, [("A5 TLS / Phase 4 Armor", "A5 TLS")], "C-10 pseudo-anchor (TLS cards)")
    pairs(d, "C-10", "- **Map to GCP:** CL-03, B5 IAM", [("B5 IAM", "B5")], "C-10: `B5 IAM` is the corrupted `0.5`")
    pairs(d, "C-10", "| IAM | CL-03, AU-*, B5 IAM/7.2 |", [("B5 IAM/7.2", "B5 / N7.2")], "C-10; C-03")
    pairs(d, "C-10", "- **Depends:** AU-*, WA-* core, AB-01/02, CL-01, CR-12/13/14/20, A10 / B5 / API auth patterns",
          [("A10 / B5 / API auth patterns + 7.3–7.4", "A7 (API auth patterns) + A10 + N7.3–N7.4")], "C-10; C-03")
    pairs(d, "C-10", "Run **SEC-CAP1** after A10 / B5 / API auth patterns + CR-20 unlocked",
          [("A10 / B5 / API auth patterns", "A7 (API auth patterns) + A10")], "C-10")
    pairs(d, "C-10", "| Storefront | Session, catalog, carts |", [("A5 TLS / Phase 4 Armor, ", "A5 TLS, ")], "C-10")
    pairs(d, "C-03", "- **Map to GCP:** IR-01, 7.6, 10", [("7.6, 10", "N7.6, N10")], "C-03")

    # ---------- C-03 generic numbered sections in prose ----------
    arch = d.L.index("## Appendix V — Verification / honesty notes")
    inside = False
    for i in range(arch):
        l = d.L[i]
        if l.lstrip().startswith("```"):
            inside = not inside
            continue
        if inside or l.startswith("#") or l.startswith("- **Provenance**") or l.startswith("| **"):
            continue
        new = PROSE_NUM.sub(lambda m: nform(m.group(1)) if m.group(1) in NUM_SET - {"5", "8", "10", "1.2"}
                            or m.group(1) in ("Part 0", "Part 2", "Part 5") or "–" in m.group(1) else m.group(1), l)
        if new != l:
            d.replace_line("C-03", "anchor-rewrite", i, new, "C-03: old parent section x.y → Nx.y (same meaning)",
                           archive=False)
    d.sub("C-09", "rename", r"\((E(\d{1,2})\.x)\)", r"(SEC-E\2.x)",
          "§5 rename: `E<level>.x` wildcards in Appendix K headings", expect_min=7, expect_max=7)

    # ---------- Appendix V: C-10 prose, numbering, one footer ----------
    s = d.one("8. **A10 / shared-responsibility principles principles** recalled never re-taught as new.")
    e = max(k for k in range(len(d.L)) if d.L[k].strip()) + 1
    old_tail = d.L[s:e]
    assert old_tail[-1].startswith("*End of The Cloud Cybersecurity Companion — GCP-Native Edition. Stitch with gcp.md")
    d.replace_block("C-10", "correction", s, e, [
        "8. **A10 / shared-responsibility principles** recalled never re-taught as new.",
        "9. **Built** 2026-09-22 for the reference cloud app / `Curriculum` pairing.",
        "10. **Line-count / completeness note:** This companion prioritizes stitchable attack+crypto depth over "
        "encyclopedic CCM dumps; use §8 as a gap finder when auditing the reference cloud app evidence.",
        "11. **When in doubt on a GCP SKU name:** prefer the `Curriculum` / Northstar product lab + live docs; "
        "companion scenarios stay valid even if a SKU renames.", "", "---", "",
        "*End of The Cloud Cybersecurity Companion. Stitch with `Curriculum`; bank ≠ dump; CR-* is a first-class "
        "pillar.*"], "C-10: doubled word; Appendix V skipped 9 and 12 and had two items after the first footer; two "
        "footers with a second title", what="Appendix V items 8–13 and the two footers")
    left = [l for l in d.L if "gcp.md" in l or re.search(r"\bE-(NT|AU|CL|CK|DD|AB)\d\b(?! \()", l)
            and "(was E-" not in l]
    assert not left, left[:3]
    return d
