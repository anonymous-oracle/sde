# Curriculum Timeline — Realistic Estimate at Sustainable Pace

Assumes ~10–15 focused hours/week, consistently sustained. These are *my* estimates,
not the curriculum's own (more optimistic) planning note — they account for the fact
that later stages involve real debugging, real infra, and real proofs, not just reading.

| Stage | Content | Estimated time | Risk notes |
|---|---|---|---|
| S0 | Zero setup — hardware, files, shell, Git, HTTP/JSON vocab | 1–2 weeks | Low risk — vocabulary, not skill-building |
| S1 | Python numerical base | 3–4 weeks | — |
| S2 | Go programming base | 3–4 weeks | — |
| S3 | Algebra and functions | 4–6 weeks | — |
| S4 | Proof, discrete math, basic DS | 6–8 weeks | Proof-writing is a new skill for most learners — can stall here |
| S5 | Geometry, coordinates, vectors | 3–4 weeks | — |
| S6 | Go types and core data structures | 5–6 weeks | — |
| S7 | Linear algebra and spectral methods | 8–10 weeks | **High risk** — gate demands residual/orthogonality/conditioning checks, not just right answers |
| S8 | Sorting, graphs, complexity | 6–8 weeks | — |
| S9 | Calculus and numerical methods | 8–10 weeks | **High risk** — multivariable calc + ODE + numerical stability in one stage |
| S10 | Probability, statistics, information theory | 8–10 weeks | **High risk** — MLE/MAP through bootstrap through entropy, gated by a real A/B analyzer |
| S11 | Classical ML from scratch | 8–10 weeks | Every model family implemented in NumPy, not sklearn-first |
| S12 | SQL and relational correctness | 4–5 weeks | — |
| S13 | Database internals | 6–8 weeks | Postgres internals down to WAL/MVCC — genuinely a "database systems course" |
| S14 | Optimization, RL, and causality | 8–10 weeks | **High risk** — three graduate-adjacent subfields in one stage |
| S15 | DSP, image processing, NLP, speech/ASR (incl. WFST/HCLG) | 14–18 weeks | **Highest risk** — this is a full DSP + CV + ASR specialization compressed into one stage |
| S16 | Deep learning and transformers | 10–12 weeks | Scratch MLP *and* scratch attention, both gradient-checked |
| S17 | IIT Kharagpur GenAI/RAG/Multimodal/Agents | 8–10 weeks | Folded in, not parallel — but still 5 named production systems to build |
| S18 | APIs and service contracts | 3–4 weeks | — |
| S19 | Go auth, security, middleware | 4–5 weeks | OAuth attack classes, ASVS-mapped tests |
| S20 | HLD/LLD, SOLID, clean architecture, distributed systems | 6–8 weeks | — |
| S21 | System-design and OOD labs | 8–10 weeks | Full six-step write-up + Go slice per problem, across 8 problem categories |
| S22 | Production ML systems and MLOps | 6–8 weeks | — |
| S23 | Nasiko capstone (Go control plane, P0–P10) | 10–14 weeks | Integration stage — bugs here often trace back to gaps in S7/S9/S13/S19/S20 |
| S24 | Optional specializations | Open-ended, skip by default | Only opened if a real need arises |

## Totals

- **Sum of midpoint estimates: ~170–175 weeks ≈ 3.3 years**, at a consistent 10–15 hrs/week.
- This is *before* accounting for the built-in review cadence: portfolio hardening every
  8–12 weeks, and interleaved spaced review every 4–12 weeks pulling you back to shore up
  weak prerequisites — both add real time on top of the table above.
- The four highest-risk stages (S7, S9, S10, S15) alone account for roughly 40–46 weeks —
  nearly a third of the whole program — and are the stages most likely to run over.

## Bottom line

24 months is achievable only if pace holds with minimal friction. A more realistic range,
given the depth this curriculum actually demands (not skimmed, but gated with real
implementations and adversarial checks), is **3 to 3.5 years** at a sustainable pace, or
**18–24 months** only at a genuinely intensive, low-interruption pace (20–25 hrs/week)
that most people can't sustain for that long without burnout.
