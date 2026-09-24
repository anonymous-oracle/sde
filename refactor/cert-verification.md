# Certification verification: all 18 retained (decision D4)

Verified 2026-09-24 against the vendors' live pages and exam guides. Third-party sites were not used as evidence.

**Rule (D3/D4): no Curriculum line is removed.** Where a line is outdated, R2 adds a dated `Verified 2026-09-24:` note directly under it. The original line stays word for word. The count "Fifteen" (lines 6 and 27) becomes "eighteen". That is the only in-place wording change, and it is logged as a factual correction.

## Summary

| # | Certification (Curriculum wording) | Code | Status on 2026-09-24 | Curriculum claims | Result |
|---|---|---|---|---|---|
| G1 | Professional Cloud Architect (PCA) | — | Active | 50 questions / 2 h / 4 case studies; domain weights 24/15/20/18/11/12 "(verified)" | **Differs.** 50–60 questions; 4 case studies are published, 2 appear per exam. The live guide's weights are 25 / 17.5 / 17.5 / 15 / 12.5 / 12.5, under different section names. |
| G2 | Professional Machine Learning Engineer | — | Active; guide revised | 6 domains; Vertex AI tooling | **Differs.** It is still 6 sections, but they were renamed (low-code AI 13, data & models 16, scaling prototypes 21, serving 20, pipelines 18, monitoring 13). The exam moved from Vertex AI to the **Gemini Enterprise Agent Platform**. |
| G3 | Data Engineer | — | Active (branding update pending) | topic list | OK |
| G4 | Cloud Developer | — | Active (page live, registration open) | topic list | OK. It is missing from the certification index page's rendered list, but its own page is live. |
| G5 | Cloud DevOps Engineer | — | Active | topic list | OK |
| G6 | Cloud Security Engineer | — | Active | topic list | OK |
| G7 | Cloud Network Engineer | — | Active | topic list | OK |
| G8 | Cloud Database Engineer | — | Active (branding update pending) | topic list | OK. Guide: design ~32%, manage ~25%, migrate ~23%, deploy ~20%. |
| G9 | Security Operations Engineer | — | Active | "newer cert" | OK. 6 sections: platform ops 14, data mgmt 14, threat hunting 19, detection engineering 22, IR 21, observability 10. |
| G10 | Agentic Architect (Beta → GA) | — | **Beta, open until Sept 30, 2026** | two-part (MC + labs in Google Skills); ~5 sections; ~⅓ agent code; ADK, Agent Registry, Agent Gateway, A2A | **Mostly confirmed.** 3 h, ~80 MC questions, then labs in Google Skills. 5 sections, with custom agents at ~33%. The guide names ADK, A2A and **MCP**; it does **not** name "Agent Registry" or "Agent Gateway". |
| A1 | Solutions Architect – Professional | SAP-C02 | **Being replaced** | 4 domains 26/29/25/20 | Weights confirmed. **New:** SAP-C03 registration opens **Oct 27, 2026**, and the last day for SAP-C02 is **Nov 17, 2026**. |
| A2 | DevOps Engineer – Professional | DOP-C02 | Active (Korean retired after Dec 31, 2026) | ~6 domains | Confirmed: 22/17/15/15/14/17. |
| A3 | Generative AI Developer – Professional | AIP-C01 | Active | topic list | Confirmed exists. 5 domains: FM integration & data 31, implementation 26, AI safety/governance 20, efficiency 12, testing 11. |
| A4 | Security – Specialty | SCS-C03 | Active (SCS-C02 retired Dec 1, 2025) | IAM 20, Data Protection 18, Infra 18, Detection 16, IR 14, "Management & Security Governance" | Weights confirmed. The last domain is actually named **"Security Foundations and Governance" (14%)**. |
| A5 | Advanced Networking – Specialty | ANS-C01 | **Retiring Dec 31, 2026** | last day Dec 31, 2026; no successor | **Confirmed.** AWS: no new certifications are issued after retirement. Domains 30/26/20/24. |
| Z1 | Azure Solutions Architect Expert | AZ-305 | Active | English version updated April 17, 2026; needs AZ-104 | **Confirmed.** Skills as of Apr 17, 2026; prerequisite is Azure Administrator Associate. |
| Z2 | DevOps Engineer Expert | AZ-400 | Active | needs AZ-104 or AZ-204 | Confirmed. **New:** skills revised as of **July 27, 2026**. Build/release pipelines is 50–55%. |
| Z3 | Cybersecurity Architect Expert | SC-100 | Active | updated July 28, 2026; needs AZ-500/SC-200/SC-300 | **Differs.** The study guide now shows skills measured **as of Oct 21, 2026** (an upcoming revision). The AZ-500 prerequisite is now listed as **"Cloud and AI Security Engineer Associate"**. |

**Count:** 10 GCP + 5 AWS + 3 Azure = **18**, all real and all currently registrable. Two have an announced end date: SAP-C02 (Nov 17, 2026, succeeded by SAP-C03) and ANS-C01 (Dec 31, 2026, no successor).

## Items for the volatility register (R4+)

These are outside the certification scope, but I noticed them:
- AWS Lab Reality (Curriculum line ~269) describes the old 12-month free tier. New AWS accounts since July 2025 get a credit-based free plan instead (`(verify)`).
- GCP page: "new customers get $300 in free credits" is confirmed.

## Sources

- Google Cloud certification pages: `cloud.google.com/learn/certification/{cloud-architect, machine-learning-engineer, data-engineer, cloud-developer, cloud-devops-engineer, cloud-security-engineer, cloud-network-engineer, cloud-database-engineer, security-operations-engineer, agentic-architect}`
- Google exam guides: `services.google.com/fh/files/misc/professional_{cloud_architect, agentic_architect, machine_learning_engineer…_new, security_operations_engineer, cloud_database_engineer}_exam_guide_english.pdf`
- AWS certification pages: `aws.amazon.com/certification/certified-{solutions-architect-professional, devops-engineer-professional, generative-ai-developer-professional, security-specialty, advanced-networking-specialty}/`
- AWS exam guides: `docs.aws.amazon.com/aws-certification/latest/{solutions-architect-professional-02, devops-engineer-professional-02, ai-professional-01, security-specialty-03, advanced-networking-specialty-01}/`
- Microsoft certification pages: `learn.microsoft.com/en-us/credentials/certifications/{azure-solutions-architect, devops-engineer, cybersecurity-architect-expert}/`
- Microsoft study guides: `learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/{az-305, az-400, sc-100}`
