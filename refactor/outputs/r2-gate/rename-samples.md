# R2 rename dry run — 20 sampled before/after lines

Judgment-based rules (RISKY list) are sampled first, then the rest round-robin across files (deterministic hash order); a line that exercises several rules covers them all. Long lines are cut to the changed region.

**1. system-design-primer-companion.md:676** (SDP-01)

```text
- | **Q20** | Online multiplayer card game | T5 | SD-30/31, SD-28, SD-05, O04 | authoritative server, tur…
+ | **Q20** | Online multiplayer card game | SDP-T5 | SD-30/31, SD-28, SD-05, O04 | authoritative server, tur…
```

**2. sql-databases-companion.md:158** (SQL-03)

```text
- | **DB-6** indexes | CS-02, CS-10 · TD-10 | E12-style workflow (§7.1) | PX-1 … PX-6, PX-9 |
+ | **DB-6** indexes | CS-02, CS-10 · TD-10 | PX-style workflow (§7.1) | PX-1 … PX-6, PX-9 |
```

**3. sql-databases-companion.md:161** (SQL-02, SQL-06)

```text
- … **DB-9** MVCC, locks, vacuum | CS-05 · TD-8, TD-9, TD-15 | E9.6 (batching), E11 labs | TX-1 … TX-7 |
+ … **DB-9** MVCC, locks, vacuum | CS-05 · TD-8, TD-9, TD-15 | SQL-E9.6 (batching), TX labs | TX-1 … TX-7 |
```

**4. sql-databases-companion.md:329** (SQL-16)

```text
- #### RT-03 · Tuple/domain calculus & safety (grad) — stitch: T.SysTheory · DB-3
+ #### RT-03 · Tuple/domain calculus & safety (SQL-T-GR) — stitch: T.SysTheory · DB-3
```

**5. sql-databases-companion.md:392** (SQL-07)

```text
- - **Lab:** E1 warm-ups: predict column visibility errors before running…
+ - **Lab:** SQL-E1 warm-ups: predict column visibility errors before running…
```

**6. sql-databases-companion.md:741** (SQL-04)

```text
- …: BQ partition expiration as the analytics cousin. Lens-2: SD-5 retention sketch.
+ …: BQ partition expiration as the analytics cousin. Lens-2: SCH-5 retention sketch.
```

**7. sql-databases-companion.md:836** (SQL-06, SQL-12)

```text
- | **S12-C** Aggregation & subqueries | Clean GROUP BY + EXISTS | E2.5, E4.5 | SL-05, SL-06 |
+ | **SQL-SKIP-SQL-C** Aggregation & subqueries | Clean GROUP BY + EXISTS | SQL-E2.5, SQL-E4.5 | SL-05, SL-06 |
```

**8. sql-databases-companion.md:1331** (SQL-01)

```text
- …dex on `(user_id, placed_at)` makes it a seq scan per user (E12.1).
+ …dex on `(user_id, placed_at)` makes it a seq scan per user (PX-1).
```

**9. sql-databases-companion.md:1833** (SQL-09)

```text
- #### C4 · Explain and fix the slow query
+ #### SQL-CAP4 · Explain and fix the slow query
```

**10. sql-databases-companion.md:1868** (SQL-17)

```text
- - **Tags:** P4
+ - **Tags:** PX-4
```

**11. sql-databases-companion.md:2165** (SQL-18)

```text
- …node types and row estimates, then run the matching `show("P…")` block. Change **one** variable between predictions (ind…
+ …node types and row estimates, then run the matching `show("PX-…")` block. Change **one** variable between predictions (ind…
```

**12. design-patterns-companion.md:31** (DP-01, DP-02, DP-03)

```text
- … styles/DDD/enterprise patterns · `AP-nn` anti-patterns. `[C]` = Creational, `[S]` = Structural, `[B]` = Behavioral (GoF's own three categories).
+ … styles/DDD/enterprise patterns · `AP-nn` anti-patterns. `[Cr]` = Creational, `[St]` = Structural, `[Bh]` = Behavioral (GoF's own three categories).
```

**13. cloud-cybersecurity-companion.md:62** (SEC-02)

```text
- | Berkeley CS161 | CR foundations, NT, DD, WA, AU |
+ | Berkeley CS161 | CR foundations, NT, DOS, WA, AU |
```

**14. cloud-cybersecurity-companion.md:88** (SEC-11)

```text
- | Exercises & capstones | scenario bank + C1–C4 | §5–§6 |
+ | Exercises & capstones | scenario bank + SEC-CAP1–SEC-CAP4 | §5–§6 |
```

**15. cloud-cybersecurity-companion.md:194** (SEC-00c)

```text
- - **Lab:** EA5 TLS / Phase 4 Armor
+ - **Lab:** SEC-E1.4
```

**16. cloud-cybersecurity-companion.md:1201** (SEC-06)

```text
- #### AI-05 · Shadow AI & sensitive paste — stitch: 9c · PR
+ #### AI-05 · Shadow AI & sensitive paste — stitch: 9c · PV
```

**17. cloud-cybersecurity-companion.md:1315** (SEC-12)

```text
- | **T3** | Auth attacks | Distinguish hijack vs fixation; CSRF r…
+ | **SEC-T3** | Auth attacks | Distinguish hijack vs fixation; CSRF r…
```

**18. cloud-cybersecurity-companion.md:1361** (SEC-00b)

```text
- #### ZB5 IAM · L0 · Shared responsibility quiz
+ #### SEC-Z0.5 · L0 · Shared responsibility quiz
```

**19. cloud-cybersecurity-companion.md:2453** (SEC-00a)

```text
- #### E1B5 IAM · L8 · Indirect prompt injection → refund tool
+ #### SEC-E10.5 · L8 · Indirect prompt injection → refund tool
```

**20. cloud-cybersecurity-companion.md:2644** (SEC-08, SEC-10)

```text
- ### K-extra (E9 / CR-E29+ / Z0.7+)
+ ### K-extra (SEC-E9 / CR-E29+ / SEC-Z0.7+)
```
