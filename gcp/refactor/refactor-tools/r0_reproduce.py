#!/usr/bin/env python3
"""R0: reproduce every conflict C-01…C-75 (+ C-NEW-nn) against work/ copies.
Each row = (id, claim, shell command run in work/, status, note). Status is the reviewer's verdict on the
captured output: reproduced | different | not reproduced | chat-only (claim about chat state, not checkable in files).
Idempotent: re-running rewrites r0-reproduction.md from fresh command output. Usage: python3 r0_reproduce.py <refactor_root>"""
import subprocess, sys, os, datetime

P, S, Y, D, C, L, K = ("system-design-primer-companion.md", "sql-databases-companion.md", "cloud-cybersecurity-companion.md",
                       "design-patterns-companion.md", "Curriculum.md", "session-progress-ledger.md", "learn-SKILL.md")
R = "reproduced"; DF = "different"; NR = "not reproduced"; CO = "chat-only"
G = "../../gcp-curriculum.md"  # original foreign parent, outside the 7 inputs

CHECKS = [
 ("C-01", "four parent names", f"for f in {P} {S} {Y}; do echo $f $(grep -o 'gcp\\.md' $f|wc -l) $(grep -o 'gcp-curriculum' $f|wc -l) $(grep -o 'unified-curriculum' $f|wc -l) $(grep -o '/Users/' $f|wc -l); done", DF,
  "Primer 58 gcp.md + 2 /Users/ paths and cyber 32 match. SQL has 38 gcp-curriculum (prompt: 3) and 4 unified-curriculum (prompt: 1): same conflict, larger count."),
 ("C-02", "SQL built on granular foreign parent", f"grep -o 'T\\.Disc\\|T\\.Algo\\|T\\.Quant\\|M\\.NS\\|T\\.SysTheory\\|12\\.S1[23]\\|9b\\.1\\|9c\\.[125]\\|8\\.1\\.5' {S} | sort | uniq -c", R, "All sampled foreign labels present."),
 ("C-03", "cyber uses same foreign numbering", f"grep -oE 'stitch: [^|]*' {Y} | grep -oE '\\b(0\\.4|1\\.2|2\\.3|3\\.0|3\\.4|4\\.[0-9]+|6\\.1[1-6]|7\\.[1-9]|8\\.1|9\\.[12]|9c(\\.2)?|10\\.[03])\\b' | sort | uniq -c | sort -rn | head -20", R, ""),
 ("C-04", "cyber stitches B4 for threat modeling", f"grep -n 'stitch: B4' {Y} | cut -c1-90", R, "PQ-S-06, TH-02, TH-03 at lines 177/197/206."),
 ("C-05", "DB-1…DB-10 owned by parent, exist nowhere", f"grep -c '^#\\+ DB-[0-9]' {S}; sed -n '151,162p' {S} | cut -c1-40; grep -n '^##### DB-' {G} | cut -c1-60", DF,
  "0 definitions in the inputs; SQL §2.2 (lines 147-162) gives only slice titles + pairings. The full slices are present in the original parent gcp-curriculum.md:3117-3178 (in repo, not in the input set). Port it, don't author it: see C-NEW-01."),
 ("C-06", "8.1 primitives missing", f"grep -n '^#### 8\\.1\\.[0-9]\\|^### 8\\.1 ' {G} | cut -c1-70", DF, "Missing from inputs; present in gcp-curriculum.md:5478-5615 (8.1.1-8.1.6). Note the original numbering differs from the prompt's N8.1.1-7 list: 8.1.5 = cursor pagination (matches); pool math/RLS/LSM/schema-evolution/idempotency sit in 8.1.6 'Other primitives'."),
 ("C-07", "other parent sections absent", f"grep -n '^### 0\\.4\\|^### 5\\.3\\|^### 8\\.0\\|^### 8\\.C\\|^### 9c\\.1\\|^## Part 11\\|^### Part 11b\\|^### 6\\.1[1-6]\\|^### 7\\.[1-9]' {G} | cut -c1-70", DF,
  "Absent from inputs, present in gcp-curriculum.md. The prompt's own C-07 rule says 'replace with original if gcp-curriculum.md … is supplied'. It is on disk."),
 ("C-08", "T.Disc/M.NS/T.SysTheory gates referenced", f"grep -n 'UG gate\\|grad gate\\|T\\.SysTheory' {S} | cut -c1-100", R, ""),
 ("C-09", "ID prefix collisions", f"for p in 'DD-0' 'DT-0' 'PR-0' 'Z0\\.' '^### E1\\.' '^### C1'; do echo \"$p $(grep -c \"$p\" {S}) $(grep -c \"$p\" {Y}) $(grep -c \"$p\" {D})\"; done", R, "cols: SQL cyber DP."),
 ("C-10", "cyber token corruption", f"grep -n 'ZB5\\|E1B5\\|EA5 TLS\\|gcp\\.md gcp\\.md\\|API auth patterns\\.3\\|§B5 IAM\\|principles principles' {Y} | cut -c1-80; awk 'NR>=2694' {Y} | grep -o '^[0-9]*\\.' | tr '\\n' ' '; grep -n 'Standalone Edition\\|End of' {Y} | cut -c1-70", DF,
  "All listed corruptions reproduce except 'see §B5 IAM' (0 hits). Extra: line 194 '- **Lab:** EA5 TLS / Phase 4 Armor' is a second E1.4 corruption; Appendix V numbering is 1-8,10,11,13 (skips 9 and 12)."),
 ("C-11", "nine phantom checkpoint IDs", f"for i in E-NT1 E-NT3 E-AU3 E-CL1 E-CL3 E-CK1 E-CK2 E-DD2 E-AB1; do echo $i $(grep -c \"$i\" {Y}) $(grep -c \"#### $i\" {Y}); done", R, "Each used once (§2), defined 0 times."),
 ("C-12", "VPC-SC cited as NT-07", f"grep -n 'VPC-SC exfil (NT-07)' {Y} | cut -c1-60; grep -n '^#### NT-0[67]' {Y} | cut -c1-60", R, ""),
 ("C-13", "WA-01 bound to A5 and A10", f"grep -n '^#### WA-01\\|WA-01 (HTTP attacker' {Y} | cut -c1-90", R, ""),
 ("C-14", "crypto placement contradiction", f"sed -n '436,441p' {Y} | cut -c1-120", R, ""),
 ("C-15", "DoS binding inconsistency", f"grep -n '^#### DD-0[1-8]' {Y} | cut -c1-90", R, ""),
 ("C-16", "DP binds everything to A7, gates ARCH-09…12 behind A9", f"sed -n '56,57p' {D} | cut -c1-160", R, ""),
 ("C-17", "'standalone' claim", f"grep -n -i 'standalone\\|does not depend' {Y} | cut -c1-100", R, ""),
 ("C-18", "A2/A4 rigour caveats", f"grep -n 'proof-level rigor\\|competitive-programming\\|red-black' {C} | cut -c1-80", R, ""),
 ("C-19", "Track G doesn't exist", f"grep -n 'Track G' {C} | cut -c1-40; grep -c '^G[0-9]\\|Track G' {C}", R, ""),
 ("C-20", "stale/time-bound text", f"grep -n 'right now\\|mid-2026\\|September 30\\|Sept 30\\|Dec 31' {C} | cut -c1-70", R, ""),
 ("C-21", "TLS split A5/A10 without rule", f"grep -n 'TLS' {C} | cut -c1-90", R, "A5 line 60 'ties into A10'; A10 line 87 'handshake in detail': no split rule."),
 ("C-22", "Part V categories as anchors", f"grep -o 'Part V[ —-]*[A-Z][A-Za-z/]*' {P} | sort | uniq -c", R, ""),
 ("C-23", "A5 checkpoints missing from ledger", f"grep -n 'P08 steps\\|E-NT1\\|CR-E12' {P} {Y} {L} | cut -c1-110", R, "Ledger has none of them."),
 ("C-24", "primer bindings disagree 26/40", "python3 ../refactor-tools/primer_bindings.py " + P + " | head -1", R, "26 of 40 header≠§2."),
 ("C-25", "23 PRIMARY-before-prereq violations", "python3 ../refactor-tools/primer_bindings.py " + P + " | grep -c VIOL", DF,
  "15 modules / 24 module-prerequisite pairs by a direct (non-transitive) earliest-binding check. Every example named in C-25 is flagged; C-26's SD-10 is only caught transitively (SD-10→SD-02→SD-01@A6)."),
 ("C-26", "SD-10@A5 needs SD-01@A6", f"grep -n '^#### SD-0[12] \\|^#### SD-10 ' {P} | cut -c1-110", R, "Transitive via SD-02."),
 ("C-27", "SD-26 header A5 needs SD-21@A8", f"grep -n '^#### SD-26\\|^| SD-26' {P} | cut -c1-110", R, ""),
 ("C-28", "SD-35 overlaps cyber, uses Prop-Locked props", f"sed -n '464,470p' {P} | grep -o 'VPC Service Controls\\|CMEK\\|Cloud Armor\\|mTLS\\|Web Security Scanner\\|SQLite' | sort -u", R, ""),
 ("C-29", "three 7-step session protocols", f"for f in {P} {S} {Y} {D}; do echo $f $(awk '/^### 0.3/{{f=1;next}} /^### 0.4/{{f=0}} f' $f | grep -c '^[0-9]\\+\\.'); done", R, "Design-patterns also has a 7-step §0.3: four protocols, not three."),
 ("C-30", "primer rule 6 'no separate tracker'", f"sed -n '25p' {P} | cut -c1-200", R, ""),
 ("C-31", "primer rule 9 'do not copy'", f"sed -n '28p' {P} | cut -c1-60; sed -n '1038p' {P} | cut -c1-120; grep -n -i 'do not copy\\|copy its contents' {P}", DF,
  "Primer rule 9 is 'Read economically'. No rule says 'do not copy its contents into other files' (0 hits). The nearest text is §7.2 item 10 (CC BY attribution). The C-31 resolution still makes sense as a new rule; record it as new content, not an amendment."),
 ("C-32", "two spines P08 vs Northstar", f"grep -c 'Northstar' {P} {S} {Y}; grep -n 'the spine' {P} | cut -c1-80", R, ""),
 ("C-33", "three P08 first-pass timings", f"sed -n '90,91p;686p' {P} | cut -c1-200; grep -o 'P08 first pass[^;]*' {P}", R, ""),
 ("C-34", "O-problem gates conflict", f"sed -n '92p' {P} | cut -c1-120; grep -n '^| \\*\\*O0[3-5]' {P} | cut -c1-110", R, ""),
 ("C-35", "SX early stitches vs 'taught with first problem'", f"sed -n '87,89p;623p' {P} | cut -c1-150", R, ""),
 ("C-36", "primer 'my addition' overlaps", f"grep -o -i 'my addition\\|my math' {P} | sort | uniq -c", R, "9 'my addition' + 2 'my math'."),
 ("C-37", "SQL SD-1…6 (35) vs primer SD-nn", f"grep -oP '(?<![\\w-])SD-[1-6](?![\\d\\w])' {S} | wc -l; grep -oP 'SD-\\d{{2}}[a-c]?' {S} | sort | uniq -c", R, "35 single-digit; two-digit refs SD-13/14/17/18/19/27/37."),
 ("C-38", "SD-38a/b/c sub-IDs", f"grep -o 'SD-38[a-c]' {P} | sort | uniq -c", R, ""),
 ("C-39", "gcp-labelled mermaid nodes/columns", f"grep -n 'gcp A[0-9]\\|gcp.md modules complete\\|gcp.md gate\\|Database Engineer domain' {P} | cut -c1-90", R, ""),
 ("C-40", "primer GCP details from Jan 2026 cutoff", f"grep -n 'cutoff January 2026' {P} | cut -c1-80", R, ""),
 ("C-41", "primer §7.3 maintenance rule", f"grep -n -A1 '^### 7.3' {P} | cut -c1-120", R, ""),
 ("C-42", "77 primer boxes all unticked", f"python3 ../refactor-tools/count_boxes.py {P}", R,
  "77 boxes (76 lines; line 686 has two: P08 first/second pass). 0 ticked. Corrected in R1: R0's first count (76+2) included a backticked `- [ ]` in rule 6 (line 25) as a box."),
 ("C-43", "SD-08 GCP lens not re-covered in DNS restart", f"grep -n 'SD-08' {L} | cut -c1-120", CO, "Chat-state claim. Ledger (dated 2026-09-21) records SD-08 as folded into A5; the restart it describes is not in any file."),
 ("C-44", "cert count 15 vs 18", f"grep -n -i 'fifteen\\|not all 8' {C} | cut -c1-70; awk 'NR>=207&&NR<=300' {C} | grep -c '^[0-9]*\\. '", R, "18 numbered cert entries (10 GCP + 5 AWS + 3 Azure)."),
 ("C-45", "no inline boxes in Curriculum", f"grep -c '\\[ \\]\\|\\[x\\]' {C}", R, ""),
 ("C-46", "no Lab Reality for Track D / per-cert", f"grep -n 'Lab Reality' {C} | cut -c1-40", R, "Only lines 14, 254, 280, 300 (per provider)."),
 ("C-47", "no teaching protocol in Curriculum", f"grep -c -i 'ten-rung\\|Prop Lock\\|Database protocol' {C}; grep -n 'ten-rung\\|Prop Lock' {G} | head -2 | cut -c1-70", DF, "Absent from Curriculum as stated, but the protocol exists in gcp-curriculum.md:198 (ten-rung) and :226 (Prop Lock). Port it."),
 ("C-48", "stale Part IX framing", f"sed -n '345,349p' {C} | cut -c1-80", R, ""),
 ("C-49", "A7 overloaded", f"grep -c 'A7' {P} {S} {Y} {D}", R, "Counts of A7 mentions per file (binding volume)."),
 ("C-50", "SQL lab kit not in any file", f"ls ../../sql-companion-work/ | tr '\\n' ' '", DF,
  "The kit is on disk at sde/sql-companion-work/: lab_schema.sql, lab_seed.sql, run_ex.py, plans.py, tx_tests.py, two.py, wrongs.py, goldens_*.json, naive/safe/slow_*.sql, BUILD_REPORT.md, plus a PG15 data dir. Goldens should be reproducible, not rebuilt. See C-NEW-02."),
 ("C-51", "E11/E12 declared, E12.1 undefined", f"grep -n 'E11\\|E12' {S} | cut -c1-110", R, ""),
 ("C-52", "runner table says P1–P11", f"grep -n 'P1–P11' {S} | cut -c1-80", R, ""),
 ("C-53", "other parent refs (G4, G12b, F1…, TB-/SRC-, protocols)", f"for t in G4 G12b F1 D0 TB- SRC- 'Lab safety' 'Database protocol' 'Teaching contract'; do echo \"$t $(grep -c -- \"$t\" {S})\"; done", R, "All present; G12b also exists in gcp-curriculum.md (8.1-G heading at :5616 covers G8-G9/G19; check G12b by grep in R2)."),
 ("C-54", "ten-rung ramp referenced but absent", f"grep -n 'ten-rung' {S} | cut -c1-80; grep -n 'Universal ten-rung' {G} | cut -c1-60", DF, "Absent from the inputs; present in gcp-curriculum.md:198."),
 ("C-55", "anchoring rules only in SQL", f"grep -c 'pre-rung-2\\|unanchored' {S} {Y} {P} {D}", R, ""),
 ("C-56", "golden env pins only in rule 7", f"sed -n '24p' {S} | cut -c1-200; grep -n 'timezone\\|collation\\|15\\.' ../../sql-companion-work/run_ex.py", R, "run_ex.py asserts none of the pins."),
 ("C-57", "SQL rule 8 points to parent ledger", f"grep -n 'Learner state' {S} | cut -c1-120", R, ""),
 ("C-58", "DP has one box for 63 items", f"python3 ../refactor-tools/count_boxes.py {D}", R, "0 real boxes. The only '[ ]' is a backticked mention in rule 6 (line 18). Resolution unchanged: add per-item boxes."),
 ("C-59", "ten ARCH modules lack Check", f"grep -n '^\\*\\*ARCH-\\|\\*\\*Check' {D} | sed -n '/ARCH-01/,$p' | cut -c1-40", DF, "No per-module Check under any ARCH item. The single §7 Check (line 363) follows ARCH-04 and reads as a shared integration check. So 11 (ARCH-01…03, 05…12) lack one; the prompt says 10, omitting ARCH-12."),
 ("C-60", "GoF quoting contradiction", f"grep -n \"GoF's own line\\|close paraphrases\\|(GoF)\" {D} | cut -c1-90", R, ""),
 ("C-61", "toy real-world examples", f"grep -n 'DocumentCreator' {D} | cut -c1-80", R, ""),
 ("C-62", "Repository defined twice", f"grep -n 'Repository' {D} | cut -c1-80", R, ""),
 ("C-63", "[C]/[S]/[B] tags collide", f"grep -o '\\[[CSB]\\]' {D} | sort | uniq -c", R, ""),
 ("C-64", "notation omits F-nn; parity gaps", f"sed -n '31p' {D} | cut -c1-120; grep -c -i 'GCP lens\\|Lens-1' {D}", R, ""),
 ("C-65", "DP dependency gate local", f"sed -n '/^## 10/,/^## 11/p' {D} | cut -c1-90", R, ""),
 ("C-66", "ledger is free text", f"grep -c '```yaml' {L}", R, ""),
 ("C-67", "two teaching errors in chat", f"grep -c -i 'CNAME' {L}", CO, "Chat-state claim (CNAME→IP exercise). Not in any file. Seed errata from the prompt's description, labelled as such."),
 ("C-68", "learner error pattern", f"grep -n 'call stack\\|centered\\|power of 9\\|authoritative server' {L} | cut -c1-80", DF, "3 of 4 examples are in ledger §2. 'returned to the OS by the authoritative server' is not in the ledger (chat-only)."),
 ("C-69", "multi-part checks asked in chat", "true", CO, "Chat-state claim."),
 ("C-70", "skill vs ledger §5", f"grep -n 'one calibrating question\\|a few sentences' {K} | cut -c1-80; grep -n 'background-probing\\|do not compress' {L} | cut -c1-80", R, ""),
 ("C-71", "no mastery model", f"grep -c -i 'shaky\\|mastered\\|unverified' {L}", R, ""),
 ("C-72", "no session-close protocol", f"grep -c -i 'delta\\|session close' {L}", R, ""),
 ("C-73", "stitch completeness not checked at close", "true", CO, "Process claim; motivated by C-43."),
 ("C-74", "no tutor accuracy standard", f"grep -c -i 'errata' {C} {L} {K}", R, ""),
 ("C-75", "uncoordinated override rules", f"grep -n -i 'can override\\|override anything' {P} {S} {Y} {D} | cut -c1-90", R, ""),
]

NEW = [
 ("C-NEW-01", "The foreign parent is available.", f"ls -la {G} ../../unified-curriculum.md | awk '{{print $5, $6, $7, $8, $9}}'; grep -c '' {G}",
  "gcp-curriculum.md (8,120 lines, 641 KB, modified 2026-09-22) and unified-curriculum.md are in the repo. The prompt assumes they are missing (C-05…C-07, C-47, C-53, C-54). Proposed default: port owner sections verbatim into northstar-reference-app.md / SQL §4.0 / Curriculum §0.4 with a provenance line, instead of reconstructing. Needs learner confirmation (open question Q1)."),
 ("C-NEW-02", "The SQL lab kit exists; the goldens are reproducible.", "ls ../../sql-companion-work/ | wc -l; head -5 ../../sql-companion-work/BUILD_REPORT.md",
  "C-50's rebuild step becomes verify-in-place: re-run run_ex.py against the existing seed and compare with the companion's §6 and Appendix K goldens. PostgreSQL 15 is at /Library/PostgreSQL/15."),
 ("C-NEW-03", "The ledger on disk is older than the state the prompt describes.", f"sed -n '2p;57,58p' {L} | cut -c1-160; grep -c 'NT-04\\|HttpOnly\\|cookie' {L}",
  "The ledger is dated 2026-09-21. Its open question is the 24-h TTL migration question; it has no NT-04 and no cookie question, and §1 lists 4 companions (no cyber). Invariant 3 says DNS is finished including NT-04, and that the HttpOnly/Domain cookie question is open. Rule: the prompt, as the learner's instruction, is treated as newer (ladder rung 1). Both open questions are preserved (Q2)."),
 ("C-NEW-04", "The Curriculum file is named gcp.md and has a spliced section.", f"sed -n '1p;93,105p' {C} | cut -c1-70",
  "`Curriculum` = sde/gcp.md (title 'The Consolidated Cloud Mastery Curriculum'). A cyber pointer section (lines 93-103) sits between A10 and A11 inside Part I; it was added on 2026-09-22 (gcp.md.pre-cyber-pointer diff). It should move to a companion-pointer block in §0 in R2 (move, not delete)."),
 ("C-NEW-05", "Curriculum has one heading, and it belongs to the spliced section.", f"grep -n '^#' {C}",
  "Its only markdown heading is line 95, from the spliced cyber section (C-NEW-04). Every native line is plain text, so the §8.1 'every heading' manifest item is empty for this file. Module lines like 'A5. Computer Networking' must be parsed by regex. R2 may add headings (anchor rewrite class)."),
 ("C-NEW-06", "The design-patterns file uses a 7-step §0.3 too.", f"awk '/^### 0.3/{{f=1;next}} /^### 0.4/{{f=0}} f' {D} | grep -c '^[0-9]'",
  "C-29 should say four session protocols, not three."),
 ("C-NEW-07", "The cyber companion has a 'Lab' line with a corrupted anchor.", f"grep -n 'Lab:\\*\\* EA5\\|Lab:\\*\\* E1B5\\|Lab:\\*\\* ZB5' {Y} | cut -c1-80",
  "Beyond the corrupted headings, the Lab: line at 194 repeats the EA5 corruption. The C-10 fix must cover references, not only headings."),
 ("C-NEW-08", "The corruption-scan regex has a false positive.", f"grep -oP '[A-Z][0-9]+[A-Z]' {C} {Y} | sort | uniq -c",
  "`A2A` (agent-to-agent protocol) matches the C-10 signature. It must be whitelisted in the R3 scan."),
 ("C-NEW-09", "Pseudo-anchor inventory is larger than the prompt lists.", f"grep -oE 'A10/B5\\.[0-9]+|A5/Phase4-Net\\.[0-9]+|Phase4-Sec\\.[0-9]+|A5 TLS / Phase 4 Armor' {Y} | wc -l; grep -oE 'A10/B5\\.[0-9]+|A5/Phase4-Net\\.[0-9]+|Phase4-Sec\\.[0-9]+|A5 TLS / Phase 4 Armor' {Y} | sort -u | wc -l",
  "90 pseudo-anchor tokens across 22 distinct forms. Each is rebound by crosswalk §6.2, not reverse-engineered (per C-10)."),
]


def run(cmd, cwd):
    p = subprocess.run(["bash", "-c", cmd], cwd=cwd, capture_output=True, text=True)
    return (p.stdout + p.stderr).strip()


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    cwd = os.path.join(root, "work")
    out = ["# R0 conflict reproduction", "",
           f"Generated by `refactor-tools/r0_reproduce.py` against `work/` (identical to `inputs-original/`). Re-run to refresh. Commands run with cwd=`work/`; `../../gcp-curriculum.md` is the original parent (not one of the 7 inputs).", "",
           "| ID | Claim | Status | Note |", "|---|---|---|---|"]
    detail = ["", "## Evidence (command → output)", ""]
    counts = {}
    for cid, claim, cmd, st, note in CHECKS:
        counts[st] = counts.get(st, 0) + 1
        out.append(f"| {cid} | {claim} | **{st}** | {note} |")
        o = run(cmd, cwd)
        detail += [f"### {cid}", "```bash", cmd, "```", "```", o[:1800] or "(no output)", "```", ""]
    out += ["", "## New conflicts found in R0 (C-NEW-nn)", "", "| ID | Finding | Note |", "|---|---|---|"]
    for cid, claim, cmd, note in NEW:
        out.append(f"| {cid} | {claim} | {note} |")
        o = run(cmd, cwd)
        detail += [f"### {cid}", "```bash", cmd, "```", "```", o[:1800] or "(no output)", "```", ""]
    summary = " · ".join(f"{k}: {v}" for k, v in sorted(counts.items()))
    out.insert(3, f"**Summary:** {len(CHECKS)} conflicts checked: {summary}. New: {len(NEW)}.\n")
    open(os.path.join(root, "r0-reproduction.md"), "w", encoding="utf-8").write("\n".join(out + detail) + "\n")
    print(summary, "| new:", len(NEW))


if __name__ == "__main__":
    main()
