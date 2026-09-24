"""R2c: the Go Language Companion, the suite's sixth part (learner decision D12).

The learner asked for a rule to teach Go, its basic language rules and its differences from other languages, as a
new companion built from the Nasiko course notes (material only, D10) and tied into the other parts. Two steps:

  cur(f)            main-course edits, run right after r2b_cur.build so that every companion's contract copy
                    (made later by r2b_pri/sql/dp/sec) already carries rule 0.4.9: §0.1 six parts, §0.3 owner rows,
                    rule 0.4.2 layer order, rule 0.4.9, the A3 Go line.
  build(files, root) the companion itself from refactor/authored/go-language-companion.md (the markers @@PREFS@@
                    and @@CONTRACT@@ become the main course's §0.2 and §0.4 + §0.5 copies), plus the tie-ins in the
                    primer, SQL, design-patterns and cybersecurity companions. Run after the other per-file builds.

Every edit is journaled (rule IDs GO-n); the new file is journaled as one new-content insert.
"""
import os

from r2b_common import CUR, PRI, SQL, DPC, SEC, F
from r2b_shared import contract_copy

GOF = "go-language-companion.md"
EV = "D12: the learner asked for a Go companion (language rules and contrasts) tied into the other parts"


def cur(f):
    f.rep("GO-1", "anchor-rewrite", "This course is one course in five parts.", "This course is one course in six "
          "parts.", EV)
    f.ins_after("GO-2", "- **The Cloud Cybersecurity Companion** — security, attacks and cryptography.",
                ["- **The Go Language Companion — Syntax, Semantics, Runtime and Contrasts** — the implementation "
                 "language: Go's grammar, semantics, runtime and toolchain, each construct contrasted with Python, "
                 "Java, C and JavaScript. Its language core is the Go block of A3; its later modules bind where they "
                 "are first used (rule 0.4.9)."], EV)
    f.rep("GO-3", "anchor-rewrite", "inline `- [ ]` boxes of the five parts", "inline `- [ ]` boxes of the six parts",
          EV)
    # §0.3 register: owners for the Go material, and the Go additions to rows it touches
    f.rep("GO-4", "anchor-rewrite", "| Rate limiting | Cyber AB-01 (algorithms + abuse) | Primer Q22 is the design "
          "exercise and recalls AB-01 |", "| Rate limiting | Cyber AB-01 (algorithms + abuse) | Primer Q22 is the "
          "design exercise and recalls AB-01; Go companion GO-19 (`golang.org/x/time/rate`) |", EV)
    f.rep("GO-4", "anchor-rewrite", "| SQL injection / parameterisation | SQL SL-13 (the SQL mechanics) | Cyber WA-05 "
          "(attacker model across the whole injection family) |", "| SQL injection / parameterisation | SQL SL-13 "
          "(the SQL mechanics) | Cyber WA-05 (attacker model across the whole injection family); Go companion GO-22 "
          "(placeholders in `database/sql`) |", EV)
    f.rep("GO-4", "anchor-rewrite", "| Garbage collection | U4 (memory management) | Primer Q21 (design problem); "
          "SX-04 (data GC/TTL) |", "| Garbage collection | U4 (memory management) | Primer Q21 (design problem); "
          "SX-04 (data GC/TTL); Go companion GO-09 (Go's collector, `GOGC`, `GOMEMLIMIT`) |", EV)
    f.ins_after("GO-5", "| Real-world architecture papers (", [
        "| Go: language, toolchain, runtime | Go companion GO-01…GO-14 (the Go block of A3) | every Go lab in every "
        "part recalls it (rule 0.4.9); A3's Python block stays the first language |",
        "| Concurrency | U5 (theory; reserved) | Go companion GO-15…GO-19 (goroutines, channels, `context`, the Go "
        "memory model, the race detector); A9 (distributed theory) |",
        "| Data-structure implementations in code | A4 / U2 (concepts and costs) | Go companion GO-27 (the Go code); "
        "Primer O01, O02, O07 (the checkpoints) |",
        "| Design patterns in Go | Design-patterns companion (the patterns) | Go companion GO-11 (the Go shape: "
        "implicit interfaces, embedding, functional options, middleware, iterators) |",
        "| HTTP server timeouts against slow clients | Cyber DOS-05 (the attack and the values) | Go companion GO-21 "
        "(which `http.Server` field does what) |",
        "| Password hashing in a service | Cyber CR-13 (the KDFs) | Go companion GO-07 + GO-21 (CR-13's build lab "
        "written in Go) |"], EV)
    f.rep("GO-6", "anchor-rewrite", "3. **Layers**, in fixed order: system design (primer) → SQL/engine → patterns → "
          "attacker/crypto (cyber).", "3. **Layers**, in fixed order: system design (primer) → SQL/engine → patterns "
          "→ Go implementation (Go companion) → attacker/crypto (cyber).", EV)
    i = f.idx("**0.4.8 Pacing, checkpoints and session close.**")
    f.ins("GO-7", i + 1, [
        "",
        "**0.4.9 Implementation language: Go.** Go is the suite's language for application code: services, build labs "
        "that write a program, and capstones. Python stays the first language of A3, the language of Track D's "
        "machine-learning work, and the language of labs already written in Python (the SQL companion's lab kit, the "
        "\"Python twin\" that some labs name). Go is taught by the Go Language Companion: its language core (GO-01…GO-14) is "
        "the Go block of A3, and its later modules bind where they are first used. Three rules:",
        "",
        "1. **Syntax unlock** — rule 0.4.6 applied to code. A Go construct appears in an explanation, a lab or a "
        "check only once the GO module that unlocks it is at least `taught`; before that, the lab runs in Python or "
        "waits, and the construct is named only as \"we'll cover this in GO-nn\". The first use of each construct "
        "carries its unlock block: signature → semantics → runtime and memory → contrast with Python, Java, C or "
        "JavaScript, naming the bug the other habit causes in Go.",
        "2. **Lab acceptance** — Go lab code is accepted when `gofmt -l` prints nothing, `go vet ./...` is clean, "
        "the tests pass (under `go test -race` from GO-19 on; the race detector needs cgo), no error is silently "
        "dropped, and every goroutine the code starts has a way to be stopped.",
        "3. **Version honesty** — the baseline release is the one the learner's own module declares. A behaviour "
        "is taught as fact only when it has been run on the installed release; anything else carries `(verify)`. "
        "The go command downloads modules, and whole toolchains when a module's `go` line is newer than the "
        "installed release: name what a step will fetch before running it."], EV)
    f.ins_after("GO-8", "Git fundamentals (deep dive lives in A11)", [
        "Go, the implementation language of the suite's labs and services: the Go companion's GO-01…GO-14, after "
        "the Python block, in four teaching blocks — A3.G1 toolchain, packages, types and control flow · A3.G2 "
        "slices and maps, functions, errors, strings · A3.G3 pointers and memory, structs and methods, interfaces, "
        "generics · A3.G4 I/O, JSON, command-line programs and logging — every construct contrasted with Python "
        "(rule 0.4.9)"], EV)


def assemble(files, root):
    src = open(os.path.join(root, "authored", GOF), encoding="utf-8").read().split("\n")
    cur = files[CUR]
    h = cur.heading("0.2 Learner teaching preferences")
    prefs = cur.L[h:cur.section_end(h)]
    while prefs and prefs[-1].strip() == "":
        prefs.pop()
    prefs[0] = prefs[0].replace("### 0.2 ", "### 0.5 ")
    out = []
    for l in src:
        if l == "@@PREFS@@":
            out += prefs
        elif l == "@@CONTRACT@@":
            out += contract_copy(files, 5, 6)
        else:
            out.append(l)
    if any("@@" in l for l in out):
        raise SystemExit("r2c_go: an unreplaced marker is left in the Go companion")
    g = F(GOF, [])
    g.ins("GO-0", 0, out, EV + "; the whole file is new, authored for R2c, built from the main course's own rule "
          "text and the Nasiko notes as material only (D10)")
    return g


def build(files, root):
    files[PRI].ins_after("GO-10", "> **Note:** O01, O02 and O07 are A4 recall checkpoints (practice, not re-teaching).",
                         ["> **Note:** the checkpoints are also written in Go: O01, O02 and O07 once the Go Language "
                          "Companion's GO-27 is taught, O03–O06 once its GO-11 is (rule 0.4.9). The Python versions "
                          "stay; the Go ones add the Go shape (no inheritance, implicit interfaces)."], EV)
    files[SQL].rep("GO-11", "anchor-rewrite", "a `cursorpage` package (Python, then Go).", "a `cursorpage` package "
                   "(Python, then Go once the Go Language Companion's GO-22 is taught, rule 0.4.9).", EV)
    files[DPC].ins_after("GO-12", "| System-design-primer companion | DP-14 Observer ↔ SD-28 Pub/Sub;", [
        "| Go Language Companion | GO-11 renders the patterns in Go: PR-05 and PR-04 as small consumer-owned "
        "interfaces, F-03 as embedding (which delegates and never dispatches back), DP-04 as functional options, "
        "DP-12 and DP-18 as `http.Handler` middleware, DP-01 as `sync.Once`, DP-13 as a function type, DP-14 as "
        "channels, DP-20 as `iter.Seq` | This file owns the patterns; the Go companion owns only their Go shape. "
        "DP-15 Template Method cannot be built by overriding in Go |"], EV)
    files[SEC].rep("GO-13", "anchor-rewrite", "- **Build lab (hardened HTTP server):** on a Go `http.Server` set",
                   "- **Build lab (hardened HTTP server):** on a Go `http.Server` (the Go Language Companion's GO-21 "
                   "teaches which field does what) set", EV)
    files[SEC].rep("GO-14", "anchor-rewrite", "from a vetted library (argon2-cffi, `golang.org/x/crypto/argon2`), "
                   "with parameters", "from a vetted library (argon2-cffi, or `golang.org/x/crypto/argon2` once the "
                   "Go Language Companion's GO-07 and GO-21 are taught), with parameters", EV)
    return assemble(files, root)
