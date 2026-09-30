# Tutor Corrections, Root Causes and Permanent Fixes
GCP Cloud Mastery, session of 2026-09-30 (A5 Computer Networking: DNS migration, DOS-02, NT-03)

**What this file is.** Every correction the learner gave the tutor in this session, with the root cause, what the course files say, and a fix that makes the tutor stop repeating it. It closes with a ledger delta (COURSE-GUIDE rule 0.4.8). Give this file back at the start of the next session; COURSE-GUIDE §1 says the ledger is carried as a block the learner keeps.

**Sources checked:** `COURSE-GUIDE.md` (rules 0.2, 0.4.1, 0.4.2, 0.4.6, 0.4.7, 0.4.8, 0.4.11, 0.5.4), `learn-SKILL.md`, `cloud-cybersecurity-companion.md` (DOS-02, NT-03, NT-04), and the uploaded `session-progress-ledger.md`.

**Priority order when instructions conflict (rule 0.4):** (1) the learner's explicit instruction in the current chat, (2) learner preferences (rule 0.2), (3) main course, (4) owning part, (5) companion defaults. Most of the corrections below come from a default at level 3 to 5 beating an instruction at level 1.

---

## 1. The corrections at a glance

| ID | What the learner said (verbatim) | Root cause | Permanent fix |
|---|---|---|---|
| C1 | "Ensure thorough curriculum coverage and academic rigour while maintaining learn skill based short turn lengths." Repeated later: "I hope you are ensuring..." | The tutor treated rigour and brevity as a trade-off and resolved it by making turns long and dense. Rule 0.4.1's "a turn may be as long as one concept needs" gave cover. | Split each concept into short blocks. Rigour lives in the number of blocks, not the length of a turn. Show a one-line coverage strip (section 4). |
| C2 | "use fenced text blocks to explain concepts using diagrams", then later "Drop the usage of text based diagrams. It is confusing." | The preference changed and was never written down, so the tutor followed whichever message it had last seen. | Record the later instruction as binding. Tables and short prose only; fenced blocks for commands and code only. |
| C3 | "Never assume I know something beforehand." (after "Cloud NAT logs" appeared undefined) | Breach of rule 0.4.6 (anchoring). The tutor used terms because the learner answered quickly and looked fluent. | A term gate: no term unless anchored, else a one-line definition first. Section 7 lists terms to re-anchor. |
| C4 | "teach me how to write these gcp commands myself. You handing it out to me does not help. For every topic going forward, if it involved gcp, teach me the relevant commands." | Lens-1 in rule 0.4.11.1 says "shows one `gcloud` line", so the tutor handed commands out. That default sits below the learner's instruction. | Command-construction pattern (section 4, item 9): teach the grammar, the learner builds the command with `--help`, the tutor confirms. |
| C5 | "Explain that gcp mapping defenses better." | The GCP lens was a three-bullet tail after the concept. | A fixed lens template: layer, resource, what it does, limit, console path, command to build, Lens-W question. |
| C6 | "try to map every valid/related concept with GCP and teach it hands on" | The 2026-09-29 hands-on brief (rule 0.2) was not applied retroactively to earlier A5 topics, and not to the DNS TTL migration. | A retro-lens backlog (section 6) taught inside recall turns. |
| C7 | "still not able to get what's the difference between a normal victim IP on an internet and what's different here", then "So when you say victim, it is the dns resolver?" | Three lapses: the roles (attacker, reflector, victim) were never stated; "victim" was used loosely; and the same open check was re-asked four times while the learner was stuck on the layer below it. | Actor table before any attack scenario, a stuck detector, and a rule never to re-ask an unanswered check word for word. |
| C8 | "wait, how did the c2VjcmV0...evil-example.com go out of the VM in the first place? ... how does he know about the ... part?" | The scenario started mid-story. The attacker's starting position and what he already held were never stated. | Scenario preamble (section 4, item 4). |
| C9 | (Not a verbal correction.) Eleven wrong or imprecise answers, listed in the register (section 6). | No misconception register was running, so each error was corrected once and then forgotten. | Register with retirement rule (0.4.5): two consecutive correct answers. |

---

## 2. Detail and what the files say

**C1. Short turns plus rigour.**
- `learn-SKILL.md`: "Keep turns short: a few sentences and one question, not a paragraph with a question tacked on." It also warns that "a diagram on every turn is decoration".
- Rule 0.4.8 says an over-budget module is split into teaching blocks, and that the budget is "never a reason to compress depth". So the files already contain the reconciliation the tutor missed.
- Fix: a concept takes several short turns (anchor, mechanism, GCP mapping, check). Target about 120 to 200 words of teaching plus one table or one worked example. If it needs more, say "part 1 of 2" and stop. Nothing is dropped; the why arrives in the next block.

**C2. Diagram format.**
- Rule 0.4 gives the current chat's latest instruction priority. "Drop text diagrams" replaces the earlier request.
- Fix: record "no text-drawn diagrams" in rule 0.2 (section 5). Use tables for comparisons, numbered steps for procedures, prose for mechanism.

**C3. Terms used before they were taught.**
- Rule 0.4.6: no term is used in an explanation, example or check unless anchored, meaning taught this session or at least `taught` on the ledger. Otherwise label it "we'll cover this in X".
- Terms used without anchoring this session are in section 7.
- Fix: before sending, scan the draft for every technical noun. For each, ask whether it is on the ledger as taught. If not, define it in one line or remove it.

**C4 and C5. GCP commands and the GCP lens.**
- Rule 0.4.11.1 (Lens-1 shows "one `gcloud` line"), rule 0.2 (hands-on brief of 2026-09-29), and the learner's new instruction (write the commands yourself) conflict. The learner's instruction wins.
- Fix: the lens template below, and for every GCP topic the learner builds the command.

**C6. Hands-on for every concept.**
- Rule 0.2: each concept with an honest GCP counterpart is done hands on "in the learner's own project", and each mapping says where to look in the workplace account (Lens-W, read-only, rule 0.5.4).
- Not yet done: no project has been named, so no Lens-2 build has happened. Open item: ask the learner once which project is theirs or employer-sanctioned for learning, and record it.

**C7. The victim confusion and the repeated check.**
- Rule 0.4.1: "give a foothold when the learner is genuinely stuck". Rule 0.2: "stop when it is understood".
- Root cause in detail: the open NT-03 question was re-asked four times with the same wording. The learner's replies showed they were still on DOS-02, so they were answering a different question each time.
- Fix: stuck detector. If a reply does not answer the open check, treat the reply itself as the learner's question, answer it first, and park the old check on the ledger. Re-ask a parked check once, reworded and smaller, and only after the layer beneath it is settled.

**C8. Missing scenario preamble.** For every attack module (DOS, NT, CL and similar) the tutor states who the attacker is, where they start, what they already hold, what they want, and what the defender controls. NT-03 begins after compromise; that was never said.

---

## 3. The tutor's own lapses (found in a self-audit, not raised by the learner)

| ID | Lapse | Rule broken | Fix |
|---|---|---|---|
| E1 | Checks with two or three asks ("Give me the command and the `--help` path", "restate the unit, then say who is billed", "yes or no, and which row it re-opens") | 0.4.7: one thing per check; split multi-part checks across turns | Test each check: does it contain "and", "then" or a second question mark? If so, split it. |
| E2 | Answered the learner's check in the same turn ("DOS-02's check is now fully answered: ... because UDP has no handshake") | 0.4.7: never answered by the tutor in the same turn | After the learner answers, confirm and sharpen only. Do not add the model answer. |
| E3 | The learner pasted a workplace firewall rule name and its contents, and the tutor said "harmless this time" | 0.5.4: no workplace resource names in a prompt | Design Lens-W questions as yes/no or a count. If output is pasted, say plainly that the rule says not to, without a "this time" exemption. |
| E4 | Named VPC Service Controls as a DNS-tunnel defence | 0.4.7: precision; rule 0.4.8 requires an open erratum | Already corrected in-session; logged in section 6. |
| E5 | Figures stated from memory with no `(verify)` flag: DNS amplification of 28 to 54x (attributed to US-CERT), memcached at tens of thousands of times, the 1.35 Tbps attack on GitHub in February 2018, "scan all IPv4 in under an hour", "tens of millions of open resolvers around 2013" | 0.4.11.4 honesty flags; 0.4.12.4 "never presents a recalled detail as current" | Mark each `(verify)` and check against a primary source before it is relied on. |
| E6 | Promised DOS-02, NT-03 and NT-04 for the DNS topic, but NT-04 has not been taught | 0.4.8 (1): nothing left unmarked | Scheduled as the next item (section 6). |
| E7 | No GCP lens for the TTL migration itself or for earlier A5 topics | 0.4.11.1: the lens comes "the moment it is taught" | Retro-lens backlog in section 6. |
| E8 | Session-close protocol not run | 0.4.8 | Section 6 is the delta. |

---

## 4. Per-turn pre-flight (the mechanical checklist)

Run this before every reply. It replaces the learner having to repeat corrections.

1. **Coverage strip (one line).** The module's bound IDs with state, for example `A5 DNS: [x] TTL migration [x] DOS-02 [ ] NT-03 (in progress) [ ] NT-04`. Shown at the start of each new concept and at close, so the learner never has to ask whether coverage is being kept.
2. **Length.** One concept per turn, about 120 to 200 words of teaching plus at most one table or worked example. Split if longer.
3. **Format.** No text-drawn diagrams. Tables, numbered steps and prose. Fenced blocks only for commands and code.
4. **Scenario preamble (attack modules).** A table of the roles (attacker, reflector or carrier, victim or target), the attacker's starting position, what they hold, what they want, and what the defender controls.
5. **Term gate.** Every technical noun is anchored on the ledger or defined in one line (rule 0.4.6).
6. **One check.** Exactly one ask, answerable from what has been taught, with the expected answer and one expected wrong answer written down first (rule 0.4.7). If a Lens-W question is also due, it is either the turn's single check or waits for its own turn.
7. **Stuck detector.** If the last reply did not answer the open check, answer the learner's actual question first. Never re-ask a check verbatim; reword and shrink it.
8. **Corrections.** Confirm the correct part, then sharpen the imprecise part with the mechanism (rule 0.4.1). Never answer the check for the learner.
9. **GCP lens template.**
   - A table: layer, GCP resource, what it does here, its limit.
   - The console path.
   - The command grammar (product, resource group, verb, name, flags) and the `--help` path to find the command.
   - The learner builds the command; the tutor confirms or corrects.
   - One Lens-W question, read-only, answerable yes/no or as a number.
   - Or one line saying there is no honest GCP counterpart.
10. **Workplace safety (0.5.4).** Read verbs only (`list`, `describe`, `get-iam-policy`). `gcloud config list` first. No names or output pasted in chat. Anything that creates or changes goes in the learner's named own project only.
11. **Numbers.** Compute with units: decimal (KB, MB) versus binary (KiB, MiB), as taught in A1.
12. **Claims.** Anything recalled, not checked, carries `(verify)`.
13. **Close.** Mark every bound ID, update mastery states and the misconception register, add errata, emit the ledger delta, and name the resume point and open questions verbatim (0.4.8).

---

## 5. Proposed additions to COURSE-GUIDE rule 0.2 (paste-ready)

- **Short turns, full rigour** (the learner's instruction, 2026-09-30, repeated): a concept is taught across several short turns; rigour is kept by never dropping the "why", not by lengthening a turn. A one-line coverage strip shows what is covered and what is pending.
- **No text-drawn diagrams** (the learner's instruction, 2026-09-30; supersedes the earlier request for fenced text diagrams). Use tables, numbered steps and prose. Fenced blocks are for commands and code only.
- **Never assume prior knowledge of a term** (2026-09-30). Every technical term is defined in one line the first time it appears, unless it is `taught` on the ledger.
- **The learner writes the GCP commands** (2026-09-30). For every GCP topic the tutor teaches the command grammar and the `--help` path; the learner builds the command. The tutor confirms. This overrides "Lens-1 shows one `gcloud` line" (rule 0.4.11.1).
- **GCP lens detail** (2026-09-30): the lens is a full table (layer, resource, function, limit), the console path, the command to build, and one read-only Lens-W question, not a tail note.
- **Attack modules open with an actor table** and the attacker's starting position.
- **A parked check is never re-asked verbatim.** An unanswered check is reworded and shrunk, and only after the layer beneath it is settled.

---

## 6. Ledger delta, session of 2026-09-30

**Mastery states**

| ID | State | Note |
|---|---|---|
| A5 DNS TTL migration (procedure) | taught | Learner gave the correct order (lower TTL, wait the old TTL, switch), the 299 s residual, and the traffic-watching idea. Drain and the full nine-step procedure were taught by the tutor. |
| DOS-02 amplification and reflection | taught | See M2 to M4 and M8. The unit restatement is still owed. |
| NT-03 egress exfil and DNS tunnelling | in-progress | Mechanism taught. Check answered 2 of 3 (see M9). The command check is open. |
| Cloud NAT (definition, logs) | taught | The command check is open. |
| NT-04 BGP and DNS threats (DNSSEC, SPF/DKIM/DMARC) | not-started | Next item. Stitched to A5 DNS. |
| A5 HTTP/HTTPS, TLS, NAT/firewalls/proxies, load balancing, VPN | not-started | Read each companion's §2 stitch table at the topic; DOS-01 (LB), DOS-05 (HTTP recall), NT-05 (VPN) and GO-21 (HTTP) are known to bind here. |

**Misconception register** (retire after two consecutive correct answers, rule 0.4.5)

| ID | Learner's answer | Correct mechanism | Status |
|---|---|---|---|
| M1 | "the client" caches DNS | The resolver caches; some apps have their own caches | active (1 wrong) |
| M2 | A TCP server "does not reply" to an uninitiated connection | It replies with a SYN-ACK to the forged source; the handshake fails because the forger never sees the sequence number | active |
| M3 | "control (a)", fix by "changing UDP to TCP" | The attacker picks the protocol; the owner controls who the server answers | active |
| M4 | "TCP for everything else" in the firewall | Allow udp/53 and tcp/53 from the range; everything else is denied by the implied rule | active |
| M5 | The VPC firewall is at the "gateway router" | It is enforced per VM, on the virtual network card | active |
| M6 | Cloud NAT translates an external IP to the internal one | One-to-one NAT is built into the external IP; Cloud NAT is a separate, outbound-only service | active |
| M7 | The "victim" is the DNS resolver | The resolver is the reflector; the victim is a third party | active |
| M8 | "even if the firewall allows it, the damage is minimal" | True only when the allowed source range is the VPC's own range | active |
| M9 | "increase in cache size" as a tunnel signal | The cache hit rate falls near zero; Cloud DNS logs show names, not cache size | active |
| M10 | "~2930 MB" for 3,000,000 bytes | 2,930 is KiB. The figure is about 3 MB, or about 2.9 MiB (A1 recall) | active |
| M11 | No DNS logging means "no way to detect anomalies" | No query-level detection; flow and NAT logs still give coarser signals | active |

**Errata:** E3 (workplace output pasted), E4 (VPC-SC is not a DNS-tunnel control), E5 (unflagged figures, `(verify)`), E6 (NT-04 untaught), E7 (no retro-lens).

**Overrides and preferences recorded:** short turns with full rigour; no text diagrams; never assume known terms; the learner writes GCP commands; every concept mapped to GCP hands-on.

**Retro-lens backlog (A5 topics already taught, to be done in recall turns; the learner builds each command using `--help`)**

| Topic taught | GCP counterpart to map |
|---|---|
| CIDR, subnetting, VLSM | VPC networks and subnets, including custom and auto mode |
| Routing, default gateway | VPC routes |
| OSI, L4 vs L7 | Cloud Load Balancing types (proxy vs passthrough) |
| TCP vs UDP | Passthrough vs proxy load balancers, Cloud Run's UDP limit |
| DNS, TTL migration | Cloud DNS zones and record sets; changing a TTL |
| Firewalls and implied rules | VPC firewall rules and their priorities |

**Open questions, verbatim and one per turn from here**
1. "Using `--help` only, find the command that lists Cloud DNS **response policies**. Give me the exact command and the `--help` path you followed." (Not yet answered.)
2. "Using `--help` only, as before, work out the command that lists the Cloud NAT gateways on one router." (Not yet answered; workplace answer is yes/no only.)
3. "Restate the victim's received data in the right unit." (Owed.)
4. Which GCP project is the learner's own, or employer-sanctioned for learning? (Needed before any Lens-2 build.)

**Resume point:** A5 Computer Networking, DNS topic. Close NT-03 (the two command checks above, one per turn), then teach NT-04 (DNSSEC, SPF/DKIM/DMARC, dangling records), then move on to HTTP/HTTPS with its stitched modules.

---

## 7. Terms used without anchoring (re-anchor each in one line, in recall turns)

RFC 1918 (private address ranges), bogon, ZMap, response rate limiting, base64, NXDOMAIN, entropy (of a label), ingress and egress, network interface card (NIC), SYN-ACK and sequence number, Cloud Router, VPC Flow Logs, log-based metric, response policy, metadata server, connection pool (taught in SD-30, confirm), drain, HTTP/2 GOAWAY, `Connection: close`.
