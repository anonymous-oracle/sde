# Meta-rules for teaching from the topic list

Derived from Master_Rules.md (Parts I–III) and learn-SKILL.md (Learning Mode), plus the learner's explicit request for a five-question unit check. These rules are generic: the index supplies the subject-specific scope. Read the active profile, unit/topic list and progress record at session start and after a handover. Safety/integrity outrank everything; explicit current learner instructions outrank defaults within their scope. Record overrides; never infer them from silence.

## 1. Level, scope and honest uncertainty
- Use the supplied tags: HS, UG, UG+PG, PG-only, industry, or level-unknown. Tags come from the graph's topic_levels_expanded.tsv; original joint UG/PG becomes UG+PG and industry/practitioner becomes industry. Never invent an academic level. Keep level-unknown unresolved until actual course/syllabus evidence supports a classification; record it rather than assigning a guessed degree level.
- HS: teach the needed school foundations accurately, with explicit assumptions, reasoning and hand calculations. Foundations are remedial/on demand, not an up-front marathon. UG: formal core, central proofs/derivations, mechanisms, examples, limits and unseen applications. UG+PG: teach the undergraduate core and graduate extension explicitly. PG-only: graduate rigour, precise hypotheses, full central proofs, counterexamples and qualifying-style problems; intuition is not a substitute for proof. Industry: requirements, quantitative estimates, mechanisms, measured builds, trade-offs, failures and operations; do not fabricate academic theorems.
- A level sets the starting benchmark/depth emphasis, not a ceiling. Master Rules L0 foundations → L1 intuition → L2 core → L3 rigorous academic pass → L4 expert/research evidence still applies. A one-line name is a whole topic, never permission to teach shallowly. Unknown level is a provenance gap, not a reason to skip the topic or falsely claim graduate-only evidence.
- Keep every listed item in the coverage record. A noise:true appendix is retained for reconciliation, not endorsed as sound teaching. Unreviewed graph extraction strings require scope validation against their actual source; do not invent a lesson from a fragment or quietly remove it.

## 2. Prerequisites and just-in-time bridges
- Follow the supplied unit index and the topologically ordered topic list inside each unit. Explicit ext_prereq links are prerequisite claims; containment, taxonomy, cooccurrence and lecture/source sequence are not automatically academic prerequisites.
- Read the order audit. If a required topic occurs later, validate the dependency, teach that listed prerequisite just in time, record the bridge/return point and resume. Never silently describe an unresolved cross-unit graph conflict as a valid global order. Noise-appendix boundaries are audited separately from the normal learning path.
- Identify prerequisites to L0. Probe within teaching, not with a battery of pre-tests. Teach a shaky link immediately at full depth; do not re-teach a link the learner already handles fluently.

## 3. Reuse existing teaching and assignments first
- Look up the topic/unit in teaching_assignments_map.md/.json. Reuse existing Topics, Results, Build, Gap-fills, proof-tagged items and assignments from their exact source references; preserve proof status, uncertainty and ownership. Do not redo complete content. A lexical link is not proof of full teaching or assessment scope.
- T/A pointers in topics.md refer to existing source lines, not embedded lessons. These two pack files do not contain the original questions, keys or proofs. A local Mac path is not automatically readable inside Claude: obtain the unchanged source/map upload before claiming to inspect or reuse it. If unavailable, say so; never pretend it was read.
- Where usable material is absent, author clearly labelled tutor-generated self-study content, never purported source excerpts. Do not invent topics, source titles, citations, course codes, editions, quotations, page numbers or empirical results. Log genuine scope gaps and obtain learner agreement before adding a new topic.

## 4. Lesson recipe for any listed topic
1. Diagnose concept/procedure/notation/question confusion from the learner's work. If unclear, ask one calibrating question, not three. For broad/contested subjects, offer the appropriate structured explanation rather than a fake testable method.
2. Unpack the problem, terms, subtopics, assumptions, central result, mechanism, numbers/limits, honest real-world counterpart, failure mode and hands-on piece into the record.
3. Start with a concrete instance before abstraction. Define each term/symbol at first use. Show one transformation per line with its reason, keep notation stable and honour a valid learner route. Split complex material into short numbered turns; never compress away the why.
4. Maintain key-result statuses: [P] prove in full; [D] derive every step; [S] proof sketch with the reason full proof is omitted; [X] stated, proof deferred with the missing dependency/destination named; [Def] definition, not proved; [check] verified by an actually executed script/test in the build. An unrun test is not [check].
5. Prove central and later-used results in dependency order: precise statement/hypotheses, purpose, what fails without each hypothesis, proof idea, justified steps, sanity/special-case check and unseen application. Explicitly defer unavailable machinery; never present it as proved.
6. After roughly 3–5 concepts, set a small build/exercise: goal, interface/files or worked-problem form, required behaviour, edge case, acceptance tests, written prediction, measurement, cost/teardown where relevant and what to report. The learner makes the artefact. Build by hand at toy size before comparing with a professional tool/oracle.
7. Complete the academic pass and escalating problem ramp, including a proof/derivation and computational/subject-equivalent problem, unseen transfer and reflection/decision record. Practical mastery needs the learner's own build/run/measurement; theoretical mastery needs an unaided proof/argument. Moving on is not evidence.

## 5. Short turns, correction and checks
- Warm, direct and precise, without cheerleading. Roughly 120–200 words per teaching turn, one small scaffold and at most one non-obvious check; no check when the learner already showed the pieces. Never answer an interactive check in the same turn.
- Explain a missing concept directly; use guided discovery only when its prerequisites exist. Work a parallel example, not the learner's assigned problem. Use prose/tables, not text-drawn diagrams. A genuinely rendered visual shows one relationship, not the completed answer.
- Explicit skip/move-on: proceed, give the answer/reason briefly and log not evidenced; do not repeat/reword the skipped check. Impatience gets a more direct hint; genuine stuckness gets a concrete foothold and the missing prerequisite. A missed submitted exercise gets one smaller retry. Stop probing after understanding is demonstrated.

## 6. Five-question unit check and hidden answer key
- Reuse a suitable existing assignment; never invent its questions/key. Otherwise label the new check tutor-generated self-study: (1) conceptual choice with reason, (2) multiple-select/conditions or counterexample, (3) numerical/computational/subject-equivalent application, (4) proof/derivation/rigorous argument, (5) build/programming/design/subject-equivalent transfer. Teach every prerequisite first. Use the actual course profile's marking rules; do not invent a universal pass mark.
- Prepare and verify the expected key before issuing the check. Interactive tutoring asks one question at a time and keeps the key unrevealed until an attempt. A requested worksheet may present all five questions with the key under <details><summary>Answer key — open only after your attempt</summary>. Collapsed Markdown is not private/security-enforced. Never include an interactive question's answer in its teaching turn.
- Hints follow an attempt and escalate one notch at a time. Do not write the learner's code, exercise, essay or assessed submission. For graded work, obey the declared integrity policy, teach parallel examples and review reasoning rather than supply final answers.

## 7. Source honesty, safety and measured evidence
- Distinguish checked sources, graph extraction, inference and recalled/not-checked claims. Topic evidence establishes inclusion/level support, not verification of every future theorem. Name genuine benchmarks; never manufacture citations. Check current interfaces, standards, prices and figures against primary sources before teaching as current.
- Labs stay local/disposable and owned/authorized; data is synthetic; secrets stay out of prompts/notes. Never attack external systems or real accounts. Security-critical toys are learning-only, never production. Work/client accounts remain read-only. Tag cost; paid resources need explicit budget/spend limits and teardown.
- Measure performance with baselines/error bars and correctness with tests/proofs. Never claim a script ran, a key was computed or an experiment passed unless it actually did.

## 8. Persistent progress and resumption
- Track each topic's state (not started/in progress/taught/mastered; shaky/unverified/sliced), highest L0–L4 depth, checks, proofs/deferrals, builds/measurements, predictions, misconceptions, errors by cause and decision evidence.
- Keep prerequisite/bridge, source-coverage, scope and level-gap ledgers. Save the exact resume point: unit/topic/block, open check or failing test, next step and return point. Moving on is never passing.
- Recall taught/mastered topics at about 1, 3, 7 and 21 sessions; reattempt missed problems cold at about 1, 3 and 7 days. This is a record cadence, not an automatic calendar service. Close sessions by updating states, recall queue, errors and resume point. Audit gaps before leaving a domain or starting a capstone; never trade depth for a calendar deadline.

## Pack-specific provenance and order audit

Full; 14046 units; 36628 distinct graph topics; 36628 topic occurrences. Source curricula and main graph were not changed to create this pack.

- Academic level-unknown topics: 17210. No level was invented.
- Order: unit prerequisite violations N/A (new graph-cluster units); explicit topic prerequisite violations 0; all main-path DAG topic-edge violations 0. Unresolved flags do not validate the semantic prerequisite claims.
- Noise appendix: 43 topics; 318 reversed graph edges caused by final appendix placement, excluded from normal-path claims.
- Reuse pointers: 26.29% teaching / 6.17% assignments; not a guarantee of complete teaching.
- FULL SCOPE: every graph topic occurs exactly once; strict base filter disabled; all 43 noise:true topics retained at the end. This is an unwritten authoring inventory, not completed teaching.

### Evidence files and source registry
- `/Users/suhas/sde/ocw-courses/uglists/graph/unified_graph.json`
- `/Users/suhas/sde/ocw-courses/uglists/graph/topic_levels_expanded.tsv`
- `/Users/suhas/sde/ocw-courses/recovery/curriculum/rebuild_full/teaching_assignments_map.md`
- `/Users/suhas/sde/ocw-courses/recovery/curriculum/rebuild_full/teaching_assignments_map.json`
- `/Users/suhas/sde/nptel/unified_cloud_curriculum.md`
- Teaching-source SHA256: `0a81c35c21c3a8343764ccd8f443933fc0db88aab51c6282318751cd5318e6a9`; line ranges refer to that unchanged original, not a rebuild.
- Rules input `/Users/suhas/sde/Master_Rules.md`; SHA256 `1d5d63e06317a7c35ca6e050595f16a7670a72979c2773d68b00145eb1372865`.
- Rules input `/Users/suhas/sde/learn-SKILL.md`; SHA256 `d794cc09183d2e0a25904a03ee24b4ce14db30ef609fbc9a123d192b8f91c83c`.
- https://github.com/donnemartin/system-design-primer/blob/master/README.md
- https://cbseacademic.nic.in/curriculum_2027.html
- https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Maths_SecP2_2026-27.pdf
- https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Physics_SecP2_2026-27.pdf
- https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Computer_Science_SecP2_2026-27.pdf

# Unit index (same order as topics.md)

1. F0001 HS ComputerScience Class XI / Unit 1: Computer Systems and Organisation — Basic computer organisation
2. F0002 HS ComputerScience Class XI / Unit 2: Computational Thinking and Programming - I — Introduction to Problem-solving
3. F0003 HS ComputerScience Class XI / Unit 3: Society, Law and Ethics — Digital Footprints
4. F0004 HS ComputerScience Class XII / Unit 1: Computational Thinking and Programming – 2 — Functions
5. F0005 HS ComputerScience Class XII / Unit 2: Computer Networks — Evolution of networking
6. F0006 HS ComputerScience Class XII / Unit 3: Database Management — Database concepts
7. F0007 HS Maths Class XI / Unit-I: Sets and Functions — Sets
8. F0008 HS Maths Class XI / Unit-II: Algebra — Complex Numbers and Quadratic Equations
9. F0009 HS Maths Class XI / Unit-III: Coordinate Geometry — Straight Lines
10. F0010 HS Maths Class XI / Unit-IV: Calculus — Limits and Derivatives
11. F0011 HS Maths Class XII / Unit-I: Relations and Functions — Relations and Functions
12. F0012 HS Maths Class XII / Unit-II: Algebra — Matrices
13. F0013 HS Maths Class XII / Unit-III: Calculus — Applications of Derivatives
14. F0014 HS Physics Class XI / Unit I:        Physical World and Measurements — Units and Measurements
15. F0015 HS Physics Class XI / Unit II:       Kinematics — Motion in a Straight Line
16. F0016 HS Physics Class XI / Unit III:      Laws of Motion — Laws of Motion
17. F0017 HS Physics Class XI / Unit IV:       Work, Energy and Power — Work, Energy and Power
18. F0018 HS Physics Class XI / Unit V:        Motion of System of Particles and Rigid Body — System of Particles and Rotational Motion
19. F0019 HS Physics Class XI / Unit VI:      Gravitation — Gravitation
20. F0020 HS Physics Class XI / Unit VII:      Properties of Bulk Matter — Mechanical Properties of Solids
21. F0021 HS Physics Class XI / Unit VIII: Thermodynamics — Thermodynamics
22. F0022 HS Physics Class XI / Unit X:       Oscillations and Waves — Oscillations
23. F0023 HS Physics Class XII / Unit I:        Electrostatics — Electric Charges and Fields
24. F0024 HS Physics Class XII / Unit II:       Current Electricity — Current Electricity
25. F0025 HS Physics Class XII / Unit III:       Magnetic Effects of Current and Magnetism — Moving Charges and Magnetism
26. F0026 HS Physics Class XII / Unit IV:      Electromagnetic Induction and Alternating Currents — Electromagnetic Induction
27. F0027 HS Physics Class XII / Unit IX:      Electronic Devices — Semiconductor Electronics: Materials, Devices and Simple Circuits
28. F0028 HS Physics Class XII / Unit V:       Electromagnetic waves — Electromagnetic Waves
29. F0029 HS Physics Class XII / Unit VI:       Optics — Ray Optics and Optical Instruments
30. F0030 HS Physics Class XII / Unit VII:    Dual Nature of Radiation and Matter — Dual Nature of Radiation and Matter
31. F0031 HS Physics Class XII / Unit VIII:      Atoms and Nuclei — Atoms
32. F0032 Algorithms & Theory of CS — a-d
33. F0033 Algorithms & Theory of CS — ancient avenue
34. F0034 Algorithms & Theory of CS — calculable
35. F0035 Algorithms & Theory of CS — dcn
36. F0036 Algorithms & Theory of CS — freiman
37. F0037 Algorithms & Theory of CS — ied
38. F0038 Algorithms & Theory of CS — junit
39. F0039 Algorithms & Theory of CS — max2sat
40. F0040 Algorithms & Theory of CS — nishing
41. F0041 Algorithms & Theory of CS — proposed
42. F0042 Algorithms & Theory of CS — sequential game
43. F0043 Algorithms & Theory of CS — stricter
44. F0044 Algorithms & Theory of CS — tnm
45. F0045 Algorithms & Theory of CS — upt
46. F0046 CS2023 gap-fill — Aspect-Oriented Programming
47. F0047 CS2023 gap-fill — Query Construction
48. F0048 CS2023 gap-fill — Accessibility and inclusive design
49. F0049 Computer Architecture — ac97 sdata
50. F0050 Computer Architecture — cd5
51. F0051 Computer Architecture — ex3
52. F0052 Computer Architecture — guitar hero
53. F0053 Computer Architecture — kivy
54. F0054 Computer Architecture — metronome
55. F0055 Computer Architecture — orji
56. F0056 Computer Architecture — presenter
57. F0057 Computer Architecture — sop
58. F0058 Computer Architecture — tpd
59. F0059 Computer Architecture — werf
60. F0060 Computer Networks — abkm01
61. F0061 Computer Architecture — audio
62. F0062 Computer Networks — brainstorming
63. F0063 Computer Networks — crl
64. F0064 Computer Networks — eos
65. F0065 Computer Networks — hdr
66. F0066 Computer Networks — jee
67. F0067 Computer Networks — marcy darnovsky
68. F0068 Computer Networks — packet train
69. F0069 Computer Networks — remedied
70. F0070 Computer Networks — si2
71. F0071 Computer Networks — theatre
72. F0072 Cryptography & Security — aadhaar
73. F0073 Cryptography & Security — ari
74. F0074 Cryptography & Security — concolic
75. F0075 Cryptography & Security — dingledine
76. F0076 Cryptography & Security — fdq
77. F0077 Cryptography & Security — icn
78. F0078 Cryptography & Security — m1 mn
79. F0079 Cryptography & Security — nacl
80. F0080 Cryptography & Security — onion
81. F0081 Cryptography & Security — platter
82. F0082 Cryptography & Security — secured
83. F0083 Algorithms & Theory of CS — sha-3
84. F0084 Cryptography & Security — shamik sural
85. F0085 Cryptography & Security — trinket
86. F0086 Cryptography & Security — zook
87. F0087 Curriculum-only — adadelta
88. F0088 Curriculum-only — armijo goldstein
89. F0089 Curriculum-only — bcube
90. F0090 Curriculum-only — bushy tree
91. F0091 Curriculum-only — cgroup
92. F0092 Curriculum-only — configured independently
93. F0093 Curriculum-only — dcell
94. F0094 Curriculum-only — dft diagonalise
95. F0095 Curriculum-only — dspy
96. F0096 Curriculum-only — eor
97. F0097 Curriculum-only — faiss and chromadb
98. F0098 Cryptography & Security — discretionary
99. F0099 Curriculum-only — foundation of security and ethical hacking
100. F0100 Curriculum-only — gmm-em
101. F0101 Curriculum-only — gsp
102. F0102 Curriculum-only — hmaster
103. F0103 Curriculum-only — islip
104. F0104 Curriculum-only — lawfulness
105. F0105 Curriculum-only — lra
106. F0106 Curriculum-only — minhash
107. F0107 Curriculum-only — multicomputer
108. F0108 Curriculum-only — newreno
109. F0109 Curriculum-only — ocb
110. F0110 Curriculum-only — parkingspot
111. F0111 Curriculum-only — plentyoffish
112. F0112 Curriculum-only — problem-first
113. F0113 Curriculum-only — ragas
114. F0114 Curriculum-only — rpc inside
115. F0115 Curriculum-only — setconnmaxlifetime
116. F0116 Curriculum-only — sinkhole
117. F0117 Curriculum-only — sponsored by aricent
118. F0118 Curriculum-only — superstep
119. F0119 Curriculum-only — three-tier
120. F0120 Curriculum-only — tripadvisor
121. F0121 Curriculum-only — pseudonymity and unlinkability
122. F0122 Curriculum-only — waitgroup
123. F0123 Curriculum-only — yolo
124. F0124 Data Mining & Databases — african american
125. F0125 Data Mining & Databases — backdrop
126. F0126 Curriculum-only — mini-batching
127. F0127 Data Mining & Databases — bean
128. F0128 Data Mining & Databases — browser
129. F0129 Cryptography & Security — authority
130. F0130 Curriculum-only — os or browser
131. F0131 Data Mining & Databases — built
132. F0132 Curriculum-only — built from scratch
133. F0133 Data Mining & Databases — Business intelligence
134. F0134 Cryptography & Security — cbc-mac
135. F0135 Data Mining & Databases — census tract
136. F0136 Cryptography & Security — sandip chakraborty
137. F0137 Data Mining & Databases — anirban chakraborty
138. F0138 Data Mining & Databases — csa
139. F0139 Data Mining & Databases — dep
140. F0140 Curriculum-only — dep and nx
141. F0141 Data Mining & Databases — depositor
142. F0142 Data Mining & Databases — eharmony
143. F0143 Curriculum-only — optimiser and executor
144. F0144 Data Mining & Databases — exhibition
145. F0145 Data Mining & Databases — getnext
146. F0146 Data Mining & Databases — highdimensional
147. F0147 Data Mining & Databases — jacknife
148. F0148 Data Mining & Databases — laughter
149. F0149 Curriculum-only — flipkart and linkedin
150. F0150 Data Mining & Databases — lob
151. F0151 Data Mining & Databases — memtable
152. F0152 Data Mining & Databases — ncardb
153. F0153 Data Mining & Databases — origami
154. F0154 Data Mining & Databases — primarily
155. F0155 Data Mining & Databases — retail merchandising
156. F0156 Curriculum-only — kadane scan
157. F0157 Data Mining & Databases — scikit-learn
158. F0158 Data Mining & Databases — subnormal
159. F0159 Data Mining & Databases — trp
160. F0160 Curriculum-only — kb per tweet
161. F0161 Data Mining & Databases — turning tweet
162. F0162 Distributed Systems & Cloud — abhisek panda
163. F0163 Distributed Systems & Cloud — algorithmic analysis
164. F0164 Distributed Systems & Cloud — authored
165. F0165 Distributed Systems & Cloud — birrell
166. F0166 Distributed Systems & Cloud — chandy
167. F0167 Distributed Systems & Cloud — committee for approval
168. F0168 Curriculum-only — stakeholder conflict
169. F0169 Distributed Systems & Cloud — contemporary large-scale
170. F0170 Algorithms & Theory of CS — diffing data
171. F0171 Computer Architecture — audio data
172. F0172 Computer Networks — carry data
173. F0173 Cryptography & Security — encrypted data
174. F0174 Curriculum-only — assemble the data
175. F0175 Data Mining & Databases — codasyl
176. F0176 Distributed Systems & Cloud — associated data
177. F0177 Curriculum-only — data curation and deduplication
178. F0178 Distributed Systems & Cloud — data platform
179. F0179 Curriculum-only — data platform ii
180. F0180 Distributed Systems & Cloud — data-intensive
181. F0181 Curriculum-only — dummy dataset
182. F0182 Data Mining & Databases — mccain
183. F0183 Distributed Systems & Cloud — ddt
184. F0184 Curriculum-only — automate devop
185. F0185 Distributed Systems & Cloud — dietz and sleator
186. F0186 Distributed Systems & Cloud — epcc
187. F0187 Distributed Systems & Cloud — flink
188. F0188 Distributed Systems & Cloud — googlenet
189. F0189 Curriculum-only — chandy misra haas
190. F0190 Distributed Systems & Cloud — hagit
191. F0191 Curriculum-only — overflow handling
192. F0192 Distributed Systems & Cloud — hands-on
193. F0193 Curriculum-only — hands-on interpreting
194. F0194 Data Mining & Databases — hands-on data
195. F0195 Distributed Systems & Cloud — hardware
196. F0196 Computer Architecture — reconfigurable hardware
197. F0197 Cryptography & Security — trusted hardware
198. F0198 Distributed Systems & Cloud — hcp
199. F0199 Distributed Systems & Cloud — iisc
200. F0200 Distributed Systems & Cloud — jalote
201. F0201 Distributed Systems & Cloud — jp singh
202. F0202 Distributed Systems & Cloud — kmp
203. F0203 Curriculum-only — bulk load
204. F0204 Distributed Systems & Cloud — logical
205. F0205 Distributed Systems & Cloud — misd
206. F0206 Data Mining & Databases — pabitra mitra
207. F0207 Distributed Systems & Cloud — mlop
208. F0208 Distributed Systems & Cloud — mpi1
209. F0209 Curriculum-only — namenode and datanode
210. F0210 Distributed Systems & Cloud — narlikar
211. F0211 Curriculum-only — nginx and haproxy
212. F0212 Distributed Systems & Cloud — nnewtemp
213. F0213 Distributed Systems & Cloud — one-week
214. F0214 Distributed Systems & Cloud — paravirtualization
215. F0215 Distributed Systems & Cloud — phil sung
216. F0216 Curriculum-only — designated port
217. F0217 Distributed Systems & Cloud — port0
218. F0218 Curriculum-only — post-hoc attribution
219. F0219 Distributed Systems & Cloud — postdoc
220. F0220 Distributed Systems & Cloud — mj quinn
221. F0221 Distributed Systems & Cloud — recoverability
222. F0222 Curriculum-only — unbuffered rendezvous
223. F0223 Distributed Systems & Cloud — reservation
224. F0224 Distributed Systems & Cloud — sandipiper
225. F0225 Data Mining & Databases — sayan ranu
226. F0226 Distributed Systems & Cloud — scala
227. F0227 Curriculum-only — cascadeless schedule
228. F0228 Distributed Systems & Cloud — scholarly
229. F0229 Distributed Systems & Cloud — shivam
230. F0230 Distributed Systems & Cloud — sline
231. F0231 Distributed Systems & Cloud — sparsifier
232. F0232 Distributed Systems & Cloud — jim sukha
233. F0233 Computer Architecture — sonar system
234. F0234 Computer Networks — erp system
235. F0235 Cryptography & Security — linq
236. F0236 Computer Networks — mobile app
237. F0237 Cryptography & Security — permissioned system
238. F0238 Curriculum-only — system hacking
239. F0239 Data Mining & Databases — delegation
240. F0240 Distributed Systems & Cloud — ap system
241. F0241 Curriculum-only — hands-on task
242. F0242 Distributed Systems & Cloud — tasking
243. F0243 Distributed Systems & Cloud — timedchannel
244. F0244 Curriculum-only — toil and postmortem
245. F0245 Distributed Systems & Cloud — towrite
246. F0246 Curriculum-only — trending topic system like twitter
247. F0247 Distributed Systems & Cloud — typ
248. F0248 Distributed Systems & Cloud — vlisside
249. F0249 Distributed Systems & Cloud — yogesh
250. F0250 Graph concepts — Avoiding fallacies and misrepresentation in argumentation
251. F0251 Graph concepts — DevOps practices
252. F0252 Graph concepts — Intended and unintended applications of stored data
253. F0253 Graph concepts — Occlusion culling
254. F0254 Graph concepts — Stored procedures
255. F0255 Information Theory & Coding — abnnr
256. F0256 Information Theory & Coding — circularly polarized
257. F0257 Information Theory & Coding — ebola
258. F0258 Curriculum-only — efficiency are illustrative
259. F0259 Information Theory & Coding — exactly-once
260. F0260 Information Theory & Coding — gnuplot
261. F0261 Algorithms & Theory of CS — berinde and indyk
262. F0262 Information Theory & Coding — guruswami and indyk
263. F0263 Data Mining & Databases — kyle keane
264. F0264 Information Theory & Coding — khandekar
265. F0265 Information Theory & Coding — messenger
266. F0266 Information Theory & Coding — pacific grove
267. F0267 Information Theory & Coding — recessive
268. F0268 Curriculum-only — needham schroeder
269. F0269 Information Theory & Coding — seenpetehh
270. F0270 Information Theory & Coding — switched system
271. F0271 Information Theory & Coding — word error rate
272. F0272 ML & AI — acharya
273. F0273 ML & AI — bmr0ldrcejbysygnvcy8
274. F0274 Algorithms & Theory of CS — caged cat
275. F0275 ML & AI — chatbot
276. F0276 ML & AI — crunch
277. F0277 ML & AI — e2f
278. F0278 ML & AI — excess risk
279. F0279 Data Mining & Databases — gspan and fsg
280. F0280 ML & AI — fud
281. F0281 ML & AI — harry potter
282. F0282 ML & AI — incandescent
283. F0283 ML & AI — lbl
284. F0284 Curriculum-only — adapt it with lora
285. F0285 ML & AI — madam
286. F0286 ML & AI — nl4k24ohax3
287. F0287 Curriculum-only — hands-on rnn for an nlp task
288. F0288 ML & AI — nmla
289. F0289 ML & AI — poa
290. F0290 ML & AI — rama
291. F0291 ML & AI — sharma
292. F0292 ML & AI — tpus
293. F0293 Curriculum-only — prefix tuning
294. F0294 ML & AI — tzs9axfsrysi39t27o1il8rvynw
295. F0295 Curriculum-only — hands-on unet
296. F0296 ML & AI — v2t u1
297. F0297 Distributed Systems & Cloud — shivam verma
298. F0298 ML & AI — vferpery
299. F0299 Curriculum-only — improvisation and vqvae
300. F0300 ML & AI — vvt
301. F0301 Curriculum-only — xai and the need for xai
302. F0302 ML & AI — xit
303. F0303 Mathematics — a2 b3
304. F0304 Curriculum-only — billing account
305. F0305 Distributed Systems & Cloud — bal
306. F0306 Mathematics — act
307. F0307 Algorithms & Theory of CS — remove
308. F0308 Curriculum-only — add autoscaling
309. F0309 Data Mining & Databases — rpl
310. F0310 Mathematics — additional
311. F0311 Mathematics — ammeter
312. F0312 Curriculum-only — smi and asn
313. F0313 Mathematics — assuming
314. F0314 Distributed Systems & Cloud — intended audience
315. F0315 Mathematics — ax bg
316. F0316 Data Mining & Databases — Peano axioms
317. F0317 Mathematics — axis
318. F0318 Curriculum-only — inspiration behind cnn
319. F0319 Mathematics — belong to fn
320. F0320 Algorithms & Theory of CS — hawk
321. F0321 Mathematics — ball
322. F0322 Algorithms & Theory of CS — ball landed
323. F0323 Mathematics — bls
324. F0324 Data Mining & Databases — brief detour
325. F0325 Mathematics — brown
326. F0326 Data Mining & Databases — arnold
327. F0327 Mathematics — btj
328. F0328 Curriculum-only — building application on gcp
329. F0329 Mathematics — bun
330. F0330 Information Theory & Coding — codon
331. F0331 Mathematics — cao
332. F0332 Mathematics — champ
333. F0333 Computer Networks — check-in
334. F0334 Curriculum-only — check it can be maintained
335. F0335 Mathematics — accept
336. F0336 Curriculum-only — cap choice
337. F0337 Mathematics — choice of z1
338. F0338 Curriculum-only — four-way close
339. F0339 ML & AI — re close
340. F0340 Mathematics — closed
341. F0341 Curriculum-only — collection warn
342. F0342 Mathematics — combine
343. F0343 Computer Architecture — complex fsm
344. F0344 Mathematics — composition
345. F0345 Curriculum-only — generic composition
346. F0346 Mathematics — compressed
347. F0347 Curriculum-only — schedule topics continue
348. F0348 Data Mining & Databases — continue winning
349. F0349 Mathematics — contractive
350. F0350 Algorithms & Theory of CS — counting spanning tree
351. F0351 Curriculum-only — counting mac
352. F0352 Data Mining & Databases — k-counting
353. F0353 Mathematics — counting trick
354. F0354 Curriculum-only — reciprocal csc
355. F0355 Mathematics — current
356. F0356 Computer Architecture — current song
357. F0357 Curriculum-only — current page is followed
358. F0358 Distributed Systems & Cloud — current timetable
359. F0359 Mathematics — currently
360. F0360 Data Mining & Databases — able to deal
361. F0361 Mathematics — decompose
362. F0362 Curriculum-only — waw dependence
363. F0363 Mathematics — dependent column
364. F0364 Algorithms & Theory of CS — extras
365. F0365 Curriculum-only — trivium detail
366. F0366 Information Theory & Coding — iana
367. F0367 Mathematics — determine
368. F0368 Information Theory & Coding — develop and analyze
369. F0369 Mathematics — developed
370. F0370 ML & AI — wasserstein distance
371. F0371 Mathematics — closest
372. F0372 Curriculum-only — arctan with their domain
373. F0373 Distributed Systems & Cloud — non-numeric domain
374. F0374 Mathematics — don
375. F0375 Mathematics — dwi
376. F0376 Cryptography & Security — avalanche effect
377. F0377 Curriculum-only — allee effect
378. F0378 Distributed Systems & Cloud — struggle
379. F0379 ML & AI — confounding
380. F0380 Mathematics — effort
381. F0381 Data Mining & Databases — empty tree
382. F0382 Mathematics — endless
383. F0383 Curriculum-only — entry can go stale
384. F0384 Mathematics — epic
385. F0385 Curriculum-only — equivalent mutant
386. F0386 Mathematics — error
387. F0387 Curriculum-only — error reporting
388. F0388 Data Mining & Databases — crim
389. F0389 Information Theory & Coding — adversarial error
390. F0390 Mathematics — esn
391. F0391 Algorithms & Theory of CS — euclid algorithm
392. F0392 Mathematics — everything
393. F0393 Information Theory & Coding — thymine
394. F0394 Mathematics — except perhap
395. F0395 Curriculum-only — exist and not exist
396. F0396 Mathematics — expected shortfall
397. F0397 Distributed Systems & Cloud — hands-on experience
398. F0398 Mathematics — content
399. F0399 Curriculum-only — content is the course map
400. F0400 Information Theory & Coding — User-generated content, content moderation, and liability
401. F0401 Mathematics — explanation
402. F0402 Curriculum-only — explanation map
403. F0403 Mathematics — explore
404. F0404 Distributed Systems & Cloud — extra hardware
405. F0405 Mathematics — f1 measurable
406. F0406 Cryptography & Security — two-factor
407. F0407 Information Theory & Coding — scale factor
408. F0408 Mathematics — fagin
409. F0409 Algorithms & Theory of CS — generalizing farkas
410. F0410 Mathematics — faster
411. F0411 Mathematics — fine
412. F0412 Algorithms & Theory of CS — finite system
413. F0413 Mathematics — finite fourier transform
414. F0414 ML & AI — thigh
415. F0415 Mathematics — fletcher
416. F0416 Mathematics — full
417. F0417 Algorithms & Theory of CS — full autonomy
418. F0418 Mathematics — function
419. F0419 Computer Architecture — ida
420. F0420 Cryptography & Security — function os
421. F0421 Curriculum-only — analyticity of function
422. F0422 Data Mining & Databases — unary function
423. F0423 Distributed Systems & Cloud — idempotent function
424. F0424 Information Theory & Coding — l2 function
425. F0425 ML & AI — coercive function
426. F0426 Mathematics — continuous
427. F0427 Curriculum-only — continuous batching
428. F0428 Mathematics — continuous proba
429. F0429 Mathematics — function of x0
430. F0430 Mathematics — gon
431. F0431 Algorithms & Theory of CS — rectangular grid
432. F0432 Curriculum-only — grid-distance
433. F0433 Mathematics — equispaced
434. F0434 Curriculum-only — gpu half
435. F0435 Mathematics — half-step
436. F0436 Curriculum-only — hand with blackjackhand
437. F0437 Mathematics — hao wu
438. F0438 Curriculum-only — living with hard
439. F0439 ML & AI — p-hard
440. F0440 Mathematics — difficult
441. F0441 Data Mining & Databases — cookbook
442. F0442 Mathematics — help yourself
443. F0443 Information Theory & Coding — high-throughput
444. F0444 ML & AI — high dimensionality
445. F0445 Mathematics — hit
446. F0446 Curriculum-only — hyperbolic function cosh
447. F0447 Mathematics — hypergeometric
448. F0448 Algorithms & Theory of CS — ice core
449. F0449 Mathematics — ici
450. F0450 Curriculum-only — immediate post-dominator reconvergence
451. F0451 Mathematics — improvement
452. F0452 Algorithms & Theory of CS — incremental improvement
453. F0453 Curriculum-only — two-choice improvement
454. F0454 Mathematics — in-class
455. F0455 Data Mining & Databases — individual learning
456. F0456 Mathematics — infima
457. F0457 Curriculum-only — adversarial full-information
458. F0458 Distributed Systems & Cloud — mpi information
459. F0459 Information Theory & Coding — extrinsic information
460. F0460 ML & AI — information gain
461. F0461 Mathematics — input
462. F0462 Algorithms & Theory of CS — robp
463. F0463 Computer Architecture — two-input polygraph
464. F0464 Curriculum-only — failing input saved under testdata
465. F0465 Mathematics — discontinuous input
466. F0466 Curriculum-only — fagan inspection
467. F0467 Mathematics — instead
468. F0468 ML & AI — interesting and challenging
469. F0469 Mathematics — interpreted
470. F0470 Curriculum-only — introduce nlp task
471. F0471 Mathematics — invitation
472. F0472 Mathematics — josephina
473. F0473 Computer Networks — moderated
474. F0474 Curriculum-only — autoscaling group
475. F0475 Data Mining & Databases — group-by
476. F0476 Distributed Systems & Cloud — group id
477. F0477 Mathematics — group d1
478. F0478 Mathematics — kxka
479. F0479 Computer Architecture — ohm law
480. F0480 Mathematics — exponential law
481. F0481 Distributed Systems & Cloud — sean lie
482. F0482 Mathematics — lieven vandenberghe
483. F0483 Computer Architecture — flaw and limitation
484. F0484 Mathematics — limt t0
485. F0485 Algorithms & Theory of CS — linear conflict
486. F0486 Data Mining & Databases — dfw
487. F0487 Information Theory & Coding — linear mmse
488. F0488 ML & AI — hlle
489. F0489 Mathematics — argmin ky
490. F0490 ML & AI — linear classi ers
491. F0491 Mathematics — geometric
492. F0492 Mathematics — ls4
493. F0493 Data Mining & Databases — major domain
494. F0494 Mathematics — manganese
495. F0495 Curriculum-only — mapping from er
496. F0496 Mathematics — continuous mapping
497. F0497 Distributed Systems & Cloud — motivational material
498. F0498 Mathematics — mathematical
499. F0499 Algorithms & Theory of CS — mathematical maturity
500. F0500 Mathematics — matter
501. F0501 Algorithms & Theory of CS — maximum load
502. F0502 Curriculum-only — maximum tolerable downtime
503. F0503 Information Theory & Coding — maximum throughput
504. F0504 Mathematics — mechanical oscillation
505. F0505 Curriculum-only — generalized elgamal
506. F0506 Mathematics — minute
507. F0507 Curriculum-only — non-specialist in five minute
508. F0508 Mathematics — missing
509. F0509 Mathematics — narrow
510. F0510 Curriculum-only — narrow waist
511. F0511 Distributed Systems & Cloud — narrow ai
512. F0512 Mathematics — natural
513. F0513 Curriculum-only — data is needed
514. F0514 Mathematics — needed to reach
515. F0515 Curriculum-only — negligible function
516. F0516 Mathematics — neurip
517. F0517 Curriculum-only — levenberg marquardt and other modified newton
518. F0518 Mathematics — nim
519. F0519 Data Mining & Databases — add nothing
520. F0520 Mathematics — nothing wrong
521. F0521 Algorithms & Theory of CS — high reynolds number
522. F0522 Curriculum-only — id and number
523. F0523 Information Theory & Coding — kissing number
524. F0524 Mathematics — digit
525. F0525 Curriculum-only — numerical method built from scratch
526. F0526 Mathematics — objective
527. F0527 Curriculum-only — clipped-surrogate objective
528. F0528 Mathematics — occur
529. F0529 Algorithms & Theory of CS — online material
530. F0530 Data Mining & Databases — online dvd rental
531. F0531 Mathematics — open book
532. F0532 Curriculum-only — derived operator
533. F0533 Data Mining & Databases — additional operator
534. F0534 Mathematics — opt
535. F0535 Data Mining & Databases — obtained to enable optimal
536. F0536 ML & AI — optimal discriminator
537. F0537 Mathematics — algo
538. F0538 Curriculum-only — check option
539. F0539 Mathematics — optional
540. F0540 Curriculum-only — optional expiration
541. F0541 Mathematics — order
542. F0542 Algorithms & Theory of CS — lexicographical order
543. F0543 Curriculum-only — group by and order
544. F0544 Data Mining & Databases — interesting order
545. F0545 Mathematics — higher
546. F0546 Cryptography & Security — output a0
547. F0547 Curriculum-only — deliberately messy output
548. F0548 Information Theory & Coding — extrinsic output
549. F0549 Mathematics — iin
550. F0550 Cryptography & Security — two-party
551. F0551 Mathematics — pasta
552. F0552 Curriculum-only — people followed
553. F0553 Mathematics — periodization
554. F0554 Algorithms & Theory of CS — joule
555. F0555 Curriculum-only — physical inclinable function
556. F0556 Information Theory & Coding — physical effect
557. F0557 Mathematics — pick
558. F0558 Algorithms & Theory of CS — child of head
559. F0559 Mathematics — piece
560. F0560 Curriculum-only — hbr online piece we googled
561. F0561 Mathematics — piecewise linear
562. F0562 Cryptography & Security — plug and play
563. F0563 Mathematics — pmat
564. F0564 Curriculum-only — content poisoning
565. F0565 Mathematics — pong
566. F0566 Data Mining & Databases — certifying positive-semidefiniteness
567. F0567 Mathematics — de nite
568. F0568 Curriculum-only — early as possible
569. F0569 ML & AI — grid of possible
570. F0570 Mathematics — number of possible
571. F0571 Mathematics — provided
572. F0572 Cryptography & Security — ability to quickly configure
573. F0573 Mathematics — quizz
574. F0574 Algorithms & Theory of CS — mini-quizz
575. F0575 Mathematics — assigned
576. F0576 Distributed Systems & Cloud — highly available
577. F0577 Mathematics — add-in
578. F0578 Algorithms & Theory of CS — deterministic
579. F0579 Cryptography & Security — random oracle
580. F0580 Mathematics — blossom
581. F0581 Computer Networks — page-rank
582. F0582 Curriculum-only — rank from the svd
583. F0583 Distributed Systems & Cloud — rank-k
584. F0584 Mathematics — rarest
585. F0585 Computer Architecture — fft real
586. F0586 Curriculum-only — group over the real
587. F0587 Data Mining & Databases — real estate
588. F0588 Mathematics — group of real
589. F0589 Curriculum-only — reason lp
590. F0590 Mathematics — prefer
591. F0591 Curriculum-only — prefer composition
592. F0592 Mathematics — recalled
593. F0593 Curriculum-only — relationship ibe abe fe
594. F0594 Mathematics — remember
595. F0595 Computer Networks — qwest response
596. F0596 Curriculum-only — incident response
597. F0597 Mathematics — conscious response
598. F0598 Curriculum-only — rpc and rest
599. F0599 Mathematics — reverse
600. F0600 Curriculum-only — reverse kl
601. F0601 Mathematics — rii
602. F0602 Data Mining & Databases — eagle river
603. F0603 Mathematics — charle
604. F0604 Distributed Systems & Cloud — robust ai
605. F0605 Mathematics — robust optimization
606. F0606 Curriculum-only — cert-in role
607. F0607 Mathematics — romeo
608. F0608 Algorithms & Theory of CS — probabilistic
609. F0609 Mathematics — amount
610. F0610 Distributed Systems & Cloud — amount of lateness summed
611. F0611 Mathematics — root test
612. F0612 Computer Architecture — combination rules
613. F0613 Computer Networks — business rule
614. F0614 Curriculum-only — explosion of rule
615. F0615 Data Mining & Databases — association rule
616. F0616 Distributed Systems & Cloud — data model
617. F0617 Mathematics — bar
618. F0618 Data Mining & Databases — error bar
619. F0619 Mathematics — daughter
620. F0620 Curriculum-only — category of response
621. F0621 Mathematics — family
622. F0622 Algorithms & Theory of CS — intersecting family
623. F0623 Curriculum-only — indexed family
624. F0624 Mathematics — l'hospital rule
625. F0625 Curriculum-only — rule of thumb rtt
626. F0626 Mathematics — s-derivative rule
627. F0627 Cryptography & Security — bfv
628. F0628 Curriculum-only — eschenauer gligor scheme
629. F0629 Data Mining & Databases — implementation of scheme
630. F0630 Mathematics — run
631. F0631 Cryptography & Security — longset run
632. F0632 Curriculum-only — dry run
633. F0633 Data Mining & Databases — predicting run
634. F0634 Distributed Systems & Cloud — re-run deterministic idempotent function
635. F0635 Mathematics — cherry blossom run
636. F0636 Mathematics — separatrix
637. F0637 Algorithms & Theory of CS — de bruijn sequence
638. F0638 Distributed Systems & Cloud — sequence id
639. F0639 Information Theory & Coding — orthonormal sequence
640. F0640 ML & AI — conserved sequence
641. F0641 Mathematics — point-wise
642. F0642 Algorithms & Theory of CS — min-set
643. F0643 Computer Networks — si1
644. F0644 Cryptography & Security — re set
645. F0645 Curriculum-only — built on set
646. F0646 Data Mining & Databases — set coded
647. F0647 Distributed Systems & Cloud — dominating set
648. F0648 ML & AI — semialgebraic set
649. F0649 Mathematics — bijection
650. F0650 Algorithms & Theory of CS — short-circuitry
651. F0651 Mathematics — shuffling
652. F0652 Distributed Systems & Cloud — handling data shuffling
653. F0653 Mathematics — side
654. F0654 Curriculum-only — map-side
655. F0655 Mathematics — multiply
656. F0656 Algorithms & Theory of CS — linear size
657. F0657 Curriculum-only — estimating size
658. F0658 Data Mining & Databases — awful
659. F0659 Distributed Systems & Cloud — sped
660. F0660 Information Theory & Coding — alphabet of size
661. F0661 Mathematics — effect size
662. F0662 Curriculum-only — dependence on effect size
663. F0663 Mathematics — larger
664. F0664 Curriculum-only — larger run
665. F0665 Mathematics — skorohod
666. F0666 Algorithms & Theory of CS — minimum number
667. F0667 Curriculum-only — i-th minimum
668. F0668 Data Mining & Databases — minimum error tree
669. F0669 Mathematics — minimizing
670. F0670 Curriculum-only — error-minimizing lpp
671. F0671 Mathematics — minimization
672. F0672 Curriculum-only — data minimisation
673. F0673 Mathematics — smell
674. F0674 Curriculum-only — full of puzzle
675. F0675 Mathematics — solve ax
676. F0676 Curriculum-only — apply family
677. F0677 Mathematics — solve for easily
678. F0678 Curriculum-only — context and tool-exhaustion
679. F0679 ML & AI — context matter
680. F0680 Mathematics — sorted group of size
681. F0681 Curriculum-only — spelled aadhaar
682. F0682 Mathematics — spiral
683. F0683 Curriculum-only — neither predict effort alone
684. F0684 Mathematics — splot
685. F0685 Curriculum-only — finaliser to spread its low
686. F0686 Distributed Systems & Cloud — data spread
687. F0687 Mathematics — epidemic
688. F0688 Curriculum-only — srs and its characteristics
689. F0689 Mathematics — staircase function
690. F0690 Computer Networks — sql standard
691. F0691 Curriculum-only — oasis standard have moved
692. F0692 Information Theory & Coding — di erently
693. F0693 Mathematics — starch
694. F0694 Computer Networks — start visual paradigm
695. F0695 Curriculum-only — dependence on the start
696. F0696 Mathematics — set start
697. F0697 Algorithms & Theory of CS — ocsp
698. F0698 Curriculum-only — legitimate state
699. F0699 Data Mining & Databases — mental state
700. F0700 Distributed Systems & Cloud — state and snapshot
701. F0701 Mathematics — chain
702. F0702 Cryptography & Security — half of chain
703. F0703 Curriculum-only — chain of custody
704. F0704 Mathematics — anti-chain
705. F0705 Curriculum-only — analysable statement
706. F0706 Mathematics — stdev
707. F0707 Data Mining & Databases — jacob strauss
708. F0708 Mathematics — stretched string
709. F0709 Curriculum-only — strong and by smallest counterexample
710. F0710 Mathematics — stuck
711. F0711 Curriculum-only — data subject
712. F0712 Data Mining & Databases — subject in system
713. F0713 Distributed Systems & Cloud — existing subject
714. F0714 Mathematics — subject to ati
715. F0715 Curriculum-only — surviving and equivalent mutant
716. F0716 Mathematics — swan
717. F0717 Data Mining & Databases — symbol and quotation
718. F0718 Information Theory & Coding — pilot symbols
719. F0719 Mathematics — nite number
720. F0720 Curriculum-only — distinguishing advantage
721. F0721 Distributed Systems & Cloud — advantage of keeping
722. F0722 Mathematics — tatooine
723. F0723 Data Mining & Databases — can't tell
724. F0724 Mathematics — forgot
725. F0725 Algorithms & Theory of CS — recurring theme
726. F0726 Mathematics — broad
727. F0727 Curriculum-only — start broad
728. F0728 Mathematics — thinking and data
729. F0729 Algorithms & Theory of CS — arithmetization
730. F0730 Computer Architecture — rise time
731. F0731 Cryptography & Security — one-time mac
732. F0732 Curriculum-only — time are criticised
733. F0733 Distributed Systems & Cloud — illogical time
734. F0734 Information Theory & Coding — time-out
735. F0735 ML & AI — typing time
736. F0736 Mathematics — cover time
737. F0737 Curriculum-only — pprof top
738. F0738 ML & AI — top-k
739. F0739 Mathematics — bottom
740. F0740 Curriculum-only — total unimodularity
741. F0741 Mathematics — proj
742. F0742 Mathematics — try
743. F0743 Algorithms & Theory of CS — try to add
744. F0744 Curriculum-only — grid of try
745. F0745 Data Mining & Databases — pause
746. F0746 Curriculum-only — pause is refused
747. F0747 Mathematics — guess
748. F0748 Computer Architecture — nothing to turn
749. F0749 Curriculum-only — full turn
750. F0750 Information Theory & Coding — taking turn
751. F0751 Mathematics — coursework
752. F0752 Cryptography & Security — bn understand
753. F0753 Mathematics — uniformly
754. F0754 Curriculum-only — composition uniformly
755. F0755 Mathematics — converging uniformly
756. F0756 Algorithms & Theory of CS — domain variable
757. F0757 Curriculum-only — built-in variable threadidx
758. F0758 Data Mining & Databases — nea
759. F0759 Information Theory & Coding — data frame
760. F0760 Curriculum-only — pandas data frame
761. F0761 Data Mining & Databases — usda data frame
762. F0762 Information Theory & Coding — symbol variable
763. F0763 ML & AI — tuber
764. F0764 Mathematics — exi
765. F0765 Curriculum-only — short version
766. F0766 Data Mining & Databases — additional version
767. F0767 Mathematics — vfr
768. F0768 Curriculum-only — refreshed about weekly so billion crawled
769. F0769 Data Mining & Databases — gm weekly
770. F0770 Mathematics — weightless
771. F0771 Distributed Systems & Cloud — wide choice
772. F0772 Mathematics — wilcoxon
773. F0773 Algorithms & Theory of CS — kashin work
774. F0774 Curriculum-only — graded work
775. F0775 Distributed Systems & Cloud — parallelism
776. F0776 Curriculum-only — advantage of parallelism
777. F0777 Distributed Systems & Cloud — explicit parallelism
778. F0778 Mathematics — encouraged to work
779. F0779 Curriculum-only — wta and wtc
780. F0780 Mathematics — x4 s2
781. F0781 Mathematics — xso
782. F0782 Curriculum-only — pb in year
783. F0783 Distributed Systems & Cloud — th year
784. F0784 ML & AI — spent year
785. F0785 Mathematics — million
786. F0786 Curriculum-only — million interpreted
787. F0787 Data Mining & Databases — million time
788. F0788 Distributed Systems & Cloud — typically million
789. F0789 Mathematics — number of year
790. F0790 NLP & Speech — acceptor
791. F0791 NLP & Speech — cluster1
792. F0792 NLP & Speech — falcon
793. F0793 Mathematics — initial
794. F0794 Data Mining & Databases — cri
795. F0795 Mathematics — transition
796. F0796 Curriculum-only — state to which it can transition
797. F0797 Mathematics — recurrent
798. F0798 Curriculum-only — billion write
799. F0799 Distributed Systems & Cloud — write in arrival order
800. F0800 Mathematics — disk
801. F0801 Curriculum-only — disk to disk
802. F0802 Mathematics — closed disk
803. F0803 Computer Architecture — content and writing
804. F0804 NLP & Speech — grammatical category
805. F0805 NLP & Speech — mayor
806. F0806 NLP & Speech — paralinguistic information
807. F0807 NLP & Speech — psycholinguistic
808. F0808 NLP & Speech — six-seven
809. F0809 NLP & Speech — synrev
810. F0810 NLP & Speech — torso
811. F0811 Computer Architecture — ultrasonic transducers
812. F0812 NLP & Speech — tuna
813. F0813 Mathematics — decide
814. F0814 NLP & Speech — wrv
815. F0815 Operating Systems — andreas reuter
816. F0816 Operating Systems — caching
817. F0817 Curriculum-only — caching and propagation delays
818. F0818 Operating Systems — clement
819. F0819 Operating Systems — fasttrack
820. F0820 Operating Systems — idc
821. F0821 Operating Systems — lpt
822. F0822 Curriculum-only — mesi with the exclusive-clean state
823. F0823 Operating Systems — messr
824. F0824 Distributed Systems & Cloud — sape mullender
825. F0825 Operating Systems — nick feamster
826. F0826 Mathematics — sit
827. F0827 Operating Systems — pgsize
828. F0828 Curriculum-only — lru and pseudo-lru
829. F0829 Operating Systems — ptx
830. F0830 Operating Systems — sysfile
831. F0831 Operating Systems — vet
832. F0832 Curriculum-only — vet is clean
833. F0833 Operating Systems — wal
834. F0834 Other/Unknown — Absorption spectroscopy
835. F0835 ML & AI — sigmoid
836. F0836 Other/Unknown — adaptive control
837. F0837 Data Mining & Databases — arnab bhattacharya
838. F0838 Other/Unknown — ast and asz
839. F0839 Other/Unknown — biomolecule
840. F0840 Other/Unknown — catalysis
841. F0841 Other/Unknown — col761
842. F0842 Other/Unknown — curriculum
843. F0843 Curriculum-only — anywhere in this curriculum
844. F0844 Other/Unknown — data and realtime
845. F0845 Curriculum-only — hardware walk are deepened
846. F0846 Other/Unknown — deh
847. F0847 Other/Unknown — doppler
848. F0848 Information Theory & Coding — doppler spread
849. F0849 Other/Unknown — durbin
850. F0850 Mathematics — life
851. F0851 Curriculum-only — data life
852. F0852 Other/Unknown — economy
853. F0853 Data Mining & Databases — electric co
854. F0854 Mathematics — Electric current
855. F0855 Other/Unknown — electronic system
856. F0856 Other/Unknown — ephraim glick
857. F0857 Curriculum-only — exploration in rl
858. F0858 Distributed Systems & Cloud — Data exploration and visual analytics; how to calculate effect size
859. F0859 Other/Unknown — extensive data
860. F0860 Other/Unknown — fluorescence
861. F0861 Cryptography & Security — governance and fintech
862. F0862 Other/Unknown — corporate governance
863. F0863 Other/Unknown — hybridization
864. F0864 Other/Unknown — institutional
865. F0865 Other/Unknown — kiran
866. F0866 Other/Unknown — lle
867. F0867 Mathematics — variation
868. F0868 Other/Unknown — lorenz
869. F0869 Curriculum-only — kl-lucb
870. F0870 Other/Unknown — machining
871. F0871 Computer Architecture — cathode ray tubes
872. F0872 Cryptography & Security — realistic device
873. F0873 Other/Unknown — assistive devices
874. F0874 Other/Unknown — metamorphic
875. F0875 Other/Unknown — natural gas
876. F0876 Curriculum-only — elmasri and navathe
877. F0877 Other/Unknown — navigation systems
878. F0878 Other/Unknown — npt
879. F0879 Other/Unknown — parthasarathy ramachandran
880. F0880 Information Theory & Coding — kelvin
881. F0881 Other/Unknown — physiology
882. F0882 Mathematics — change
883. F0883 Curriculum-only — change confined
884. F0884 Mathematics — cause
885. F0885 Other/Unknown — poincar bendixson
886. F0886 Distributed Systems & Cloud — policy
887. F0887 Curriculum-only — alerting policy
888. F0888 Distributed Systems & Cloud — attendance policy
889. F0889 Mathematics — discuss
890. F0890 Computer Networks — esd264
891. F0891 Distributed Systems & Cloud — prepared to discuss
892. F0892 Mathematics — discussing
893. F0893 Operating Systems — encourage discussion
894. F0894 Other/Unknown — national
895. F0895 Curriculum-only — national and sectoral policy
896. F0896 Other/Unknown — porous material
897. F0897 Curriculum-only — sram puf
898. F0898 Other/Unknown — pv system
899. F0899 Curriculum-only — lora and qlora
900. F0900 Other/Unknown — quantificationally
901. F0901 Other/Unknown — respiratory system
902. F0902 Cryptography & Security — sustainable
903. F0903 Other/Unknown — rust
904. F0904 Distributed Systems & Cloud — comfortable with rust
905. F0905 Other/Unknown — santa claus
906. F0906 Distributed Systems & Cloud — genome sequencing
907. F0907 Other/Unknown — shallow
908. F0908 Other/Unknown — strange attractor
909. F0909 Curriculum-only — supply-chain and trusted-fabrication
910. F0910 Other/Unknown — suspension system
911. F0911 Other/Unknown — textile
912. F0912 Mathematics — truth
913. F0913 Other/Unknown — truth-functionally
914. F0914 Information Theory & Coding — intraoral pressure
915. F0915 Other/Unknown — variable and stochastic
916. F0916 Other/Unknown — workforce
917. F0917 Signal/Image/Audio/Video Processing — abt
918. F0918 Signal/Image/Audio/Video Processing — audio cd
919. F0919 Curriculum-only — little-oh and big-oh
920. F0920 Signal/Image/Audio/Video Processing — boldsymbol
921. F0921 Curriculum-only — barzilai and borwein
922. F0922 Signal/Image/Audio/Video Processing — brake
923. F0923 Mathematics — gear
924. F0924 Other/Unknown — planetary gears
925. F0925 Signal/Image/Audio/Video Processing — calcutta
926. F0926 Mathematics — binary
927. F0927 Curriculum-only — binary as the output
928. F0928 Data Mining & Databases — binary exponentiation
929. F0929 Information Theory & Coding — binary digit
930. F0930 Mathematics — binary function
931. F0931 Signal/Image/Audio/Video Processing — correct version
932. F0932 Mathematics — multiplying
933. F0933 Signal/Image/Audio/Video Processing — dale
934. F0934 Signal/Image/Audio/Video Processing — electrocardiography
935. F0935 Curriculum-only — capture filter
936. F0936 Data Mining & Databases — filter function
937. F0937 Distributed Systems & Cloud — bloom filter
938. F0938 Curriculum-only — bloom filter for deduplication
939. F0939 Information Theory & Coding — filter and composition
940. F0940 Mathematics — filter state
941. F0941 Other/Unknown — comb filters
942. F0942 Signal/Image/Audio/Video Processing — decimation filter
943. F0943 Signal/Image/Audio/Video Processing — gari clifford
944. F0944 Signal/Image/Audio/Video Processing — hirsh
945. F0945 Information Theory & Coding — window
946. F0946 ML & AI — context window
947. F0947 Mathematics — component
948. F0948 Algorithms & Theory of CS — strong component
949. F0949 Computer Networks — Defining places, as devices executing actions, including hardware components, remote hosts, may also include external, uncontrolled devices, hosts, and users
950. F0950 Curriculum-only — common goal of the component
951. F0951 Mathematics — length
952. F0952 Computer Networks — key length
953. F0953 Cryptography & Security — length preserving
954. F0954 Curriculum-only — length-prefixed
955. F0955 Mathematics — sequence of length
956. F0956 Signal/Image/Audio/Video Processing — filter length
957. F0957 Data Mining & Databases — ira haimowitz
958. F0958 Signal/Image/Audio/Video Processing — kf k2
959. F0959 Signal/Image/Audio/Video Processing — lp1
960. F0960 Signal/Image/Audio/Video Processing — mumford
961. F0961 Signal/Image/Audio/Video Processing — parzen window
962. F0962 Curriculum-only — parzen window and knn
963. F0963 Signal/Image/Audio/Video Processing — peak factor
964. F0964 Signal/Image/Audio/Video Processing — realpart
965. F0965 Curriculum-only — recoverable schedule
966. F0966 Signal/Image/Audio/Video Processing — reeve
967. F0967 Signal/Image/Audio/Video Processing — shiva
968. F0968 Signal/Image/Audio/Video Processing — tamas
969. F0969 Algorithms & Theory of CS — tamas sarlo
970. F0970 Signal/Image/Audio/Video Processing — tracked correctly
971. F0971 Signal/Image/Audio/Video Processing — wnn
972. F0972 Software Engineering — aas
973. F0973 Software Engineering — andreas schulz
974. F0974 Mathematics — report
975. F0975 Computer Architecture — checkoff and report
976. F0976 Curriculum-only — number in the report is produced
977. F0977 Data Mining & Databases — bug reports
978. F0978 Distributed Systems & Cloud — draft of report
979. F0979 Mathematics — battle
980. F0980 Operating Systems — dp report
981. F0981 Software Engineering — arltl
982. F0982 Curriculum-only — multivalued attribute
983. F0983 Information Theory & Coding — articulatory attribute
984. F0984 ML & AI — categorical attribute
985. F0985 Software Engineering — auth
986. F0986 Software Engineering — blinding
987. F0987 Curriculum-only — byte created-at
988. F0988 Software Engineering — cbr
989. F0989 Algorithms & Theory of CS — corrupt chronicle
990. F0990 Software Engineering — civic
991. F0991 Curriculum-only — client-go
992. F0992 Software Engineering — clo
993. F0993 Curriculum-only — clo and fat tree
994. F0994 Software Engineering — closurize
995. F0995 Software Engineering — contd
996. F0996 Computer Architecture — binary counter
997. F0997 Curriculum-only — microprogram counter
998. F0998 Software Engineering — cpo
999. F0999 Curriculum-only — data-handling policy
1000. F1000 Software Engineering — data6
1001. F1001 Data Mining & Databases — manager
1002. F1002 Distributed Systems & Cloud — action
1003. F1003 Algorithms & Theory of CS — cook
1004. F1004 Computer Architecture — pickup
1005. F1005 Curriculum-only — action on objective
1006. F1006 Distributed Systems & Cloud — bz rc ra
1007. F1007 Software Engineering — deconstructor
1008. F1008 Cryptography & Security — run of identical character
1009. F1009 Software Engineering — denny freeman
1010. F1010 Mathematics — balance
1011. F1011 Curriculum-only — probabilistic balance
1012. F1012 Software Engineering — disrupt
1013. F1013 Curriculum-only — nullable dtype
1014. F1014 Software Engineering — dur
1015. F1015 Operating Systems — joel emer
1016. F1016 Software Engineering — emergent
1017. F1017 Computer Architecture — noisy environment
1018. F1018 Operating Systems — system environment
1019. F1019 Other/Unknown — grid environments
1020. F1020 Mathematics — temperature
1021. F1021 Computer Architecture — skin conductivity
1022. F1022 Software Engineering — eri
1023. F1023 Mathematics — equal
1024. F1024 Software Engineering — amount equal
1025. F1025 Software Engineering — function walk
1026. F1026 Curriculum-only — composition and generics
1027. F1027 Software Engineering — gensym
1028. F1028 Data Mining & Databases — install
1029. F1029 Software Engineering — github account
1030. F1030 Mathematics — david
1031. F1031 Cryptography & Security — david mazi res
1032. F1032 Distributed Systems & Cloud — david zhang
1033. F1033 Mathematics — david ingerman
1034. F1034 Curriculum-only — treated in depth
1035. F1035 Operating Systems — david gifford
1036. F1036 Signal/Image/Audio/Video Processing — non-integer factor
1037. F1037 Software Engineering — hay
1038. F1038 Distributed Systems & Cloud — api
1039. F1039 Curriculum-only — rest api
1040. F1040 Distributed Systems & Cloud — graphx api
1041. F1041 Mathematics — const
1042. F1042 Software Engineering — howto
1043. F1043 Software Engineering — input handling
1044. F1044 Curriculum-only — minhash for jaccard
1045. F1045 Software Engineering — jason ansel
1046. F1046 Curriculum-only — ede with two or three keys
1047. F1047 Distributed Systems & Cloud — hashing
1048. F1048 Algorithms & Theory of CS — hashing family
1049. F1049 Curriculum-only — b-bit hashing
1050. F1050 Distributed Systems & Cloud — linear hashing
1051. F1051 Information Theory & Coding — random hashing
1052. F1052 Software Engineering — keyword
1053. F1053 Mathematics — rate
1054. F1054 Curriculum-only — annualised rate of occurrence
1055. F1055 Distributed Systems & Cloud — available bandwidth
1056. F1056 Information Theory & Coding — full rate
1057. F1057 Mathematics — angular rate
1058. F1058 Curriculum-only — saddle-point optimality
1059. F1059 Other/Unknown — Lapse rate
1060. F1060 Signal/Image/Audio/Video Processing — Frame rate
1061. F1061 Software Engineering — lcr
1062. F1062 Distributed Systems & Cloud — live migration
1063. F1063 Curriculum-only — gcp live migration
1064. F1064 Information Theory & Coding — time-to-live
1065. F1065 Software Engineering — load file
1066. F1066 Algorithms & Theory of CS — data aggregation
1067. F1067 Computer Architecture — loop counter
1068. F1068 Curriculum-only — loop and if-then-else
1069. F1069 Distributed Systems & Cloud — parallelization
1070. F1070 Information Theory & Coding — subscriber loop
1071. F1071 Mathematics — gathering
1072. F1072 Signal/Image/Audio/Video Processing — z-1
1073. F1073 Software Engineering — loop interchange
1074. F1074 Mathematics — finger
1075. F1075 Software Engineering — manifesto
1076. F1076 Curriculum-only — chain and merge
1077. F1077 Data Mining & Databases — sort-merge
1078. F1078 Software Engineering — g-ef2 h-ef4
1079. F1079 Cryptography & Security — mnk mn
1080. F1080 Software Engineering — model-view-controller
1081. F1081 Computer Networks — rapid development
1082. F1082 Curriculum-only — development lecture of the kharagpur
1083. F1083 Other/Unknown — impact
1084. F1084 Computer Architecture — Broader impacts
1085. F1085 Curriculum-only — reconnaissance through impact
1086. F1086 Other/Unknown — rural development
1087. F1087 Software Engineering — modern architecture
1088. F1088 Mathematics — constraint
1089. F1089 Algorithms & Theory of CS — physical constraint
1090. F1090 Curriculum-only — clarify constraint
1091. F1091 Mathematics — adding constraint
1092. F1092 Computer Networks — load condition
1093. F1093 Curriculum-only — deny policy and condition
1094. F1094 Data Mining & Databases — truth condition
1095. F1095 ML & AI — felicity condition
1096. F1096 Mathematics — condition for exactly
1097. F1097 Signal/Image/Audio/Video Processing — condition on h0
1098. F1098 Software Engineering — instruction
1099. F1099 Computer Architecture — instruction labeled
1100. F1100 Curriculum-only — cpi of an instruction mix
1101. F1101 Other/Unknown — scheme of instruction
1102. F1102 Software Engineering — constraint in moving instruction
1103. F1103 Software Engineering — named
1104. F1104 Curriculum-only — cocomo ii named
1105. F1105 Curriculum-only — psis-loo named
1106. F1106 Software Engineering — executable named
1107. F1107 Software Engineering — num1
1108. F1108 Algorithms & Theory of CS — constructed object
1109. F1109 Curriculum-only — client treat individual object
1110. F1110 Data Mining & Databases — object handle
1111. F1111 Distributed Systems & Cloud — atomic
1112. F1112 ML & AI — caltech object dataset
1113. F1113 Signal/Image/Audio/Video Processing — percent of object tracked
1114. F1114 Software Engineering — function object
1115. F1115 Software Engineering — operational semantics
1116. F1116 Curriculum-only — optimism at merge
1117. F1117 Software Engineering — ote
1118. F1118 Curriculum-only — owasp juice shop
1119. F1119 Software Engineering — owasp top
1120. F1120 Algorithms & Theory of CS — tms
1121. F1121 Computer Networks — markup language
1122. F1122 Curriculum-only — classad language
1123. F1123 Data Mining & Databases — encyclopedias
1124. F1124 Distributed Systems & Cloud — language and system
1125. F1125 Information Theory & Coding — language development
1126. F1126 Mathematics — lisp
1127. F1127 Data Mining & Databases — dialect
1128. F1128 NLP & Speech — language family
1129. F1129 Software Engineering — algol
1130. F1130 Cryptography & Security — ltp
1131. F1131 Curriculum-only — name drdo
1132. F1132 Data Mining & Databases — dno
1133. F1133 Distributed Systems & Cloud — dns name
1134. F1134 Operating Systems — dentry
1135. F1135 Other/Unknown — grant
1136. F1136 Computer Networks — grant option
1137. F1137 Signal/Image/Audio/Video Processing — crd
1138. F1138 Software Engineering — app name
1139. F1139 Algorithms & Theory of CS — pointer associated
1140. F1140 Cryptography & Security — fat pointer
1141. F1141 Curriculum-only — data and the pointer
1142. F1142 Software Engineering — parent
1143. F1143 Algorithms & Theory of CS — add parent
1144. F1144 Distributed Systems & Cloud — parent function
1145. F1145 Software Engineering — popcount
1146. F1146 Algorithms & Theory of CS — pre-requisite
1147. F1147 Distributed Systems & Cloud — industry
1148. F1148 Curriculum-only — role in industry
1149. F1149 Distributed Systems & Cloud — industry system
1150. F1150 Mathematics — literature
1151. F1151 NLP & Speech — pre indic
1152. F1152 Other/Unknown — current literature
1153. F1153 Signal/Image/Audio/Video Processing — pre-multiplying
1154. F1154 Software Engineering — pre-condition
1155. F1155 Distributed Systems & Cloud — network and primitive
1156. F1156 Mathematics — number of primitive
1157. F1157 Other/Unknown — geometric primitive
1158. F1158 Software Engineering — primop
1159. F1159 Mathematics — list
1160. F1160 Curriculum-only — collection list
1161. F1161 Data Mining & Databases — numbered list
1162. F1162 Distributed Systems & Cloud — list length
1163. F1163 ML & AI — extended list
1164. F1164 Curriculum-only — common extended list
1165. F1165 Software Engineering — append
1166. F1166 Mathematics — call
1167. F1167 Computer Architecture — original call
1168. F1168 Curriculum-only — call and callcenter
1169. F1169 Distributed Systems & Cloud — call mpi
1170. F1170 Mathematics — call duration
1171. F1171 Algorithms & Theory of CS — hardware element
1172. F1172 Computer Architecture — lumped element
1173. F1173 Cryptography & Security — element of set
1174. F1174 Curriculum-only — time the element size
1175. F1175 Distributed Systems & Cloud — array
1176. F1176 Algorithms & Theory of CS — linear time
1177. F1177 Computer Architecture — phased arrays
1178. F1178 Distributed Systems & Cloud — titled
1179. F1179 ML & AI — iui
1180. F1180 Mathematics — element of sn
1181. F1181 Algorithms & Theory of CS — edge coloring of bipartite
1182. F1182 Curriculum-only — berge theorem
1183. F1183 Data Mining & Databases — lob theorem
1184. F1184 Distributed Systems & Cloud — pacelc theorem
1185. F1185 Information Theory & Coding — theorem of irrelevance
1186. F1186 Mathematics — complete
1187. F1187 Algorithms & Theory of CS — nl-complete
1188. F1188 Mathematics — existence
1189. F1189 Curriculum-only — existence of optima
1190. F1190 Mathematics — ksn
1191. F1191 Curriculum-only — projection cascade
1192. F1192 Mathematics — generalised projection
1193. F1193 Algorithms & Theory of CS — theorem of schur
1194. F1194 Mathematics — proof
1195. F1195 Algorithms & Theory of CS — graham-kleitman theorem
1196. F1196 Curriculum-only — developed with proof
1197. F1197 Data Mining & Databases — existence proof
1198. F1198 Distributed Systems & Cloud — proof of mnr labeling
1199. F1199 Information Theory & Coding — proof of birkhoff khintchine
1200. F1200 Mathematics — applying
1201. F1201 Curriculum-only — non-prime attribute
1202. F1202 Data Mining & Databases — tpr
1203. F1203 Mathematics — discriminant
1204. F1204 Curriculum-only — factoring rule
1205. F1205 Mathematics — clever
1206. F1206 Cryptography & Security — reconciliation
1207. F1207 Curriculum-only — application-assisted reconciliation
1208. F1208 Data Mining & Databases — lockout
1209. F1209 Curriculum-only — lockout policy
1210. F1210 Distributed Systems & Cloud — simulating process
1211. F1211 ML & AI — renewal
1212. F1212 Mathematics — llse of process
1213. F1213 Algorithms & Theory of CS — input receive
1214. F1214 Curriculum-only — receive task with data
1215. F1215 Mathematics — latex
1216. F1216 Computer Networks — kab
1217. F1217 Curriculum-only — send kb
1218. F1218 Mathematics — ses complete
1219. F1219 Algorithms & Theory of CS — tree of element setting
1220. F1220 Curriculum-only — adversarial setting with full information
1221. F1221 Mathematics — sketch
1222. F1222 Curriculum-only — misra gry sketch
1223. F1223 Data Mining & Databases — fm sketch
1224. F1224 Mathematics — split
1225. F1225 Curriculum-only — axis-aligned split
1226. F1226 ML & AI — multiway split
1227. F1227 Mathematics — stated
1228. F1228 Curriculum-only — kuratowski theorem stated
1229. F1229 Mathematics — theorem and proof
1230. F1230 Curriculum-only — order matter in practice
1231. F1231 Mathematics — implied volatility
1232. F1232 Computer Architecture — written response
1233. F1233 Curriculum-only — hand-written sampler
1234. F1234 Data Mining & Databases — you've written
1235. F1235 Distributed Systems & Cloud — written in rust
1236. F1236 Mathematics — xn xm
1237. F1237 NLP & Speech — complete-subtree
1238. F1238 Operating Systems — assertional proof
1239. F1239 Other/Unknown — ascoli theorem
1240. F1240 Curriculum-only — epidemic dynamics
1241. F1241 Distributed Systems & Cloud — future direction
1242. F1242 Mathematics — science
1243. F1243 Curriculum-only — role in industry and science
1244. F1244 Distributed Systems & Cloud — synchrony
1245. F1245 ML & AI — poem
1246. F1246 Mathematics — computational
1247. F1247 Curriculum-only — computational mac
1248. F1248 Mathematics — accurate computational shortcut
1249. F1249 Data Mining & Databases — jeffrey
1250. F1250 Computer Architecture — agarwal and jeffrey
1251. F1251 Mathematics — level
1252. F1252 Algorithms & Theory of CS — idealized level
1253. F1253 Curriculum-only — error-reporting level
1254. F1254 Data Mining & Databases — el0
1255. F1255 Distributed Systems & Cloud — high level
1256. F1256 Curriculum-only — high-level statement
1257. F1257 Distributed Systems & Cloud — pg level
1258. F1258 Information Theory & Coding — positive level evenly spaced
1259. F1259 ML & AI — mid-level
1260. F1260 Distributed Systems & Cloud — wait
1261. F1261 Mathematics — array gain
1262. F1262 Data Mining & Databases — abhinav gandhi
1263. F1263 Mathematics — level of mathematical rigor
1264. F1264 HS Maths Class XI / Unit-V Statistics and Probability — probability
1265. F1265 Algorithms & Theory of CS — complexity
1266. F1266 Cryptography & Security — m0 and m1
1267. F1267 Curriculum-only — close the mathematics
1268. F1268 Data Mining & Databases — classification
1269. F1269 Curriculum-only — classification approached with lp
1270. F1270 Data Mining & Databases — mathematics of data science
1271. F1271 Distributed Systems & Cloud — computability and complexity
1272. F1272 Information Theory & Coding — complexity pro le
1273. F1273 ML & AI — classification scheme
1274. F1274 Curriculum-only — v-prediction
1275. F1275 Data Mining & Databases — classification and prediction
1276. F1276 Mathematics — applied probability
1277. F1277 HS Maths Class XI / Unit-V Statistics and Probability — statistics
1278. F1278 Curriculum-only — arithmetic is stated
1279. F1279 Data Mining & Databases — language of arithmetic
1280. F1280 ML & AI — annal of statistics
1281. F1281 Distributed Systems & Cloud — computer
1282. F1282 Cryptography & Security — computer system
1283. F1283 Curriculum-only — computer-misuse statute
1284. F1284 Data Mining & Databases — computer help
1285. F1285 Distributed Systems & Cloud — anthony
1286. F1286 ML & AI — shuttle
1287. F1287 Mathematics — addition
1288. F1288 Data Mining & Databases — addition chain
1289. F1289 Mathematics — change of state
1290. F1290 Cryptography & Security — btc
1291. F1291 Mathematics — equality
1292. F1292 Data Mining & Databases — representing expression
1293. F1293 Distributed Systems & Cloud — arithmetic expression
1294. F1294 ML & AI — facial expression
1295. F1295 Mathematics — equivalent expression
1296. F1296 Computer Networks — fair queuing
1297. F1297 Mathematics — finite additivity
1298. F1298 Curriculum-only — axiom and their consequence
1299. F1299 Data Mining & Databases — tautological consequence
1300. F1300 ML & AI — consequence of action
1301. F1301 Mathematics — interpreting expectation
1302. F1302 Computer Architecture — aff
1303. F1303 Computer Networks — finish line
1304. F1304 Curriculum-only — track line
1305. F1305 Distributed Systems & Cloud — buffered
1306. F1306 Mathematics — dividing line
1307. F1307 Curriculum-only — edit log
1308. F1308 Data Mining & Databases — cs log
1309. F1309 Distributed Systems & Cloud — arrays
1310. F1310 HS Maths Class XII / Unit-IV: Vectors and Three-dimensional Geometry — vector
1311. F1311 Curriculum-only — full bit-vector
1312. F1312 Data Mining & Databases — lj yj
1313. F1313 Distributed Systems & Cloud — Disk arrays
1314. F1314 Information Theory & Coding — app vector
1315. F1315 Curriculum-only — one-bit and two-bit saturating counter
1316. F1316 ML & AI — epx
1317. F1317 Mathematics — direction vector
1318. F1318 Curriculum-only — anki flashcard
1319. F1319 Mathematics — equation
1320. F1320 Curriculum-only — distance between point and the equation
1321. F1321 Data Mining & Databases — weierstrass equation
1322. F1322 Mathematics — bessel equation
1323. F1323 Curriculum-only — hardware boundary
1324. F1324 Mathematics — c2 y2
1325. F1325 ML & AI — prediction di erence
1326. F1326 Mathematics — centered di erence
1327. F1327 Algorithms & Theory of CS — system of difference constraint
1328. F1328 Curriculum-only — difference are listed
1329. F1329 Mathematics — difference schemes
1330. F1330 Algorithms & Theory of CS — differential game
1331. F1331 Cryptography & Security — linear and differential
1332. F1332 Mathematics — c1 y1
1333. F1333 Curriculum-only — first-order method for ml
1334. F1334 Mathematics — first-order differential equation
1335. F1335 Algorithms & Theory of CS — intersection condition
1336. F1336 Mathematics — line segment
1337. F1337 Information Theory & Coding — rtt measurement
1338. F1338 Mathematics — mx1
1339. F1339 Algorithms & Theory of CS — input size
1340. F1340 Curriculum-only — cap choice made per operation
1341. F1341 Data Mining & Databases — operation on vector
1342. F1342 Distributed Systems & Cloud — rdd operation
1343. F1343 Mathematics — build
1344. F1344 Curriculum-only — from-scratch build
1345. F1345 Mathematics — overall
1346. F1346 Curriculum-only — category of response and overall
1347. F1347 Mathematics — perpendicular
1348. F1348 Algorithms & Theory of CS — marked with prob
1349. F1349 Mathematics — probability and statistics
1350. F1350 Algorithms & Theory of CS — cur and related
1351. F1351 Mathematics — relative
1352. F1352 Curriculum-only — zab as relative
1353. F1353 Data Mining & Databases — relative distance
1354. F1354 Information Theory & Coding — relative level
1355. F1355 Mathematics — relative gain
1356. F1356 Algorithms & Theory of CS — rural school
1357. F1357 Curriculum-only — eight-school data
1358. F1358 Data Mining & Databases — kid
1359. F1359 Mathematics — learned
1360. F1360 Algorithms & Theory of CS — binary try
1361. F1361 Curriculum-only — dangling node
1362. F1362 Data Mining & Databases — getnode
1363. F1363 Information Theory & Coding — check node
1364. F1364 Curriculum-only — mac flooding
1365. F1365 Information Theory & Coding — node capture
1366. F1366 ML & AI — node name
1367. F1367 Mathematics — set operation
1368. F1368 Information Theory & Coding — offered load
1369. F1369 Mathematics — staggered grid
1370. F1370 Distributed Systems & Cloud — palo alto
1371. F1371 Mathematics — sorry
1372. F1372 Algorithms & Theory of CS — bart
1373. F1373 Curriculum-only — max-sum subarray in linear time
1374. F1374 Distributed Systems & Cloud — gnode
1375. F1375 Information Theory & Coding — sum-rate
1376. F1376 Mathematics — Empty sum
1377. F1377 Algorithms & Theory of CS — coin crafting
1378. F1378 Mathematics — coin flipping
1379. F1379 Curriculum-only — prior justified
1380. F1380 Mathematics — je reys prior
1381. F1381 Computer Networks — type attribute
1382. F1382 Curriculum-only — client type
1383. F1383 Data Mining & Databases — type checker
1384. F1384 Distributed Systems & Cloud — instruction type
1385. F1385 Mathematics — type of group
1386. F1386 Curriculum-only — last-writer-win
1387. F1387 Mathematics — heather win
1388. F1388 Curriculum-only — event and caching
1389. F1389 Distributed Systems & Cloud — time and event
1390. F1390 Mathematics — event time
1391. F1391 Curriculum-only — event time and sketch
1392. F1392 Mathematics — fip
1393. F1393 Algorithms & Theory of CS — binary constraint
1394. F1394 Curriculum-only — find that the memo
1395. F1395 Data Mining & Databases — can't find
1396. F1396 Mathematics — nonzero number
1397. F1397 Curriculum-only — ml intuition
1398. F1398 Mathematics — won
1399. F1399 Algorithms & Theory of CS — type of prize
1400. F1400 Mathematics — x2 log
1401. F1401 Algorithms & Theory of CS — test vectors
1402. F1402 Computer Architecture — self-test
1403. F1403 Cryptography & Security — duck test
1404. F1404 Curriculum-only — error and test
1405. F1405 Distributed Systems & Cloud — test-lab-3
1406. F1406 Information Theory & Coding — binary test
1407. F1407 Mathematics — compare
1408. F1408 Curriculum-only — build and compare
1409. F1409 Data Mining & Databases — compare to knn
1410. F1410 Mathematics — comparison test
1411. F1411 NLP & Speech — advp np
1412. F1412 Mathematics — cost
1413. F1413 Algorithms & Theory of CS — copt
1414. F1414 Cryptography & Security — cost of communicating
1415. F1415 Curriculum-only — cost in bit operation
1416. F1416 Data Mining & Databases — cost metrics
1417. F1417 Mathematics — compute
1418. F1418 Data Mining & Databases — attempt to compute
1419. F1419 Information Theory & Coding — compute pext
1420. F1420 Mathematics — a2 ab
1421. F1421 Curriculum-only — computed automatically
1422. F1422 Mathematics — cost change
1423. F1423 NLP & Speech — i-vector
1424. F1424 Operating Systems — athletic event
1425. F1425 Mathematics — easy
1426. F1426 ML & AI — easy and hard
1427. F1427 Mathematics — self-adjointness
1428. F1428 Operating Systems — level-triggered
1429. F1429 Other/Unknown — atmospheric science
1430. F1430 Cryptography & Security — das and nr
1431. F1431 Distributed Systems & Cloud — gupta
1432. F1432 Mathematics — edition
1433. F1433 Curriculum-only — check the current edition
1434. F1434 Distributed Systems & Cloud — kumar
1435. F1435 Computer Networks — ravi kumar
1436. F1436 Data Mining & Databases — sreenivasa kumar
1437. F1437 Distributed Systems & Cloud — shankar
1438. F1438 ML & AI — lee
1439. F1439 Distributed Systems & Cloud — edward lee
1440. F1440 Mathematics — abhinav kumar
1441. F1441 Other/Unknown — divided difference
1442. F1442 Distributed Systems & Cloud — maxwell krohn
1443. F1443 Other/Unknown — newton divided difference
1444. F1444 Distributed Systems & Cloud — queuing system
1445. F1445 Other/Unknown — rank test
1446. F1446 Mathematics — least-square
1447. F1447 Curriculum-only — alternating least square
1448. F1448 Mathematics — least-square line
1449. F1449 Other/Unknown — reverse engineering
1450. F1450 Mathematics — phenomenon
1451. F1451 Other/Unknown — truth-functionally complete
1452. F1452 Signal/Image/Audio/Video Processing — av node
1453. F1453 Mathematics — mean
1454. F1454 Algorithms & Theory of CS — gavagai
1455. F1455 Curriculum-only — mean number in system
1456. F1456 Information Theory & Coding — optimality of zero-mean constellation
1457. F1457 Mathematics — aov
1458. F1458 Algorithms & Theory of CS — axin
1459. F1459 Computer Architecture — independent equation
1460. F1460 Computer Networks — independent binary
1461. F1461 Mathematics — arrival time
1462. F1462 Information Theory & Coding — rst observe
1463. F1463 Mathematics — wise independent
1464. F1464 Algorithms & Theory of CS — k-wise independent
1465. F1465 Curriculum-only — min-wise independent family
1466. F1466 Other/Unknown — possibilistic c-means
1467. F1467 Signal/Image/Audio/Video Processing — depicted in osb
1468. F1468 Information Theory & Coding — noise
1469. F1469 Computer Architecture — remove noise
1470. F1470 Curriculum-only — noise schedule
1471. F1471 Information Theory & Coding — di culty
1472. F1472 Mathematics — identity
1473. F1473 Curriculum-only — zout identity
1474. F1474 Mathematics — identity operator
1475. F1475 NLP & Speech — noise robustness
1476. F1476 Mathematics — confidence
1477. F1477 Other/Unknown — flicker noise
1478. F1478 Signal/Image/Audio/Video Processing — einstein-wiener-khinchin theorem
1479. F1479 Cryptography & Security — vm image
1480. F1480 Curriculum-only — image as vector
1481. F1481 Data Mining & Databases — bright
1482. F1482 Information Theory & Coding — reconstructed image
1483. F1483 ML & AI — noisy image
1484. F1484 Mathematics — light
1485. F1485 ML & AI — training
1486. F1486 Curriculum-only — cnn training
1487. F1487 Data Mining & Databases — error report
1488. F1488 Distributed Systems & Cloud — ml training
1489. F1489 Information Theory & Coding — training sequence
1490. F1490 ML & AI — classification function
1491. F1491 NLP & Speech — accent
1492. F1492 Other/Unknown — hyper-spectral images
1493. F1493 Signal/Image/Audio/Video Processing — brightness
1494. F1494 Mathematics — depending
1495. F1495 Signal/Image/Audio/Video Processing — level detail
1496. F1496 Software Engineering — ada
1497. F1497 Information Theory & Coding — body temperature
1498. F1498 Software Engineering — bogo
1499. F1499 Curriculum-only — buffer sizing
1500. F1500 Data Mining & Databases — buffer pool
1501. F1501 Software Engineering — array buffer
1502. F1502 Data Mining & Databases — brain
1503. F1503 ML & AI — synapse
1504. F1504 Mathematics — connection
1505. F1505 Algorithms & Theory of CS — connection to rsk
1506. F1506 Computer Networks — data connection
1507. F1507 Curriculum-only — connection draining
1508. F1508 Mathematics — dose
1509. F1509 NLP & Speech — poggio
1510. F1510 Operating Systems — connection-oriented
1511. F1511 Software Engineering — computational component
1512. F1512 Data Mining & Databases — computational component learned
1513. F1513 Software Engineering — computer language
1514. F1514 Mathematics — landing
1515. F1515 NLP & Speech — removed for copyright reason
1516. F1516 Computer Networks — attachment
1517. F1517 Mathematics — graph
1518. F1518 Algorithms & Theory of CS — borg
1519. F1519 Algorithms & Theory of CS — nbc theorem
1520. F1520 Curriculum-only — colouring of graph
1521. F1521 Distributed Systems & Cloud — data graph
1522. F1522 Information Theory & Coding — bi-partite graph
1523. F1523 ML & AI — intersection graph
1524. F1524 Mathematics — connected
1525. F1525 Algorithms & Theory of CS — choice of cycle
1526. F1526 Curriculum-only — crisp-dm cycle named
1527. F1527 Distributed Systems & Cloud — cycle accurate
1528. F1528 Information Theory & Coding — temperature cycle
1529. F1529 ML & AI — chordless cycle
1530. F1530 Distributed Systems & Cloud — read
1531. F1531 Algorithms & Theory of CS — read and solve
1532. F1532 Computer Architecture — line read
1533. F1533 Curriculum-only — billion read
1534. F1534 Curriculum-only — read can outnumber write
1535. F1535 Curriculum-only — thousand read
1536. F1536 Data Mining & Databases — hard to read
1537. F1537 Curriculum-only — non-repeatable read
1538. F1538 Distributed Systems & Cloud — disk read
1539. F1539 Mathematics — definition
1540. F1540 Computer Networks — silver bullet
1541. F1541 Curriculum-only — lp and its definition
1542. F1542 Data Mining & Databases — current definition
1543. F1543 Distributed Systems & Cloud — t1 t2
1544. F1544 Mathematics — biconditional
1545. F1545 Algorithms & Theory of CS — addedge
1546. F1546 Computer Architecture — edge map
1547. F1547 Curriculum-only — dfs tree and edge classification
1548. F1548 Data Mining & Databases — analytics edge
1549. F1549 Distributed Systems & Cloud — edge rdd
1550. F1550 ML & AI — set of node
1551. F1551 Mathematics — formal
1552. F1552 Distributed Systems & Cloud — safety and liveness
1553. F1553 Mathematics — formal definition
1554. F1554 Algorithms & Theory of CS — binary search
1555. F1555 Curriculum-only — average or complex
1556. F1556 Data Mining & Databases — batting average
1557. F1557 Information Theory & Coding — average number
1558. F1558 Mathematics — lightly
1559. F1559 Curriculum-only — multiplication multiply moduli
1560. F1560 Data Mining & Databases — binary multiplication
1561. F1561 Mathematics — base
1562. F1562 Computer Architecture — base addr
1563. F1563 Curriculum-only — base plus
1564. F1564 Data Mining & Databases — factor base
1565. F1565 Mathematics — count
1566. F1566 Algorithms & Theory of CS — hop count
1567. F1567 Computer Architecture — line count
1568. F1568 Curriculum-only — average hop count
1569. F1569 Distributed Systems & Cloud — character count
1570. F1570 Mathematics — fallacy
1571. F1571 Curriculum-only — standard fallacy
1572. F1572 Mathematics — multiplication modulo
1573. F1573 Curriculum-only — definition use pair
1574. F1574 Data Mining & Databases — kxi xj
1575. F1575 Mathematics — distinct
1576. F1576 Curriculum-only — sketch for distinct count
1577. F1577 Distributed Systems & Cloud — distinct ip
1578. F1578 Mathematics — garden
1579. F1579 Computer Networks — product line
1580. F1580 Curriculum-only — compare product
1581. F1581 Data Mining & Databases — exploratory
1582. F1582 Mathematics — ai bi
1583. F1583 Curriculum-only — cross-producting
1584. F1584 Mathematics — product group
1585. F1585 Algorithms & Theory of CS — cross product
1586. F1586 Curriculum-only — dot and cross product
1587. F1587 Mathematics — random walk on graph
1588. F1588 Algorithms & Theory of CS — gnfa
1589. F1589 Mathematics — related to graph
1590. F1590 Curriculum-only — product-to-sum and sum-to-product
1591. F1591 Mathematics — testing
1592. F1592 Curriculum-only — baillie psw testing
1593. F1593 Data Mining & Databases — average of loo testing
1594. F1594 Mathematics — typo
1595. F1595 Computer Architecture — compare value read
1596. F1596 Curriculum-only — error as value
1597. F1597 Data Mining & Databases — id in expr
1598. F1598 Distributed Systems & Cloud — value prediction
1599. F1599 ML & AI — number of component
1600. F1600 Mathematics — apx
1601. F1601 Curriculum-only — evaluate computational
1602. F1602 Data Mining & Databases — predicate expression
1603. F1603 Distributed Systems & Cloud — order of operation
1604. F1604 Mathematics — improper integral
1605. F1605 Curriculum-only — proof of the mean value theorem
1606. F1606 Mathematics — minimum value
1607. F1607 NLP & Speech — atomic value
1608. F1608 Operating Systems — atomic read
1609. F1609 Mathematics — practical
1610. F1610 Computer Networks — practical experience
1611. F1611 Distributed Systems & Cloud — practical mutual exclusion algorithm
1612. F1612 Mathematics — equip
1613. F1613 Operating Systems — average run-length
1614. F1614 Other/Unknown — count-min
1615. F1615 Curriculum-only — count-min and count sketch
1616. F1616 Other/Unknown — count-min sketch
1617. F1617 Other/Unknown — symmetric and skew-symmetric
1618. F1618 Signal/Image/Audio/Video Processing — complex addition
1619. F1619 Software Engineering — counting operation
1620. F1620 Curriculum-only — mccabe cyclomatic complexity
1621. F1621 Software Engineering — deadpool
1622. F1622 Mathematics — division
1623. F1623 Curriculum-only — division by multiplying numerator
1624. F1624 ML & AI — mathematical science
1625. F1625 Software Engineering — div
1626. F1626 Software Engineering — function call
1627. F1627 Curriculum-only — function from handler to handler
1628. F1628 Software Engineering — high-level programming
1629. F1629 Distributed Systems & Cloud — high level language
1630. F1630 Algorithms & Theory of CS — connectivity
1631. F1631 Computer Architecture — dynamic discipline
1632. F1632 Computer Networks — dynamic sql
1633. F1633 Curriculum-only — connectivity test
1634. F1634 Distributed Systems & Cloud — dynamic extent
1635. F1635 Mathematics — connectivity and tree
1636. F1636 Other/Unknown — dynamic re-configuration
1637. F1637 Software Engineering — increasing complexity
1638. F1638 Curriculum-only — preinstantiate and maintain
1639. F1639 Software Engineering — malleability
1640. F1640 Cryptography & Security — malleability of el gamal
1641. F1641 Software Engineering — meyer
1642. F1642 Curriculum-only — davy meyer
1643. F1643 Software Engineering — million element
1644. F1644 Mathematics — constant
1645. F1645 Algorithms & Theory of CS — E (mathematical constant)
1646. F1646 Computer Architecture — vcp
1647. F1647 Curriculum-only — set expected constant
1648. F1648 Data Mining & Databases — constant x1
1649. F1649 Information Theory & Coding — constant rate
1650. F1650 ML & AI — arity
1651. F1651 Mathematics — coefficient
1652. F1652 Curriculum-only — circular array
1653. F1653 Mathematics — cover-up
1654. F1654 Curriculum-only — plus homogeneous
1655. F1655 Mathematics — order linear equation
1656. F1656 NLP & Speech — cepstral coefficients
1657. F1657 Other/Unknown — linear system with constant
1658. F1658 Curriculum-only — homogeneous and non-homogeneous system
1659. F1659 Other/Unknown — thermal conductivity
1660. F1660 Signal/Image/Audio/Video Processing — connection coefficient
1661. F1661 Software Engineering — coefficient bk
1662. F1662 Curriculum-only — product name and tier change
1663. F1663 Software Engineering — pvalue
1664. F1664 Curriculum-only — random testing as the base
1665. F1665 Software Engineering — read balance
1666. F1666 Software Engineering — rotator
1667. F1667 Other/Unknown — planning
1668. F1668 Algorithms & Theory of CS — planning algorithm
1669. F1669 Curriculum-only — planning of the next loop
1670. F1670 Data Mining & Databases — staffing
1671. F1671 Mathematics — iii
1672. F1672 Computer Architecture — ii iii
1673. F1673 Curriculum-only — sql iii
1674. F1674 Mathematics — ii and iii
1675. F1675 Other/Unknown — factor affecting
1676. F1676 Computer Networks — forecasting system
1677. F1677 Curriculum-only — forecasting and operation
1678. F1678 Other/Unknown — maintenance
1679. F1679 Algorithms & Theory of CS — order maintenance
1680. F1680 Mathematics — immediately
1681. F1681 Other/Unknown — process planning
1682. F1682 Signal/Image/Audio/Video Processing — lsi
1683. F1683 Software Engineering — rt ui
1684. F1684 Software Engineering — sequence of byte
1685. F1685 Mathematics — surely
1686. F1686 Other/Unknown — ideal gas
1687. F1687 Software Engineering — shell scripting
1688. F1688 CS2023 gap-fill — File abstraction and operators
1689. F1689 Distributed Systems & Cloud — workflow
1690. F1690 Curriculum-only — msfconsole workflow
1691. F1691 Software Engineering — sho
1692. F1692 Curriculum-only — cycle-level simulator
1693. F1693 Software Engineering — singly
1694. F1694 Curriculum-only — slo and slas
1695. F1695 Software Engineering — software development process
1696. F1696 Computer Networks — agile process
1697. F1697 Curriculum-only — agile fit
1698. F1698 Distributed Systems & Cloud — organization
1699. F1699 Computer Architecture — organization and architecture
1700. F1700 Curriculum-only — physical unclonable function
1701. F1701 Data Mining & Databases — data organization
1702. F1702 Operating Systems — os organization
1703. F1703 Other/Unknown — accelerator
1704. F1704 Curriculum-only — cnn accelerator
1705. F1705 Other/Unknown — chiplet
1706. F1706 Curriculum-only — chiplet joined over an interposer
1707. F1707 Other/Unknown — computer organization
1708. F1708 Distributed Systems & Cloud — parallel computer organization
1709. F1709 Other/Unknown — fpga
1710. F1710 Computer Architecture — xilinx fpga
1711. F1711 Other/Unknown — quantum
1712. F1712 Algorithms & Theory of CS — Quantum factoring (Shor's Algorithm)
1713. F1713 ML & AI — quantum golfing
1714. F1714 Other/Unknown — mechanical system
1715. F1715 Software Engineering — soup
1716. F1716 Signal/Image/Audio/Video Processing — set of speci cation
1717. F1717 Software Engineering — specification
1718. F1718 Curriculum-only — specification can be wrong
1719. F1719 Mathematics — formal proof
1720. F1720 Software Engineering — Specification languages
1721. F1721 Mathematics — startup in palo alto
1722. F1722 Software Engineering — statics dynamics
1723. F1723 Algorithms & Theory of CS — lg nk
1724. F1724 Curriculum-only — content store
1725. F1725 Data Mining & Databases — graph store
1726. F1726 Information Theory & Coding — object store
1727. F1727 Curriculum-only — rest in the object store
1728. F1728 Mathematics — min and max
1729. F1729 Curriculum-only — min and max size
1730. F1730 Operating Systems — store set
1731. F1731 Software Engineering — strictness
1732. F1732 NLP & Speech — effect of syntactic complexity
1733. F1733 Software Engineering — syntactic sugar
1734. F1734 Mathematics — white
1735. F1735 Curriculum-only — white-list
1736. F1736 Distributed Systems & Cloud — tom white
1737. F1737 Software Engineering — char
1738. F1738 Distributed Systems & Cloud — buf
1739. F1739 Operating Systems — outb
1740. F1740 ML & AI — mask
1741. F1741 Mathematics — annealing
1742. F1742 Software Engineering — Numeric vs non-numeric, character strings
1743. F1743 Mathematics — vertical
1744. F1744 Algorithms & Theory of CS — vertical ray shooting
1745. F1745 Computer Architecture — vertical deflection
1746. F1746 Mathematics — dimensional
1747. F1747 Curriculum-only — three-dimensional grid
1748. F1748 Data Mining & Databases — dimensional data
1749. F1749 ML & AI — low-dimensional
1750. F1750 Mathematics — complex vector
1751. F1751 Algorithms & Theory of CS — bound on chromatic number
1752. F1752 Curriculum-only — missing bound check
1753. F1753 Data Mining & Databases — vikram srinivasan
1754. F1754 Distributed Systems & Cloud — conn
1755. F1755 Information Theory & Coding — dependence-testing bound
1756. F1756 ML & AI — margin bound
1757. F1757 Mathematics — explicit calculation
1758. F1758 Algorithms & Theory of CS — lower bound to ramsey
1759. F1759 Curriculum-only — generic-group lower bound
1760. F1760 Mathematics — upper
1761. F1761 ML & AI — corr
1762. F1762 Mathematics — s1 s2
1763. F1763 ML & AI — s1 s2 s3
1764. F1764 Signal/Image/Audio/Video Processing — bound on y2
1765. F1765 Curriculum-only — cycle detection in precedence graph
1766. F1766 Distributed Systems & Cloud — conflict detection
1767. F1767 Information Theory & Coding — coherent detection
1768. F1768 Mathematics — detection probabilities
1769. F1769 Other/Unknown — change detection
1770. F1770 Curriculum-only — miscellaneous system
1771. F1771 Signal/Image/Audio/Video Processing — probability of detection
1772. F1772 Software Engineering — taproot
1773. F1773 Algorithms & Theory of CS — command window
1774. F1774 Curriculum-only — command activate
1775. F1775 ML & AI — rtrain
1776. F1776 Mathematics — gaussian
1777. F1777 Curriculum-only — gaussian marginalization
1778. F1778 Information Theory & Coding — gaussian rv
1779. F1779 ML & AI — gaussian graphical model
1780. F1780 Mathematics — curvature
1781. F1781 NLP & Speech — speech
1782. F1782 Computer Networks — bos
1783. F1783 Distributed Systems & Cloud — speech synthesizer
1784. F1784 Information Theory & Coding — speech error
1785. F1785 NLP & Speech — acoustic
1786. F1786 Information Theory & Coding — acoustic consequence
1787. F1787 NLP & Speech — acoustic impedance
1788. F1788 Other/Unknown — Hate speech
1789. F1789 Signal/Image/Audio/Video Processing — cjk
1790. F1790 Mathematics — boston
1791. F1791 Computer Networks — san francisco
1792. F1792 Data Mining & Databases — phoenix
1793. F1793 Signal/Image/Audio/Video Processing — lung
1794. F1794 Software Engineering — postfix
1795. F1795 Distributed Systems & Cloud — infix
1796. F1796 Software Engineering — infix to postfix
1797. F1797 Mathematics — failure
1798. F1798 Algorithms & Theory of CS — failure probability
1799. F1799 Curriculum-only — context failure
1800. F1800 Distributed Systems & Cloud — classification of failure
1801. F1801 Information Theory & Coding — handling failure
1802. F1802 Mathematics — failure rate
1803. F1803 Operating Systems — dealing with disk failure
1804. F1804 Other/Unknown — failure data
1805. F1805 Software Engineering — tenv
1806. F1806 Software Engineering — tvar
1807. F1807 Software Engineering — vad
1808. F1808 Software Engineering — wcs
1809. F1809 Distributed Systems & Cloud — structure
1810. F1810 HS ComputerScience Class XII / Unit 1: Computational Thinking and Programming – 2 — data structure
1811. F1811 Algorithms & Theory of CS — binary search tree
1812. F1812 Computer Networks — timeline
1813. F1813 Cryptography & Security — quoting
1814. F1814 Curriculum-only — augmenting data structure
1815. F1815 Curriculum-only — structure of the data
1816. F1816 Data Mining & Databases — geometric structure
1817. F1817 Algorithms & Theory of CS — geometric structure related
1818. F1818 Data Mining & Databases — high-dimensionality structure
1819. F1819 Distributed Systems & Cloud — Array data structure
1820. F1820 Mathematics — extra structure
1821. F1821 NLP & Speech — data structure algorithm
1822. F1822 Other/Unknown — organisation structure
1823. F1823 Signal/Image/Audio/Video Processing — cascade structure
1824. F1824 Software Engineering — amortized
1825. F1825 Curriculum-only — amortised context
1826. F1826 Software Engineering — array-of-structure
1827. F1827 Algorithms & Theory of CS — pr fer code
1828. F1828 Computer Architecture — check-off
1829. F1829 Computer Networks — code to load
1830. F1830 Cryptography & Security — arbitrary code
1831. F1831 Curriculum-only — code over gf
1832. F1832 Data Mining & Databases — code number
1833. F1833 Distributed Systems & Cloud — list size
1834. F1834 Information Theory & Coding — abnnr code
1835. F1835 Computer Architecture — encoding tree
1836. F1836 Curriculum-only — ber encoding
1837. F1837 Information Theory & Coding — error correcting
1838. F1838 Curriculum-only — error-detecting and error-correcting code
1839. F1839 Information Theory & Coding — fixed-length
1840. F1840 Curriculum-only — char for fixed length
1841. F1841 Information Theory & Coding — fixed-length encoding
1842. F1842 Algorithms & Theory of CS — paperback
1843. F1843 ML & AI — boilerplate code
1844. F1844 Mathematics — aleph
1845. F1845 Distributed Systems & Cloud — marc
1846. F1846 Mathematics — density
1847. F1847 Computer Architecture — air density
1848. F1848 Curriculum-only — distance and by density
1849. F1849 Information Theory & Coding — density parity check code
1850. F1850 Mathematics — area
1851. F1851 Algorithms & Theory of CS — area yield
1852. F1852 Data Mining & Databases — area ii
1853. F1853 Information Theory & Coding — area code
1854. F1854 ML & AI — follow-up
1855. F1855 Mathematics — base area
1856. F1856 Curriculum-only — board summary is readable
1857. F1857 Mathematics — cm2
1858. F1858 Curriculum-only — curriculum figure depend
1859. F1859 Mathematics — easier to understand
1860. F1860 Curriculum-only — multiplicative for multiplication
1861. F1861 Data Mining & Databases — multiplicative order
1862. F1862 Information Theory & Coding — multiplicative noise
1863. F1863 Mathematics — completely multiplicative
1864. F1864 Curriculum-only — shorter page load
1865. F1865 Mathematics — significant
1866. F1866 Algorithms & Theory of CS — significant set
1867. F1867 Curriculum-only — significant data fiduciary
1868. F1868 ML & AI — entail significant
1869. F1869 Mathematics — awarded
1870. F1870 Computer Architecture — sinusoidal steady state
1871. F1871 Distributed Systems & Cloud — volume set
1872. F1872 Information Theory & Coding — hearing
1873. F1873 Mathematics — wellesley cambridge press
1874. F1874 NLP & Speech — speech and hearing
1875. F1875 Operating Systems — instruction encoding
1876. F1876 Other/Unknown — compliance
1877. F1877 Cryptography & Security — regulatory compliance
1878. F1878 Curriculum-only — compliance report
1879. F1879 Other/Unknown — density of state
1880. F1880 Signal/Image/Audio/Video Processing — microphone
1881. F1881 Distributed Systems & Cloud — microphone arrays
1882. F1882 NLP & Speech — speaker
1883. F1883 Mathematics — adapted
1884. F1884 NLP & Speech — phonetic
1885. F1885 Mathematics — word
1886. F1886 Curriculum-only — predicting the next word
1887. F1887 Distributed Systems & Cloud — word co-occurrence
1888. F1888 ML & AI — one-hot vector
1889. F1889 Curriculum-only — one-hot vector and classification
1890. F1890 ML & AI — vocabulary
1891. F1891 Curriculum-only — graph vocabulary
1892. F1892 ML & AI — word prediction
1893. F1893 Mathematics — caution
1894. F1894 Information Theory & Coding — nak
1895. F1895 ML & AI — geometric meaning
1896. F1896 Mathematics — character sets
1897. F1897 ML & AI — ea etb
1898. F1898 Mathematics — mathematical writing
1899. F1899 Curriculum-only — mathematical writing and how to read
1900. F1900 Mathematics — probabilistic meaning
1901. F1901 NLP & Speech — lexicon
1902. F1902 Computer Architecture — one-sentence
1903. F1903 Curriculum-only — sentence-level task
1904. F1904 Data Mining & Databases — sc sentence
1905. F1905 Information Theory & Coding — sentence-level phenomenon in speech
1906. F1906 ML & AI — phi
1907. F1907 NLP & Speech — discourse
1908. F1908 Mathematics — iff
1909. F1909 Cryptography & Security — valid char
1910. F1910 Curriculum-only — bound must be valid
1911. F1911 Data Mining & Databases — set of sentence valid
1912. F1912 Information Theory & Coding — value of pi
1913. F1913 NLP & Speech — speaker diarisation
1914. F1914 Algorithms & Theory of CS — arbitrarily long
1915. F1915 NLP & Speech — word spotting
1916. F1916 Operating Systems — couple sentence
1917. F1917 Other/Unknown — equivalent sentence
1918. F1918 Algorithms & Theory of CS — propositional proofs
1919. F1919 Mathematics — pigeon
1920. F1920 Other/Unknown — quantified sentence
1921. F1921 Mathematics — completeness
1922. F1922 Curriculum-only — completeness of rn
1923. F1923 Other/Unknown — set of sl sentence
1924. F1924 Signal/Image/Audio/Video Processing — ventricular escape beat
1925. F1925 Software Engineering — character code
1926. F1926 HS ComputerScience Class XI / Unit 2: Computational Thinking and Programming - I — dictionary
1927. F1927 Software Engineering — code inspection
1928. F1928 Curriculum-only — packed data type
1929. F1929 Distributed Systems & Cloud — mpi derived data type
1930. F1930 Mathematics — multiset
1931. F1931 Software Engineering — abstract data type
1932. F1932 Algorithms & Theory of CS — delete
1933. F1933 Curriculum-only — delete by tombstone
1934. F1934 Software Engineering — avx2
1935. F1935 Mathematics — record
1936. F1936 Computer Architecture — input record
1937. F1937 Computer Networks — ns record
1938. F1938 Curriculum-only — checksummed record
1939. F1939 Software Engineering — data-structure augmentation
1940. F1940 Algorithms & Theory of CS — insert and delete
1941. F1941 Curriculum-only — giving read priority over write
1942. F1942 Distributed Systems & Cloud — implement process wait
1943. F1943 Software Engineering — incremental change
1944. F1944 Computer Networks — version of python
1945. F1945 Curriculum-only — lazily evaluated property in python
1946. F1946 Curriculum-only — svm in python
1947. F1947 Data Mining & Databases — python language
1948. F1948 Curriculum-only — multiprocessing remain the tool for the python-language
1949. F1949 Information Theory & Coding — python ps7
1950. F1950 ML & AI — implemented in python
1951. F1951 Mathematics — graphing
1952. F1952 Curriculum-only — cause effect graphing
1953. F1953 Mathematics — derivative of product
1954. F1954 Software Engineering — data attribute
1955. F1955 Mathematics — coordinate
1956. F1956 Cryptography & Security — relief
1957. F1957 Curriculum-only — coordinate on write
1958. F1958 Data Mining & Databases — asked to coordinate
1959. F1959 Distributed Systems & Cloud — sdf
1960. F1960 Mathematics — pair of coordinate
1961. F1961 Other/Unknown — animal
1962. F1962 Data Mining & Databases — farm
1963. F1963 NLP & Speech — frog
1964. F1964 Mathematics — dart
1965. F1965 Software Engineering — matter in python
1966. F1966 Mathematics — understanding
1967. F1967 Data Mining & Databases — understanding food
1968. F1968 Distributed Systems & Cloud — in-depth understanding
1969. F1969 ML & AI — poor understanding
1970. F1970 Mathematics — deeper
1971. F1971 Curriculum-only — start broad and go deeper
1972. F1972 NLP & Speech — speech understanding
1973. F1973 Software Engineering — record type
1974. F1974 Curriculum-only — dns record type
1975. F1975 Software Engineering — set code
1976. F1976 Computer Architecture — signed data
1977. F1977 Distributed Systems & Cloud — vector signed
1978. F1978 Mathematics — signed-rank
1979. F1979 Other/Unknown — signed rank test
1980. F1980 Software Engineering — cond
1981. F1981 Computer Networks — cdr
1982. F1982 Data Mining & Databases — cadr
1983. F1983 Information Theory & Coding — input and output
1984. F1984 Mathematics — exp
1985. F1985 ML & AI — iej
1986. F1986 Mathematics — upper bounded
1987. F1987 Software Engineering — exp body
1988. F1988 Curriculum-only — practical instantiation
1989. F1989 Distributed Systems & Cloud — instantiation rule
1990. F1990 Software Engineering — stack
1991. F1991 Algorithms & Theory of CS — stack symbol
1992. F1992 Curriculum-only — axiom of the stack
1993. F1993 Data Mining & Databases — current environment
1994. F1994 Distributed Systems & Cloud — call tree
1995. F1995 Mathematics — multidimensional
1996. F1996 Algorithms & Theory of CS — modi cation
1997. F1997 Computer Architecture — code to reduce cdma
1998. F1998 Curriculum-only — reduce average
1999. F1999 Mathematics — stacking
2000. F2000 Operating Systems — stack isa
2001. F2001 Other/Unknown — imap-reduce
2002. F2002 Software Engineering — function pointer
2003. F2003 Algorithms & Theory of CS — avl
2004. F2004 Curriculum-only — arrays and linked list
2005. F2005 Mathematics — direct
2006. F2006 Cryptography & Security — insecure direct object
2007. F2007 Mathematics — double
2008. F2008 Algorithms & Theory of CS — double hashing
2009. F2009 Cryptography & Security — double spend
2010. F2010 Curriculum-only — double dogleg
2011. F2011 Data Mining & Databases — double-edged sword
2012. F2012 Mathematics — const double
2013. F2013 Algorithms & Theory of CS — avl tree
2014. F2014 Curriculum-only — add an item
2015. F2015 Data Mining & Databases — apriori
2016. F2016 ML & AI — item set
2017. F2017 Mathematics — walk on binary tree
2018. F2018 Other/Unknown — item and lsh
2019. F2019 Software Engineering — abstraction
2020. F2020 Computer Architecture — language abstraction
2021. F2021 Distributed Systems & Cloud — log abstraction
2022. F2022 Mathematics — abstraction mean
2023. F2023 Software Engineering — address
2024. F2024 Cryptography & Security — mac address
2025. F2025 Curriculum-only — address of element
2026. F2026 Data Mining & Databases — feeding time
2027. F2027 Distributed Systems & Cloud — disk address
2028. F2028 Operating Systems — address mapping
2029. F2029 Software Engineering — address stack
2030. F2030 Mathematics — world
2031. F2031 Computer Networks — highly connected world
2032. F2032 Cryptography & Security — myth
2033. F2033 Data Mining & Databases — war
2034. F2034 ML & AI — world dynamics
2035. F2035 Mathematics — bottom line
2036. F2036 Computer Networks — count include
2037. F2037 Data Mining & Databases — include pa
2038. F2038 Mathematics — solving
2039. F2039 Other/Unknown — Equation solving
2040. F2040 Software Engineering — iostream
2041. F2041 Algorithms & Theory of CS — write correct
2042. F2042 Computer Networks — training program
2043. F2043 Cryptography & Security — program to delete
2044. F2044 Curriculum-only — call chain client program
2045. F2045 Data Mining & Databases — infinite loop
2046. F2046 Distributed Systems & Cloud — hotspot
2047. F2047 Data Mining & Databases — relational
2048. F2048 Curriculum-only — eer to relational mapping
2049. F2049 Data Mining & Databases — object-relational
2050. F2050 Distributed Systems & Cloud — nasa
2051. F2051 Data Mining & Databases — nsf data
2052. F2052 Distributed Systems & Cloud — profiler
2053. F2053 Curriculum-only — non-relational data
2054. F2054 Distributed Systems & Cloud — tempo program
2055. F2055 Mathematics — inb
2056. F2056 Curriculum-only — sensitivity and interior-point
2057. F2057 Mathematics — klee
2058. F2058 Distributed Systems & Cloud — execution
2059. F2059 Computer Networks — process execution
2060. F2060 Cryptography & Security — concolic execution
2061. F2061 Curriculum-only — execution as event sequence
2062. F2062 Distributed Systems & Cloud — incorrect execution
2063. F2063 Mathematics — contain infinitely
2064. F2064 Algorithms & Theory of CS — odd cycle
2065. F2065 Curriculum-only — equalised odd
2066. F2066 Data Mining & Databases — odd of adopting
2067. F2067 Mathematics — odd size
2068. F2068 Algorithms & Theory of CS — brian william
2069. F2069 Computer Architecture — william putnam
2070. F2070 Distributed Systems & Cloud — leevar william
2071. F2071 Mathematics — consistent
2072. F2072 Data Mining & Databases — consistent state
2073. F2073 Distributed Systems & Cloud — consistent hashing
2074. F2074 Curriculum-only — consistent hashing reduce the data moved
2075. F2075 NLP & Speech — feasible pair
2076. F2076 Operating Systems — data consistent
2077. F2077 Other/Unknown — consistent set
2078. F2078 Signal/Image/Audio/Video Processing — z-n
2079. F2079 Software Engineering — abstract syntax tree
2080. F2080 Mathematics — table
2081. F2081 Algorithms & Theory of CS — load factor
2082. F2082 Computer Networks — add table
2083. F2083 Curriculum-only — account api writing the account table
2084. F2084 Curriculum-only — table ageing
2085. F2085 Data Mining & Databases — hibernate
2086. F2086 Distributed Systems & Cloud — finger table
2087. F2087 Information Theory & Coding — punctuation mark
2088. F2088 ML & AI — piece of information
2089. F2089 Mathematics — cr4
2090. F2090 Operating Systems — physical memory
2091. F2091 Software Engineering — algorithm to program
2092. F2092 Distributed Systems & Cloud — queue
2093. F2093 Algorithms & Theory of CS — binary heap
2094. F2094 Curriculum-only — axiom of the stack and queue
2095. F2095 Distributed Systems & Cloud — command queue
2096. F2096 Information Theory & Coding — queue lengths
2097. F2097 Mathematics — pollaczek-khinchin
2098. F2098 Operating Systems — droptail
2099. F2099 Other/Unknown — Discrete-event simulation
2100. F2100 Mathematics — discrete
2101. F2101 Algorithms & Theory of CS — discrete mathematical
2102. F2102 Curriculum-only — deterministic discrete
2103. F2103 Distributed Systems & Cloud — discrete transition
2104. F2104 Mathematics — discrete optimization
2105. F2105 ML & AI — nonnegative rank
2106. F2106 Mathematics — nonnegative discrete rv
2107. F2107 Other/Unknown — discrete choice
2108. F2108 Mathematics — jackson
2109. F2109 Other/Unknown — standard discrete
2110. F2110 Software Engineering — data object
2111. F2111 Curriculum-only — declarative reconciliation
2112. F2112 Data Mining & Databases — declarative querying
2113. F2113 Software Engineering — deterministic execution
2114. F2114 Curriculum-only — execute-never
2115. F2115 Distributed Systems & Cloud — hive to execute
2116. F2116 Data Mining & Databases — el1
2117. F2117 Distributed Systems & Cloud — alexandru caracas
2118. F2118 Curriculum-only — vector and array processor
2119. F2119 Distributed Systems & Cloud — bsp
2120. F2120 Information Theory & Coding — processor cores
2121. F2121 Mathematics — robin
2122. F2122 Algorithms & Theory of CS — polynomial time
2123. F2123 Mathematics — ans
2124. F2124 Curriculum-only — smo solver is named
2125. F2125 ML & AI — qp solver
2126. F2126 Mathematics — v0 cos
2127. F2127 Operating Systems — interrupt handler
2128. F2128 Other/Unknown — processor design
2129. F2129 Signal/Image/Audio/Video Processing — aco
2130. F2130 Software Engineering — don't
2131. F2131 Mathematics — probably
2132. F2132 Information Theory & Coding — probably won
2133. F2133 Mathematics — favorite
2134. F2134 Software Engineering — dsp processor
2135. F2135 Software Engineering — interview
2136. F2136 Distributed Systems & Cloud — library
2137. F2137 Curriculum-only — built from scratch before the library
2138. F2138 Distributed Systems & Cloud — blas
2139. F2139 Information Theory & Coding — full oneping library
2140. F2140 Software Engineering — compiling
2141. F2141 Computer Architecture — compiling expression
2142. F2142 Software Engineering — Discuss the need for allowing calls to external calls and system libraries and the consequences for language implementation
2143. F2143 Distributed Systems & Cloud — linux
2144. F2144 Curriculum-only — linux proficiency
2145. F2145 Distributed Systems & Cloud — linux shell
2146. F2146 Operating Systems — version of linux
2147. F2147 Software Engineering — hello
2148. F2148 Curriculum-only — encrypted client hello
2149. F2149 Mathematics — hello friend
2150. F2150 Algorithms & Theory of CS — text justification
2151. F2151 Curriculum-only — byte of text
2152. F2152 ML & AI — text analysis
2153. F2153 NLP & Speech — natural language
2154. F2154 ML & AI — natural language text
2155. F2155 NLP & Speech — text corpus
2156. F2156 Software Engineering — executable named hello
2157. F2157 Distributed Systems & Cloud — assistant
2158. F2158 Curriculum-only — devop assistant
2159. F2159 Mathematics — checked
2160. F2160 Curriculum-only — bounds-checked
2161. F2161 Mathematics — reveal
2162. F2162 Curriculum-only — corporate secret
2163. F2163 Information Theory & Coding — secret word
2164. F2164 Software Engineering — deliverable
2165. F2165 Cryptography & Security — edge linking
2166. F2166 Software Engineering — proof assistant
2167. F2167 Curriculum-only — ssl terminated
2168. F2168 Software Engineering — test program
2169. F2169 Curriculum-only — third-party and data-handling policy
2170. F2170 Software Engineering — thorough understanding
2171. F2171 Mathematics — assume
2172. F2172 Information Theory & Coding — assume bounded llr
2173. F2173 Mathematics — assume fn
2174. F2174 Curriculum-only — assumption that would reverse
2175. F2175 Mathematics — ambiguous
2176. F2176 Curriculum-only — spirit of newton
2177. F2177 Mathematics — state assumption
2178. F2178 NLP & Speech — relative clause
2179. F2179 Signal/Image/Audio/Video Processing — set of assumption
2180. F2180 Software Engineering — builtin assume aligned
2181. F2181 Curriculum-only — clarify constraint and assumption
2182. F2182 Software Engineering — lawyer
2183. F2183 Data Mining & Databases — hotel
2184. F2184 Mathematics — card
2185. F2185 Curriculum-only — card with blackjackcard
2186. F2186 Information Theory & Coding — line card
2187. F2187 Mathematics — card dealt
2188. F2188 Algorithms & Theory of CS — pigeonhole
2189. F2189 Curriculum-only — pigeonhole and double counting
2190. F2190 Mathematics — th card
2191. F2191 NLP & Speech — cheap hotel
2192. F2192 Software Engineering — parse
2193. F2193 NLP & Speech — able to parse
2194. F2194 Software Engineering — finite-state control
2195. F2195 Software Engineering — work environments
2196. F2196 Curriculum-only — wound-wait scheme
2197. F2197 Software Engineering — writeup
2198. F2198 Mathematics — extension
2199. F2199 Algorithms & Theory of CS — one-step extension
2200. F2200 Computer Architecture — extension cord
2201. F2201 Curriculum-only — length-extension
2202. F2202 Distributed Systems & Cloud — rdma
2203. F2203 Mathematics — abelian
2204. F2204 Curriculum-only — alternative and loop
2205. F2205 Data Mining & Databases — alternative to pca
2206. F2206 Mathematics — computation
2207. F2207 Algorithms & Theory of CS — lba
2208. F2208 Computer Architecture — despreading computation
2209. F2209 Cryptography & Security — mpc
2210. F2210 Curriculum-only — cnn computation
2211. F2211 Distributed Systems & Cloud — communication-to-computation ratio
2212. F2212 Curriculum-only — alternating projection for computing lra
2213. F2213 Data Mining & Databases — computing distance
2214. F2214 Distributed Systems & Cloud — baruch
2215. F2215 Curriculum-only — edge computing and its classification
2216. F2216 Distributed Systems & Cloud — exascale computing
2217. F2217 ML & AI — computing nodes
2218. F2218 Algorithms & Theory of CS — breadth-first search
2219. F2219 Curriculum-only — breadth-first and depth-first search
2220. F2220 ML & AI — artificial
2221. F2221 Mathematics — element of order
2222. F2222 Curriculum-only — endpoint detection
2223. F2223 Mathematics — factoring integer
2224. F2224 Curriculum-only — free port
2225. F2225 Data Mining & Databases — free version
2226. F2226 Distributed Systems & Cloud — conflict free
2227. F2227 Information Theory & Coding — pre x-free
2228. F2228 Mathematics — free group
2229. F2229 Distributed Systems & Cloud — event ordering
2230. F2230 Mathematics — ordered
2231. F2231 Curriculum-only — scaling effect
2232. F2232 Data Mining & Databases — boxplot
2233. F2233 Mathematics — box
2234. F2234 Computer Architecture — text box
2235. F2235 Curriculum-only — p-box
2236. F2236 ML & AI — gray-box
2237. F2237 Mathematics — box contain coin
2238. F2238 Curriculum-only — order-statistic tree
2239. F2239 Operating Systems — multicast
2240. F2240 Computer Networks — multicast routing
2241. F2241 Other/Unknown — alternative fuel
2242. F2242 Signal/Image/Audio/Video Processing — compression
2243. F2243 Computer Architecture — compression methods
2244. F2244 Curriculum-only — compression function
2245. F2245 Data Mining & Databases — jpeg2000 compression
2246. F2246 Information Theory & Coding — compression efficiency
2247. F2247 Algorithms & Theory of CS — color
2248. F2248 Curriculum-only — depth-first search with the three colour
2249. F2249 Information Theory & Coding — optimal compressor
2250. F2250 Signal/Image/Audio/Video Processing — audio compression
2251. F2251 Software Engineering — benchmarking
2252. F2252 Curriculum-only — stig benchmarking
2253. F2253 Software Engineering — branching and iteration
2254. F2254 Mathematics — approximation
2255. F2255 Algorithms & Theory of CS — approx vertex cover
2256. F2256 Curriculum-only — approximation of christofide
2257. F2257 ML & AI — approximation bounds
2258. F2258 Mathematics — approximate value
2259. F2259 Cryptography & Security — quadratic residuosity
2260. F2260 Curriculum-only — quadratic with negative discriminant
2261. F2261 Data Mining & Databases — quadratic integer
2262. F2262 Mathematics — linear approximation
2263. F2263 Curriculum-only — linear approximation table
2264. F2264 Mathematics — differentiable
2265. F2265 ML & AI — non-differentiable
2266. F2266 Mathematics — continuous and differentiable
2267. F2267 Curriculum-only — barzilai borwein gradient
2268. F2268 Distributed Systems & Cloud — averaged gradient
2269. F2269 ML & AI — computation graph
2270. F2270 Curriculum-only — exploding gradient in deep neural network
2271. F2271 ML & AI — gradient clipping
2272. F2272 Mathematics — dgn
2273. F2273 Other/Unknown — linear quadratic regulator
2274. F2274 Curriculum-only — linear-quadratic regulator are named
2275. F2275 Other/Unknown — unconstrained optimization
2276. F2276 Curriculum-only — constrained and unconstrained optimization
2277. F2277 Mathematics — multi
2278. F2278 Algorithms & Theory of CS — multi-attribute
2279. F2279 Cryptography & Security — multi-party computation
2280. F2280 Curriculum-only — multi-class svm
2281. F2281 Distributed Systems & Cloud — multi-core
2282. F2282 Curriculum-only — multi-level page table
2283. F2283 Mathematics — multi-dimensional
2284. F2284 Curriculum-only — multi-dimensional mapping of dataspace
2285. F2285 Data Mining & Databases — multi-dimensional data modeling
2286. F2286 Mathematics — multi-input multi-output
2287. F2287 Other/Unknown — multi armed
2288. F2288 Curriculum-only — multi-agent infinite loop
2289. F2289 Other/Unknown — multi-core processor
2290. F2290 Signal/Image/Audio/Video Processing — applying orthogonality
2291. F2291 Software Engineering — Computing industry
2292. F2292 Mathematics — induced
2293. F2293 Software Engineering — dennard scaling
2294. F2294 Algorithms & Theory of CS — conquer
2295. F2295 Mathematics — median
2296. F2296 Curriculum-only — i-th minimum and the median
2297. F2297 Mathematics — median value
2298. F2298 Signal/Image/Audio/Video Processing — median filter
2299. F2299 Software Engineering — lego color
2300. F2300 Curriculum-only — python own decorator syntax for function
2301. F2301 Data Mining & Databases — invalid syntax
2302. F2302 Other/Unknown — predicate
2303. F2303 Curriculum-only — contradictory predicate
2304. F2304 Data Mining & Databases — binary predicate
2305. F2305 Other/Unknown — individual constant
2306. F2306 Algorithms & Theory of CS — propositional satisfiability
2307. F2307 ML & AI — empirical
2308. F2308 Mathematics — assign
2309. F2309 Computer Architecture — dina
2310. F2310 Mathematics — cdf and empirical
2311. F2311 Data Mining & Databases — induction axiom
2312. F2312 Mathematics — according to proposition
2313. F2313 Algorithms & Theory of CS — centered difference formula
2314. F2314 Curriculum-only — hadamard formula
2315. F2315 Data Mining & Databases — bounded formula
2316. F2316 Distributed Systems & Cloud — duplication
2317. F2317 Information Theory & Coding — probability formula
2318. F2318 Mathematics — aj ak
2319. F2319 Curriculum-only — argument by convention
2320. F2320 Data Mining & Databases — keyword argument
2321. F2321 Distributed Systems & Cloud — add argument
2322. F2322 Curriculum-only — multiplication multiply moduli and add argument
2323. F2323 ML & AI — lucas
2324. F2324 Curriculum-only — lucas lehmer
2325. F2325 Mathematics — complex argument
2326. F2326 Curriculum-only — bius map and the exponential function
2327. F2327 Mathematics — formula for derivative
2328. F2328 Curriculum-only — unrestricted negation is not domain independent
2329. F2329 Mathematics — principle
2330. F2330 Curriculum-only — pontryagin principle
2331. F2331 Data Mining & Databases — principle of hands-on data
2332. F2332 Distributed Systems & Cloud — parallelization principle
2333. F2333 Information Theory & Coding — orthogonality principle
2334. F2334 Mathematics — duhamel principle
2335. F2335 Curriculum-only — mean absolute error
2336. F2336 Mathematics — min-max theorem
2337. F2337 Computer Architecture — sign extension
2338. F2338 Curriculum-only — immediate and their sign extension
2339. F2339 Data Mining & Databases — sign mean
2340. F2340 Mathematics — absolute value
2341. F2341 Operating Systems — sign extender
2342. F2342 Other/Unknown — atomic sentence
2343. F2343 Mathematics — substitution
2344. F2344 Algorithms & Theory of CS — operation count
2345. F2345 Mathematics — anti-derivative
2346. F2346 Curriculum-only — solving trigonometric equation
2347. F2347 Mathematics — covering ses
2348. F2348 Other/Unknown — binary connective
2349. F2349 Curriculum-only — design principle of confusion
2350. F2350 Other/Unknown — fluid
2351. F2351 Computer Networks — linear and non-linear
2352. F2352 Mathematics — differentiation
2353. F2353 Curriculum-only — differentiation and mean value theorem
2354. F2354 Mathematics — implicit differentiation
2355. F2355 Curriculum-only — leibnitz rule of differentiation
2356. F2356 Other/Unknown — formula of pl
2357. F2357 Mathematics — sound
2358. F2358 Computer Architecture — everyday sound object
2359. F2359 ML & AI — proof checker
2360. F2360 Mathematics — complex with sound
2361. F2361 NLP & Speech — acoustics
2362. F2362 Information Theory & Coding — acoustics of speech
2363. F2363 Mathematics — sept
2364. F2364 Curriculum-only — calculus and sql
2365. F2365 Data Mining & Databases — predicate calculus
2366. F2366 Mathematics — continuity
2367. F2367 Curriculum-only — continuity and fokker planck equation
2368. F2368 Mathematics — discrete systems
2369. F2369 Algorithms & Theory of CS — banded matrix
2370. F2370 Computer Networks — akj
2371. F2371 Curriculum-only — byte matrix over gf
2372. F2372 Curriculum-only — matrix for statistics
2373. F2373 Data Mining & Databases — bii
2374. F2374 Distributed Systems & Cloud — matrix computa tion
2375. F2375 Information Theory & Coding — hess
2376. F2376 ML & AI — data matrices
2377. F2377 Mathematics — aij
2378. F2378 Curriculum-only — gaussian elimination over gf
2379. F2379 ML & AI — connection to gaussian elimination
2380. F2380 Mathematics — graph and network
2381. F2381 Data Mining & Databases — matrix math
2382. F2382 ML & AI — math joke
2383. F2383 Mathematics — matrix algebra
2384. F2384 Curriculum-only — full matrix algebra
2385. F2385 Mathematics — discrete time
2386. F2386 Curriculum-only — composition and inverse
2387. F2387 Mathematics — difference matrix
2388. F2388 Curriculum-only — common modulus
2389. F2389 Mathematics — modulus and argument
2390. F2390 Algorithms & Theory of CS — multiplication and norm
2391. F2391 Curriculum-only — vector and norm
2392. F2392 Mathematics — induced norm
2393. F2393 Mathematics — positive definite
2394. F2394 Mathematics — space and subspace
2395. F2395 Curriculum-only — square approximation and minimum-norm
2396. F2396 Mathematics — formulas
2397. F2397 Algorithms & Theory of CS — cnf formulas
2398. F2398 Curriculum-only — formulas and their meaning
2399. F2399 Mathematics — addition formulas
2400. F2400 Curriculum-only — gram schmidt process
2401. F2401 Mathematics — gram-schmidt projection
2402. F2402 Curriculum-only — area ab sin
2403. F2403 Mathematics — asin
2404. F2404 Curriculum-only — system of equation using rank
2405. F2405 Mathematics — system of ordinary differential
2406. F2406 Curriculum-only — cos and tan
2407. F2407 Mathematics — arcsin
2408. F2408 NLP & Speech — auditory
2409. F2409 Information Theory & Coding — acoust
2410. F2410 NLP & Speech — auditory system
2411. F2411 Data Mining & Databases — anatomy
2412. F2412 NLP & Speech — interaural
2413. F2413 Other/Unknown — Differential calculus
2414. F2414 Curriculum-only — cost and observability
2415. F2415 Other/Unknown — Propositional calculus
2416. F2416 Curriculum-only — validity of argument
2417. F2417 Mathematics — propositional formula
2418. F2418 Other/Unknown — viscous fluids
2419. F2419 Signal/Image/Audio/Video Processing — discrete-time system
2420. F2420 Software Engineering — algorithm for matrix
2421. F2421 Algorithms & Theory of CS — function argument for coloring
2422. F2422 Mathematics — height
2423. F2423 Algorithms & Theory of CS — balanced tree
2424. F2424 Curriculum-only — black-height
2425. F2425 Mathematics — cauldron
2426. F2426 Algorithms & Theory of CS — weighted equally
2427. F2427 Mathematics — weighted least-square
2428. F2428 Software Engineering — math structure
2429. F2429 Algorithms & Theory of CS — consciousness
2430. F2430 Computer Architecture — fsm modularity
2431. F2431 Operating Systems — enforced modularity
2432. F2432 Signal/Image/Audio/Video Processing — equation and modularity
2433. F2433 Software Engineering — abstraction and modularity
2434. F2434 Mathematics — row
2435. F2435 Computer Architecture — row store
2436. F2436 Curriculum-only — minimum over row for count-min
2437. F2437 Distributed Systems & Cloud — row keys
2438. F2438 Information Theory & Coding — hadamard matrix
2439. F2439 Mathematics — elementary row
2440. F2440 Curriculum-only — complex number are taken to depth
2441. F2441 Mathematics — ac bd
2442. F2442 Algorithms & Theory of CS — manzini
2443. F2443 Curriculum-only — norm and space
2444. F2444 Data Mining & Databases — curse
2445. F2445 Distributed Systems & Cloud — analyzing space bound
2446. F2446 Information Theory & Coding — space of code
2447. F2447 ML & AI — isometric
2448. F2448 Mathematics — ai aj
2449. F2449 Algorithms & Theory of CS — higher dimension
2450. F2450 Curriculum-only — dimension equality
2451. F2451 Information Theory & Coding — complex dimension
2452. F2452 Mathematics — dimension formula
2453. F2453 Algorithms & Theory of CS — mathematical logic
2454. F2454 Computer Networks — form group
2455. F2455 Curriculum-only — multilinear form
2456. F2456 Distributed Systems & Cloud — form factors
2457. F2457 Mathematics — approximating sum
2458. F2458 Mathematics — pell
2459. F2459 Data Mining & Databases — ypll
2460. F2460 Mathematics — measure
2461. F2461 Computer Networks — graph measure
2462. F2462 Curriculum-only — halstead measure
2463. F2463 ML & AI — empirical measure
2464. F2464 Mathematics — borel
2465. F2465 Algorithms & Theory of CS — cantelli
2466. F2466 Mathematics — dp1
2467. F2467 Curriculum-only — measure-theoretic probability is not needed
2468. F2468 Mathematics — posteriori
2469. F2469 Algorithms & Theory of CS — number of map
2470. F2470 Distributed Systems & Cloud — map task
2471. F2471 Information Theory & Coding — rsum
2472. F2472 Distributed Systems & Cloud — rsum node
2473. F2473 ML & AI — map con guration
2474. F2474 Mathematics — continuous extension
2475. F2475 Curriculum-only — differential inclusion
2476. F2476 Mathematics — linear map
2477. F2477 Curriculum-only — second-preimage
2478. F2478 Mathematics — pushforward
2479. F2479 Algorithms & Theory of CS — ial
2480. F2480 Curriculum-only — computational rule for determinant
2481. F2481 Mathematics — cramer rule
2482. F2482 Computer Networks — defected
2483. F2483 Data Mining & Databases — previous work
2484. F2484 Mathematics — site
2485. F2485 Computer Networks — distributor
2486. F2486 Curriculum-only — checked against the owasp project site
2487. F2487 Mathematics — party site
2488. F2488 Curriculum-only — cart view
2489. F2489 Data Mining & Databases — materialized view
2490. F2490 Distributed Systems & Cloud — previous view
2491. F2491 Information Theory & Coding — system view
2492. F2492 Mathematics — matrix view
2493. F2493 Computer Architecture — rf stage
2494. F2494 Curriculum-only — build stage
2495. F2495 Data Mining & Databases — el2
2496. F2496 Information Theory & Coding — initial stage
2497. F2497 Mathematics — ex1
2498. F2498 NLP & Speech — additional measure
2499. F2499 Data Mining & Databases — additional measure cleaned
2500. F2500 NLP & Speech — erb
2501. F2501 Distributed Systems & Cloud — file
2502. F2502 HS ComputerScience Class XII / Unit 1: Computational Thinking and Programming – 2 — text file
2503. F2503 Computer Architecture — additional file
2504. F2504 Computer Networks — gz file
2505. F2505 Cryptography & Security — passwd
2506. F2506 Curriculum-only — append-only file
2507. F2507 Data Mining & Databases — file organisation
2508. F2508 Curriculum-only — file organisation and hashing
2509. F2509 Data Mining & Databases — meval
2510. F2510 Curriculum-only — misc group
2511. F2511 Data Mining & Databases — patching file
2512. F2512 Distributed Systems & Cloud — file attribute
2513. F2513 Information Theory & Coding — compressed file
2514. F2514 Mathematics — based
2515. F2515 Computer Networks — choice based
2516. F2516 Cryptography & Security — based on recent
2517. F2517 Curriculum-only — attribute-based
2518. F2518 Curriculum-only — tcam-based classification
2519. F2519 Data Mining & Databases — density based
2520. F2520 Distributed Systems & Cloud — credit-based
2521. F2521 Information Theory & Coding — code-based
2522. F2522 ML & AI — cnn-based
2523. F2523 Mathematics — based on observation
2524. F2524 Computer Architecture — file created
2525. F2525 Curriculum-only — create tablespace
2526. F2526 Data Mining & Databases — image to create data
2527. F2527 Mathematics — gpu-based
2528. F2528 NLP & Speech — error decision rule
2529. F2529 Operating Systems — db file
2530. F2530 Other/Unknown — atomic formula
2531. F2531 Mathematics — integral
2532. F2532 Curriculum-only — expectation as an integral
2533. F2533 Information Theory & Coding — gaussian integral
2534. F2534 Mathematics — boundary integrals
2535. F2535 Curriculum-only — change of variable for density
2536. F2536 Mathematics — equivalent definition
2537. F2537 Curriculum-only — differentiation under the integral sign
2538. F2538 Mathematics — integration
2539. F2539 Computer Networks — system integration
2540. F2540 Curriculum-only — change of order of integration
2541. F2541 Mathematics — cxh
2542. F2542 Curriculum-only — rational function and asymptote
2543. F2543 Mathematics — asymptotic
2544. F2544 Algorithms & Theory of CS — rrg
2545. F2545 Curriculum-only — definition of asymptotic notation are proved
2546. F2546 Mathematics — asymptotic expressions
2547. F2547 Curriculum-only — real integral and conformal mapping
2548. F2548 Mathematics — riemann integrability
2549. F2549 Curriculum-only — area and volume integral
2550. F2550 NLP & Speech — complex integration
2551. F2551 Other/Unknown — choquet integral
2552. F2552 Curriculum-only — continuous dynamical system
2553. F2553 Other/Unknown — site investigation
2554. F2554 Signal/Image/Audio/Video Processing — anticausal
2555. F2555 Mathematics — anticausal system
2556. F2556 Signal/Image/Audio/Video Processing — based on successive
2557. F2557 Signal/Image/Audio/Video Processing — unique continuous extension
2558. F2558 Software Engineering — boolean
2559. F2559 Algorithms & Theory of CS — boolean function
2560. F2560 Curriculum-only — boolean mask
2561. F2561 Data Mining & Databases — boolean classification
2562. F2562 Mathematics — cn0
2563. F2563 Cryptography & Security — cnk ep
2564. F2564 Mathematics — match
2565. F2565 Algorithms & Theory of CS — set of tile
2566. F2566 Curriculum-only — openflow match action table
2567. F2567 Distributed Systems & Cloud — match length
2568. F2568 Information Theory & Coding — longest-prefix match
2569. F2569 Mathematics — optimal match
2570. F2570 Other/Unknown — Boolean algebras
2571. F2571 Software Engineering — boolean value
2572. F2572 Mathematics — source
2573. F2573 Algorithms & Theory of CS — rover
2574. F2574 Computer Architecture — ambient noise
2575. F2575 Curriculum-only — definition as the source of proof
2576. F2576 Curriculum-only — source write
2577. F2577 Information Theory & Coding — optimal source
2578. F2578 ML & AI — image source
2579. F2579 Data Mining & Databases — yval
2580. F2580 Mathematics — atmospheric pressure
2581. F2581 Computer Networks — branch office
2582. F2582 Curriculum-only — branch mispredict ns
2583. F2583 Information Theory & Coding — branch complexity
2584. F2584 Mathematics — mar
2585. F2585 Data Mining & Databases — mar-07
2586. F2586 Mathematics — sink nodes
2587. F2587 Curriculum-only — forecasting using statistical
2588. F2588 Data Mining & Databases — statistical distance
2589. F2589 Curriculum-only — statistical distance and distinguishing advantage
2590. F2590 Data Mining & Databases — statistical sommelier
2591. F2591 Information Theory & Coding — statistical difference
2592. F2592 ML & AI — ising model
2593. F2593 Curriculum-only — rule-based guessing
2594. F2594 Mathematics — error decision rule based
2595. F2595 Algorithms & Theory of CS — triple element
2596. F2596 Curriculum-only — bgw approach with beaver triple for multiplication
2597. F2597 Mathematics — ubiquitous
2598. F2598 Computer Architecture — physics ii
2599. F2599 Mathematics — motion
2600. F2600 Algorithms & Theory of CS — based motion
2601. F2601 ML & AI — motion detection
2602. F2602 Mathematics — Euler%27s laws of motion
2603. F2603 Computer Architecture — vertical velocity
2604. F2604 Distributed Systems & Cloud — coordinate and velocity
2605. F2605 Mathematics — current velocity
2606. F2606 Algorithms & Theory of CS — kruskal
2607. F2607 Curriculum-only — input weight activation output
2608. F2608 Data Mining & Databases — relative weights
2609. F2609 ML & AI — kruskal rank
2610. F2610 Mathematics — bias
2611. F2611 Curriculum-only — bias of the mle
2612. F2612 Data Mining & Databases — handling bias
2613. F2613 Mathematics — biased
2614. F2614 NLP & Speech — acoustic compliance
2615. F2615 Operating Systems — branch target buffer
2616. F2616 Other/Unknown — circuit
2617. F2617 Algorithms & Theory of CS — power source
2618. F2618 Computer Architecture — circuit breaker
2619. F2619 Computer Networks — jitter
2620. F2620 Curriculum-only — circuit breaker and graceful shutdown
2621. F2621 Data Mining & Databases — circuit court
2622. F2622 ML & AI — Circuit complexity
2623. F2623 Mathematics — voltage
2624. F2624 Computer Architecture — nought
2625. F2625 Mathematics — squared
2626. F2626 Data Mining & Databases — r-squared value
2627. F2627 Mathematics — length squared
2628. F2628 Other/Unknown — arithmetic circuit
2629. F2629 Curriculum-only — billion delivery
2630. F2630 Information Theory & Coding — continuous delivery
2631. F2631 Curriculum-only — agile method and continuous delivery
2632. F2632 Information Theory & Coding — reliable delivery
2633. F2633 Operating Systems — content delivery
2634. F2634 Curriculum-only — content delivery and anycast
2635. F2635 Other/Unknown — device physics
2636. F2636 Data Mining & Databases — harvest
2637. F2637 Mathematics — analytical
2638. F2638 Curriculum-only — analytical method and grid approximation
2639. F2639 Data Mining & Databases — analytical policeman
2640. F2640 Mathematics — extinction
2641. F2641 ML & AI — rating
2642. F2642 Data Mining & Databases — collaborative
2643. F2643 Mathematics — extinction probability
2644. F2644 Algorithms & Theory of CS — body surface
2645. F2645 Data Mining & Databases — volume element
2646. F2646 Mathematics — area element
2647. F2647 Curriculum-only — element that appear
2648. F2648 NLP & Speech — snow
2649. F2649 Operating Systems — type of material appear
2650. F2650 Other/Unknown — drug delivery
2651. F2651 Mathematics — electrical
2652. F2652 Data Mining & Databases — science and electrical
2653. F2653 Mathematics — analogy
2654. F2654 Other/Unknown — electrical energy
2655. F2655 Curriculum-only — integrated circuit to microprocessor
2656. F2656 Distributed Systems & Cloud — Hardware accelerators
2657. F2657 Other/Unknown — inverter
2658. F2658 Operating Systems — worksheet
2659. F2659 Computer Architecture — instruction set architecture
2660. F2660 Computer Networks — data manipulation
2661. F2661 Curriculum-only — data manipulation and query language
2662. F2662 Distributed Systems & Cloud — maximum inner product
2663. F2663 Operating Systems — mip isa
2664. F2664 Computer Networks — End-of-life issues with sunsetting operating systems. Example concept: Privacy implications of using proprietary operating systems/operating environments, including telemetry, automated scanning of personal data, built-in advertising, and automatic cloud integration
2665. F2665 Operating Systems — pc hardware
2666. F2666 Other/Unknown — light source
2667. F2667 Algorithms & Theory of CS — additional information
2668. F2668 Other/Unknown — molecular
2669. F2669 ML & AI — glass
2670. F2670 Mathematics — composite
2671. F2671 Computer Networks — composite keys
2672. F2672 Curriculum-only — decisional composite residuosity assumption
2673. F2673 Mathematics — composite function
2674. F2674 Other/Unknown — composite structures
2675. F2675 Mathematics — potential
2676. F2676 Other/Unknown — action potential
2677. F2677 ML & AI — neural
2678. F2678 Other/Unknown — free energy
2679. F2679 Mathematics — correspondence
2680. F2680 Curriculum-only — correspondence to sql
2681. F2681 Other/Unknown — operational amplifier
2682. F2682 Mathematics — mirror
2683. F2683 Cryptography & Security — elliptic and hyper-elliptic
2684. F2684 Mathematics — elliptic operator
2685. F2685 Other/Unknown — current mirror
2686. F2686 Curriculum-only — analysis-and-design process
2687. F2687 Mathematics — perspective
2688. F2688 Curriculum-only — administrative perspective
2689. F2689 Other/Unknown — historical
2690. F2690 Curriculum-only — historical content
2691. F2691 Other/Unknown — projective
2692. F2692 Cryptography & Security — tamper resistance
2693. F2693 Other/Unknown — Superconducting circuits
2694. F2694 Signal/Image/Audio/Video Processing — amount of drug
2695. F2695 Other/Unknown — curve and surface
2696. F2696 Signal/Image/Audio/Video Processing — resting potential
2697. F2697 Information Theory & Coding — posteriori probability
2698. F2698 Signal/Image/Audio/Video Processing — time constant
2699. F2699 Mathematics — tank
2700. F2700 Curriculum-only — inverted and hashed page table
2701. F2701 Signal/Image/Audio/Video Processing — leaky tank
2702. F2702 Mathematics — second-order
2703. F2703 Computer Architecture — second-order filter
2704. F2704 Curriculum-only — second-order and natural-gradient
2705. F2705 Mathematics — initial value problem
2706. F2706 Other/Unknown — second-order necessary
2707. F2707 Software Engineering — assembly
2708. F2708 Curriculum-only — cgo and assembly
2709. F2709 Software Engineering — branch prediction
2710. F2710 Computer Networks — set default
2711. F2711 Curriculum-only — default client
2712. F2712 Software Engineering — default argument
2713. F2713 Curriculum-only — file input and output
2714. F2714 Software Engineering — file structure
2715. F2715 Distributed Systems & Cloud — folder structure
2716. F2716 Software Engineering — format
2717. F2717 Computer Networks — response format
2718. F2718 Curriculum-only — instruction encoding and format
2719. F2719 Distributed Systems & Cloud — Data formats: Marshaling, validation, encryption, compression
2720. F2720 Software Engineering — elf
2721. F2721 Operating Systems — elf format
2722. F2722 Software Engineering — argc
2723. F2723 Curriculum-only — lakehouse idiom
2724. F2724 Mathematics — refinement
2725. F2725 Signal/Image/Audio/Video Processing — refinement equation
2726. F2726 Software Engineering — inferred
2727. F2727 Curriculum-only — verified in the interpreter
2728. F2728 Data Mining & Databases — interpreter code
2729. F2729 Mathematics — blackboard
2730. F2730 Curriculum-only — table headed other hold blackboard
2731. F2731 Software Engineering — js file
2732. F2732 Mathematics — logarithm
2733. F2733 Curriculum-only — law of logarithm
2734. F2734 Information Theory & Coding — Binary logarithm
2735. F2735 Mathematics — complex logarithm
2736. F2736 Information Theory & Coding — log2
2737. F2737 Data Mining & Databases — d2 log2 ne
2738. F2738 Mathematics — decimal digit
2739. F2739 Algorithms & Theory of CS — criterion for tileability
2740. F2740 Curriculum-only — comparative study by criterion
2741. F2741 Information Theory & Coding — nyquist criterion
2742. F2742 Mathematics — cauchy criterion
2743. F2743 Curriculum-only — stated outcome
2744. F2744 ML & AI — test outcome
2745. F2745 Mathematics — probability of outcome
2746. F2746 Curriculum-only — shift and mask
2747. F2747 Information Theory & Coding — doppler shift
2748. F2748 Mathematics — starting
2749. F2749 Other/Unknown — failure criterion
2750. F2750 Signal/Image/Audio/Video Processing — circular shift
2751. F2751 Software Engineering — mar program
2752. F2752 Mathematics — member
2753. F2753 Algorithms & Theory of CS — set cover
2754. F2754 Curriculum-only — sql subset
2755. F2755 Data Mining & Databases — borel measurable
2756. F2756 ML & AI — mammal
2757. F2757 Mathematics — bijection rule
2758. F2758 Data Mining & Databases — finite set of natural
2759. F2759 Mathematics — infinite set
2760. F2760 Other/Unknown — ith member
2761. F2761 Software Engineering — member data
2762. F2762 Curriculum-only — ssh daemon option
2763. F2763 Software Engineering — stepwise
2764. F2764 Distributed Systems & Cloud — structure and algorithm
2765. F2765 Curriculum-only — data structure and algorithm
2766. F2766 Mathematics — skip
2767. F2767 Computer Networks — skip data
2768. F2768 Curriculum-only — bloom filter to skip
2769. F2769 Data Mining & Databases — web-based
2770. F2770 Mathematics — including
2771. F2771 Curriculum-only — including ocr
2772. F2772 Distributed Systems & Cloud — including multi-core
2773. F2773 Mathematics — responsible
2774. F2774 Curriculum-only — responsible ai
2775. F2775 Data Mining & Databases — responsible ir
2776. F2776 Mathematics — skip proof
2777. F2777 Operating Systems — operating system
2778. F2778 Cryptography & Security — include operating system
2779. F2779 Distributed Systems & Cloud — cloud computing
2780. F2780 Curriculum-only — type of cloud computing
2781. F2781 Distributed Systems & Cloud — data-intensive computing
2782. F2782 Curriculum-only — remainder of week beyond the file-system
2783. F2783 Distributed Systems & Cloud — event-driven programming
2784. F2784 Cryptography & Security — remote code execution
2785. F2785 Curriculum-only — remote work
2786. F2786 Distributed Systems & Cloud — utility computing
2787. F2787 Mathematics — cont
2788. F2788 Algorithms & Theory of CS — color theorem
2789. F2789 Computer Networks — event-driven
2790. F2790 Curriculum-only — event-driven function
2791. F2791 Distributed Systems & Cloud — interactive
2792. F2792 Cryptography & Security — non-interactive
2793. F2793 Mathematics — hundred
2794. F2794 Curriculum-only — hundred tweet per cached timeline
2795. F2795 Distributed Systems & Cloud — kepner
2796. F2796 Mathematics — jeremy
2797. F2797 Distributed Systems & Cloud — jeremy kepner
2798. F2798 Mathematics — able to compute
2799. F2799 Computer Networks — additional resource
2800. F2800 Curriculum-only — awkward when resource
2801. F2801 Distributed Systems & Cloud — compute resource
2802. F2802 Mathematics — computational resource
2803. F2803 Distributed Systems & Cloud — thank to mythilli vutukuru
2804. F2804 Mathematics — turned
2805. F2805 Data Mining & Databases — d2hawkeye story
2806. F2806 NLP & Speech — wm resource
2807. F2807 Operating Systems — boot loader
2808. F2808 Mathematics — path
2809. F2809 Algorithms & Theory of CS — branching program
2810. F2810 Curriculum-only — byte path
2811. F2811 Data Mining & Databases — negative cost
2812. F2812 Distributed Systems & Cloud — failure and recovery
2813. F2813 Mathematics — ai to bj
2814. F2814 Algorithms & Theory of CS — acyclic
2815. F2815 Curriculum-only — cycle and acyclic graph
2816. F2816 Information Theory & Coding — directed information
2817. F2817 Mathematics — connected and acyclic
2818. F2818 NLP & Speech — mean free path
2819. F2819 Operating Systems — log-structured file system
2820. F2820 Mathematics — local
2821. F2821 Algorithms & Theory of CS — lov sz local
2822. F2822 Computer Networks — ldf
2823. F2823 Distributed Systems & Cloud — local store
2824. F2824 Algorithms & Theory of CS — memory store
2825. F2825 Computer Architecture — memory density
2826. F2826 Curriculum-only — agentic memory
2827. F2827 Data Mining & Databases — organized
2828. F2828 Distributed Systems & Cloud — access
2829. F2829 Algorithms & Theory of CS — direct access array
2830. F2830 Computer Architecture — access time
2831. F2831 Computer Networks — Broadband access
2832. F2832 Curriculum-only — access its element
2833. F2833 Data Mining & Databases — Access paths
2834. F2834 Distributed Systems & Cloud — chunk
2835. F2835 Computer Architecture — data chunk
2836. F2836 Data Mining & Databases — mb chunk
2837. F2837 Distributed Systems & Cloud — chunk size
2838. F2838 Curriculum-only — load-store queue
2839. F2839 Distributed Systems & Cloud — memory and gpu
2840. F2840 Curriculum-only — owner of che approximation
2841. F2841 Data Mining & Databases — non-owner
2842. F2842 Distributed Systems & Cloud — current owner
2843. F2843 Information Theory & Coding — memory-less source
2844. F2844 ML & AI — local minimizer
2845. F2845 Mathematics — archimedean
2846. F2846 Algorithms & Theory of CS — monochromatic
2847. F2847 Mathematics — continuous function
2848. F2848 Curriculum-only — vertical scaling get expensive
2849. F2849 Mathematics — local mapping
2850. F2850 Computer Networks — rfi
2851. F2851 Curriculum-only — minima by setting the derivative
2852. F2852 Distributed Systems & Cloud — inflection
2853. F2853 Mathematics — parameter
2854. F2854 Algorithms & Theory of CS — fixed-parameter algorithm
2855. F2855 Curriculum-only — fixed-parameter algorithm are named
2856. F2856 Data Mining & Databases — cp parameter
2857. F2857 Information Theory & Coding — acoustic parameter
2858. F2858 ML & AI — pai
2859. F2859 Mathematics — likelihood
2860. F2860 Curriculum-only — likelihood bound
2861. F2861 ML & AI — data likelihood
2862. F2862 Mathematics — continuous likelihood
2863. F2863 NLP & Speech — parameter specification
2864. F2864 Operating Systems — address space
2865. F2865 Cryptography & Security — attack
2866. F2866 Algorithms & Theory of CS — based on linear
2867. F2867 Cryptography & Security — attack scenario
2868. F2868 Curriculum-only — attack and defence
2869. F2869 Curriculum-only — size and attack-surface consequence
2870. F2870 Operating Systems — adversarial attack
2871. F2871 Distributed Systems & Cloud — crash
2872. F2872 Data Mining & Databases — system crash
2873. F2873 Operating Systems — memory and disk
2874. F2874 Other/Unknown — access to secondary storage
2875. F2875 Curriculum-only — cost of durability
2876. F2876 Other/Unknown — elastic resource
2877. F2877 ML & AI — philosophy of ai
2878. F2878 Other/Unknown — process parameter
2879. F2879 Curriculum-only — computational resource and robustness
2880. F2880 Other/Unknown — transparency
2881. F2881 Distributed Systems & Cloud — wide-area storage
2882. F2882 Mathematics — day
2883. F2883 Curriculum-only — same-day teardown
2884. F2884 Mathematics — distribution
2885. F2885 Algorithms & Theory of CS — condition distribution
2886. F2886 Computer Networks — distribution of mean
2887. F2887 Curriculum-only — difference distribution table
2888. F2888 Distributed Systems & Cloud — distribution and scheduling
2889. F2889 ML & AI — out-of-distribution
2890. F2890 Mathematics — coin with probability
2891. F2891 Curriculum-only — probabilistic solution from joint
2892. F2892 Mathematics — continuous distribution
2893. F2893 ML & AI — clown fish
2894. F2894 Mathematics — golf
2895. F2895 Computer Architecture — leap motion
2896. F2896 Mathematics — markovian
2897. F2897 Curriculum-only — probability distribution over word
2898. F2898 Mathematics — flashlight
2899. F2899 Operating Systems — local area network
2900. F2900 Distributed Systems & Cloud — lan
2901. F2901 Operating Systems — self-configuring local area network
2902. F2902 Other/Unknown — geographical distribution
2903. F2903 Mathematics — central
2904. F2904 Curriculum-only — ppf and rvs
2905. F2905 Information Theory & Coding — function of rvs
2906. F2906 Mathematics — strongly nondegenerate self-concordant
2907. F2907 Curriculum-only — inverse function arcsin
2908. F2908 Mathematics — inverse function theorem
2909. F2909 Curriculum-only — test for two variance
2910. F2910 Mathematics — equality of variance
2911. F2911 NLP & Speech — aspirated
2912. F2912 Other/Unknown — plc
2913. F2913 Signal/Image/Audio/Video Processing — counting parameter in svd
2914. F2914 Software Engineering — access key
2915. F2915 Curriculum-only — environment variable and secret hygiene
2916. F2916 Software Engineering — group work
2917. F2917 Curriculum-only — projection push-down
2918. F2918 Distributed Systems & Cloud — node push
2919. F2919 ML & AI — top of stack
2920. F2920 Mathematics — added
2921. F2921 Cryptography & Security — expansion function
2922. F2922 Curriculum-only — multibit try with controlled prefix expansion
2923. F2923 Information Theory & Coding — orthonormal expansion
2924. F2924 Mathematics — loeve expansion
2925. F2925 Other/Unknown — half-range expansion
2926. F2926 Software Engineering — function push
2927. F2927 Cryptography & Security — git action
2928. F2928 Software Engineering — remote file
2929. F2929 Distributed Systems & Cloud — remote file system
2930. F2930 Software Engineering — resource and cost
2931. F2931 Curriculum-only — stack and stack frame
2932. F2932 Distributed Systems & Cloud — call stack
2933. F2933 Mathematics — continuation
2934. F2934 Software Engineering — call-with-current-continuation
2935. F2935 Algorithms & Theory of CS — extra space
2936. F2936 Curriculum-only — override are stored
2937. F2937 Distributed Systems & Cloud — read and write
2938. F2938 Curriculum-only — monotonic read and write
2939. F2939 Mathematics — bus
2940. F2940 Computer Architecture — output buffer
2941. F2941 Curriculum-only — bus read-exclusive
2942. F2942 Data Mining & Databases — chien
2943. F2943 Distributed Systems & Cloud — chat
2944. F2944 Algorithms & Theory of CS — tv chat
2945. F2945 Curriculum-only — chat app like whatsapp
2946. F2946 Information Theory & Coding — bus arbitration
2947. F2947 Mathematics — maxima
2948. F2948 Operating Systems — bus operator
2949. F2949 Software Engineering — streamline
2950. F2950 Operating Systems — physical memory address
2951. F2951 Software Engineering — addressing
2952. F2952 Curriculum-only — classful addressing
2953. F2953 Operating Systems — byte addressing
2954. F2954 Other/Unknown — ip addressing
2955. F2955 Software Engineering — url
2956. F2956 Curriculum-only — changed url
2957. F2957 Software Engineering — view tree
2958. F2958 Curriculum-only — white-box attack
2959. F2959 Software Engineering — whitelist
2960. F2960 Mathematics — measured
2961. F2961 Curriculum-only — measured and contracted
2962. F2962 Mathematics — plot
2963. F2963 Data Mining & Databases — bar graph
2964. F2964 Mathematics — plotting
2965. F2965 Signal/Image/Audio/Video Processing — hw4
2966. F2966 Software Engineering — plt
2967. F2967 Distributed Systems & Cloud — file server
2968. F2968 Operating Systems — qemu
2969. F2969 Software Engineering — yuxiong
2970. F2970 System Design Primer / Application layer — Application layer
2971. F2971 System Design Primer / Asynchronism — asynchronism
2972. F2972 Curriculum-only — asynchronism and microservice
2973. F2973 System Design Primer / Asynchronism — Task queues
2974. F2974 System Design Primer / Availability patterns — Availability patterns
2975. F2975 System Design Primer / Availability vs consistency — Availability vs consistency
2976. F2976 System Design Primer / Consistency patterns — Consistency patterns
2977. F2977 System Design Primer / Database — database
2978. F2978 Computer Networks — mdf file
2979. F2979 Curriculum-only — database as the backbone
2980. F2980 Data Mining & Databases — bachelor-level database
2981. F2981 Curriculum-only — relational-algebra tree
2982. F2982 Data Mining & Databases — schema
2983. F2983 Computer Networks — database schema
2984. F2984 Curriculum-only — tighten the schema
2985. F2985 Data Mining & Databases — axiom schema
2986. F2986 Computer Networks — utf-8
2987. F2987 Distributed Systems & Cloud — database transaction
2988. F2988 Data Mining & Databases — database management system
2989. F2989 Curriculum-only — data dictionary
2990. F2990 Distributed Systems & Cloud — programming
2991. F2991 Algorithms & Theory of CS — constraint programming
2992. F2992 Computer Networks — vpp
2993. F2993 Cryptography & Security — expertise in programming
2994. F2994 Curriculum-only — n-version programming
2995. F2995 Data Mining & Databases — python programming
2996. F2996 Distributed Systems & Cloud — apgas programming
2997. F2997 Curriculum-only — kem dem paradigm
2998. F2998 Distributed Systems & Cloud — data paradigm
2999. F2999 Curriculum-only — programming and data structure are assumed
3000. F3000 Distributed Systems & Cloud — programming and scala
3001. F3001 Mathematics — constant factor
3002. F3002 ML & AI — constant-factor approximation
3003. F3003 Mathematics — formulation
3004. F3004 Curriculum-only — source of randomness for sketch
3005. F3005 Mathematics — statistical formulation
3006. F3006 Algorithms & Theory of CS — bellman-ford
3007. F3007 Curriculum-only — run bellman ford for potential
3008. F3008 Mathematics — topological consideration
3009. F3009 NLP & Speech — probabilistic formulation
3010. F3010 Operating Systems — computation structure
3011. F3011 Mathematics — description
3012. F3012 Algorithms & Theory of CS — detailed description
3013. F3013 Computer Networks — description language
3014. F3014 Curriculum-only — use-case description
3015. F3015 Distributed Systems & Cloud — description of metis
3016. F3016 Computer Architecture — digital system
3017. F3017 Curriculum-only — permission-based
3018. F3018 Distributed Systems & Cloud — laboratory
3019. F3019 Curriculum-only — laboratory set-up
3020. F3020 Data Mining & Databases — programming laboratory
3021. F3021 Distributed Systems & Cloud — data laboratory
3022. F3022 Information Theory & Coding — error-correcting code laboratory
3023. F3023 Mathematics — hour
3024. F3024 Cryptography & Security — consist of hour
3025. F3025 Curriculum-only — failure per device-hour
3026. F3026 Mathematics — days
3027. F3027 Data Mining & Databases — aim to equip
3028. F3028 Mathematics — familiarity with proof
3029. F3029 Curriculum-only — suite such as spec
3030. F3030 Distributed Systems & Cloud — lower level
3031. F3031 Mathematics — three-hour comprehensive
3032. F3032 Operating Systems — disk spec
3033. F3033 Other/Unknown — agriculture
3034. F3034 Cryptography & Security — sector
3035. F3035 Curriculum-only — sector area
3036. F3036 Distributed Systems & Cloud — centralized
3037. F3037 Curriculum-only — centralised daisy chain
3038. F3038 Mathematics — Circular sector
3039. F3039 Operating Systems — bwrite sector
3040. F3040 Other/Unknown — col703
3041. F3041 Mathematics — transformation
3042. F3042 Algorithms & Theory of CS — Transformation (function)
3043. F3043 Curriculum-only — discrete transformation
3044. F3044 Distributed Systems & Cloud — code transformation
3045. F3045 ML & AI — graph transformation
3046. F3046 Mathematics — change of basis
3047. F3047 Other/Unknown — definite description
3048. F3048 Computer Networks — actor
3049. F3049 Cryptography & Security — state actor
3050. F3050 Curriculum-only — actor runtime built on dsim
3051. F3051 Data Mining & Databases — world health organization
3052. F3052 Information Theory & Coding — health science
3053. F3053 Mathematics — epidemiology
3054. F3054 Algorithms & Theory of CS — tape cell
3055. F3055 Computer Architecture — storage device
3056. F3056 Cryptography & Security — mechanism
3057. F3057 Curriculum-only — secondary storage device
3058. F3058 Distributed Systems & Cloud — cell programming hands-on
3059. F3059 Curriculum-only — commit dag
3060. F3060 Distributed Systems & Cloud — atomic commit
3061. F3061 Information Theory & Coding — cell processor
3062. F3062 ML & AI — cell state
3063. F3063 Mathematics — market
3064. F3064 Computer Networks — counterparty
3065. F3065 Cryptography & Security — equity market
3066. F3066 Curriculum-only — depend on market data
3067. F3067 Data Mining & Databases — capitalization
3068. F3068 Distributed Systems & Cloud — leverage
3069. F3069 Mathematics — exchange
3070. F3070 Cryptography & Security — bill of exchange
3071. F3071 Curriculum-only — exchange argument
3072. F3072 Distributed Systems & Cloud — binary exchange
3073. F3073 Mathematics — market prediction
3074. F3074 Curriculum-only — market prediction and forecasting
3075. F3075 Mathematics — membrane
3076. F3076 Curriculum-only — maximum and perfect
3077. F3077 Mathematics — price
3078. F3078 Computer Networks — optimal price
3079. F3079 Data Mining & Databases — difference in price
3080. F3080 Mathematics — pull
3081. F3081 Algorithms & Theory of CS — push and pull
3082. F3082 Curriculum-only — push-pull rumour spreading
3083. F3083 Mathematics — recover
3084. F3084 Data Mining & Databases — time to recover
3085. F3085 Mathematics — reviewed
3086. F3086 Curriculum-only — lp characterisation
3087. F3087 Mathematics — row exchange
3088. F3088 Curriculum-only — solid principle
3089. F3089 Mathematics — gravitational attraction
3090. F3090 Curriculum-only — ore sufficient condition stated
3091. F3091 Mathematics — tutorial
3092. F3092 Algorithms & Theory of CS — tutorial to help
3093. F3093 Curriculum-only — tutorial with scikit-learn
3094. F3094 Distributed Systems & Cloud — tutorial and programming
3095. F3095 Operating Systems — commit stage
3096. F3096 Other/Unknown — air pollution
3097. F3097 Mathematics — weather
3098. F3098 Data Mining & Databases — happiness
3099. F3099 ML & AI — intelligence
3100. F3100 Algorithms & Theory of CS — design of algorithm
3101. F3101 Curriculum-only — intelligence level
3102. F3102 Mathematics — intelligence analysts
3103. F3103 NLP & Speech — dew
3104. F3104 Other/Unknown — cell biology
3105. F3105 Mathematics — equation of fluid mechanics
3106. F3106 Other/Unknown — fuel cell
3107. F3107 Curriculum-only — chief information security officer
3108. F3108 Mathematics — risk
3109. F3109 Cryptography & Security — breach
3110. F3110 Curriculum-only — breach duty
3111. F3111 Curriculum-only — third-party and supply-chain risk
3112. F3112 Data Mining & Databases — risk factor
3113. F3113 Mathematics — european call option
3114. F3114 Other/Unknown — assessment
3115. F3115 Curriculum-only — assessment by probability
3116. F3116 Operating Systems — self-assessment test
3117. F3117 Other/Unknown — impact assessment
3118. F3118 ML & AI — Data preparation (e.g., standardization, representation, one-hot encoding)
3119. F3119 Other/Unknown — reactive
3120. F3120 Data Mining & Databases — compound statement
3121. F3121 Distributed Systems & Cloud — register
3122. F3122 Computer Architecture — adr
3123. F3123 Curriculum-only — datapath element
3124. F3124 Data Mining & Databases — number in register
3125. F3125 Distributed Systems & Cloud — atomic register
3126. F3126 Computer Architecture — data read
3127. F3127 Curriculum-only — fetch of several instruction per cycle
3128. F3128 Distributed Systems & Cloud — mmio
3129. F3129 Mathematics — flow
3130. F3130 Algorithms & Theory of CS — flow of value
3131. F3131 Curriculum-only — cut and the max-flow min-cut theorem
3132. F3132 Data Mining & Databases — stratified
3133. F3133 Distributed Systems & Cloud — flow paradigm
3134. F3134 Information Theory & Coding — flow-based
3135. F3135 ML & AI — gradient flow
3136. F3136 Mathematics — amount of flow
3137. F3137 Operating Systems — cause register
3138. F3138 Other/Unknown — cash flow
3139. F3139 Mathematics — reduction
3140. F3140 Algorithms & Theory of CS — mapping reduction
3141. F3141 Curriculum-only — dadda tree reduction
3142. F3142 Mathematics — distance function
3143. F3143 Other/Unknown — resource assessment
3144. F3144 Signal/Image/Audio/Video Processing — axial
3145. F3145 Other/Unknown — axial flow
3146. F3146 Computer Architecture — mechanical vibrations
3147. F3147 Other/Unknown — non-linear vibrations
3148. F3148 Signal/Image/Audio/Video Processing — discrete linear
3149. F3149 Computer Architecture — wea
3150. F3150 Signal/Image/Audio/Video Processing — lighting conditions
3151. F3151 Software Engineering — abstract machine
3152. F3152 Mathematics — describe
3153. F3153 Data Mining & Databases — briefly describe
3154. F3154 Software Engineering — conversion
3155. F3155 Other/Unknown — wavelength conversion
3156. F3156 Software Engineering — csail
3157. F3157 Mathematics — flat
3158. F3158 Curriculum-only — flat application address
3159. F3159 Mathematics — flat piece
3160. F3160 Other/Unknown — holographic displays
3161. F3161 Software Engineering — compiling flex to flat
3162. F3162 Computer Networks — markup
3163. F3163 Curriculum-only — document database
3164. F3164 Data Mining & Databases — text document
3165. F3165 Distributed Systems & Cloud — million document
3166. F3166 ML & AI — idf
3167. F3167 Distributed Systems & Cloud — email
3168. F3168 Curriculum-only — dns and email
3169. F3169 Data Mining & Databases — email sent
3170. F3170 ML & AI — number of document
3171. F3171 Mathematics — Document preparation
3172. F3172 Algorithms & Theory of CS — poke mon
3173. F3173 Mathematics — nov
3174. F3174 Distributed Systems & Cloud — jul-nov
3175. F3175 Mathematics — typing email
3176. F3176 NLP & Speech — wordx
3177. F3177 Software Engineering — documentation
3178. F3178 Cryptography & Security — contract
3179. F3179 Curriculum-only — data documentation
3180. F3180 Distributed Systems & Cloud — inconsistency
3181. F3181 Mathematics — invariant
3182. F3182 Algorithms & Theory of CS — structure algorithm
3183. F3183 Curriculum-only — invariant of transformation
3184. F3184 Distributed Systems & Cloud — simulation relation
3185. F3185 Algorithms & Theory of CS — polynomial multiplication
3186. F3186 Curriculum-only — traversal that build
3187. F3187 Information Theory & Coding — invariant set
3188. F3188 Mathematics — coordinate invariant
3189. F3189 Curriculum-only — arbitrage detection in exchange rate
3190. F3190 Mathematics — candidate
3191. F3191 Curriculum-only — candidate keys
3192. F3192 Mathematics — contract paying
3193. F3193 Algorithms & Theory of CS — disjoint-set data structure
3194. F3194 Curriculum-only — disjoint or overlapping
3195. F3195 Distributed Systems & Cloud — node-disjoint paths
3196. F3196 Mathematics — a1 a2
3197. F3197 Algorithms & Theory of CS — interest include
3198. F3198 Curriculum-only — interest flooding
3199. F3199 Mathematics — compound interest
3200. F3200 Cryptography & Security — blockchain and money
3201. F3201 Curriculum-only — decimal for currency
3202. F3202 Mathematics — amount of money
3203. F3203 Curriculum-only — opentelemetry as the vendor-neutral standard
3204. F3204 Mathematics — parallelogram
3205. F3205 Curriculum-only — trace plot
3206. F3206 Mathematics — translational
3207. F3207 Curriculum-only — invariant direct sum
3208. F3208 Mathematics — eigenspace
3209. F3209 Data Mining & Databases — diffusion map
3210. F3210 Mathematics — complex eigenvalue
3211. F3211 Curriculum-only — mru for repeated scan
3212. F3212 Mathematics — sum and product
3213. F3213 Operating Systems — unreachable
3214. F3214 Other/Unknown — current interest
3215. F3215 Mathematics — switching
3216. F3216 Curriculum-only — multicast switching
3217. F3217 Mathematics — switching systems
3218. F3218 NLP & Speech — tut
3219. F3219 Computer Networks — router
3220. F3220 Curriculum-only — side-buffered deflection router
3221. F3221 Information Theory & Coding — multi-hop network
3222. F3222 Mathematics — link
3223. F3223 Computer Networks — link structure
3224. F3224 Curriculum-only — biconnectedness by the low-link value
3225. F3225 Distributed Systems & Cloud — destination
3226. F3226 Information Theory & Coding — data link
3227. F3227 Mathematics — link suggest
3228. F3228 Curriculum-only — medium or long
3229. F3229 Information Theory & Coding — medium access
3230. F3230 Mathematics — bulk modulus
3231. F3231 Curriculum-only — burn-rate alerting with multiple window
3232. F3232 Data Mining & Databases — multiple time
3233. F3233 Distributed Systems & Cloud — multiple computer
3234. F3234 Information Theory & Coding — multiple client
3235. F3235 Mathematics — backward
3236. F3236 Algorithms & Theory of CS — amplification factor
3237. F3237 Mathematics — backward difference
3238. F3238 Curriculum-only — die cost
3239. F3239 Mathematics — re ector
3240. F3240 Algorithms & Theory of CS — shortest path tree
3241. F3241 Computer Networks — multiple routes
3242. F3242 Curriculum-only — escape route
3243. F3243 Distributed Systems & Cloud — asynchronous
3244. F3244 Data Mining & Databases — asynchronous computing
3245. F3245 Distributed Systems & Cloud — asynchronous programming
3246. F3246 Information Theory & Coding — routing protocol
3247. F3247 Algorithms & Theory of CS — ase
3248. F3248 Mathematics — sharing
3249. F3249 Cryptography & Security — risk sharing
3250. F3250 Curriculum-only — confidence and sharing rule
3251. F3251 Distributed Systems & Cloud — File sharing
3252. F3252 Mathematics — stability
3253. F3253 Algorithms & Theory of CS — absolute stability
3254. F3254 Curriculum-only — read stability
3255. F3255 Mathematics — backward stability
3256. F3256 NLP & Speech — conducting medium
3257. F3257 Operating Systems — Backward compatibility
3258. F3258 Curriculum-only — branch and branch-and-link
3259. F3259 Operating Systems — context switching
3260. F3260 Other/Unknown — asynchronous counter
3261. F3261 Curriculum-only — framing of the whole domain
3262. F3262 Other/Unknown — krylov
3263. F3263 Mathematics — krylov space
3264. F3264 Other/Unknown — robust stability
3265. F3265 Signal/Image/Audio/Video Processing — continuity argument
3266. F3266 Mathematics — proof writing
3267. F3267 Signal/Image/Audio/Video Processing — translational motion
3268. F3268 Software Engineering — abstraction function
3269. F3269 Mathematics — rep
3270. F3270 Operating Systems — generalizing abstraction function
3271. F3271 Software Engineering — asynchronous call
3272. F3272 Mathematics — website
3273. F3273 Software Engineering — endgame database
3274. F3274 Mathematics — pascal
3275. F3275 Algorithms & Theory of CS — hypergraph
3276. F3276 Mathematics — enumeration
3277. F3277 Curriculum-only — ecmp path enumeration
3278. F3278 Mathematics — enumeration tree
3279. F3279 Curriculum-only — intersect and except
3280. F3280 Mathematics — multinomial coefficient
3281. F3281 Algorithms & Theory of CS — chosen uniformly
3282. F3282 Curriculum-only — uniform fit
3283. F3283 Information Theory & Coding — uniform graph
3284. F3284 ML & AI — uniform stability
3285. F3285 Mathematics — discrete uniform law
3286. F3286 Curriculum-only — calculus definition and the series
3287. F3287 Distributed Systems & Cloud — series-parallel graph
3288. F3288 Mathematics — alternating series
3289. F3289 Curriculum-only — interleaved addressing with divergent branch
3290. F3290 Mathematics — finite sum
3291. F3291 Mathematics — number converge
3292. F3292 Algorithms & Theory of CS — amortized cost
3293. F3293 Curriculum-only — api root
3294. F3294 Data Mining & Databases — root function
3295. F3295 Mathematics — complex root
3296. F3296 Curriculum-only — quadratics with complex root
3297. F3297 Mathematics — cube
3298. F3298 Algorithms & Theory of CS — corner cube
3299. F3299 Mathematics — eigenvalue and eigenvector
3300. F3300 Algorithms & Theory of CS — perpendicular bisector
3301. F3301 Computer Networks — symmetric keys
3302. F3302 Curriculum-only — doubling symmetric key length
3303. F3303 Mathematics — concluding
3304. F3304 Computer Networks — decision node
3305. F3305 Curriculum-only — condition-and-decision
3306. F3306 Data Mining & Databases — initial decision
3307. F3307 Distributed Systems & Cloud — readiness
3308. F3308 ML & AI — decision boundary
3309. F3309 Information Theory & Coding — squared distance
3310. F3310 ML & AI — mahalanobis distance
3311. F3311 Mathematics — diagonal matrix
3312. F3312 Curriculum-only — angular region to disk
3313. F3313 ML & AI — playground
3314. F3314 Mathematics — appropriate region
3315. F3315 Computer Architecture — circuit and electronics
3316. F3316 Curriculum-only — nonlinear least square
3317. F3317 Data Mining & Databases — data stream
3318. F3318 Mathematics — nonlinear filter
3319. F3319 Curriculum-only — qnorm and rnorm
3320. F3320 Mathematics — critical
3321. F3321 Cryptography & Security — critical infrastructure
3322. F3322 Curriculum-only — critical word
3323. F3323 Distributed Systems & Cloud — cpu1
3324. F3324 Mathematics — derivative test
3325. F3325 Curriculum-only — lipschitz continuity and directional derivative
3326. F3326 Mathematics — multiplier
3327. F3327 Curriculum-only — alternating direction method of multiplier
3328. F3328 Mathematics — taylor
3329. F3329 Curriculum-only — taylor and maclaurin theorem and series
3330. F3330 Mathematics — proof of taylor
3331. F3331 Curriculum-only — series and power series
3332. F3332 Mathematics — formal power series
3333. F3333 Curriculum-only — theorem of calculus are sketched
3334. F3334 Mathematics — transience
3335. F3335 NLP & Speech — left-corner
3336. F3336 Mathematics — upper-left corner
3337. F3337 Operating Systems — local decisions
3338. F3338 Other/Unknown — corner detection
3339. F3339 Mathematics — curl
3340. F3340 Curriculum-only — gradient and curl
3341. F3341 Mathematics — eld
3342. F3342 Curriculum-only — double and triple integral
3343. F3343 Mathematics — surface integral
3344. F3344 Curriculum-only — line and surface integral
3345. F3345 Mathematics — divergence theorem
3346. F3346 Other/Unknown — stator flux
3347. F3347 Signal/Image/Audio/Video Processing — ce saro
3348. F3348 Curriculum-only — continuous batching and quantization
3349. F3349 Signal/Image/Audio/Video Processing — parameter quantization
3350. F3350 Software Engineering — critical component
3351. F3351 Curriculum-only — design decision for document
3352. F3352 Software Engineering — hug
3353. F3353 Curriculum-only — loop invariant and variant
3354. F3354 Software Engineering — matrix of eigenvector
3355. F3355 Curriculum-only — router microarchitecture
3356. F3356 Software Engineering — multiple classification
3357. F3357 Computer Architecture — cmo recipe
3358. F3358 Software Engineering — redex
3359. F3359 Mathematics — choose
3360. F3360 Curriculum-only — choose among the option
3361. F3361 Mathematics — choosing
3362. F3362 Algorithms & Theory of CS — choosing prize
3363. F3363 Curriculum-only — choosing between sql
3364. F3364 Mathematics — deck of card
3365. F3365 Computer Networks — incumbent
3366. F3366 Algorithms & Theory of CS — relaxation
3367. F3367 Curriculum-only — bound-and-maximise argument
3368. F3368 Mathematics — poker hand
3369. F3369 Algorithms & Theory of CS — revisited
3370. F3370 Mathematics — bradley
3371. F3371 Distributed Systems & Cloud — bradley kuszmaul
3372. F3372 Mathematics — number of ace
3373. F3373 Algorithms & Theory of CS — successive refinement
3374. F3374 Computer Networks — choice of strategy
3375. F3375 Curriculum-only — continuous improvement strategy
3376. F3376 Data Mining & Databases — relational database
3377. F3377 HS ComputerScience Class XII / Unit 3: Database Management — relational data model
3378. F3378 Curriculum-only — dual decomposition
3379. F3379 Data Mining & Databases — write strategy
3380. F3380 Distributed Systems & Cloud — brief description
3381. F3381 Mathematics — probability of selecting
3382. F3382 Curriculum-only — weak file permission
3383. F3383 Mathematics — maximum principle
3384. F3384 NLP & Speech — entity
3385. F3385 Computer Networks — entity type
3386. F3386 Curriculum-only — entity or attribute
3387. F3387 Data Mining & Databases — weak entity
3388. F3388 Curriculum-only — weak-entity type
3389. F3389 Operating Systems — weak-ordering
3390. F3390 Other/Unknown — bidding strategy
3391. F3391 Software Engineering — reduce conflict
3392. F3392 Mathematics — happen
3393. F3393 Curriculum-only — report an unsynchronised conflicting access when it happen in the run
3394. F3394 Mathematics — happened
3395. F3395 Curriculum-only — run again whatever happened
3396. F3396 Mathematics — joint event
3397. F3397 HS ComputerScience Class XI / Unit 2: Computational Thinking and Programming - I — conditional
3398. F3398 Curriculum-only — conditional and biconditional
3399. F3399 ML & AI — naive
3400. F3400 Mathematics — base rate
3401. F3401 Curriculum-only — bayes optimal predictor
3402. F3402 Mathematics — bayes variation
3403. F3403 Curriculum-only — conditional probability and bayes theorem
3404. F3404 Mathematics — conditional distribution
3405. F3405 Curriculum-only — gaussian marginalization and conditioning
3406. F3406 Mathematics — die roll
3407. F3407 Software Engineering — conditional gradient
3408. F3408 Curriculum-only — commit and rollback
3409. F3409 Software Engineering — exec
3410. F3410 Operating Systems — number of byte
3411. F3411 Information Theory & Coding — distance vector
3412. F3412 Mathematics — infinity
3413. F3413 Algorithms & Theory of CS — multiple infinity
3414. F3414 Mathematics — infinity norm
3415. F3415 Other/Unknown — region descriptor
3416. F3416 Software Engineering — runtime structure
3417. F3417 Computer Networks — cascading
3418. F3418 Algorithms & Theory of CS — fractional cascading
3419. F3419 Cryptography & Security — cascading failure
3420. F3420 Curriculum-only — akka style
3421. F3421 Curriculum-only — swim-style
3422. F3422 Mathematics — lii
3423. F3423 Software Engineering — modifying style
3424. F3424 Curriculum-only — wait-die and wound-wait scheme
3425. F3425 Software Engineering — write-up
3426. F3426 Curriculum-only — read from the public case write-up
3427. F3427 Software Engineering — additionally
3428. F3428 Distributed Systems & Cloud — storing
3429. F3429 Signal/Image/Audio/Video Processing — surface orientation
3430. F3430 Data Mining & Databases — grey
3431. F3431 Distributed Systems & Cloud — bidirectional
3432. F3432 ML & AI — grey-box
3433. F3433 Curriculum-only — grey-box and random testing
3434. F3434 Mathematics — red
3435. F3435 Distributed Systems & Cloud — synch
3436. F3436 Mathematics — green
3437. F3437 Other/Unknown — stoke
3438. F3438 Curriculum-only — gauss and stoke theorem
3439. F3439 Mathematics — gradient field
3440. F3440 Other/Unknown — stokes parameters
3441. F3441 Signal/Image/Audio/Video Processing — grey level
3442. F3442 Mathematics — applied
3443. F3443 Curriculum-only — applied extra
3444. F3444 Mathematics — applied mathematics
3445. F3445 Data Mining & Databases — richard
3446. F3446 Software Engineering — astronaut
3447. F3447 Mathematics — cosine
3448. F3448 Curriculum-only — cosine as the real
3449. F3449 Mathematics — direction cosine
3450. F3450 Algorithms & Theory of CS — Euclidean vector
3451. F3451 Data Mining & Databases — non-euclidean
3452. F3452 Mathematics — old
3453. F3453 Curriculum-only — old and new row
3454. F3454 Mathematics — trig
3455. F3455 Algorithms & Theory of CS — partial match
3456. F3456 Curriculum-only — partial least square
3457. F3457 Data Mining & Databases — calculable partial
3458. F3458 Distributed Systems & Cloud — partial failure
3459. F3459 ML & AI — partial path
3460. F3460 Mathematics — di erential equation
3461. F3461 Cryptography & Security — settlement fail
3462. F3462 Curriculum-only — api call that fail
3463. F3463 Mathematics — integral calculus
3464. F3464 HS Maths Class XII / Unit-III: Calculus — differential equation
3465. F3465 Mathematics — characteristic polynomial
3466. F3466 Algorithms & Theory of CS — discrete mathematics
3467. F3467 Curriculum-only — correspondence with the algebra
3468. F3468 Data Mining & Databases — algebra and calculus
3469. F3469 Mathematics — algebra and number
3470. F3470 Algorithms & Theory of CS — fkg inequality
3471. F3471 Curriculum-only — gronwall inequality
3472. F3472 Data Mining & Databases — matrix am-gm inequality
3473. F3473 Information Theory & Coding — fano inequality
3474. F3474 ML & AI — bernstein inequality
3475. F3475 Mathematics — bounding
3476. F3476 Algorithms & Theory of CS — bounding volume
3477. F3477 Mathematics — concluded
3478. F3478 Algorithms & Theory of CS — hamilton
3479. F3479 Mathematics — katrin wehrheim
3480. F3480 Curriculum-only — accepted phase
3481. F3481 Mathematics — mathlet phase
3482. F3482 Information Theory & Coding — r0 r1 r2
3483. F3483 Mathematics — rudin
3484. F3484 Distributed Systems & Cloud — flag
3485. F3485 Mathematics — ave
3486. F3486 Algorithms & Theory of CS — critter
3487. F3487 Information Theory & Coding — capacity
3488. F3488 Algorithms & Theory of CS — edmond
3489. F3489 Computer Architecture — total capacity
3490. F3490 Curriculum-only — capacity log
3491. F3491 Data Mining & Databases — detroit
3492. F3492 Information Theory & Coding — channel coding
3493. F3493 Mathematics — commodity
3494. F3494 Curriculum-only — commodity failure
3495. F3495 Mathematics — negative integer
3496. F3496 NLP & Speech — resource capacity
3497. F3497 Operating Systems — cell storage
3498. F3498 Curriculum-only — central assumption that failure are fail-stop
3499. F3499 Other/Unknown — functor
3500. F3500 Signal/Image/Audio/Video Processing — definition and inequality
3501. F3501 Computer Architecture — adder
3502. F3502 Cryptography & Security — digital cash
3503. F3503 CS2023 gap-fill — Attacks on forensics and preventing such attacks
3504. F3504 Cryptography & Security — digital id
3505. F3505 Curriculum-only — half and full adder
3506. F3506 Data Mining & Databases — babbage
3507. F3507 Distributed Systems & Cloud — digital picture
3508. F3508 Information Theory & Coding — digital informations
3509. F3509 Mathematics — domino
3510. F3510 Distributed Systems & Cloud — domino effect
3511. F3511 Operating Systems — loopback
3512. F3512 Other/Unknown — digital arithmetic
3513. F3513 Signal/Image/Audio/Video Processing — delays
3514. F3514 Mathematics — queueing
3515. F3515 Curriculum-only — input queueing
3516. F3516 Information Theory & Coding — fair queueing
3517. F3517 Mathematics — exponentially distributed
3518. F3518 Distributed Systems & Cloud — service
3519. F3519 Computer Networks — service delivery
3520. F3520 Curriculum-only — categorise through the category service
3521. F3521 Curriculum-only — service delete expired paste
3522. F3522 Distributed Systems & Cloud — access management
3523. F3523 Curriculum-only — lease and fencing
3524. F3524 Distributed Systems & Cloud — service platform
3525. F3525 Mathematics — asset
3526. F3526 Curriculum-only — asset value
3527. F3527 Data Mining & Databases — total asset
3528. F3528 Mathematics — queueing system
3529. F3529 Information Theory & Coding — stability of queueing system
3530. F3530 Other/Unknown — ancillary service
3531. F3531 Cryptography & Security — deployment consideration
3532. F3532 Curriculum-only — multi-tier deployment
3533. F3533 Distributed Systems & Cloud — deployment model
3534. F3534 Curriculum-only — cloud computing service and deployment model
3535. F3535 Other/Unknown — financial
3536. F3536 Computer Networks — financial network
3537. F3537 Cryptography & Security — financial account
3538. F3538 Curriculum-only — million financial account
3539. F3539 Mathematics — capital
3540. F3540 Algorithms & Theory of CS — number of round
3541. F3541 Curriculum-only — four-round feistel
3542. F3542 Other/Unknown — financial statement
3543. F3543 Curriculum-only — pricing style
3544. F3544 ML & AI — dynamic pricing
3545. F3545 Mathematics — asset pricing
3546. F3546 Other/Unknown — option pricing
3547. F3547 Signal/Image/Audio/Video Processing — finite number of adder
3548. F3548 Mathematics — linear homogeneous differential equation
3549. F3549 Signal/Image/Audio/Video Processing — number of delays
3550. F3550 Software Engineering — arena
3551. F3551 Data Mining & Databases — python programming language
3552. F3552 Software Engineering — architectural
3553. F3553 Curriculum-only — unique architectural difference
3554. F3554 Operating Systems — architectural vulnerability factor
3555. F3555 Software Engineering — engineering
3556. F3556 Algorithms & Theory of CS — engineering curriculum
3557. F3557 Computer Networks — engineering computation
3558. F3558 Curriculum-only — detection engineering
3559. F3559 Information Theory & Coding — meng
3560. F3560 Mathematics — calendar
3561. F3561 Other/Unknown — automation
3562. F3562 Cryptography & Security — fuzzing
3563. F3563 Curriculum-only — fuzzing with go test fuzz
3564. F3564 ML & AI — automated
3565. F3565 Other/Unknown — biochemical engineering
3566. F3566 Data Mining & Databases — franklin
3567. F3567 Curriculum-only — boneh franklin scheme
3568. F3568 Mathematics — death
3569. F3569 Data Mining & Databases — death rate
3570. F3570 Other/Unknown — engineering material
3571. F3571 Software Engineering — automated systems
3572. F3572 Curriculum-only — abstraction and polymorphism
3573. F3573 Other/Unknown — logic
3574. F3574 Algorithms & Theory of CS — xor
3575. F3575 Computer Architecture — carry logic
3576. F3576 Cryptography & Security — m1 xor m2
3577. F3577 Curriculum-only — cost-based optimiser logic
3578. F3578 Data Mining & Databases — formal logic
3579. F3579 Mathematics — fol
3580. F3580 Other/Unknown — description logic
3581. F3581 Computer Architecture — archana venkataraman
3582. F3582 Curriculum-only — boolean function and of finite-state machine
3583. F3583 Mathematics — diagram
3584. F3584 Algorithms & Theory of CS — Decision diagrams
3585. F3585 Computer Architecture — pipeline diagram
3586. F3586 Computer Networks — component diagram
3587. F3587 Curriculum-only — diagram type
3588. F3588 Data Mining & Databases — er diagram
3589. F3589 Distributed Systems & Cloud — register-file port
3590. F3590 ML & AI — breast
3591. F3591 Mathematics — chord diagram
3592. F3592 Curriculum-only — generated input
3593. F3593 Mathematics — finitely generated
3594. F3594 Operating Systems — physical register file
3595. F3595 Other/Unknown — computer generated holograms
3596. F3596 Mathematics — picard
3597. F3597 Other/Unknown — phase diagram
3598. F3598 Signal/Image/Audio/Video Processing — signal
3599. F3599 Algorithms & Theory of CS — nonlinear circuit
3600. F3600 Computer Architecture — dc bias
3601. F3601 Curriculum-only — process it and signal completion
3602. F3602 Data Mining & Databases — xcor
3603. F3603 Information Theory & Coding — bits-signal boundary
3604. F3604 Mathematics — amplitude
3605. F3605 Information Theory & Coding — amplitude and phase
3606. F3606 Mathematics — continuous time
3607. F3607 Curriculum-only — deterministic discrete and continuous time
3608. F3608 Mathematics — distribution of amplitude
3609. F3609 Algorithms & Theory of CS — noise and error
3610. F3610 Computer Architecture — audio signal
3611. F3611 Computer Networks — time spread
3612. F3612 Curriculum-only — count-min sketch for frequency
3613. F3613 Data Mining & Databases — frequent
3614. F3614 Computer Networks — frequent physical obstruction
3615. F3615 Data Mining & Databases — time difference
3616. F3616 Information Theory & Coding — frequency distribution
3617. F3617 Data Mining & Databases — histogram
3618. F3618 Information Theory & Coding — frequency hopping
3619. F3619 ML & AI — frequent items
3620. F3620 Mathematics — circular frequency
3621. F3621 Cryptography & Security — computed jump
3622. F3622 Mathematics — jump process
3623. F3623 Curriculum-only — tan for in radian
3624. F3624 Mathematics — cube root
3625. F3625 Algorithms & Theory of CS — mod log
3626. F3626 Data Mining & Databases — coefficient of hd
3627. F3627 Mathematics — a2 mod
3628. F3628 Mathematics — mod-p
3629. F3629 Curriculum-only — bias of convenience sample
3630. F3630 Data Mining & Databases — hold-out
3631. F3631 Curriculum-only — hold out rating
3632. F3632 Distributed Systems & Cloud — sample file
3633. F3633 ML & AI — burn-in
3634. F3634 Mathematics — population
3635. F3635 Computer Networks — lyapunov function
3636. F3636 Curriculum-only — common population distribution
3637. F3637 Mathematics — population dynamics
3638. F3638 Curriculum-only — non-linear population dynamics
3639. F3639 Mathematics — population parameter
3640. F3640 NLP & Speech — interaural time difference
3641. F3641 Operating Systems — bypass signal
3642. F3642 Other/Unknown — eeg signals
3643. F3643 Information Theory & Coding — nature of quantum mechanics
3644. F3644 Mathematics — linear algebra
3645. F3645 Algorithms & Theory of CS — linear algebra operation
3646. F3646 Algorithms & Theory of CS — traveling salesman problem
3647. F3647 Cryptography & Security — os security
3648. F3648 Curriculum-only — connection to the linear algebra
3649. F3649 Data Mining & Databases — erdos-hajnal conjecture
3650. F3650 Algorithms & Theory of CS — least recently used
3651. F3651 Distributed Systems & Cloud — d4m
3652. F3652 ML & AI — sc linear algebra
3653. F3653 Mathematics — city
3654. F3654 Algorithms & Theory of CS — claw covering
3655. F3655 Distributed Systems & Cloud — covering equivalent material
3656. F3656 Mathematics — cubic
3657. F3657 Algorithms & Theory of CS — cubic graph
3658. F3658 Curriculum-only — cubic and bbr
3659. F3659 Mathematics — eigenvector and eigenvalue
3660. F3660 Curriculum-only — cover all important aspect including normalization
3661. F3661 Data Mining & Databases — schema normalization
3662. F3662 Mathematics — progression
3663. F3663 Curriculum-only — arithmetic and geometric progression
3664. F3664 Mathematics — related rate
3665. F3665 Curriculum-only — tournament predictor that choose between predictor
3666. F3666 Mathematics — twin
3667. F3667 Other/Unknown — applied linear algebra
3668. F3668 Distributed Systems & Cloud — network evaluation metrics
3669. F3669 Other/Unknown — finite dimensional
3670. F3670 Curriculum-only — matrix completion by iterated truncated svd
3671. F3671 Other/Unknown — vibration signal
3672. F3672 Signal/Image/Audio/Video Processing — biorthogonal
3673. F3673 Information Theory & Coding — biorthogonal code
3674. F3674 Signal/Image/Audio/Video Processing — circulant matrix
3675. F3675 Mathematics — periodic
3676. F3676 Algorithms & Theory of CS — periodic motion
3677. F3677 Mathematics — periodic structures
3678. F3678 Signal/Image/Audio/Video Processing — effect of windowing
3679. F3679 Curriculum-only — arithmetic and geometric sequence
3680. F3680 Signal/Image/Audio/Video Processing — h1 h0
3681. F3681 Mathematics — dirac
3682. F3682 Curriculum-only — dirac and ore condition
3683. F3683 Mathematics — dirac distribution
3684. F3684 Other/Unknown — arma
3685. F3685 Mathematics — autocorrelation
3686. F3686 Signal/Image/Audio/Video Processing — autocorrelation matrix
3687. F3687 Mathematics — analog
3688. F3688 Computer Architecture — adc
3689. F3689 Curriculum-only — hardware analogue
3690. F3690 Mathematics — analog of theorem
3691. F3691 Other/Unknown — analog integrated circuit
3692. F3692 Signal/Image/Audio/Video Processing — Analog computers
3693. F3693 Mathematics — capacitor
3694. F3694 Computer Architecture — diode
3695. F3695 Mathematics — constant input signal
3696. F3696 Information Theory & Coding — pressure drop
3697. F3697 Other/Unknown — junction
3698. F3698 Mathematics — indirect
3699. F3699 Other/Unknown — p-n junction
3700. F3700 Signal/Image/Audio/Video Processing — inductor
3701. F3701 Other/Unknown — short circuit
3702. F3702 Signal/Image/Audio/Video Processing — instantaneous frequency
3703. F3703 Computer Architecture — fir lowpass filter
3704. F3704 Signal/Image/Audio/Video Processing — analog filter
3705. F3705 Mathematics — invariance
3706. F3706 Signal/Image/Audio/Video Processing — highpass
3707. F3707 ML & AI — reconstruction-based
3708. F3708 Mathematics — total variation reconstruction
3709. F3709 Signal/Image/Audio/Video Processing — ak0
3710. F3710 Signal/Image/Audio/Video Processing — ssi
3711. F3711 Curriculum-only — system with input and output
3712. F3712 Other/Unknown — linear time-invariant
3713. F3713 Mathematics — superposition
3714. F3714 Algorithms & Theory of CS — quantum superposition
3715. F3715 Computer Architecture — linear circuit
3716. F3716 Mathematics — principle of superposition
3717. F3717 Other/Unknown — linear time invariant system
3718. F3718 Signal/Image/Audio/Video Processing — lmmse
3719. F3719 Mathematics — estimator
3720. F3720 Curriculum-only — k-minimum-value estimator
3721. F3721 ML & AI — ml estimator
3722. F3722 Mathematics — asymptotic level
3723. F3723 Algorithms & Theory of CS — bivariate function
3724. F3724 Mathematics — hypothesis
3725. F3725 Data Mining & Databases — multiple hypothesis
3726. F3726 Mathematics — alter
3727. F3727 Curriculum-only — alter and drop
3728. F3728 Mathematics — contin
3729. F3729 Algorithms & Theory of CS — binary decision
3730. F3730 Data Mining & Databases — multiple testing
3731. F3731 Mathematics — interested in computing
3732. F3732 Data Mining & Databases — high dimension
3733. F3733 Mathematics — likelihood ratio
3734. F3734 Mathematics — sample variance
3735. F3735 Curriculum-only — one-sided error of count-min
3736. F3736 Distributed Systems & Cloud — one-sided communication
3737. F3737 Mathematics — alternative hypothesis
3738. F3738 Other/Unknown — testing of hypothesis
3739. F3739 Signal/Image/Audio/Video Processing — lmmse estimation
3740. F3740 Curriculum-only — filtering and rounding
3741. F3741 Data Mining & Databases — amy
3742. F3742 Distributed Systems & Cloud — bloom filtering
3743. F3743 Information Theory & Coding — inverse filtering
3744. F3744 Signal/Image/Audio/Video Processing — lti system
3745. F3745 Mathematics — stable
3746. F3746 Curriculum-only — stable identity
3747. F3747 Mathematics — asymptotically stable
3748. F3748 Signal/Image/Audio/Video Processing — dt system
3749. F3749 Information Theory & Coding — channel
3750. F3750 Cryptography & Security — covert channels
3751. F3751 Curriculum-only — channel that nobody close
3752. F3752 Distributed Systems & Cloud — locality
3753. F3753 Curriculum-only — principle of locality
3754. F3754 Distributed Systems & Cloud — data locality
3755. F3755 Information Theory & Coding — audiocom
3756. F3756 Curriculum-only — fading-capacity case are named
3757. F3757 Information Theory & Coding — flat fading
3758. F3758 Distributed Systems & Cloud — shared
3759. F3759 Curriculum-only — register file as the shared resource of wide
3760. F3760 Distributed Systems & Cloud — chat and shared
3761. F3761 Other/Unknown — ion channel
3762. F3762 Signal/Image/Audio/Video Processing — digital frequency response
3763. F3763 Other/Unknown — frequency selective fading
3764. F3764 Signal/Image/Audio/Video Processing — frequency-selective filter
3765. F3765 Mathematics — hermitian form
3766. F3766 Signal/Image/Audio/Video Processing — bilinear tran
3767. F3767 Mathematics — summability
3768. F3768 Signal/Image/Audio/Video Processing — ce saro summable
3769. F3769 Information Theory & Coding — acoustic sources
3770. F3770 Mathematics — female
3771. F3771 Algorithms & Theory of CS — relaxed decision
3772. F3772 Curriculum-only — training job on cpus
3773. F3773 Distributed Systems & Cloud — job scheduling
3774. F3774 Mathematics — hedge fund
3775. F3775 NLP & Speech — fricative
3776. F3776 Curriculum-only — non-production only on the current
3777. F3777 ML & AI — production rule
3778. F3778 Mathematics — overtime
3779. F3779 NLP & Speech — speech production
3780. F3780 Mathematics — lip
3781. F3781 NLP & Speech — constriction
3782. F3782 Information Theory & Coding — supraglottal constriction
3783. F3783 NLP & Speech — theory of speech production
3784. F3784 Operating Systems — job interview
3785. F3785 Other/Unknown — joint venture
3786. F3786 Signal/Image/Audio/Video Processing — cavity
3787. F3787 Mathematics — equation and z-transform
3788. F3788 Signal/Image/Audio/Video Processing — bilateral z-transform
3789. F3789 Curriculum-only — unilateral and bilateral z-transform
3790. F3790 Signal/Image/Audio/Video Processing — zero-order hold
3791. F3791 Software Engineering — arithmetic and logic
3792. F3792 Mathematics — subtraction
3793. F3793 Curriculum-only — subtraction of signed number
3794. F3794 Mathematics — flop
3795. F3795 Algorithms & Theory of CS — n2 flop
3796. F3796 Mathematics — elimination
3797. F3797 Data Mining & Databases — contraint elimination
3798. F3798 Distributed Systems & Cloud — lu decomposition
3799. F3799 Algorithms & Theory of CS — sparse
3800. F3800 Curriculum-only — limitation of sparse
3801. F3801 Data Mining & Databases — available online
3802. F3802 Distributed Systems & Cloud — sparse table
3803. F3803 Information Theory & Coding — achieving
3804. F3804 ML & AI — sparse approximations
3805. F3805 Mathematics — anti-elimination
3806. F3806 Algorithms & Theory of CS — floyd warshall
3807. F3807 Curriculum-only — floyd warshall and johnson
3808. F3808 Data Mining & Databases — johnson and wichern
3809. F3809 Mathematics — chi
3810. F3810 Curriculum-only — multivariate probability distribution
3811. F3811 ML & AI — mean vector
3812. F3812 Mathematics — likelihood ratio test
3813. F3813 Curriculum-only — sparsity make it solvable
3814. F3814 Mathematics — subtour elimination constraint
3815. F3815 Other/Unknown — compressed sensing
3816. F3816 ML & AI — nuclear norm
3817. F3817 Mathematics — prove
3818. F3818 Algorithms & Theory of CS — doob martingale
3819. F3819 Distributed Systems & Cloud — omission
3820. F3820 Mathematics — appeal
3821. F3821 Curriculum-only — coordinate-free algebraic
3822. F3822 Mathematics — algebraic closure
3823. F3823 Curriculum-only — birthday simulator
3824. F3824 Mathematics — birthday match
3825. F3825 Curriculum-only — memory contradiction
3826. F3826 Mathematics — contrapositive
3827. F3827 Computer Architecture — truth table
3828. F3828 Curriculum-only — contradiction and by contrapositive
3829. F3829 Mathematics — contrast
3830. F3830 Curriculum-only — contrast between queueing
3831. F3831 Mathematics — converse
3832. F3832 Curriculum-only — disproof and counter-example
3833. F3833 Mathematics — direct proof
3834. F3834 Algorithms & Theory of CS — b1 and b2
3835. F3835 Curriculum-only — algebraic equivalence
3836. F3836 Distributed Systems & Cloud — equivalence rule
3837. F3837 Information Theory & Coding — bps
3838. F3838 Mathematics — disjunctive normal form
3839. F3839 Curriculum-only — minimal base image running
3840. F3840 Mathematics — minimal cover
3841. F3841 Curriculum-only — confidence and lift
3842. F3842 Data Mining & Databases — k-lift of graph
3843. F3843 Mathematics — mutually independent
3844. F3844 Curriculum-only — non-trivial mvd
3845. F3845 Mathematics — primitive element
3846. F3846 Algorithms & Theory of CS — mar orbit
3847. F3847 Curriculum-only — orbit counting
3848. F3848 Mathematics — periodic orbits
3849. F3849 Algorithms & Theory of CS — strategy for proving
3850. F3850 Mathematics — primality
3851. F3851 Cryptography & Security — certificate
3852. F3852 Computer Networks — revocation
3853. F3853 Cryptography & Security — certificate authority
3854. F3854 Curriculum-only — cascading revocation
3855. F3855 Mathematics — primality testing
3856. F3856 Curriculum-only — meaning primality testing
3857. F3857 Mathematics — relative maximum
3858. F3858 Algorithms & Theory of CS — number of satisfying
3859. F3859 Mathematics — pxn
3860. F3860 Information Theory & Coding — sum-product
3861. F3861 ML & AI — sum-product on trees
3862. F3862 Mathematics — disjoint union
3863. F3863 Curriculum-only — set data structure with disjoint-union
3864. F3864 Mathematics — cartesian product
3865. F3865 Information Theory & Coding — cartesian-product constellation
3866. F3866 Mathematics — c1 c2
3867. F3867 Algorithms & Theory of CS — error convergence
3868. F3868 Curriculum-only — convergence diagnostics
3869. F3869 Mathematics — conditional convergence
3870. F3870 Curriculum-only — absolute and conditional convergence
3871. F3871 Mathematics — convergence in l1
3872. F3872 Algorithms & Theory of CS — relative error
3873. F3873 Curriculum-only — size and convergence rate
3874. F3874 Mathematics — discretization
3875. F3875 Algorithms & Theory of CS — physical quantity
3876. F3876 Mathematics — disk of convergence
3877. F3877 Curriculum-only — infinite series and their convergence
3878. F3878 Mathematics — integral test
3879. F3879 Algorithms & Theory of CS — monotone graph
3880. F3880 Mathematics — dominated convergence theorem
3881. F3881 Mathematics — laplace
3882. F3882 Mathematics — xn converge absolutely
3883. F3883 Other/Unknown — characteristic and minimal
3884. F3884 Curriculum-only — controllability and observability as rank condition
3885. F3885 Other/Unknown — Equivalence principle
3886. F3886 Algorithms & Theory of CS — literal
3887. F3887 NLP & Speech — english
3888. F3888 Curriculum-only — translating english to symbol
3889. F3889 Data Mining & Databases — english expression
3890. F3890 Mathematics — german enigma
3891. F3891 NLP & Speech — english word
3892. F3892 Data Mining & Databases — fertility
3893. F3893 NLP & Speech — pas
3894. F3894 Distributed Systems & Cloud — der pas
3895. F3895 Other/Unknown — gauss elimination
3896. F3896 Curriculum-only — gauss elimination and inverse
3897. F3897 Other/Unknown — heat and laplace
3898. F3898 Curriculum-only — rank and the rank nullity theorem
3899. F3899 Other/Unknown — sharpening
3900. F3900 Signal/Image/Audio/Video Processing — convergence in law
3901. F3901 Other/Unknown — fourier integral theorem
3902. F3902 Signal/Image/Audio/Video Processing — fourier integral of measure
3903. F3903 Software Engineering — algebraic type
3904. F3904 Distributed Systems & Cloud — cse
3905. F3905 Software Engineering — document frequency
3906. F3906 Mathematics — periodic function
3907. F3907 Software Engineering — frequency shift
3908. F3908 Mathematics — experiment
3909. F3909 Cryptography & Security — ordered sequence of experiment
3910. F3910 Curriculum-only — experiment for misra gry
3911. F3911 Data Mining & Databases — collect data
3912. F3912 Distributed Systems & Cloud — post-mortem
3913. F3913 Curriculum-only — post-mortem and official report
3914. F3914 Information Theory & Coding — listener
3915. F3915 Mathematics — cilantro
3916. F3916 Curriculum-only — dimension independence
3917. F3917 Data Mining & Databases — data independence
3918. F3918 Curriculum-only — logical and physical data independence
3919. F3919 ML & AI — cocktail party
3920. F3920 Mathematics — independence hypothesis
3921. F3921 Curriculum-only — longest-chain rule
3922. F3922 Mathematics — division rule
3923. F3923 NLP & Speech — non-restrictive
3924. F3924 Other/Unknown — experimental design
3925. F3925 Mathematics — auxiliary
3926. F3926 Curriculum-only — correlation and relationship
3927. F3927 ML & AI — correlation matrix
3928. F3928 Mathematics — correlation coefficient
3929. F3929 Data Mining & Databases — spearman rank correlation
3930. F3930 Mathematics — sample correlation coefficient
3931. F3931 Other/Unknown — methodology
3932. F3932 Curriculum-only — practical methodology
3933. F3933 Software Engineering — event listener
3934. F3934 Distributed Systems & Cloud — le system
3935. F3935 Algorithms & Theory of CS — indirect addressing
3936. F3936 Curriculum-only — grounded multi-agent support
3937. F3937 Data Mining & Databases — decision support
3938. F3938 Distributed Systems & Cloud — industry support
3939. F3939 Curriculum-only — industry support named
3940. F3940 ML & AI — minimum support
3941. F3941 Operating Systems — support sophisticated
3942. F3942 Other/Unknown — Decision support systems
3943. F3943 Signal/Image/Audio/Video Processing — compact support
3944. F3944 Mathematics — smooth
3945. F3945 Algorithms & Theory of CS — morphism
3946. F3946 Mathematics — covariant functor
3947. F3947 Algorithms & Theory of CS — cayley
3948. F3948 Curriculum-only — adjacency list and matrix
3949. F3949 Distributed Systems & Cloud — incidence matrix
3950. F3950 Mathematics — non-smooth
3951. F3951 Signal/Image/Audio/Video Processing — genus
3952. F3952 Data Mining & Databases — genus formula
3953. F3953 Mathematics — modular
3954. F3954 Curriculum-only — hashing as modular arithmetic
3955. F3955 Mathematics — modular inverse
3956. F3956 Curriculum-only — modular inverse and when it exist
3957. F3957 Mathematics — multiplicative inverse
3958. F3958 Software Engineering — gif
3959. F3959 Mathematics — article
3960. F3960 ML & AI — news article
3961. F3961 Mathematics — came
3962. F3962 Software Engineering — developer
3963. F3963 Computer Networks — world wide web
3964. F3964 Distributed Systems & Cloud — developer library
3965. F3965 Software Engineering — matrix multiply
3966. F3966 Curriculum-only — tiled matrix multiply
3967. F3967 Distributed Systems & Cloud — sparse matrix
3968. F3968 Software Engineering — matrix multiply run
3969. F3969 Information Theory & Coding — meta channel
3970. F3970 Software Engineering — minimumx
3971. F3971 Mathematics — dual
3972. F3972 Algorithms & Theory of CS — dual ascent
3973. F3973 Curriculum-only — dual ascent and dual decomposition
3974. F3974 Data Mining & Databases — ihi
3975. F3975 Distributed Systems & Cloud — dual major
3976. F3976 Information Theory & Coding — dual code
3977. F3977 ML & AI — dual norm
3978. F3978 Mathematics — dual description
3979. F3979 Algorithms & Theory of CS — induction and recursion
3980. F3980 Curriculum-only — induction and reduction is named
3981. F3981 Data Mining & Databases — horse
3982. F3982 Mathematics — casework and strong
3983. F3983 Computer Networks — booklist
3984. F3984 Cryptography & Security — book website
3985. F3985 Curriculum-only — book is in the reading list
3986. F3986 Distributed Systems & Cloud — book series
3987. F3987 Curriculum-only — checked against press and google
3988. F3988 Data Mining & Databases — google adword
3989. F3989 Distributed Systems & Cloud — google file system
3990. F3990 Mathematics — center of mass
3991. F3991 Curriculum-only — inductive hypothesis spelled
3992. F3992 Mathematics — karush kuhn tucker
3993. F3993 Curriculum-only — karush kuhn tucker condition
3994. F3994 Mathematics — lagrangean dual
3995. F3995 Curriculum-only — recompute centre
3996. F3996 Distributed Systems & Cloud — c3i center
3997. F3997 Mathematics — center difference
3998. F3998 Distributed Systems & Cloud — nat
3999. F3999 Mathematics — phase lag
4000. F4000 Curriculum-only — equal primal
4001. F4001 Mathematics — dual linear program
4002. F4002 Algorithms & Theory of CS — running time
4003. F4003 Curriculum-only — euclid algorithm with its running time
4004. F4004 Mathematics — cmax
4005. F4005 Curriculum-only — controlling how instance
4006. F4006 Data Mining & Databases — conjectured instance of tightness
4007. F4007 ML & AI — erent instance of cleb
4008. F4008 Mathematics — cate
4009. F4009 Curriculum-only — tlb and page walker
4010. F4010 Data Mining & Databases — random walker
4011. F4011 Distributed Systems & Cloud — cloud
4012. F4012 Cryptography & Security — cloud-based
4013. F4013 Curriculum-only — cloud anyway
4014. F4014 Curriculum-only — google cloud compute service
4015. F4015 Distributed Systems & Cloud — category of cloud
4016. F4016 Curriculum-only — cloud security and identity
4017. F4017 Distributed Systems & Cloud — cloud service
4018. F4018 Curriculum-only — cloud service apply
4019. F4019 Distributed Systems & Cloud — cloud simulator
4020. F4020 Curriculum-only — google cloud storage
4021. F4021 Distributed Systems & Cloud — cloud-native
4022. F4022 Curriculum-only — generalise the two-stage mapreduce graph
4023. F4023 Data Mining & Databases — elastic mapreduce
4024. F4024 Distributed Systems & Cloud — hadoop
4025. F4025 Curriculum-only — industry list name amazon
4026. F4026 Data Mining & Databases — amazon mechanical turk
4027. F4027 Distributed Systems & Cloud — amazon dynamo
4028. F4028 Curriculum-only — pair amazon dynamo
4029. F4029 Distributed Systems & Cloud — hadoop distributed file system
4030. F4030 Curriculum-only — hadoop and the mapreduce model
4031. F4031 Distributed Systems & Cloud — mapreduce program
4032. F4032 Operating Systems — josh cate
4033. F4033 Other/Unknown — amazon-aw
4034. F4034 Other/Unknown — substitution instance
4035. F4035 Software Engineering — book include
4036. F4036 Data Mining & Databases — extensible hashing
4037. F4037 Curriculum-only — dynamic hashing by extensible hashing
4038. F4038 Software Engineering — display
4039. F4039 Computer Architecture — display logic
4040. F4040 Curriculum-only — dimensionality reduction for display
4041. F4041 Mathematics — cursor
4042. F4042 Curriculum-only — cursor stability
4043. F4043 Mathematics — display system
4044. F4044 Information Theory & Coding — antenna
4045. F4045 Mathematics — antenna element
4046. F4046 Computer Architecture — cosine omega
4047. F4047 Mathematics — random telegraph wave
4048. F4048 Algorithms & Theory of CS — sequence of elementary row
4049. F4049 Mathematics — differential form
4050. F4050 Computer Architecture — external connection
4051. F4051 Curriculum-only — counting external input
4052. F4052 Data Mining & Databases — external data
4053. F4053 Information Theory & Coding — external variable
4054. F4054 Mathematics — linear system
4055. F4055 Curriculum-only — linear system by elimination
4056. F4056 Mathematics — inhomogeneous linear system
4057. F4057 Curriculum-only — runge kutta step for ode
4058. F4058 Mathematics — euler
4059. F4059 Algorithms & Theory of CS — euler backward
4060. F4060 Computer Networks — nigsberg
4061. F4061 Curriculum-only — euler criterion
4062. F4062 Mathematics — euler formula
4063. F4063 Curriculum-only — euler formula and the identity
4064. F4064 Mathematics — euler function
4065. F4065 NLP & Speech — external ear
4066. F4066 Other/Unknown — divider
4067. F4067 Computer Architecture — music
4068. F4068 Curriculum-only — multiplier and divider
4069. F4069 Information Theory & Coding — tone
4070. F4070 Mathematics — music signal
4071. F4071 Other/Unknown — euler theorem
4072. F4072 Curriculum-only — euler phi-function and euler theorem
4073. F4073 Other/Unknown — lamb wave
4074. F4074 Data Mining & Databases — gilbert
4075. F4075 Distributed Systems & Cloud — seth gilbert
4076. F4076 Mathematics — fast fourier transform
4077. F4077 Distributed Systems & Cloud — memory model
4078. F4078 Curriculum-only — memory model are named
4079. F4079 Distributed Systems & Cloud — language memory model
4080. F4080 Mathematics — dit
4081. F4081 Algorithms & Theory of CS — gauss quadrature
4082. F4082 ML & AI — gauss newton
4083. F4083 Mathematics — gauss showed
4084. F4084 Other/Unknown — gauss seidel
4085. F4085 Signal/Image/Audio/Video Processing — continuous-time system
4086. F4086 Mathematics — oscillating
4087. F4087 Signal/Image/Audio/Video Processing — fourier series
4088. F4088 Information Theory & Coding — discrete-time fourier series
4089. F4089 Mathematics — operation on fourier series
4090. F4090 Signal/Image/Audio/Video Processing — fourier series of image
4091. F4091 Information Theory & Coding — channel impulse response
4092. F4092 Mathematics — chebychev
4093. F4093 Curriculum-only — ordinary and exponential generating function
4094. F4094 Mathematics — probability generating function
4095. F4095 Signal/Image/Audio/Video Processing — fir filter
4096. F4096 ML & AI — data manifold
4097. F4097 Signal/Image/Audio/Video Processing — low-dimensional manifold
4098. F4098 Mathematics — finite-impulse response
4099. F4099 Signal/Image/Audio/Video Processing — infinite impulse response
4100. F4100 Software Engineering — computational science
4101. F4101 Data Mining & Databases — javascript
4102. F4102 Information Theory & Coding — gaussian source
4103. F4103 Operating Systems — binary translation
4104. F4104 Software Engineering — assembly language
4105. F4105 Curriculum-only — move on to discuss assembly language
4106. F4106 Software Engineering — css
4107. F4107 Data Mining & Databases — tagged data
4108. F4108 Operating Systems — dispatch
4109. F4109 Cryptography & Security — commitment
4110. F4110 Curriculum-only — dispatch table
4111. F4111 Mathematics — complete proof
4112. F4112 Software Engineering — binding
4113. F4113 Computer Networks — flk
4114. F4114 Cryptography & Security — perfectly binding
4115. F4115 Curriculum-only — parameter binding
4116. F4116 Distributed Systems & Cloud — language binding
4117. F4117 Mathematics — strict
4118. F4118 Curriculum-only — strict priority
4119. F4119 Mathematics — antichain
4120. F4120 Other/Unknown — tight binding
4121. F4121 Software Engineering — call-by-value flk
4122. F4122 Curriculum-only — expanding opcode
4123. F4123 Software Engineering — operational semantics of flk
4124. F4124 Cryptography & Security — cur pad
4125. F4125 Software Engineering — passing and shared
4126. F4126 Curriculum-only — address type and scope
4127. F4127 Other/Unknown — assumption with scope
4128. F4128 Software Engineering — conditional statement
4129. F4129 Curriculum-only — prove conditional statement
4130. F4130 Software Engineering — inside func
4131. F4131 Computer Architecture — screen buffer
4132. F4132 Mathematics — printout
4133. F4133 Signal/Image/Audio/Video Processing — front view
4134. F4134 Software Engineering — strength reduction
4135. F4135 Distributed Systems & Cloud — aba
4136. F4136 ML & AI — text string
4137. F4137 Mathematics — distinct phrase
4138. F4138 Information Theory & Coding — coding
4139. F4139 Curriculum-only — coding and testing
4140. F4140 Data Mining & Databases — coding errors
4141. F4141 Information Theory & Coding — binary coding
4142. F4142 Information Theory & Coding — lossy joint source-channel coding
4143. F4143 Distributed Systems & Cloud — cluster
4144. F4144 Algorithms & Theory of CS — cluster high
4145. F4145 Curriculum-only — balance between varying cluster size
4146. F4146 Data Mining & Databases — cluster of size
4147. F4147 Distributed Systems & Cloud — cluster and cloud
4148. F4148 ML & AI — coding region
4149. F4149 Mathematics — belonging
4150. F4150 Curriculum-only — area between nominal
4151. F4151 Mathematics — nominal value
4152. F4152 Algorithms & Theory of CS — spectral and flow-based
4153. F4153 Data Mining & Databases — wigner matrix
4154. F4154 Information Theory & Coding — spectral character of noise
4155. F4155 ML & AI — graph laplacian
4156. F4156 NLP & Speech — Image coding
4157. F4157 Operating Systems — format string
4158. F4158 Other/Unknown — multi-spectral
4159. F4159 Signal/Image/Audio/Video Processing — spectral analysis
4160. F4160 Operating Systems — guest
4161. F4161 Signal/Image/Audio/Video Processing — discrete fourier transform
4162. F4162 Curriculum-only — discrete fourier transform xk
4163. F4163 Signal/Image/Audio/Video Processing — circular convolution
4164. F4164 Curriculum-only — circular convolution become pointwise multiplication
4165. F4165 Signal/Image/Audio/Video Processing — goertzel algorithm
4166. F4166 Software Engineering — array of pointer
4167. F4167 Mathematics — monadic
4168. F4168 Software Engineering — openfile
4169. F4169 Algorithms & Theory of CS — anagram substring
4170. F4170 Cryptography & Security — substring of ci
4171. F4171 Mathematics — longest increasing subsequence
4172. F4172 Algorithms & Theory of CS — ford
4173. F4173 Curriculum-only — d-dimensional matching
4174. F4174 Data Mining & Databases — brad
4175. F4175 Mathematics — matched
4176. F4176 Algorithms & Theory of CS — character table
4177. F4177 Algorithms & Theory of CS — linear group
4178. F4178 Computer Architecture — digital audio theory
4179. F4179 Cryptography & Security — contract theory
4180. F4180 Curriculum-only — eulerian and hamiltonian graph
4181. F4181 Data Mining & Databases — discrepancy theory
4182. F4182 Distributed Systems & Cloud — longest common subsequence
4183. F4183 Algorithms & Theory of CS — warshall
4184. F4184 Distributed Systems & Cloud — sequential
4185. F4185 Computer Architecture — combinational
4186. F4186 Distributed Systems & Cloud — theory of timed
4187. F4187 Information Theory & Coding — hadamard code
4188. F4188 ML & AI — artificial intelligence
4189. F4189 Curriculum-only — formal logic of first-order theory
4190. F4190 ML & AI — foundational
4191. F4191 Algorithms & Theory of CS — arithmetic progression
4192. F4192 ML & AI — vc theory
4193. F4193 Mathematics — benefit
4194. F4194 Data Mining & Databases — deviation of mean
4195. F4195 Mathematics — chebyshev
4196. F4196 Curriculum-only — chebyshev with proof
4197. F4197 Mathematics — chebyshev differentiation
4198. F4198 Data Mining & Databases — insurance company
4199. F4199 Mathematics — bet
4200. F4200 Cryptography & Security — financial derivative
4201. F4201 Mathematics — equal probability
4202. F4202 Algorithms & Theory of CS — discrete mathematical structure
4203. F4203 Mathematics — neil
4204. F4204 Algorithms & Theory of CS — igor
4205. F4205 Computer Architecture — igor ginzburg
4206. F4206 Curriculum-only — number theory and algebra
4207. F4207 Mathematics — appendix
4208. F4208 Computer Architecture — code appendix
4209. F4209 Curriculum-only — flagged in appendix
4210. F4210 Mathematics — condition number
4211. F4211 Algorithms & Theory of CS — open addressing
4212. F4212 Computer Architecture — open circuit voltage
4213. F4213 Curriculum-only — open addressing hashing
4214. F4214 Data Mining & Databases — mallat and zeitouni
4215. F4215 Distributed Systems & Cloud — open list
4216. F4216 Mathematics — called open
4217. F4217 Curriculum-only — pig and hbase
4218. F4218 Mathematics — posterior distribution
4219. F4219 Cryptography & Security — rsa
4220. F4220 Curriculum-only — rsa-kem
4221. F4221 Mathematics — distribution of prime
4222. F4222 Curriculum-only — matrix in probability theory
4223. F4223 Mathematics — programming theory
4224. F4224 Curriculum-only — branch resolution in id
4225. F4225 Data Mining & Databases — high resolution image
4226. F4226 ML & AI — conflict resolution
4227. F4227 Mathematics — ross
4228. F4228 ML & AI — conditional independence
4229. F4229 Mathematics — independent random variable
4230. F4230 Distributed Systems & Cloud — abelian semigroup
4231. F4231 Mathematics — commutative
4232. F4232 Algorithms & Theory of CS — non commutative khintchine
4233. F4233 Data Mining & Databases — non-commutative khintchine improvement
4234. F4234 Mathematics — commutative law
4235. F4235 Algorithms & Theory of CS — single node
4236. F4236 Computer Architecture — single set
4237. F4237 Computer Networks — single attribute
4238. F4238 Curriculum-only — kerberos-style single sign-on
4239. F4239 Distributed Systems & Cloud — multiple process
4240. F4240 Mathematics — deeply
4241. F4241 Data Mining & Databases — empirical rule
4242. F4242 Mathematics — confidence interval
4243. F4243 Algorithms & Theory of CS — joint confidence interval
4244. F4244 Curriculum-only — confidence interval by formula
4245. F4245 Mathematics — computing confidence interval
4246. F4246 Curriculum-only — arbitrary-precision integer
4247. F4247 Distributed Systems & Cloud — double precision
4248. F4248 Mathematics — plan
4249. F4249 Algorithms & Theory of CS — Plan graphs and GraphPlan
4250. F4250 Curriculum-only — dryad plan
4251. F4251 Data Mining & Databases — cpu cost
4252. F4252 ML & AI — space of plan
4253. F4253 Mathematics — estimate
4254. F4254 Algorithms & Theory of CS — estimate ca
4255. F4255 Curriculum-only — early estimate are wide
4256. F4256 Data Mining & Databases — cient estimate
4257. F4257 Information Theory & Coding — channel estimator
4258. F4258 Curriculum-only — log-likelihood that never decrease
4259. F4259 ML & AI — map estimate
4260. F4260 Mathematics — error estimate
4261. F4261 Information Theory & Coding — radio
4262. F4262 Curriculum-only — memory and radio
4263. F4263 Data Mining & Databases — radio play
4264. F4264 Distributed Systems & Cloud — send and receive
4265. F4265 Information Theory & Coding — ghz frequencies
4266. F4266 Mathematics — letter
4267. F4267 Curriculum-only — digit and letter
4268. F4268 Data Mining & Databases — wrapping
4269. F4269 Mathematics — bookkeeper
4270. F4270 Algorithms & Theory of CS — hall theorem
4271. F4271 Curriculum-only — nig theorem and hall theorem
4272. F4272 Mathematics — observed
4273. F4273 Curriculum-only — compare desired and observed
4274. F4274 Mathematics — perfect square
4275. F4275 Curriculum-only — sigma named
4276. F4276 Mathematics — single precision
4277. F4277 Curriculum-only — confidence interval and hypothesis testing
4278. F4278 Mathematics — stochastic
4279. F4279 Cryptography & Security — stochastic financial network
4280. F4280 Curriculum-only — stochastic gd
4281. F4281 ML & AI — training with stochastic gradient
4282. F4282 Mathematics — cross correlation
4283. F4283 Curriculum-only — tautology and contradiction
4284. F4284 Mathematics — theorem of arithmetic
4285. F4285 Cryptography & Security — integer factorization
4286. F4286 Curriculum-only — chain-rule factorization
4287. F4287 Mathematics — ladder
4288. F4288 Curriculum-only — marginal and conditional distribution
4289. F4289 ML & AI — y0t
4290. F4290 Mathematics — dxi
4291. F4291 Computer Networks — car rental
4292. F4292 Curriculum-only — car and bus
4293. F4293 Data Mining & Databases — lst
4294. F4294 Distributed Systems & Cloud — proc
4295. F4295 Computer Networks — proc acm sigcomm
4296. F4296 Data Mining & Databases — france
4297. F4297 Mathematics — bike
4298. F4298 Cryptography & Security — administrator
4299. F4299 Mathematics — plausible
4300. F4300 Curriculum-only — uv and why it is plausible
4301. F4301 Mathematics — type ii
4302. F4302 Computer Architecture — shifter
4303. F4303 Mathematics — vertex degree
4304. F4304 Algorithms & Theory of CS — crossing number inequality
4305. F4305 Mathematics — big-o
4306. F4306 Curriculum-only — big-o form
4307. F4307 Mathematics — least-upper-bound
4308. F4308 Curriculum-only — taylor theorem with remainder in little-o
4309. F4309 Mathematics — previous theorem
4310. F4310 NLP & Speech — lms
4311. F4311 Curriculum-only — rnn lms
4312. F4312 Mathematics — linear lms
4313. F4313 Operating Systems — radio systems
4314. F4314 Other/Unknown — Color theory
4315. F4315 Other/Unknown — parametric oscillators
4316. F4316 Curriculum-only — conformal mapping to potential theory
4317. F4317 Other/Unknown — punctuated
4318. F4318 Algorithms & Theory of CS — robot navigation
4319. F4319 Curriculum-only — robot joint
4320. F4320 Mathematics — elbow
4321. F4321 Other/Unknown — multi-robot systems
4322. F4322 Other/Unknown — system theory
4323. F4323 Signal/Image/Audio/Video Processing — azt
4324. F4324 Mathematics — kf kl1
4325. F4325 Signal/Image/Audio/Video Processing — low resolution
4326. F4326 ML & AI — low resolution image
4327. F4327 Signal/Image/Audio/Video Processing — matched filtering
4328. F4328 Mathematics — heart
4329. F4329 Data Mining & Databases — cardiac
4330. F4330 Distributed Systems & Cloud — roger rigg
4331. F4331 ML & AI — courtesy
4332. F4332 Computer Networks — courtesy of elsevier
4333. F4333 Distributed Systems & Cloud — acknowledgement
4334. F4334 Curriculum-only — delayed acknowledgement
4335. F4335 ML & AI — courtesy of gabriel
4336. F4336 Mathematics — doi
4337. F4337 Distributed Systems & Cloud — dissertation
4338. F4338 Mathematics — business
4339. F4339 Computer Networks — business continuity
4340. F4340 Curriculum-only — business insight from operation
4341. F4341 ML & AI — ai business
4342. F4342 Mathematics — business decisions
4343. F4343 Data Mining & Databases — hospital run smoothly
4344. F4344 Mathematics — jack
4345. F4345 Distributed Systems & Cloud — jack dongarra
4346. F4346 Data Mining & Databases — milne
4347. F4347 Mathematics — dover
4348. F4348 Curriculum-only — fermat little theorem
4349. F4349 Mathematics — carmichael number
4350. F4350 Curriculum-only — fermat test and carmichael number
4351. F4351 Mathematics — fermat witness
4352. F4352 Operating Systems — business relationship
4353. F4353 Other/Unknown — asia
4354. F4354 Curriculum-only — compliance in the current business environment
4355. F4355 Other/Unknown — enterprise
4356. F4356 Computer Networks — enterprise resources
4357. F4357 Curriculum-only — enterprise devop
4358. F4358 Distributed Systems & Cloud — saas
4359. F4359 Other/Unknown — business model
4360. F4360 Distributed Systems & Cloud — pay-as-you-go business model
4361. F4361 Other/Unknown — enterprise system
4362. F4362 Algorithms & Theory of CS — gsat
4363. F4363 Other/Unknown — linear algebraic
4364. F4364 Data Mining & Databases — database marketing
4365. F4365 Other/Unknown — emerging
4366. F4366 Curriculum-only — ml accelerator with emerging
4367. F4367 Other/Unknown — current and emerging
4368. F4368 Mathematics — influence
4369. F4369 Curriculum-only — cognitive-science influence
4370. F4370 ML & AI — influence diagrams
4371. F4371 Other/Unknown — film
4372. F4372 Mathematics — condensation
4373. F4373 Algorithms & Theory of CS — external memory
4374. F4374 Computer Architecture — voltage transfer
4375. F4375 Curriculum-only — cost in page transfer
4376. F4376 Distributed Systems & Cloud — asynchronous transfer
4377. F4377 Curriculum-only — representational state transfer
4378. F4378 Information Theory & Coding — data transfer
4379. F4379 Curriculum-only — data transfer cost
4380. F4380 Mathematics — integration with weight function
4381. F4381 Other/Unknown — mass transfer
4382. F4382 Mathematics — pearson correlation
4383. F4383 Other/Unknown — education
4384. F4384 Data Mining & Databases — nutritional education with data
4385. F4385 Mathematics — high school
4386. F4386 Distributed Systems & Cloud — foundation
4387. F4387 Curriculum-only — foundation for eda
4388. F4388 Data Mining & Databases — Foundations of mathematics
4389. F4389 Other/Unknown — consolidation
4390. F4390 Computer Networks — aimd
4391. F4391 Curriculum-only — quic transport
4392. F4392 Mathematics — reactor
4393. F4393 Data Mining & Databases — novel
4394. F4394 Other/Unknown — equation of state
4395. F4395 Signal/Image/Audio/Video Processing — courtesy of stanley hong
4396. F4396 Software Engineering — adam hartz
4397. F4397 Mathematics — partition
4398. F4398 Algorithms & Theory of CS — integer partition
4399. F4399 Curriculum-only — partition table
4400. F4400 ML & AI — distribution on partition
4401. F4401 Mathematics — choice of partition
4402. F4402 Software Engineering — demo courtesy
4403. F4403 Mathematics — volt
4404. F4404 Computer Architecture — noise margin
4405. F4405 Software Engineering — kitchen
4406. F4406 Mathematics — global
4407. F4407 Curriculum-only — global qualifier
4408. F4408 Data Mining & Databases — global health
4409. F4409 Mathematics — global error
4410. F4410 Other/Unknown — rainfall
4411. F4411 Signal/Image/Audio/Video Processing — global edition
4412. F4412 Software Engineering — global mean
4413. F4413 Mathematics — greatest common divisor
4414. F4414 Algorithms & Theory of CS — halting
4415. F4415 Mathematics — divisibility
4416. F4416 Algorithms & Theory of CS — diophantine
4417. F4417 Mathematics — arithmetical
4418. F4418 Data Mining & Databases — arithmetical sentence
4419. F4419 Mathematics — euclidean algorithm
4420. F4420 Curriculum-only — solving linear congruence
4421. F4421 Mathematics — mod pj
4422. F4422 Curriculum-only — factor and remainder theorem
4423. F4423 Mathematics — chinese remainder
4424. F4424 Data Mining & Databases — quadratic residue
4425. F4425 Mathematics — index calculus
4426. F4426 Curriculum-only — bilinear and quadratic form
4427. F4427 Mathematics — binary quadratic form
4428. F4428 Curriculum-only — custom metric
4429. F4429 Mathematics — compact subset
4430. F4430 Mathematics — square mod
4431. F4431 Other/Unknown — arithmetical function
4432. F4432 Signal/Image/Audio/Video Processing — isoperimetric
4433. F4433 Software Engineering — lit
4434. F4434 Algorithms & Theory of CS — causal link
4435. F4435 Mathematics — drill
4436. F4436 Software Engineering — recon-test
4437. F4437 Curriculum-only — dns redirection
4438. F4438 Software Engineering — resolution theorem
4439. F4439 Algorithms & Theory of CS — satisfiability
4440. F4440 Mathematics — sum of product
4441. F4441 Computer Architecture — minimal sum-of-product
4442. F4442 Curriculum-only — sum-of-product and product-of-sum form
4443. F4443 Software Engineering — satisfiability modulo theories
4444. F4444 Distributed Systems & Cloud — computer system engineering
4445. F4445 Software Engineering — temporary
4446. F4446 Curriculum-only — temporary data
4447. F4447 Software Engineering — temporary memory
4448. F4448 Algorithms & Theory of CS — one-time pad
4449. F4449 Cryptography & Security — cryptographic
4450. F4450 Algorithms & Theory of CS — substitution cipher
4451. F4451 Cryptography & Security — cipher based on linear
4452. F4452 Computer Networks — encryption standard
4453. F4453 Cryptography & Security — ddh
4454. F4454 Curriculum-only — autokey cipher
4455. F4455 Mathematics — block
4456. F4456 Algorithms & Theory of CS — block boundaries
4457. F4457 Computer Architecture — block to set
4458. F4458 Cryptography & Security — block encryption
4459. F4459 Curriculum-only — block device
4460. F4460 Data Mining & Databases — innodb
4461. F4461 Distributed Systems & Cloud — block executed
4462. F4462 ML & AI — step-by-step
4463. F4463 Mathematics — block matrix
4464. F4464 Operating Systems — block number
4465. F4465 Other/Unknown — block of text
4466. F4466 Curriculum-only — attribute-based and functional encryption
4467. F4467 Software Engineering — block and compound
4468. F4468 Signal/Image/Audio/Video Processing — block diagram
4469. F4469 Mathematics — fibonacci sequence
4470. F4470 Signal/Image/Audio/Video Processing — diagram and operator
4471. F4471 Software Engineering — totality
4472. F4472 Information Theory & Coding — unspeci ed value
4473. F4473 Software Engineering — val
4474. F4474 Algorithms & Theory of CS — set avl tree
4475. F4475 Operating Systems — old val
4476. F4476 Software Engineering — idx
4477. F4477 System Design Primer / Availability patterns — fail-over
4478. F4478 Curriculum-only — elastic ip help fail-over
4479. F4479 System Design Primer / Cache — cache
4480. F4480 Computer Architecture — average access time
4481. F4481 Cryptography & Security — cache poisoning
4482. F4482 Curriculum-only — add to the cache
4483. F4483 Curriculum-only — constant cache
4484. F4484 Distributed Systems & Cloud — cache complexity
4485. F4485 Computer Architecture — cache hit ratio
4486. F4486 Curriculum-only — zipf popularity and cache hit ratio
4487. F4487 Distributed Systems & Cloud — first-level cache
4488. F4488 Curriculum-only — two-level fredman koml
4489. F4489 Mathematics — cache and backsubstitution
4490. F4490 Distributed Systems & Cloud — dirty
4491. F4491 Curriculum-only — dirty page table
4492. F4492 Distributed Systems & Cloud — flush
4493. F4493 Mathematics — poisson
4494. F4494 Computer Networks — cpe
4495. F4495 Cryptography & Security — customer data
4496. F4496 Curriculum-only — customer churn
4497. F4497 Mathematics — customer demands
4498. F4498 Information Theory & Coding — entropy
4499. F4499 Algorithms & Theory of CS — bern
4500. F4500 Curriculum-only — anti-entropy
4501. F4501 Information Theory & Coding — entropy function
4502. F4502 Algorithms & Theory of CS — nite number of state
4503. F4503 Curriculum-only — discrete number of state
4504. F4504 Mathematics — binary number
4505. F4505 Mathematics — limiting distribution
4506. F4506 Curriculum-only — mean time between page change
4507. F4507 Mathematics — expected number
4508. F4508 Mathematics — integer value
4509. F4509 Information Theory & Coding — bernoulli factory
4510. F4510 Mathematics — central limit theorem
4511. F4511 Curriculum-only — central limit theorem at work
4512. F4512 Mathematics — de moivre
4513. F4513 Curriculum-only — de moivre theorem
4514. F4514 Mathematics — discrete distribution
4515. F4515 Distributed Systems & Cloud — election
4516. F4516 Curriculum-only — election under failure
4517. F4517 Data Mining & Databases — election forecasting
4518. F4518 Distributed Systems & Cloud — gossip
4519. F4519 Curriculum-only — failure detection by gossip
4520. F4520 Distributed Systems & Cloud — epidemic and gossip
4521. F4521 Mathematics — probability of success
4522. F4522 ML & AI — beta
4523. F4523 Algorithms & Theory of CS — mario
4524. F4524 Computer Architecture — beta implementation
4525. F4525 Curriculum-only — beta family
4526. F4526 Data Mining & Databases — beta coefficient
4527. F4527 ML & AI — beta function
4528. F4528 Mathematics — process of rate
4529. F4529 Data Mining & Databases — electoral vote
4530. F4530 Mathematics — plan to vote
4531. F4531 Operating Systems — alewife
4532. F4532 Curriculum-only — kept in the memory cache
4533. F4533 Other/Unknown — bernoulli equation
4534. F4534 Algorithms & Theory of CS — planar
4535. F4535 Mathematics — closed walk
4536. F4536 Algorithms & Theory of CS — digraph
4537. F4537 Mathematics — digraph and dag
4538. F4538 Other/Unknown — activity digraph
4539. F4539 Signal/Image/Audio/Video Processing — bernoulli sequence
4540. F4540 Software Engineering — alu
4541. F4541 Distributed Systems & Cloud — pipelined
4542. F4542 Computer Architecture — combinational circuit
4543. F4543 Curriculum-only — pipelined sram
4544. F4544 Operating Systems — pipelined datapath
4545. F4545 Other/Unknown — gate
4546. F4546 HS ComputerScience Class XI / Unit 1: Computer Systems and Organisation — boolean logic
4547. F4547 Computer Architecture — cmo gate
4548. F4548 Curriculum-only — rule recombined with boolean logic
4549. F4549 Distributed Systems & Cloud — gate stacks
4550. F4550 Information Theory & Coding — possible input
4551. F4551 Mathematics — exclusive and collectively
4552. F4552 Computer Architecture — music history
4553. F4553 Cryptography & Security — history of money
4554. F4554 Curriculum-only — history of ai
4555. F4555 Data Mining & Databases — version history
4556. F4556 Distributed Systems & Cloud — access history
4557. F4557 Mathematics — introductory
4558. F4558 Distributed Systems & Cloud — timing
4559. F4559 Algorithms & Theory of CS — timing attacks
4560. F4560 Computer Architecture — register timing
4561. F4561 ML & AI — rex
4562. F4562 Mathematics — tournament history
4563. F4563 Operating Systems — history variable
4564. F4564 Other/Unknown — culture
4565. F4565 Curriculum-only — devop culture
4566. F4566 Other/Unknown — cell culture
4567. F4567 Mathematics — propositional formulas
4568. F4568 Other/Unknown — logic circuit
4569. F4569 Curriculum-only — type of mathematical model
4570. F4570 Other/Unknown — mos capacitor
4571. F4571 Signal/Image/Audio/Video Processing — time delay
4572. F4572 Data Mining & Databases — computer program
4573. F4573 Distributed Systems & Cloud — philosopher
4574. F4574 Software Engineering — beta assigned
4575. F4575 ML & AI — helper matrix
4576. F4576 Software Engineering — in-memory data
4577. F4577 Curriculum-only — predictor with global and local history
4578. F4578 Software Engineering — programmable gate array
4579. F4579 Algorithms & Theory of CS — recursive algorithm
4580. F4580 Curriculum-only — recursive flow classification
4581. F4581 Distributed Systems & Cloud — jacobi
4582. F4582 Curriculum-only — jacobi and gauss seidel
4583. F4583 Mathematics — compu
4584. F4584 Data Mining & Databases — compu tational
4585. F4585 Mathematics — cyclotomic polynomial
4586. F4586 Curriculum-only — language of recurrence
4587. F4587 Mathematics — linear recurrence
4588. F4588 Curriculum-only — enterprise matrix in the author
4589. F4589 Mathematics — rabbit
4590. F4590 Signal/Image/Audio/Video Processing — recursive filters
4591. F4591 Software Engineering — child
4592. F4592 Algorithms & Theory of CS — min heap
4593. F4593 Curriculum-only — failure handling by successor list
4594. F4594 Data Mining & Databases — child book
4595. F4595 Distributed Systems & Cloud — ruud van
4596. F4596 Mathematics — randomization
4597. F4597 Algorithms & Theory of CS — divide conquer
4598. F4598 Curriculum-only — randomisation half of the source
4599. F4599 Other/Unknown — van der
4600. F4600 Algorithms & Theory of CS — combinatorics
4601. F4601 Curriculum-only — generating function and combinatorics
4602. F4602 Distributed Systems & Cloud — lynch
4603. F4603 Mathematics — additive
4604. F4604 Algorithms & Theory of CS — lower bound in schur
4605. F4605 Curriculum-only — additive for addition
4606. F4606 ML & AI — additive form
4607. F4607 Curriculum-only — multiplicative and additive form
4608. F4608 Mathematics — additive function
4609. F4609 Algorithms & Theory of CS — enumerative combinatorics
4610. F4610 Mathematics — paterson
4611. F4611 Other/Unknown — van der waal
4612. F4612 Software Engineering — fib
4613. F4613 Curriculum-only — fib and content store
4614. F4614 Software Engineering — fib ii
4615. F4615 Algorithms & Theory of CS — worst
4616. F4616 Curriculum-only — worst case lg
4617. F4617 Distributed Systems & Cloud — ame
4618. F4618 Software Engineering — inner loop
4619. F4619 Mathematics — switch
4620. F4620 Curriculum-only — atomic switch at commit
4621. F4621 Distributed Systems & Cloud — bene network
4622. F4622 Information Theory & Coding — input queued switch
4623. F4623 Operating Systems — coding switch
4624. F4624 Signal/Image/Audio/Video Processing — butterfly computation
4625. F4625 Software Engineering — rabbit instance
4626. F4626 Distributed Systems & Cloud — matrix mul
4627. F4627 Software Engineering — rbp
4628. F4628 Mathematics — leave
4629. F4629 Software Engineering — callee-saved
4630. F4630 Curriculum-only — caller and callee-saved register
4631. F4631 Software Engineering — rbx
4632. F4632 Mathematics — sub
4633. F4633 Algorithms & Theory of CS — sub-gaussian
4634. F4634 Curriculum-only — published outline give no sub-list
4635. F4635 Data Mining & Databases — frequent sub-sequence
4636. F4636 Information Theory & Coding — sub eld
4637. F4637 Software Engineering — rcx
4638. F4638 Curriculum-only — calling and orchestration
4639. F4639 Software Engineering — recursive descent parser
4640. F4640 Algorithms & Theory of CS — mast
4641. F4641 Curriculum-only — script kiddy
4642. F4642 Distributed Systems & Cloud — jquery
4643. F4643 Curriculum-only — grid of block of thread
4644. F4644 Distributed Systems & Cloud — lock
4645. F4645 Curriculum-only — lock compatibility matrix
4646. F4646 Data Mining & Databases — lock manager
4647. F4647 Distributed Systems & Cloud — add lock
4648. F4648 Curriculum-only — deadlock handling
4649. F4649 Data Mining & Databases — global deadlock
4650. F4650 Distributed Systems & Cloud — lock acquired
4651. F4651 Curriculum-only — test race
4652. F4652 Distributed Systems & Cloud — set lock
4653. F4653 ML & AI — script load p1
4654. F4654 Mathematics — considered
4655. F4655 Data Mining & Databases — smarter
4656. F4656 Algorithms & Theory of CS — smarter interval scheduling
4657. F4657 Distributed Systems & Cloud — smarter planet
4658. F4658 Mathematics — race time
4659. F4659 Information Theory & Coding — amount of information
4660. F4660 Curriculum-only — joint and conditional entropy
4661. F4661 Distributed Systems & Cloud — mutual
4662. F4662 Information Theory & Coding — mutual information
4663. F4663 Mathematics — binary channel
4664. F4664 NLP & Speech — startup script
4665. F4665 Operating Systems — lock and condition
4666. F4666 Other/Unknown — gender
4667. F4667 Mathematics — discrimination
4668. F4668 Computer Architecture — demonstration audio
4669. F4669 Information Theory & Coding — equalizer
4670. F4670 Mathematics — location
4671. F4671 Algorithms & Theory of CS — candidate location
4672. F4672 Computer Architecture — read location
4673. F4673 Computer Networks — location data
4674. F4674 Curriculum-only — location address
4675. F4675 Data Mining & Databases — location based
4676. F4676 Distributed Systems & Cloud — facility
4677. F4677 Algorithms & Theory of CS — open facility
4678. F4678 Distributed Systems & Cloud — location services
4679. F4679 Information Theory & Coding — hamming
4680. F4680 Curriculum-only — crc and hamming code
4681. F4681 Information Theory & Coding — repeater
4682. F4682 Mathematics — distant
4683. F4683 Algorithms & Theory of CS — mutual friend
4684. F4684 Computer Networks — close friend
4685. F4685 Cryptography & Security — friend finder
4686. F4686 Curriculum-only — friend each so billion friend relationship
4687. F4687 Mathematics — invite
4688. F4688 Other/Unknown — hamming bound
4689. F4689 Signal/Image/Audio/Video Processing — filter design
4690. F4690 Mathematics — symmetric lowpass filter design
4691. F4691 Signal/Image/Audio/Video Processing — butterworth
4692. F4692 Software Engineering — add friend
4693. F4693 Curriculum-only — flush to immutable sstable
4694. F4694 Software Engineering — immutable value
4695. F4695 Curriculum-only — byte snippet
4696. F4696 Software Engineering — javascript snippet
4697. F4697 Algorithms & Theory of CS — design and analysis
4698. F4698 Distributed Systems & Cloud — report submitted
4699. F4699 Computer Architecture — clocked
4700. F4700 Curriculum-only — clocked timing
4701. F4701 Distributed Systems & Cloud — synchronous
4702. F4702 Algorithms & Theory of CS — synchronous ring
4703. F4703 Mathematics — binary relation
4704. F4704 Information Theory & Coding — boolean algebra
4705. F4705 Curriculum-only — boolean algebra and gate-level logic
4706. F4706 Mathematics — injective
4707. F4707 Data Mining & Databases — fast exponentiation
4708. F4708 Curriculum-only — inverse and fast exponentiation
4709. F4709 Mathematics — nonnegative integer
4710. F4710 Data Mining & Databases — manhattan
4711. F4711 Mathematics — ll call
4712. F4712 Algorithms & Theory of CS — minimum element
4713. F4713 Mathematics — odd integer
4714. F4714 Algorithms & Theory of CS — floyd
4715. F4715 Curriculum-only — floyd tortoise-and-hare cycle detection
4716. F4716 Mathematics — partially
4717. F4717 Algorithms & Theory of CS — pomdp
4718. F4718 Curriculum-only — partially committed
4719. F4719 Mathematics — collection of set
4720. F4720 Curriculum-only — partial order and the dsim simulator
4721. F4721 Distributed Systems & Cloud — total order
4722. F4722 Curriculum-only — total order and linear extension
4723. F4723 Mathematics — sock
4724. F4724 Algorithms & Theory of CS — pigeonhole principle
4725. F4725 Curriculum-only — division and pigeonhole principle
4726. F4726 Mathematics — state machine terminate
4727. F4727 Other/Unknown — sequential logic
4728. F4728 Computer Architecture — digital abstraction
4729. F4729 Curriculum-only — karnaugh-map minimisation
4730. F4730 ML & AI — image courtesy
4731. F4731 Computer Architecture — analog device
4732. F4732 Cryptography & Security — cc by-nc
4733. F4733 ML & AI — cc-by-nc-sa
4734. F4734 Mathematics — ripple
4735. F4735 NLP & Speech — lookahead
4736. F4736 Other/Unknown — chip
4737. F4737 Computer Architecture — data bus
4738. F4738 Curriculum-only — common data bus
4739. F4739 Distributed Systems & Cloud — on-chip cache
4740. F4740 Information Theory & Coding — clock frequency
4741. F4741 Mathematics — continued
4742. F4742 Curriculum-only — continued lecture on newton
4743. F4743 Mathematics — continued fraction
4744. F4744 Cryptography & Security — rim esk
4745. F4745 Mathematics — memory chip
4746. F4746 Curriculum-only — memory chip and their organisation
4747. F4747 Mathematics — periodic continued fraction
4748. F4748 Curriculum-only — carry lookahead with generate gi
4749. F4749 Mathematics — generate sn
4750. F4750 Operating Systems — chip multiprocessing
4751. F4751 Curriculum-only — dram organisation
4752. F4752 Distributed Systems & Cloud — cpu
4753. F4753 Curriculum-only — cpu load
4754. F4754 Distributed Systems & Cloud — cpu to execute read
4755. F4755 Operating Systems — bounded buffer
4756. F4756 Other/Unknown — torque ripples
4757. F4757 Software Engineering — alternation
4758. F4758 Software Engineering — taxonomy
4759. F4759 Computer Architecture — flynn taxonomy
4760. F4760 Curriculum-only — foundation and taxonomy
4761. F4761 Software Engineering — thread group
4762. F4762 Algorithms & Theory of CS — gorge
4763. F4763 Curriculum-only — eulerian trail
4764. F4764 Mathematics — surjective
4765. F4765 Algorithms & Theory of CS — topological order
4766. F4766 Curriculum-only — acyclic graph and topological order
4767. F4767 Mathematics — recursive data type
4768. F4768 Curriculum-only — birth death chain
4769. F4769 Mathematics — baby
4770. F4770 Curriculum-only — compare product and to explain
4771. F4771 Mathematics — ferry
4772. F4772 Algorithms & Theory of CS — smallest number
4773. F4773 Mathematics — sequence of number
4774. F4774 Data Mining & Databases — calculable total function
4775. F4775 Mathematics — year ago
4776. F4776 Other/Unknown — diagonalization
4777. F4777 Algorithms & Theory of CS — block diagonalization
4778. F4778 Curriculum-only — characteristic value and diagonalization
4779. F4779 Other/Unknown — diagonalization of matrix
4780. F4780 Software Engineering — constructor
4781. F4781 Curriculum-only — instead of multiple constructor
4782. F4782 Mathematics — structural induction
4783. F4783 Algorithms & Theory of CS — read-once branching program
4784. F4784 Mathematics — definition of conditional probability
4785. F4785 Algorithms & Theory of CS — merged
4786. F4786 Mathematics — bernoulli process with parameter
4787. F4787 Distributed Systems & Cloud — sorting
4788. F4788 Algorithms & Theory of CS — linear sorting
4789. F4789 Distributed Systems & Cloud — linear arrays
4790. F4790 Curriculum-only — service mesh
4791. F4791 Data Mining & Databases — mesh theorem
4792. F4792 Distributed Systems & Cloud — hypercube
4793. F4793 Curriculum-only — hypercube and gray code
4794. F4794 Distributed Systems & Cloud — hypercube networks-iii
4795. F4795 Computer Architecture — number of memory access
4796. F4796 Distributed Systems & Cloud — sorting and permuting
4797. F4797 Mathematics — cost of sorting
4798. F4798 Curriculum-only — disk and the cost of sorting
4799. F4799 Mathematics — number of customer
4800. F4800 Information Theory & Coding — average amount of time
4801. F4801 Mathematics — combining
4802. F4802 Algorithms & Theory of CS — combining spectral
4803. F4803 Mathematics — reject
4804. F4804 Algorithms & Theory of CS — nondeterministically pick
4805. F4805 Curriculum-only — reject rate
4806. F4806 Mathematics — reject h0
4807. F4807 Curriculum-only — recursive binary splitting
4808. F4808 Mathematics — splitting of poisson
4809. F4809 Data Mining & Databases — continuum hypothesis
4810. F4810 Mathematics — elasticity
4811. F4811 Curriculum-only — rapid elasticity
4812. F4812 Mathematics — isotropic
4813. F4813 Curriculum-only — non-linear plant are linearised
4814. F4814 Other/Unknown — continuum structures
4815. F4815 Software Engineering — code for sorting
4816. F4816 Mathematics — closure
4817. F4817 Curriculum-only — attribute closure
4818. F4818 ML & AI — downward-closure
4819. F4819 Mathematics — integral closure
4820. F4820 Software Engineering — closure block
4821. F4821 Algorithms & Theory of CS — deterministic finite automaton
4822. F4822 Algorithms & Theory of CS — accept everything
4823. F4823 Curriculum-only — regular expression and git
4824. F4824 Data Mining & Databases — accepting
4825. F4825 Curriculum-only — stop accepting
4826. F4826 NLP & Speech — context-free grammar
4827. F4827 Algorithms & Theory of CS — pda
4828. F4828 Distributed Systems & Cloud — pspace
4829. F4829 Algorithms & Theory of CS — dfa pspace
4830. F4830 Data Mining & Databases — geography
4831. F4831 Algorithms & Theory of CS — generalized geography
4832. F4832 Distributed Systems & Cloud — hierarchy
4833. F4833 Algorithms & Theory of CS — hierarchy theorem
4834. F4834 Curriculum-only — hierarchy of bus
4835. F4835 Distributed Systems & Cloud — bigtable
4836. F4836 Curriculum-only — bigtable tablet location
4837. F4837 Distributed Systems & Cloud — memory hierarchy
4838. F4838 Curriculum-only — host and the device
4839. F4839 Distributed Systems & Cloud — io virtualization
4840. F4840 Algorithms & Theory of CS — hypergraph container
4841. F4841 Curriculum-only — container and access its element
4842. F4842 Distributed Systems & Cloud — container runtime
4843. F4843 Curriculum-only — container runtime is available
4844. F4844 Distributed Systems & Cloud — linux container
4845. F4845 NLP & Speech — chomsky hierarchy
4846. F4846 Mathematics — markov
4847. F4847 Curriculum-only — inequality of markov
4848. F4848 Information Theory & Coding — markov source
4849. F4849 ML & AI — markov with respect
4850. F4850 Mathematics — classification of state
4851. F4851 Algorithms & Theory of CS — reducible
4852. F4852 Mathematics — irreducible and recurrence
4853. F4853 Information Theory & Coding — codeword
4854. F4854 Computer Architecture — local decoding of walsh
4855. F4855 Curriculum-only — llm decoding
4856. F4856 Information Theory & Coding — binary erasure channel
4857. F4857 Information Theory & Coding — list decoding
4858. F4858 ML & AI — underlying probability
4859. F4859 Mathematics — codebook
4860. F4860 Information Theory & Coding — error probability
4861. F4861 Computer Networks — radio signals
4862. F4862 Curriculum-only — fft at the receiver
4863. F4863 Information Theory & Coding — narrow band
4864. F4864 Mathematics — associated error probability
4865. F4865 Information Theory & Coding — gaussian and stationary
4866. F4866 Mathematics — irreducible with stationary
4867. F4867 Curriculum-only — inverse fft at the transmitter
4868. F4868 Mathematics — uniqueness of stationary
4869. F4869 Operating Systems — direct memory access
4870. F4870 Other/Unknown — analytical hierarchy process
4871. F4871 Mathematics — infinitesimal
4872. F4872 Other/Unknown — embedded
4873. F4873 Computer Architecture — embedded memories
4874. F4874 Computer Networks — embedded images
4875. F4875 Curriculum-only — embedded sql
4876. F4876 Operating Systems — embedded device
4877. F4877 Other/Unknown — embedded computing
4878. F4878 Information Theory & Coding — isi
4879. F4879 Mathematics — eye
4880. F4880 Curriculum-only — google keep an eye
4881. F4881 Data Mining & Databases — eye on healthcare cost
4882. F4882 Information Theory & Coding — eye diagram
4883. F4883 Mathematics — inv
4884. F4884 Signal/Image/Audio/Video Processing — dithering
4885. F4885 Mathematics — measuring
4886. F4886 Computer Architecture — oscilloscope
4887. F4887 Mathematics — horizontal
4888. F4888 Algorithms & Theory of CS — shutter
4889. F4889 Computer Architecture — horizontal space
4890. F4890 Mathematics — horizontal and vertical
4891. F4891 Curriculum-only — constrained least square
4892. F4892 Mathematics — horizontal vector
4893. F4893 Curriculum-only — continued lecture on newton and quasi-newton
4894. F4894 Distributed Systems & Cloud — barrier
4895. F4895 Curriculum-only — barrier across block inside
4896. F4896 Mathematics — short-step barrier
4897. F4897 Software Engineering — cout
4898. F4898 Curriculum-only — exit criterion
4899. F4899 Distributed Systems & Cloud — stdout
4900. F4900 Operating Systems — sys exit
4901. F4901 Software Engineering — dynamically allocated
4902. F4902 Curriculum-only — favor composition over inheritance
4903. F4903 Software Engineering — linearly constrained
4904. F4904 Computer Networks — transport header
4905. F4905 Curriculum-only — extension header
4906. F4906 Operating Systems — program header
4907. F4907 Software Engineering — offset
4908. F4908 Mathematics — offset frequencies
4909. F4909 Software Engineering — assembler
4910. F4910 Operating Systems — pc-relative
4911. F4911 Software Engineering — parent process
4912. F4912 Curriculum-only — searching for people online
4913. F4913 Software Engineering — linear search
4914. F4914 Mathematics — hour of sleep
4915. F4915 Software Engineering — Sorting and searching
4916. F4916 Curriculum-only — subclass and inheritance
4917. F4917 Software Engineering — uop
4918. F4918 Algorithms & Theory of CS — signup
4919. F4919 Computer Architecture — ddr
4920. F4920 Computer Networks — user access
4921. F4921 Cryptography & Security — attacker
4922. F4922 Computer Networks — s-box
4923. F4923 Cryptography & Security — cryptographically secure
4924. F4924 Algorithms & Theory of CS — pseudorandom
4925. F4925 Cryptography & Security — secure computer system
4926. F4926 Curriculum-only — aes-based hashing
4927. F4927 Curriculum-only — knowing your attacker
4928. F4928 Curriculum-only — user and product database
4929. F4929 Data Mining & Databases — database user
4930. F4930 Curriculum-only — user rating prediction
4931. F4931 Data Mining & Databases — window user
4932. F4932 Distributed Systems & Cloud — allow user
4933. F4933 Computer Networks — delegate
4934. F4934 Curriculum-only — cdn fetch on the first request
4935. F4935 Distributed Systems & Cloud — secure boot
4936. F4936 Mathematics — compromise
4937. F4937 Cryptography & Security — adversary
4938. F4938 Mathematics — generator
4939. F4939 Algorithms & Theory of CS — pseudorandom generator
4940. F4940 Computer Architecture — function generator
4941. F4941 Cryptography & Security — generator of zp
4942. F4942 Curriculum-only — generator differ
4943. F4943 Information Theory & Coding — generator string
4944. F4944 Mathematics — malicious adversary
4945. F4945 Data Mining & Databases — pip install
4946. F4946 Mathematics — tor
4947. F4947 NLP & Speech — singing
4948. F4948 Operating Systems — malicious codes
4949. F4949 Other/Unknown — dc generators
4950. F4950 Cryptography & Security — xss
4951. F4951 Curriculum-only — indirect injection
4952. F4952 Other/Unknown — injection molding
4953. F4953 Cryptography & Security — authentication
4954. F4954 Curriculum-only — api authentication by oauth
4955. F4955 Mathematics — remote authentication
4956. F4956 Other/Unknown — key distribution
4957. F4957 Curriculum-only — symmetric key distribution
4958. F4958 Other/Unknown — user interface
4959. F4959 Mathematics — graphical
4960. F4960 Curriculum-only — graphical solution by cobweb diagram
4961. F4961 Mathematics — graphical and numerical
4962. F4962 Cryptography & Security — public-key
4963. F4963 Algorithms & Theory of CS — public-key cryptography
4964. F4964 Cryptography & Security — public-key parameter
4965. F4965 Curriculum-only — distribution of order statistics
4966. F4966 NLP & Speech — asr
4967. F4967 Algorithms & Theory of CS — landmark
4968. F4968 Operating Systems — process and memory
4969. F4969 Mathematics — initial value
4970. F4970 Curriculum-only — second-order ode and auxiliary
4971. F4971 Operating Systems — support for os
4972. F4972 Curriculum-only — unix and window
4973. F4973 Data Mining & Databases — network file system
4974. F4974 Distributed Systems & Cloud — unix semaphore
4975. F4975 Operating Systems — unix abstraction
4976. F4976 Other/Unknown — information system
4977. F4977 Curriculum-only — database and information system
4978. F4978 Data Mining & Databases — multimedia database
4979. F4979 Distributed Systems & Cloud — web service
4980. F4980 Computer Networks — web service description
4981. F4981 ML & AI — sep
4982. F4982 Mathematics — soap
4983. F4983 Other/Unknown — geographical information system
4984. F4984 Algorithms & Theory of CS — primary objective
4985. F4985 Computer Networks — foreign key
4986. F4986 Cryptography & Security — primary market
4987. F4987 Curriculum-only — check and foreign key
4988. F4988 Mathematics — column
4989. F4989 Computer Architecture — output column
4990. F4990 Computer Networks — row player
4991. F4991 Curriculum-only — cacheable column
4992. F4992 Data Mining & Databases — ats
4993. F4993 Curriculum-only — column-store system
4994. F4994 Data Mining & Databases — column-family
4995. F4995 Curriculum-only — column-family and graph store
4996. F4996 Distributed Systems & Cloud — column type
4997. F4997 Mathematics — cofactor
4998. F4998 Data Mining & Databases — Two-dimensional space
4999. F4999 ML & AI — low-dimensional space
5000. F5000 Mathematics — entry in column
5001. F5001 Curriculum-only — integral dependent on parameter
5002. F5002 Mathematics — dependent row
5003. F5003 Algorithms & Theory of CS — rank and select
5004. F5004 Computer Architecture — column select
5005. F5005 Curriculum-only — block select
5006. F5006 Mathematics — square matrix
5007. F5007 Operating Systems — double-column
5008. F5008 Other/Unknown — select logic
5009. F5009 Curriculum-only — wake-up and select logic
5010. F5010 Signal/Image/Audio/Video Processing — bigger square matrix
5011. F5011 Software Engineering — code generator
5012. F5012 Mathematics — modern
5013. F5013 Algorithms & Theory of CS — cover modern development
5014. F5014 Computer Networks — modern perspective
5015. F5015 Cryptography & Security — modern encryption
5016. F5016 Curriculum-only — modern business
5017. F5017 Data Mining & Databases — develop modern
5018. F5018 Mathematics — modern algebra
5019. F5019 Curriculum-only — non-restoring division
5020. F5020 Mathematics — classical
5021. F5021 Algorithms & Theory of CS — bqp
5022. F5022 Curriculum-only — classical cipher
5023. F5023 Mathematics — classical inference
5024. F5024 Curriculum-only — distribution of arrival and service time
5025. F5025 Mathematics — service rate
5026. F5026 Algorithms & Theory of CS — universal set of quantum
5027. F5027 NLP & Speech — modern statistical
5028. F5028 Operating Systems — interrupt
5029. F5029 Computer Architecture — device and interrupt
5030. F5030 Curriculum-only — vectored interrupt
5031. F5031 Distributed Systems & Cloud — mark
5032. F5032 Data Mining & Databases — mark vrablic
5033. F5033 Distributed Systems & Cloud — hypervisor
5034. F5034 Curriculum-only — compression in production hypervisor
5035. F5035 Distributed Systems & Cloud — mark in major
5036. F5036 Operating Systems — context switch
5037. F5037 Distributed Systems & Cloud — locking
5038. F5038 Curriculum-only — double-checked locking are named
5039. F5039 Data Mining & Databases — phase locking
5040. F5040 Operating Systems — acquire
5041. F5041 Mathematics — conflict graph
5042. F5042 Operating Systems — crash recovery
5043. F5043 Curriculum-only — crash recovery and the database
5044. F5044 Operating Systems — interrupt vector
5045. F5045 Other/Unknown — classical mechanics
5046. F5046 Curriculum-only — limitation of classical nlp
5047. F5047 Software Engineering — creating
5048. F5048 Mathematics — editing
5049. F5049 Algorithms & Theory of CS — Text editing
5050. F5050 Distributed Systems & Cloud — collaborative editing
5051. F5051 Operating Systems — compare-and-swap
5052. F5052 Distributed Systems & Cloud — waitfor
5053. F5053 Software Engineering — cross site scripting
5054. F5054 Curriculum-only — deadline at every call
5055. F5055 Distributed Systems & Cloud — deadline variable
5056. F5056 Software Engineering — decide to select
5057. F5057 Computer Architecture — eec
5058. F5058 Computer Networks — courier
5059. F5059 Mathematics — fun
5060. F5060 Signal/Image/Audio/Video Processing — eec ii
5061. F5061 Software Engineering — ebp
5062. F5062 Distributed Systems & Cloud — junk
5063. F5063 Software Engineering — linux inter process communication
5064. F5064 Curriculum-only — mail exchange
5065. F5065 Distributed Systems & Cloud — cluster-based mail service
5066. F5066 Software Engineering — mer
5067. F5067 Mathematics — associative
5068. F5068 Distributed Systems & Cloud — associative array
5069. F5069 Software Engineering — associative operator
5070. F5070 Distributed Systems & Cloud — ruby
5071. F5071 Software Engineering — reorder buffer
5072. F5072 Computer Architecture — reg
5073. F5073 Data Mining & Databases — click through rate
5074. F5074 Distributed Systems & Cloud — dest
5075. F5075 Mathematics — ls2
5076. F5076 Operating Systems — img
5077. F5077 Computer Architecture — fft img
5078. F5078 Software Engineering — matt
5079. F5079 Mathematics — plain
5080. F5080 Software Engineering — json
5081. F5081 Computer Networks — ajax
5082. F5082 Curriculum-only — json document
5083. F5083 Other/Unknown — rail
5084. F5084 Computer Architecture — positive rail
5085. F5085 Computer Networks — rail line
5086. F5086 Software Engineering — event ajax
5087. F5087 Curriculum-only — cost-aware selection of countermeasure
5088. F5088 Operating Systems — secure channel
5089. F5089 Curriculum-only — secure channel from your own primitive
5090. F5090 Software Engineering — rest in rail
5091. F5091 Algorithms & Theory of CS — heapify
5092. F5092 Mathematics — pair of element
5093. F5093 Software Engineering — arr
5094. F5094 Distributed Systems & Cloud — scalability
5095. F5095 Cryptography & Security — interoperability
5096. F5096 Curriculum-only — cache-privacy attack
5097. F5097 Curriculum-only — scalability article
5098. F5098 Data Mining & Databases — user privacy
5099. F5099 Mathematics — cohesion
5100. F5100 Curriculum-only — lack of cohesion
5101. F5101 Mathematics — privacy concern
5102. F5102 Operating Systems — linux scalability
5103. F5103 Other/Unknown — critique
5104. F5104 Curriculum-only — queueing theory and reliability
5105. F5105 Distributed Systems & Cloud — critical path
5106. F5106 Information Theory & Coding — reliability function
5107. F5107 Mathematics — mbta
5108. F5108 Operating Systems — quantifying reliability
5109. F5109 Other/Unknown — Reliability of data
5110. F5110 Curriculum-only — queueing theory and reliability theory
5111. F5111 Software Engineering — debugging program
5112. F5112 Curriculum-only — maintainability of the code
5113. F5113 Software Engineering — postcondition
5114. F5114 Curriculum-only — pre and postcondition
5115. F5115 Software Engineering — repository
5116. F5116 Cryptography & Security — repository assigned
5117. F5117 Distributed Systems & Cloud — secure untrusted data repository
5118. F5118 Software Engineering — github repository
5119. F5119 Mathematics — resource constraint
5120. F5120 Software Engineering — Run-time layout of memory: activation record (with various pointers), static data, call-stack, heap
5121. F5121 Software Engineering — user information
5122. F5122 Computer Architecture — button
5123. F5123 Curriculum-only — sanitize all user input to prevent xss
5124. F5124 Software Engineering — ps2
5125. F5125 System Design Primer / Cache — client caching
5126. F5126 System Design Primer / Database — Relational database management system (RDBMS)
5127. F5127 Curriculum-only — choosing between sql and nosql
5128. F5128 Distributed Systems & Cloud — dryadlinq
5129. F5129 Curriculum-only — condor and dryadlinq
5130. F5130 Distributed Systems & Cloud — gfs
5131. F5131 Curriculum-only — colossus as gfs successor
5132. F5132 Distributed Systems & Cloud — nosql data model
5133. F5133 Curriculum-only — family of nosql database
5134. F5134 Other/Unknown — nosql system
5135. F5135 Distributed Systems & Cloud — incremental mapreduce
5136. F5136 Curriculum-only — map-reduce and related paradigm
5137. F5137 Distributed Systems & Cloud — map-reduce paradigm
5138. F5138 Mathematics — update
5139. F5139 Computer Networks — lost update
5140. F5140 Curriculum-only — consistent update
5141. F5141 Distributed Systems & Cloud — delete and update
5142. F5142 Information Theory & Coding — asynchronous update
5143. F5143 Curriculum-only — update cost and route-flap handling
5144. F5144 ML & AI — asat
5145. F5145 Information Theory & Coding — sum-product update rule
5146. F5146 ML & AI — update statement
5147. F5147 Mathematics — dual update
5148. F5148 NLP & Speech — update expression
5149. F5149 Operating Systems — write-update
5150. F5150 Other/Unknown — extension of map-reduce
5151. F5151 Signal/Image/Audio/Video Processing — atb
5152. F5152 Software Engineering — destructive update
5153. F5153 System Design Primer / Availability vs consistency — cap theorem
5154. F5154 Curriculum-only — cap theorem and base
5155. F5155 System Design Primer / Availability vs consistency — CP - consistency and partition tolerance
5156. F5156 System Design Primer / Database — key-value store
5157. F5157 Curriculum-only — built-in key-value store
5158. F5158 Distributed Systems & Cloud — highly available key-value store
5159. F5159 Software Engineering — symbol table
5160. F5160 Data Mining & Databases — expression tree
5161. F5161 Curriculum-only — composition and expression tree
5162. F5162 Software Engineering — local descriptor
5163. F5163 Curriculum-only — subclass and superclass
5164. F5164 Software Engineering — superclass constructor
5165. F5165 CS2023 gap-fill — Propositions as types (implication as a function, conjunction as a product, disjunction as a sum)
5166. F5166 Mathematics — intermediate
5167. F5167 Computer Architecture — intermediate checkoff
5168. F5168 Curriculum-only — intermediate register
5169. F5169 Distributed Systems & Cloud — intermediate mpi
5170. F5170 Mathematics — intermediate value
5171. F5171 NLP & Speech — intermediate file
5172. F5172 Software Engineering — Dependent types (universal quantification as dependent function, existential quantification as dependent product). Illustrative learning outcomes
5173. F5173 Cryptography & Security — access control
5174. F5174 Computer Networks — bridging
5175. F5175 Cryptography & Security — mandatory access control
5176. F5176 Curriculum-only — access control and least privilege
5177. F5177 Data Mining & Databases — datalog
5178. F5178 Distributed Systems & Cloud — multiprocessor
5179. F5179 Curriculum-only — multiprocessor and multicomputer
5180. F5180 Distributed Systems & Cloud — interconnection
5181. F5181 Curriculum-only — interconnection between seemingly disjoint
5182. F5182 Distributed Systems & Cloud — lock-free
5183. F5183 Curriculum-only — lock-free structure are named
5184. F5184 Distributed Systems & Cloud — concurrent data structure
5185. F5185 Curriculum-only — retry storm that unjittered retry cause
5186. F5186 Information Theory & Coding — ipv4
5187. F5187 NLP & Speech — Compositional Semantics
5188. F5188 Data Mining & Databases — free variable
5189. F5189 Distributed Systems & Cloud — lexical scope
5190. F5190 NLP & Speech — ambiguity resolution
5191. F5191 Operating Systems — concurrent transaction
5192. F5192 Other/Unknown — bound variable
5193. F5193 Curriculum-only — free and bound variable
5194. F5194 Other/Unknown — distributional semantics
5195. F5195 Curriculum-only — soundness argument stated
5196. F5196 Software Engineering — abstract interpretation
5197. F5197 Algorithms & Theory of CS — priority queue
5198. F5198 Curriculum-only — correctness by euler theorem
5199. F5199 Distributed Systems & Cloud — atomicity
5200. F5200 Curriculum-only — atomicity of update
5201. F5201 Distributed Systems & Cloud — correctness proof of mnr
5202. F5202 Curriculum-only — graceful stop on the termination signal
5203. F5203 ML & AI — principle of artificial intelligence
5204. F5204 Distributed Systems & Cloud — machine
5205. F5205 Algorithms & Theory of CS — computing machine
5206. F5206 Curriculum-only — committee machine
5207. F5207 Curriculum-only — wayback machine
5208. F5208 Data Mining & Databases — emin
5209. F5209 Distributed Systems & Cloud — ose
5210. F5210 Curriculum-only — data replicated asynchronously
5211. F5211 Distributed Systems & Cloud — replicated log
5212. F5212 Information Theory & Coding — state diagram
5213. F5213 ML & AI — bartlett
5214. F5214 Mathematics — cdc
5215. F5215 Curriculum-only — makespan minimization on identical machine
5216. F5216 Mathematics — machine precision
5217. F5217 Operating Systems — achieving atomicity
5218. F5218 Other/Unknown — electrical machine
5219. F5219 Signal/Image/Audio/Video Processing — bartlett window
5220. F5220 Software Engineering — correctness argument
5221. F5221 Curriculum-only — hmac and its nested
5222. F5222 Software Engineering — nested loop
5223. F5223 Curriculum-only — block nested loop
5224. F5224 Software Engineering — object file
5225. F5225 Curriculum-only — non-executable memory
5226. F5226 Software Engineering — cpp
5227. F5227 Algorithms & Theory of CS — psr
5228. F5228 Curriculum-only — log-structured merge tree
5229. F5229 ML & AI — structured output
5230. F5230 Software Engineering — style and structure
5231. F5231 Operating Systems — data block
5232. F5232 Software Engineering — top-down
5233. F5233 Algorithms & Theory of CS — skip list
5234. F5234 Curriculum-only — b-tree and skip list
5235. F5235 Distributed Systems & Cloud — algorithm
5236. F5236 Algorithms & Theory of CS — algorithm and real
5237. F5237 Algorithms & Theory of CS — exact algorithms
5238. F5238 Algorithms & Theory of CS — pseudopolynomial algorithm
5239. F5239 Computer Networks — abstraction and algorithm
5240. F5240 Cryptography & Security — algorithm tn
5241. F5241 Algorithms & Theory of CS — digital signature standard
5242. F5242 Cryptography & Security — mqv algorithm
5243. F5243 Curriculum-only — algorithm and its correctness
5244. F5244 Curriculum-only — grover algorithm
5245. F5245 Curriculum-only — short-step algorithm
5246. F5246 Data Mining & Databases — algorithm for answering
5247. F5247 Distributed Systems & Cloud — algorithm for analyzing
5248. F5248 Distributed Systems & Cloud — central algorithm
5249. F5249 Algorithms & Theory of CS — prefix sum
5250. F5250 Data Mining & Databases — strassen
5251. F5251 Curriculum-only — solovay strassen
5252. F5252 Distributed Systems & Cloud — cilk poeg
5253. F5253 Curriculum-only — epidemic and gossip-based algorithm
5254. F5254 Distributed Systems & Cloud — gpu algorithm
5255. F5255 Distributed Systems & Cloud — optimistic algorithm
5256. F5256 Curriculum-only — franklin and peterson algorithm
5257. F5257 Distributed Systems & Cloud — pion
5258. F5258 Curriculum-only — paradigm and the programming model
5259. F5259 Distributed Systems & Cloud — distributed programming model
5260. F5260 Curriculum-only — local memory to shared memory
5261. F5261 Distributed Systems & Cloud — asynchronous shared memory
5262. F5262 Cryptography & Security — based consensus
5263. F5263 Curriculum-only — consensus form
5264. F5264 Distributed Systems & Cloud — consensus algorithm
5265. F5265 Curriculum-only — distributed-memory multicomputer
5266. F5266 Distributed Systems & Cloud — distributed memory programming
5267. F5267 Curriculum-only — mobile gadget
5268. F5268 Data Mining & Databases — warehousing
5269. F5269 Distributed Systems & Cloud — mobile nodes
5270. F5270 Algorithms & Theory of CS — self-stabilizing algorithm
5271. F5271 Distributed Systems & Cloud — Shared memory algorithms
5272. F5272 Curriculum-only — simd lane
5273. F5273 Distributed Systems & Cloud — graphic processing unit
5274. F5274 Distributed Systems & Cloud — synthesizing parallel program
5275. F5275 Curriculum-only — worker consume the latest cached object
5276. F5276 Information Theory & Coding — centralized algorithms
5277. F5277 Curriculum-only — link-layer attack
5278. F5278 ML & AI — algebraic algorithm
5279. F5279 Curriculum-only — llm operational exploitation
5280. F5280 ML & AI — exploration and exploitation
5281. F5281 Mathematics — algorithm and system
5282. F5282 Curriculum-only — algorithm for multiplication and division
5283. F5283 Mathematics — algorithm themselve
5284. F5284 Curriculum-only — bag semantics
5285. F5285 Distributed Systems & Cloud — p-bag
5286. F5286 Mathematics — compute log
5287. F5287 Curriculum-only — efficient vector database is required
5288. F5288 Data Mining & Databases — algorithm for computing
5289. F5289 Distributed Systems & Cloud — efficient parallel program
5290. F5290 Information Theory & Coding — efficient encoding
5291. F5291 ML & AI — efficient computation
5292. F5292 Mathematics — efficient estimate
5293. F5293 Cryptography & Security — efficiently computed
5294. F5294 Mathematics — eigensolver algorithm
5295. F5295 Distributed Systems & Cloud — fastest machine
5296. F5296 Mathematics — g-s
5297. F5297 Curriculum-only — matrix and matrix operation
5298. F5298 Mathematics — matrix product
5299. F5299 Algorithms & Theory of CS — matrix product checker
5300. F5300 Curriculum-only — min-plus matrix product view
5301. F5301 Mathematics — maximum value
5302. F5302 Algorithms & Theory of CS — memory transfer
5303. F5303 Mathematics — funnel
5304. F5304 Curriculum-only — object funnel operation
5305. F5305 Distributed Systems & Cloud — input buffer
5306. F5306 Mathematics — ers
5307. F5307 ML & AI — classi ers
5308. F5308 Mathematics — modified gram-schmidt
5309. F5309 Algorithms & Theory of CS — add path extension
5310. F5310 Algorithms & Theory of CS — search tree
5311. F5311 Curriculum-only — billion search
5312. F5312 Curriculum-only — mechanical search
5313. F5313 Data Mining & Databases — keyword search
5314. F5314 Distributed Systems & Cloud — expected search time
5315. F5315 ML & AI — domain reduction
5316. F5316 Curriculum-only — geometric view of rule
5317. F5317 ML & AI — greedy decoding
5318. F5318 Mathematics — heuristic
5319. F5319 Algorithms & Theory of CS — distance heuristic
5320. F5320 Curriculum-only — heuristic detection
5321. F5321 Mathematics — interval
5322. F5322 Cryptography & Security — interval tree
5323. F5323 Curriculum-only — highest-density interval
5324. F5324 Information Theory & Coding — reservation interval
5325. F5325 ML & AI — reward function
5326. F5326 Mathematics — arrival in disjoint time
5327. F5327 Algorithms & Theory of CS — key card
5328. F5328 Computer Networks — composite key
5329. F5329 Cryptography & Security — equivalent key
5330. F5330 Curriculum-only — alternate key
5331. F5331 Curriculum-only — key-policy
5332. F5332 Data Mining & Databases — key size
5333. F5333 Distributed Systems & Cloud — key id
5334. F5334 ML & AI — acme
5335. F5335 Mathematics — eevee
5336. F5336 Algorithms & Theory of CS — pseudo code
5337. F5337 Curriculum-only — reached after turning
5338. F5338 Mathematics — shifted qr
5339. F5339 Curriculum-only — singleton with shared state among instance
5340. F5340 Mathematics — sparse matrix algorithm
5341. F5341 NLP & Speech — earley algorithm
5342. F5342 Operating Systems — manchester
5343. F5343 Other/Unknown — bch code
5344. F5344 Other/Unknown — mobile systems
5345. F5345 Distributed Systems & Cloud — leader
5346. F5346 Curriculum-only — stable leader
5347. F5347 Distributed Systems & Cloud — based leader
5348. F5348 ML & AI — perturbed leader
5349. F5349 Other/Unknown — page-rank algorithm
5350. F5350 Curriculum-only — confidence and prediction interval
5351. F5351 Other/Unknown — professional ethics
5352. F5352 Distributed Systems & Cloud — ieee
5353. F5353 Computer Networks — proc ieee infocom
5354. F5354 Curriculum-only — ieee code
5355. F5355 Distributed Systems & Cloud — thompson
5356. F5356 Cryptography & Security — josh thompson
5357. F5357 Other/Unknown — random access
5358. F5358 Algorithms & Theory of CS — random-access machine
5359. F5359 Computer Architecture — dynamic random access memory
5360. F5360 Curriculum-only — sequential against random access
5361. F5361 Other/Unknown — sequential versus random access
5362. F5362 Signal/Image/Audio/Video Processing — cascade algorithm
5363. F5363 Mathematics — twiddle factor
5364. F5364 Signal/Image/Audio/Video Processing — decimation-in
5365. F5365 Software Engineering — bisection algorithm
5366. F5366 Curriculum-only — dissemination barrier
5367. F5367 Software Engineering — efficiency of program
5368. F5368 Mathematics — code fragments
5369. F5369 Other/Unknown — communication network
5370. F5370 Distributed Systems & Cloud — computer network
5371. F5371 Curriculum-only — computer network history
5372. F5372 Distributed Systems & Cloud — fault tolerant computing system
5373. F5373 Curriculum-only — dependability
5374. F5374 Information Theory & Coding — bandwidth
5375. F5375 Computer Networks — analog bandwidth
5376. F5376 Curriculum-only — bisection bandwidth
5377. F5377 Distributed Systems & Cloud — interconnect
5378. F5378 Computer Architecture — Programmable interconnect
5379. F5379 Curriculum-only — processor-memory interconnect
5380. F5380 Information Theory & Coding — congestion control
5381. F5381 Computer Networks — end-to-end congestion control
5382. F5382 Curriculum-only — congestion control principle
5383. F5383 Information Theory & Coding — data communication network
5384. F5384 Curriculum-only — switch fabrics
5385. F5385 Information Theory & Coding — internetworking
5386. F5386 Computer Networks — internetworking and routing
5387. F5387 Information Theory & Coding — multiplexing
5388. F5388 Curriculum-only — sc-fdma
5389. F5389 Information Theory & Coding — signal bandwidth
5390. F5390 NLP & Speech — wide bandwidth
5391. F5391 Operating Systems — active queue management
5392. F5392 Other/Unknown — bandwidth efficiency
5393. F5393 Software Engineering — data structure computer network
5394. F5394 Mathematics — country
5395. F5395 Software Engineering — identi ers
5396. F5396 Mathematics — university
5397. F5397 Computer Networks — online version
5398. F5398 Distributed Systems & Cloud — tel aviv
5399. F5399 Data Mining & Databases — harvard university press
5400. F5400 Distributed Systems & Cloud — matrix computation
5401. F5401 ML & AI — thomas
5402. F5402 Algorithms & Theory of CS — geoffrey thomas
5403. F5403 Curriculum-only — thomas write rule
5404. F5404 Mathematics — cambridge univ
5405. F5405 Other/Unknown — rd edition
5406. F5406 Mathematics — suggested
5407. F5407 Computer Networks — suggested time
5408. F5408 Curriculum-only — suggested content
5409. F5409 Software Engineering — private
5410. F5410 Cryptography & Security — private browsing
5411. F5411 Curriculum-only — private one for the rest
5412. F5412 Operating Systems — private memory
5413. F5413 Curriculum-only — local and private memory
5414. F5414 Software Engineering — client server
5415. F5415 Algorithms & Theory of CS — vertex colouring
5416. F5416 Data Mining & Databases — turing
5417. F5417 Cryptography & Security — contract and turing
5418. F5418 Data Mining & Databases — Computational thinking
5419. F5419 Distributed Systems & Cloud — real time
5420. F5420 Data Mining & Databases — real time database
5421. F5421 Other/Unknown — prevention
5422. F5422 Distributed Systems & Cloud — parallel programming
5423. F5423 Cryptography & Security — hybrid argument
5424. F5424 Curriculum-only — hybrid connectivity
5425. F5425 Distributed Systems & Cloud — hybrid algorithm
5426. F5426 ML & AI — nir
5427. F5427 Data Mining & Databases — nir ailon
5428. F5428 Distributed Systems & Cloud — herlihy and nir
5429. F5429 Other/Unknown — pipelining
5430. F5430 Computer Architecture — dynamic pipelining
5431. F5431 Curriculum-only — materialisation against pipelining
5432. F5432 Distributed Systems & Cloud — concurrency
5433. F5433 Curriculum-only — bound on concurrency
5434. F5434 Data Mining & Databases — query plan
5435. F5435 Distributed Systems & Cloud — concurrency ch
5436. F5436 Computer Architecture — set-associative
5437. F5437 Curriculum-only — amazon sqs hosted but with higher latency
5438. F5438 Distributed Systems & Cloud — latency memory
5439. F5439 Curriculum-only — multithreading half
5440. F5440 Distributed Systems & Cloud — dynamic multithreading
5441. F5441 Computer Architecture — associative cache
5442. F5442 Computer Networks — rf-id tags
5443. F5443 Curriculum-only — cost tag
5444. F5444 Mathematics — pessimistic
5445. F5445 Curriculum-only — pessimistic estimate
5446. F5446 Operating Systems — average cache read latency
5447. F5447 Other/Unknown — real-time embedded
5448. F5448 Software Engineering — complex pipelining
5449. F5449 Curriculum-only — mutex is simpler
5450. F5450 Operating Systems — condition variable
5451. F5451 Distributed Systems & Cloud — message
5452. F5452 Algorithms & Theory of CS — caesar cipher
5453. F5453 Cryptography & Security — Attacker capabilities: chosen-message attack (for signatures), birthday attacks, side channel attacks, and fault injection attacks
5454. F5454 Curriculum-only — change-root message
5455. F5455 Data Mining & Databases — key message
5456. F5456 Distributed Systems & Cloud — byzantine
5457. F5457 Algorithms & Theory of CS — time bound
5458. F5458 Cryptography & Security — byzantine consensus
5459. F5459 Distributed Systems & Cloud — approximate agreement
5460. F5460 Cryptography & Security — byzantine fault
5461. F5461 Curriculum-only — controlled fault injection
5462. F5462 Distributed Systems & Cloud — Fault handling and reliability
5463. F5463 Computer Networks — virtual private
5464. F5464 Curriculum-only — virtual and materialised view
5465. F5465 Distributed Systems & Cloud — isas
5466. F5466 Curriculum-only — owner of nested paging
5467. F5467 Distributed Systems & Cloud — virtual channel
5468. F5468 Curriculum-only — virtual-channel reservation
5469. F5469 Distributed Systems & Cloud — virtual private cloud
5470. F5470 Information Theory & Coding — decode
5471. F5471 Curriculum-only — lossy virtual link
5472. F5472 ML & AI — fbethe
5473. F5473 Mathematics — distinct value
5474. F5474 Curriculum-only — encrypt-and-mac
5475. F5475 Mathematics — inherited
5476. F5476 Curriculum-only — lock inherited by the parent
5477. F5477 Mathematics — notion
5478. F5478 Computer Networks — notion of centrality
5479. F5479 Data Mining & Databases — notion of truth
5480. F5480 Mathematics — peter
5481. F5481 Data Mining & Databases — eric grimson
5482. F5482 Distributed Systems & Cloud — peter druschel
5483. F5483 Operating Systems — encrypt-then-mac
5484. F5484 Curriculum-only — table and page-table entry
5485. F5485 Operating Systems — virtual processor
5486. F5486 Other/Unknown — fault location
5487. F5487 Signal/Image/Audio/Video Processing — peter hagelstein
5488. F5488 Software Engineering — account mutex
5489. F5489 Operating Systems — out-of-order completion
5490. F5490 Software Engineering — in-order
5491. F5491 Operating Systems — in-order commit
5492. F5492 Software Engineering — physical and virtual
5493. F5493 Algorithms & Theory of CS — String searching algorithm
5494. F5494 Curriculum-only — inserting and searching algorithm
5495. F5495 Software Engineering — stack algorithm
5496. F5496 Curriculum-only — step-size condition
5497. F5497 Software Engineering — stepwise refinement
5498. F5498 Curriculum-only — unified kill chain
5499. F5499 Operating Systems — unified cache
5500. F5500 Software Engineering — unsorted
5501. F5501 Algorithms & Theory of CS — unsorted array
5502. F5502 Software Engineering — variable scope
5503. F5503 Algorithms & Theory of CS — shortest path
5504. F5504 Curriculum-only — augmenting path and berge theorem
5505. F5505 Mathematics — algorithm to find
5506. F5506 HS Maths Class XII / Unit-IV: Vectors and Three-dimensional Geometry — three-dimensional geometry
5507. F5507 Algorithms & Theory of CS — isoperimetric inequality
5508. F5508 Algorithms & Theory of CS — edit distance
5509. F5509 Algorithms & Theory of CS — colorability of multigraph
5510. F5510 Algorithms & Theory of CS — polytope theorem
5511. F5511 Computer Networks — unweighted graph
5512. F5512 Curriculum-only — automl became vertex ai
5513. F5513 Curriculum-only — vector geometry
5514. F5514 Distributed Systems & Cloud — vertex rdd
5515. F5515 Information Theory & Coding — outgoing message
5516. F5516 ML & AI — cn vertex
5517. F5517 Curriculum-only — item item similarity
5518. F5518 ML & AI — pancake
5519. F5519 Mathematics — curve
5520. F5520 Algorithms & Theory of CS — hilbert curve
5521. F5521 Curriculum-only — curve order
5522. F5522 Data Mining & Databases — algebraic curve
5523. F5523 Distributed Systems & Cloud — Linear combinations of polynomials, Bezier curves
5524. F5524 ML & AI — expression curve
5525. F5525 Mathematics — circle
5526. F5526 Algorithms & Theory of CS — random cut
5527. F5527 Curriculum-only — cut and cycle
5528. F5528 Data Mining & Databases — maxbis
5529. F5529 Distributed Systems & Cloud — consistent cut
5530. F5530 Mathematics — branch cut
5531. F5531 Curriculum-only — transformation in euclidean geometry
5532. F5532 Mathematics — face
5533. F5533 Algorithms & Theory of CS — outside face
5534. F5534 Curriculum-only — mean face
5535. F5535 Mathematics — gradient eld
5536. F5536 Algorithms & Theory of CS — back to multicommodity cut
5537. F5537 Curriculum-only — back-of-the-envelope estimate
5538. F5538 Data Mining & Databases — latest version
5539. F5539 Algorithms & Theory of CS — offline
5540. F5540 Curriculum-only — available offline
5541. F5541 Distributed Systems & Cloud — send message
5542. F5542 Information Theory & Coding — length of back cavity
5543. F5543 ML & AI — choose operator
5544. F5544 Mathematics — backpack
5545. F5545 Curriculum-only — arithmetic of origin load
5546. F5546 Mathematics — orthogonal trajectory
5547. F5547 Computer Networks — Rotational symmetry
5548. F5548 Data Mining & Databases — sanity check
5549. F5549 Mathematics — continuous symmetry
5550. F5550 Curriculum-only — tunnelling and translation
5551. F5551 Data Mining & Databases — translation scheme
5552. F5552 Information Theory & Coding — frequency translation
5553. F5553 Mathematics — translation in time
5554. F5554 Curriculum-only — group with their own parameter drawn
5555. F5555 Mathematics — velocity eld
5556. F5556 NLP & Speech — anow
5557. F5557 Distributed Systems & Cloud — ibm
5558. F5558 Curriculum-only — ibm page gave two licence description
5559. F5559 Data Mining & Databases — ibm built
5560. F5560 Mathematics — synergistic processor element
5561. F5561 Distributed Systems & Cloud — status
5562. F5562 Computer Networks — status code
5563. F5563 Curriculum-only — request counting by status
5564. F5564 Distributed Systems & Cloud — mbox
5565. F5565 NLP & Speech — translation systems
5566. F5566 Operating Systems — address translation
5567. F5567 Algorithms & Theory of CS — searching sorting
5568. F5568 Distributed Systems & Cloud — parallel
5569. F5569 Algorithms & Theory of CS — parallel sorting
5570. F5570 Computer Architecture — on-the-fly
5571. F5571 Curriculum-only — centralised parallel
5572. F5572 Distributed Systems & Cloud — algorithm parallel
5573. F5573 Curriculum-only — global memory order
5574. F5574 Distributed Systems & Cloud — hybrid parallel
5575. F5575 Curriculum-only — map of the parallel architecture
5576. F5576 Distributed Systems & Cloud — multicore
5577. F5577 Curriculum-only — map of the multicore
5578. F5578 Distributed Systems & Cloud — multicore chip
5579. F5579 Curriculum-only — parallel prefix adder
5580. F5580 Distributed Systems & Cloud — parallel prex
5581. F5581 Curriculum-only — non-serialized schedule
5582. F5582 Distributed Systems & Cloud — series-parallel dag
5583. F5583 Computer Architecture — Process synchronization
5584. F5584 Curriculum-only — point-to-point synchronisation with flag
5585. F5585 Distributed Systems & Cloud — barrier synchronization
5586. F5586 Curriculum-only — bayes consistency
5587. F5587 Distributed Systems & Cloud — causal consistency
5588. F5588 Curriculum-only — cloud course key-value
5589. F5589 Distributed Systems & Cloud — key-value abstraction
5590. F5590 Curriculum-only — chandy lamport snapshot
5591. F5591 Distributed Systems & Cloud — lamport algorithm
5592. F5592 Distributed Systems & Cloud — tolerance
5593. F5593 Curriculum-only — link back to byzantine tolerance
5594. F5594 Distributed Systems & Cloud — fault tolerance
5595. F5595 Cryptography & Security — byzantine fault tolerance
5596. F5596 Curriculum-only — fault tolerance by re-execution
5597. F5597 Distributed Systems & Cloud — exclusion
5598. F5598 Curriculum-only — exclusion between level
5599. F5599 Distributed Systems & Cloud — dining philosopher
5600. F5600 Curriculum-only — virtualization using docker
5601. F5601 Distributed Systems & Cloud — benefit of virtualization
5602. F5602 Distributed Systems & Cloud — virtualization and cloud
5603. F5603 Curriculum-only — zookeeper also appear in the reading list
5604. F5604 Information Theory & Coding — redundancy
5605. F5605 Curriculum-only — n-modular redundancy
5606. F5606 Information Theory & Coding — Time synchronization/scheduling
5607. F5607 Curriculum-only — time synchronisation at the level of name
5608. F5608 ML & AI — leslie kaelbling
5609. F5609 Curriculum-only — raw fnv
5610. F5610 Distributed Systems & Cloud — bill thy
5611. F5611 Mathematics — cleverly
5612. F5612 ML & AI — eat qt
5613. F5613 Mathematics — edge-cut
5614. F5614 Algorithms & Theory of CS — partitioning
5615. F5615 Curriculum-only — channel partitioning
5616. F5616 Data Mining & Databases — recursive partitioning
5617. F5617 Distributed Systems & Cloud — Horizontal partitioning
5618. F5618 Mathematics — fast
5619. F5619 Algorithms & Theory of CS — fast pointer
5620. F5620 Curriculum-only — common case fast
5621. F5621 Data Mining & Databases — fast johnson-lindenstrauss
5622. F5622 Distributed Systems & Cloud — fast data
5623. F5623 ML & AI — fast computation
5624. F5624 Mathematics — correct value
5625. F5625 NLP & Speech — fast car
5626. F5626 Operating Systems — cpu virtualization
5627. F5627 Curriculum-only — fault and demand paging
5628. F5628 Operating Systems — fast retransmit
5629. F5629 Other/Unknown — array geometries
5630. F5630 Distributed Systems & Cloud — heterogeneous clusters
5631. F5631 Other/Unknown — heterogeneous catalysis
5632. F5632 Curriculum-only — effect and an interaction
5633. F5633 Data Mining & Databases — interaction detection
5634. F5634 Distributed Systems & Cloud — migration
5635. F5635 Curriculum-only — live vm migration
5636. F5636 Mathematics — complicated interaction
5637. F5637 Other/Unknown — biological
5638. F5638 Curriculum-only — biological inspiration
5639. F5639 Mathematics — species
5640. F5640 Other/Unknown — biological database
5641. F5641 Data Mining & Databases — chemical data
5642. F5642 Mathematics — drip
5643. F5643 Other/Unknown — chemical engineering
5644. F5644 Curriculum-only — brief primer on word-level
5645. F5645 Distributed Systems & Cloud — citation
5646. F5646 Computer Architecture — citation format
5647. F5647 Curriculum-only — citation in the multi-agent
5648. F5648 Distributed Systems & Cloud — citation data
5649. F5649 Other/Unknown — Projective geometry
5650. F5650 Information Theory & Coding — sporadic job
5651. F5651 Other/Unknown — structure and function
5652. F5652 Signal/Image/Audio/Video Processing — back matter
5653. F5653 Mathematics — cos nx
5654. F5654 Cryptography & Security — shock
5655. F5655 Mathematics — damping condition
5656. F5656 Computer Architecture — complex amplitude
5657. F5657 Mathematics — angle
5658. F5658 Computer Architecture — angle checker
5659. F5659 Curriculum-only — ambiguous side-side-angle
5660. F5660 Data Mining & Databases — synchronization-type
5661. F5661 Mathematics — arcco
5662. F5662 Algorithms & Theory of CS — diagonal set
5663. F5663 Data Mining & Databases — dual player
5664. F5664 Mathematics — block diagonal
5665. F5665 Curriculum-only — addition and double-angle formulas
5666. F5666 Mathematics — ection
5667. F5667 Data Mining & Databases — descending
5668. F5668 Mathematics — orthonormal eigenvector
5669. F5669 Algorithms & Theory of CS — arborally satis
5670. F5670 Curriculum-only — minimum bounding rectangle
5671. F5671 Mathematics — rectangle rule
5672. F5672 Other/Unknown — function space
5673. F5673 NLP & Speech — resonance frequency
5674. F5674 Other/Unknown — surface plasmon resonance
5675. F5675 Signal/Image/Audio/Video Processing — averaging
5676. F5676 Curriculum-only — polyak ruppert averaging
5677. F5677 Signal/Image/Audio/Video Processing — borel measure
5678. F5678 Computer Architecture — input impedance
5679. F5679 Data Mining & Databases — impedance mismatch
5680. F5680 Mathematics — mechanical impedance
5681. F5681 NLP & Speech — acoustic mass
5682. F5682 Mathematics — terminal
5683. F5683 Computer Architecture — exposed terminal
5684. F5684 Information Theory & Coding — terminal stage
5685. F5685 Mathematics — positive terminal
5686. F5686 NLP & Speech — acoustic circuit
5687. F5687 Computer Architecture — pair of terminal
5688. F5688 NLP & Speech — characteristic impedance
5689. F5689 Mathematics — intrinsic
5690. F5690 Cryptography & Security — intrinsic value
5691. F5691 Mathematics — intrinsic norm
5692. F5692 NLP & Speech — intrinsic pressure
5693. F5693 Other/Unknown — equivalent circuit
5694. F5694 Signal/Image/Audio/Video Processing — inverse filter
5695. F5695 Mathematics — triangle
5696. F5696 Algorithms & Theory of CS — monochromatic triangle
5697. F5697 Computer Networks — triangle graph
5698. F5698 Curriculum-only — cia triangle
5699. F5699 Mathematics — equilateral
5700. F5700 Algorithms & Theory of CS — thumbtack
5701. F5701 Curriculum-only — meet-in-the-middle attack on double encryption
5702. F5702 Mathematics — pyramid
5703. F5703 Curriculum-only — pyramid of pain
5704. F5704 Mathematics — triangle inequality
5705. F5705 Algorithms & Theory of CS — negative weight cycle
5706. F5706 Information Theory & Coding — hamming distance
5707. F5707 Algorithms & Theory of CS — respect to hamming distance
5708. F5708 Information Theory & Coding — code word
5709. F5709 Algorithms & Theory of CS — number of message
5710. F5710 Distributed Systems & Cloud — message sent
5711. F5711 Data Mining & Databases — anomaly
5712. F5712 Computer Networks — update anomaly
5713. F5713 Curriculum-only — anomaly each permit
5714. F5714 Data Mining & Databases — outlier
5715. F5715 Curriculum-only — local outlier factor
5716. F5716 Data Mining & Databases — robust to outlier
5717. F5717 Distributed Systems & Cloud — acm
5718. F5718 Algorithms & Theory of CS — icalp
5719. F5719 Algorithms & Theory of CS — constant-time insertion
5720. F5720 Algorithms & Theory of CS — post correspondence
5721. F5721 Computer Networks — acm sosp
5722. F5722 Cryptography & Security — acm ccs
5723. F5723 Curriculum-only — acm and ieee code
5724. F5724 Data Mining & Databases — acm sigmod
5725. F5725 Algorithms & Theory of CS — recursively enumerable language
5726. F5726 Data Mining & Databases — Recursively enumerable set
5727. F5727 Distributed Systems & Cloud — acm operating system
5728. F5728 Cryptography & Security — enforce legal contract
5729. F5729 Curriculum-only — constraint on every legal instance
5730. F5730 Data Mining & Databases — legal system
5731. F5731 Information Theory & Coding — end-to-end
5732. F5732 Distributed Systems & Cloud — metrics
5733. F5733 Computer Architecture — classification metrics
5734. F5734 Curriculum-only — base metrics
5735. F5735 Data Mining & Databases — common metrics
5736. F5736 Mathematics — decided
5737. F5737 Data Mining & Databases — calculable partial function
5738. F5738 Mathematics — triangle inequality for integral
5739. F5739 NLP & Speech — finite state automaton
5740. F5740 Other/Unknown — debt
5741. F5741 Cryptography & Security — cme
5742. F5742 Other/Unknown — fractal
5743. F5743 Signal/Image/Audio/Video Processing — l1 fourier
5744. F5744 Curriculum-only — rotor machine
5745. F5745 Mathematics — rotation
5746. F5746 Algorithms & Theory of CS — binary tree ii
5747. F5747 Computer Architecture — rotation and translation
5748. F5748 Curriculum-only — key rotation
5749. F5749 Mathematics — computational efficiency
5750. F5750 Other/Unknown — rotor resistances
5751. F5751 Signal/Image/Audio/Video Processing — euclidean motion
5752. F5752 Software Engineering — analyzing origin
5753. F5753 Algorithms & Theory of CS — cost circulation
5754. F5754 Mathematics — minimum cost flow
5755. F5755 Algorithms & Theory of CS — wolf
5756. F5756 Other/Unknown — ocean circulation
5757. F5757 Software Engineering — complexity metrics
5758. F5758 HS ComputerScience Class XI / Unit 2: Computational Thinking and Programming - I — flow of control
5759. F5759 Computer Architecture — alu instruction
5760. F5760 Computer Networks — form and control
5761. F5761 Curriculum-only — assessment and control
5762. F5762 Curriculum-only — discretionary and mandatory control
5763. F5763 Data Mining & Databases — control and recovery
5764. F5764 Distributed Systems & Cloud — element interconnect bus
5765. F5765 Information Theory & Coding — control channels
5766. F5766 ML & AI — command and control
5767. F5767 Mathematics — advance
5768. F5768 Algorithms & Theory of CS — implement advance
5769. F5769 Data Mining & Databases — advance in database
5770. F5770 Mathematics — forward
5771. F5771 Algorithms & Theory of CS — euler forward
5772. F5772 Computer Networks — store-and-forward
5773. F5773 Curriculum-only — backward-taken forward-not-taken
5774. F5774 ML & AI — forward chaining
5775. F5775 Mathematics — backward di erence
5776. F5776 Algorithms & Theory of CS — conflict-directed back jumping
5777. F5777 Mathematics — rem
5778. F5778 NLP & Speech — forward-traveling
5779. F5779 Operating Systems — alu control
5780. F5780 Curriculum-only — control and the alu control
5781. F5781 Operating Systems — buffer overrun
5782. F5782 Other/Unknown — control and automation
5783. F5783 Curriculum-only — reliability and cost control
5784. F5784 Other/Unknown — digital control
5785. F5785 NLP & Speech — speech information processing
5786. F5786 Other/Unknown — instrumentation and control
5787. F5787 Other/Unknown — supervisory control
5788. F5788 Signal/Image/Audio/Video Processing — derivative control
5789. F5789 Mathematics — force
5790. F5790 Algorithms & Theory of CS — collision
5791. F5791 Curriculum-only — collision bound
5792. F5792 Distributed Systems & Cloud — collision function
5793. F5793 Mathematics — Electromotive force
5794. F5794 NLP & Speech — viscous force
5795. F5795 Other/Unknown — atomic force microscopy
5796. F5796 Signal/Image/Audio/Video Processing — turbulent wind
5797. F5797 Software Engineering — aircraft control
5798. F5798 Software Engineering — fast-paced
5799. F5799 Distributed Systems & Cloud — greg gagne
5800. F5800 Software Engineering — hiding
5801. F5801 Cryptography & Security — hiding and binding
5802. F5802 Distributed Systems & Cloud — tioas
5803. F5803 Software Engineering — ikx dx
5804. F5804 Algorithms & Theory of CS — correct implementation
5805. F5805 Computer Architecture — python implementation
5806. F5806 Computer Networks — database implementation
5807. F5807 Cryptography & Security — implementation of secure computer
5808. F5808 Curriculum-only — covering algorithm and implementation
5809. F5809 Data Mining & Databases — Implementation strategies
5810. F5810 Distributed Systems & Cloud — ananian
5811. F5811 Mathematics — break
5812. F5812 Cryptography & Security — cryptosystem
5813. F5813 Algorithms & Theory of CS — scribe
5814. F5814 Cryptography & Security — ciphertext
5815. F5815 Algorithms & Theory of CS — number of possible plaintext
5816. F5816 Cryptography & Security — chosen plaintext attack
5817. F5817 Curriculum-only — break history
5818. F5818 Distributed Systems & Cloud — protocol
5819. F5819 Algorithms & Theory of CS — deliver
5820. F5820 Cryptography & Security — consensus protocol
5821. F5821 Curriculum-only — asynchronous protocol
5822. F5822 Curriculum-only — vi protocol
5823. F5823 Distributed Systems & Cloud — gossip protocol
5824. F5824 Information Theory & Coding — mac protocol
5825. F5825 Distributed Systems & Cloud — contention
5826. F5826 Curriculum-only — retry with backoff
5827. F5827 Distributed Systems & Cloud — backoff algorithm
5828. F5828 Computer Architecture — throughput and latency
5829. F5829 Curriculum-only — batching for throughput against latency
5830. F5830 Information Theory & Coding — improving throughput
5831. F5831 Curriculum-only — request and response protocol
5832. F5832 Information Theory & Coding — routing table
5833. F5833 Mathematics — common lisp
5834. F5834 Cryptography & Security — secret key
5835. F5835 Computer Networks — triple des
5836. F5836 Cryptography & Security — secret-key and public-key
5837. F5837 Curriculum-only — matsui des attack
5838. F5838 Mathematics — girlfriend with subject
5839. F5839 Operating Systems — bus-based implementation
5840. F5840 Curriculum-only — adversary emulation plan
5841. F5841 Operating Systems — implementation of operating system
5842. F5842 Distributed Systems & Cloud — efcient lock implementation
5843. F5843 Other/Unknown — classical cryptosystem
5844. F5844 Software Engineering — bisect
5845. F5845 Distributed Systems & Cloud — bivalent
5846. F5846 Mathematics — ext
5847. F5847 Software Engineering — lock and synchronization
5848. F5848 Distributed Systems & Cloud — multicore programming primer
5849. F5849 Data Mining & Databases — creative
5850. F5850 Other/Unknown — creative expression
5851. F5851 Data Mining & Databases — creative expression with arduino
5852. F5852 Software Engineering — network flow ii
5853. F5853 Curriculum-only — pq recap
5854. F5854 Software Engineering — robust network flow
5855. F5855 Curriculum-only — stored-program idea through vacuum tube
5856. F5856 Software Engineering — test suite
5857. F5857 Information Theory & Coding — transmission
5858. F5858 Distributed Systems & Cloud — current time
5859. F5859 Information Theory & Coding — block transmissions
5860. F5860 Information Theory & Coding — signalling
5861. F5861 Mathematics — loop transmission
5862. F5862 Other/Unknown — cellular
5863. F5863 Curriculum-only — cellular mac
5864. F5864 Information Theory & Coding — cellular phone
5865. F5865 Other/Unknown — cellular system
5866. F5866 Curriculum-only — utilisation of pipelined protocol
5867. F5867 Information Theory & Coding — link utilization
5868. F5868 Software Engineering — acknowledge
5869. F5869 Curriculum-only — interrupt request and acknowledge
5870. F5870 Software Engineering — victim
5871. F5871 Curriculum-only — victim machine
5872. F5872 Software Engineering — virtual function
5873. F5873 Curriculum-only — loop weakest precondition need an invariant
5874. F5874 Software Engineering — window machine
5875. F5875 System Design Primer / Asynchronism — message queue
5876. F5876 Curriculum-only — credit-based and on off back-pressure
5877. F5877 System Design Primer / Availability patterns — replication
5878. F5878 Computer Networks — database replication
5879. F5879 Curriculum-only — database replication and partitioning
5880. F5880 Distributed Systems & Cloud — chain replication
5881. F5881 Curriculum-only — group with intra-group dependence check
5882. F5882 Distributed Systems & Cloud — replication of state
5883. F5883 Curriculum-only — key ideas of sdn
5884. F5884 Information Theory & Coding — time division multiple access
5885. F5885 Algorithms & Theory of CS — tim
5886. F5886 Computer Networks — carrier sense multiple access
5887. F5887 Information Theory & Coding — packet
5888. F5888 Algorithms & Theory of CS — ip version
5889. F5889 Computer Networks — forwarding
5890. F5890 Curriculum-only — forwarding strategy
5891. F5891 Data Mining & Databases — youtube
5892. F5892 Computer Networks — isp
5893. F5893 Distributed Systems & Cloud — packet capture
5894. F5894 Information Theory & Coding — accept packet
5895. F5895 Curriculum-only — channel access protocol
5896. F5896 Information Theory & Coding — fast packet
5897. F5897 Curriculum-only — virtual switch and fast packet
5898. F5898 Information Theory & Coding — fast packet switching
5899. F5899 Mathematics — hop
5900. F5900 Curriculum-only — route and next hop
5901. F5901 Mathematics — suggestion
5902. F5902 Operating Systems — intra-domain routing protocol
5903. F5903 Curriculum-only — write-through with write buffer
5904. F5904 Other/Unknown — dna
5905. F5905 Mathematics — bacterial
5906. F5906 Other/Unknown — gene expression
5907. F5907 Curriculum-only — isolation level
5908. F5908 Other/Unknown — protein and nucleic
5909. F5909 Information Theory & Coding — messenger rna
5910. F5910 Other/Unknown — rna splicing
5911. F5911 Curriculum-only — centralized traffic engineering
5912. F5912 Software Engineering — ben bitdiddle
5913. F5913 Computer Architecture — debugging strategy
5914. F5914 Distributed Systems & Cloud — cell debugging
5915. F5915 Software Engineering — debug
5916. F5916 Data Mining & Databases — hard to debug
5917. F5917 Curriculum-only — hard to debug and cache
5918. F5918 ML & AI — imm
5919. F5919 Operating Systems — nop
5920. F5920 Computer Architecture — sram addr
5921. F5921 Distributed Systems & Cloud — system programming
5922. F5922 Curriculum-only — map of the cloud-and-distributed-system
5923. F5923 Distributed Systems & Cloud — building distributed system
5924. F5924 Curriculum-only — time and ordering in distributed system
5925. F5925 Distributed Systems & Cloud — peer-to-peer system
5926. F5926 Curriculum-only — unstructured peer-to-peer system
5927. F5927 Distributed Systems & Cloud — proficiency with system programming
5928. F5928 Mathematics — rhombus
5929. F5929 Distributed Systems & Cloud — robert scheifler
5930. F5930 Information Theory & Coding — gallager
5931. F5931 Distributed Systems & Cloud — state-machine simulation
5932. F5932 Curriculum-only — wait-for-graph deadlock detection
5933. F5933 Distributed Systems & Cloud — minimum spanning tree
5934. F5934 Algorithms & Theory of CS — euclidean minimum spanning tree
5935. F5935 Curriculum-only — algorithm for max flow
5936. F5936 Mathematics — guy named robert
5937. F5937 Cryptography & Security — password
5938. F5938 Algorithms & Theory of CS — sdk
5939. F5939 Computer Networks — password generator
5940. F5940 Cryptography & Security — channel attack
5941. F5941 Curriculum-only — password and lockout policy
5942. F5942 Data Mining & Databases — han
5943. F5943 Distributed Systems & Cloud — serializability
5944. F5944 Curriculum-only — conflict equivalence and conflict serializability
5945. F5945 Data Mining & Databases — concurrency control
5946. F5946 Curriculum-only — concurrency control protocol
5947. F5947 Distributed Systems & Cloud — serializable
5948. F5948 Curriculum-only — serializable snapshot isolation
5949. F5949 Mathematics — engineer
5950. F5950 Algorithms & Theory of CS — mechanical engineer
5951. F5951 Curriculum-only — number every engineer carry
5952. F5952 Mathematics — optimization
5953. F5953 Algorithms & Theory of CS — career fair optimization
5954. F5954 Cryptography & Security — graph optimization
5955. F5955 Curriculum-only — approximation algorithm are named
5956. F5956 Curriculum-only — optimization technique in cache memory
5957. F5957 Data Mining & Databases — adword optimization
5958. F5958 Curriculum-only — linear regression and classification by lp
5959. F5959 Data Mining & Databases — one-variable linear regression
5960. F5960 Algorithms & Theory of CS — fks
5961. F5961 Computer Networks — complex queries
5962. F5962 Curriculum-only — byte query
5963. F5963 Curriculum-only — query written in algebra
5964. F5964 Data Mining & Databases — preprocessing
5965. F5965 Curriculum-only — data and preprocessing
5966. F5966 Data Mining & Databases — Query planning
5967. F5967 Distributed Systems & Cloud — billion query
5968. F5968 Cryptography & Security — provenance
5969. F5969 Curriculum-only — agentic state provenance
5970. F5970 Distributed Systems & Cloud — Focus on how they work without going into mathematical or optimization details; enough to understand and use existing implementations correctly
5971. F5971 Algorithms & Theory of CS — constraint networks
5972. F5972 Computer Architecture — linear networks
5973. F5973 Computer Networks — centrality measure
5974. F5974 Computer Networks — geographic
5975. F5975 Computer Networks — network data
5976. F5976 Computer Networks — price of anarchy
5977. F5977 Curriculum-only — broad network access
5978. F5978 Curriculum-only — help to network
5979. F5979 Data Mining & Databases — geographic location
5980. F5980 Distributed Systems & Cloud — acc
5981. F5981 Curriculum-only — high-bandwidth dram
5982. F5982 Distributed Systems & Cloud — hypercubic network
5983. F5983 Curriculum-only — network-based attack
5984. F5984 Distributed Systems & Cloud — network programming
5985. F5985 Algorithms & Theory of CS — perfect matching
5986. F5986 Curriculum-only — networked service
5987. F5987 Distributed Systems & Cloud — senior
5988. F5988 Information Theory & Coding — atm switch
5989. F5989 Curriculum-only — circuit switching and packet switching
5990. F5990 Information Theory & Coding — congested
5991. F5991 Computer Networks — mpeg-1
5992. F5992 Information Theory & Coding — Network components
5993. F5993 ML & AI — conjunctive queries
5994. F5994 Curriculum-only — linear perceptron
5995. F5995 ML & AI — perceptron test
5996. F5996 Curriculum-only — implementation of unsupervised learning in python
5997. F5997 ML & AI — reinforcement
5998. F5998 Mathematics — ampl
5999. F5999 Algorithms & Theory of CS — phase ph
6000. F6000 Cryptography & Security — user connect
6001. F6001 Curriculum-only — object that know how to connect other object
6002. F6002 ML & AI — undirected edge
6003. F6003 Mathematics — constant folding
6004. F6004 Algorithms & Theory of CS — caro
6005. F6005 Computer Networks — betweenness
6006. F6006 Curriculum-only — degree and radian
6007. F6007 Data Mining & Databases — Degree (angle)
6008. F6008 Distributed Systems & Cloud — bachelor of engineering degree
6009. F6009 Mathematics — derivative-free
6010. F6010 Data Mining & Databases — advertiser
6011. F6011 Mathematics — linear regression in high
6012. F6012 ML & AI — local extremum of fbethe
6013. F6013 Mathematics — magnanti
6014. F6014 ML & AI — mistake probability
6015. F6015 Mathematics — bigger mistake
6016. F6016 Algorithms & Theory of CS — alice bob
6017. F6017 Cryptography & Security — hellman
6018. F6018 Curriculum-only — hellman table
6019. F6019 Information Theory & Coding — equivocation
6020. F6020 Mathematics — bob win
6021. F6021 Distributed Systems & Cloud — speculative
6022. F6022 Curriculum-only — speculative decoding
6023. F6023 Information Theory & Coding — link state advertisement
6024. F6024 Algorithms & Theory of CS — neighbor
6025. F6025 Cryptography & Security — neighbour indistinguishability
6026. F6026 Curriculum-only — element no larger than its neighbour
6027. F6027 Mathematics — holme
6028. F6028 Distributed Systems & Cloud — journal
6029. F6029 Algorithms & Theory of CS — street
6030. F6030 Distributed Systems & Cloud — journal of parallel
6031. F6031 Mathematics — journal article
6032. F6032 Curriculum-only — circuit minimization and simplification
6033. F6033 Mathematics — sinusoidal response
6034. F6034 Curriculum-only — ip subnet
6035. F6035 Mathematics — subspace
6036. F6036 Algorithms & Theory of CS — random subspaces
6037. F6037 Curriculum-only — definition of subspace
6038. F6038 ML & AI — arxiv
6039. F6039 Computer Networks — blog
6040. F6040 Algorithms & Theory of CS — blog post
6041. F6041 Computer Architecture — blog site
6042. F6042 Mathematics — cyclic group
6043. F6043 Curriculum-only — cyclic group they form
6044. F6044 Mathematics — echelon
6045. F6045 Curriculum-only — effect of the pivot
6046. F6046 Data Mining & Databases — bucket
6047. F6047 Curriculum-only — bucket and object
6048. F6048 Distributed Systems & Cloud — s3 bucket
6049. F6049 Information Theory & Coding — leaky bucket
6050. F6050 Mathematics — exchange for nonzero pivot
6051. F6051 Curriculum-only — column reduced matrix
6052. F6052 Mathematics — reduced gradient
6053. F6053 Curriculum-only — shamo hoey sweep
6054. F6054 Mathematics — symmetric matrix
6055. F6055 Curriculum-only — definiteness of matrix
6056. F6056 Mathematics — diagonalization of symmetric matrix
6057. F6057 NLP & Speech — graph network
6058. F6058 Operating Systems — atm network
6059. F6059 Curriculum-only — network attack and defence
6060. F6060 Operating Systems — network failure
6061. F6061 Distributed Systems & Cloud — software
6062. F6062 Algorithms & Theory of CS — inertial
6063. F6063 Computer Networks — cmmi
6064. F6064 Cryptography & Security — collaborative softwares
6065. F6065 Curriculum-only — customer see software
6066. F6066 Curriculum-only — software equation
6067. F6067 Data Mining & Databases — Explain multiple benefits and limitations of static typing in writing, maintaining, and debugging software
6068. F6068 Distributed Systems & Cloud — fault tolerance in software
6069. F6069 Curriculum-only — open-source intelligence
6070. F6070 Data Mining & Databases — implementation in open-source software
6071. F6071 Curriculum-only — nessus and the open-source alternative
6072. F6072 Distributed Systems & Cloud — azure
6073. F6073 Curriculum-only — global software-defined network
6074. F6074 Distributed Systems & Cloud — software paradigm
6075. F6075 Mathematics — cot
6076. F6076 Algorithms & Theory of CS — renewed focus on efficiency
6077. F6077 ML & AI — primary focus
6078. F6078 Mathematics — ellipse
6079. F6079 Algorithms & Theory of CS — time fewer
6080. F6080 Distributed Systems & Cloud — qemu sec
6081. F6081 Mathematics — decay rate
6082. F6082 NLP & Speech — beach
6083. F6083 Algorithms & Theory of CS — beach line
6084. F6084 NLP & Speech — Mathematical software
6085. F6085 Operating Systems — emulator
6086. F6086 Operating Systems — srp
6087. F6087 Curriculum-only — conflict and view serializability
6088. F6088 Operating Systems — view server
6089. F6089 Distributed Systems & Cloud — server
6090. F6090 Computer Networks — microsoft sql server
6091. F6091 Cryptography & Security — compromising
6092. F6092 Curriculum-only — authoritative server
6093. F6093 Curriculum-only — server need both address in dns
6094. F6094 Data Mining & Databases — Network servers
6095. F6095 Distributed Systems & Cloud — close-to-open
6096. F6096 Curriculum-only — system continue despite network partition
6097. F6097 Distributed Systems & Cloud — replica
6098. F6098 Curriculum-only — in-sync replicas
6099. F6099 Distributed Systems & Cloud — response time
6100. F6100 Curriculum-only — response time and throughput
6101. F6101 Distributed Systems & Cloud — server virtualization
6102. F6102 Information Theory & Coding — client connect
6103. F6103 Mathematics — chubby
6104. F6104 Curriculum-only — google chubby
6105. F6105 Mathematics — ipad
6106. F6106 Operating Systems — path name
6107. F6107 Other/Unknown — algebra and optimization
6108. F6108 Other/Unknown — Markov networks
6109. F6109 Information Theory & Coding — delay
6110. F6110 Computer Architecture — retiming
6111. F6111 Curriculum-only — bandwidth delay product
6112. F6112 Distributed Systems & Cloud — cache access
6113. F6113 Information Theory & Coding — added delay
6114. F6114 Other/Unknown — network simulator
6115. F6115 Computer Networks — ns2 network simulator
6116. F6116 Other/Unknown — opengl
6117. F6117 Computer Networks — eia
6118. F6118 Information Theory & Coding — advantage of qubit
6119. F6119 Mathematics — prepare
6120. F6120 Cryptography & Security — decided to prepare
6121. F6121 Mathematics — expected to prepare
6122. F6122 Algorithms & Theory of CS — pocket sphere
6123. F6123 Information Theory & Coding — bloch sphere
6124. F6124 Mathematics — extrema
6125. F6125 Other/Unknown — reinforcement learning
6126. F6126 Curriculum-only — reinforcement learning for fine-tuning
6127. F6127 Other/Unknown — actor critic
6128. F6128 Curriculum-only — in-transit
6129. F6129 Distributed Systems & Cloud — peer
6130. F6130 Curriculum-only — edit log and checkpoint
6131. F6131 Distributed Systems & Cloud — asynchronous consistent checkpoint
6132. F6132 Information Theory & Coding — peer-to-peer network
6133. F6133 Distributed Systems & Cloud — sharing file
6134. F6134 Mathematics — chord
6135. F6135 Algorithms & Theory of CS — diameter
6136. F6136 Computer Networks — average path length
6137. F6137 Curriculum-only — distance and diameter
6138. F6138 Mathematics — passenger
6139. F6139 Computer Networks — reception in passenger car
6140. F6140 Data Mining & Databases — warehouse
6141. F6141 Information Theory & Coding — detect
6142. F6142 Mathematics — addressed
6143. F6143 Curriculum-only — content-addressed object
6144. F6144 Mathematics — spacecraft
6145. F6145 NLP & Speech — retention
6146. F6146 Operating Systems — dp peer
6147. F6147 Other/Unknown — gps
6148. F6148 Computer Networks — gps receivers
6149. F6149 ML & AI — gps signal
6150. F6150 Signal/Image/Audio/Video Processing — accumulator
6151. F6151 Other/Unknown — motor
6152. F6152 Cryptography & Security — tracker
6153. F6153 Curriculum-only — tracker and noise
6154. F6154 Mathematics — crime
6155. F6155 Other/Unknown — Computer crime
6156. F6156 Signal/Image/Audio/Video Processing — digital network
6157. F6157 Mathematics — fixed
6158. F6158 Algorithms & Theory of CS — fixed parameter tractability
6159. F6159 Curriculum-only — fixed and variable length
6160. F6160 Distributed Systems & Cloud — fixed-connection
6161. F6161 ML & AI — fixed vector
6162. F6162 Mathematics — complete metric space
6163. F6163 Signal/Image/Audio/Video Processing — signal ow
6164. F6164 Software Engineering — abelson
6165. F6165 Mathematics — ann
6166. F6166 Data Mining & Databases — artist
6167. F6167 Signal/Image/Audio/Video Processing — fuzzy
6168. F6168 Curriculum-only — fuzzy extractor with helper data
6169. F6169 Data Mining & Databases — fuzzy c-means
6170. F6170 ML & AI — learning
6171. F6171 Algorithms & Theory of CS — learning objective
6172. F6172 Curriculum-only — bayes learning
6173. F6173 Data Mining & Databases — crawling
6174. F6174 Distributed Systems & Cloud — interested in learning
6175. F6175 ML & AI — Adversarial learning
6176. F6176 Data Mining & Databases — open learning library
6177. F6177 ML & AI — learning theory
6178. F6178 Curriculum-only — written learning-theory
6179. F6179 Data Mining & Databases — bulletin
6180. F6180 ML & AI — meta-learning
6181. F6181 Curriculum-only — relu family
6182. F6182 ML & AI — softmax
6183. F6183 Curriculum-only — softmax cross-entropy
6184. F6184 ML & AI — weighted majority
6185. F6185 Mathematics — algebra and learning
6186. F6186 Curriculum-only — mainly for python
6187. F6187 Other/Unknown — advancement
6188. F6188 Distributed Systems & Cloud — recent advancement
6189. F6189 Other/Unknown — fuzzy set
6190. F6190 Mathematics — game
6191. F6191 Algorithms & Theory of CS — alpha-beta
6192. F6192 Computer Architecture — Game play
6193. F6193 Computer Networks — learning game
6194. F6194 Curriculum-only — elgamal in those game
6195. F6195 Data Mining & Databases — game theoretical
6196. F6196 Distributed Systems & Cloud — game development
6197. F6197 ML & AI — alpha beta search
6198. F6198 Mathematics — contestant
6199. F6199 Curriculum-only — compute metric score
6200. F6200 Data Mining & Databases — match score
6201. F6201 ML & AI — tf-idf
6202. F6202 Curriculum-only — apply tf-idf
6203. F6203 ML & AI — tfidf
6204. F6204 Mathematics — ind
6205. F6205 Cryptography & Security — ind-cpa
6206. F6206 Curriculum-only — formal definition of ind-cpa by left-or-right
6207. F6207 Mathematics — test score
6208. F6208 Other/Unknown — multitask learning
6209. F6209 Mathematics — finding
6210. F6210 Algorithms & Theory of CS — haystack
6211. F6211 Computer Architecture — buddy
6212. F6212 Cryptography & Security — prime finding
6213. F6213 Curriculum-only — behavioural finding that stated
6214. F6214 Distributed Systems & Cloud — finding moment
6215. F6215 Mathematics — easy to find
6216. F6216 Distributed Systems & Cloud — efficient algorithm for determining
6217. F6217 Other/Unknown — Statistical relational learning
6218. F6218 Signal/Image/Audio/Video Processing — finding cluster in graph
6219. F6219 Software Engineering — buddy assigned
6220. F6220 Software Engineering — global dynamic data
6221. F6221 Software Engineering — mat
6222. F6222 ML & AI — llc
6223. F6223 Software Engineering — itl
6224. F6224 Curriculum-only — single box is loaded
6225. F6225 Software Engineering — memory optimization
6226. F6226 Curriculum-only — cache memory optimization
6227. F6227 Software Engineering — namespace
6228. F6228 Curriculum-only — cgroup and namespace
6229. F6229 Software Engineering — nesting
6230. F6230 Curriculum-only — nist publication
6231. F6231 Software Engineering — nutshell
6232. F6232 Information Theory & Coding — input value
6233. F6233 Software Engineering — parameterised query
6234. F6234 Cryptography & Security — balance sheet
6235. F6235 Distributed Systems & Cloud — notification
6236. F6236 Curriculum-only — notification and error-reporting level
6237. F6237 Mathematics — ratio
6238. F6238 Algorithms & Theory of CS — approximation ratio
6239. F6239 Curriculum-only — approximation algorithm and the ratio
6240. F6240 Data Mining & Databases — odd ratio
6241. F6241 Information Theory & Coding — compression ratio (machinery)
6242. F6242 ML & AI — gain ratio
6243. F6243 Mathematics — critical damping
6244. F6244 Curriculum-only — bilinear transformation and cross ratio
6245. F6245 Mathematics — damping ratio
6246. F6246 Algorithms & Theory of CS — shipping server
6247. F6247 Mathematics — starbuck
6248. F6248 NLP & Speech — pressure and volume
6249. F6249 Other/Unknown — strehl ratio
6250. F6250 Software Engineering — guideline
6251. F6251 Other/Unknown — standard and guideline
6252. F6252 Software Engineering — personnel
6253. F6253 Other/Unknown — development process
6254. F6254 Mathematics — established
6255. F6255 Other/Unknown — equipment
6256. F6256 Mathematics — heat
6257. F6257 Algorithms & Theory of CS — fin
6258. F6258 Data Mining & Databases — heat map
6259. F6259 Mathematics — aka heat
6260. F6260 Curriculum-only — ax and the matrix exponential
6261. F6261 Mathematics — observer
6262. F6262 Curriculum-only — constructor and observer
6263. F6263 Mathematics — pole diagram
6264. F6264 Computer Networks — Concept of user/system state and protection, transition to kernel mode using system calls
6265. F6265 Curriculum-only — defined here by its numerical behaviour
6266. F6266 Information Theory & Coding — chaotic behaviors
6267. F6267 Mathematics — pole diagram mathlet
6268. F6268 Curriculum-only — formal definition of the react loop
6269. F6269 Mathematics — rest initial condition
6270. F6270 Curriculum-only — complex gain per subcarrier
6271. F6271 Mathematics — laplace transform
6272. F6272 Algorithms & Theory of CS — olution
6273. F6273 Mathematics — constant coefficient
6274. F6274 Curriculum-only — rational form
6275. F6275 Data Mining & Databases — rational root
6276. F6276 Mathematics — archimedian
6277. F6277 Curriculum-only — include and extend
6278. F6278 Mathematics — pole
6279. F6279 Computer Networks — telephone pole
6280. F6280 Mathematics — euler approximation
6281. F6281 Curriculum-only — kendall tau
6282. F6282 Mathematics — undetermined coefficient
6283. F6283 Operating Systems — atomic action
6284. F6284 Other/Unknown — diffusion equation
6285. F6285 Mathematics — back and forth
6286. F6286 Curriculum-only — existence of linear transformation
6287. F6287 Mathematics — convex set
6288. F6288 Curriculum-only — commonly occurring convex set
6289. F6289 Mathematics — cone
6290. F6290 Curriculum-only — cone of feasible direction
6291. F6291 Mathematics — central axis
6292. F6292 Algorithms & Theory of CS — lattice vector
6293. F6293 Curriculum-only — complemented lattice
6294. F6294 Information Theory & Coding — lattice definition
6295. F6295 Mathematics — field
6296. F6296 Algorithms & Theory of CS — potential field
6297. F6297 Computer Architecture — tag field
6298. F6298 Cryptography & Security — cryptology
6299. F6299 Curriculum-only — computational diffie hellman
6300. F6300 Data Mining & Databases — adjoining
6301. F6301 Curriculum-only — boneh shoup
6302. F6302 Data Mining & Databases — transcendence degree
6303. F6303 Information Theory & Coding — berlekamp
6304. F6304 ML & AI — receptive field
6305. F6305 Mathematics — adjoining element
6306. F6306 Distributed Systems & Cloud — ams sketch
6307. F6307 Mathematics — auxiliary field
6308. F6308 Distributed Systems & Cloud — conservative locking
6309. F6309 Mathematics — criterion for gradient field
6310. F6310 Algorithms & Theory of CS — brick
6311. F6311 Computer Networks — control plane
6312. F6312 Curriculum-only — argand plane
6313. F6313 Mathematics — coordinate system
6314. F6314 Curriculum-only — horizontal-line test
6315. F6315 Mathematics — initial guess
6316. F6316 Algorithms & Theory of CS — g1 and g2
6317. F6317 Mathematics — artin
6318. F6318 Data Mining & Databases — algebraically closed field
6319. F6319 Mathematics — rectangular lattice
6320. F6320 Data Mining & Databases — semide nite programming
6321. F6321 Mathematics — positive semide nite
6322. F6322 Curriculum-only — network slicing
6323. F6323 Data Mining & Databases — time-slicing
6324. F6324 Mathematics — standard rectangular coordinate system
6325. F6325 Algorithms & Theory of CS — tower function
6326. F6326 Curriculum-only — tower of hanoi as the recurrence
6327. F6327 Mathematics — tower of field
6328. F6328 ML & AI — arg max
6329. F6329 Mathematics — branch of arg
6330. F6330 Data Mining & Databases — auc
6331. F6331 Mathematics — aaa
6332. F6332 Algorithms & Theory of CS — oor
6333. F6333 Curriculum-only — hitting the wall
6334. F6334 Mathematics — floor
6335. F6335 Information Theory & Coding — error floor
6336. F6336 Mathematics — yij
6337. F6337 NLP & Speech — air space
6338. F6338 Other/Unknown — air conditioners
6339. F6339 Curriculum-only — operator on inner-product space
6340. F6340 Mathematics — adjoint
6341. F6341 Curriculum-only — adjoint determinant theorem
6342. F6342 Mathematics — adjoint equation
6343. F6343 Curriculum-only — projection and real symmetric matrix
6344. F6344 Mathematics — rotation group
6345. F6345 Curriculum-only — conditioning of random variable
6346. F6346 Data Mining & Databases — gaussian concentration
6347. F6347 ML & AI — algorithm for inference
6348. F6348 Curriculum-only — primer on concentration inequality
6349. F6349 ML & AI — independent gaussian
6350. F6350 Mathematics — central moment
6351. F6351 Curriculum-only — joint probability and covariance
6352. F6352 Mathematics — cumulative
6353. F6353 Algorithms & Theory of CS — cumulative frequency
6354. F6354 Curriculum-only — cumulative and delayed acknowledgement
6355. F6355 Mathematics — discrete-valued random variable
6356. F6356 Mathematics — function fx
6357. F6357 Information Theory & Coding — modem
6358. F6358 Algorithms & Theory of CS — earliest
6359. F6359 Curriculum-only — earliest and latest start and finish
6360. F6360 Mathematics — joint density
6361. F6361 Curriculum-only — multiple integral are used only for joint density
6362. F6362 Mathematics — jointly
6363. F6363 Curriculum-only — expectation by linearity
6364. F6364 Mathematics — linearity of expectation
6365. F6365 Curriculum-only — expectation and linearity of expectation
6366. F6366 Mathematics — manipulating continuous random variable
6367. F6367 Curriculum-only — erlang and akka style
6368. F6368 Mathematics — erlang random variable
6369. F6369 Algorithms & Theory of CS — suffix
6370. F6370 Curriculum-only — bor vka-style fragment merging
6371. F6371 Data Mining & Databases — sorting and merging
6372. F6372 Mathematics — merging poisson
6373. F6373 Curriculum-only — moment-generating-function sketch
6374. F6374 Mathematics — erx
6375. F6375 Curriculum-only — covariance and correlation matrix
6376. F6376 Mathematics — iterated expectation
6377. F6377 Curriculum-only — graphical displays of multivariate data
6378. F6378 Mathematics — nonsingular
6379. F6379 Curriculum-only — lose the quadrant
6380. F6380 Mathematics — joint distribution function
6381. F6381 Curriculum-only — random experiment and event
6382. F6382 Mathematics — random variable ii
6383. F6383 Curriculum-only — probability and random variable ii
6384. F6384 Mathematics — random variable of variance
6385. F6385 Mathematics — converge to in probability
6386. F6386 Mathematics — value with probability
6387. F6387 NLP & Speech — diagonal-covariance gaussian
6388. F6388 Other/Unknown — linearizing cone
6389. F6389 Algorithms & Theory of CS — cnot
6390. F6390 Computer Networks — spanning tree protocol
6391. F6391 Curriculum-only — switching and spanning tree
6392. F6392 Data Mining & Databases — weighted shortest path
6393. F6393 Algorithms & Theory of CS — subset sum
6394. F6394 Distributed Systems & Cloud — reducer
6395. F6395 Curriculum-only — reducer size
6396. F6396 Mathematics — teen
6397. F6397 ML & AI — singular vector
6398. F6398 Mathematics — singular value
6399. F6399 Curriculum-only — singular value and singular vector
6400. F6400 Mathematics — hermitian
6401. F6401 ML & AI — hermitian transpose
6402. F6402 Mathematics — hermitian space
6403. F6403 Distributed Systems & Cloud — fortran
6404. F6404 Mathematics — julia programming language
6405. F6405 Algorithms & Theory of CS — analytic bound
6406. F6406 Curriculum-only — analytic store
6407. F6407 Information Theory & Coding — analytic form
6408. F6408 Mathematics — analytic geometry
6409. F6409 Algorithms & Theory of CS — binet-cauchy
6410. F6410 Curriculum-only — cauchy integral theorem
6411. F6411 Mathematics — cauchy data
6412. F6412 Curriculum-only — function of complex variable
6413. F6413 Mathematics — complex plane
6414. F6414 Curriculum-only — line integral in the complex plane
6415. F6415 Mathematics — analytic function
6416. F6416 Curriculum-only — analytic function and complex integration
6417. F6417 Mathematics — cauchy-riemann equation
6418. F6418 Curriculum-only — analytic function and cauchy riemann equation
6419. F6419 Mathematics — connected region
6420. F6420 Mathematics — heat equation
6421. F6421 Mathematics — circle of radius
6422. F6422 Mathematics — polar form
6423. F6423 Curriculum-only — polar form and why multiplication
6424. F6424 Mathematics — proof of analytic
6425. F6425 Curriculum-only — taylor series with gradient
6426. F6426 Mathematics — taylor series expansion
6427. F6427 Curriculum-only — karatsuba three-product trick
6428. F6428 ML & AI — datapoint
6429. F6429 Mathematics — practical trick
6430. F6430 Other/Unknown — analytic hierarchies
6431. F6431 Curriculum-only — fourier series to boundary value
6432. F6432 Mathematics — boundary value prob
6433. F6433 HS Maths Class XI / Unit-II: Algebra — sequence and series
6434. F6434 Algorithms & Theory of CS — sunny
6435. F6435 Computer Networks — yeast
6436. F6436 Cryptography & Security — ripe
6437. F6437 Curriculum-only — winding number and maximum modulus principle
6438. F6438 ML & AI — statistical learning
6439. F6439 Algorithms & Theory of CS — blumer
6440. F6440 Curriculum-only — perceptron learning algorithm
6441. F6441 Mathematics — ordered field
6442. F6442 Cryptography & Security — peso
6443. F6443 Mathematics — lognormal
6444. F6444 Mathematics — significance testing
6445. F6445 Algorithms & Theory of CS — shorting stock
6446. F6446 Curriculum-only — reorder when the stock
6447. F6447 Data Mining & Databases — stock price
6448. F6448 Mathematics — number of share
6449. F6449 Curriculum-only — uniform convergence of series
6450. F6450 Mathematics — bounded function
6451. F6451 Curriculum-only — riemann darboux definition
6452. F6452 Mathematics — darboux sum
6453. F6453 Curriculum-only — differentiability and analyticity of function
6454. F6454 Mathematics — sequence of function
6455. F6455 Curriculum-only — generalization and modern overparametrization
6456. F6456 ML & AI — generalization theory
6457. F6457 Mathematics — riemann hypothesis
6458. F6458 Curriculum-only — power series and radius of convergence
6459. F6459 Mathematics — sequence of rational number
6460. F6460 Computer Networks — newman
6461. F6461 Mathematics — dirichlet
6462. F6462 ML & AI — dirichlet distribution
6463. F6463 Mathematics — dirichlet boundary condition
6464. F6464 Mathematics — removable discontinuity
6465. F6465 Curriculum-only — gradient of vector-valued function
6466. F6466 Mathematics — matrix-valued function
6467. F6467 NLP & Speech — tiger
6468. F6468 Other/Unknown — algebraic equation
6469. F6469 Mathematics — differential algebraic equation
6470. F6470 Other/Unknown — continuous system
6471. F6471 Mathematics — derivative of analytic function
6472. F6472 Other/Unknown — differentiation and integration
6473. F6473 Mathematics — lim inf
6474. F6474 Algorithms & Theory of CS — convex hull
6475. F6475 Curriculum-only — convex hull by graham scan
6476. F6476 Information Theory & Coding — achievable region
6477. F6477 ML & AI — convex pz
6478. F6478 Mathematics — affine
6479. F6479 Curriculum-only — conic and structured convex program
6480. F6480 Mathematics — conic optimization
6481. F6481 Curriculum-only — harmonic and geometric mean
6482. F6482 Mathematics — global minima
6483. F6483 Curriculum-only — reduced hessian matrix
6484. F6484 Mathematics — hyperplane
6485. F6485 Algorithms & Theory of CS — random-hyperplane rounding
6486. F6486 Curriculum-only — hyperplane and half-space
6487. F6487 Mathematics — inequality hold
6488. F6488 Curriculum-only — discontinuous piecewise linear function
6489. F6489 Mathematics — local optimum
6490. F6490 Algorithms & Theory of CS — search algorithm
6491. F6491 Curriculum-only — graph search and hsm
6492. F6492 Mathematics — nonlinear optimization
6493. F6493 Curriculum-only — linearly constrained nonlinear optimization algorithm
6494. F6494 ML & AI — ridge regression
6495. F6495 Mathematics — optimal value
6496. F6496 Data Mining & Databases — optimal value of satisfy
6497. F6497 Mathematics — positive semidefinite
6498. F6498 Distributed Systems & Cloud — model
6499. F6499 Algorithms & Theory of CS — cell-probe
6500. F6500 Algorithms & Theory of CS — random model
6501. F6501 Computer Architecture — impedance model
6502. F6502 Computer Networks — create model
6503. F6503 Computer Networks — information spread
6504. F6504 Cryptography & Security — attack model
6505. F6505 Curriculum-only — actor model
6506. F6506 Curriculum-only — cell-division model
6507. F6507 Curriculum-only — model are treated
6508. F6508 Curriculum-only — model weakness
6509. F6509 Curriculum-only — predictor model
6510. F6510 Curriculum-only — score-based model
6511. F6511 Curriculum-only — unified process and agile model named
6512. F6512 Data Mining & Databases — aic
6513. F6513 Curriculum-only — information criterion aic
6514. F6514 Data Mining & Databases — available data
6515. F6515 Curriculum-only — cross-datacenter replication
6516. F6516 Data Mining & Databases — discuss model
6517. F6517 Distributed Systems & Cloud — cio
6518. F6518 Curriculum-only — combiner generator
6519. F6519 Distributed Systems & Cloud — combiner and partitioner
6520. F6520 Curriculum-only — federated system
6521. F6521 Distributed Systems & Cloud — game models
6522. F6522 Curriculum-only — including the git object model
6523. F6523 Distributed Systems & Cloud — resource sharing
6524. F6524 Curriculum-only — latency and throughput model
6525. F6525 Distributed Systems & Cloud — time-based
6526. F6526 Information Theory & Coding — continuous-time model
6527. F6527 ML & AI — alternate model
6528. F6528 Curriculum-only — generative-model service
6529. F6529 ML & AI — image model
6530. F6530 Curriculum-only — finite mixture of distribution
6531. F6531 ML & AI — algorithm for learning mixture
6532. F6532 Curriculum-only — openai api
6533. F6533 ML & AI — pre-training
6534. F6534 Information Theory & Coding — encoder
6535. F6535 Curriculum-only — bi-encoder
6536. F6536 Information Theory & Coding — noisy channel
6537. F6537 Curriculum-only — dangling-node correction
6538. F6538 Information Theory & Coding — Error identification and correction mechanisms, checksums of volatile memory in RAM
6539. F6539 ML & AI — text-to-image model
6540. F6540 Curriculum-only — toy spn
6541. F6541 ML & AI — tractable
6542. F6542 Curriculum-only — invertible network with tractable determinant
6543. F6543 ML & AI — training data
6544. F6544 Curriculum-only — training-data contamination
6545. F6545 ML & AI — filing cabinet
6546. F6546 Mathematics — checkout counter model
6547. F6547 Computer Networks — data normalization
6548. F6548 Algorithms & Theory of CS — insert
6549. F6549 Computer Networks — modeling and measurement-i
6550. F6550 Curriculum-only — including insert
6551. F6551 Data Mining & Databases — er modeling
6552. F6552 Distributed Systems & Cloud — list insert
6553. F6553 ML & AI — insert state
6554. F6554 Mathematics — cured
6555. F6555 Curriculum-only — prey predator
6556. F6556 Mathematics — predator-prey system
6557. F6557 Curriculum-only — structured probabilistic model
6558. F6558 Mathematics — axiom of probability
6559. F6559 Algorithms & Theory of CS — collectively exhaustive
6560. F6560 Mathematics — probability model
6561. F6561 Curriculum-only — measure-theoretic probability space
6562. F6562 Mathematics — discrete probability space
6563. F6563 Curriculum-only — optimization in real-world
6564. F6564 Mathematics — convergence wp1
6565. F6565 Information Theory & Coding — repetition
6566. F6566 Curriculum-only — repetition to reduce soundness error
6567. F6567 Information Theory & Coding — code rate
6568. F6568 Mathematics — real-world scenario
6569. F6569 Algorithms & Theory of CS — Synchronous group communication (e.g., chat rooms, conferencing, online games)
6570. F6570 Computer Architecture — living room
6571. F6571 Data Mining & Databases — surgeon
6572. F6572 Distributed Systems & Cloud — booking
6573. F6573 Algorithms & Theory of CS — beaver booking
6574. F6574 Distributed Systems & Cloud — room booking
6575. F6575 Mathematics — admission
6576. F6576 Data Mining & Databases — admission control
6577. F6577 Mathematics — outdoor
6578. F6578 Distributed Systems & Cloud — supporting file
6579. F6579 Mathematics — symmetric positive
6580. F6580 Curriculum-only — database treatment
6581. F6581 ML & AI — nri
6582. F6582 Mathematics — ecmo
6583. F6583 Computer Architecture — vdac
6584. F6584 Computer Networks — networkx
6585. F6585 ML & AI — rct
6586. F6586 Mathematics — comparison
6587. F6587 Algorithms & Theory of CS — comparison search lower bound
6588. F6588 Curriculum-only — comparison of attribute
6589. F6589 Curriculum-only — post-hoc comparison
6590. F6590 Distributed Systems & Cloud — comparison of cost
6591. F6591 Curriculum-only — comparison of cost and key size
6592. F6592 Distributed Systems & Cloud — su xes
6593. F6593 ML & AI — decision tree
6594. F6594 Algorithms & Theory of CS — binary decision trees
6595. F6595 Curriculum-only — decision table and decision tree
6596. F6596 Data Mining & Databases — classification rule
6597. F6597 ML & AI — support vector
6598. F6598 Curriculum-only — maximum-margin separator
6599. F6599 Mathematics — batcher
6600. F6600 Curriculum-only — principal value log
6601. F6601 Mathematics — limit
6602. F6602 HS Maths Class XII / Unit-III: Calculus — continuity and differentiability
6603. F6603 Algorithms & Theory of CS — graph limit
6604. F6604 Cryptography & Security — limit order
6605. F6605 Curriculum-only — accelerator-side limit
6606. F6606 Curriculum-only — limit on function length and nesting
6607. F6607 Data Mining & Databases — common-sense
6608. F6608 Information Theory & Coding — hop limit
6609. F6609 Mathematics — convergent series
6610. F6610 Mathematics — lim yn
6611. F6611 Curriculum-only — random variable as measurable function
6612. F6612 Mathematics — monotone sequence
6613. F6613 Curriculum-only — monotonic function and inverse function
6614. F6614 Mathematics — pointwise convergence
6615. F6615 Curriculum-only — cap theorem and its precise statement
6616. F6616 Mathematics — region ii
6617. F6617 Curriculum-only — rigorous pl
6618. F6618 Mathematics — round to nearest
6619. F6619 Algorithms & Theory of CS — finite metric space
6620. F6620 Curriculum-only — metric space and normed space
6621. F6621 Mathematics — arbitrary metric space
6622. F6622 Algorithms & Theory of CS — expansion ratio
6623. F6623 Mathematics — bounded and nonempty
6624. F6624 Curriculum-only — optimization over open set
6625. F6625 Mathematics — compact set
6626. F6626 Curriculum-only — slope and noise
6627. F6627 Mathematics — rubric
6628. F6628 Distributed Systems & Cloud — benchmark
6629. F6629 Curriculum-only — benchmark and pprof
6630. F6630 Data Mining & Databases — database benchmark
6631. F6631 Distributed Systems & Cloud — benchmark based
6632. F6632 Computer Architecture — Leveraging interrupts from hardware level: service routines and implementations. Example concepts
6633. F6633 Mathematics — transitivity
6634. F6634 Curriculum-only — chain transitivity
6635. F6635 Mathematics — twin prime
6636. F6636 HS Maths Class XI / Unit-I: Sets and Functions — trigonometric function
6637. F6637 Curriculum-only — angle and the trigonometric function
6638. F6638 Mathematics — row rank
6639. F6639 Algorithms & Theory of CS — splay
6640. F6640 Algorithms & Theory of CS — zig-zag product
6641. F6641 Computer Networks — out-degree
6642. F6642 Cryptography & Security — recession
6643. F6643 Curriculum-only — opt for the tour
6644. F6644 Data Mining & Databases — you're
6645. F6645 Distributed Systems & Cloud — strict totally ordered set
6646. F6646 Information Theory & Coding — voronoi constellation
6647. F6647 ML & AI — pair-wise comparison
6648. F6648 Data Mining & Databases — matrix concentration
6649. F6649 Mathematics — column rank
6650. F6650 Distributed Systems & Cloud — parallel fft
6651. F6651 Curriculum-only — key-value store like redis
6652. F6652 Distributed Systems & Cloud — reduce call
6653. F6653 Mathematics — convex function
6654. F6654 Algorithms & Theory of CS — log-concave
6655. F6655 Curriculum-only — convex function and their calculus
6656. F6656 ML & AI — chance constraint
6657. F6657 Mathematics — closed convex
6658. F6658 HS Maths Class XII / Unit-V: Linear Programming Problem — linear programming
6659. F6659 Curriculum-only — behind studying linear programming
6660. F6660 Data Mining & Databases — linear matrix inequalities
6661. F6661 ML & AI — support vector machine
6662. F6662 Mathematics — athena scientific
6663. F6663 Curriculum-only — condition for convexity
6664. F6664 Mathematics — closedness
6665. F6665 Curriculum-only — convex function with convex inequality constraint
6666. F6666 Mathematics — irn
6667. F6667 ML & AI — irm
6668. F6668 Mathematics — jensen
6669. F6669 Mathematics — minimize card
6670. F6670 ML & AI — negative orthant
6671. F6671 Mathematics — polyhedral set
6672. F6672 Curriculum-only — polyhedral set and cone
6673. F6673 Mathematics — extreme
6674. F6674 Curriculum-only — extreme point of linear programming
6675. F6675 Data Mining & Databases — Extreme weather
6676. F6676 Mathematics — extreme event
6677. F6677 Algorithms & Theory of CS — preferred child
6678. F6678 Mathematics — primal-dual
6679. F6679 Curriculum-only — primal-dual method for set cover
6680. F6680 Mathematics — programming and cvx
6681. F6681 Curriculum-only — chord ring
6682. F6682 Data Mining & Databases — adic
6683. F6683 Distributed Systems & Cloud — ring-based
6684. F6684 Information Theory & Coding — ring-oscillator
6685. F6685 Curriculum-only — ring-oscillator and sram puf
6686. F6686 Mathematics — commutative ring
6687. F6687 Curriculum-only — congruence and the ring zn
6688. F6688 Mathematics — schwarz
6689. F6689 Data Mining & Databases — complexity parameter
6690. F6690 Mathematics — nondegenerate self-concordant function
6691. F6691 Curriculum-only — singularity of an analytic function
6692. F6692 Mathematics — removable singularity
6693. F6693 Algorithms & Theory of CS — rooted tree
6694. F6694 Mathematics — square
6695. F6695 Algorithms & Theory of CS — an-1
6696. F6696 Computer Networks — epidemic model
6697. F6697 Cryptography & Security — modular square
6698. F6698 Curriculum-only — modular exponentiation by square-and-multiply
6699. F6699 Data Mining & Databases — number of row
6700. F6700 Mathematics — a2 t2
6701. F6701 Curriculum-only — gaussian projection matrix
6702. F6702 Mathematics — real square
6703. F6703 Computer Architecture — square root of lc
6704. F6704 Cryptography & Security — modular square root
6705. F6705 Data Mining & Databases — square root modulo
6706. F6706 Mathematics — carmichael
6707. F6707 Information Theory & Coding — prime subfield
6708. F6708 Mathematics — subject to card
6709. F6709 Curriculum-only — cone for constrained optimization
6710. F6710 Mathematics — chance constrained optimization
6711. F6711 ML & AI — davis
6712. F6712 Mathematics — taylor expansion
6713. F6713 Curriculum-only — taylor expansion in several variable
6714. F6714 Mathematics — theorem l4
6715. F6715 Curriculum-only — trapezoidal rule for evaluating
6716. F6716 Mathematics — trefethen
6717. F6717 Algorithms & Theory of CS — script to matlab
6718. F6718 Data Mining & Databases — scipy
6719. F6719 Curriculum-only — distribution in scipy
6720. F6720 Mathematics — eig
6721. F6721 Curriculum-only — rank-k truncation
6722. F6722 Mathematics — truncate
6723. F6723 Algorithms & Theory of CS — time in quote
6724. F6724 Curriculum-only — twice the limit across
6725. F6725 Mathematics — twice differentiable
6726. F6726 Curriculum-only — strongly convex rate
6727. F6727 ML & AI — strongly convex with respect
6728. F6728 Mathematics — distance to optimality
6729. F6729 Algorithms & Theory of CS — make-set
6730. F6730 Curriculum-only — linked-list version with weighted union
6731. F6731 Mathematics — complementation
6732. F6732 Information Theory & Coding — countable union of interval
6733. F6733 Mathematics — extension theorem
6734. F6734 Algorithms & Theory of CS — measure space
6735. F6735 Mathematics — counting measure
6736. F6736 Curriculum-only — monotone and dominated convergence
6737. F6737 Mathematics — fubini
6738. F6738 Curriculum-only — expectation as lebesgue integral
6739. F6739 Mathematics — integrable function
6740. F6740 Mathematics — smooth vectorfield
6741. F6741 Data Mining & Databases — local weak limit
6742. F6742 Mathematics — weak maximum principle
6743. F6743 NLP & Speech — acoustic-phonetic modeling
6744. F6744 Mathematics — feature
6745. F6745 Curriculum-only — feature of today cloud
6746. F6746 Data Mining & Databases — derived feature
6747. F6747 Distributed Systems & Cloud — feature detection
6748. F6748 Information Theory & Coding — feature geometry
6749. F6749 ML & AI — feature subset
6750. F6750 Curriculum-only — search over model and feature
6751. F6751 Mathematics — fictional
6752. F6752 Algorithms & Theory of CS — levin
6753. F6753 Computer Networks — garage
6754. F6754 Computer Architecture — garage door opener
6755. F6755 Curriculum-only — cook levin proof
6756. F6756 Mathematics — placing
6757. F6757 NLP & Speech — acoustic features
6758. F6758 Curriculum-only — dfs tree and articulation
6759. F6759 NLP & Speech — color features
6760. F6760 NLP & Speech — nominative
6761. F6761 Operating Systems — fixup
6762. F6762 Other/Unknown — Adversary models
6763. F6763 Other/Unknown — entailment
6764. F6764 Curriculum-only — approximation and local search
6765. F6765 Mathematics — neighborhood
6766. F6766 ML & AI — neighborhood graph
6767. F6767 Other/Unknown — mathematical modeling
6768. F6768 Data Mining & Databases — medical software
6769. F6769 Other/Unknown — medical device
6770. F6770 NLP & Speech — Multimodal input and output
6771. F6771 Other/Unknown — Multiscale modeling
6772. F6772 Curriculum-only — post-training quantisation
6773. F6773 Other/Unknown — product feature
6774. F6774 Curriculum-only — layered style
6775. F6775 Mathematics — dam
6776. F6776 Other/Unknown — rock mass
6777. F6777 Curriculum-only — sigma-field and monotone
6778. F6778 Other/Unknown — situ
6779. F6779 Curriculum-only — standard-model alternative
6780. F6780 Other/Unknown — treatment option
6781. F6781 Cryptography & Security — portal
6782. F6782 Curriculum-only — loopback tunnel
6783. F6783 Other/Unknown — walk model
6784. F6784 Data Mining & Databases — space and time
6785. F6785 Mathematics — absorbing
6786. F6786 Curriculum-only — absorbing chain
6787. F6787 Mathematics — absorbing material
6788. F6788 Other/Unknown — waveguide
6789. F6789 Mathematics — waveguide eigenproblem
6790. F6790 Other/Unknown — evanescent
6791. F6791 Mathematics — evanescent wave
6792. F6792 Other/Unknown — rectangular waveguides
6793. F6793 Signal/Image/Audio/Video Processing — albedo
6794. F6794 Signal/Image/Audio/Video Processing — finite measure
6795. F6795 NLP & Speech — spectral flatness
6796. F6796 Signal/Image/Audio/Video Processing — foraging behaviors
6797. F6797 Mathematics — forward euler rule
6798. F6798 HS Maths Class XII / Unit-I: Relations and Functions — inverse trigonometric function
6799. F6799 Curriculum-only — angle-difference formulas for sine
6800. F6800 ML & AI — leapfrog
6801. F6801 Mathematics — bn sin
6802. F6802 Algorithms & Theory of CS — knapsack
6803. F6803 Curriculum-only — approximation algorithm for the knapsack
6804. F6804 Mathematics — di erentiation
6805. F6805 Curriculum-only — sine and cosine as the real
6806. F6806 Mathematics — sine integral
6807. F6807 Other/Unknown — hyperbolic equations
6808. F6808 Signal/Image/Audio/Video Processing — Geometric Modeling
6809. F6809 Signal/Image/Audio/Video Processing — continuous linear mapping
6810. F6810 Curriculum-only — model compression and quantization
6811. F6811 Signal/Image/Audio/Video Processing — moment of random variable
6812. F6812 Curriculum-only — non-gaussian and non-linear case are named
6813. F6813 Signal/Image/Audio/Video Processing — observer performance
6814. F6814 Computer Architecture — periodic square
6815. F6815 Signal/Image/Audio/Video Processing — periodic square wave
6816. F6816 Software Engineering — allowable limit
6817. F6817 NLP & Speech — text categorization
6818. F6818 Software Engineering — cilk and reducer
6819. F6819 Curriculum-only — gradient flow for equality-constrained optimization
6820. F6820 Software Engineering — event model
6821. F6821 Curriculum-only — anomalous-curve exception
6822. F6822 Mathematics — raise
6823. F6823 Operating Systems — precise exception
6824. F6824 Curriculum-only — resulting precise-exception
6825. F6825 Operating Systems — tlb entry
6826. F6826 Software Engineering — dealing with exception
6827. F6827 Software Engineering — low level
6828. F6828 Mathematics — water
6829. F6829 Curriculum-only — write it water fall model
6830. F6830 Mathematics — cooler
6831. F6831 Data Mining & Databases — refrigerator
6832. F6832 NLP & Speech — caplan water
6833. F6833 Other/Unknown — network design
6834. F6834 Mathematics — construct
6835. F6835 Algorithms & Theory of CS — decide acctm
6836. F6836 Algorithms & Theory of CS — x2 mod
6837. F6837 Curriculum-only — approximation algorithm for the vertex cover
6838. F6838 Data Mining & Databases — systolic
6839. F6839 Distributed Systems & Cloud — linear systolic array
6840. F6840 Information Theory & Coding — shannon
6841. F6841 Curriculum-only — jensen shannon
6842. F6842 Information Theory & Coding — memoryless channel
6843. F6843 ML & AI — scv
6844. F6844 Algorithms & Theory of CS — suffix tree
6845. F6845 Computer Networks — strong connectivity
6846. F6846 Cryptography & Security — hash
6847. F6847 Algorithms & Theory of CS — hash family
6848. F6848 Computer Networks — hash-based
6849. F6849 Cryptography & Security — attack on hash
6850. F6850 Cryptography & Security — keyed hash function
6851. F6851 Curriculum-only — collision-resistance reduction
6852. F6852 Curriculum-only — rabin and elgamal
6853. F6853 Data Mining & Databases — hash tree
6854. F6854 Curriculum-only — model to transaction processing
6855. F6855 Data Mining & Databases — web-based information system
6856. F6856 Distributed Systems & Cloud — webgraph and implementation
6857. F6857 Information Theory & Coding — soft
6858. F6858 Curriculum-only — soft margin
6859. F6859 Distributed Systems & Cloud — fuzziness and soft
6860. F6860 Information Theory & Coding — hard and soft
6861. F6861 Mathematics — arguably
6862. F6862 Curriculum-only — existential unforgeability under chosen-message attack
6863. F6863 Mathematics — k1 and k2
6864. F6864 Algorithms & Theory of CS — order logic
6865. F6865 Curriculum-only — discrete reasoning
6866. F6866 Distributed Systems & Cloud — algorithm description
6867. F6867 Mathematics — briefly explain
6868. F6868 Algorithms & Theory of CS — gauss space
6869. F6869 Curriculum-only — normal and binormal
6870. F6870 Data Mining & Databases — back to normal
6871. F6871 Information Theory & Coding — normal graph
6872. F6872 Mathematics — characteristically normal
6873. F6873 Mathematics — normal derivative
6874. F6874 Algorithms & Theory of CS — conjunctive normal form
6875. F6875 Curriculum-only — boyce codd normal form
6876. F6876 Mathematics — normal form of green
6877. F6877 Algorithms & Theory of CS — constraint satisfaction
6878. F6878 Mathematics — sorting network
6879. F6879 Curriculum-only — normal and log-normal distribution
6880. F6880 Mathematics — multidimensional normal distribution
6881. F6881 Curriculum-only — covariance and multivariate normal
6882. F6882 Data Mining & Databases — multivariate normal distribution
6883. F6883 Mathematics — covariance matrix
6884. F6884 Curriculum-only — sample geometry and covariance matrix
6885. F6885 Information Theory & Coding — gaussian variable
6886. F6886 ML & AI — gaussian vector
6887. F6887 Mathematics — one-parameter
6888. F6888 Curriculum-only — cis benchmark
6889. F6889 Mathematics — stays
6890. F6890 NLP & Speech — fusion
6891. F6891 Curriculum-only — operator fusion
6892. F6892 Data Mining & Databases — decision fusion
6893. F6893 NLP & Speech — rhythm
6894. F6894 Other/Unknown — data fusion
6895. F6895 Curriculum-only — partial and total correctness
6896. F6896 Other/Unknown — water resource
6897. F6897 Curriculum-only — hydrology and water-resource
6898. F6898 Other/Unknown — water-resource engineering
6899. F6899 Signal/Image/Audio/Video Processing — normal sinus rhythm
6900. F6900 Software Engineering — design
6901. F6901 Algorithms & Theory of CS — design and optimisation
6902. F6902 Computer Architecture — control design
6903. F6903 Computer Networks — cooperative game
6904. F6904 Algorithms & Theory of CS — noncooperative game
6905. F6905 Computer Networks — correct design
6906. F6906 Cryptography & Security — value proposition
6907. F6907 Curriculum-only — always-writable design
6908. F6908 Curriculum-only — design documented
6909. F6909 Curriculum-only — function-oriented design
6910. F6910 Curriculum-only — relational algebra session of database design
6911. F6911 Data Mining & Databases — automobile
6912. F6912 Distributed Systems & Cloud — algorithm design in map-reduce
6913. F6913 ML & AI — facade
6914. F6914 Mathematics — computer arithmetic
6915. F6915 Algorithms & Theory of CS — additional material
6916. F6916 Computer Architecture — quality factor
6917. F6917 Computer Networks — data quality
6918. F6918 Curriculum-only — data quality and cost control
6919. F6919 Data Mining & Databases — donation
6920. F6920 Distributed Systems & Cloud — high quality journal
6921. F6921 Mathematics — image quality
6922. F6922 Curriculum-only — seam for testing shape design
6923. F6923 Data Mining & Databases — blob
6924. F6924 Mathematics — stretching
6925. F6925 Curriculum-only — key stretching
6926. F6926 Mathematics — coordinate stretching
6927. F6927 Operating Systems — ability to design
6928. F6928 Other/Unknown — air quality
6929. F6929 Curriculum-only — grad-cam
6930. F6930 Other/Unknown — automotive
6931. F6931 Other/Unknown — mechanism design
6932. F6932 Curriculum-only — decoding into micro-operation
6933. F6933 Other/Unknown — micro and nano
6934. F6934 Distributed Systems & Cloud — processing
6935. F6935 Algorithms & Theory of CS — algorithm for efficient processing
6936. F6936 Computer Architecture — processing-in-memory
6937. F6937 Cryptography & Security — word processing
6938. F6938 Curriculum-only — fragment processing
6939. F6939 Data Mining & Databases — query processing
6940. F6940 Curriculum-only — query transformation
6941. F6941 Data Mining & Databases — Parallel Query Processing (e.g., parallel scan, parallel join, parallel aggregation)
6942. F6942 Distributed Systems & Cloud — graph processing
6943. F6943 Curriculum-only — compute device made of compute unit made of processing element
6944. F6944 Distributed Systems & Cloud — processing volume
6945. F6945 Information Theory & Coding — source of delay
6946. F6946 Mathematics — audio processing
6947. F6947 Algorithms & Theory of CS — simplex algorithm
6948. F6948 Curriculum-only — foundation of simplex
6949. F6949 Information Theory & Coding — simplex signal set
6950. F6950 ML & AI — intermediate simplex
6951. F6951 Mathematics — feasible region
6952. F6952 Algorithms & Theory of CS — am2
6953. F6953 Cryptography & Security — generic function
6954. F6954 Curriculum-only — generic function and type
6955. F6955 Data Mining & Databases — logics
6956. F6956 Curriculum-only — propositional logics
6957. F6957 Data Mining & Databases — sums-of-square interpretation
6958. F6958 ML & AI — compositionality
6959. F6959 Mathematics — combinatorial interpretation
6960. F6960 Curriculum-only — partial derivative and their geometrical interpretation
6961. F6961 Mathematics — non-euclidean interpretation
6962. F6962 Curriculum-only — test level as the right-hand side of the v-model
6963. F6963 Mathematics — holomorphic
6964. F6964 Data Mining & Databases — holomorphic map
6965. F6965 ML & AI — rez
6966. F6966 Mathematics — analytic continuation
6967. F6967 Curriculum-only — shadow page table
6968. F6968 Distributed Systems & Cloud — shadow paging
6969. F6969 Mathematics — shadow constraint
6970. F6970 Data Mining & Databases — differential slack
6971. F6971 Mathematics — slack variable
6972. F6972 Algorithms & Theory of CS — subset sum variant
6973. F6973 Computer Networks — sql variant
6974. F6974 Curriculum-only — authenticated variant
6975. F6975 Distributed Systems & Cloud — tree variant
6976. F6976 Mathematics — bear attack
6977. F6977 Data Mining & Databases — constant x1 x2 x3
6978. F6978 Mathematics — z1 z2
6979. F6979 NLP & Speech — memory load
6980. F6980 Operating Systems — setstate
6981. F6981 Other/Unknown — complementarity
6982. F6982 Curriculum-only — complementarity problem and algorithm
6983. F6983 Other/Unknown — interpretation for pl
6984. F6984 Curriculum-only — query processing and optimization
6985. F6985 Other/Unknown — quality models
6986. F6986 Mathematics — cutting
6987. F6987 Other/Unknown — cutting forces
6988. F6988 Mathematics — energy
6989. F6989 Computer Architecture — dynamic energy
6990. F6990 Curriculum-only — constraint on energy
6991. F6991 Data Mining & Databases — energy crisis
6992. F6992 Information Theory & Coding — electric field
6993. F6993 ML & AI — energy interpretation
6994. F6994 Mathematics — absence
6995. F6995 Curriculum-only — proving the absence of fault
6996. F6996 Mathematics — energy estimate
6997. F6997 Curriculum-only — linear first-order equation
6998. F6998 Mathematics — companion
6999. F6999 Mathematics — spherical mean
7000. F7000 Other/Unknown — Energy level
7001. F7001 Other/Unknown — structural
7002. F7002 Computer Architecture — structural description
7003. F7003 Distributed Systems & Cloud — structural operator
7004. F7004 Mathematics — raf
7005. F7005 Other/Unknown — concrete structure
7006. F7006 Mathematics — steel
7007. F7007 Curriculum-only — heavy-write cost
7008. F7008 Information Theory & Coding — heavy tail
7009. F7009 Other/Unknown — protein folding
7010. F7010 Computer Networks — distribution center
7011. F7011 Curriculum-only — key-distribution centre
7012. F7012 Other/Unknown — demand forecasting
7013. F7013 Computer Networks — chemical inventory
7014. F7014 Curriculum-only — cryptographic inventory
7015. F7015 Mathematics — inventory level
7016. F7016 Other/Unknown — transportation planning
7017. F7017 Curriculum-only — conservation of vehicle at every junction
7018. F7018 Data Mining & Databases — motor vehicle theft
7019. F7019 Distributed Systems & Cloud — vehicle control
7020. F7020 Other/Unknown — electric vehicle
7021. F7021 Signal/Image/Audio/Video Processing — a-c
7022. F7022 Curriculum-only — information-theoretic secure mac
7023. F7023 Signal/Image/Audio/Video Processing — neural processing
7024. F7024 Curriculum-only — z-step is soft thresholding
7025. F7025 Signal/Image/Audio/Video Processing — segmentation
7026. F7026 Curriculum-only — network segmentation
7027. F7027 Data Mining & Databases — customer segmentation
7028. F7028 Mathematics — grouping
7029. F7029 Information Theory & Coding — huffman
7030. F7030 Distributed Systems & Cloud — acknowledgment
7031. F7031 Curriculum-only — cumulative acknowledgment
7032. F7032 Distributed Systems & Cloud — round-trip time
7033. F7033 Information Theory & Coding — decodable
7034. F7034 Curriculum-only — prefix-free fix
7035. F7035 Information Theory & Coding — prefix-free code
7036. F7036 Mathematics — loss
7037. F7037 Curriculum-only — annualised loss expectancy
7038. F7038 Information Theory & Coding — hearing loss
7039. F7039 Curriculum-only — henry kafura information-flow measure
7040. F7040 Information Theory & Coding — input probability
7041. F7041 ML & AI — exp yt
7042. F7042 Information Theory & Coding — ensemble
7043. F7043 Curriculum-only — building an ensemble model
7044. F7044 ML & AI — exponential weight
7045. F7045 Mathematics — feedback
7046. F7046 Computer Architecture — user feedback
7047. F7047 Computer Networks — feedback scheme
7048. F7048 Cryptography & Security — linear feedback
7049. F7049 Curriculum-only — ai-feedback
7050. F7050 Information Theory & Coding — channel coding with feedback
7051. F7051 Mathematics — bode
7052. F7052 Curriculum-only — lagrange mvt
7053. F7053 Mathematics — duality
7054. F7054 Curriculum-only — column space row space duality
7055. F7055 Data Mining & Databases — convex duality
7056. F7056 Mathematics — complementary slackness
7057. F7057 Curriculum-only — duality and complementary slackness
7058. F7058 Mathematics — convex programming
7059. F7059 Algorithms & Theory of CS — bty
7060. F7060 Mathematics — disciplined
7061. F7061 Curriculum-only — lagrange multiplier on surface
7062. F7062 Mathematics — lagrangian duality
7063. F7063 Curriculum-only — kkt condition and primal
7064. F7064 Mathematics — normalized
7065. F7065 Data Mining & Databases — normalized function
7066. F7066 Information Theory & Coding — normalized rate
7067. F7067 ML & AI — shi
7068. F7068 Mathematics — optimality condition
7069. F7069 Curriculum-only — first-order kkt sufficient optimality condition
7070. F7070 Data Mining & Databases — first-order optimality condition
7071. F7071 Mathematics — feasibility
7072. F7072 Curriculum-only — geometric interpretation of duality
7073. F7073 Mathematics — necessary and sufficient
7074. F7074 Curriculum-only — second-order kkt necessary and sufficient condition
7075. F7075 Mathematics — p1 p2
7076. F7076 Information Theory & Coding — generator matrix
7077. F7077 Mathematics — primal and dual
7078. F7078 Curriculum-only — duality theory and strong duality
7079. F7079 Mathematics — dual optimal
7080. F7080 Curriculum-only — factorization theorem for sufficiency
7081. F7081 Mathematics — symmetric binary channel
7082. F7082 Information Theory & Coding — information measure
7083. F7083 Mathematics — saddle
7084. F7084 Operating Systems — feedback forms
7085. F7085 Other/Unknown — Ensemble learning
7086. F7086 Curriculum-only — convex optimization and nonlinear programming
7087. F7087 Mathematics — constraint qualification
7088. F7088 Curriculum-only — slater constraint qualification imply strong duality
7089. F7089 Mathematics — wolfe
7090. F7090 Curriculum-only — wolfe powell
7091. F7091 Mathematics — quadratic program
7092. F7092 Other/Unknown — open system
7093. F7093 Curriculum-only — maintenance process model
7094. F7094 Other/Unknown — controller
7095. F7095 Computer Architecture — game controller
7096. F7096 Curriculum-only — controller cluster
7097. F7097 Distributed Systems & Cloud — interrupt controller
7098. F7098 Mathematics — controller to meet
7099. F7099 Other/Unknown — controller design
7100. F7100 Signal/Image/Audio/Video Processing — em segmentation
7101. F7101 Curriculum-only — cnn-based segmentation algorithm
7102. F7102 Signal/Image/Audio/Video Processing — signal ensemble for outcome
7103. F7103 Mathematics — feedback loop
7104. F7104 Distributed Systems & Cloud — sensor
7105. F7105 Computer Architecture — infra-red sensor
7106. F7106 Curriculum-only — explosion of data generated by sensor
7107. F7107 Distributed Systems & Cloud — sensor and mesh
7108. F7108 Information Theory & Coding — contention window
7109. F7109 ML & AI — gauge
7110. F7110 Mathematics — sensor quantization
7111. F7111 Other/Unknown — acoustic sensors
7112. F7112 Distributed Systems & Cloud — Computational chemistry
7113. F7113 Other/Unknown — coordination
7114. F7114 Computer Networks — coordination game
7115. F7115 Curriculum-only — coordination of work
7116. F7116 Distributed Systems & Cloud — coordination algorithm
7117. F7117 Operating Systems — lock-free coordination
7118. F7118 Other/Unknown — ion bombardment
7119. F7119 Computer Architecture — ram1 mem
7120. F7120 Other/Unknown — mems design
7121. F7121 Information Theory & Coding — tage
7122. F7122 Curriculum-only — tage and perceptron predictor
7123. F7123 ML & AI — frozen
7124. F7124 Curriculum-only — frozen distribution
7125. F7125 Other/Unknown — physical chemistry
7126. F7126 Signal/Image/Audio/Video Processing — sensor delays
7127. F7127 Software Engineering — architectural design
7128. F7128 Curriculum-only — builder object receive parameter
7129. F7129 Distributed Systems & Cloud — graph builder
7130. F7130 Mathematics — set builder
7131. F7131 Software Engineering — coordination mechanisms
7132. F7132 Software Engineering — design pattern
7133. F7133 Curriculum-only — book design pattern
7134. F7134 Distributed Systems & Cloud — distributed
7135. F7135 Computer Architecture — write-behind
7136. F7136 Computer Networks — distributed computer systems
7137. F7137 Cryptography & Security — distributed and replicated
7138. F7138 Curriculum-only — distributed asynchronous bellman ford
7139. F7139 Curriculum-only — zipf-distributed access
7140. F7140 Data Mining & Databases — distributed query
7141. F7141 Distributed Systems & Cloud — apis
7142. F7142 Curriculum-only — enabling apis
7143. F7143 Distributed Systems & Cloud — attiya
7144. F7144 Curriculum-only — bittorrent dht
7145. F7145 Distributed Systems & Cloud — cassandra
7146. F7146 Curriculum-only — lelann chang robert
7147. F7147 Distributed Systems & Cloud — consistency level in cassandra
7148. F7148 Curriculum-only — query processing in distributed database
7149. F7149 Distributed Systems & Cloud — distributed deadlock detection
7150. F7150 Distributed Systems & Cloud — distributed resource
7151. F7151 Curriculum-only — liskov substitution
7152. F7152 Distributed Systems & Cloud — mutual exclusion
7153. F7153 Curriculum-only — mutual exclusion with lease in industry
7154. F7154 Distributed Systems & Cloud — distributed mutual
7155. F7155 Computer Networks — traffic
7156. F7156 Curriculum-only — heavy-tail traffic
7157. F7157 Data Mining & Databases — craig
7158. F7158 Distributed Systems & Cloud — replicated data
7159. F7159 Curriculum-only — convergent replicated data type
7160. F7160 Distributed Systems & Cloud — conflict-free replicated data type
7161. F7161 Algorithms & Theory of CS — fischer
7162. F7162 Curriculum-only — fischer lynch paterson
7163. F7163 Distributed Systems & Cloud — shared-nothing
7164. F7164 Information Theory & Coding — distributed compression
7165. F7165 Distributed Systems & Cloud — subject name distributed system
7166. F7166 Information Theory & Coding — traffic shaping
7167. F7167 ML & AI — parallel distributed
7168. F7168 Mathematics — allison chang
7169. F7169 Data Mining & Databases — mann whitney
7170. F7170 Distributed Systems & Cloud — timothy mann
7171. F7171 Mathematics — replace
7172. F7172 Curriculum-only — curriculum replace
7173. F7173 Mathematics — replace with negative
7174. F7174 Algorithms & Theory of CS — smallest cut
7175. F7175 Algorithms & Theory of CS — independently and uniformly
7176. F7176 Algorithms & Theory of CS — vertex coloring
7177. F7177 Computer Architecture — traffic light controller
7178. F7178 Curriculum-only — forest version with union by rank
7179. F7179 Distributed Systems & Cloud — convergecast
7180. F7180 Algorithms & Theory of CS — bfs tree
7181. F7181 Distributed Systems & Cloud — rooted spanning tree
7182. F7182 Information Theory & Coding — minimum weight outgoing edge
7183. F7183 Distributed Systems & Cloud — initiate
7184. F7184 Curriculum-only — dma and interrupt
7185. F7185 Data Mining & Databases — data size
7186. F7186 Distributed Systems & Cloud — dma and computation
7187. F7187 Information Theory & Coding — spanning set
7188. F7188 Mathematics — affine plane
7189. F7189 Algorithms & Theory of CS — brook theorem
7190. F7190 Curriculum-only — brook theorem stated
7191. F7191 Mathematics — min-weight
7192. F7192 Algorithms & Theory of CS — acyclic orientation
7193. F7193 Algorithms & Theory of CS — knot theory
7194. F7194 Algorithms & Theory of CS — polynomial space
7195. F7195 Algorithms & Theory of CS — time hierarchy theorem
7196. F7196 Cryptography & Security — probabilistic polynomial size
7197. F7197 Curriculum-only — feedback polynomial
7198. F7198 Curriculum-only — worst-case polynomial algorithm
7199. F7199 Data Mining & Databases — euclidean division
7200. F7200 Algorithms & Theory of CS — read-only input
7201. F7201 Curriculum-only — read only of committed data
7202. F7202 Distributed Systems & Cloud — goldberg
7203. F7203 Algorithms & Theory of CS — goldberg-tarjan min-cost circulation algorithm
7204. F7204 Distributed Systems & Cloud — goldberg theorem
7205. F7205 Computer Architecture — count internal
7206. F7206 Computer Networks — internal network
7207. F7207 Curriculum-only — internal level
7208. F7208 Data Mining & Databases — arrogant
7209. F7209 Distributed Systems & Cloud — map-reduce internal
7210. F7210 Curriculum-only — type and the popek goldberg theorem
7211. F7211 Information Theory & Coding — internal edge
7212. F7212 ML & AI — local optima
7213. F7213 Curriculum-only — local optima and its variant
7214. F7214 ML & AI — polynomial family
7215. F7215 Curriculum-only — inverse and pseudo-inverse
7216. F7216 Mathematics — ai xi
7217. F7217 Mathematics — easy to verify
7218. F7218 Algorithms & Theory of CS — winning strategy
7219. F7219 Mathematics — Injective function
7220. F7220 ML & AI — sft
7221. F7221 Mathematics — chebyshev interpolant
7222. F7222 Curriculum-only — counting monomial
7223. F7223 Mathematics — nonnegative polynomial
7224. F7224 Curriculum-only — ideal scenario
7225. F7225 Data Mining & Databases — homogeneous ideal
7226. F7226 ML & AI — ascending chain of ideal
7227. F7227 Mathematics — fraction field
7228. F7228 Curriculum-only — ideal and integral domain
7229. F7229 Mathematics — maximal
7230. F7230 Curriculum-only — direction of maximal variance
7231. F7231 Data Mining & Databases — maximal matching
7232. F7232 Information Theory & Coding — zero-error capacity
7233. F7233 Mathematics — maximal ideal
7234. F7234 Data Mining & Databases — uniformizer
7235. F7235 Mathematics — maximal inequality
7236. F7236 Curriculum-only — doob maximal inequality
7237. F7237 Mathematics — polynomial rule
7238. F7238 Distributed Systems & Cloud — pos addr
7239. F7239 Mathematics — positive degree
7240. F7240 Cryptography & Security — mediation
7241. F7241 Curriculum-only — data principal
7242. F7242 Data Mining & Databases — value of log
7243. F7243 Distributed Systems & Cloud — principal ideal domain
7244. F7244 Data Mining & Databases — discrete valuation ring
7245. F7245 Mathematics — principal branch
7246. F7246 Curriculum-only — quadratic formula and the discriminant
7247. F7247 Mathematics — quadratic polynomial
7248. F7248 Mathematics — trapezoid
7249. F7249 Information Theory & Coding — prime polynomial
7250. F7250 Mathematics — number of prime
7251. F7251 Information Theory & Coding — stream
7252. F7252 Curriculum-only — click stream
7253. F7253 Data Mining & Databases — stream data
7254. F7254 Distributed Systems & Cloud — discretized stream
7255. F7255 Information Theory & Coding — byte stream
7256. F7256 Curriculum-only — byte-stream service
7257. F7257 ML & AI — ventral stream
7258. F7258 Mathematics — field sieve
7259. F7259 Curriculum-only — wallace and dadda tree reduction
7260. F7260 Mathematics — department
7261. F7261 Cryptography & Security — micali
7262. F7262 Curriculum-only — blum micali
7263. F7263 Distributed Systems & Cloud — engineering department
7264. F7264 Mathematics — wallace vander velde
7265. F7265 NLP & Speech — medial
7266. F7266 Algorithms & Theory of CS — medial graph
7267. F7267 Operating Systems — major internal
7268. F7268 Other/Unknown — annihilating polynomial
7269. F7269 Mathematics — correlation function rxx
7270. F7270 Other/Unknown — cross-correlation function
7271. F7271 Curriculum-only — discrete and continuous dynamical system
7272. F7272 Other/Unknown — distributed energy resources
7273. F7273 Curriculum-only — host-only
7274. F7274 Distributed Systems & Cloud — host language
7275. F7275 Other/Unknown — ideal chain
7276. F7276 Signal/Image/Audio/Video Processing — gk1
7277. F7277 Software Engineering — air traffic controller
7278. F7278 Software Engineering — immutability
7279. F7279 Distributed Systems & Cloud — paper
7280. F7280 Computer Networks — number to call
7281. F7281 Cryptography & Security — brumley
7282. F7282 Curriculum-only — primary paper
7283. F7283 Data Mining & Databases — influential
7284. F7284 Curriculum-only — influential point and cook distance
7285. F7285 Data Mining & Databases — pencil
7286. F7286 Distributed Systems & Cloud — authored paper in ieee
7287. F7287 Algorithms & Theory of CS — asynchronous distributed algorithm
7288. F7288 Curriculum-only — distributed algorithm for failure
7289. F7289 Distributed Systems & Cloud — describe distributed algorithm
7290. F7290 Curriculum-only — leader election problem statement
7291. F7291 Distributed Systems & Cloud — asynchronous network
7292. F7292 Curriculum-only — gallager humblet spira
7293. F7293 Distributed Systems & Cloud — gallager humblet spira algorithm
7294. F7294 Mathematics — approximate
7295. F7295 Algorithms & Theory of CS — set of quantum gate
7296. F7296 Curriculum-only — approximate algorithm
7297. F7297 Data Mining & Databases — approximate search
7298. F7298 ML & AI — frobenius norm
7299. F7299 Mathematics — approximate percentage
7300. F7300 Curriculum-only — kerberos-style ticket
7301. F7301 Mathematics — purchase
7302. F7302 Computer Networks — payable
7303. F7303 Curriculum-only — purchase over time
7304. F7304 NLP & Speech — approximate map
7305. F7305 Operating Systems — bakery algorithm
7306. F7306 Other/Unknown — boundary element
7307. F7307 Signal/Image/Audio/Video Processing — approximate identity
7308. F7308 Software Engineering — current value
7309. F7309 Operating Systems — early interim report
7310. F7310 Software Engineering — lagrangian dual
7311. F7311 Curriculum-only — primal and lagrangian dual
7312. F7312 Software Engineering — local reasoning
7313. F7313 Data Mining & Databases — macro-f measure
7314. F7314 Software Engineering — follower
7315. F7315 Computer Architecture — source follower
7316. F7316 Software Engineering — macro de nition
7317. F7317 Mathematics — centering
7318. F7318 Software Engineering — model and process
7319. F7319 Curriculum-only — optionally out of order
7320. F7320 Software Engineering — password hash
7321. F7321 Computer Architecture — state and memory
7322. F7322 Curriculum-only — kruskal and prim
7323. F7323 Data Mining & Databases — trec
7324. F7324 Distributed Systems & Cloud — shared-memory programming
7325. F7325 Signal/Image/Audio/Video Processing — scene
7326. F7326 Data Mining & Databases — pedestrian detection
7327. F7327 Mathematics — company
7328. F7328 Curriculum-only — company engineering blog the primer list
7329. F7329 Data Mining & Databases — Age II (Early modern computing): ENIAC, UNIVAC, Bombes (Bletchley Park and codebreakers), computer companies (e.g., IBM), mainframes, etc
7330. F7330 Mathematics — employee
7331. F7331 Curriculum-only — employee with operator
7332. F7332 Signal/Image/Audio/Video Processing — Scene understanding
7333. F7333 Software Engineering — processing algorithm
7334. F7334 Distributed Systems & Cloud — generated in production system
7335. F7335 Software Engineering — Program constructs
7336. F7336 Curriculum-only — latency number every programmer
7337. F7337 Data Mining & Databases — python programmer
7338. F7338 Software Engineering — ps4
7339. F7339 Algorithms & Theory of CS — solving recurrence
7340. F7340 Curriculum-only — divide-and-conquer recursion of the fft
7341. F7341 Data Mining & Databases — recursion theory
7342. F7342 Mathematics — lik
7343. F7343 Software Engineering — recursive function
7344. F7344 Data Mining & Databases — partial recursive function
7345. F7345 Software Engineering — relational calculus
7346. F7346 Curriculum-only — domain relational calculus
7347. F7347 Software Engineering — reliability modeling
7348. F7348 Curriculum-only — rtt replay risk
7349. F7349 Software Engineering — restful apis
7350. F7350 Distributed Systems & Cloud — efficient execution
7351. F7351 Mathematics — abase
7352. F7352 Data Mining & Databases — reservoir
7353. F7353 Distributed Systems & Cloud — storage
7354. F7354 Algorithms & Theory of CS — password storage
7355. F7355 Computer Architecture — storage nodes
7356. F7356 Computer Networks — stable storage
7357. F7357 Curriculum-only — columnar storage
7358. F7358 Data Mining & Databases — amount of data
7359. F7359 Distributed Systems & Cloud — block storage
7360. F7360 Computer Networks — persistent connection
7361. F7361 Curriculum-only — persistent connection and pipelining
7362. F7362 Distributed Systems & Cloud — runtime and storage
7363. F7363 Curriculum-only — storage hierarchy and stable storage
7364. F7364 Distributed Systems & Cloud — storage system
7365. F7365 Curriculum-only — primary storage system
7366. F7366 Distributed Systems & Cloud — virtual storage
7367. F7367 Mathematics — digital storage
7368. F7368 Algorithms & Theory of CS — knowledge of algorithm
7369. F7369 Cryptography & Security — commitment scheme
7370. F7370 Curriculum-only — intimate knowledge of how thing work
7371. F7371 Data Mining & Databases — knowledge to explore
7372. F7372 Distributed Systems & Cloud — knowledge in programming
7373. F7373 Information Theory & Coding — information storage
7374. F7374 ML & AI — commonsense knowledge
7375. F7375 Mathematics — external site
7376. F7376 Curriculum-only — morera theorem
7377. F7377 Mathematics — real analysis
7378. F7378 Curriculum-only — optimization overview of real analysis
7379. F7379 Mathematics — complex analysis
7380. F7380 Curriculum-only — fourier and complex analysis
7381. F7381 Mathematics — analytic number theory
7382. F7382 Algorithms & Theory of CS — paley
7383. F7383 Mathematics — cauchy residue
7384. F7384 Curriculum-only — legendre and jacobi symbol
7385. F7385 Mathematics — legendre symbol
7386. F7386 Curriculum-only — gauss lemma for the legendre symbol
7387. F7387 Mathematics — prime congruent
7388. F7388 Data Mining & Databases — dirichlet series
7389. F7389 Mathematics — euler product
7390. F7390 Curriculum-only — countable and uncountable infinity
7391. F7391 Mathematics — sharing knowledge
7392. F7392 Curriculum-only — taylor and laurent series
7393. F7393 Mathematics — residue theorem
7394. F7394 Operating Systems — durable storage
7395. F7395 Curriculum-only — half storage structure
7396. F7396 Operating Systems — data storage structure
7397. F7397 Computer Architecture — ttl
7398. F7398 Computer Networks — scaling ip
7399. F7399 Cryptography & Security — possible pad byte
7400. F7400 Curriculum-only — caching and ttl
7401. F7401 Data Mining & Databases — shared disk
7402. F7402 Distributed Systems & Cloud — tcl
7403. F7403 Algorithms & Theory of CS — configuration
7404. F7404 Curriculum-only — configuration from the environment
7405. F7405 Distributed Systems & Cloud — namd configuration
7406. F7406 ML & AI — map configuration
7407. F7407 Algorithms & Theory of CS — configuration space
7408. F7408 ML & AI — spam
7409. F7409 Computer Networks — spam message
7410. F7410 Data Mining & Databases — spammer
7411. F7411 ML & AI — spam
7412. F7412 Mathematics — checking
7413. F7413 Distributed Systems & Cloud — constraint satisfaction problem
7414. F7414 Mathematics — configuration design
7415. F7415 Curriculum-only — order in which column are placed
7416. F7416 Mathematics — ant
7417. F7417 NLP & Speech — upper saddle river
7418. F7418 Operating Systems — bound checking
7419. F7419 Cryptography & Security — baggy bound checking
7420. F7420 Operating Systems — unicast
7421. F7421 Distributed Systems & Cloud — sleeping
7422. F7422 Mathematics — sheet
7423. F7423 Computer Networks — style sheet
7424. F7424 Operating Systems — atomic instruction
7425. F7425 Other/Unknown — acquisition
7426. F7426 Computer Architecture — acquisition process
7427. F7427 Cryptography & Security — fingerprint
7428. F7428 Computer Architecture — fingerprint images
7429. F7429 Curriculum-only — audio fingerprint are named
7430. F7430 NLP & Speech — knowledge acquisition
7431. F7431 Other/Unknown — acquisition system
7432. F7432 Algorithms & Theory of CS — confluent persistence
7433. F7433 Curriculum-only — persistence at the level of detection
7434. F7434 Other/Unknown — prior knowledge
7435. F7435 Cryptography & Security — network propagation
7436. F7436 Curriculum-only — network propagation and action on objective
7437. F7437 Information Theory & Coding — propagation delay
7438. F7438 Mathematics — time propagation
7439. F7439 NLP & Speech — propagation velocity
7440. F7440 Other/Unknown — light propagation
7441. F7441 Mathematics — reflection
7442. F7442 Curriculum-only — reflection in the line
7443. F7443 Mathematics — computational region
7444. F7444 Cryptography & Security — number field sieve
7445. F7445 Mathematics — arbitrary number
7446. F7446 Curriculum-only — cyclic prefix
7447. F7447 Data Mining & Databases — cyclic graph
7448. F7448 Information Theory & Coding — bose chaudhuri hocquenhem
7449. F7449 Mathematics — dihedral
7450. F7450 Algorithms & Theory of CS — cayley graph
7451. F7451 Mathematics — multiplicative group
7452. F7452 Operating Systems — reflection attack
7453. F7453 Curriculum-only — replay and reflection attack
7454. F7454 Other/Unknown — algebraic number theory
7455. F7455 Curriculum-only — run formation by sorting
7456. F7456 Data Mining & Databases — plan formation
7457. F7457 Other/Unknown — chip formations
7458. F7458 Signal/Image/Audio/Video Processing — cyclic signal path
7459. F7459 Curriculum-only — fourier integral and fourier transform
7460. F7460 Mathematics — summation formula
7461. F7461 Signal/Image/Audio/Video Processing — fourier transform on l1
7462. F7462 Mathematics — center of projection
7463. F7463 Other/Unknown — camera geometry
7464. F7464 Signal/Image/Audio/Video Processing — foreshortening
7465. F7465 Other/Unknown — radiation
7466. F7466 Information Theory & Coding — radiation impedance
7467. F7467 Other/Unknown — antenna radiation
7468. F7468 Mathematics — radiation therapy
7469. F7469 Other/Unknown — phase change
7470. F7470 Computer Networks — zone transfer
7471. F7471 Curriculum-only — demilitarised zone
7472. F7472 Other/Unknown — fracture
7473. F7473 Signal/Image/Audio/Video Processing — observer configuration
7474. F7474 Mathematics — interior
7475. F7475 Curriculum-only — convex set and normal cone
7476. F7476 Mathematics — relative interior
7477. F7477 Software Engineering — algebraic identity
7478. F7478 Distributed Systems & Cloud — namd configuration file
7479. F7479 Software Engineering — constant propagation
7480. F7480 Computer Networks — temporary directory
7481. F7481 Cryptography & Security — directory service
7482. F7482 Curriculum-only — directory system
7483. F7483 Distributed Systems & Cloud — emac
7484. F7484 Mathematics — copy
7485. F7485 Algorithms & Theory of CS — copy forward
7486. F7486 Computer Networks — mgr
7487. F7487 Curriculum-only — code to copy
7488. F7488 Data Mining & Databases — old list
7489. F7489 Distributed Systems & Cloud — post-copy
7490. F7490 Information Theory & Coding — parity
7491. F7491 Curriculum-only — demographic parity
7492. F7492 Information Theory & Coding — correcting
7493. F7493 ML & AI — noisy parity
7494. F7494 Mathematics — error correction code
7495. F7495 Distributed Systems & Cloud — feel free to collaborate
7496. F7496 Information Theory & Coding — feel free to ask
7497. F7497 Mathematics — generating function for sum
7498. F7498 Operating Systems — directory based protocol
7499. F7499 Curriculum-only — snooping and directory protocol
7500. F7500 Operating Systems — i-node
7501. F7501 Distributed Systems & Cloud — recovery
7502. F7502 Curriculum-only — business-continuity plan with recovery objective
7503. F7503 Curriculum-only — recovery point objective
7504. F7504 Data Mining & Databases — recovery algorithm
7505. F7505 Distributed Systems & Cloud — checkpointing and recovery
7506. F7506 Curriculum-only — checkpointing and recovery algorithm
7507. F7507 Distributed Systems & Cloud — commit protocol
7508. F7508 Curriculum-only — lock manager and recovery manager
7509. F7509 Distributed Systems & Cloud — recovery protocol
7510. F7510 Information Theory & Coding — Data recovery
7511. F7511 Curriculum-only — type of recovery system
7512. F7512 Information Theory & Coding — reliable
7513. F7513 Computer Networks — reliable multicast
7514. F7514 Curriculum-only — network are not reliable you must support partition tolerance
7515. F7515 Distributed Systems & Cloud — reliable and atomic
7516. F7516 Information Theory & Coding — reliable data delivery
7517. F7517 Curriculum-only — log sequence number
7518. F7518 Information Theory & Coding — initial sequence number
7519. F7519 Mathematics — increasing sequence
7520. F7520 Operating Systems — misprediction recovery
7521. F7521 Curriculum-only — misprediction recovery and precise exception
7522. F7522 Operating Systems — open file
7523. F7523 Other/Unknown — waste heat recovery
7524. F7524 Signal/Image/Audio/Video Processing — shape recovery
7525. F7525 Software Engineering — copy prop
7526. F7526 Distributed Systems & Cloud — collaborative editor
7527. F7527 Software Engineering — emptyset
7528. F7528 Computer Architecture — full frame
7529. F7529 Computer Networks — ethernet frame
7530. F7530 Curriculum-only — bandwidth share per frame
7531. F7531 Data Mining & Databases — respect to e1
7532. F7532 Distributed Systems & Cloud — call foo
7533. F7533 Software Engineering — gensubset
7534. F7534 Curriculum-only — documented bgp hijack
7535. F7535 Software Engineering — knowledge engineering
7536. F7536 Software Engineering — root directory
7537. F7537 Curriculum-only — operate what in each service model
7538. F7538 Software Engineering — serving
7539. F7539 Curriculum-only — serving store
7540. F7540 Data Mining & Databases — longest-serving president
7541. F7541 Software Engineering — set intersection
7542. F7542 Mathematics — asymptotic sequence
7543. F7543 Software Engineering — shortcircuit
7544. F7544 Mathematics — fix
7545. F7545 Algorithms & Theory of CS — call to fix
7546. F7546 Curriculum-only — build-and-fix
7547. F7547 Mathematics — automorphism
7548. F7548 Information Theory & Coding — alternative proof of theorem
7549. F7549 Curriculum-only — berlekamp massey algorithm
7550. F7550 Software Engineering — soc in architectural design
7551. F7551 Curriculum-only — halstead estimator of bug
7552. F7552 Distributed Systems & Cloud — parallel code
7553. F7553 Mathematics — candy bar
7554. F7554 Operating Systems — software bug
7555. F7555 Software Engineering — software failure
7556. F7556 Software Engineering — strict complementary slackness
7557. F7557 Distributed Systems & Cloud — sun studio
7558. F7558 ML & AI — agenda
7559. F7559 Algorithms & Theory of CS — uniform cost
7560. F7560 Mathematics — discrete variable
7561. F7561 Curriculum-only — expectation and the limit theorem
7562. F7562 Mathematics — finite variance
7563. F7563 Curriculum-only — chebyshev inequality with their proof
7564. F7564 Mathematics — tomorrow
7565. F7565 Data Mining & Databases — stock market
7566. F7566 Mathematics — numerical value
7567. F7567 ML & AI — predictive
7568. F7568 Curriculum-only — expected log predictive density
7569. F7569 Data Mining & Databases — predictive coding
7570. F7570 Algorithms & Theory of CS — euclidean distance
7571. F7571 Computer Networks — small-world model
7572. F7572 Curriculum-only — clustering with single
7573. F7573 Data Mining & Databases — clustering analysis
7574. F7574 Curriculum-only — clustering algorithm including k-mean
7575. F7575 Data Mining & Databases — number of cluster
7576. F7576 Curriculum-only — centroid-based clustering
7577. F7577 Data Mining & Databases — initial centroid
7578. F7578 Distributed Systems & Cloud — distributed clustering
7579. F7579 ML & AI — cluster center
7580. F7580 Mathematics — betting
7581. F7581 Information Theory & Coding — galois
7582. F7582 Data Mining & Databases — isogeny
7583. F7583 Curriculum-only — isogeny family
7584. F7584 ML & AI — kernel
7585. F7585 Algorithms & Theory of CS — kernel diagnose
7586. F7586 Curriculum-only — computing kernel of training
7587. F7587 Distributed Systems & Cloud — memory-mapped
7588. F7588 Curriculum-only — posix signal semantics
7589. F7589 Distributed Systems & Cloud — posix thread library
7590. F7590 ML & AI — kernel matrix
7591. F7591 Mathematics — aut
7592. F7592 Data Mining & Databases — pkg
7593. F7593 Mathematics — f1 f2
7594. F7594 ML & AI — partition function
7595. F7595 Mathematics — noted
7596. F7596 Algorithms & Theory of CS — robot localization
7597. F7597 Curriculum-only — fault localisation
7598. F7598 Mathematics — multiplicative subset
7599. F7599 Algorithms & Theory of CS — coupon
7600. F7600 Mathematics — coupon collecting
7601. F7601 Curriculum-only — convergence for separable data
7602. F7602 Data Mining & Databases — separable polynomial
7603. F7603 Mathematics — irreducible factor
7604. F7604 Data Mining & Databases — finite separable extension
7605. F7605 Mathematics — state space
7606. F7606 Algorithms & Theory of CS — state space search
7607. F7607 Computer Networks — countable set of value
7608. F7608 Information Theory & Coding — state space size
7609. F7609 ML & AI — continuous state
7610. F7610 Algorithms & Theory of CS — continuous state space
7611. F7611 Mathematics — countably infinite
7612. F7612 Curriculum-only — weak law of large number
7613. F7613 ML & AI — parameter learning
7614. F7614 Mathematics — finite mean
7615. F7615 ML & AI — gaussian markov process
7616. F7616 Mathematics — forward and backward
7617. F7617 Data Mining & Databases — stanford
7618. F7618 Curriculum-only — stanford encyclopedia of philosophy entry on privacy
7619. F7619 Mathematics — ee364b
7620. F7620 Information Theory & Coding — prefix code
7621. F7621 ML & AI — strong converse
7622. F7622 Mathematics — reflection principle
7623. F7623 Curriculum-only — acceptance rule of this domain
7624. F7624 Mathematics — acceptance rate
7625. F7625 Mathematics — z-score
7626. F7626 Curriculum-only — outlier by z-score
7627. F7627 Operating Systems — file descriptor
7628. F7628 Curriculum-only — process and file descriptor
7629. F7629 Operating Systems — guest os
7630. F7630 Other/Unknown — acoustic source localization
7631. F7631 Algorithms & Theory of CS — e1 and e2
7632. F7632 Curriculum-only — elliptic curve modulo
7633. F7633 Data Mining & Databases — complex manifold
7634. F7634 Curriculum-only — counting point and the hasse interval
7635. F7635 Data Mining & Databases — modular form
7636. F7636 Mathematics — algorithm to compute
7637. F7637 Curriculum-only — conformal mapping from half-plane to disk
7638. F7638 Mathematics — montgomery
7639. F7639 Cryptography & Security — montgomery multiplication
7640. F7640 Data Mining & Databases — montgomery ladder
7641. F7641 Mathematics — sage
7642. F7642 Data Mining & Databases — division polynomial
7643. F7643 Mathematics — weierstrass
7644. F7644 Data Mining & Databases — edward curve
7645. F7645 Mathematics — weierstrass approximation theorem
7646. F7646 Data Mining & Databases — elliptic function
7647. F7647 Mathematics — weierstrass m-test
7648. F7648 Other/Unknown — elliptic curve cryptosystem
7649. F7649 Mathematics — lagrangian field theory
7650. F7650 Other/Unknown — galois theory
7651. F7651 Mathematics — finite field
7652. F7652 Curriculum-only — finite field and linear algebra
7653. F7653 Data Mining & Databases — end0
7654. F7654 Algorithms & Theory of CS — transcendental function
7655. F7655 Mathematics — algebraic structure
7656. F7656 Curriculum-only — data fitting with least square
7657. F7657 Data Mining & Databases — fitting model
7658. F7658 ML & AI — over-fitting
7659. F7659 Mathematics — approximation and fitting
7660. F7660 Curriculum-only — imaginary word
7661. F7661 Mathematics — Imaginary number
7662. F7662 Curriculum-only — distributive and complemented lattice
7663. F7663 Mathematics — real and imaginary
7664. F7664 Curriculum-only — algebraic and transcendental equation
7665. F7665 Mathematics — unity
7666. F7666 Curriculum-only — matrix of root of unity
7667. F7667 Mathematics — sinusoidal input
7668. F7668 Other/Unknown — graph clustering
7669. F7669 Curriculum-only — generalization rate with universal kernel machine
7670. F7670 Other/Unknown — multiple kernels
7671. F7671 Signal/Image/Audio/Video Processing — backward euler
7672. F7672 Mathematics — vary
7673. F7673 Curriculum-only — statistics on project failure vary
7674. F7674 Signal/Image/Audio/Video Processing — magnitude and angle
7675. F7675 Mathematics — analysis
7676. F7676 Algorithms & Theory of CS — analysis for integer-valued cost
7677. F7677 Computer Architecture — incremental analysis
7678. F7678 Computer Networks — awk
7679. F7679 Curriculum-only — algorithm and their analysis
7680. F7680 Curriculum-only — markov-noise and constant-step-size analysis
7681. F7681 Data Mining & Databases — graph data
7682. F7682 Curriculum-only — user graph data
7683. F7683 Data Mining & Databases — market basket analysis
7684. F7684 Distributed Systems & Cloud — delphi
7685. F7685 Curriculum-only — variant on structured data
7686. F7686 Distributed Systems & Cloud — analysis of structured data
7687. F7687 Information Theory & Coding — acoustic analysis
7688. F7688 ML & AI — analysis easier
7689. F7689 Mathematics — analysis and numerics
7690. F7690 Curriculum-only — cauchy euler equation
7691. F7691 Mathematics — fourier cosine
7692. F7692 Computer Networks — observational learning
7693. F7693 Mathematics — polynomial equation
7694. F7694 ML & AI — system of polynomial equation
7695. F7695 Mathematics — population structure
7696. F7696 Algorithms & Theory of CS — abstraction relation
7697. F7697 Cryptography & Security — bft
7698. F7698 Curriculum-only — allen thirteen interval relation
7699. F7699 Curriculum-only — relation to condition number
7700. F7700 Data Mining & Databases — accessibility relation
7701. F7701 Distributed Systems & Cloud — arb
7702. F7702 Information Theory & Coding — parity relation
7703. F7703 ML & AI — oval
7704. F7704 Curriculum-only — oval check
7705. F7705 Data Mining & Databases — fred
7706. F7706 Distributed Systems & Cloud — fred schneider
7707. F7707 Mathematics — c1 x1
7708. F7708 Algorithms & Theory of CS — algorithm require
7709. F7709 Curriculum-only — distributed k-mean where each iteration
7710. F7710 Mathematics — cg iteration
7711. F7711 Computer Networks — gap analysis
7712. F7712 Cryptography & Security — gap group
7713. F7713 Curriculum-only — cycle the gap between them shrink
7714. F7714 Data Mining & Databases — integrality gap
7715. F7715 Mathematics — duality gap
7716. F7716 Curriculum-only — absence of duality gap
7717. F7717 Mathematics — order relation
7718. F7718 Curriculum-only — classic five stage
7719. F7719 Mathematics — orthogonality relation
7720. F7720 ML & AI — partially ordered plan
7721. F7721 Mathematics — partially ordered set
7722. F7722 Mathematics — sdo
7723. F7723 Curriculum-only — single relation with type flag
7724. F7724 Mathematics — special
7725. F7725 Algorithms & Theory of CS — matrix-matrix product
7726. F7726 Computer Architecture — Reconfigurable computing
7727. F7727 Curriculum-only — matrix matrix product by column
7728. F7728 Distributed Systems & Cloud — col862 special
7729. F7729 ML & AI — special distribution
7730. F7730 Mathematics — nan
7731. F7731 Curriculum-only — infinity and nan
7732. F7732 Mathematics — special cauchy
7733. F7733 Distributed Systems & Cloud — total number of pre-class
7734. F7734 Mathematics — time required
7735. F7735 Curriculum-only — internally chain transitive set
7736. F7736 Distributed Systems & Cloud — irreflexive
7737. F7737 Mathematics — linear order
7738. F7738 Curriculum-only — cone of uncertainty
7739. F7739 Information Theory & Coding — input event
7740. F7740 Mathematics — data uncertainty
7741. F7741 Data Mining & Databases — dis-cussion
7742. F7742 ML & AI — continuous dis
7743. F7743 Mathematics — x2 x1
7744. F7744 NLP & Speech — agglomerative clustering
7745. F7745 Operating Systems — pcs
7746. F7746 Cryptography & Security — message authentication code
7747. F7747 Curriculum-only — message authentication code are split
7748. F7748 Information Theory & Coding — adder mac
7749. F7749 Mathematics — contraction
7750. F7750 Curriculum-only — contraction in the mean ode
7751. F7751 Information Theory & Coding — contraction mac
7752. F7752 Operating Systems — pcs running
7753. F7753 Other/Unknown — analysis and page-rank
7754. F7754 Curriculum-only — descriptive attribute
7755. F7755 Other/Unknown — detection and analysis
7756. F7756 Mathematics — linearized error propagation
7757. F7757 Other/Unknown — failure analysis
7758. F7758 Mathematics — cable
7759. F7759 Computer Architecture — cable modem
7760. F7760 Other/Unknown — fiber bragg
7761. F7761 Computer Networks — fiber optic networks
7762. F7762 Other/Unknown — fiber optic components
7763. F7763 Curriculum-only — business impact analysis
7764. F7764 Other/Unknown — link analysis
7765. F7765 Mathematics — numerical integration
7766. F7766 Algorithms & Theory of CS — elementary symmetric polynomial
7767. F7767 Curriculum-only — elementary divisor theorem
7768. F7768 Distributed Systems & Cloud — elementary algorithm
7769. F7769 Mathematics — elementary operation
7770. F7770 Other/Unknown — compressible flow
7771. F7771 Curriculum-only — kiefer wolfowitz finite-difference variant
7772. F7772 Mathematics — finite-difference approximation
7773. F7773 Algorithms & Theory of CS — forward difference formula
7774. F7774 Mathematics — multidimensional finite difference
7775. F7775 Other/Unknown — finite difference time domain
7776. F7776 Curriculum-only — sensitivity analysis of least square
7777. F7777 Mathematics — local sensitivity analysis
7778. F7778 Other/Unknown — shrinkage
7779. F7779 Curriculum-only — absolute shrinkage
7780. F7780 Other/Unknown — singularity analysis
7781. F7781 Curriculum-only — laplace transform of special function
7782. F7782 Mathematics — special function in julia
7783. F7783 Other/Unknown — special matrix
7784. F7784 Mathematics — singular
7785. F7785 Curriculum-only — determinant mean singular
7786. F7786 ML & AI — low rank
7787. F7787 Curriculum-only — link to svd low-rank theory
7788. F7788 Mathematics — closest rank
7789. F7789 Other/Unknown — low rank approximation
7790. F7790 Curriculum-only — low-rank approximation built from actual column
7791. F7791 Other/Unknown — stability analysis
7792. F7792 Curriculum-only — functional design approach like structured analysis
7793. F7793 Other/Unknown — system and control
7794. F7794 Curriculum-only — structured low-rank approximation with model order selection in time series
7795. F7795 ML & AI — Time series data (aggregation, join)
7796. F7796 Other/Unknown — Traffic analysis
7797. F7797 Signal/Image/Audio/Video Processing — adding delay tend
7798. F7798 Other/Unknown — visual
7799. F7799 Computer Architecture — visual design
7800. F7800 Computer Networks — Visual inspection
7801. F7801 Data Mining & Databases — visual neuroscience
7802. F7802 Distributed Systems & Cloud — data visualization
7803. F7803 ML & AI — visual cortex
7804. F7804 NLP & Speech — interactive data visualization
7805. F7805 Other/Unknown — dispersion
7806. F7806 Algorithms & Theory of CS — guided
7807. F7807 Information Theory & Coding — channel dispersion
7808. F7808 Mathematics — light cone
7809. F7809 Other/Unknown — Central tendency
7810. F7810 Information Theory & Coding — interference
7811. F7811 Mathematics — interference ratio
7812. F7812 Other/Unknown — fourier optics
7813. F7813 Signal/Image/Audio/Video Processing — attenuation
7814. F7814 Information Theory & Coding — multipath
7815. F7815 Curriculum-only — multipath computation
7816. F7816 Information Theory & Coding — multipath channel
7817. F7817 Mathematics — attenuation rate
7818. F7818 Other/Unknown — fading multipath
7819. F7819 Signal/Image/Audio/Video Processing — find kt for fastest
7820. F7820 Algorithms & Theory of CS — error bound
7821. F7821 Curriculum-only — backward interpolation formulae
7822. F7822 Mathematics — differentiation rule
7823. F7823 Curriculum-only — error in interpolation polynomial
7824. F7824 Mathematics — interpolation theorem
7825. F7825 Curriculum-only — reconstruction by lagrange interpolation
7826. F7826 Mathematics — polynomial interpolation
7827. F7827 Curriculum-only — matrix in polynomial interpolation
7828. F7828 Mathematics — piecewise
7829. F7829 Curriculum-only — piecewise function
7830. F7830 Mathematics — piecewise continuity
7831. F7831 Curriculum-only — rolle theorem and lagrange mvt
7832. F7832 Mathematics — sharp
7833. F7833 ML & AI — sharp teeth
7834. F7834 Mathematics — spectral interpolation
7835. F7835 Signal/Image/Audio/Video Processing — bicubic interpolation
7836. F7836 Information Theory & Coding — second-formant
7837. F7837 NLP & Speech — vowel
7838. F7838 Mathematics — lax
7839. F7839 Algorithms & Theory of CS — total cost
7840. F7840 Data Mining & Databases — billion in revenue
7841. F7841 Mathematics — decision variable
7842. F7842 NLP & Speech — consonant
7843. F7843 Information Theory & Coding — consonant sequence
7844. F7844 NLP & Speech — glide
7845. F7845 Mathematics — glide line
7846. F7846 NLP & Speech — glottal
7847. F7847 Information Theory & Coding — glottal opening
7848. F7848 Curriculum-only — consistency spectrum
7849. F7849 Information Theory & Coding — spread spectrum
7850. F7850 Curriculum-only — stream job with event-time window
7851. F7851 Mathematics — continuous spectrum
7852. F7852 Computer Networks — grace period
7853. F7853 Information Theory & Coding — long period
7854. F7854 Mathematics — character of modulus
7855. F7855 ML & AI — random function
7856. F7856 NLP & Speech — nasal consonant
7857. F7857 Other/Unknown — dynamic spectrum
7858. F7858 Signal/Image/Audio/Video Processing — angular frequency
7859. F7859 Curriculum-only — angular frequency and period
7860. F7860 Signal/Image/Audio/Video Processing — continuous-time signal
7861. F7861 Information Theory & Coding — sample rate
7862. F7862 Distributed Systems & Cloud — clock
7863. F7863 Computer Architecture — clock generator
7864. F7864 Curriculum-only — bus width and clock
7865. F7865 Distributed Systems & Cloud — clock-based
7866. F7866 Algorithms & Theory of CS — global snapshot
7867. F7867 Distributed Systems & Cloud — asynchronous distributed system
7868. F7868 Curriculum-only — agreed timestamp
7869. F7869 Distributed Systems & Cloud — commit timestamp
7870. F7870 Curriculum-only — lamport timestamp and the clock condition
7871. F7871 Distributed Systems & Cloud — start timestamp of lock-free
7872. F7872 Curriculum-only — lamport clock and vector clock
7873. F7873 Information Theory & Coding — clock recovery
7874. F7874 Computer Architecture — four-fsm sample waveform
7875. F7875 Information Theory & Coding — channel waveform
7876. F7876 ML & AI — ltime
7877. F7877 Mathematics — cen
7878. F7878 Operating Systems — reliable message
7879. F7879 Signal/Image/Audio/Video Processing — low rank change
7880. F7880 Information Theory & Coding — aperiodic
7881. F7881 NLP & Speech — acoustics of speech hearing
7882. F7882 Signal/Image/Audio/Video Processing — continuous-time fourier series
7883. F7883 Mathematics — ak and bk
7884. F7884 Signal/Image/Audio/Video Processing — fourier series coefficient
7885. F7885 Algorithms & Theory of CS — spatial tree
7886. F7886 Computer Architecture — transmittance
7887. F7887 Curriculum-only — spatial and multimedia database
7888. F7888 Information Theory & Coding — spatial correlations
7889. F7889 ML & AI — spatial distance
7890. F7890 Mathematics — derivative with respect
7891. F7891 NLP & Speech — spatial dependence
7892. F7892 Operating Systems — exploiting spatial
7893. F7893 Other/Unknown — lorentz transformation
7894. F7894 Signal/Image/Audio/Video Processing — spatial filtering
7895. F7895 Mathematics — basis
7896. F7896 Algorithms & Theory of CS — llb
7897. F7897 Curriculum-only — basis for planning
7898. F7898 Data Mining & Databases — equiangular tight frame
7899. F7899 Information Theory & Coding — projection theorem
7900. F7900 ML & AI — component-by-component basis
7901. F7901 Cryptography & Security — hidden monomial cryptosystem
7902. F7902 Curriculum-only — hidden and exposed terminal
7903. F7903 Information Theory & Coding — hidden terminal
7904. F7904 ML & AI — hidden node
7905. F7905 Mathematics — basis change
7906. F7906 Information Theory & Coding — orthogonal mac
7907. F7907 Mathematics — basis vector
7908. F7908 Curriculum-only — empirical orthogonal function
7909. F7909 Mathematics — orthogonal operator
7910. F7910 ML & AI — orthonormal basis in l2
7911. F7911 Mathematics — output basis
7912. F7912 Curriculum-only — spanned and unspanned
7913. F7913 Mathematics — start with basis matrix
7914. F7914 Curriculum-only — unitary matrix after scaling
7915. F7915 Mathematics — ut su
7916. F7916 Data Mining & Databases — x1 x2 x3 x4
7917. F7917 NLP & Speech — physiological basis
7918. F7918 Other/Unknown — orthogonal frequency division
7919. F7919 Signal/Image/Audio/Video Processing — a2 orthogonal
7920. F7920 Software Engineering — alias analysis
7921. F7921 Mathematics — separation
7922. F7922 Curriculum-only — data plane separation
7923. F7923 Information Theory & Coding — channel separation
7924. F7924 Mathematics — separating hyperplane
7925. F7925 Curriculum-only — definite integral and the fundamental theorem
7926. F7926 Mathematics — contour
7927. F7927 Other/Unknown — phase separation
7928. F7928 Signal/Image/Audio/Video Processing — negentropy
7929. F7929 Software Engineering — better separation
7930. F7930 Curriculum-only — dennard scaling as the reason clock rate stopped rising
7931. F7931 Software Engineering — dream
7932. F7932 Computer Architecture — floating gates
7933. F7933 Curriculum-only — floating point number
7934. F7934 Mathematics — floating-point addition
7935. F7935 Software Engineering — fourier coefficient ak
7936. F7936 Algorithms & Theory of CS — halttm
7937. F7937 Curriculum-only — vote to halt
7938. F7938 Data Mining & Databases — nothing change
7939. F7939 Operating Systems — add halt
7940. F7940 Software Engineering — imprecision
7941. F7941 Curriculum-only — root cause and remedy
7942. F7942 Software Engineering — running ame vary
7943. F7943 Computer Networks — cost savings
7944. F7944 Mathematics — life saving
7945. F7945 Other/Unknown — energy savings
7946. F7946 Software Engineering — saving rate
7947. F7947 Curriculum-only — jackson structured programming
7948. F7948 Software Engineering — sturm liouville
7949. F7949 Algorithms & Theory of CS — min-cut
7950. F7950 Curriculum-only — max-flow and min-cut
7951. F7951 Mathematics — menger
7952. F7952 Algorithms & Theory of CS — menger theorem
7953. F7953 Mathematics — pattern
7954. F7954 Computer Architecture — pattern state
7955. F7955 Computer Networks — structural pattern
7956. F7956 Curriculum-only — attack-pattern
7957. F7957 Curriculum-only — named for matching many pattern
7958. F7958 Curriculum-only — traversal and pattern query
7959. F7959 Data Mining & Databases — understanding cluster pattern
7960. F7960 Distributed Systems & Cloud — pattern for mapping computation
7961. F7961 Information Theory & Coding — antenna pattern
7962. F7962 ML & AI — binary patterns
7963. F7963 Mathematics — color pattern
7964. F7964 Other/Unknown — path and distance
7965. F7965 Mathematics — transform
7966. F7966 Algorithms & Theory of CS — fast j-l transform
7967. F7967 Computer Networks — hw7
7968. F7968 Curriculum-only — box muller transform
7969. F7969 Data Mining & Databases — hadamard transform
7970. F7970 Algorithms & Theory of CS — sparse johnson-lindenstrauss transform
7971. F7971 Data Mining & Databases — fast johnson-lindenstrauss transform
7972. F7972 Distributed Systems & Cloud — burrows-wheeler transform
7973. F7973 ML & AI — hw2
7974. F7974 Mathematics — discrete sine transforms
7975. F7975 Curriculum-only — circle inversion
7976. F7976 Mathematics — bius inversion
7977. F7977 Curriculum-only — calculus of residue for the inversion formula of z-transform
7978. F7978 Mathematics — l1 and l2
7979. F7979 Curriculum-only — toeplitz data matrix
7980. F7980 Mathematics — transform based
7981. F7981 NLP & Speech — short-time spectral analysis
7982. F7982 Other/Unknown — channel inversion
7983. F7983 Signal/Image/Audio/Video Processing — biomedical
7984. F7984 Other/Unknown — biomedical engineering
7985. F7985 Data Mining & Databases — structure to biomedical image
7986. F7986 Other/Unknown — biomedical signal
7987. F7987 Mathematics — stationarity
7988. F7988 Signal/Image/Audio/Video Processing — convolution
7989. F7989 Curriculum-only — activation memory of convolution
7990. F7990 Information Theory & Coding — convolution code
7991. F7991 Mathematics — convolution product
7992. F7992 Distributed Systems & Cloud — data-lake
7993. F7993 Curriculum-only — data-lake and lakehouse idiom
7994. F7994 Information Theory & Coding — mead
7995. F7995 ML & AI — electric guitar
7996. F7996 Mathematics — length sequence
7997. F7997 Curriculum-only — maximal-length sequence
7998. F7998 Signal/Image/Audio/Video Processing — block convolution
7999. F7999 Curriculum-only — causality and logical time
8000. F8000 Mathematics — condition for causality
8001. F8001 Signal/Image/Audio/Video Processing — continuous-time fourier transform
8002. F8002 Mathematics — periodic with period
8003. F8003 Signal/Image/Audio/Video Processing — discrete-time fourier transform
8004. F8004 Signal/Image/Audio/Video Processing — fourier transform in physics
8005. F8005 Mathematics — ghost
8006. F8006 NLP & Speech — brain imaging
8007. F8007 Other/Unknown — image sensor
8008. F8008 Mathematics — speed
8009. F8009 Algorithms & Theory of CS — speed of sound
8010. F8010 Curriculum-only — crt-rsa decryption speed-up
8011. F8011 Distributed Systems & Cloud — braking
8012. F8012 Algorithms & Theory of CS — regenerative braking
8013. F8013 Mathematics — computational kernel
8014. F8014 Algorithms & Theory of CS — slow pointer
8015. F8015 Curriculum-only — serialisable and slow
8016. F8016 ML & AI — fast rate
8017. F8017 Mathematics — slow-wave guiding
8018. F8018 Other/Unknown — cmos image sensor
8019. F8019 Data Mining & Databases — high speed networks
8020. F8020 Distributed Systems & Cloud — high-speed interconnect
8021. F8021 Information Theory & Coding — high-speed lan
8022. F8022 Other/Unknown — imaging geometry
8023. F8023 Signal/Image/Audio/Video Processing — constant speed
8024. F8024 Information Theory & Coding — solid line
8025. F8025 Mathematics — a1 cos
8026. F8026 Signal/Image/Audio/Video Processing — cosine sequence
8027. F8027 Algorithms & Theory of CS — sampling algorithm for l2
8028. F8028 Curriculum-only — decoding strategy and sampling
8029. F8029 Data Mining & Databases — convenience sampling
8030. F8030 Algorithms & Theory of CS — kane and nelson
8031. F8031 Data Mining & Databases — jelani nelson
8032. F8032 ML & AI — missing value
8033. F8033 Curriculum-only — pandas missing value
8034. F8034 ML & AI — sampling strategy
8035. F8035 Mathematics — bach
8036. F8036 Data Mining & Databases — violin
8037. F8037 Mathematics — cluster sampling
8038. F8038 Other/Unknown — sampling and approximating
8039. F8039 Signal/Image/Audio/Video Processing — discrete-time sampling
8040. F8040 NLP & Speech — formant frequency
8041. F8041 Signal/Image/Audio/Video Processing — db spl
8042. F8042 Mathematics — bandlimited differentiation
8043. F8043 Other/Unknown — analog signal
8044. F8044 Information Theory & Coding — digital data
8045. F8045 Signal/Image/Audio/Video Processing — bandlimited signal
8046. F8046 Other/Unknown — digital signal processors
8047. F8047 Signal/Image/Audio/Video Processing — low pass
8048. F8048 Mathematics — poisson summation formula
8049. F8049 Signal/Image/Audio/Video Processing — sampling and quantization
8050. F8050 Mathematics — discrete set
8051. F8051 Signal/Image/Audio/Video Processing — inverse transform
8052. F8052 Curriculum-only — inverse-transform sampling
8053. F8053 Signal/Image/Audio/Video Processing — roc
8054. F8054 Curriculum-only — roc and auc
8055. F8055 Data Mining & Databases — algebraic expression
8056. F8056 Signal/Image/Audio/Video Processing — pole-zero plot
8057. F8057 Information Theory & Coding — baseband
8058. F8058 Computer Networks — skip modulation
8059. F8059 Information Theory & Coding — amplitude modulation
8060. F8060 Curriculum-only — matched filter that correlate
8061. F8061 Information Theory & Coding — ofdm
8062. F8062 Curriculum-only — dft-precoded ofdm
8063. F8063 Information Theory & Coding — trellis-coded modulation
8064. F8064 Mathematics — ple
8065. F8065 Other/Unknown — carrier
8066. F8066 Computer Networks — multiple carrier
8067. F8067 Curriculum-only — carrier-grade nat
8068. F8068 Distributed Systems & Cloud — word count
8069. F8069 Curriculum-only — word-count vector
8070. F8070 Distributed Systems & Cloud — word count distribution
8071. F8071 Information Theory & Coding — carrier frequency
8072. F8072 Mathematics — mail carrier
8073. F8073 Other/Unknown — ple semantics
8074. F8074 Signal/Image/Audio/Video Processing — carrier signal
8075. F8075 Information Theory & Coding — sideband
8076. F8076 Signal/Image/Audio/Video Processing — sigma-delta modulation
8077. F8077 Other/Unknown — wave theory
8078. F8078 Signal/Image/Audio/Video Processing — spectra associated
8079. F8079 Signal/Image/Audio/Video Processing — transform and series
8080. F8080 Software Engineering — anti-pattern
8081. F8081 Computer Architecture — dd month yyyy
8082. F8082 Curriculum-only — month if all unique
8083. F8083 Mathematics — negative feedback
8084. F8084 Signal/Image/Audio/Video Processing — second-order system
8085. F8085 NLP & Speech — input admittance system function
8086. F8086 Signal/Image/Audio/Video Processing — wallfinder
8087. F8087 Software Engineering — sub2
8088. F8088 Algorithms & Theory of CS — max temp
8089. F8089 Distributed Systems & Cloud — set temp
8090. F8090 Software Engineering — avg
8091. F8091 Computer Networks — select avg
8092. F8092 NLP & Speech — yds avg td
8093. F8093 Software Engineering — termination and correctness
8094. F8094 Information Theory & Coding — sliding window
8095. F8095 Curriculum-only — sliding window and flow control
8096. F8096 Information Theory & Coding — reliable transport
8097. F8097 Curriculum-only — interest and data packet
8098. F8098 Information Theory & Coding — packet loss
8099. F8099 Mathematics — failed
8100. F8100 Algorithms & Theory of CS — enginea
8101. F8101 Curriculum-only — control that failed
8102. F8102 Mathematics — failed to find
8103. F8103 Computer Architecture — minterm
8104. F8104 Curriculum-only — affine combination
8105. F8105 Data Mining & Databases — special form
8106. F8106 Mathematics — convex combination
8107. F8107 HS Maths Class XI / Unit-II: Algebra — binomial theorem
8108. F8108 Algorithms & Theory of CS — bernoulli random variable
8109. F8109 Curriculum-only — beta binomial
8110. F8110 Mathematics — binomial coe
8111. F8111 Curriculum-only — combination and the binomial coefficient
8112. F8112 Mathematics — integer linear
8113. F8113 Algorithms & Theory of CS — integer linear programs
8114. F8114 Curriculum-only — quantity as an integer linear program
8115. F8115 Mathematics — interval of length
8116. F8116 Distributed Systems & Cloud — lin and dyer
8117. F8117 Mathematics — linear combination
8118. F8118 Curriculum-only — affine and linear combination
8119. F8119 Information Theory & Coding — stationary state
8120. F8120 Mathematics — m1 m2
8121. F8121 Signal/Image/Audio/Video Processing — finite linear combination
8122. F8122 Mathematics — examination
8123. F8123 Curriculum-only — kasiski examination
8124. F8124 Mathematics — posted
8125. F8125 Computer Architecture — dance
8126. F8126 Curriculum-only — difficulty adjustment
8127. F8127 Mathematics — positive value
8128. F8128 Signal/Image/Audio/Video Processing — digital camera
8129. F8129 Distributed Systems & Cloud — cds
8130. F8130 Information Theory & Coding — achievability bound
8131. F8131 Mathematics — dpy
8132. F8132 Signal/Image/Audio/Video Processing — crossover distortion
8133. F8133 Other/Unknown — bode plot
8134. F8134 Signal/Image/Audio/Video Processing — feedback system
8135. F8135 Other/Unknown — feedback control
8136. F8136 Signal/Image/Audio/Video Processing — phase distortions
8137. F8137 Mathematics — sin cos
8138. F8138 Algorithms & Theory of CS — ellipsoid algorithm
8139. F8139 Mathematics — analytic center
8140. F8140 Signal/Image/Audio/Video Processing — wide-sense stationary
8141. F8141 Mathematics — stochastic process
8142. F8142 Distributed Systems & Cloud — vocoder
8143. F8143 Information Theory & Coding — theory and coding
8144. F8144 Mathematics — Stochastic differential equations
8145. F8145 Other/Unknown — detector
8146. F8146 Curriculum-only — termination detector by snapshot
8147. F8147 Distributed Systems & Cloud — failure detector
8148. F8148 Curriculum-only — partial synchrony and failure detector
8149. F8149 Distributed Systems & Cloud — unreliable failure detector
8150. F8150 Mathematics — u1 u2
8151. F8151 NLP & Speech — pitch
8152. F8152 Distributed Systems & Cloud — analyzer
8153. F8153 Mathematics — signal analyzer
8154. F8154 Other/Unknown — network analyzer
8155. F8155 Curriculum-only — linear stochastic approximation
8156. F8156 Signal/Image/Audio/Video Processing — ground truth
8157. F8157 Mathematics — random process
8158. F8158 Curriculum-only — random process and queueing for network
8159. F8159 Information Theory & Coding — filtered random process
8160. F8160 Mathematics — random number
8161. F8161 Cryptography & Security — cryptographically secure random number
8162. F8162 Algorithms & Theory of CS — pseudorandom number generator
8163. F8163 Cryptography & Security — pseudo-random number generation
8164. F8164 Curriculum-only — random number and plotting
8165. F8165 Mathematics — normal random number
8166. F8166 Other/Unknown — monte carlo
8167. F8167 Curriculum-only — monte carlo loss exceedance
8168. F8168 Mathematics — model based
8169. F8169 Curriculum-only — model-based clustering
8170. F8170 Mathematics — model based on conditional
8171. F8171 Other/Unknown — model-based control
8172. F8172 Signal/Image/Audio/Video Processing — filtering of wss process
8173. F8173 Software Engineering — ati
8174. F8174 Algorithms & Theory of CS — evaluation function
8175. F8175 Curriculum-only — benchmarking and evaluation
8176. F8176 Curriculum-only — model evaluation
8177. F8177 Data Mining & Databases — applicative
8178. F8178 Curriculum-only — stack data structure and expression evaluation
8179. F8179 Distributed Systems & Cloud — evaluation strategy
8180. F8180 ML & AI — evaluation functional
8181. F8181 Algorithms & Theory of CS — minimax search
8182. F8182 Curriculum-only — saddle point and minimax
8183. F8183 ML & AI — bayesian
8184. F8184 Algorithms & Theory of CS — recursive bayesian
8185. F8185 Curriculum-only — bayesian alternative
8186. F8186 Data Mining & Databases — redo
8187. F8187 Curriculum-only — redo rule
8188. F8188 Data Mining & Databases — redo information
8189. F8189 Information Theory & Coding — bayesian criterion
8190. F8190 ML & AI — bayesian score
8191. F8191 Curriculum-only — descent method converge
8192. F8192 ML & AI — double descent
8193. F8193 Curriculum-only — minimax game and optimal discriminator
8194. F8194 Mathematics — bayesian decision
8195. F8195 Curriculum-only — deferred and immediate update
8196. F8196 Data Mining & Databases — deferred operation
8197. F8197 Mathematics — descent direction
8198. F8198 Curriculum-only — cone of descent direction
8199. F8199 Mathematics — differentiable convex function
8200. F8200 Curriculum-only — non-differentiable convex function
8201. F8201 Mathematics — direction of descent
8202. F8202 Computer Networks — infectious disease
8203. F8203 Data Mining & Databases — coronary artery disease
8204. F8204 Information Theory & Coding — disorder
8205. F8205 ML & AI — diagnosis
8206. F8206 Data Mining & Databases — predictive diagnosis
8207. F8207 Mathematics — fermat descent
8208. F8208 Curriculum-only — man-in-the-middle failure
8209. F8209 Mathematics — optimality gap
8210. F8210 Curriculum-only — false-positive rate
8211. F8211 Mathematics — rare disease
8212. F8212 Curriculum-only — global convergence of steepest descent
8213. F8213 Mathematics — linear convergence
8214. F8214 NLP & Speech — evaluation measure
8215. F8215 Curriculum-only — classification evaluation measure
8216. F8216 NLP & Speech — evaluation of machine translation
8217. F8217 Operating Systems — analysis and evaluation
8218. F8218 Other/Unknown — Bayesian linear regression
8219. F8219 Data Mining & Databases — prostate cancer
8220. F8220 ML & AI — breast cancer
8221. F8221 Mathematics — cure
8222. F8222 Curriculum-only — cure algorithm
8223. F8223 Other/Unknown — cause of cancer
8224. F8224 Signal/Image/Audio/Video Processing — bayesian filtering
8225. F8225 Software Engineering — convergence constant
8226. F8226 Curriculum-only — logical evaluation order
8227. F8227 Software Engineering — inexact
8228. F8228 Mathematics — restriction
8229. F8229 Curriculum-only — election restriction
8230. F8230 Data Mining & Databases — set of constraint
8231. F8231 Other/Unknown — simulink
8232. F8232 Signal/Image/Audio/Video Processing — image removed
8233. F8233 NLP & Speech — copyright consideration
8234. F8234 Software Engineering — exact and inexact
8235. F8235 ML & AI — descent algorithm
8236. F8236 Mathematics — divergence
8237. F8237 Curriculum-only — branch divergence
8238. F8238 Distributed Systems & Cloud — data processing
8239. F8239 Algorithms & Theory of CS — data processing inequality
8240. F8240 Curriculum-only — applied to data-processing job
8241. F8241 Distributed Systems & Cloud — divergence in control transfer
8242. F8242 Information Theory & Coding — capacity saddle
8243. F8243 Curriculum-only — standard distribution and the memoryless
8244. F8244 Information Theory & Coding — distortion function
8245. F8245 Algorithms & Theory of CS — deletion
8246. F8246 Curriculum-only — deletion and modification written as algebra
8247. F8247 Data Mining & Databases — skew
8248. F8248 Curriculum-only — shortest distance between skew line
8249. F8249 Information Theory & Coding — binary string
8250. F8250 ML & AI — contrastive divergence
8251. F8251 Mathematics — comparable
8252. F8252 Computer Networks — conductance
8253. F8253 Cryptography & Security — public-key encryption
8254. F8254 Algorithms & Theory of CS — rsa signature
8255. F8255 Computer Architecture — ta signature
8256. F8256 Cryptography & Security — homomorphic
8257. F8257 Curriculum-only — aho corasick matching used by signature-based detection
8258. F8258 Curriculum-only — somewhat and fully homomorphic scheme
8259. F8259 Data Mining & Databases — time signature
8260. F8260 Curriculum-only — one-time signature from one-way function
8261. F8261 ML & AI — unsupervised
8262. F8262 Mathematics — birth-death markov chain
8263. F8263 Curriculum-only — discrete-time markov chain and operation
8264. F8264 Mathematics — fij
8265. F8265 Mathematics — martingale
8266. F8266 Curriculum-only — conditional expectation and martingale
8267. F8267 Information Theory & Coding — martingale difference sequence
8268. F8268 Mathematics — backward martingale
8269. F8269 Computer Networks — dbs
8270. F8270 Mathematics — bs dbs
8271. F8271 Mathematics — reversible markov chain
8272. F8272 Computer Networks — doubly stochastic matrix
8273. F8273 Mathematics — waiting time
8274. F8274 Computer Architecture — change state
8275. F8275 Curriculum-only — exponential as the waiting time
8276. F8276 Mathematics — exponential distribution
8277. F8277 Curriculum-only — long lifetime
8278. F8278 Mathematics — light bulb
8279. F8279 Operating Systems — cryptographic signature
8280. F8280 Other/Unknown — principal component analysis
8281. F8281 ML & AI — sparse pca
8282. F8282 Mathematics — principal component analysis pca
8283. F8283 Other/Unknown — renewal theory
8284. F8284 Software Engineering — coinjoin
8285. F8285 Curriculum-only — primer code for these design is not reproduced
8286. F8286 Software Engineering — risk evaluation
8287. F8287 Data Mining & Databases — st elevation
8288. F8288 Curriculum-only — wormhole switching
8289. F8289 Mathematics — roulette
8290. F8290 Data Mining & Databases — american roulette
8291. F8291 Mathematics — sample size
8292. F8292 Curriculum-only — effective sample size
8293. F8293 ML & AI — ijk
8294. F8294 Software Engineering — scanf
8295. F8295 Curriculum-only — model in the standard library
8296. F8296 Software Engineering — assert
8297. F8297 Other/Unknown — archive
8298. F8298 Cryptography & Security — cryptology eprint archive
8299. F8299 Signal/Image/Audio/Video Processing — dspace archive
8300. F8300 Software Engineering — stdarg
8301. F8301 Computer Architecture — schmitt trigger
8302. F8302 Curriculum-only — trigger as event-condition-action rule
8303. F8303 Software Engineering — triplet
8304. F8304 Curriculum-only — modeling of union type using category
8305. F8305 Software Engineering — variable argument list
8306. F8306 Curriculum-only — spot vms
8307. F8307 Software Engineering — water system
8308. F8308 Cryptography & Security — government
8309. F8309 Data Mining & Databases — secretary
8310. F8310 Computer Networks — federal
8311. F8311 Data Mining & Databases — united state presidential election
8312. F8312 Mathematics — judge
8313. F8313 Cryptography & Security — supreme court
8314. F8314 Curriculum-only — llm-as-a-judge
8315. F8315 Data Mining & Databases — forecasting supreme court decision
8316. F8316 Mathematics — warrant
8317. F8317 NLP & Speech — extradition
8318. F8318 Software Engineering — word count program
8319. F8319 System Design Primer / Consistency patterns — weak consistency
8320. F8320 System Design Primer / Content delivery network — content delivery network
8321. F8321 Curriculum-only — content delivery network like cloudflare
8322. F8322 System Design Primer / Content delivery network — Push CDNs
8323. F8323 System Design Primer / Database — tune the query cache
8324. F8324 Curriculum-only — wide-column store on dynamo ring
8325. F8325 System Design Primer / Database — sql or nosql
8326. F8326 System Design Primer / Design Amazon's sales ranking by category feature — Design Amazon's sales ranking by category feature
8327. F8327 System Design Primer / Design Mint.com — Design Mint.com
8328. F8328 System Design Primer / Design Pastebin.com (or Bit.ly) — Design Pastebin.com (or Bit.ly)
8329. F8329 System Design Primer / Design a key-value store for a search engine — Design a key-value store for a search engine
8330. F8330 System Design Primer / Design a system that scales to millions of users on AWS — Design a system that scales to millions of users on AWS
8331. F8331 System Design Primer / Design a web crawler — Design a web crawler
8332. F8332 System Design Primer / Design the Twitter timeline and search (or Facebook feed and search) — Design the Twitter timeline and search (or Facebook feed and search)
8333. F8333 System Design Primer / Design the data structures for a social network — Design the data structures for a social network
8334. F8334 System Design Primer / Domain name system — domain name system
8335. F8335 System Design Primer / How to approach a system design interview question — How to approach a system design interview question
8336. F8336 System Design Primer / Latency numbers every programmer should know — Latency numbers every programmer should know
8337. F8337 System Design Primer / Latency vs throughput — Latency vs throughput
8338. F8338 System Design Primer / Load balancer — load balancer
8339. F8339 Curriculum-only — load balancer and replicas
8340. F8340 System Design Primer / Load balancer — Layer 4 load balancing
8341. F8341 Curriculum-only — horizontal scaling behind
8342. F8342 System Design Primer / Performance vs scalability — Performance vs scalability
8343. F8343 System Design Primer / Powers of two table — Powers of two table
8344. F8344 System Design Primer / Reverse proxy (web server) — Reverse proxy (web server)
8345. F8345 System Design Primer / Security — security
8346. F8346 Computer Networks — anderson
8347. F8347 Cryptography & Security — achieving security
8348. F8348 Cryptography & Security — gm security
8349. F8349 Cryptography & Security — security game
8350. F8350 Algorithms & Theory of CS — random line
8351. F8351 Cryptography & Security — secure computation
8352. F8352 Curriculum-only — api security
8353. F8353 Curriculum-only — discrete-log analogue
8354. F8354 Curriculum-only — perfect security and its limitation
8355. F8355 Curriculum-only — security-critical component
8356. F8356 Data Mining & Databases — criminal
8357. F8357 Curriculum-only — statistical database security
8358. F8358 Data Mining & Databases — elliptic-curve discrete log
8359. F8359 Curriculum-only — ecdh and the elliptic-curve discrete log
8360. F8360 Data Mining & Databases — network intrusion
8361. F8361 Curriculum-only — network intrusion detection and prevention
8362. F8362 Distributed Systems & Cloud — authentication security in ds
8363. F8363 Curriculum-only — on-demand self-service
8364. F8364 Distributed Systems & Cloud — security and authentication
8365. F8365 ML & AI — insider
8366. F8366 Curriculum-only — weak against insider
8367. F8367 Mathematics — total degree
8368. F8368 Operating Systems — cryptography and cryptanalysis
8369. F8369 Algorithms & Theory of CS — unsatisfiable
8370. F8370 Cryptography & Security — yael tauman kalai
8371. F8371 Distributed Systems & Cloud — computer science
8372. F8372 Algorithms & Theory of CS — amortized analysis
8373. F8373 Algorithms & Theory of CS — short proof
8374. F8374 Computer Architecture — game design
8375. F8375 Cryptography & Security — verifier
8376. F8376 Algorithms & Theory of CS — verifier check
8377. F8377 Curriculum-only — cook levin theorem stated
8378. F8378 Data Mining & Databases — astronomy
8379. F8379 Distributed Systems & Cloud — degree in computer science
8380. F8380 Algorithms & Theory of CS — distributed computing model
8381. F8381 Curriculum-only — distributed computing with mapreduce
8382. F8382 Distributed Systems & Cloud — distributed computing environment
8383. F8383 Computer Networks — socket programming
8384. F8384 Distributed Systems & Cloud — science and engineering
8385. F8385 Curriculum-only — department of computer science and engineering
8386. F8386 ML & AI — computer science artificial intelligence
8387. F8387 Mathematics — chlipala
8388. F8388 Data Mining & Databases — dan boneh
8389. F8389 Mathematics — effective programming
8390. F8390 Data Mining & Databases — world war
8391. F8391 ML & AI — silhouette
8392. F8392 Curriculum-only — elbow and the silhouette
8393. F8393 Mathematics — great circle
8394. F8394 Algorithms & Theory of CS — sak
8395. F8395 Computer Architecture — max index
8396. F8396 Computer Networks — create index
8397. F8397 Algorithms & Theory of CS — single-index array
8398. F8398 Cryptography & Security — cur index
8399. F8399 Curriculum-only — central index
8400. F8400 Curriculum-only — index-only
8401. F8401 Data Mining & Databases — cgi
8402. F8402 Curriculum-only — gini index and entropy
8403. F8403 Data Mining & Databases — inverted index
8404. F8404 Curriculum-only — try and the inverted index
8405. F8405 Data Mining & Databases — primary index
8406. F8406 Distributed Systems & Cloud — h-index
8407. F8407 Information Theory & Coding — time index
8408. F8408 Mathematics — aij xj
8409. F8409 Algorithms & Theory of CS — aij xj bi
8410. F8410 Mathematics — resource index
8411. F8411 Computer Networks — technical material
8412. F8412 Curriculum-only — technical remedy that the source course does not list
8413. F8413 Distributed Systems & Cloud — technical computing
8414. F8414 Curriculum-only — technical debt and its interest
8415. F8415 Mathematics — language for technical computing
8416. F8416 Operating Systems — computer design
8417. F8417 Distributed Systems & Cloud — data structure computer design
8418. F8418 Operating Systems — index register
8419. F8419 Curriculum-only — remote system call for migration
8420. F8420 Distributed Systems & Cloud — mkdir
8421. F8421 Other/Unknown — big-data
8422. F8422 Curriculum-only — enabling technology for big data
8423. F8423 Other/Unknown — business strategy
8424. F8424 Curriculum-only — business strategy and privacy
8425. F8425 Other/Unknown — data collection
8426. F8426 Curriculum-only — business question through data collection
8427. F8427 NLP & Speech — questionnaire
8428. F8428 Curriculum-only — self-assessment questionnaire
8429. F8429 Other/Unknown — Differences between data security and data privacy
8430. F8430 Curriculum-only — data privacy risk
8431. F8431 Other/Unknown — effective index
8432. F8432 Curriculum-only — physical unclonable function and hardware trojan
8433. F8433 Other/Unknown — horn
8434. F8434 Algorithms & Theory of CS — stanley
8435. F8435 Other/Unknown — index structure
8436. F8436 Data Mining & Databases — hash index
8437. F8437 Other/Unknown — logic for computer science
8438. F8438 Mathematics — higher order
8439. F8439 Curriculum-only — higher-order differential equation with constant coefficient
8440. F8440 Data Mining & Databases — order model
8441. F8441 Mathematics — derivative of higher order
8442. F8442 Other/Unknown — horn clause
8443. F8443 Curriculum-only — model-checking small protocol with tla
8444. F8444 Distributed Systems & Cloud — concurrent
8445. F8445 Curriculum-only — concurrent skip list are named
8446. F8446 Distributed Systems & Cloud — concurrent access
8447. F8447 Curriculum-only — consistency model and the cap theorem
8448. F8448 Distributed Systems & Cloud — test-and-set
8449. F8449 ML & AI — state model
8450. F8450 Operating Systems — concurrent caching
8451. F8451 Curriculum-only — memory consistency model and synchronisation primitive
8452. F8452 Other/Unknown — negative index
8453. F8453 Computer Networks — secondary paths
8454. F8454 Curriculum-only — read from secondary report while building this curriculum
8455. F8455 Data Mining & Databases — secondary index
8456. F8456 Curriculum-only — primary and secondary index
8457. F8457 Other/Unknown — random access to secondary
8458. F8458 Distributed Systems & Cloud — department of electrical engineering
8459. F8459 ML & AI — inference
8460. F8460 Algorithms & Theory of CS — computational complexity of graphical model inference
8461. F8461 Curriculum-only — common llm inference
8462. F8462 Data Mining & Databases — saw earlier
8463. F8463 Curriculum-only — python for system work
8464. F8464 Information Theory & Coding — inference strategy
8465. F8465 ML & AI — amortized inference
8466. F8466 Curriculum-only — entropy and kl divergence
8467. F8467 Information Theory & Coding — differential entropy
8468. F8468 Algorithms & Theory of CS — string of length
8469. F8469 Information Theory & Coding — converse coding theorem
8470. F8470 ML & AI — probability table
8471. F8471 Mathematics — confidence region
8472. F8472 ML & AI — bayesian perspective
8473. F8473 Mathematics — Bayesian probability
8474. F8474 Other/Unknown — dog bark
8475. F8475 Algorithms & Theory of CS — quantifier
8476. F8476 Curriculum-only — quantifier and their negation
8477. F8477 Data Mining & Databases — existential quantifier
8478. F8478 Other/Unknown — quantifier equivalence
8479. F8479 Algorithms & Theory of CS — Temporal reasoning
8480. F8480 Data Mining & Databases — temporal database
8481. F8481 Operating Systems — spatial and temporal
8482. F8482 Other/Unknown — spatio-temporal
8483. F8483 Curriculum-only — normal form for temporal data
8484. F8484 Other/Unknown — spatio-temporal data
8485. F8485 Signal/Image/Audio/Video Processing — berthold horn
8486. F8486 Other/Unknown — medical image
8487. F8487 Signal/Image/Audio/Video Processing — image reconstruction
8488. F8488 Curriculum-only — image reconstruction and deblurring
8489. F8489 Signal/Image/Audio/Video Processing — index start
8490. F8490 ML & AI — subsampling
8491. F8491 Curriculum-only — shrinkage and subsampling
8492. F8492 ML & AI — visual system
8493. F8493 Other/Unknown — vision and speech
8494. F8494 Signal/Image/Audio/Video Processing — direct motion vision
8495. F8495 Mathematics — manufactured
8496. F8496 Curriculum-only — engineered and not manufactured
8497. F8497 Other/Unknown — patent
8498. F8498 Information Theory & Coding — welch
8499. F8499 Curriculum-only — pooled and welch
8500. F8500 Data Mining & Databases — welch bound
8501. F8501 Information Theory & Coding — welch-berlekamp
8502. F8502 Mathematics — png
8503. F8503 Computer Architecture — png file
8504. F8504 Signal/Image/Audio/Video Processing — edge detectors
8505. F8505 Algorithms & Theory of CS — subroutine
8506. F8506 Signal/Image/Audio/Video Processing — edge and line
8507. F8507 ML & AI — human
8508. F8508 Curriculum-only — human-in-the-loop
8509. F8509 Data Mining & Databases — full text
8510. F8510 Distributed Systems & Cloud — human genome
8511. F8511 Information Theory & Coding — laryngeal
8512. F8512 Mathematics — clarification
8513. F8513 NLP & Speech — human evaluation
8514. F8514 Curriculum-only — human evaluation design
8515. F8515 NLP & Speech — language acquisition
8516. F8516 Other/Unknown — everyday life
8517. F8517 Mathematics — estimated
8518. F8518 Other/Unknown — human development
8519. F8519 NLP & Speech — recognition
8520. F8520 Curriculum-only — constitutional recognition of privacy
8521. F8521 Data Mining & Databases — character recognition
8522. F8522 ML & AI — handwriting recognition
8523. F8523 NLP & Speech — baseform
8524. F8524 Other/Unknown — biometric recognition
8525. F8525 Signal/Image/Audio/Video Processing — human vision
8526. F8526 Software Engineering — base pointer
8527. F8527 Operating Systems — stack pointer
8528. F8528 Software Engineering — buchi automaton
8529. F8529 Algorithms & Theory of CS — abstract base
8530. F8530 Curriculum-only — inherit only from abstract
8531. F8531 Mathematics — abstract set
8532. F8532 Software Engineering — abstract domain
8533. F8533 Distributed Systems & Cloud — pattern matching
8534. F8534 Algorithms & Theory of CS — persistent data structure
8535. F8535 Mathematics — pattern matching algorithms
8536. F8536 Software Engineering — graphics
8537. F8537 Distributed Systems & Cloud — bioinformatics
8538. F8538 ML & AI — graphics processing
8539. F8539 Computer Networks — jpg file
8540. F8540 ML & AI — science artificial intelligence graphics
8541. F8541 Operating Systems — graphics card
8542. F8542 Other/Unknown — Graphics Libraries and APIs (e.g., DirectX; SDL; OpenGL; Metal; Vulkan; WebGL)
8543. F8543 Software Engineering — great job
8544. F8544 Curriculum-only — doubly linked sharing list
8545. F8545 Distributed Systems & Cloud — load-linked
8546. F8546 Signal/Image/Audio/Video Processing — linked data
8547. F8547 Software Engineering — dynamic data structure
8548. F8548 ML & AI — basis pursuit
8549. F8549 Software Engineering — rail security
8550. F8550 Operating Systems — stack smashing
8551. F8551 Software Engineering — security attacks
8552. F8552 Mathematics — unification
8553. F8553 ML & AI — regularization
8554. F8554 Curriculum-only — min-norm regularization for linear regression
8555. F8555 ML & AI — advance in computational
8556. F8556 Curriculum-only — artificial intelligence and neural network
8557. F8557 ML & AI — activation function
8558. F8558 Mathematics — entropy regularization
8559. F8559 Other/Unknown — adaptive
8560. F8560 Computer Networks — adaptive network
8561. F8561 Curriculum-only — adaptive method are named
8562. F8562 Data Mining & Databases — adaptive query processing
8563. F8563 Information Theory & Coding — equalization
8564. F8564 ML & AI — adaptive filtering
8565. F8565 Mathematics — adaptive learning
8566. F8566 Other/Unknown — adaptive regularization
8567. F8567 Curriculum-only — behavioral data analysis
8568. F8568 Data Mining & Databases — Exploratory data analysis
8569. F8569 Other/Unknown — cluster analysis
8570. F8570 Curriculum-only — cluster analysis and clustering analysis
8571. F8571 Data Mining & Databases — anomaly detection
8572. F8572 Curriculum-only — clustering as data mining
8573. F8573 Data Mining & Databases — association rule mining
8574. F8574 Curriculum-only — association rule mining and classification
8575. F8575 Data Mining & Databases — comparison of data mining
8576. F8576 Distributed Systems & Cloud — scalable data mining
8577. F8577 HS ComputerScience Class XII / Unit 3: Database Management — structured query language
8578. F8578 Algorithms & Theory of CS — indegree
8579. F8579 Computer Architecture — db2
8580. F8580 Computer Networks — app server
8581. F8581 Algorithms & Theory of CS — asp johnson
8582. F8582 Computer Networks — aspx
8583. F8583 Computer Networks — sitemap
8584. F8584 Computer Networks — xml file
8585. F8585 Cryptography & Security — authentication protocol
8586. F8586 Curriculum-only — attack on web server
8587. F8587 Curriculum-only — secure the web server
8588. F8588 Data Mining & Databases — create table
8589. F8589 Curriculum-only — cost estimate in query optimization
8590. F8590 Data Mining & Databases — query execution
8591. F8591 Distributed Systems & Cloud — apache
8592. F8592 Curriculum-only — google chubby and apache zookeeper
8593. F8593 Distributed Systems & Cloud — design of apache cassandra
8594. F8594 Computer Networks — Data integrity
8595. F8595 Curriculum-only — ciphertext integrity
8596. F8596 Distributed Systems & Cloud — academic integrity
8597. F8597 Computer Architecture — academic integrity policy
8598. F8598 Distributed Systems & Cloud — microsoft
8599. F8599 Computer Networks — microsoft azure
8600. F8600 Cryptography & Security — ibm and microsoft
8601. F8601 Distributed Systems & Cloud — microsoft dryadlinq
8602. F8602 Computer Architecture — clk
8603. F8603 Curriculum-only — first-class function and module
8604. F8604 Curriculum-only — module-lwe
8605. F8605 Curriculum-only — transaction processing module
8606. F8606 Distributed Systems & Cloud — cnt
8607. F8607 Computer Architecture — inter row cnt
8608. F8608 Distributed Systems & Cloud — kit
8609. F8609 Algorithms & Theory of CS — development kit
8610. F8610 Distributed Systems & Cloud — mkfifo
8611. F8611 Data Mining & Databases — virtualized environment
8612. F8612 Distributed Systems & Cloud — web-data management
8613. F8613 Information Theory & Coding — dos
8614. F8614 ML & AI — classifier
8615. F8615 Curriculum-only — choosing among classifier
8616. F8616 Data Mining & Databases — description length
8617. F8617 ML & AI — adaptive boosting
8618. F8618 ML & AI — margin classifier
8619. F8619 Curriculum-only — soft margin classifier
8620. F8620 ML & AI — misclassification
8621. F8621 Data Mining & Databases — misclassification error
8622. F8622 ML & AI — mixture model
8623. F8623 Curriculum-only — mixture model and the em algorithm
8624. F8624 ML & AI — na ve bayes
8625. F8625 Curriculum-only — two-class and multi-class least-square classifier
8626. F8626 ML & AI — type of mixture model
8627. F8627 Mathematics — estimation
8628. F8628 Computer Networks — software estimation
8629. F8629 Curriculum-only — advantage estimation
8630. F8630 Data Mining & Databases — linear measurement
8631. F8631 ML & AI — density estimation
8632. F8632 Curriculum-only — non-parametric density estimation
8633. F8633 ML & AI — gradient ascent
8634. F8634 Mathematics — bayes estimator
8635. F8635 Curriculum-only — jury stability test
8636. F8636 Mathematics — leaf
8637. F8637 Algorithms & Theory of CS — deterministic algorithm
8638. F8638 Curriculum-only — leaf in log
8639. F8639 ML & AI — root node
8640. F8640 Mathematics — marking
8641. F8641 Curriculum-only — object marking
8642. F8642 Mathematics — complexity analysis
8643. F8643 Curriculum-only — normal density and discriminant function
8644. F8644 Mathematics — normal random variable
8645. F8645 Curriculum-only — simpson integration
8646. F8646 Mathematics — composite simpson
8647. F8647 Curriculum-only — simpson rule for evaluating
8648. F8648 Mathematics — standard normal random variable
8649. F8649 Algorithms & Theory of CS — reachability
8650. F8650 Mathematics — t2k
8651. F8651 Curriculum-only — unbiased gradient
8652. F8652 Data Mining & Databases — mutually unbiased basis
8653. F8653 ML & AI — unbiased estimation
8654. F8654 Mathematics — vector space
8655. F8655 Curriculum-only — direct sum of vector space
8656. F8656 Information Theory & Coding — field element
8657. F8657 Mathematics — bilinear form
8658. F8658 Curriculum-only — inner-product fe as an instance
8659. F8659 Mathematics — l2 inner product
8660. F8660 Curriculum-only — pythagorean identity sin
8661. F8661 Mathematics — polyhedron
8662. F8662 Curriculum-only — cone and polyhedra
8663. F8663 Data Mining & Databases — polygon
8664. F8664 Algorithms & Theory of CS — convex polygon
8665. F8665 Mathematics — pythagorean triple
8666. F8666 Curriculum-only — stability analysis of system of linear difference equation
8667. F8667 Mathematics — schur complement
8668. F8668 Curriculum-only — underdetermined system of linear equation
8669. F8669 Mathematics — tetrahedron
8670. F8670 Computer Networks — lecture18
8671. F8671 Distributed Systems & Cloud — login
8672. F8672 Computer Networks — login name
8673. F8673 Mathematics — web traffic
8674. F8674 NLP & Speech — homer simpson
8675. F8675 Computer Architecture — lab4 labkit
8676. F8676 NLP & Speech — marker
8677. F8677 Curriculum-only — chandy lamport snapshot algorithm with marker
8678. F8678 NLP & Speech — multiple classifiers
8679. F8679 Curriculum-only — ppo and dpo
8680. F8680 NLP & Speech — probabilistic classifier
8681. F8681 Curriculum-only — density estimation and probabilistic classifier
8682. F8682 NLP & Speech — questioned
8683. F8683 Distributed Systems & Cloud — join
8684. F8684 Computer Networks — join order
8685. F8685 Curriculum-only — complex join
8686. F8686 Data Mining & Databases — equi-join
8687. F8687 Curriculum-only — theta and equi-join
8688. F8688 Data Mining & Databases — hash join
8689. F8689 Curriculum-only — merge and hash join
8690. F8690 Data Mining & Databases — join operator
8691. F8691 Curriculum-only — join ordering is hard
8692. F8692 Data Mining & Databases — nested loop join
8693. F8693 Curriculum-only — indexed nested loop join
8694. F8694 Distributed Systems & Cloud — database join
8695. F8695 NLP & Speech — semi-parametric classifier
8696. F8696 ML & AI — gaussian mixture
8697. F8697 Mathematics — univariate
8698. F8698 Curriculum-only — univariate polynomial and rational function
8699. F8699 ML & AI — univariate algorithm
8700. F8700 Mathematics — univariate function
8701. F8701 NLP & Speech — sequential estimation
8702. F8702 Operating Systems — mobile app server
8703. F8703 Other/Unknown — control-flow integrity
8704. F8704 Computer Architecture — data sheet
8705. F8705 Other/Unknown — control loop
8706. F8706 Computer Networks — resource discovery
8707. F8707 Curriculum-only — benjamini hochberg procedure for the false discovery rate
8708. F8708 Mathematics — agrawal kayal saxena
8709. F8709 Other/Unknown — higher dimensional
8710. F8710 Curriculum-only — block identification by tag
8711. F8711 NLP & Speech — face identification
8712. F8712 Other/Unknown — k-l expansion
8713. F8713 Algorithms & Theory of CS — full modal
8714. F8714 Data Mining & Databases — normal modal system
8715. F8715 Mathematics — asymptotic stability
8716. F8716 Other/Unknown — modal analysis
8717. F8717 Cryptography & Security — control hijacking
8718. F8718 Curriculum-only — sharing threat intelligence
8719. F8719 Other/Unknown — defense
8720. F8720 Cryptography & Security — privilege separation
8721. F8721 Curriculum-only — limit and defense
8722. F8722 Other/Unknown — web information
8723. F8723 Signal/Image/Audio/Video Processing — adaptive filters
8724. F8724 Curriculum-only — echo-state
8725. F8725 Signal/Image/Audio/Video Processing — least-square estimate
8726. F8726 Mathematics — bayes least-square estimate
8727. F8727 Signal/Image/Audio/Video Processing — lter
8728. F8728 Information Theory & Coding — simpli ed
8729. F8729 NLP & Speech — predictor coe cient
8730. F8730 Signal/Image/Audio/Video Processing — complex exponential
8731. F8731 Mathematics — linear combination of complex
8732. F8732 Curriculum-only — sum of sinusoid of equal frequency
8733. F8733 Information Theory & Coding — frequency response of lti
8734. F8734 Signal/Image/Audio/Video Processing — dt frequency response
8735. F8735 Mathematics — undetermined
8736. F8736 Signal/Image/Audio/Video Processing — lattice lter
8737. F8737 Mathematics — process noise
8738. F8738 Signal/Image/Audio/Video Processing — nite di erence
8739. F8739 Distributed Systems & Cloud — master
8740. F8740 Computer Networks — master file
8741. F8741 Curriculum-only — master fail the system run read-only
8742. F8742 Distributed Systems & Cloud — e-master
8743. F8743 Curriculum-only — slave is promoted
8744. F8744 Mathematics — minor
8745. F8745 Computer Architecture — state minor
8746. F8746 Distributed Systems & Cloud — minor program
8747. F8747 Information Theory & Coding — coll
8748. F8748 Mathematics — principal minor
8749. F8749 Information Theory & Coding — node attempt success coll
8750. F8750 Mathematics — bernoulli distribution
8751. F8751 Algorithms & Theory of CS — binomial distribution with mean
8752. F8752 ML & AI — likelihood function
8753. F8753 Mathematics — negative binomial distribution
8754. F8754 NLP & Speech — humanity
8755. F8755 Operating Systems — data register
8756. F8756 Information Theory & Coding — pulse
8757. F8757 Computer Architecture — pulse count
8758. F8758 Information Theory & Coding — pulse coded modulation
8759. F8759 Mathematics — relevant
8760. F8760 ML & AI — recommender
8761. F8761 Mathematics — reflected
8762. F8762 Other/Unknown — critical success factor
8763. F8763 Signal/Image/Audio/Video Processing — quantization noise
8764. F8764 Curriculum-only — optimization for signal estimation
8765. F8765 Signal/Image/Audio/Video Processing — training neural network
8766. F8766 Algorithms & Theory of CS — video game
8767. F8767 Computer Architecture — film and video
8768. F8768 Computer Networks — video conferencing
8769. F8769 Curriculum-only — digital picture and video
8770. F8770 Data Mining & Databases — surveillance
8771. F8771 Algorithms & Theory of CS — surveillance cameras
8772. F8772 Data Mining & Databases — video to watch
8773. F8773 Distributed Systems & Cloud — digital video
8774. F8774 Information Theory & Coding — buffering
8775. F8775 Curriculum-only — buffering of block
8776. F8776 Information Theory & Coding — compressed images
8777. F8777 Data Mining & Databases — television networks
8778. F8778 Information Theory & Coding — television transmission
8779. F8779 ML & AI — video streams
8780. F8780 Mathematics — road
8781. F8781 Algorithms & Theory of CS — disjoint road
8782. F8782 Computer Architecture — icy
8783. F8783 Computer Networks — direct road
8784. F8784 Mathematics — absorber
8785. F8785 Operating Systems — bus video
8786. F8786 Signal/Image/Audio/Video Processing — image and video
8787. F8787 ML & AI — autoregressive
8788. F8788 Curriculum-only — autoregressive flow
8789. F8789 ML & AI — prediction error
8790. F8790 Signal/Image/Audio/Video Processing — autoregressive process
8791. F8791 Information Theory & Coding — additive noise
8792. F8792 Signal/Image/Audio/Video Processing — spectral estimation
8793. F8793 Mathematics — karhunen
8794. F8794 Software Engineering — alf
8795. F8795 Computer Architecture — fine art
8796. F8796 Other/Unknown — social
8797. F8797 Computer Networks — network effect
8798. F8798 Curriculum-only — biometric authentication and social engineering
8799. F8799 Data Mining & Databases — social network
8800. F8800 Computer Networks — friendship
8801. F8801 Cryptography & Security — social graph
8802. F8802 Curriculum-only — crawler and the social graph
8803. F8803 Data Mining & Databases — mining
8804. F8804 Cryptography & Security — distributed mining
8805. F8805 Curriculum-only — hard mining
8806. F8806 Data Mining & Databases — knowledge mining
8807. F8807 Curriculum-only — association-rule or sequence-mining
8808. F8808 Data Mining & Databases — text mining
8809. F8809 Distributed Systems & Cloud — analytics
8810. F8810 Curriculum-only — analytics database
8811. F8811 Data Mining & Databases — analytics help
8812. F8812 Distributed Systems & Cloud — algorithm and analytics
8813. F8813 Curriculum-only — expressed as pass over distributed data
8814. F8814 Distributed Systems & Cloud — distributed data management
8815. F8815 ML & AI — algorithm in data mining
8816. F8816 Mathematics — download
8817. F8817 Computer Networks — unzip
8818. F8818 Data Mining & Databases — download and install
8819. F8819 Mathematics — contact
8820. F8820 Algorithms & Theory of CS — contact area
8821. F8821 Mathematics — contact force
8822. F8822 Computer Networks — game theory ii
8823. F8823 Mathematics — welcome
8824. F8824 NLP & Speech — natural language processing
8825. F8825 Mathematics — graduate
8826. F8826 Algorithms & Theory of CS — combinatorial theory
8827. F8827 Data Mining & Databases — introduce graduate
8828. F8828 Distributed Systems & Cloud — post graduate
8829. F8829 ML & AI — introductory graduate
8830. F8830 Mathematics — extremal volume ellipsoid
8831. F8831 Algorithms & Theory of CS — introductory graduate level
8832. F8832 Cryptography & Security — proposed syllabus
8833. F8833 Curriculum-only — nptel syllabus of database design
8834. F8834 Algorithms & Theory of CS — discrete math
8835. F8835 Cryptography & Security — biometrics
8836. F8836 Curriculum-only — audience and prerequisite
8837. F8837 Data Mining & Databases — prerequisite and knowledge
8838. F8838 Distributed Systems & Cloud — official prerequisite
8839. F8839 Information Theory & Coding — voice
8840. F8840 Computer Networks — central office
8841. F8841 Information Theory & Coding — voice traffic
8842. F8842 Mathematics — maturity
8843. F8843 Computer Networks — maturity model
8844. F8844 Curriculum-only — maturity and continuous improvement strategy
8845. F8845 Mathematics — meeting
8846. F8846 Curriculum-only — meeting of database
8847. F8847 Mathematics — faq
8848. F8848 Mathematics — bayesian updating
8849. F8849 Curriculum-only — bayesian updating and decision under uncertainty
8850. F8850 Mathematics — beta distribution
8851. F8851 Curriculum-only — beta distribution derived from their story
8852. F8852 ML & AI — bayesian parameter estimation
8853. F8853 NLP & Speech — em in nlp
8854. F8854 Operating Systems — check-off meeting
8855. F8855 Other/Unknown — contact models
8856. F8856 Computer Networks — american economic
8857. F8857 Curriculum-only — economic value of privacy
8858. F8858 Data Mining & Databases — Economic impact
8859. F8859 Mathematics — income
8860. F8860 Cryptography & Security — money supply
8861. F8861 Data Mining & Databases — gross national income
8862. F8862 Mathematics — investment
8863. F8863 Cryptography & Security — stock exchange
8864. F8864 Curriculum-only — security investment
8865. F8865 Mathematics — investment strategy
8866. F8866 Computer Networks — pareto optimal
8867. F8867 Curriculum-only — pareto severity
8868. F8868 Mathematics — vector optimization
8869. F8869 NLP & Speech — income tax
8870. F8870 Operating Systems — competing economic interest
8871. F8871 Other/Unknown — capital investment
8872. F8872 Data Mining & Databases — model of human behavior
8873. F8873 Other/Unknown — humanity and social
8874. F8874 Information Theory & Coding — morphology and phonology
8875. F8875 NLP & Speech — level morphology
8876. F8876 Other/Unknown — beach morphology
8877. F8877 Mathematics — info
8878. F8878 Curriculum-only — multiget call to the tweet info
8879. F8879 Data Mining & Databases — database system
8880. F8880 Algorithms & Theory of CS — regular language
8881. F8881 Computer Networks — extensible markup language
8882. F8882 Curriculum-only — database system with the help
8883. F8883 Data Mining & Databases — dewitt
8884. F8884 Distributed Systems & Cloud — time info
8885. F8885 Mathematics — expected value of perfect
8886. F8886 NLP & Speech — speaker recognition
8887. F8887 Mathematics — speaker identification
8888. F8888 NLP & Speech — word segmentation
8889. F8889 Operating Systems — principle of computer
8890. F8890 Curriculum-only — end-to-end principle of computer network
8891. F8891 Operating Systems — principle of computer system
8892. F8892 Other/Unknown — frequent pattern
8893. F8893 Signal/Image/Audio/Video Processing — george verghese
8894. F8894 Mathematics — motivating
8895. F8895 Curriculum-only — motivating example from web-crawling
8896. F8896 Mathematics — vanishing
8897. F8897 Curriculum-only — vanishing and exploding gradient
8898. F8898 Mathematics — vanishing gradient
8899. F8899 Other/Unknown — calibration
8900. F8900 Curriculum-only — calibration to local data is the practice that matter
8901. F8901 Signal/Image/Audio/Video Processing — camera calibration
8902. F8902 Mathematics — quadratic equation
8903. F8903 Curriculum-only — complex number and quadratic equation
8904. F8904 Signal/Image/Audio/Video Processing — binocular stereo
8905. F8905 Mathematics — abc
8906. F8906 Information Theory & Coding — abca
8907. F8907 Mathematics — bac
8908. F8908 Signal/Image/Audio/Video Processing — binocular disparity
8909. F8909 Software Engineering — allocation
8910. F8910 Computer Networks — bandwidth allocation
8911. F8911 Curriculum-only — allocation in distributed database
8912. F8912 Distributed Systems & Cloud — number of thread
8913. F8913 Data Mining & Databases — desire
8914. F8914 Distributed Systems & Cloud — number of processor
8915. F8915 Software Engineering — allocate
8916. F8916 Operating Systems — write-allocate
8917. F8917 Curriculum-only — no-write-allocate
8918. F8918 Software Engineering — allocation site
8919. F8919 Curriculum-only — integrity and confidentiality
8920. F8920 Software Engineering — data object modeling
8921. F8921 Curriculum-only — keys and integrity constraint
8922. F8922 Software Engineering — lexical analysis
8923. F8923 Algorithms & Theory of CS — list labeling
8924. F8924 Software Engineering — origin policy
8925. F8925 Cryptography & Security — same-origin policy
8926. F8926 Software Engineering — perl
8927. F8927 Mathematics — growth
8928. F8928 Algorithms & Theory of CS — asymptotic growth
8929. F8929 Curriculum-only — fp-growth
8930. F8930 Data Mining & Databases — asymptotic complexity
8931. F8931 Mathematics — exponential growth
8932. F8932 Curriculum-only — growth rate from log
8933. F8933 Mathematics — natural growth
8934. F8934 Other/Unknown — cell growth
8935. F8935 Curriculum-only — cell-growth model
8936. F8936 Software Engineering — pool
8937. F8937 Computer Networks — collusion
8938. F8938 Cryptography & Security — mining pool
8939. F8939 Curriculum-only — connection pool
8940. F8940 Distributed Systems & Cloud — node pool
8941. F8941 Mathematics — boiling
8942. F8942 NLP & Speech — pool of resource
8943. F8943 Operating Systems — bu er
8944. F8944 Data Mining & Databases — bu er pool
8945. F8945 Information Theory & Coding — bu ers
8946. F8946 Mathematics — busy
8947. F8947 Distributed Systems & Cloud — buffer cache
8948. F8948 Software Engineering — nibble
8949. F8949 Mathematics — wire
8950. F8950 Algorithms & Theory of CS — truly random
8951. F8951 Data Mining & Databases — seed
8952. F8952 Curriculum-only — seed corpus
8953. F8953 Mathematics — heading
8954. F8954 Other/Unknown — quantum wires
8955. F8955 Software Engineering — ps1
8956. F8956 Data Mining & Databases — database internal
8957. F8957 Curriculum-only — boolean indexing
8958. F8958 Data Mining & Databases — indexing and searching
8959. F8959 Curriculum-only — storage and indexing structure
8960. F8960 Distributed Systems & Cloud — michael
8961. F8961 Computer Architecture — michael huh
8962. F8962 Data Mining & Databases — samuel
8963. F8963 Distributed Systems & Cloud — cbe
8964. F8964 Curriculum-only — trusted execution environment
8965. F8965 Distributed Systems & Cloud — ibm corp
8966. F8966 Computer Architecture — nlocal
8967. F8967 Distributed Systems & Cloud — balancing
8968. F8968 Curriculum-only — balancing and red-black tree
8969. F8969 Distributed Systems & Cloud — data dependence
8970. F8970 Information Theory & Coding — send data
8971. F8971 ML & AI — zero-based indexing
8972. F8972 Mathematics — michael artin
8973. F8973 Curriculum-only — cos repeat
8974. F8974 Information Theory & Coding — irregular repeat
8975. F8975 Curriculum-only — go-back-n and selective repeat
8976. F8976 Mathematics — algorithm terminate
8977. F8977 Algorithms & Theory of CS — arc consistency
8978. F8978 Curriculum-only — perimeter-centric
8979. F8979 Mathematics — circular arc
8980. F8980 Curriculum-only — iterating on benchmark
8981. F8981 Mathematics — line search
8982. F8982 Curriculum-only — wolfe-condition line-search algorithm
8983. F8983 Mathematics — inexact line search
8984. F8984 Computer Networks — originally taught
8985. F8985 Curriculum-only — cassandra are taught
8986. F8986 Curriculum-only — taught in python with pymc
8987. F8987 Data Mining & Databases — data science
8988. F8988 Curriculum-only — data science in hydroclimatology
8989. F8989 Data Mining & Databases — taught jointly
8990. F8990 Distributed Systems & Cloud — system for data science
8991. F8991 ML & AI — algorithm and data
8992. F8992 Mathematics — undergraduate
8993. F8993 Algorithms & Theory of CS — morris
8994. F8994 Cryptography & Security — unprepared
8995. F8995 Curriculum-only — knuth morris pratt algorithm
8996. F8996 Mathematics — arthur
8997. F8997 Distributed Systems & Cloud — core
8998. F8998 Computer Architecture — processing core
8999. F8999 Computer Networks — cisco
9000. F9000 Cryptography & Security — hard core predicate
9001. F9001 Curriculum-only — core loop
9002. F9002 Data Mining & Databases — core evaluator
9003. F9003 Distributed Systems & Cloud — core graduate subject
9004. F9004 Curriculum-only — server should be stateless
9005. F9005 Distributed Systems & Cloud — stateful
9006. F9006 Mathematics — algebra ii
9007. F9007 NLP & Speech — michael collin
9008. F9008 Operating Systems — michael schroeder
9009. F9009 Other/Unknown — core component
9010. F9010 Curriculum-only — core component with data model
9011. F9011 Other/Unknown — foundation of data science
9012. F9012 Mathematics — concerning
9013. F9013 Curriculum-only — computation concerning subspace
9014. F9014 Mathematics — evidence
9015. F9015 Curriculum-only — digital forensics at the level of evidence handling
9016. F9016 ML & AI — bacterial infection
9017. F9017 Mathematics — scientific
9018. F9018 Computer Networks — scientific python
9019. F9019 Cryptography & Security — scientific american
9020. F9020 Curriculum-only — scientific notation in base
9021. F9021 Data Mining & Databases — modern scientific
9022. F9022 Information Theory & Coding — scientific data
9023. F9023 Distributed Systems & Cloud — scientific data model
9024. F9024 Mathematics — scientific and engineering
9025. F9025 Other/Unknown — contemporary
9026. F9026 Mathematics — conceptual
9027. F9027 Curriculum-only — conceptual and internal level
9028. F9028 Mathematics — conceptual understanding
9029. F9029 Curriculum-only — conceptual understanding of bayesian inference
9030. F9030 Other/Unknown — offered
9031. F9031 Mathematics — s1 and s2
9032. F9032 Other/Unknown — the evidence approximation
9033. F9033 Signal/Image/Audio/Video Processing — michael mermelstein
9034. F9034 Software Engineering — administration
9035. F9035 Cryptography & Security — computer security
9036. F9036 Distributed Systems & Cloud — cyber security
9037. F9037 Cryptography & Security — cryptography
9038. F9038 Algorithms & Theory of CS — computer science cryptography theory
9039. F9039 Computer Networks — data encryption standard
9040. F9040 Cryptography & Security — bilinear map
9041. F9041 Cryptography & Security — function pseudo-random generator
9042. F9042 Cryptography & Security — pseudo-random function
9043. F9043 Cryptography & Security — blockchain security
9044. F9044 Cryptography & Security — direction in blockchain
9045. F9045 Cryptography & Security — network security
9046. F9046 Cryptography & Security — Security analysis: safety and liveness in the presence of hostile or buggy behaviors by other parties; required properties of communication mechanisms (for example lack of cross-layer leakage), input screening, rate limiting
9047. F9047 Cryptography & Security — yao security
9048. F9048 Curriculum-only — articulate cyber security governance
9049. F9049 Curriculum-only — cyber security operation
9050. F9050 Curriculum-only — incentive problem and free riding
9051. F9051 Curriculum-only — organisational view of cyber security with the human
9052. F9052 Computer Networks — phishing
9053. F9053 Curriculum-only — source course name blockchain
9054. F9054 Data Mining & Databases — discrete logarithm problem
9055. F9055 Cryptography & Security — hyper-elliptic curve cryptography
9056. F9056 Data Mining & Databases — goldwasser
9057. F9057 Cryptography & Security — goldwasser-micali encryption goldreich-levin theorem
9058. F9058 Curriculum-only — goldwasser micali xor-homomorphic scheme
9059. F9059 Data Mining & Databases — identity-based encryption
9060. F9060 Distributed Systems & Cloud — distributed denial of service
9061. F9061 Curriculum-only — default credential on iot device
9062. F9062 Distributed Systems & Cloud — ms in cyber security
9063. F9063 Cryptography & Security — native client
9064. F9064 Curriculum-only — gvisor-style sandbox
9065. F9065 Distributed Systems & Cloud — network traffic
9066. F9066 Cryptography & Security — bitcoin
9067. F9067 Curriculum-only — bitcoin as the application context
9068. F9068 Data Mining & Databases — ecdsa
9069. F9069 Cryptography & Security — ecdsa signature
9070. F9070 Curriculum-only — dsa and ecdsa
9071. F9071 Distributed Systems & Cloud — bitcoin and blockchain
9072. F9072 Cryptography & Security — p2p computing
9073. F9073 Distributed Systems & Cloud — peer-to-peer computing
9074. F9074 Cryptography & Security — logging of critical event
9075. F9075 Curriculum-only — logging and recovery
9076. F9076 Data Mining & Databases — log record
9077. F9077 Curriculum-only — compensation log record
9078. F9078 Distributed Systems & Cloud — security in distributed system
9079. F9079 Curriculum-only — version vector for replicated data
9080. F9080 Information Theory & Coding — network and computer
9081. F9081 Algorithms & Theory of CS — rivest
9082. F9082 ML & AI — simon
9083. F9083 Mathematics — birthday attack
9084. F9084 Curriculum-only — birthday attack and the random-oracle model
9085. F9085 Mathematics — gtx
9086. F9086 Algorithms & Theory of CS — sample realization
9087. F9087 Curriculum-only — open-source realisation
9088. F9088 Information Theory & Coding — behavioral realization
9089. F9089 ML & AI — cut set
9090. F9090 Mathematics — rsa cryptosystem
9091. F9091 NLP & Speech — phonological rule
9092. F9092 Operating Systems — bitcoin and tor
9093. F9093 Other/Unknown — bitcoin blockchain
9094. F9094 Cryptography & Security — scripting
9095. F9095 Other/Unknown — cryptography and security
9096. F9096 Cryptography & Security — cyberattacks
9097. F9097 Curriculum-only — cyber insurance as transfer
9098. F9098 Distributed Systems & Cloud — cyber network data processing
9099. F9099 Other/Unknown — cyber-physical
9100. F9100 Curriculum-only — fault attack on crt-rsa
9101. F9101 Other/Unknown — hardness
9102. F9102 Curriculum-only — hardness of improving on known ratio
9103. F9103 ML & AI — hardness of inference
9104. F9104 Other/Unknown — hardness of approximation
9105. F9105 Cryptography & Security — assymetric key cryptography
9106. F9106 Operating Systems — symmetric key cryptography
9107. F9107 Information Theory & Coding — cliff
9108. F9108 Mathematics — prentice hall inc
9109. F9109 Information Theory & Coding — cramer-rao lower bound
9110. F9110 ML & AI — maximum likelihood
9111. F9111 Curriculum-only — large-sample property of maximum likelihood estimator
9112. F9112 Information Theory & Coding — maximum likelihood decoding
9113. F9113 ML & AI — likelihood estimation
9114. F9114 Mathematics — crame r-rao bound
9115. F9115 ML & AI — observed data
9116. F9116 Mathematics — prior information
9117. F9117 Other/Unknown — expectation maximization
9118. F9118 NLP & Speech — expectation maximization algorithm
9119. F9119 Other/Unknown — factor analysis
9120. F9120 Mathematics — regression
9121. F9121 Algorithms & Theory of CS — regression and relative
9122. F9122 Curriculum-only — clustering and regression
9123. F9123 Data Mining & Databases — adding variable
9124. F9124 Curriculum-only — standard error and an interval
9125. F9125 Data Mining & Databases — Statistical software
9126. F9126 ML & AI — identifiability
9127. F9127 Curriculum-only — parameter identifiability
9128. F9128 ML & AI — kernel regression
9129. F9129 Data Mining & Databases — panel
9130. F9130 Cryptography & Security — digest
9131. F9131 ML & AI — missing data
9132. F9132 Data Mining & Databases — dealing with missing data
9133. F9133 ML & AI — nonlinear regression
9134. F9134 Curriculum-only — dealing with overfitting via regularization
9135. F9135 Data Mining & Databases — curse of dimensionality
9136. F9136 Curriculum-only — curse of dimensionality for clustering
9137. F9137 ML & AI — overfitting and underfitting
9138. F9138 Curriculum-only — regularized and constrained least square
9139. F9139 ML & AI — feature vector
9140. F9140 Curriculum-only — recursive partition of the feature space
9141. F9141 ML & AI — kernel trick
9142. F9142 Curriculum-only — matrix and kernel function
9143. F9143 ML & AI — radial basis kernel
9144. F9144 Algorithms & Theory of CS — horizon ridge
9145. F9145 ML & AI — softmax regression
9146. F9146 Curriculum-only — training and test set
9147. F9147 Data Mining & Databases — test set prediction
9148. F9148 ML & AI — variance for regression
9149. F9149 Mathematics — background
9150. F9150 Computer Networks — engineering background
9151. F9151 Curriculum-only — background of concentration inequality
9152. F9152 Distributed Systems & Cloud — background model
9153. F9153 ML & AI — background pixels
9154. F9154 Mathematics — background knowledge
9155. F9155 Curriculum-only — bayesian statistics as modern ai thinking
9156. F9156 Mathematics — detection theory
9157. F9157 Data Mining & Databases — multicollinearity
9158. F9158 Curriculum-only — multicollinearity and the variance inflation factor
9159. F9159 ML & AI — logistic
9160. F9160 Curriculum-only — logistic and poisson regression
9161. F9161 ML & AI — log-odd
9162. F9162 Curriculum-only — distributed least square and logistic regression
9163. F9163 Data Mining & Databases — regression tree
9164. F9164 ML & AI — classification error
9165. F9165 Curriculum-only — convex optimisation and gradient descent
9166. F9166 Distributed Systems & Cloud — spectral gradient descent
9167. F9167 ML & AI — coordinate descent
9168. F9168 Curriculum-only — learning-rate behaviour
9169. F9169 ML & AI — learning-rate schedule
9170. F9170 Data Mining & Databases — hidden neurons
9171. F9171 ML & AI — ndla
9172. F9172 Mathematics — analysis of gradient descent
9173. F9173 Data Mining & Databases — explanatory variable
9174. F9174 Mathematics — label
9175. F9175 Algorithms & Theory of CS — extract-min
9176. F9176 Computer Networks — label switching
9177. F9177 Curriculum-only — bell lapadula label
9178. F9178 Data Mining & Databases — estyval
9179. F9179 Distributed Systems & Cloud — mnr labeling algorithm
9180. F9180 ML & AI — dasgupta
9181. F9181 Algorithms & Theory of CS — anirban dasgupta
9182. F9182 ML & AI — image and label
9183. F9183 Data Mining & Databases — gradient boosting
9184. F9184 ML & AI — decision stump
9185. F9185 Cryptography & Security — security of voting
9186. F9186 Curriculum-only — primary-site and voting
9187. F9187 Distributed Systems & Cloud — voting protocol
9188. F9188 ML & AI — voting margin
9189. F9189 Mathematics — distance label
9190. F9190 Curriculum-only — counting of labelled
9191. F9191 Data Mining & Databases — labelled graph
9192. F9192 Mathematics — labelling
9193. F9193 Curriculum-only — sequence labelling for part of speech
9194. F9194 Mathematics — lack of identifiability
9195. F9195 Curriculum-only — lasso and ridge
9196. F9196 Mathematics — logistic equation
9197. F9197 Curriculum-only — logit link and odd ratio
9198. F9198 Mathematics — normality
9199. F9199 Curriculum-only — continued lecture on variant of gradient descent
9200. F9200 NLP & Speech — errn
9201. F9201 Other/Unknown — bayesian regression
9202. F9202 Curriculum-only — bayesian regression modeling
9203. F9203 Other/Unknown — classification and regression
9204. F9204 Curriculum-only — kernel function and kernel svm
9205. F9205 Other/Unknown — label propagation
9206. F9206 Curriculum-only — mathematical background and number theory
9207. F9207 Other/Unknown — modelling
9208. F9208 Curriculum-only — copula-based joint modelling
9209. F9209 NLP & Speech — n-gram
9210. F9210 ML & AI — supervised
9211. F9211 Curriculum-only — difference between supervised
9212. F9212 Distributed Systems & Cloud — supervision
9213. F9213 ML & AI — latexit
9214. F9214 Information Theory & Coding — autoregressive model
9215. F9215 Curriculum-only — autoregressive model order
9216. F9216 ML & AI — layer
9217. F9217 Algorithms & Theory of CS — output node
9218. F9218 Curriculum-only — broad objective is to understand how the layer fit
9219. F9219 Curriculum-only — stuffing and physical-layer coding violation
9220. F9220 Data Mining & Databases — backprop algorithm
9221. F9221 Distributed Systems & Cloud — abstraction layer
9222. F9222 Computer Networks — cross-layer protocol
9223. F9223 Information Theory & Coding — arq
9224. F9224 ML & AI — dense layer
9225. F9225 Curriculum-only — bias in embedding
9226. F9226 Data Mining & Databases — isomap
9227. F9227 Curriculum-only — nonlinear dimensionality reduction via uniform manifold approximation
9228. F9228 Data Mining & Databases — sobolev embedding theorem
9229. F9229 ML & AI — embedding dimension
9230. F9230 Curriculum-only — activation function and non-linearity
9231. F9231 ML & AI — normalization layer
9232. F9232 Data Mining & Databases — ramesh hariharan
9233. F9233 ML & AI — single-layer perceptron
9234. F9234 Curriculum-only — single-layer perceptron numerical
9235. F9235 ML & AI — vector embedding
9236. F9236 Mathematics — absorbing boundary
9237. F9237 Algorithms & Theory of CS — edge and vertex
9238. F9238 Computer Networks — weighted path
9239. F9239 Curriculum-only — orthogonal projection and the spectral theorem
9240. F9240 ML & AI — operator norm
9241. F9241 Mathematics — con dence
9242. F9242 Curriculum-only — unbiased and consistent estimator
9243. F9243 Mathematics — denoted
9244. F9244 Data Mining & Databases — laurent polynomial
9245. F9245 Mathematics — addition and multiplication
9246. F9246 Curriculum-only — small-subgroup attack
9247. F9247 Data Mining & Databases — borel subgroup
9248. F9248 Mathematics — abelian extension
9249. F9249 Algorithms & Theory of CS — polynomial freiman ruzsa
9250. F9250 Mathematics — cyclic group of order
9251. F9251 Mathematics — subgroup of order
9252. F9252 Curriculum-only — row and column reduced matrix
9253. F9253 Information Theory & Coding — single error
9254. F9254 Curriculum-only — hamming single-error correction
9255. F9255 Information Theory & Coding — rectangular code
9256. F9256 Mathematics — single error correcting code
9257. F9257 Algorithms & Theory of CS — additive combinatorics
9258. F9258 Curriculum-only — additive homomorphism of paillier
9259. F9259 Data Mining & Databases — contravariant
9260. F9260 Mathematics — b1 b2
9261. F9261 Curriculum-only — logarithm as inverse function with the base-change rule
9262. F9262 Mathematics — character group
9263. F9263 Algorithms & Theory of CS — combinatorica
9264. F9264 Computer Networks — positive linear
9265. F9265 Curriculum-only — convergence and the second eigenvalue
9266. F9266 Data Mining & Databases — enumeration of spanning tree
9267. F9267 ML & AI — generalized eigenvalue
9268. F9268 Mathematics — block form
9269. F9269 Mathematics — laplacian
9270. F9270 Algorithms & Theory of CS — matrix-tree theorem
9271. F9271 Curriculum-only — laplacian and harmonic function
9272. F9272 ML & AI — laplacian eigenmap
9273. F9273 Mathematics — continuous laplacian
9274. F9274 Algorithms & Theory of CS — proper coloring
9275. F9275 Algorithms & Theory of CS — subset of vertex
9276. F9276 Computer Networks — hub
9277. F9277 Curriculum-only — b-tree of minimum degree
9278. F9278 Data Mining & Databases — dimension reduction
9279. F9279 Information Theory & Coding — jacobson
9280. F9280 Curriculum-only — jacobson and karel
9281. F9281 ML & AI — high dimensional
9282. F9282 Mathematics — alteration
9283. F9283 Data Mining & Databases — rooted graph
9284. F9284 Algorithms & Theory of CS — random rooted graph
9285. F9285 Mathematics — det b1
9286. F9286 Distributed Systems & Cloud — pig latin
9287. F9287 Mathematics — lipschitz function
9288. F9288 Curriculum-only — newton method and its local convergence
9289. F9289 Data Mining & Databases — local convergence of graph
9290. F9290 Mathematics — matrix norm
9291. F9291 Curriculum-only — zp and its multiplicative homomorphism
9292. F9292 Mathematics — orthogonal complement
9293. F9293 Curriculum-only — orthogonal complement and orthogonal complement
9294. F9294 Mathematics — pair of distinct
9295. F9295 Mathematics — taking inverse
9296. F9296 Algorithms & Theory of CS — hausdorff distance
9297. F9297 Data Mining & Databases — hausdorff space
9298. F9298 Mathematics — hausdorff metric
9299. F9299 Distributed Systems & Cloud — transposing
9300. F9300 Mathematics — number of transposition
9301. F9301 Algorithms & Theory of CS — laplacian matrix
9302. F9302 Curriculum-only — adjacency and laplacian matrix
9303. F9303 NLP & Speech — nom
9304. F9304 Operating Systems — congestion window
9305. F9305 Other/Unknown — compact group
9306. F9306 Mathematics — locally compact group
9307. F9307 Other/Unknown — computer modelling
9308. F9308 Mathematics — double layer potential
9309. F9309 Other/Unknown — error control
9310. F9310 Curriculum-only — flow control and error control
9311. F9311 Other/Unknown — glove
9312. F9312 Mathematics — position
9313. F9313 Computer Networks — shu
9314. F9314 Curriculum-only — man-in-the-middle position
9315. F9315 Data Mining & Databases — soldier
9316. F9316 Information Theory & Coding — di er
9317. F9317 ML & AI — admissible heuristic
9318. F9318 Curriculum-only — heuristics in query optimization
9319. F9319 Data Mining & Databases — manhattan distance
9320. F9320 Algorithms & Theory of CS — manhattan distance heuristic
9321. F9321 ML & AI — isotropic position
9322. F9322 Mathematics — bonus
9323. F9323 Data Mining & Databases — optional bonus
9324. F9324 Mathematics — Position (vector)
9325. F9325 Other/Unknown — group theory
9326. F9326 Curriculum-only — mathematical modelling in biological science
9327. F9327 Other/Unknown — multiparty computation
9328. F9328 Curriculum-only — secret sharing and secure multiparty computation
9329. F9329 Other/Unknown — spectral radius
9330. F9330 ML & AI — synaptic weight
9331. F9331 Signal/Image/Audio/Video Processing — accelerating gradient descent
9332. F9332 Mathematics — haar measure
9333. F9333 Signal/Image/Audio/Video Processing — l2 regularization
9334. F9334 Curriculum-only — document processing
9335. F9335 Data Mining & Databases — face recognition
9336. F9336 Mathematics — face recognition systems
9337. F9337 Other/Unknown — computer graphics
9338. F9338 Algorithms & Theory of CS — visibility
9339. F9339 Curriculum-only — visibility by capitalisation
9340. F9340 Data Mining & Databases — visualization
9341. F9341 Curriculum-only — evaluation and visualization
9342. F9342 Data Mining & Databases — scatterplot
9343. F9343 Distributed Systems & Cloud — better visualization
9344. F9344 Curriculum-only — parallel coordinate
9345. F9345 Distributed Systems & Cloud — peter visualization series
9346. F9346 Information Theory & Coding — perception
9347. F9347 Algorithms & Theory of CS — sensory
9348. F9348 Computer Architecture — perception of sound
9349. F9349 Information Theory & Coding — speech perception
9350. F9350 ML & AI — graphics and visualization
9351. F9351 Distributed Systems & Cloud — available visualization software
9352. F9352 NLP & Speech — handbook of sensory
9353. F9353 Other/Unknown — digital image
9354. F9354 Data Mining & Databases — gray level
9355. F9355 Mathematics — wood
9356. F9356 Other/Unknown — flow visualization
9357. F9357 Distributed Systems & Cloud — data visual analytics
9358. F9358 Signal/Image/Audio/Video Processing — eigenface
9359. F9359 Curriculum-only — eigenface for facial recognition
9360. F9360 Signal/Image/Audio/Video Processing — gonzalez and wood
9361. F9361 Mathematics — time average
9362. F9362 Signal/Image/Audio/Video Processing — autocorrelation function
9363. F9363 Mathematics — crosscorrelation
9364. F9364 Algorithms & Theory of CS — rx1
9365. F9365 Mathematics — lag
9366. F9366 Computer Architecture — max lag
9367. F9367 Curriculum-only — traffic and lag
9368. F9368 Mathematics — sinusoidal input signal
9369. F9369 Signal/Image/Audio/Video Processing — autocovariance
9370. F9370 Software Engineering — anonymous
9371. F9371 Cryptography & Security — anonymity
9372. F9372 Curriculum-only — anonymity and breach
9373. F9373 Software Engineering — beta cutoff
9374. F9374 ML & AI — projected
9375. F9375 Curriculum-only — projected and reduced gradient
9376. F9376 Mathematics — proximal
9377. F9377 ML & AI — proximal policy optimization
9378. F9378 Curriculum-only — actor critic and proximal policy optimization
9379. F9379 Mathematics — meth
9380. F9380 Software Engineering — group member
9381. F9381 Mathematics — late
9382. F9382 Algorithms & Theory of CS — emergency
9383. F9383 Curriculum-only — cost of error found late
9384. F9384 Distributed Systems & Cloud — backup
9385. F9385 Curriculum-only — backup strategy
9386. F9386 Distributed Systems & Cloud — backup task
9387. F9387 Mathematics — abb
9388. F9388 Computer Networks — suggestion handed
9389. F9389 Mathematics — minute in-class
9390. F9390 Curriculum-only — frequency penalty
9391. F9391 Data Mining & Databases — penalty error
9392. F9392 Information Theory & Coding — binary code
9393. F9393 Mathematics — certainty equivalent
9394. F9394 Operating Systems — late hour
9395. F9395 Software Engineering — henzinger
9396. F9396 Curriculum-only — hyperthreading and simd
9397. F9397 Software Engineering — judgment
9398. F9398 Curriculum-only — puttaswamy judgment
9399. F9399 Software Engineering — key feature
9400. F9400 Mathematics — remaining
9401. F9401 Curriculum-only — expected number of fault remaining
9402. F9402 Software Engineering — lavender
9403. F9403 Mathematics — cutting plane
9404. F9404 Curriculum-only — dom-based
9405. F9405 Data Mining & Databases — rainbow
9406. F9406 Cryptography & Security — rainbow table
9407. F9407 Curriculum-only — rainbow and sike fell
9408. F9408 Mathematics — convex subset
9409. F9409 ML & AI — convex subset of ird
9410. F9410 Mathematics — condition hold
9411. F9411 Curriculum-only — linearization method for system of ode
9412. F9412 Mathematics — nonempty and compact
9413. F9413 Other/Unknown — feedback linearization
9414. F9414 Signal/Image/Audio/Video Processing — inverted pendulum
9415. F9415 Information Theory & Coding — rayleigh fading
9416. F9416 Mathematics — sinc
9417. F9417 Operating Systems — uptime
9418. F9418 Computer Networks — percentage of uptime
9419. F9419 Curriculum-only — uptime check
9420. F9420 Signal/Image/Audio/Video Processing — bandlimited interpolation
9421. F9421 Distributed Systems & Cloud — illusion
9422. F9422 Information Theory & Coding — noise model
9423. F9423 Mathematics — discussed
9424. F9424 Curriculum-only — geometrical significance
9425. F9425 Data Mining & Databases — level of significance
9426. F9426 Curriculum-only — practical significance against statistical significance
9427. F9427 ML & AI — bootstrapping
9428. F9428 Curriculum-only — gentry bootstrapping
9429. F9429 Mathematics — based on normal data
9430. F9430 Data Mining & Databases — studentized
9431. F9431 Mathematics — one-sample
9432. F9432 Curriculum-only — test and the one-sample
9433. F9433 Mathematics — one-sample test
9434. F9434 Curriculum-only — testing iii and debugging
9435. F9435 Mathematics — hypothesis significance testing iii
9436. F9436 Curriculum-only — large-sample test for variance and two-sample
9437. F9437 Mathematics — class19
9438. F9438 Curriculum-only — recovery time and recovery point objective
9439. F9439 Signal/Image/Audio/Video Processing — additive noise model
9440. F9440 Signal/Image/Audio/Video Processing — pendulum angle
9441. F9441 Information Theory & Coding — compander
9442. F9442 Mathematics — di erential
9443. F9443 Algorithms & Theory of CS — scalar random variable
9444. F9444 Curriculum-only — hessian of scalar
9445. F9445 Data Mining & Databases — deviation inequality
9446. F9446 Distributed Systems & Cloud — scalar operation
9447. F9447 Information Theory & Coding — di erential entropy
9448. F9448 Mathematics — lv1
9449. F9449 Curriculum-only — scalar multiplication by double-and-add
9450. F9450 Information Theory & Coding — prime field
9451. F9451 Mathematics — group operation
9452. F9452 Data Mining & Databases — baby-step giant-step
9453. F9453 Mathematics — generic algorithm
9454. F9454 Curriculum-only — pollard rho for logarithm
9455. F9455 Mathematics — residue field
9456. F9456 Data Mining & Databases — ramification
9457. F9457 Mathematics — hensel
9458. F9458 Operating Systems — scalar instruction
9459. F9459 Other/Unknown — scalar and vector
9460. F9460 Curriculum-only — vector and scalar field
9461. F9461 Other/Unknown — scalar wave
9462. F9462 Mathematics — anti-hermitian
9463. F9463 Signal/Image/Audio/Video Processing — rad
9464. F9464 Algorithms & Theory of CS — crossover
9465. F9465 Mathematics — crossover frequency
9466. F9466 Signal/Image/Audio/Video Processing — normalized frequency
9467. F9467 Curriculum-only — one-tap equalisation
9468. F9468 Information Theory & Coding — tap gain
9469. F9469 Other/Unknown — diversity
9470. F9470 Curriculum-only — fault tolerance by design diversity
9471. F9471 Data Mining & Databases — diversity-aware
9472. F9472 ML & AI — cognition
9473. F9473 Curriculum-only — human cognition of the input operator
9474. F9474 Other/Unknown — diversity reception
9475. F9475 Signal/Image/Audio/Video Processing — daubechy tap filter
9476. F9476 Mathematics — limited
9477. F9477 Curriculum-only — time-limited lock
9478. F9478 Data Mining & Databases — limited-pass algorithm
9479. F9479 Distributed Systems & Cloud — fitness
9480. F9480 ML & AI — fitness function
9481. F9481 Mathematics — limited memory
9482. F9482 Algorithms & Theory of CS — convex body
9483. F9483 Curriculum-only — translate to algebra
9484. F9484 Distributed Systems & Cloud — translate existing data-intensive algorithm
9485. F9485 Signal/Image/Audio/Video Processing — wiener
9486. F9486 Curriculum-only — wiener small-d attack
9487. F9487 Mathematics — decomposition
9488. F9488 Algorithms & Theory of CS — heavy-light decomposition
9489. F9489 Curriculum-only — decomposition and modularity
9490. F9490 Data Mining & Databases — nf decomposition
9491. F9491 Distributed Systems & Cloud — cur decomposition
9492. F9492 ML & AI — decomposition algorithm
9493. F9493 Curriculum-only — differential equation solution via eigen-decomposition
9494. F9494 ML & AI — nonnegative matrix
9495. F9495 Algorithms & Theory of CS — polynomial inequality
9496. F9496 ML & AI — system of polynomial inequality
9497. F9497 Mathematics — compute variance with decomposition
9498. F9498 Mathematics — wiener lter
9499. F9499 Other/Unknown — cholesky
9500. F9500 Mathematics — cholesky factorization
9501. F9501 Other/Unknown — cholesky decomposition
9502. F9502 Mathematics — power
9503. F9503 Algorithms & Theory of CS — computational power
9504. F9504 Computer Architecture — clock gating
9505. F9505 Computer Architecture — supply voltage
9506. F9506 Computer Networks — power grid
9507. F9507 Cryptography & Security — market power
9508. F9508 Curriculum-only — clock gating and power gating
9509. F9509 Curriculum-only — power-of-two test
9510. F9510 Data Mining & Databases — analysed
9511. F9511 Curriculum-only — analysed through inversion
9512. F9512 Data Mining & Databases — imbalance
9513. F9513 Distributed Systems & Cloud — load imbalance
9514. F9514 Information Theory & Coding — pareto distribution
9515. F9515 Mathematics — arbitrarily close
9516. F9516 Computer Networks — hard drive
9517. F9517 Curriculum-only — controller drive the observed state
9518. F9518 Mathematics — circuit board
9519. F9519 Curriculum-only — arithmetic intensity
9520. F9520 Information Theory & Coding — noise intensities
9521. F9521 Mathematics — lower power
9522. F9522 Curriculum-only — phantom read
9523. F9523 Mathematics — poisson process with intensity
9524. F9524 Curriculum-only — power allocation in multi-cell cooperative ofdm
9525. F9525 Mathematics — power iteration
9526. F9526 Algorithms & Theory of CS — working set
9527. F9527 Computer Networks — working paper
9528. F9528 Cryptography & Security — bitcoin p2p
9529. F9529 Curriculum-only — conventional single-machine tool stop working
9530. F9530 Data Mining & Databases — hands-on experience on working
9531. F9531 Distributed Systems & Cloud — algorithm working
9532. F9532 Curriculum-only — graphx api and graphx working
9533. F9533 Distributed Systems & Cloud — working in department
9534. F9534 Information Theory & Coding — recent paper
9535. F9535 Mathematics — demonstrate
9536. F9536 NLP & Speech — acoustic resistance
9537. F9537 Other/Unknown — circuit analysis
9538. F9538 Curriculum-only — concern instrument
9539. F9539 Distributed Systems & Cloud — load and store
9540. F9540 Other/Unknown — matrix analysis
9541. F9541 Algorithms & Theory of CS — steiner
9542. F9542 Curriculum-only — permanent fault from wear-out
9543. F9543 Other/Unknown — permanent magnet
9544. F9544 Curriculum-only — power and energy metrics
9545. F9545 Other/Unknown — power converter
9546. F9546 HS ComputerScience Class XI / Unit 3: Society, Law and Ethics — data protection
9547. F9547 Curriculum-only — company protection of its core asset
9548. F9548 Other/Unknown — power system protection
9549. F9549 Curriculum-only — rotator and reflector
9550. F9550 Mathematics — householder reflector
9551. F9551 Operating Systems — route reflector
9552. F9552 Other/Unknown — root finding
9553. F9553 Signal/Image/Audio/Video Processing — intensity transform
9554. F9554 Signal/Image/Audio/Video Processing — wiener filter
9555. F9555 ML & AI — fisher
9556. F9556 Computer Architecture — scott fisher
9557. F9557 Curriculum-only — fisher exact test
9558. F9558 Mathematics — causal wiener filter
9559. F9559 Curriculum-only — fisher information are named
9560. F9560 ML & AI — informative
9561. F9561 Curriculum-only — weakly informative
9562. F9562 Mathematics — fisher information matrix
9563. F9563 ML & AI — nonparametric regression
9564. F9564 Mathematics — nonparametric estimation
9565. F9565 Signal/Image/Audio/Video Processing — wiener filtering
9566. F9566 Mathematics — time wiener filtering
9567. F9567 Other/Unknown — kalman
9568. F9568 ML & AI — Kalman smoother
9569. F9569 Mathematics — kalman gain
9570. F9570 Curriculum-only — shared address space model
9571. F9571 Signal/Image/Audio/Video Processing — wiener filtering illustration
9572. F9572 Software Engineering — bundle
9573. F9573 Information Theory & Coding — exterior
9574. F9574 Curriculum-only — exterior penalty
9575. F9575 Information Theory & Coding — exterior product
9576. F9576 Signal/Image/Audio/Video Processing — orthonormal matrix
9577. F9577 Software Engineering — elt
9578. F9578 Curriculum-only — elt pattern
9579. F9579 Software Engineering — flow graph
9580. F9580 Distributed Systems & Cloud — bit-reversed
9581. F9581 ML & AI — network structure
9582. F9582 Signal/Image/Audio/Video Processing — bit-reversed order
9583. F9583 Other/Unknown — closed loop
9584. F9584 Mathematics — loop system
9585. F9585 Signal/Image/Audio/Video Processing — closed-loop system
9586. F9586 Mathematics — closed loop system stable
9587. F9587 Signal/Image/Audio/Video Processing — signal flow graph
9588. F9588 Mathematics — guide
9589. F9589 Curriculum-only — guide to the number of test
9590. F9590 Distributed Systems & Cloud — definitive guide
9591. F9591 Mathematics — cvx user guide
9592. F9592 Curriculum-only — service recommend
9593. F9593 Mathematics — recommend working
9594. F9594 Software Engineering — control-flow graph
9595. F9595 Curriculum-only — measure of functionality from the specification
9596. F9596 Software Engineering — common functionality
9597. F9597 Mathematics — hessenberg factorization
9598. F9598 Curriculum-only — quotient and chain
9599. F9599 Data Mining & Databases — quotient map
9600. F9600 Mathematics — artin map
9601. F9601 Curriculum-only — isomorphism theorem of vector space
9602. F9602 Mathematics — principal ideal
9603. F9603 Curriculum-only — fractional knapsack bound
9604. F9604 Data Mining & Databases — field norm
9605. F9605 Mathematics — fractional error
9606. F9606 Data Mining & Databases — ideal norm
9607. F9607 Mathematics — absolute norm
9608. F9608 Information Theory & Coding — signal-to-noise ratio
9609. F9609 Computer Architecture — double data rate
9610. F9610 Curriculum-only — synchronous dram and double data rate
9611. F9611 Information Theory & Coding — gaussian noise
9612. F9612 Cryptography & Security — buffer overflow
9613. F9613 Computer Networks — youn
9614. F9614 Cryptography & Security — paul youn
9615. F9615 Algorithms & Theory of CS — capability to acquire data
9616. F9616 Computer Networks — Capability Maturity Model
9617. F9617 Cryptography & Security — capability of providing
9618. F9618 Curriculum-only — access matrix with acl and capability
9619. F9619 Distributed Systems & Cloud — failure recovery
9620. F9620 Curriculum-only — failure recovery approach in distributed system
9621. F9621 Information Theory & Coding — additive white gaussian noise
9622. F9622 Algorithms & Theory of CS — union bound
9623. F9623 Curriculum-only — add the union bound
9624. F9624 Data Mining & Databases — nearest neighbor
9625. F9625 Distributed Systems & Cloud — nearest neighbor search
9626. F9626 Information Theory & Coding — balakrishnan
9627. F9627 Distributed Systems & Cloud — parallel computing
9628. F9628 Computer Networks — qos
9629. F9629 Curriculum-only — network neutrality and qos
9630. F9630 Distributed Systems & Cloud — napster
9631. F9631 Curriculum-only — parallel processing and context awareness
9632. F9632 Distributed Systems & Cloud — conference
9633. F9633 Algorithms & Theory of CS — preprint
9634. F9634 Cryptography & Security — conference on advance
9635. F9635 Curriculum-only — dartmouth conference
9636. F9636 Distributed Systems & Cloud — asplo
9637. F9637 Curriculum-only — pastry prefix routing table
9638. F9638 Distributed Systems & Cloud — pastry and bittorrent
9639. F9639 Curriculum-only — percolator and spanner
9640. F9640 Distributed Systems & Cloud — google spanner
9641. F9641 Curriculum-only — consensus in synchronous and asynchronous system
9642. F9642 Distributed Systems & Cloud — technical conferences
9643. F9643 Curriculum-only — linkedin voldemort
9644. F9644 Information Theory & Coding — content distribution
9645. F9645 Information Theory & Coding — average power
9646. F9646 Curriculum-only — lower peak-to-average power ratio
9647. F9647 Information Theory & Coding — principle of digital communication
9648. F9648 ML & AI — nearest neighbor graph
9649. F9649 Mathematics — ary
9650. F9650 Algorithms & Theory of CS — n-ary
9651. F9651 Curriculum-only — n-ary relationship
9652. F9652 Data Mining & Databases — ary recovery
9653. F9653 Curriculum-only — ary recovery algorithm
9654. F9654 Information Theory & Coding — m-ary
9655. F9655 Mathematics — bayes numerator
9656. F9656 Curriculum-only — exploit is written or adapted
9657. F9657 Distributed Systems & Cloud — spatial locality
9658. F9658 Mathematics — m-ary hypothesis testing
9659. F9659 Curriculum-only — acceptance include one real flaw you introduce on purpose
9660. F9660 Distributed Systems & Cloud — disclaimer
9661. F9661 Mathematics — control purpose
9662. F9662 Curriculum-only — quantize and serve
9663. F9663 Mathematics — set of sample
9664. F9664 Information Theory & Coding — probability of error
9665. F9665 Mathematics — probability of error decision
9666. F9666 Cryptography & Security — trustless setup
9667. F9667 Curriculum-only — asynchronous setup
9668. F9668 ML & AI — limited feedback
9669. F9669 Curriculum-only — limited-feedback and fading-capacity case are named
9670. F9670 Mathematics — sinh
9671. F9671 Curriculum-only — hyperbolic function cosh and sinh
9672. F9672 Mathematics — likewise
9673. F9673 ML & AI — resample
9674. F9674 Mathematics — stabilise
9675. F9675 NLP & Speech — low signal-to-noise ratio
9676. F9676 Operating Systems — purpose register
9677. F9677 Curriculum-only — master serve read
9678. F9678 Other/Unknown — article and conference
9679. F9679 ML & AI — mission
9680. F9680 Algorithms & Theory of CS — assurance
9681. F9681 Computer Networks — soho
9682. F9682 Distributed Systems & Cloud — safety
9683. F9683 Cryptography & Security — enforcement
9684. F9684 Curriculum-only — memory-safety bug
9685. F9685 Distributed Systems & Cloud — dependency
9686. F9686 Algorithms & Theory of CS — dependency graph
9687. F9687 Computer Architecture — mtx
9688. F9688 Curriculum-only — channel dependency graph
9689. F9689 Curriculum-only — inclusion dependency
9690. F9690 Curriculum-only — normalisation helper read functional dependency
9691. F9691 Distributed Systems & Cloud — wide dependency
9692. F9692 ML & AI — ai safety
9693. F9693 Curriculum-only — ai safety foundation
9694. F9694 Mathematics — canonical
9695. F9695 Algorithms & Theory of CS — canonical negative dependency graph
9696. F9696 Curriculum-only — canonical np-complete
9697. F9697 Mathematics — canonical form
9698. F9698 Distributed Systems & Cloud — mar polar lander
9699. F9699 Mathematics — m1 and m2
9700. F9700 Information Theory & Coding — concatenation
9701. F9701 Mathematics — rev
9702. F9702 Curriculum-only — bayesian modeling with stan
9703. F9703 Mathematics — uniquely determine
9704. F9704 Other/Unknown — canonical correlation
9705. F9705 Data Mining & Databases — climate data
9706. F9706 Other/Unknown — budget
9707. F9707 Curriculum-only — budget and unreliable
9708. F9708 Curriculum-only — slo and error-budget vocabulary
9709. F9709 Other/Unknown — climate change
9710. F9710 ML & AI — adaptation
9711. F9711 Mathematics — carbon
9712. F9712 ML & AI — Carbon footprint, hardware electronic waste
9713. F9713 Curriculum-only — carbon footprint of training
9714. F9714 Mathematics — implication
9715. F9715 Curriculum-only — strong convexity and its implication
9716. F9716 Mathematics — converse implication
9717. F9717 Operating Systems — Social implications (e.g., political and cultural ideologies) in a hyper-networked world where the capabilities and impact of social media, artificial intelligence, and computing in general are rapidly evolving
9718. F9718 Other/Unknown — Carbon sequestration
9719. F9719 Mathematics — gas law
9720. F9720 Other/Unknown — chemical reaction
9721. F9721 Mathematics — calculation
9722. F9722 Curriculum-only — calculation of centre of gravity
9723. F9723 Information Theory & Coding — back-of-the-envelope calculation
9724. F9724 Mathematics — calculation for power
9725. F9725 Other/Unknown — cryogenic
9726. F9726 Mathematics — model of heat flow
9727. F9727 Other/Unknown — information assurance
9728. F9728 Computer Networks — jordan form
9729. F9729 Curriculum-only — canonical form and jordan form
9730. F9730 Mathematics — jordan block
9731. F9731 Other/Unknown — jordan canonical form
9732. F9732 Curriculum-only — jordan form and jordan canonical form
9733. F9733 Other/Unknown — non-gaussian noise
9734. F9734 Curriculum-only — sampling and sampling distribution
9735. F9735 Other/Unknown — special emphasis
9736. F9736 Signal/Image/Audio/Video Processing — Carbon dioxide
9737. F9737 Other/Unknown — emission
9738. F9738 Signal/Image/Audio/Video Processing — colored noise
9739. F9739 Mathematics — estimation in colored noise
9740. F9740 Signal/Image/Audio/Video Processing — fractional delay
9741. F9741 Computer Architecture — chirp
9742. F9742 Signal/Image/Audio/Video Processing — chirp signals
9743. F9743 Curriculum-only — duality and quotient space
9744. F9744 Signal/Image/Audio/Video Processing — sampling rate conversion
9745. F9745 Software Engineering — dependency rest
9746. F9746 Curriculum-only — evaluation of deployed system
9747. F9747 Distributed Systems & Cloud — routing
9748. F9748 Computer Architecture — Wire routing
9749. F9749 Computer Networks — failover
9750. F9750 Curriculum-only — bufferless routing
9751. F9751 Curriculum-only — routing and caching
9752. F9752 Distributed Systems & Cloud — butterfly network
9753. F9753 Information Theory & Coding — cidr
9754. F9754 Curriculum-only — ripe or cidr report
9755. F9755 Information Theory & Coding — distance-vector protocol
9756. F9756 Curriculum-only — deterministic rounding
9757. F9757 Information Theory & Coding — network topology
9758. F9758 Curriculum-only — query routing strategy
9759. F9759 ML & AI — adaptive routing
9760. F9760 Curriculum-only — oblivious and adaptive routing
9761. F9761 Mathematics — network and routing
9762. F9762 Algorithms & Theory of CS — time algorithm
9763. F9763 Curriculum-only — clever linear-time algorithm
9764. F9764 ML & AI — time algorithm to learn
9765. F9765 Operating Systems — bgp routing
9766. F9766 Other/Unknown — path algorithm
9767. F9767 Algorithms & Theory of CS — directed cycle
9768. F9768 Curriculum-only — bellman ford and negative cycle
9769. F9769 Distributed Systems & Cloud — relaxed consistency model
9770. F9770 Curriculum-only — iit madras
9771. F9771 Distributed Systems & Cloud — iit delhi
9772. F9772 Curriculum-only — iit delhi analysis of its privacy
9773. F9773 Distributed Systems & Cloud — iit kanpur
9774. F9774 Operating Systems — thread block
9775. F9775 Distributed Systems & Cloud — process-to-processor mapping
9776. F9776 Computer Architecture — programming multiprocessor
9777. F9777 Data Mining & Databases — parallel structure
9778. F9778 Distributed Systems & Cloud — message passing interface
9779. F9779 Algorithms & Theory of CS — q-learning
9780. F9780 Computer Architecture — design architecture
9781. F9781 Cryptography & Security — Distributed architectures
9782. F9782 Curriculum-only — architecture and component
9783. F9783 Curriculum-only — llm architecture and long context
9784. F9784 Curriculum-only — spectrum of citation architecture
9785. F9785 Data Mining & Databases — Database architecture, data independence, and data abstraction
9786. F9786 Distributed Systems & Cloud — algorithm and architecture
9787. F9787 Curriculum-only — computer architecture for virtualization
9788. F9788 Distributed Systems & Cloud — computing architecture
9789. F9789 Curriculum-only — pig as higher-level language
9790. F9790 Distributed Systems & Cloud — ierror
9791. F9791 Computer Networks — missing manual
9792. F9792 Curriculum-only — manual feature
9793. F9793 Distributed Systems & Cloud — cilk manual
9794. F9794 Curriculum-only — training an mlp
9795. F9795 Distributed Systems & Cloud — model and architecture
9796. F9796 Curriculum-only — parallel programming model and architecture
9797. F9797 Distributed Systems & Cloud — mpi bsend
9798. F9798 Distributed Systems & Cloud — massively parallel processor
9799. F9799 Computer Architecture — music performance
9800. F9800 Computer Networks — database server
9801. F9801 Curriculum-only — better write performance
9802. F9802 Data Mining & Databases — actual performance
9803. F9803 Curriculum-only — legality and rule of engagement
9804. F9804 Data Mining & Databases — tablet server
9805. F9805 Distributed Systems & Cloud — access pattern
9806. F9806 Curriculum-only — store by access pattern
9807. F9807 Distributed Systems & Cloud — amdahl
9808. F9808 Computer Networks — bottleneck ratio
9809. F9809 Distributed Systems & Cloud — execution time
9810. F9810 Computer Architecture — storage overhead
9811. F9811 Distributed Systems & Cloud — performance algorithm for visualization
9812. F9812 Algorithms & Theory of CS — md1
9813. F9813 Computer Architecture — complex pipeline
9814. F9814 Cryptography & Security — md2
9815. F9815 Curriculum-only — classical nlp pipeline
9816. F9816 Curriculum-only — optimal pipeline depth
9817. F9817 Distributed Systems & Cloud — cycle per instruction
9818. F9818 Curriculum-only — instruction count and cycle per instruction
9819. F9819 Distributed Systems & Cloud — graphics hardware
9820. F9820 Curriculum-only — instruction pipeline and performance
9821. F9821 Distributed Systems & Cloud — joiner
9822. F9822 Data Mining & Databases — sparse linear system
9823. F9823 Distributed Systems & Cloud — sparse linear algebra
9824. F9824 Curriculum-only — append-heavy workload
9825. F9825 Distributed Systems & Cloud — workload manager
9826. F9826 Information Theory & Coding — decoding performance
9827. F9827 Curriculum-only — impact on network architecture
9828. F9828 Information Theory & Coding — spatial multiplexing
9829. F9829 Curriculum-only — protocol-independent switch architecture
9830. F9830 Information Theory & Coding — tradeoff
9831. F9831 Computer Networks — design tradeoff
9832. F9832 Curriculum-only — diversity tradeoff
9833. F9833 ML & AI — bias variance
9834. F9834 Curriculum-only — subsumption relation
9835. F9835 ML & AI — tabular data
9836. F9836 Mathematics — equivalent form
9837. F9837 Curriculum-only — equivalent form of regularization
9838. F9838 Information Theory & Coding — equivalent form of theorem
9839. F9839 Mathematics — if1
9840. F9840 Curriculum-only — updated by ttl
9841. F9841 Data Mining & Databases — refresh
9842. F9842 Curriculum-only — default one-week refresh
9843. F9843 Data Mining & Databases — updated software version
9844. F9844 NLP & Speech — model size
9845. F9845 Operating Systems — architecture memory
9846. F9846 Curriculum-only — wider in-order pipeline
9847. F9847 Operating Systems — instruction fetch
9848. F9848 Curriculum-only — specifically focus on out-of-order pipeline
9849. F9849 Operating Systems — performance of firefly rpc
9850. F9850 Mathematics — ghz powerpc g5
9851. F9851 Operating Systems — proposed architectures
9852. F9852 Curriculum-only — raid as the other organisation
9853. F9853 Operating Systems — reliable architecture
9854. F9854 Other/Unknown — architecture and organization
9855. F9855 Curriculum-only — computer architecture and organization
9856. F9856 Other/Unknown — architecture description
9857. F9857 Computer Architecture — risc
9858. F9858 Curriculum-only — load-store risc like the mip
9859. F9859 Operating Systems — cisc isa
9860. F9860 Other/Unknown — computer aided design
9861. F9861 Information Theory & Coding — shift register
9862. F9862 Computer Architecture — linear feedback shift register
9863. F9863 Other/Unknown — computer aided
9864. F9864 Computer Architecture — data hazard
9865. F9865 Curriculum-only — cause hazard in an in-order pipeline
9866. F9866 Operating Systems — pipelining and hazard
9867. F9867 Curriculum-only — waw hazard and out-of-order completion
9868. F9868 Other/Unknown — learning rule
9869. F9869 Computer Architecture — nand
9870. F9870 Curriculum-only — nand and nor as universal gate
9871. F9871 Information Theory & Coding — input state
9872. F9872 Other/Unknown — asynchronous circuit
9873. F9873 Curriculum-only — handler and middleware
9874. F9874 Other/Unknown — Network performance modeling
9875. F9875 Curriculum-only — quantitative assessment
9876. F9876 Other/Unknown — quantitative analysis
9877. F9877 Computer Architecture — bipolar junction transistor
9878. F9878 Curriculum-only — layer from transistor
9879. F9879 Distributed Systems & Cloud — vlsi
9880. F9880 Computer Architecture — leakage
9881. F9881 Curriculum-only — indirect injection and leakage
9882. F9882 Other/Unknown — field effect transistors
9883. F9883 Computer Architecture — hot spot
9884. F9884 Curriculum-only — downtime set by hot standby
9885. F9885 Other/Unknown — compaction
9886. F9886 Curriculum-only — log compaction
9887. F9887 Other/Unknown — low power
9888. F9888 Computer Architecture — clock distribution
9889. F9889 Distributed Systems & Cloud — deal with clock-skew
9890. F9890 Other/Unknown — clock period
9891. F9891 Distributed Systems & Cloud — propagate
9892. F9892 Cryptography & Security — taint
9893. F9893 Curriculum-only — propagate pi
9894. F9894 Other/Unknown — semiconductor
9895. F9895 Signal/Image/Audio/Video Processing — band
9896. F9896 Computer Architecture — red band
9897. F9897 Curriculum-only — credible band for the regression line
9898. F9898 Information Theory & Coding — critical band
9899. F9899 Mathematics — rubber band
9900. F9900 Information Theory & Coding — epoch
9901. F9901 Curriculum-only — store compare epoch
9902. F9902 Other/Unknown — band structure
9903. F9903 Signal/Image/Audio/Video Processing — cnn architecture
9904. F9904 Curriculum-only — cnn operation and cnn architecture
9905. F9905 Signal/Image/Audio/Video Processing — detection performance
9906. F9906 Curriculum-only — in-band network telemetry
9907. F9907 Information Theory & Coding — jointly gaussian
9908. F9908 Signal/Image/Audio/Video Processing — organ transport system
9909. F9909 ML & AI — Spline models
9910. F9910 Mathematics — spline interpolation
9911. F9911 Signal/Image/Audio/Video Processing — cubic spline
9912. F9912 Data Mining & Databases — title
9913. F9913 Computer Architecture — song title
9914. F9914 Curriculum-only — byte title
9915. F9915 Distributed Systems & Cloud — broad title
9916. F9916 Signal/Image/Audio/Video Processing — bookmark
9917. F9917 Curriculum-only — outer-join null padding is defined
9918. F9918 Data Mining & Databases — border
9919. F9919 Cryptography & Security — cross border payment
9920. F9920 Curriculum-only — border and noise
9921. F9921 Signal/Image/Audio/Video Processing — saved bookmark
9922. F9922 Software Engineering — architecture guide
9923. F9923 Mathematics — identify
9924. F9924 Computer Architecture — identify flaw
9925. F9925 Curriculum-only — curriculum could identify
9926. F9926 Mathematics — identifying
9927. F9927 Curriculum-only — identifying relationship
9928. F9928 Distributed Systems & Cloud — intent
9929. F9929 Other/Unknown — design intent
9930. F9930 Signal/Image/Audio/Video Processing — ecg
9931. F9931 Software Engineering — caching and cachegrind
9932. F9932 Curriculum-only — memory access coalescing
9933. F9933 Software Engineering — conditional branch
9934. F9934 Curriculum-only — compare and conditional branch
9935. F9935 Software Engineering — control hazard
9936. F9936 Curriculum-only — data and control hazard
9937. F9937 Software Engineering — cost model
9938. F9938 Curriculum-only — constructive cost model
9939. F9939 Software Engineering — datatype
9940. F9940 Distributed Systems & Cloud — derived datatype
9941. F9941 Curriculum-only — grid-stride loop
9942. F9942 Distributed Systems & Cloud — unit-stride
9943. F9943 Mathematics — displacement
9944. F9944 Curriculum-only — base plus displacement
9945. F9945 Mathematics — acceleration
9946. F9946 Distributed Systems & Cloud — velocity and acceleration
9947. F9947 Mathematics — Displacement (vector)
9948. F9948 Signal/Image/Audio/Video Processing — angular displacement
9949. F9949 Software Engineering — bitfield
9950. F9950 Curriculum-only — design choice with the alternative rejected
9951. F9951 Software Engineering — device architectures
9952. F9952 Computer Architecture — domain specific accelerator
9953. F9953 Software Engineering — enforcement mechanism
9954. F9954 Cryptography & Security — contract enforcement mechanism
9955. F9955 Software Engineering — engine
9956. F9956 Algorithms & Theory of CS — mover
9957. F9957 Computer Architecture — difference engine
9958. F9958 Curriculum-only — bigtable engine
9959. F9959 Distributed Systems & Cloud — app engine
9960. F9960 Information Theory & Coding — propulsion
9961. F9961 Mathematics — s2 s1
9962. F9962 Other/Unknown — aircraft engines
9963. F9963 Software Engineering — facilitate
9964. F9964 Curriculum-only — data fragmentation
9965. F9965 Software Engineering — game engine
9966. F9966 Curriculum-only — gpr in python
9967. F9967 Software Engineering — inference engines
9968. F9968 Operating Systems — interlock to resolve data
9969. F9969 Software Engineering — jet propulsion laboratory
9970. F9970 Curriculum-only — language feature related
9971. F9971 Software Engineering — larger block
9972. F9972 Curriculum-only — goroutine leak
9973. F9973 Software Engineering — low intensity
9974. F9974 Cryptography & Security — sandboxing native code
9975. F9975 Distributed Systems & Cloud — security model
9976. F9976 Software Engineering — nonempty closed convex cone
9977. F9977 ML & AI — nonempty convex subset
9978. F9978 Mathematics — c1 and c2
9979. F9979 Algorithms & Theory of CS — auxiliary tree
9980. F9980 Computer Architecture — remember to solve
9981. F9981 Computer Networks — compartment
9982. F9982 Cryptography & Security — separate machine
9983. F9983 Curriculum-only — separate box
9984. F9984 Information Theory & Coding — separate control
9985. F9985 Curriculum-only — separate control and data connection
9986. F9986 Mathematics — cnx
9987. F9987 Operating Systems — preferred path
9988. F9988 Algorithms & Theory of CS — path-parent
9989. F9989 Software Engineering — closed halfspace
9990. F9990 Mathematics — nonvertical hyperplane
9991. F9991 Software Engineering — nonempty convex set
9992. F9992 Curriculum-only — sequent numa
9993. F9993 Distributed Systems & Cloud — numa-q
9994. F9994 Curriculum-only — origin and numa-q
9995. F9995 Software Engineering — payload
9996. F9996 Curriculum-only — payload bloat as field grow
9997. F9997 Software Engineering — performance consideration
9998. F9998 Distributed Systems & Cloud — Using virtualization and isolation to achieve protection and predictable performance
9999. F9999 Software Engineering — promise
10000. F10000 Curriculum-only — distributed-system concept work inside cloud that the course promise
10001. F10001 Data Mining & Databases — thunk
10002. F10002 Software Engineering — pubkey hash
10003. F10003 Distributed Systems & Cloud — multithreaded
10004. F10004 Curriculum-only — multithreaded core
10005. F10005 Distributed Systems & Cloud — executing multithreaded program efficiently
10006. F10006 Operating Systems — multithreaded architecture
10007. F10007 Software Engineering — analysis of multithreaded algorithm
10008. F10008 Curriculum-only — reply forwarding
10009. F10009 Data Mining & Databases — mount
10010. F10010 Software Engineering — reuse
10011. F10011 Algorithms & Theory of CS — common substring
10012. F10012 Computer Networks — frequency re-use
10013. F10013 Cryptography & Security — pad reuse
10014. F10014 Curriculum-only — append reuse the array while capacity
10015. F10015 Other/Unknown — recycling
10016. F10016 Curriculum-only — differ from the silent recycling
10017. F10017 Software Engineering — reusable
10018. F10018 Curriculum-only — reuse distance and stack algorithm
10019. F10019 Software Engineering — routing model-view-controller design
10020. F10020 Curriculum-only — semantic caching
10021. F10021 Data Mining & Databases — semantic optimisation
10022. F10022 Mathematics — mother
10023. F10023 Curriculum-only — f-score with stem and synonym
10024. F10024 NLP & Speech — coreference resolution
10025. F10025 Distributed Systems & Cloud — linguistic support for robust
10026. F10026 NLP & Speech — linguistic complexity
10027. F10027 Algorithms & Theory of CS — ancestor
10028. F10028 Cryptography & Security — external node
10029. F10029 Curriculum-only — common ancestor with its conflict rule
10030. F10030 Distributed Systems & Cloud — canonical parse tree
10031. F10031 Mathematics — sided
10032. F10032 ML & AI — bayesian network
10033. F10033 Algorithms & Theory of CS — observable variable
10034. F10034 ML & AI — d-separation
10035. F10035 Mathematics — sided test
10036. F10036 Data Mining & Databases — two-sided test
10037. F10037 Curriculum-only — one-sided and two-sided test
10038. F10038 Mathematics — one-sided test
10039. F10039 NLP & Speech — bayes ball
10040. F10040 Curriculum-only — episodic and semantic memory
10041. F10041 NLP & Speech — Semantic networks
10042. F10042 Operating Systems — semantic file system
10043. F10043 Other/Unknown — bayesian estimation
10044. F10044 Curriculum-only — bayesian estimation of an event frequency
10045. F10045 Other/Unknown — distribution network
10046. F10046 Software Engineering — semantic checker
10047. F10047 Curriculum-only — packet sniffing using wireshark
10048. F10048 Software Engineering — Social Context
10049. F10049 CS2023 gap-fill — Accessibility issues, including legal requirements such as Web Content Accessibility Guidelines (www.w3.org/TR/WCAG21)
10050. F10050 Software Engineering — Software performance
10051. F10051 Information Theory & Coding — efficient source code
10052. F10052 Software Engineering — special value
10053. F10053 Mathematics — activity
10054. F10054 Algorithms & Theory of CS — brain activity
10055. F10055 Computer Architecture — activity factor
10056. F10056 Computer Networks — activity diagram
10057. F10057 Cryptography & Security — illicit activity
10058. F10058 Curriculum-only — activity stream
10059. F10059 Distributed Systems & Cloud — malicious activities
10060. F10060 Mathematics — participation
10061. F10061 Curriculum-only — partial participation
10062. F10062 Other/Unknown — activity recognition
10063. F10063 Signal/Image/Audio/Video Processing — activity interpretation
10064. F10064 Software Engineering — design activity
10065. F10065 Curriculum-only — speculative execution of straggler
10066. F10066 Operating Systems — virtual memory
10067. F10067 Curriculum-only — cache and virtual memory
10068. F10068 Distributed Systems & Cloud — memory system
10069. F10069 Computer Architecture — timing constraint
10070. F10070 Curriculum-only — design of cache memory system
10071. F10071 Distributed Systems & Cloud — distributed shared
10072. F10072 Operating Systems — include virtual memory
10073. F10073 Software Engineering — sql query
10074. F10074 Distributed Systems & Cloud — storage virtualisation
10075. F10075 Software Engineering — storage allocation assigned
10076. F10076 Curriculum-only — visual table of content of the system
10077. F10077 Mathematics — conclusion
10078. F10078 Curriculum-only — distributed clustering and conclusion
10079. F10079 Data Mining & Databases — resolution rule
10080. F10080 Distributed Systems & Cloud — interior point method
10081. F10081 Mathematics — common factor
10082. F10082 Algorithms & Theory of CS — retroactivity
10083. F10083 Curriculum-only — consul as present-day equivalent
10084. F10084 Distributed Systems & Cloud — monograph present
10085. F10085 Mathematics — co present
10086. F10086 Other/Unknown — merton
10087. F10087 Software Engineering — tale
10088. F10088 Curriculum-only — reviewer can rerun the differential tester
10089. F10089 Software Engineering — line of code
10090. F10090 Algorithms & Theory of CS — binary trie
10091. F10091 Curriculum-only — compressed or radix trie named
10092. F10092 Mathematics — ordered tree
10093. F10093 Algorithms & Theory of CS — rooted ordered tree
10094. F10094 Software Engineering — txt
10095. F10095 Data Mining & Databases — txt file
10096. F10096 Mathematics — reproduce
10097. F10097 Curriculum-only — single command reproduce the run
10098. F10098 Software Engineering — Type safety and errors caused by using values inconsistently given their intended types
10099. F10099 Curriculum-only — upload content when it change
10100. F10100 Software Engineering — submission
10101. F10101 Computer Networks — submission deadline
10102. F10102 ML & AI — penalized
10103. F10103 Mathematics — bayesian information criterion
10104. F10104 Curriculum-only — akaike and bayesian information criterion
10105. F10105 Data Mining & Databases — provide necessary prerequisite
10106. F10106 ML & AI — propensity score
10107. F10107 Mathematics — excel submission
10108. F10108 Other/Unknown — fold
10109. F10109 Curriculum-only — fold or merge
10110. F10110 Other/Unknown — statistical inference
10111. F10111 Algorithms & Theory of CS — classical statistical
10112. F10112 Curriculum-only — classical statistical and data-mining model
10113. F10113 Data Mining & Databases — apply suitable statistical inference
10114. F10114 Information Theory & Coding — sufficient statistic
10115. F10115 ML & AI — machine learning
10116. F10116 Algorithms & Theory of CS — algorithmic
10117. F10117 Cryptography & Security — algorithmic implementation
10118. F10118 Curriculum-only — adaptive control and machine learning
10119. F10119 Curriculum-only — machine learning and algorithm
10120. F10120 Data Mining & Databases — algorithmic language
10121. F10121 Cryptography & Security — data security
10122. F10122 HS ComputerScience Class XI / Unit 3: Society, Law and Ethics — malware
10123. F10123 Computer Networks — botnet
10124. F10124 Cryptography & Security — honeypot
10125. F10125 Curriculum-only — algebraic attack
10126. F10126 Curriculum-only — malware taxonomy and analysis
10127. F10127 Data Mining & Databases — cs data analytics
10128. F10128 Distributed Systems & Cloud — algorithmic model
10129. F10129 Curriculum-only — distributed machine learning and optimisation
10130. F10130 Distributed Systems & Cloud — distributed optimization
10131. F10131 Curriculum-only — distributed optimisation behind the trainer
10132. F10132 Distributed Systems & Cloud — consensus based distributed optimization
10133. F10133 Information Theory & Coding — discrete cosine transformation
10134. F10134 ML & AI — adaboost
10135. F10135 Curriculum-only — adaboost and gradient boosting
10136. F10136 ML & AI — adaboost algorithm
10137. F10137 Curriculum-only — explainability by feature attribution
10138. F10138 ML & AI — freund
10139. F10139 Algorithms & Theory of CS — temporal-difference learning
10140. F10140 Curriculum-only — inductive logic programming
10141. F10141 Data Mining & Databases — apriori algorithm
10142. F10142 Curriculum-only — apriori algorithm and the downward-closure
10143. F10143 Distributed Systems & Cloud — federated learning
10144. F10144 Curriculum-only — computational heterogeneity in federated learning
10145. F10145 Distributed Systems & Cloud — test-and-test-and-set
10146. F10146 ML & AI — feature learning
10147. F10147 Curriculum-only — dimensionality reduction and feature learning
10148. F10148 Data Mining & Databases — manifold learning
10149. F10149 Distributed Systems & Cloud — linear dimensionality reduction
10150. F10150 ML & AI — low-rank adaptation
10151. F10151 Curriculum-only — decision tree with pruning
10152. F10152 ML & AI — cost-complexity pruning
10153. F10153 Curriculum-only — information-theoretic security of steganography
10154. F10154 ML & AI — svm model
10155. F10155 Curriculum-only — synthetic data generator you write yourself
10156. F10156 ML & AI — waypoint
10157. F10157 Mathematics — admm
10158. F10158 Curriculum-only — admm and dual decomposition
10159. F10159 Distributed Systems & Cloud — admm and decomposition
10160. F10160 Mathematics — classical statistical inference
10161. F10161 Algorithms & Theory of CS — active-set
10162. F10162 Computer Architecture — active region
10163. F10163 Cryptography & Security — active adversary
10164. F10164 Curriculum-only — active defence
10165. F10165 Curriculum-only — potential data loss if the active fail before replication
10166. F10166 Data Mining & Databases — active database
10167. F10167 Distributed Systems & Cloud — active round
10168. F10168 Information Theory & Coding — active network
10169. F10169 ML & AI — active learning
10170. F10170 Curriculum-only — cost of deep pipeline
10171. F10171 Data Mining & Databases — left-deep
10172. F10172 Curriculum-only — left-deep and bushy tree
10173. F10173 Data Mining & Databases — list of element
10174. F10174 Distributed Systems & Cloud — deep dive
10175. F10175 ML & AI — Deep belief networks
10176. F10176 Curriculum-only — classical nlp deep learning
10177. F10177 Information Theory & Coding — decoder
10178. F10178 Computer Architecture — suboptimal decoder
10179. F10179 Curriculum-only — complete decoder
10180. F10180 Distributed Systems & Cloud — macroblock
10181. F10181 Information Theory & Coding — compressor
10182. F10182 Curriculum-only — boundary burst
10183. F10183 Information Theory & Coding — encoding scheme
10184. F10184 ML & AI — alexander
10185. F10185 Curriculum-only — explainable ai for deep model
10186. F10186 ML & AI — deep network
10187. F10187 Curriculum-only — generalization in deep network
10188. F10188 Information Theory & Coding — convolutional
10189. F10189 ML & AI — convolutional filter
10190. F10190 Curriculum-only — probabilistic model for supervised learning
10191. F10191 Data Mining & Databases — learning to rank
10192. F10192 Distributed Systems & Cloud — distributed supervised learning
10193. F10193 ML & AI — transfer learning
10194. F10194 Curriculum-only — hands-on transfer learning
10195. F10195 ML & AI — one-shot learning
10196. F10196 Mathematics — absorb
10197. F10197 Data Mining & Databases — john elder iv
10198. F10198 Distributed Systems & Cloud — john ebenezer augustine
10199. F10199 Mathematics — bought
10200. F10200 ML & AI — approachability
10201. F10201 Mathematics — reporter
10202. F10202 Algorithms & Theory of CS — conic programming ii
10203. F10203 Mathematics — lp relaxation
10204. F10204 Data Mining & Databases — kadison-singer
10205. F10205 Mathematics — stochastic optimization
10206. F10206 NLP & Speech — language processing
10207. F10207 Mathematics — wed
10208. F10208 NLP & Speech — computational linguistics
10209. F10209 Data Mining & Databases — association
10210. F10210 Curriculum-only — association with multiplicity
10211. F10211 Data Mining & Databases — association list
10212. F10212 Distributed Systems & Cloud — type of data
10213. F10213 NLP & Speech — access control list
10214. F10214 Algorithms & Theory of CS — protein parsing
10215. F10215 Data Mining & Databases — chart
10216. F10216 Computer Networks — flow chart
10217. F10217 Curriculum-only — burn-down chart
10218. F10218 Data Mining & Databases — bar chart
10219. F10219 Curriculum-only — lift chart and cost-sensitive evaluation
10220. F10220 Data Mining & Databases — pie chart
10221. F10221 Information Theory & Coding — state set
10222. F10222 NLP & Speech — Earley Parsing
10223. F10223 Mathematics — bootstrap
10224. F10224 Curriculum-only — confidence interval and the bootstrap
10225. F10225 Data Mining & Databases — sample data
10226. F10226 Curriculum-only — sample data well-suited for nosql
10227. F10227 ML & AI — sample complexity
10228. F10228 Mathematics — bootstrap confidence interval
10229. F10229 NLP & Speech — speech tagging
10230. F10230 Operating Systems — active learning work
10231. F10231 Other/Unknown — active control
10232. F10232 Curriculum-only — multi-layer perceptron and back-propagation
10233. F10233 Other/Unknown — cognitive
10234. F10234 Computer Architecture — emotional
10235. F10235 NLP & Speech — language and cognitive
10236. F10236 Other/Unknown — Cognitive architectures (e.g., ACT-R, SOAR, ICARUS, FORR)
10237. F10237 Curriculum-only — cognitive model of categorical data
10238. F10238 Other/Unknown — cognitive radio
10239. F10239 Curriculum-only — cognitive radio system
10240. F10240 Other/Unknown — computational model
10241. F10241 Curriculum-only — statistical decision theory for regression
10242. F10242 Mathematics — preference
10243. F10243 Curriculum-only — aligning model with human preference
10244. F10244 Data Mining & Databases — ranking
10245. F10245 Curriculum-only — google page ranking algorithm
10246. F10246 Data Mining & Databases — county health ranking
10247. F10247 Distributed Systems & Cloud — list ranking
10248. F10248 Mathematics — integra
10249. F10249 Curriculum-only — med and nexthop
10250. F10250 Mathematics — preference list
10251. F10251 NLP & Speech — attachment preference
10252. F10252 Curriculum-only — bayes decision theory for binary feature
10253. F10253 NLP & Speech — recency
10254. F10254 Computer Networks — referential integrity
10255. F10255 Curriculum-only — entity integrity and referential integrity
10256. F10256 Other/Unknown — allocation preference
10257. F10257 Curriculum-only — gan as deep generative model
10258. F10258 Other/Unknown — deep Q-network
10259. F10259 Curriculum-only — descriptive statistics and visualisation
10260. F10260 Other/Unknown — design of experiment
10261. F10261 Curriculum-only — first-order fritz john
10262. F10262 Other/Unknown — genetic algorithm
10263. F10263 Data Mining & Databases — interpretability
10264. F10264 Curriculum-only — sparsity and interpretability
10265. F10265 Other/Unknown — gpus
10266. F10266 Curriculum-only — kernel source for cpus and gpus
10267. F10267 ML & AI — gpus and tpus
10268. F10268 Other/Unknown — graph convolutional networks
10269. F10269 Algorithms & Theory of CS — private-key encryption
10270. F10270 Computer Networks — symmetric-key encryption
10271. F10271 Curriculum-only — private-key encryption and public-key encryption introduced
10272. F10272 Other/Unknown — latch
10273. F10273 Computer Architecture — hold time
10274. F10274 Curriculum-only — setup and hold time
10275. F10275 Distributed Systems & Cloud — master-slave
10276. F10276 Curriculum-only — sql write master-slave
10277. F10277 Other/Unknown — mathematical foundation
10278. F10278 Curriculum-only — architecture of ae with mathematical foundation
10279. F10279 ML & AI — mathematical foundation of learning
10280. F10280 Other/Unknown — measure of association
10281. F10281 Curriculum-only — descriptive statistics and measure of association
10282. F10282 Other/Unknown — mining streaming data
10283. F10283 Cryptography & Security — user profile
10284. F10284 Other/Unknown — reduced k-map
10285. F10285 Curriculum-only — dsa algorithm
10286. F10286 Other/Unknown — steganalysis
10287. F10287 Signal/Image/Audio/Video Processing — active appearance model
10288. F10288 Other/Unknown — flexible
10289. F10289 Curriculum-only — dynamic or flexible schema
10290. F10290 Information Theory & Coding — flexible computation
10291. F10291 Signal/Image/Audio/Video Processing — data association
10292. F10292 Information Theory & Coding — jpeg image
10293. F10293 Mathematics — discrete cosines
10294. F10294 Curriculum-only — photo upload
10295. F10295 ML & AI — text encoder
10296. F10296 Mathematics — college
10297. F10297 Data Mining & Databases — encouraged to attend
10298. F10298 Mathematics — dome
10299. F10299 NLP & Speech — photo removed for copyright
10300. F10300 Operating Systems — attend whichever
10301. F10301 Other/Unknown — image compression
10302. F10302 Curriculum-only — image compression and sparse signal
10303. F10303 Other/Unknown — evolution
10304. F10304 Curriculum-only — end-to-end evolution
10305. F10305 Data Mining & Databases — substitution model
10306. F10306 Distributed Systems & Cloud — evolution of sdn
10307. F10307 Information Theory & Coding — Conceptual models (e.g., entity-relationship, UML diagrams)
10308. F10308 Other/Unknown — Molecular evolution
10309. F10309 Signal/Image/Audio/Video Processing — curve evolution
10310. F10310 Data Mining & Databases — add subplot
10311. F10311 Software Engineering — alert
10312. F10312 Curriculum-only — alert not acted
10313. F10313 NLP & Speech — advisory
10314. F10314 Software Engineering — cartesian space
10315. F10315 Curriculum-only — shallow and deep copy
10316. F10316 Software Engineering — eval
10317. F10317 Data Mining & Databases — eval and apply
10318. F10318 Software Engineering — expected to regularly attend
10319. F10319 Algorithms & Theory of CS — neighboring domain
10320. F10320 Curriculum-only — inconsistent cut
10321. F10321 Distributed Systems & Cloud — inconsistent checkpoint
10322. F10322 ML & AI — bayes net
10323. F10323 Mathematics — superset
10324. F10324 Other/Unknown — truth-functionally inconsistent
10325. F10325 Software Engineering — information hiding
10326. F10326 ML & AI — alpha
10327. F10327 Computer Architecture — minus alpha
10328. F10328 ML & AI — alpha and beta
10329. F10329 Software Engineering — linear complexity
10330. F10330 Curriculum-only — berlekamp massey linear-complexity attack
10331. F10331 Software Engineering — max cut
10332. F10332 Algorithms & Theory of CS — approximation algorithm for max-cut
10333. F10333 Curriculum-only — semidefinite programming for max cut
10334. F10334 Mathematics — maximum cut
10335. F10335 Software Engineering — mutation
10336. F10336 Curriculum-only — mutation operator
10337. F10337 Data Mining & Databases — data mutation
10338. F10338 Software Engineering — mutation and iteration
10339. F10339 HS ComputerScience Class XII / Unit 1: Computational Thinking and Programming – 2 — exception handling
10340. F10340 Curriculum-only — function-oriented and object-oriented
10341. F10341 Data Mining & Databases — meta-circular evaluator
10342. F10342 Software Engineering — Object-oriented abstractions: multiple inheritance, mixins, traits, multimethods
10343. F10343 Curriculum-only — api and object-oriented design
10344. F10344 Distributed Systems & Cloud — distributed object
10345. F10345 Computer Networks — ttr
10346. F10346 Distributed Systems & Cloud — test set lock
10347. F10347 Algorithms & Theory of CS — universality
10348. F10348 Distributed Systems & Cloud — blocking
10349. F10349 Mathematics — blocking factor
10350. F10350 Algorithms & Theory of CS — guarantee provided
10351. F10351 Cryptography & Security — strong cryptographic guarantee
10352. F10352 Curriculum-only — absolute guarantee
10353. F10353 Distributed Systems & Cloud — list-based set guarantee atomicity
10354. F10354 Information Theory & Coding — sufficient to guarantee
10355. F10355 ML & AI — performance guarantee
10356. F10356 Mathematics — abd
10357. F10357 Curriculum-only — irreducibility and aperiodicity
10358. F10358 Data Mining & Databases — algebraic extension
10359. F10359 Mathematics — top row
10360. F10360 Operating Systems — consistency guarantee
10361. F10361 Curriculum-only — pipelined and non-blocking cache
10362. F10362 Other/Unknown — lock-free and wait-free
10363. F10363 Algorithms & Theory of CS — process automaton pu
10364. F10364 Curriculum-only — legal clause
10365. F10365 Data Mining & Databases — consequent
10366. F10366 ML & AI — empty clause
10367. F10367 Mathematics — homogeneous equation
10368. F10368 Curriculum-only — homogeneous equation and bernoulli equation
10369. F10369 Mathematics — corresponding homogeneous equation
10370. F10370 Data Mining & Databases — modus
10371. F10371 Mathematics — derivation
10372. F10372 Cryptography & Security — key derivation
10373. F10373 Curriculum-only — fuzzy extractor for biometric key derivation
10374. F10374 Mathematics — drove
10375. F10375 NLP & Speech — drove pp
10376. F10376 Other/Unknown — derivation in pd
10377. F10377 Software Engineering — assertion
10378. F10378 Cryptography & Security — neo
10379. F10379 Curriculum-only — assertion in code
10380. F10380 Data Mining & Databases — watson
10381. F10381 ML & AI — list of assertion
10382. F10382 Mathematics — checkable proof
10383. F10383 Cryptography & Security — probabilistically checkable proof
10384. F10384 Mathematics — galton-watson tree
10385. F10385 Curriculum-only — truth value unknown
10386. F10386 ML & AI — propositional variable
10387. F10387 NLP & Speech — vb pp
10388. F10388 Software Engineering — implementing
10389. F10389 Cryptography & Security — implementing and compromising
10390. F10390 Curriculum-only — implementing causal order with vector clock
10391. F10391 Distributed Systems & Cloud — concurrent object
10392. F10392 Operating Systems — implementing lock
10393. F10393 Software Engineering — implementing evolution
10394. F10394 Data Mining & Databases — object oriented programming iii
10395. F10395 Operating Systems — return-oriented programming
10396. F10396 Software Engineering — object-oriented programming languages
10397. F10397 Algorithms & Theory of CS — bottom-up
10398. F10398 Curriculum-only — query processor with parser
10399. F10399 NLP & Speech — CFGs and chart parsers (e.g., CYK)
10400. F10400 Curriculum-only — gcloud grammar
10401. F10401 Data Mining & Databases — formal language
10402. F10402 Curriculum-only — proof paradigm and formal language
10403. F10403 Mathematics — detective
10404. F10404 NLP & Speech — earley parser
10405. F10405 Curriculum-only — finding class by noun
10406. F10406 Mathematics — topping
10407. F10407 NLP & Speech — determiner
10408. F10408 Algorithms & Theory of CS — conjunction
10409. F10409 Distributed Systems & Cloud — placement
10410. F10410 Curriculum-only — block placement by direct mapping
10411. F10411 Distributed Systems & Cloud — placement policy
10412. F10412 Mathematics — placement and location
10413. F10413 NLP & Speech — brown corpus
10414. F10414 Algorithms & Theory of CS — chomsky normal form
10415. F10415 Mathematics — y1 y2
10416. F10416 NLP & Speech — rewrite rule
10417. F10417 ML & AI — learnability
10418. F10418 Curriculum-only — tradeoff between representational power and learnability
10419. F10419 NLP & Speech — top-down and bottom-up
10420. F10420 Other/Unknown — pole placement
10421. F10421 Software Engineering — abstract syntax
10422. F10422 Curriculum-only — auto-converge
10423. F10423 Distributed Systems & Cloud — std
10424. F10424 Information Theory & Coding — auto-regressive model
10425. F10425 Curriculum-only — vector auto-regressive model
10426. F10426 Information Theory & Coding — tos
10427. F10427 Mathematics — auto story
10428. F10428 NLP & Speech — auto and cross-correlation
10429. F10429 Other/Unknown — auto encoder
10430. F10430 Curriculum-only — auto encoder and relation to pca
10431. F10431 Signal/Image/Audio/Video Processing — freq
10432. F10432 Software Engineering — bottom-up parsing
10433. F10433 NLP & Speech — sentence comprehension
10434. F10434 Signal/Image/Audio/Video Processing — verbal
10435. F10435 Mathematics — disadvantage
10436. F10436 Curriculum-only — disadvantage are application complexity
10437. F10437 Mathematics — preserve
10438. F10438 Curriculum-only — guarantee does and does not preserve
10439. F10439 Distributed Systems & Cloud — preserve dependency
10440. F10440 Mathematics — arnoldi
10441. F10441 Other/Unknown — advantage and disadvantage
10442. F10442 Signal/Image/Audio/Video Processing — verbal working memory
10443. F10443 Software Engineering — comprehension test score
10444. F10444 Distributed Systems & Cloud — gibson
10445. F10445 NLP & Speech — desmet gibson
10446. F10446 Distributed Systems & Cloud — tagged
10447. F10447 Curriculum-only — dual-tagged cache
10448. F10448 Data Mining & Databases — tagged-list
10449. F10449 Information Theory & Coding — bass
10450. F10450 NLP & Speech — chunking
10451. F10451 Curriculum-only — chunking and query formulation
10452. F10452 NLP & Speech — verb
10453. F10453 Curriculum-only — finding class from noun and verb
10454. F10454 Mathematics — sim
10455. F10455 NLP & Speech — acura
10456. F10456 Mathematics — ate
10457. F10457 Data Mining & Databases — paired
10458. F10458 Curriculum-only — development phase paired
10459. F10459 Mathematics — head
10460. F10460 Algorithms & Theory of CS — add child
10461. F10461 Cryptography & Security — agr
10462. F10462 Curriculum-only — combining head
10463. F10463 Information Theory & Coding — head-of-line blocking
10464. F10464 ML & AI — head normal form
10465. F10465 Mathematics — bent coin
10466. F10466 Algorithms & Theory of CS — unbiased coin flip
10467. F10467 Mathematics — bernoulli trial
10468. F10468 Algorithms & Theory of CS — extended path
10469. F10469 Cryptography & Security — extended euclid
10470. F10470 Curriculum-only — extended euclid algorithm
10471. F10471 Data Mining & Databases — period of time
10472. F10472 Information Theory & Coding — error curve
10473. F10473 ML & AI — extended node
10474. F10474 Mathematics — extended cover
10475. F10475 Algorithms & Theory of CS — biased coin flip
10476. F10476 Mathematics — coin toss
10477. F10477 Curriculum-only — posterior of the coefficient
10478. F10478 ML & AI — m-step
10479. F10479 Data Mining & Databases — k-means algorithm
10480. F10480 ML & AI — metropolis-hasting algorithm
10481. F10481 Mathematics — bayes factor
10482. F10482 Data Mining & Databases — predictive probability
10483. F10483 ML & AI — posterior predictive
10484. F10484 Curriculum-only — posterior predictive interval
10485. F10485 Mathematics — bayesian updating with continuous
10486. F10486 Curriculum-only — denominator by the conjugate
10487. F10487 Information Theory & Coding — nelder
10488. F10488 ML & AI — bra
10489. F10489 Curriculum-only — hyperparameter tuning
10490. F10490 Mathematics — choosing prior
10491. F10491 Information Theory & Coding — ket
10492. F10492 Mathematics — conjugacy
10493. F10493 ML & AI — convex conjugate
10494. F10494 Mathematics — conjugate pair
10495. F10495 Curriculum-only — conjugate-pair theorem for real coefficient
10496. F10496 Mathematics — conjugate transpose
10497. F10497 Curriculum-only — complex vector and the conjugate transpose
10498. F10498 Mathematics — data with continuous prior
10499. F10499 Curriculum-only — harmonic conjugate and milne
10500. F10500 Mathematics — multinomial
10501. F10501 Curriculum-only — bernoulli trial and the multinomial
10502. F10502 Data Mining & Databases — multinomial repr
10503. F10503 Mathematics — polar cone
10504. F10504 Data Mining & Databases — srw
10505. F10505 Information Theory & Coding — virtual circuit
10506. F10506 Curriculum-only — virtual-circuit service
10507. F10507 ML & AI — mathematics of machine learning
10508. F10508 Distributed Systems & Cloud — oct
10509. F10509 ML & AI — loss function
10510. F10510 Curriculum-only — activation and loss function
10511. F10511 Data Mining & Databases — artificial neural network
10512. F10512 Curriculum-only — hands-on artificial neural network for classification
10513. F10513 ML & AI — arg min
10514. F10514 Data Mining & Databases — gradient boosting bagging
10515. F10515 ML & AI — boosting and bagging
10516. F10516 Curriculum-only — soft margin and the hinge loss
10517. F10517 ML & AI — convex surrogate
10518. F10518 Algorithms & Theory of CS — novel data-motivated matrix factorization
10519. F10519 ML & AI — noise condition
10520. F10520 Curriculum-only — cart and random forest
10521. F10521 Data Mining & Databases — random forest model
10522. F10522 ML & AI — regret
10523. F10523 Curriculum-only — bayesian regret
10524. F10524 ML & AI — expert
10525. F10525 Curriculum-only — information expert
10526. F10526 Data Mining & Databases — expert judgement
10527. F10527 Curriculum-only — expert judgement and the delphi
10528. F10528 Data Mining & Databases — replicating expert assessment
10529. F10529 Distributed Systems & Cloud — subject matter expert
10530. F10530 ML & AI — bandit
10531. F10531 Cryptography & Security — bandit setting
10532. F10532 Curriculum-only — adversarial full-information and bandit setting
10533. F10533 ML & AI — adversarial bandit
10534. F10534 Curriculum-only — att ck navigator layer
10535. F10535 ML & AI — att zt
10536. F10536 Curriculum-only — mixture of expert are named
10537. F10537 ML & AI — prediction with expert advise
10538. F10538 Curriculum-only — lower bound for stochastic bandit
10539. F10539 ML & AI — train
10540. F10540 Algorithms & Theory of CS — minimum and maximum
10541. F10541 Computer Architecture — source signal
10542. F10542 Cryptography & Security — blind
10543. F10543 Curriculum-only — blind and time-based
10544. F10544 Data Mining & Databases — double blind
10545. F10545 Distributed Systems & Cloud — blind signature
10546. F10546 ML & AI — a8z1sltj6zd7
10547. F10547 Algorithms & Theory of CS — probably approximately correct learning
10548. F10548 ML & AI — structural risk minimization
10549. F10549 Mathematics — accuracy
10550. F10550 Curriculum-only — accuracy paradox on skewed
10551. F10551 Mathematics — arg min fk
10552. F10552 Curriculum-only — cost function as maximum likelihood
10553. F10553 ML & AI — wij
10554. F10554 Data Mining & Databases — ncut
10555. F10555 ML & AI — zi zj
10556. F10556 Mathematics — de ne
10557. F10557 Algorithms & Theory of CS — dynamic programming
10558. F10558 Cryptography & Security — brute force attack
10559. F10559 Curriculum-only — conjecture by brute force before proving
10560. F10560 Data Mining & Databases — memoisation
10561. F10561 Curriculum-only — memoisation against tabulation
10562. F10562 Mathematics — bellman equation
10563. F10563 ML & AI — forecaster choose
10564. F10564 Mathematics — high-order accuracy
10565. F10565 ML & AI — positive real value
10566. F10566 Mathematics — earning
10567. F10567 Computer Networks — earning report
10568. F10568 Mathematics — positive real axis
10569. F10569 Curriculum-only — read kb randomly from ssd
10570. F10570 Mathematics — stability and accuracy
10571. F10571 Data Mining & Databases — decomposition group
10572. F10572 Mathematics — support function
10573. F10573 Computer Architecture — attitude indicator
10574. F10574 Computer Networks — key performance indicator
10575. F10575 Curriculum-only — domain object such as indicator
10576. F10576 Mathematics — compass
10577. F10577 Algorithms & Theory of CS — compass and straightedge
10578. F10578 Mathematics — indicator variable
10579. F10579 Curriculum-only — linearity of expectation and indicator variable
10580. F10580 Mathematics — ruler
10581. F10581 Data Mining & Databases — projective curve
10582. F10582 Mathematics — sgn
10583. F10583 Algorithms & Theory of CS — finding tangent
10584. F10584 Curriculum-only — chord-and-tangent law
10585. F10585 ML & AI — tangent space
10586. F10586 Mathematics — conformal
10587. F10587 Curriculum-only — argument principle and rouch
10588. F10588 Mathematics — contour plot
10589. F10589 Data Mining & Databases — algebraic set
10590. F10590 Mathematics — local ring
10591. F10591 ML & AI — acceptable understanding
10592. F10592 Mathematics — ax2
10593. F10593 Mathematics — updating with continuous prior
10594. F10594 Curriculum-only — m-step as weighted average
10595. F10595 ML & AI — exponentially weighted average
10596. F10596 Mathematics — semicircle
10597. F10597 NLP & Speech — baseline
10598. F10598 Curriculum-only — baseline and advantage estimation
10599. F10599 Data Mining & Databases — covariate
10600. F10600 Mathematics — link function
10601. F10601 NLP & Speech — cat ate
10602. F10602 ML & AI — mixture of gaussian model
10603. F10603 NLP & Speech — hair
10604. F10604 Operating Systems — blind write
10605. F10605 Other/Unknown — approximate dynamic programming
10606. F10606 Algorithms & Theory of CS — robot arm
10607. F10607 Curriculum-only — arm and risc-v weak model
10608. F10608 Other/Unknown — artificial neural network (ann)
10609. F10609 Distributed Systems & Cloud — preconditioned conjugate gradient
10610. F10610 Mathematics — convergence of conjugate gradient
10611. F10611 Curriculum-only — reduced gradient algorithm
10612. F10612 Mathematics — biconjugate gradient algorithm
10613. F10613 Other/Unknown — discriminant analysis
10614. F10614 Data Mining & Databases — linear discriminant
10615. F10615 Mathematics — net
10616. F10616 Algorithms & Theory of CS — bayes net inference
10617. F10617 ML & AI — doutdx
10618. F10618 Mathematics — net dollar
10619. F10619 NLP & Speech — semantic net
10620. F10620 Other/Unknown — expert elicitation
10621. F10621 Curriculum-only — calibrated estimation and expert elicitation
10622. F10622 Other/Unknown — function approximation
10623. F10623 Curriculum-only — convergence under linear function approximation
10624. F10624 Other/Unknown — graph neural network
10625. F10625 Curriculum-only — graph neural network inference system
10626. F10626 Other/Unknown — kurtosis
10627. F10627 Mathematics — markov decision theory
10628. F10628 Other/Unknown — multi-armed bandit
10629. F10629 Curriculum-only — policy gradient theorem
10630. F10630 Other/Unknown — robotic arms
10631. F10631 Algorithms & Theory of CS — policy evaluation
10632. F10632 Curriculum-only — offline policy evaluation
10633. F10633 Signal/Image/Audio/Video Processing — blind separation
10634. F10634 Curriculum-only — deadlock prevention
10635. F10635 Other/Unknown — modeling and analysis
10636. F10636 Signal/Image/Audio/Video Processing — signal separation
10637. F10637 Software Engineering — bandit algorithm
10638. F10638 Curriculum-only — stochastic bandit algorithm ucb
10639. F10639 Software Engineering — data synchronization
10640. F10640 Mathematics — Solving equations, row-reduction
10641. F10641 Curriculum-only — newton method for solving equation
10642. F10642 Software Engineering — gen subset
10643. F10643 Mathematics — initial state
10644. F10644 Software Engineering — shift-reduce parsing
10645. F10645 Distributed Systems & Cloud — aws
10646. F10646 Curriculum-only — primer cloud example are aws
10647. F10647 Distributed Systems & Cloud — high performance
10648. F10648 Computer Architecture — architecture of high performance
10649. F10649 Curriculum-only — high-performance network are designed
10650. F10650 Distributed Systems & Cloud — data parallel
10651. F10651 Curriculum-only — message passing and data parallel
10652. F10652 Distributed Systems & Cloud — data-parallel model
10653. F10653 Other/Unknown — data-parallel programming
10654. F10654 Software Engineering — complex software systems
10655. F10655 Mathematics — dynamic language for technical
10656. F10656 Software Engineering — high-performance memory
10657. F10657 Distributed Systems & Cloud — charle leiserson
10658. F10658 Algorithms & Theory of CS — michael bender
10659. F10659 Distributed Systems & Cloud — kuszmaul
10660. F10660 Computer Networks — ftp
10661. F10661 Cryptography & Security — symposium
10662. F10662 Algorithms & Theory of CS — computational geometry
10663. F10663 Curriculum-only — amortised analysis and more computational geometry
10664. F10664 ML & AI — extending to tree
10665. F10665 Mathematics — annual
10666. F10666 Distributed Systems & Cloud — st annual ieee symposium
10667. F10667 Mathematics — proceeding
10668. F10668 Algorithms & Theory of CS — symposium on theory
10669. F10669 Cryptography & Security — mas
10670. F10670 Curriculum-only — model of aggarwal
10671. F10671 Data Mining & Databases — carter
10672. F10672 Curriculum-only — carter wegman universal hashing
10673. F10673 Data Mining & Databases — hierarchical
10674. F10674 Curriculum-only — hierarchical and k-mean clustering
10675. F10675 Data Mining & Databases — hierarchical clustering
10676. F10676 Distributed Systems & Cloud — hierarchical lock
10677. F10677 Information Theory & Coding — ieee tran
10678. F10678 ML & AI — conference proceeding
10679. F10679 Curriculum-only — bayesian regression and hierarchical model
10680. F10680 ML & AI — hierarchical modeling
10681. F10681 Curriculum-only — bayesian hierarchical modeling
10682. F10682 ML & AI — national academy of science
10683. F10683 Mathematics — pub
10684. F10684 Distributed Systems & Cloud — ieee computer
10685. F10685 Mathematics — xi yi
10686. F10686 NLP & Speech — computation hierarchical parsing
10687. F10687 ML & AI — gaussian bp
10688. F10688 Mathematics — brill
10689. F10689 Algorithms & Theory of CS — pebble game
10690. F10690 NLP & Speech — aabb
10691. F10691 Information Theory & Coding — bbn
10692. F10692 Distributed Systems & Cloud — internet
10693. F10693 HS ComputerScience Class XII / Unit 2: Computer Networks — network protocol
10694. F10694 Computer Networks — future internet
10695. F10695 Cryptography & Security — firewall
10696. F10696 Curriculum-only — cloud service platform over the internet
10697. F10697 Distributed Systems & Cloud — facebook
10698. F10698 Curriculum-only — facebook chat function
10699. F10699 Distributed Systems & Cloud — facebook cassandra
10700. F10700 Curriculum-only — facebook cassandra and google percolator
10701. F10701 Distributed Systems & Cloud — firewall rule
10702. F10702 Curriculum-only — firewall rule as stateful
10703. F10703 Information Theory & Coding — berkley
10704. F10704 ML & AI — multivariate gaussian
10705. F10705 Mathematics — akamai
10706. F10706 Curriculum-only — gamma and beta family
10707. F10707 ML & AI — exponential family
10708. F10708 Curriculum-only — mixture distribution and the exponential family
10709. F10709 ML & AI — generalized linear model
10710. F10710 Mathematics — canonical exponential family
10711. F10711 NLP & Speech — acoustic modeling
10712. F10712 Computer Networks — size estimation
10713. F10713 Curriculum-only — size estimation and semantic optimisation
10714. F10714 NLP & Speech — spoken language processing
10715. F10715 Information Theory & Coding — possible state
10716. F10716 ML & AI — hidden state
10717. F10717 Mathematics — odd number
10718. F10718 Algorithms & Theory of CS — variable ordering
10719. F10719 Curriculum-only — read repair
10720. F10720 Mathematics — genetic
10721. F10721 Data Mining & Databases — genetics
10722. F10722 Distributed Systems & Cloud — evolutionary
10723. F10723 Data Mining & Databases — Evolutionary algorithms
10724. F10724 Mathematics — genetic marker
10725. F10725 NLP & Speech — hidden state sequence
10726. F10726 Operating Systems — austin
10727. F10727 Data Mining & Databases — los angele
10728. F10728 Operating Systems — austin clement
10729. F10729 Other/Unknown — electric power
10730. F10730 Information Theory & Coding — electric power industries
10731. F10731 Other/Unknown — evolutionary optimization
10732. F10732 Curriculum-only — dram system
10733. F10733 Other/Unknown — noise source
10734. F10734 Information Theory & Coding — turbulence noise source
10735. F10735 Other/Unknown — Population genetics
10736. F10736 Signal/Image/Audio/Video Processing — signal noise
10737. F10737 Software Engineering — engineering and computer
10738. F10738 Algorithms & Theory of CS — eric price
10739. F10739 Distributed Systems & Cloud — eric brewer
10740. F10740 Software Engineering — evolutionary model
10741. F10741 Curriculum-only — incremental and the evolutionary model
10742. F10742 Software Engineering — excerpt
10743. F10743 Mathematics — charge
10744. F10744 Computer Architecture — capacitance
10745. F10745 Mathematics — charge density
10746. F10746 Data Mining & Databases — fixed-charge covering ratio
10747. F10747 Mathematics — inductance
10748. F10748 Other/Unknown — battery
10749. F10749 Information Theory & Coding — voltage battery
10750. F10750 Other/Unknown — charge carrier
10751. F10751 Computer Architecture — low voltage
10752. F10752 Information Theory & Coding — high voltage battery
10753. F10753 Other/Unknown — charging
10754. F10754 Curriculum-only — momentum and adaptive method are named
10755. F10755 Mathematics — position and momentum
10756. F10756 Other/Unknown — angular momentum
10757. F10757 Software Engineering — firefox
10758. F10758 Mathematics — adam
10759. F10759 Curriculum-only — sgd with momentum and adam
10760. F10760 Data Mining & Databases — adam marcus
10761. F10761 Operating Systems — adam belay
10762. F10762 Software Engineering — adam barth
10763. F10763 Other/Unknown — coherence
10764. F10764 Curriculum-only — coherence half
10765. F10765 Distributed Systems & Cloud — coherence protocol
10766. F10766 Curriculum-only — coherence protocol snooping
10767. F10767 Information Theory & Coding — coherence frequency
10768. F10768 NLP & Speech — local coherence
10769. F10769 Other/Unknown — coherence and consistency
10770. F10770 Software Engineering — software evolution
10771. F10771 Curriculum-only — lehman law of software evolution
10772. F10772 Software Engineering — specifier
10773. F10773 Algorithms & Theory of CS — devise
10774. F10774 Computer Architecture — report template
10775. F10775 Curriculum-only — aws design use the same template
10776. F10776 Other/Unknown — template protection
10777. F10777 Signal/Image/Audio/Video Processing — template matching
10778. F10778 NLP & Speech — automatic
10779. F10779 Algorithms & Theory of CS — church
10780. F10780 Curriculum-only — automatic cot
10781. F10781 Data Mining & Databases — alonzo church
10782. F10782 Distributed Systems & Cloud — designing
10783. F10783 Computer Architecture — designing sound
10784. F10784 Curriculum-only — designing efficient algorithm for approximately optimal
10785. F10785 Distributed Systems & Cloud — designing algorithm
10786. F10786 Information Theory & Coding — alarm
10787. F10787 Distributed Systems & Cloud — miss
10788. F10788 Algorithms & Theory of CS — recursion tree
10789. F10789 Computer Architecture — direct-mapped
10790. F10790 Curriculum-only — analytic miss model
10791. F10791 Curriculum-only — solving the recurrence for merge sort by the recursion tree
10792. F10792 Distributed Systems & Cloud — cache line
10793. F10793 Algorithms & Theory of CS — Asymptotic analysis
10794. F10794 Distributed Systems & Cloud — cache miss
10795. F10795 Algorithms & Theory of CS — cache-oblivious
10796. F10796 Computer Architecture — cache performance
10797. F10797 Curriculum-only — correctness of coherence protocol type of cache miss
10798. F10798 Distributed Systems & Cloud — incorporating cache-oblivious distribution
10799. F10799 Information Theory & Coding — cannon
10800. F10800 Curriculum-only — family-wise error rate
10801. F10801 Information Theory & Coding — error occur
10802. F10802 ML & AI — american english
10803. F10803 Computer Networks — dialog box
10804. F10804 Curriculum-only — dialog as nlp
10805. F10805 ML & AI — model parameter
10806. F10806 Mathematics — associativity
10807. F10807 Curriculum-only — loss of associativity
10808. F10808 Mathematics — additive inverse
10809. F10809 ML & AI — umbrella
10810. F10810 Mathematics — cooley-tukey
10811. F10811 Distributed Systems & Cloud — cooley-tukey butterfly
10812. F10812 Mathematics — codelet
10813. F10813 Curriculum-only — layer guarantee compose
10814. F10814 Mathematics — cooley-tukey algorithm present
10815. F10815 Curriculum-only — donne martin
10816. F10816 Mathematics — ml estimation
10817. F10817 ML & AI — ml estimate
10818. F10818 Mathematics — noon
10819. F10819 Information Theory & Coding — control character
10820. F10820 Mathematics — apr
10821. F10821 Algorithms & Theory of CS — star tracker
10822. F10822 Computer Networks — star graphs
10823. F10823 Curriculum-only — multiset and star and bar
10824. F10824 Mathematics — submatrix
10825. F10825 NLP & Speech — acoustic modelling
10826. F10826 Mathematics — perturbation
10827. F10827 Algorithms & Theory of CS — perturbation analysis
10828. F10828 ML & AI — data augmentation
10829. F10829 Curriculum-only — image preprocessing and data augmentation
10830. F10830 NLP & Speech — bayesian classification
10831. F10831 Data Mining & Databases — breadth
10832. F10832 Algorithms & Theory of CS — depth rst search
10833. F10833 ML & AI — hill-climbing
10834. F10834 Mathematics — best
10835. F10835 Algorithms & Theory of CS — constituent kernel
10836. F10836 Cryptography & Security — best score
10837. F10837 Curriculum-only — best and average
10838. F10838 Data Mining & Databases — best experience
10839. F10839 Distributed Systems & Cloud — best n-1
10840. F10840 Information Theory & Coding — best effort
10841. F10841 ML & AI — approximation error
10842. F10842 Mathematics — alien
10843. F10843 Information Theory & Coding — maximum possible
10844. F10844 ML & AI — kmax
10845. F10845 Mathematics — bivariate data
10846. F10846 Algorithms & Theory of CS — a-approximation algorithm
10847. F10847 Computer Networks — modularity maximization
10848. F10848 Curriculum-only — rate maximisation
10849. F10849 Data Mining & Databases — influence maximization in social
10850. F10850 Mathematics — sum of square
10851. F10851 Curriculum-only — sum of square finite
10852. F10852 Data Mining & Databases — sst
10853. F10853 Mathematics — squared error
10854. F10854 Data Mining & Databases — sum of squared error
10855. F10855 ML & AI — least squared error
10856. F10856 Curriculum-only — linear minimum mean squared error
10857. F10857 Data Mining & Databases — root mean squared error
10858. F10858 Information Theory & Coding — scalar quantizer
10859. F10859 ML & AI — vt av
10860. F10860 Mathematics — mean square
10861. F10861 Information Theory & Coding — mean square estimation
10862. F10862 Mathematics — necessary condition
10863. F10863 NLP & Speech — best path
10864. F10864 Curriculum-only — roc curve and equal error rate
10865. F10865 NLP & Speech — filler
10866. F10866 Mathematics — overlap
10867. F10867 Algorithms & Theory of CS — camera model
10868. F10868 Curriculum-only — double buffering to overlap transfer
10869. F10869 Data Mining & Databases — significant overlap
10870. F10870 Distributed Systems & Cloud — approximate percentage of overlap
10871. F10871 Information Theory & Coding — gestural overlap
10872. F10872 NLP & Speech — galaxy
10873. F10873 Distributed Systems & Cloud — release
10874. F10874 Curriculum-only — differentially private release of one statistic
10875. F10875 Distributed Systems & Cloud — acquire and release
10876. F10876 Curriculum-only — release-consistency family
10877. F10877 Information Theory & Coding — consonant release
10878. F10878 NLP & Speech — voiceless
10879. F10879 Operating Systems — cache block
10880. F10880 Curriculum-only — set associativity and full associativity
10881. F10881 Operating Systems — higher associativity
10882. F10882 Curriculum-only — larger cache and higher associativity
10883. F10883 Operating Systems — lru cache
10884. F10884 Curriculum-only — structure behind an lru cache
10885. F10885 Operating Systems — miss rate
10886. F10886 Distributed Systems & Cloud — cache miss rate
10887. F10887 Operating Systems — victim cache
10888. F10888 Other/Unknown — lie algebras
10889. F10889 Mathematics — topology
10890. F10890 Algorithms & Theory of CS — optimal substructure
10891. F10891 Computer Networks — degree distribution
10892. F10892 Curriculum-only — clo topology
10893. F10893 Data Mining & Databases — homeomorphism
10894. F10894 ML & AI — induced topology
10895. F10895 Mathematics — closed subset
10896. F10896 Data Mining & Databases — finite abelian extension
10897. F10897 Mathematics — norm group
10898. F10898 Other/Unknown — Algebraic topology
10899. F10899 Mathematics — linear operator
10900. F10900 Other/Unknown — functional analysis
10901. F10901 ML & AI — hilbert space
10902. F10902 Mathematics — infinite-dimensional
10903. F10903 ML & AI — infinite-dimensional space
10904. F10904 Other/Unknown — measure of central tendency
10905. F10905 Mathematics — skewness
10906. F10906 Other/Unknown — star topology
10907. F10907 Signal/Image/Audio/Video Processing — associated mean-square
10908. F10908 Data Mining & Databases — orthogonal group
10909. F10909 Mathematics — euclidean space
10910. F10910 ML & AI — non-euclidean space
10911. F10911 Signal/Image/Audio/Video Processing — orthonormal rotation matrix
10912. F10912 Software Engineering — align
10913. F10913 Curriculum-only — align it with sft plus dpo
10914. F10914 Software Engineering — autotuning
10915. F10915 Distributed Systems & Cloud — framework
10916. F10916 Computer Architecture — rls
10917. F10917 Computer Networks — financial stability
10918. F10918 Cryptography & Security — Legal frameworks, compliance requirements
10919. F10919 Curriculum-only — analyse data in the bayesian framework
10920. F10920 Curriculum-only — risk management framework
10921. F10921 Distributed Systems & Cloud — framework for map-reduce
10922. F10922 ML & AI — common framework
10923. F10923 Mathematics — approximation framework
10924. F10924 Curriculum-only — np-completeness and the approximation framework
10925. F10925 Mathematics — better understand
10926. F10926 Distributed Systems & Cloud — tioa
10927. F10927 Mathematics — covered
10928. F10928 Curriculum-only — straggler problem are covered
10929. F10929 Distributed Systems & Cloud — partially covered
10930. F10930 Mathematics — pose
10931. F10931 ML & AI — object pose
10932. F10932 Curriculum-only — compliance scoring
10933. F10933 Data Mining & Databases — scoring algorithm
10934. F10934 Mathematics — fisher-scoring
10935. F10935 NLP & Speech — confidence scoring
10936. F10936 Other/Unknown — computing framework
10937. F10937 Signal/Image/Audio/Video Processing — deep learning framework
10938. F10938 Curriculum-only — deep-learning framework from scratch
10939. F10939 Signal/Image/Audio/Video Processing — devoted to material covered
10940. F10940 ML & AI — multiclass classification
10941. F10941 Signal/Image/Audio/Video Processing — patquick
10942. F10942 Software Engineering — available expression
10943. F10943 Software Engineering — fewer capacity miss
10944. F10944 Cryptography & Security — disclosure
10945. F10945 Curriculum-only — coordinated disclosure
10946. F10946 Software Engineering — kleene star
10947. F10947 Mathematics — dual function
10948. F10948 Curriculum-only — differentiability of the dual function
10949. F10949 Mathematics — lagrange dual function
10950. F10950 Software Engineering — rec mult
10951. F10951 Mathematics — abcd
10952. F10952 Algorithms & Theory of CS — shortest path estimate
10953. F10953 Mathematics — schrodinger fd adj
10954. F10954 Software Engineering — star rating widget
10955. F10955 Cryptography & Security — usage data
10956. F10956 Curriculum-only — calculate usage
10957. F10957 Distributed Systems & Cloud — resource usage
10958. F10958 Algorithms & Theory of CS — number of node
10959. F10959 Distributed Systems & Cloud — htm
10960. F10960 Mathematics — compared
10961. F10961 Algorithms & Theory of CS — space efficient compared
10962. F10962 Curriculum-only — bayesian interval compared
10963. F10963 Mathematics — desirable
10964. F10964 Information Theory & Coding — cellular network
10965. F10965 ML & AI — estimation error
10966. F10966 Curriculum-only — bounding estimation error in binary classification
10967. F10967 Mathematics — mean-square estimation error
10968. F10968 Curriculum-only — slower write
10969. F10969 Mathematics — station
10970. F10970 Curriculum-only — station-to-station
10971. F10971 Information Theory & Coding — base station
10972. F10972 Mathematics — service station
10973. F10973 Other/Unknown — charging station
10974. F10974 Signal/Image/Audio/Video Processing — absolute orientation
10975. F10975 Mathematics — quaternion
10976. F10976 Data Mining & Databases — quaternion algebra
10977. F10977 Mathematics — division ring
10978. F10978 Signal/Image/Audio/Video Processing — outlier and robustness
10979. F10979 Software Engineering — block size
10980. F10980 Curriculum-only — choosing block size
10981. F10981 Software Engineering — user id
10982. F10982 Curriculum-only — byte user id
10983. F10983 Software Engineering — uti uj
10984. F10984 ML & AI — variable binding constraint
10985. F10985 Software Engineering — vector add
10986. F10986 Curriculum-only — deliberately vulnerable lab vm
10987. F10987 Software Engineering — walkerton
10988. F10988 Curriculum-only — trigger and watermark
10989. F10989 Software Engineering — web app
10990. F10990 Curriculum-only — unpatched web framework
10991. F10991 Software Engineering — web programming
10992. F10992 Distributed Systems & Cloud — curr
10993. F10993 Software Engineering — wrapper
10994. F10994 Curriculum-only — handler wrapper
10995. F10995 Software Engineering — xeon
10996. F10996 Data Mining & Databases — zip code
10997. F10997 Mathematics — zlp zd zip
10998. F10998 System Design Primer / Application layer — service discovery
10999. F10999 System Design Primer / Availability patterns — active-active
11000. F11000 System Design Primer / Cache — web server caching
11001. F11001 System Design Primer / Communication — communication
11002. F11002 Algorithms & Theory of CS — communication complexity
11003. F11003 Computer Architecture — digital signaling
11004. F11004 Computer Networks — carry voice
11005. F11005 Curriculum-only — average is the only communication
11006. F11006 Curriculum-only — role and communication
11007. F11007 Distributed Systems & Cloud — Application-level sequential processing: single thread
11008. F11008 Curriculum-only — inter-process communication and synchronization
11009. F11009 Distributed Systems & Cloud — communication area
11010. F11010 Curriculum-only — complexity measure of code
11011. F11011 Distributed Systems & Cloud — computation-to-communication ratio
11012. F11012 Curriculum-only — dedicated interconnect
11013. F11013 Distributed Systems & Cloud — distributed network
11014. F11014 Curriculum-only — group communication and virtual synchrony
11015. F11015 Distributed Systems & Cloud — load balance
11016. F11016 Curriculum-only — communication-to-computation ratio and load balance
11017. F11017 Distributed Systems & Cloud — load balancing
11018. F11018 Curriculum-only — ecmp and load balancing
11019. F11019 Distributed Systems & Cloud — dynamic load balancing
11020. F11020 Computer Networks — instant messaging
11021. F11021 Curriculum-only — broker form is the messaging
11022. F11022 Distributed Systems & Cloud — messaging system
11023. F11023 Information Theory & Coding — acoustic channels
11024. F11024 Computer Networks — tcp
11025. F11025 Computer Architecture — handshake
11026. F11026 Computer Networks — ip protocol
11027. F11027 Cryptography & Security — anonymous communication
11028. F11028 Curriculum-only — anonymous communication by mix
11029. F11029 Data Mining & Databases — arp
11030. F11030 Cryptography & Security — arp spoofing
11031. F11031 Curriculum-only — arp protocol
11032. F11032 Data Mining & Databases — bellovin
11033. F11033 Distributed Systems & Cloud — avoidance
11034. F11034 Algorithms & Theory of CS — pattern avoidance
11035. F11035 Computer Networks — collision avoidance
11036. F11036 Curriculum-only — avoidance of deadlock
11037. F11037 Distributed Systems & Cloud — communicating
11038. F11038 Computer Architecture — communicating process
11039. F11039 Curriculum-only — share-memory-by-communicating idiom
11040. F11040 Distributed Systems & Cloud — communicating sequential process
11041. F11041 Information Theory & Coding — arp cache
11042. F11042 Computer Networks — manet
11043. F11043 Curriculum-only — music algorithm
11044. F11044 Distributed Systems & Cloud — broadcast
11045. F11045 Algorithms & Theory of CS — machine broadcast
11046. F11046 Cryptography & Security — atomic broadcast
11047. F11047 Curriculum-only — atomic-broadcast protocol that order write
11048. F11048 Distributed Systems & Cloud — ghs
11049. F11049 Data Mining & Databases — scatter gather
11050. F11050 Curriculum-only — consistent hashing and scatter gather
11051. F11051 Data Mining & Databases — scatter plot
11052. F11052 Curriculum-only — scatter-plot matrix
11053. F11053 Data Mining & Databases — box plot
11054. F11054 Curriculum-only — box plot and scatter plot
11055. F11055 Information Theory & Coding — broadcast channels
11056. F11056 Curriculum-only — gps signal from cell phone
11057. F11057 Information Theory & Coding — channel estimation
11058. F11058 Curriculum-only — mimo-ofdm system
11059. F11059 Information Theory & Coding — multiple paths
11060. F11060 Computer Networks — OSI model
11061. F11061 Curriculum-only — comparison with the osi reference model
11062. F11062 Information Theory & Coding — osi layer architecture
11063. F11063 Computer Networks — tcp congestion control impediment
11064. F11064 Information Theory & Coding — user datagram protocol
11065. F11065 Mathematics — binary communication system
11066. F11066 Information Theory & Coding — number of packet
11067. F11067 Mathematics — dinger equation
11068. F11068 Data Mining & Databases — mid-term quizz
11069. F11069 Mathematics — front
11070. F11070 Algorithms & Theory of CS — path extension to front
11071. F11071 Curriculum-only — front controller
11072. F11072 Information Theory & Coding — added node
11073. F11073 Mathematics — rayleigh
11074. F11074 Curriculum-only — rayleigh norden staffing curve
11075. F11075 Information Theory & Coding — power control
11076. F11076 Mathematics — schro dinger equation
11077. F11077 Curriculum-only — real-world application in secure communication
11078. F11078 Mathematics — sensitive informations
11079. F11079 Cryptography & Security — shamir secret sharing
11080. F11080 Curriculum-only — fiat shamir transform
11081. F11081 Mathematics — adi shamir
11082. F11082 Information Theory & Coding — covariance function
11083. F11083 Curriculum-only — inference and gaussian process
11084. F11084 Information Theory & Coding — linear functional
11085. F11085 Curriculum-only — linear operator and linear functional
11086. F11086 Information Theory & Coding — spectral density
11087. F11087 Computer Networks — irwin handbook of telecommunication
11088. F11088 Data Mining & Databases — telecommunication services
11089. F11089 Information Theory & Coding — telecommunication systems
11090. F11090 Mathematics — carefully
11091. F11091 ML & AI — identification tree
11092. F11092 Mathematics — spectral density function
11093. F11093 Algorithms & Theory of CS — slice rank
11094. F11094 Curriculum-only — half-open slice
11095. F11095 Data Mining & Databases — mri
11096. F11096 Mathematics — horizontal slice
11097. F11097 NLP & Speech — broadcast news
11098. F11098 Operating Systems — carefully acknowledge
11099. F11099 Other/Unknown — acoustic wave
11100. F11100 Curriculum-only — icmp echo
11101. F11101 Other/Unknown — iec
11102. F11102 Curriculum-only — iec family
11103. F11103 Other/Unknown — Interfacing and Communication
11104. F11104 Mathematics — public-key cryptosystem
11105. F11105 Curriculum-only — public-key cryptosystem and the key-exchange
11106. F11106 Other/Unknown — medical imaging
11107. F11107 Computer Networks — nuclear war
11108. F11108 Mathematics — coal
11109. F11109 Other/Unknown — energy source
11110. F11110 Computer Architecture — pxx
11111. F11111 ML & AI — reproducing kernel
11112. F11112 Other/Unknown — dual space
11113. F11113 Curriculum-only — double dual space
11114. F11114 Other/Unknown — quantum cryptography
11115. F11115 Curriculum-only — quantum and post-quantum cryptography
11116. F11116 Other/Unknown — surface acoustic waves
11117. F11117 Data Mining & Databases — operating room
11118. F11118 Other/Unknown — tcp and udp
11119. F11119 Curriculum-only — tcp and udp compared
11120. F11120 Other/Unknown — visual communication
11121. F11121 Signal/Image/Audio/Video Processing — fluctuation spectral density
11122. F11122 ML & AI — feature map
11123. F11123 Other/Unknown — linear space
11124. F11124 Signal/Image/Audio/Video Processing — ultrasound images
11125. F11125 Software Engineering — authorisation
11126. F11126 Cryptography & Security — written authorisation
11127. F11127 Curriculum-only — authorisation and capability
11128. F11128 Software Engineering — card number
11129. F11129 Mathematics — e-mail
11130. F11130 Computer Networks — e-mail spam
11131. F11131 Cryptography & Security — e-mail security
11132. F11132 Software Engineering — coverage
11133. F11133 Curriculum-only — att ck coverage map
11134. F11134 Signal/Image/Audio/Video Processing — music players
11135. F11135 Software Engineering — data store
11136. F11136 Curriculum-only — cache write synchronously to the data store
11137. F11137 Software Engineering — defensive
11138. F11138 Data Mining & Databases — kenneth
11139. F11139 ML & AI — inference on tree
11140. F11140 Mathematics — isaac
11141. F11141 Computer Architecture — isaac rosmarin
11142. F11142 Mathematics — isaac newton
11143. F11143 Other/Unknown — conservation law
11144. F11144 Mathematics — scattering
11145. F11145 Other/Unknown — brillouin scattering
11146. F11146 Computer Architecture — electron gun
11147. F11147 ML & AI — nucleus
11148. F11148 Mathematics — eventual
11149. F11149 Data Mining & Databases — household
11150. F11150 Mathematics — household income
11151. F11151 Other/Unknown — atom
11152. F11152 Cryptography & Security — side chain
11153. F11153 Mathematics — bond
11154. F11154 Cryptography & Security — bond market
11155. F11155 Mathematics — hydrogen
11156. F11156 Curriculum-only — degeneracy and cycling
11157. F11157 Mathematics — degenerate
11158. F11158 Mathematics — mirror descent
11159. F11159 ML & AI — stochastic gradient descent
11160. F11160 Curriculum-only — gradient descent and stochastic gradient descent
11161. F11161 ML & AI — backpropagation
11162. F11162 Curriculum-only — backpropagation and training deep network
11163. F11163 ML & AI — backpropagation algorithm
11164. F11164 Curriculum-only — mathematical formulation of the backpropagation algorithm
11165. F11165 ML & AI — convolutional neural
11166. F11166 Distributed Systems & Cloud — tensorflow
11167. F11167 Curriculum-only — full model in pytorch
11168. F11168 Distributed Systems & Cloud — tensorflow computational model
11169. F11169 ML & AI — output layer
11170. F11170 Information Theory & Coding — output value
11171. F11171 ML & AI — colab
11172. F11172 Curriculum-only — colab environment
11173. F11173 Distributed Systems & Cloud — notebook
11174. F11174 Data Mining & Databases — Jupyter notebooks; Google Colab; R; SPSS; Observable
11175. F11175 Distributed Systems & Cloud — databrick notebook
11176. F11176 ML & AI — perceptron algorithm
11177. F11177 Mathematics — acceleration and momentum
11178. F11178 Curriculum-only — discrete-time linear model
11179. F11179 ML & AI — parameter estimate
11180. F11180 Curriculum-only — variation in parameter estimate in regression
11181. F11181 Mathematics — objective value
11182. F11182 Curriculum-only — dual objective value imply optimality
11183. F11183 Mathematics — revised
11184. F11184 Algorithms & Theory of CS — revised version
11185. F11185 Curriculum-only — revised workflow
11186. F11186 Mathematics — abel
11187. F11187 Other/Unknown — accelerated
11188. F11188 Curriculum-only — accelerated decoding
11189. F11189 Mathematics — accelerated gradient descent
11190. F11190 Other/Unknown — adagrad
11191. F11191 Mathematics — adagrad and adam
11192. F11192 Other/Unknown — cryo-electron tomography
11193. F11193 Mathematics — genetic linkage
11194. F11194 Other/Unknown — hydrogen energy
11195. F11195 Curriculum-only — python collection stress
11196. F11196 Mathematics — residual
11197. F11197 Algorithms & Theory of CS — meas
11198. F11198 Curriculum-only — dual residual
11199. F11199 Information Theory & Coding — residual noise
11200. F11200 Mathematics — admissible
11201. F11201 ML & AI — optimal path
11202. F11202 Mathematics — nonlin meas data
11203. F11203 Other/Unknown — equation of motion
11204. F11204 Curriculum-only — grain and trivium detail
11205. F11205 Other/Unknown — grain boundary
11206. F11206 Signal/Image/Audio/Video Processing — abel summable
11207. F11207 Other/Unknown — magnetic
11208. F11208 Computer Architecture — dielectric
11209. F11209 Information Theory & Coding — magnetic storage
11210. F11210 Mathematics — insulating materials
11211. F11211 Information Theory & Coding — exponential backoff
11212. F11212 Curriculum-only — cd and binary exponential backoff
11213. F11213 Information Theory & Coding — pauli matrix
11214. F11214 Mathematics — wheel
11215. F11215 Distributed Systems & Cloud — root wheel feb
11216. F11216 Operating Systems — magnetic disk
11217. F11217 Curriculum-only — magnetic disk organisation into platter
11218. F11218 Operating Systems — Magnetic tapes
11219. F11219 Other/Unknown — spin transfer torque
11220. F11220 Signal/Image/Audio/Video Processing — angular velocity
11221. F11221 Computer Architecture — delay estimation
11222. F11222 Curriculum-only — signal processing and data analytics
11223. F11223 Data Mining & Databases — modality
11224. F11224 Algorithms & Theory of CS — sparse recovery
11225. F11225 Distributed Systems & Cloud — signal processing on database
11226. F11226 Information Theory & Coding — wireless
11227. F11227 Computer Architecture — wireless security system
11228. F11228 Computer Networks — mobile communications
11229. F11229 Curriculum-only — channel shortening for wireless equalization
11230. F11230 Distributed Systems & Cloud — ad hoc
11231. F11231 Curriculum-only — ad hoc anonymity
11232. F11232 Distributed Systems & Cloud — broadcasting
11233. F11233 Curriculum-only — arrays and broadcasting
11234. F11234 Distributed Systems & Cloud — computing and wireless
11235. F11235 Information Theory & Coding — Ad hoc networks
11236. F11236 Computer Networks — gateways
11237. F11237 Information Theory & Coding — bluetooth device
11238. F11238 Curriculum-only — wireless link on chip
11239. F11239 Information Theory & Coding — wireless mesh
11240. F11240 Algorithms & Theory of CS — max system
11241. F11241 Computer Networks — ad hoc wireless networks
11242. F11242 Information Theory & Coding — wireless channel
11243. F11243 ML & AI — low-rank matrix
11244. F11244 Algorithms & Theory of CS — relative error low-rank matrix
11245. F11245 ML & AI — low-rank matrix approximation
11246. F11246 Curriculum-only — compressive sensing and orthogonal matching pursuit
11247. F11247 ML & AI — sparsest
11248. F11248 Algorithms & Theory of CS — max-cut and sparsest-cut
11249. F11249 ML & AI — sparsest non-zero vector
11250. F11250 Mathematics — beamforming
11251. F11251 Curriculum-only — beamforming along the top singular vector
11252. F11252 Mathematics — bridge
11253. F11253 Curriculum-only — bridge to genai
11254. F11254 Mathematics — bridge of koenigsberg
11255. F11255 Computer Networks — verizon
11256. F11256 Mathematics — phased-array antenna beamforming
11257. F11257 Other/Unknown — access network
11258. F11258 Curriculum-only — access network and the core
11259. F11259 Other/Unknown — array signal processing
11260. F11260 ML & AI — kalman filter algorithms
11261. F11261 Other/Unknown — ensemble kalman filter
11262. F11262 Operating Systems — mobility pattern
11263. F11263 Other/Unknown — electron mobility
11264. F11264 Computer Networks — geo satellites
11265. F11265 Cryptography & Security — borrow
11266. F11266 Information Theory & Coding — geometric picture
11267. F11267 Mathematics — gps satellites
11268. F11268 Other/Unknown — Wireless access networks
11269. F11269 Signal/Image/Audio/Video Processing — adaptive signal processing
11270. F11270 Distributed Systems & Cloud — array processing
11271. F11271 Curriculum-only — array processing and the music algorithm
11272. F11272 Signal/Image/Audio/Video Processing — discrete-time speech signal processing
11273. F11273 Mathematics — analytic proof
11274. F11274 Other/Unknown — plancherel theorem
11275. F11275 Signal/Image/Audio/Video Processing — iir filter
11276. F11276 Curriculum-only — array multiplier
11277. F11277 Distributed Systems & Cloud — software radio
11278. F11278 Other/Unknown — multichannel
11279. F11279 Algorithms & Theory of CS — lens
11280. F11280 Computer Networks — optical links
11281. F11281 Data Mining & Databases — optical surfaces
11282. F11282 ML & AI — Optical character recognition
11283. F11283 Mathematics — optical transmissions
11284. F11284 NLP & Speech — orthographic
11285. F11285 Data Mining & Databases — orthographic projection
11286. F11286 Other/Unknown — holographic optical elements
11287. F11287 Other/Unknown — optical sensors
11288. F11288 Algorithms & Theory of CS — parallel scan
11289. F11289 Cryptography & Security — port scanning
11290. F11290 Curriculum-only — detection of planarity
11291. F11291 Distributed Systems & Cloud — snir
11292. F11292 Algorithms & Theory of CS — snir stoc
11293. F11293 Distributed Systems & Cloud — marc snir
11294. F11294 Mathematics — focusing
11295. F11295 NLP & Speech — semiring
11296. F11296 Other/Unknown — module focusing
11297. F11297 Computer Architecture — parallel plates
11298. F11298 Mathematics — shaft
11299. F11299 Other/Unknown — plate and shell
11300. F11300 Signal/Image/Audio/Video Processing — defocusing
11301. F11301 Distributed Systems & Cloud — demo
11302. F11302 Cryptography & Security — salt
11303. F11303 Computer Architecture — salt water
11304. F11304 Curriculum-only — demo and exam preparation
11305. F11305 Information Theory & Coding — pyaudio channel demo
11306. F11306 Operating Systems — improve performance
11307. F11307 Distributed Systems & Cloud — order to improve performance
11308. F11308 Operating Systems — improving performance
11309. F11309 Signal/Image/Audio/Video Processing — focusing with feedback control
11310. F11310 Computer Networks — digital radio
11311. F11311 Information Theory & Coding — quadrature amplitude modulation
11312. F11312 Signal/Image/Audio/Video Processing — cyclostationarity
11313. F11313 Mathematics — time frequency response
11314. F11314 Signal/Image/Audio/Video Processing — discrete-time frequency
11315. F11315 Algorithms & Theory of CS — voxel-based exploration game
11316. F11316 Mathematics — beam
11317. F11317 Algorithms & Theory of CS — beam widths
11318. F11318 ML & AI — beam search
11319. F11319 Curriculum-only — beam search are deterministic
11320. F11320 Mathematics — beam pattern
11321. F11321 Other/Unknown — beam-shaping
11322. F11322 Curriculum-only — potential theory and bending of beam
11323. F11323 Other/Unknown — domain analysis
11324. F11324 Signal/Image/Audio/Video Processing — frequency domain
11325. F11325 Computer Architecture — decimator
11326. F11326 Curriculum-only — aliasing and synonym
11327. F11327 Other/Unknown — suppression
11328. F11328 Curriculum-only — k-anonymity by generalisation and suppression
11329. F11329 Signal/Image/Audio/Video Processing — birefringent
11330. F11330 Signal/Image/Audio/Video Processing — sampling period
11331. F11331 Mathematics — stieltje integral
11332. F11332 Signal/Image/Audio/Video Processing — bank
11333. F11333 Algorithms & Theory of CS — actual cost
11334. F11334 Computer Architecture — bufferedreader
11335. F11335 Computer Networks — remittance
11336. F11336 Cryptography & Security — accenture
11337. F11337 Curriculum-only — bank group
11338. F11338 Mathematics — bank account
11339. F11339 Computer Networks — bank account number
11340. F11340 Mathematics — bank account model
11341. F11341 Curriculum-only — product decision and experimentation
11342. F11342 Mathematics — feminist
11343. F11343 Curriculum-only — inductive learning based on symbolic
11344. F11344 ML & AI — neuro-symbolic reasoning
11345. F11345 Mathematics — symbolic algebra
11346. F11346 NLP & Speech — wall street journal
11347. F11347 Cryptography & Security — trade
11348. F11348 Curriculum-only — trade between header length
11349. F11349 Data Mining & Databases — trade-off
11350. F11350 Curriculum-only — cap trade-off
11351. F11351 ML & AI — bias variance trade-off
11352. F11352 Curriculum-only — regularisation and the bias variance trade-off
11353. F11353 Operating Systems — bank conflict
11354. F11354 Curriculum-only — interleaved addressing with bank conflict
11355. F11355 Operating Systems — bank file
11356. F11356 Other/Unknown — protein data bank
11357. F11357 Signal/Image/Audio/Video Processing — inverse symbolic calculator
11358. F11358 Mathematics — lifting
11359. F11359 Other/Unknown — wavelet packet
11360. F11360 Signal/Image/Audio/Video Processing — analysis and wavelet
11361. F11361 Signal/Image/Audio/Video Processing — wavelet decomposition
11362. F11362 Software Engineering — alias
11363. F11363 Curriculum-only — slice can alias
11364. F11364 Mathematics — cancellation
11365. F11365 Curriculum-only — cancellation and deadline passed
11366. F11366 Information Theory & Coding — interference cancellation
11367. F11367 Signal/Image/Audio/Video Processing — alias cancellation
11368. F11368 Mathematics — avoid
11369. F11369 Curriculum-only — avoid expensive join
11370. F11370 Distributed Systems & Cloud — deadlock avoidance
11371. F11371 Curriculum-only — weak fiat shamir pitfall
11372. F11372 Distributed Systems & Cloud — presentation
11373. F11373 Algorithms & Theory of CS — paper and presentation
11374. F11374 Computer Architecture — design presentation
11375. F11375 Cryptography & Security — paper presentation
11376. F11376 Curriculum-only — presentation attack
11377. F11377 Data Mining & Databases — polycyclic
11378. F11378 Distributed Systems & Cloud — presenting
11379. F11379 Information Theory & Coding — avoid measurability
11380. F11380 Curriculum-only — oral message om
11381. F11381 Data Mining & Databases — oral surgery
11382. F11382 Information Theory & Coding — oral presentation
11383. F11383 Curriculum-only — round and sticky
11384. F11384 Mathematics — caveat
11385. F11385 Curriculum-only — caveat in production
11386. F11386 Mathematics — checklist
11387. F11387 Curriculum-only — checklist file
11388. F11388 Mathematics — exercised
11389. F11389 ML & AI — yinia2
11390. F11390 Mathematics — hat
11391. F11391 Curriculum-only — r-hat
11392. F11392 Mathematics — preliminary
11393. F11393 Curriculum-only — high-level or preliminary design
11394. F11394 Distributed Systems & Cloud — preliminary work
11395. F11395 Mathematics — tin
11396. F11396 Algorithms & Theory of CS — block operation
11397. F11397 Algorithms & Theory of CS — random graph
11398. F11398 Algorithms & Theory of CS — regular partition
11399. F11399 Algorithms & Theory of CS — uniformly random
11400. F11400 Computer Networks — spectral gap
11401. F11401 Cryptography & Security — one-way permutation
11402. F11402 Curriculum-only — bipartite and regular graph
11403. F11403 Data Mining & Databases — clustering on random graph
11404. F11404 ML & AI — exact recovery
11405. F11405 Data Mining & Databases — community
11406. F11406 Computer Networks — community edition
11407. F11407 Cryptography & Security — community currency
11408. F11408 Curriculum-only — community benchmark with similar role
11409. F11409 Data Mining & Databases — community detection
11410. F11410 Computer Networks — spectral graph theory
11411. F11411 Data Mining & Databases — database community
11412. F11412 Distributed Systems & Cloud — membership
11413. F11413 Algorithms & Theory of CS — oracle
11414. F11414 Curriculum-only — cassandra membership
11415. F11415 Distributed Systems & Cloud — group membership
11416. F11416 Curriculum-only — group membership and view change
11417. F11417 Distributed Systems & Cloud — membership change
11418. F11418 Information Theory & Coding — network communities
11419. F11419 ML & AI — expander code
11420. F11420 Mathematics — central role
11421. F11421 Algorithms & Theory of CS — sumset
11422. F11422 Mathematics — incidence
11423. F11423 Algorithms & Theory of CS — Angle of incidence
11424. F11424 Curriculum-only — incidence response
11425. F11425 Mathematics — increment
11426. F11426 Computer Architecture — fs1
11427. F11427 Curriculum-only — auto-increment as pre
11428. F11428 Distributed Systems & Cloud — invalidate
11429. F11429 Mathematics — epsilon
11430. F11430 Algorithms & Theory of CS — removal
11431. F11431 Curriculum-only — fewest vertex whose removal
11432. F11432 Mathematics — dense
11433. F11433 Algorithms & Theory of CS — sparse graph
11434. F11434 Curriculum-only — dense kernel
11435. F11435 Distributed Systems & Cloud — dense and sparse
11436. F11436 Curriculum-only — dense and sparse index
11437. F11437 Distributed Systems & Cloud — dense matrix
11438. F11438 ML & AI — keras
11439. F11439 Mathematics — dense subset
11440. F11440 Mathematics — number of independent
11441. F11441 Curriculum-only — doubly stochastic matrix and permutation matrix
11442. F11442 Mathematics — poisson arrival process
11443. F11443 Distributed Systems & Cloud — blue-steel ray tracer
11444. F11444 Mathematics — shrinking
11445. F11445 Curriculum-only — downgrade while shrinking
11446. F11446 Data Mining & Databases — shrinking phase
11447. F11447 Mathematics — solving ax
11448. F11448 Algorithms & Theory of CS — ap-free subset
11449. F11449 Mathematics — textbook
11450. F11450 Algorithms & Theory of CS — attiya and welch
11451. F11451 Curriculum-only — textbook attack
11452. F11452 Distributed Systems & Cloud — clock synchronization
11453. F11453 Curriculum-only — global state and termination detection
11454. F11454 Distributed Systems & Cloud — global state snapshot
11455. F11455 Mathematics — mathematical function
11456. F11456 Curriculum-only — benefit of the recommended policy with an interval
11457. F11457 Mathematics — matlab recommended
11458. F11458 Operating Systems — dp presentation
11459. F11459 Other/Unknown — analysis of variance
11460. F11460 Curriculum-only — trapdoor permutation and the rsa assumption
11461. F11461 Signal/Image/Audio/Video Processing — circulant
11462. F11462 Data Mining & Databases — circulant permutation matrix
11463. F11463 Signal/Image/Audio/Video Processing — condition for alias cancellation
11464. F11464 Software Engineering — avoid semantic model
11465. F11465 Curriculum-only — compiler technique for enhancing ilp
11466. F11466 Distributed Systems & Cloud — automatic parallelization
11467. F11467 Curriculum-only — data flow between store
11468. F11468 Distributed Systems & Cloud — data flow processing library
11469. F11469 Curriculum-only — cost model of vectorisation
11470. F11470 Mathematics — par
11471. F11471 Other/Unknown — statistical physics
11472. F11472 Information Theory & Coding — maximum entropy
11473. F11473 Curriculum-only — occupancy and the resource that limit
11474. F11474 Information Theory & Coding — queue occupancy distribution
11475. F11475 Mathematics — total energy
11476. F11476 Information Theory & Coding — system and environment
11477. F11477 NLP & Speech — maximum entropy model
11478. F11478 Mathematics — adult
11479. F11479 Data Mining & Databases — adult son
11480. F11480 NLP & Speech — syllable
11481. F11481 Information Theory & Coding — time of onset
11482. F11482 NLP & Speech — utterance
11483. F11483 Operating Systems — bus occupancy
11484. F11484 Other/Unknown — statistical mechanics
11485. F11485 Data Mining & Databases — einstein
11486. F11486 Mathematics — mc2
11487. F11487 Other/Unknown — tensor
11488. F11488 Curriculum-only — per-tensor
11489. F11489 Distributed Systems & Cloud — tensor processing
11490. F11490 Curriculum-only — systolic arrays as in tensor-processing
11491. F11491 ML & AI — convolutional layer
11492. F11492 Curriculum-only — cp tensor decomposition
11493. F11493 ML & AI — algorithm for tensor decomposition
11494. F11494 Mathematics — eigendecomposition of covariance matrix
11495. F11495 Signal/Image/Audio/Video Processing — tongue
11496. F11496 Software Engineering — architecture and vectorization
11497. F11497 Mathematics — k-4
11498. F11498 Software Engineering — calling convention
11499. F11499 Other/Unknown — flow analysis
11500. F11500 Software Engineering — data-flow optimization
11501. F11501 Distributed Systems & Cloud — omp
11502. F11502 Software Engineering — duality and degeneracy
11503. F11503 Software Engineering — intentional
11504. F11504 Mathematics — trajectory
11505. F11505 Algorithms & Theory of CS — billiard trajectory
11506. F11506 Curriculum-only — asymptotic pseudo-trajectory
11507. F11507 ML & AI — set of variable
11508. F11508 Mathematics — evolve
11509. F11509 Signal/Image/Audio/Video Processing — phase factor
11510. F11510 Software Engineering — abnormal
11511. F11511 Mathematics — harris
11512. F11512 Software Engineering — lam
11513. F11513 Curriculum-only — multiple-condition and path coverage
11514. F11514 Software Engineering — philip
11515. F11515 Curriculum-only — matrix factorisation for recommendation
11516. F11516 Data Mining & Databases — netflix
11517. F11517 Curriculum-only — data completion and the netflix
11518. F11518 Data Mining & Databases — recommendation system
11519. F11519 Curriculum-only — recommendation system like amazon
11520. F11520 Data Mining & Databases — collaborative filtering
11521. F11521 Curriculum-only — alternating-least-square algorithm for collaborative filtering
11522. F11522 Distributed Systems & Cloud — distributed recommendation
11523. F11523 ML & AI — learning bayesian network
11524. F11524 Algorithms & Theory of CS — set theoretic
11525. F11525 ML & AI — probabilistic inference ii
11526. F11526 Mathematics — worth
11527. F11527 Curriculum-only — generic is worth
11528. F11528 Data Mining & Databases — recommendation worth
11529. F11529 ML & AI — semantic distance
11530. F11530 Computer Networks — pma
11531. F11531 ML & AI — a0bf4ptzocwi1k6pude
11532. F11532 Curriculum-only — autoencoder and representation learning
11533. F11533 ML & AI — contrastive learning
11534. F11534 Algorithms & Theory of CS — tikhonov
11535. F11535 Curriculum-only — hypothesis space and inductive bias
11536. F11536 ML & AI — j2vtaimno6wyv
11537. F11537 Curriculum-only — latent-factor
11538. F11538 ML & AI — latent semantic indexing
11539. F11539 Distributed Systems & Cloud — network time protocol
11540. F11540 ML & AI — one-hot encoding
11541. F11541 Curriculum-only — optimizer taught
11542. F11542 Data Mining & Databases — query optimizer
11543. F11543 ML & AI — phillip isola
11544. F11544 Curriculum-only — complete pooling
11545. F11545 ML & AI — pooling layer
11546. F11546 Curriculum-only — pretraining compute budget
11547. F11547 ML & AI — qlepcji1v
11548. F11548 Curriculum-only — exist to trc
11549. F11549 ML & AI — vae
11550. F11550 Curriculum-only — vae and gan compared
11551. F11551 ML & AI — conditional vae
11552. F11552 Curriculum-only — hierarchical and conditional vae
11553. F11553 ML & AI — version space
11554. F11554 Mathematics — annuity
11555. F11555 Curriculum-only — assemble part the learner built
11556. F11556 ML & AI — weak learner
11557. F11557 Mathematics — learner and educator
11558. F11558 ML & AI — emd
11559. F11559 Mathematics — sharing knowledge with learner
11560. F11560 Other/Unknown — resource pooling
11561. F11561 Curriculum-only — modern transformer zoo
11562. F11562 ML & AI — bag of word
11563. F11563 Curriculum-only — self-supervised learning and the llm landscape
11564. F11564 ML & AI — sequence labeling
11565. F11565 NLP & Speech — contextual
11566. F11566 Curriculum-only — contextual integrity
11567. F11567 ML & AI — contextual embedding
11568. F11568 Curriculum-only — positional-interpolation trick for long context
11569. F11569 ML & AI — qh69lbbbu0leuw8flx4r2g9oq9lsn
11570. F11570 NLP & Speech — ideal transformer
11571. F11571 Signal/Image/Audio/Video Processing — generative adversarial network
11572. F11572 ML & AI — image classification
11573. F11573 NLP & Speech — hidden markov modeling
11574. F11574 Data Mining & Databases — segment-based
11575. F11575 ML & AI — graphical model
11576. F11576 Algorithms & Theory of CS — grid graph
11577. F11577 Data Mining & Databases — information form
11578. F11578 ML & AI — graph structure
11579. F11579 ML & AI — markov chain monte carlo
11580. F11580 Curriculum-only — metropolis and metropolis hasting algorithm
11581. F11581 ML & AI — max-product algorithm
11582. F11582 Mathematics — factorized
11583. F11583 NLP & Speech — bilme
11584. F11584 Mathematics — segment
11585. F11585 Algorithms & Theory of CS — balanced binary search tree
11586. F11586 Computer Networks — network segment
11587. F11587 Cryptography & Security — market segment
11588. F11588 Curriculum-only — arp discovery on the local segment
11589. F11589 Mathematics — koch snowflake
11590. F11590 NLP & Speech — phonetic transcription
11591. F11591 Operating Systems — base address
11592. F11592 Other/Unknown — convolutional neural network
11593. F11593 Curriculum-only — convolutional neural network and image
11594. F11594 ML & AI — imagenet
11595. F11595 Other/Unknown — hyperspectral image classification
11596. F11596 Signal/Image/Audio/Video Processing — background subtraction
11597. F11597 Curriculum-only — cnn-based object detection model
11598. F11598 Signal/Image/Audio/Video Processing — speech segments
11599. F11599 Software Engineering — contextual bandit
11600. F11600 Curriculum-only — contextual bandit algorithm
11601. F11601 Software Engineering — control register
11602. F11602 Curriculum-only — fake and injected dependency
11603. F11603 Data Mining & Databases — bias and fake-new
11604. F11604 Software Engineering — krn
11605. F11605 Curriculum-only — loc and iloc
11606. F11606 Software Engineering — run time
11607. F11607 Curriculum-only — carry-save addition
11608. F11608 Data Mining & Databases — salary
11609. F11609 Mathematics — ll save
11610. F11610 Curriculum-only — semi-weak keys
11611. F11611 Data Mining & Databases — semi-structured data
11612. F11612 Algorithms & Theory of CS — first-order logic
11613. F11613 Curriculum-only — first-order logic for the relational model
11614. F11614 Distributed Systems & Cloud — semi-honest
11615. F11615 ML & AI — high-dimensional data
11616. F11616 Curriculum-only — compress high-dimensional data
11617. F11617 ML & AI — positive semi-definite
11618. F11618 Computer Networks — positive semi-definite matrix
11619. F11619 Curriculum-only — covariance are positive semi-definite matrix
11620. F11620 ML & AI — semi-bandit
11621. F11621 Mathematics — axiom of choice
11622. F11622 Algorithms & Theory of CS — bipartite matching
11623. F11623 Curriculum-only — cardinality ratio
11624. F11624 ML & AI — shatter
11625. F11625 Mathematics — bijective
11626. F11626 Algorithms & Theory of CS — direct bijective proof
11627. F11627 Mathematics — cardinality constraint
11628. F11628 Curriculum-only — cardinality of finite set and counting
11629. F11629 Mathematics — convex-cardinality
11630. F11630 NLP & Speech — word sense disambiguation
11631. F11631 Operating Systems — mcs
11632. F11632 Distributed Systems & Cloud — elapsed time
11633. F11633 Cryptography & Security — proof of elapsed time
11634. F11634 Operating Systems — save energy
11635. F11635 Signal/Image/Audio/Video Processing — cpl
11636. F11636 Operating Systems — privilege level
11637. F11637 Curriculum-only — privilege level and protection ring
11638. F11638 Operating Systems — trap
11639. F11639 Cryptography & Security — trap-door permutation
11640. F11640 Curriculum-only — chasm trap
11641. F11641 Distributed Systems & Cloud — kernel stack
11642. F11642 Operating Systems — syscall
11643. F11643 Signal/Image/Audio/Video Processing — cpl function
11644. F11644 Data Mining & Databases — ello
11645. F11645 Mathematics — congruence subgroup
11646. F11646 Data Mining & Databases — cusp form
11647. F11647 Software Engineering — breakpoint
11648. F11648 Data Mining & Databases — compound-procedure
11649. F11649 Software Engineering — epilogue
11650. F11650 Distributed Systems & Cloud — attach
11651. F11651 Software Engineering — asm
11652. F11652 Distributed Systems & Cloud — asm code for sorting
11653. F11653 Software Engineering — debugging with gdb
11654. F11654 Curriculum-only — knowledge graph of defensive countermeasure
11655. F11655 Other/Unknown — expert system
11656. F11656 ML & AI — rule-based expert system
11657. F11657 Software Engineering — number of month
11658. F11658 Data Mining & Databases — constructor and selector
11659. F11659 Operating Systems — segment selector
11660. F11660 Software Engineering — semi-definite programming
11661. F11661 Curriculum-only — semi-detached and embedded
11662. F11662 Software Engineering — seminar
11663. F11663 Mathematics — opportunity
11664. F11664 Distributed Systems & Cloud — dependence analysis
11665. F11665 Distributed Systems & Cloud — spawn fib
11666. F11666 Information Theory & Coding — opportunity to apply
11667. F11667 ML & AI — data space
11668. F11668 Distributed Systems & Cloud — wang junqing
11669. F11669 Mathematics — fibonacci number
11670. F11670 Curriculum-only — professional library
11671. F11671 Mathematics — reader
11672. F11672 Computer Networks — rfid readers
11673. F11673 Mathematics — bully
11674. F11674 Curriculum-only — bully algorithm
11675. F11675 Mathematics — skill
11676. F11676 Curriculum-only — forecast-skill metrics
11677. F11677 Data Mining & Databases — invent
11678. F11678 Mathematics — writing skill
11679. F11679 NLP & Speech — configuration of serial cable
11680. F11680 Operating Systems — serial schedule
11681. F11681 Other/Unknown — opportunity cost
11682. F11682 Software Engineering — cilk sync
11683. F11683 Distributed Systems & Cloud — parallel execution
11684. F11684 Curriculum-only — user id and metadata
11685. F11685 Distributed Systems & Cloud — streamit parallelizing compiler
11686. F11686 Mathematics — ceiling
11687. F11687 Information Theory & Coding — priority ceiling protocol
11688. F11688 Software Engineering — reducer hyperobject
11689. F11689 Distributed Systems & Cloud — transactional
11690. F11690 Curriculum-only — fault tolerance and self-stabilization
11691. F11691 Distributed Systems & Cloud — transactional cilk
11692. F11692 Information Theory & Coding — maurice
11693. F11693 Distributed Systems & Cloud — maurice herlihy
11694. F11694 Mathematics — propose
11695. F11695 Software Engineering — ben
11696. F11696 Computer Architecture — proposal conference with tas
11697. F11697 Distributed Systems & Cloud — subject proposal
11698. F11698 ML & AI — proposal distribution
11699. F11699 Operating Systems — design proposal
11700. F11700 Software Engineering — sliced
11701. F11701 Curriculum-only — struct embed
11702. F11702 Data Mining & Databases — stat
11703. F11703 Distributed Systems & Cloud — multidimensional arrays
11704. F11704 Operating Systems — ilock
11705. F11705 Distributed Systems & Cloud — ref
11706. F11706 Operating Systems — le descriptor
11707. F11707 Distributed Systems & Cloud — fork
11708. F11708 Cryptography & Security — hard fork
11709. F11709 Curriculum-only — longest-chain rule and fork
11710. F11710 Distributed Systems & Cloud — unix fork model
11711. F11711 Operating Systems — struct buf
11712. F11712 Curriculum-only — user-space tcp
11713. F11713 Software Engineering — child process
11714. F11714 Curriculum-only — delayed duplicate
11715. F11715 Distributed Systems & Cloud — split duplicate
11716. F11716 Mathematics — commutativity
11717. F11717 Curriculum-only — join commutativity
11718. F11718 Data Mining & Databases — commutative diagram
11719. F11719 Mathematics — exact sequence
11720. F11720 Other/Unknown — homology
11721. F11721 Mathematics — homology group
11722. F11722 Software Engineering — enum
11723. F11723 Curriculum-only — requeststatus as an enum
11724. F11724 Software Engineering — guarded
11725. F11725 NLP & Speech — pilot
11726. F11726 Curriculum-only — channel estimation from pilot subcarrier
11727. F11727 Other/Unknown — dynamic analysis
11728. F11728 Cryptography & Security — integrity of information
11729. F11729 Computer Architecture — gateway
11730. F11730 Computer Networks — smart card
11731. F11731 Cryptography & Security — bitcoin scripting
11732. F11732 Cryptography & Security — distributed ledger
11733. F11733 Curriculum-only — dynamic analysis methodology
11734. F11734 Distributed Systems & Cloud — smart pointer ch
11735. F11735 Curriculum-only — relation to state-machine replication
11736. F11736 ML & AI — headless
11737. F11737 Mathematics — assessing
11738. F11738 Curriculum-only — assessing their performance
11739. F11739 Data Mining & Databases — assessing prediction performance
11740. F11740 Mathematics — monetary
11741. F11741 Cryptography & Security — monetary theory
11742. F11742 Mathematics — reserve
11743. F11743 Cryptography & Security — liquidity
11744. F11744 Other/Unknown — commercial
11745. F11745 Cryptography & Security — digital currency
11746. F11746 Curriculum-only — commercial system oracle
11747. F11747 Information Theory & Coding — nsfnet
11748. F11748 Mathematics — deposit
11749. F11749 Computer Networks — account balance
11750. F11750 Cryptography & Security — bank deposit
11751. F11751 Mathematics — mint
11752. F11752 Curriculum-only — design mint
11753. F11753 NLP & Speech — system initiative
11754. F11754 Operating Systems — decentralized digital currency
11755. F11755 Other/Unknown — commercial building
11756. F11756 Signal/Image/Audio/Video Processing — prototype filter
11757. F11757 Software Engineering — assessing risk
11758. F11758 Curriculum-only — identifying and assessing risk
11759. F11759 Software Engineering — function prototype
11760. F11760 Mathematics — tracing
11761. F11761 Curriculum-only — distributed tracing
11762. F11762 Distributed Systems & Cloud — ray tracing
11763. F11763 Other/Unknown — Image-based rendering
11764. F11764 Signal/Image/Audio/Video Processing — p2 a3
11765. F11765 Software Engineering — task parallelism
11766. F11766 Cryptography & Security — token system
11767. F11767 Curriculum-only — access token as signed
11768. F11768 Distributed Systems & Cloud — token-based
11769. F11769 Curriculum-only — token-based algorithm
11770. F11770 Information Theory & Coding — code vector
11771. F11771 Curriculum-only — k-state token ring
11772. F11772 ML & AI — ach
11773. F11773 Curriculum-only — byte-pair encoding and subword tokenization
11774. F11774 ML & AI — dl33hd9ttav8vglyc
11775. F11775 Curriculum-only — patch and delete with their idempotent
11776. F11776 ML & AI — guineafowl
11777. F11777 Curriculum-only — relative positional encoding
11778. F11778 ML & AI — qjembj1ogcb
11779. F11779 Algorithms & Theory of CS — pre-processing
11780. F11780 Curriculum-only — search tokenise the query
11781. F11781 ML & AI — tokenizer
11782. F11782 Mathematics — a1 and a2
11783. F11783 Algorithms & Theory of CS — number of item
11784. F11784 Curriculum-only — attention alone
11785. F11785 Curriculum-only — hands-on unet and attention unet
11786. F11786 ML & AI — attention layer
11787. F11787 Curriculum-only — softmax and the attention matrix
11788. F11788 ML & AI — attention mechanism
11789. F11789 Curriculum-only — attention mechanism vectorized
11790. F11790 ML & AI — attention network
11791. F11791 Curriculum-only — text-to-image conditioning with cross-attention
11792. F11792 ML & AI — dwp
11793. F11793 Curriculum-only — masked or tail handling
11794. F11794 ML & AI — multi-head attention
11795. F11795 Curriculum-only — masked multi-head self-attention
11796. F11796 ML & AI — masked self-attention
11797. F11797 Curriculum-only — masked self-attention and masked multi-head self-attention
11798. F11798 ML & AI — stand-alone embedding
11799. F11799 Mathematics — scanner
11800. F11800 Curriculum-only — openscap as the open-source scanner
11801. F11801 Mathematics — vanilla
11802. F11802 ML & AI — neuronize
11803. F11803 Other/Unknown — Attention Models
11804. F11804 Curriculum-only — limitation of pre-attention model
11805. F11805 Other/Unknown — data pre-processing
11806. F11806 Data Mining & Databases — japan
11807. F11807 Distributed Systems & Cloud — international conference
11808. F11808 Information Theory & Coding — berlin
11809. F11809 Computer Networks — bryan
11810. F11810 Data Mining & Databases — crowd-sourcing
11811. F11811 Distributed Systems & Cloud — collective
11812. F11812 Cryptography & Security — collective action
11813. F11813 Curriculum-only — collective ownership
11814. F11814 Distributed Systems & Cloud — collective operations
11815. F11815 Information Theory & Coding — international standard serial number
11816. F11816 Mathematics — yang
11817. F11817 Curriculum-only — netconf and yang
11818. F11818 Operating Systems — th annual international
11819. F11819 Other/Unknown — international business
11820. F11820 Distributed Systems & Cloud — courtesy of international business
11821. F11821 Other/Unknown — international telecommunications
11822. F11822 Computer Networks — institution
11823. F11823 Other/Unknown — financial institution
11824. F11824 Distributed Systems & Cloud — management
11825. F11825 Algorithms & Theory of CS — spatial data
11826. F11826 Computer Networks — change control
11827. F11827 Cryptography & Security — data base
11828. F11828 Curriculum-only — api management
11829. F11829 Curriculum-only — release management
11830. F11830 Data Mining & Databases — airline revenue management
11831. F11831 Curriculum-only — cover oltp environment
11832. F11832 Data Mining & Databases — data warehouse
11833. F11833 Distributed Systems & Cloud — agreement
11834. F11834 Curriculum-only — agreement and consensus
11835. F11835 Distributed Systems & Cloud — agreement protocol
11836. F11836 Curriculum-only — checkpointing and exactly-once
11837. F11837 Distributed Systems & Cloud — consensus agreement
11838. F11838 Curriculum-only — iam member
11839. F11839 Distributed Systems & Cloud — managed
11840. F11840 Curriculum-only — cloud bigtable as the managed product
11841. F11841 Curriculum-only — accelerator behind managed training
11842. F11842 Distributed Systems & Cloud — managed compute
11843. F11843 Curriculum-only — reverse engineering and re-engineering
11844. F11844 Distributed Systems & Cloud — resiliency
11845. F11845 Curriculum-only — cluster resource management
11846. F11846 Distributed Systems & Cloud — resource management in cloud
11847. F11847 Curriculum-only — checkpointing rollback recovery
11848. F11848 Distributed Systems & Cloud — rollback recovery scheme
11849. F11849 Information Theory & Coding — health care management
11850. F11850 ML & AI — develop principled
11851. F11851 Mathematics — areas
11852. F11852 Computer Networks — metro areas
11853. F11853 Curriculum-only — areas and hierarchy
11854. F11854 Mathematics — asset management
11855. F11855 Curriculum-only — customer brand switching
11856. F11856 Mathematics — elliptical orbit
11857. F11857 Data Mining & Databases — european roulette
11858. F11858 ML & AI — european parliament
11859. F11859 Mathematics — real life
11860. F11860 Cryptography & Security — token sale
11861. F11861 Curriculum-only — sale log in the object store
11862. F11862 Data Mining & Databases — amt
11863. F11863 Mathematics — quota
11864. F11864 Curriculum-only — system optimization for graph neural network
11865. F11865 Mathematics — trapezoidal and simpson
11866. F11866 NLP & Speech — dialogue management
11867. F11867 Curriculum-only — kappa architecture
11868. F11868 Operating Systems — in-network resource management
11869. F11869 Other/Unknown — acid
11870. F11870 Curriculum-only — collection of table with the acid
11871. F11871 Mathematics — growing
11872. F11872 Computer Networks — growing network
11873. F11873 Curriculum-only — growing and shrinking phase
11874. F11874 Other/Unknown — amino acid
11875. F11875 Mathematics — essential
11876. F11876 Curriculum-only — essential difficulty of brook
11877. F11877 Data Mining & Databases — essential coding theory
11878. F11878 Mathematics — gln
11879. F11879 Other/Unknown — broad areas
11880. F11880 Algorithms & Theory of CS — no-cloning
11881. F11881 Curriculum-only — avoid file-based caching because it hamper cloning
11882. F11882 Other/Unknown — consumer
11883. F11883 Curriculum-only — consumer group with partition
11884. F11884 NLP & Speech — tts
11885. F11885 Operating Systems — rhead
11886. F11886 Other/Unknown — Consumer products
11887. F11887 Cryptography & Security — banking finance
11888. F11888 Curriculum-only — control and finance
11889. F11889 Data Mining & Databases — dispute
11890. F11890 Distributed Systems & Cloud — trend
11891. F11891 Algorithms & Theory of CS — trend in theoretical
11892. F11892 Curriculum-only — bootstrapping cost trend
11893. F11893 Data Mining & Databases — trend in mining text
11894. F11894 Distributed Systems & Cloud — trend in cloud computing
11895. F11895 ML & AI — foundation and trend
11896. F11896 Mathematics — clearing
11897. F11897 Cryptography & Security — common domain model
11898. F11898 Mathematics — labour
11899. F11899 Other/Unknown — emerging trend
11900. F11900 Computer Architecture — power harvesting
11901. F11901 Other/Unknown — energy harvesting
11902. F11902 Computer Architecture — energy scavenging
11903. F11903 Other/Unknown — intelligent transportation
11904. F11904 Curriculum-only — resource and inventory management
11905. F11905 Other/Unknown — management system
11906. F11906 Computer Networks — warehouse management system
11907. F11907 Data Mining & Databases — data base management system
11908. F11908 Other/Unknown — marketing management
11909. F11909 Computer Networks — Network monitoring
11910. F11910 Curriculum-only — monitoring at host
11911. F11911 Distributed Systems & Cloud — management and monitoring
11912. F11912 Other/Unknown — condition monitoring
11913. F11913 Computer Networks — civil and environmental
11914. F11914 NLP & Speech — Pervasive computing: Information processing that has been integrated into everyday objects and activities, such as smart energy systems, social networking, and feedback systems to promote sustainable behavior, transportation, environmental monitoring, citizen science and activism
11915. F11915 Other/Unknown — environmental impact
11916. F11916 Cryptography & Security — risk exposure
11917. F11917 Curriculum-only — cache-timing exposure
11918. F11918 Other/Unknown — life cycle
11919. F11919 Curriculum-only — dominate the life-cycle cost
11920. F11920 Other/Unknown — life cycle analysis
11921. F11921 Computer Networks — network service
11922. F11922 Curriculum-only — fcap network-management model
11923. F11923 Distributed Systems & Cloud — network virtualisation
11924. F11924 Curriculum-only — google andromeda network virtualisation
11925. F11925 Distributed Systems & Cloud — virtual node
11926. F11926 Curriculum-only — consistent hashing and its virtual node
11927. F11927 Other/Unknown — nucleic acid
11928. F11928 Mathematics — selected
11929. F11929 Curriculum-only — selected hqc
11930. F11930 Data Mining & Databases — vast
11931. F11931 Distributed Systems & Cloud — vast amount of data
11932. F11932 Information Theory & Coding — unknown outcome
11933. F11933 Mathematics — diamond
11934. F11934 Curriculum-only — diamond model
11935. F11935 Mathematics — element selected
11936. F11936 Other/Unknown — laboratory experiment
11937. F11937 Mathematics — super
11938. F11938 Algorithms & Theory of CS — super mario brother
11939. F11939 Curriculum-only — super computer
11940. F11940 Data Mining & Databases — super halting
11941. F11941 ML & AI — super-resolution
11942. F11942 Mathematics — sub and super
11943. F11943 Other/Unknown — combined cycle power plants
11944. F11944 Curriculum-only — flexibility and design effort
11945. F11945 Other/Unknown — recurrent neural network
11946. F11946 Curriculum-only — recurrent neural network implementation in python
11947. F11947 ML & AI — feed-forward
11948. F11948 Distributed Systems & Cloud — scale
11949. F11949 Computer Networks — logarithmic scale
11950. F11950 Curriculum-only — clustering at scale
11951. F11951 Curriculum-only — scale the design
11952. F11952 Data Mining & Databases — gray-scale images
11953. F11953 Distributed Systems & Cloud — extreme-scale
11954. F11954 Curriculum-only — maturity model and their level scale
11955. F11955 Distributed Systems & Cloud — scale data
11956. F11956 Information Theory & Coding — absolute temperature
11957. F11957 Mathematics — changing scale
11958. F11958 Curriculum-only — derivative and dilation
11959. F11959 Mathematics — horizontal axis
11960. F11960 Data Mining & Databases — number of data
11961. F11961 Information Theory & Coding — dash
11962. F11962 Mathematics — reflectionless
11963. F11963 Other/Unknown — key component
11964. F11964 Distributed Systems & Cloud — challenge
11965. F11965 Cryptography & Security — challenge-response
11966. F11966 Curriculum-only — bitcoin and crypto-currency
11967. F11967 Data Mining & Databases — key challenge
11968. F11968 Distributed Systems & Cloud — programming challenge in cluster
11969. F11969 Information Theory & Coding — challenge lie
11970. F11970 Mathematics — investor
11971. F11971 Cryptography & Security — investor protection
11972. F11972 NLP & Speech — challenge in machine translation
11973. F11973 Other/Unknown — accounting
11974. F11974 Curriculum-only — accounting and potential
11975. F11975 Other/Unknown — recurrent network
11976. F11976 Curriculum-only — scale out on commodity machine
11977. F11977 Other/Unknown — security challenge
11978. F11978 Curriculum-only — map of the two security-management
11979. F11979 Other/Unknown — sequence-to-sequence
11980. F11980 Curriculum-only — sequence-to-sequence with attention
11981. F11981 Other/Unknown — sequence-to-sequence model
11982. F11982 Algorithms & Theory of CS — competitive
11983. F11983 Computer Networks — strategic game
11984. F11984 Distributed Systems & Cloud — competitive algorithms
11985. F11985 ML & AI — Online algorithms
11986. F11986 Mathematics — dominance
11987. F11987 Curriculum-only — frontier model
11988. F11988 Mathematics — efficient frontier
11989. F11989 Curriculum-only — minimum-variance portfolio
11990. F11990 Mathematics — portfolio data
11991. F11991 Curriculum-only — financial model and portfolio optimization
11992. F11992 Other/Unknown — auction
11993. F11993 Cryptography & Security — bidder
11994. F11994 Other/Unknown — managing
11995. F11995 Cryptography & Security — teaming
11996. F11996 Curriculum-only — blue teaming
11997. F11997 Data Mining & Databases — managing data
11998. F11998 Distributed Systems & Cloud — including managing
11999. F11999 Mathematics — personal
12000. F12000 Cryptography & Security — personal data
12001. F12001 Curriculum-only — digital personal data protection act
12002. F12002 ML & AI — personal finance
12003. F12003 Operating Systems — personal information
12004. F12004 Other/Unknown — media
12005. F12005 Computer Architecture — time-sharing
12006. F12006 Curriculum-only — kb of media
12007. F12007 Data Mining & Databases — campaign
12008. F12008 Information Theory & Coding — media access
12009. F12009 Mathematics — homogeneous media
12010. F12010 Other/Unknown — digital media
12011. F12011 Mathematics — group-velocity derivation
12012. F12012 Other/Unknown — layered media
12013. F12013 Cryptography & Security — including supply chain management
12014. F12014 Curriculum-only — inventory and supply-chain management
12015. F12015 Other/Unknown — system design
12016. F12016 Algorithms & Theory of CS — XR (encompasses virtual reality, augmented reality, and mixed reality)
12017. F12017 Curriculum-only — index of system design
12018. F12018 Distributed Systems & Cloud — Hardware design
12019. F12019 Curriculum-only — column store layout
12020. F12020 Distributed Systems & Cloud — Data layout
12021. F12021 Computer Architecture — hardware platform
12022. F12022 Cryptography & Security — blockchain platform
12023. F12023 Cryptography & Security — trade finance blockchain
12024. F12024 Curriculum-only — ai platform access ended
12025. F12025 Distributed Systems & Cloud — algorithm and platform
12026. F12026 Curriculum-only — managed equivalent on the cloud platform
12027. F12027 Distributed Systems & Cloud — computing platform
12028. F12028 Curriculum-only — google cloud platform fit
12029. F12029 Distributed Systems & Cloud — iaas
12030. F12030 Distributed Systems & Cloud — pragma omp
12031. F12031 Information Theory & Coding — saltzer
12032. F12032 Operating Systems — heterogeneous programming with openmp
12033. F12033 Other/Unknown — communication protocol
12034. F12034 Computer Architecture — design flows
12035. F12035 Curriculum-only — network on chip
12036. F12036 Distributed Systems & Cloud — flash
12037. F12037 Computer Architecture — flash drive
12038. F12038 Computer Networks — fishing
12039. F12039 Curriculum-only — disk or flash access cost
12040. F12040 Distributed Systems & Cloud — memory access latency
12041. F12041 Computer Networks — key management
12042. F12042 Curriculum-only — attack specific to sensor network
12043. F12043 Operating Systems — hard disk
12044. F12044 Other/Unknown — energy balance
12045. F12045 Curriculum-only — cover aspect of low-power design
12046. F12046 Other/Unknown — microcontroller
12047. F12047 Data Mining & Databases — expression with arduino microcontroller
12048. F12048 Other/Unknown — moving platform
12049. F12049 Cryptography & Security — information systems development
12050. F12050 Other/Unknown — system dynamics
12051. F12051 Mathematics — potential energy
12052. F12052 Distributed Systems & Cloud — potential energy surface
12053. F12053 NLP & Speech — time-scale modification
12054. F12054 Other/Unknown — finite element
12055. F12055 Mathematics — galerkin discretization
12056. F12056 Other/Unknown — soft tissue
12057. F12057 Computer Architecture — single-cycle
12058. F12058 Curriculum-only — critical path of the single-cycle design
12059. F12059 Distributed Systems & Cloud — vector computer
12060. F12060 Mathematics — scheduled
12061. F12061 Curriculum-only — compiler-scheduled delay slot
12062. F12062 Information Theory & Coding — registrar
12063. F12063 Mathematics — associate
12064. F12064 Distributed Systems & Cloud — associate arrays
12065. F12065 Information Theory & Coding — associate editor
12066. F12066 Operating Systems — statically scheduled ilp
12067. F12067 Other/Unknown — waste management
12068. F12068 Signal/Image/Audio/Video Processing — enhancement
12069. F12069 Curriculum-only — iterative-enhancement model
12070. F12070 Signal/Image/Audio/Video Processing — essential matrix
12071. F12071 Other/Unknown — histogram equalizations
12072. F12072 Signal/Image/Audio/Video Processing — kaiser
12073. F12073 Mathematics — linear scale
12074. F12074 Signal/Image/Audio/Video Processing — noise removal
12075. F12075 Software Engineering — addison
12076. F12076 Computer Networks — adopter
12077. F12077 Curriculum-only — ip adoption
12078. F12078 Software Engineering — aliasing and cloning
12079. F12079 Computer Networks — back bay book
12080. F12080 Software Engineering — configuration management
12081. F12081 Curriculum-only — quality management and configuration management
12082. F12082 Software Engineering — consent
12083. F12083 Curriculum-only — consent-manager provision after about month
12084. F12084 Mathematics — semester
12085. F12085 Distributed Systems & Cloud — offering semester
12086. F12086 Information Theory & Coding — noc
12087. F12087 Curriculum-only — energy efficient noc
12088. F12088 Mathematics — vii
12089. F12089 Curriculum-only — component vii of advanced linear algebra
12090. F12090 Other/Unknown — elective
12091. F12091 Data Mining & Databases — elective for ug
12092. F12092 Distributed Systems & Cloud — pg elective
12093. F12093 ML & AI — batch
12094. F12094 Curriculum-only — batch offline into nosql
12095. F12095 Distributed Systems & Cloud — batch computation
12096. F12096 ML & AI — Batch learning
12097. F12097 Mathematics — mini-batch
12098. F12098 Curriculum-only — mini-batch and learning-rate behaviour
12099. F12099 Mathematics — requirement
12100. F12100 Computer Architecture — cim requirement
12101. F12101 Computer Networks — changing requirement
12102. F12102 Cryptography & Security — certification
12103. F12103 Curriculum-only — allocation of requirement to the component
12104. F12104 Curriculum-only — throw-away prototype to settle requirement
12105. F12105 Data Mining & Databases — dept
12106. F12106 Distributed Systems & Cloud — implementation detail
12107. F12107 ML & AI — atc
12108. F12108 Mathematics — boston area
12109. F12109 NLP & Speech — programme
12110. F12110 Curriculum-only — security programme
12111. F12111 Data Mining & Databases — award
12112. F12112 Distributed Systems & Cloud — award ceremony
12113. F12113 Computer Networks — institute for data
12114. F12114 Distributed Systems & Cloud — broad institute
12115. F12115 Mathematics — counted
12116. F12116 Curriculum-only — operand counted
12117. F12117 Mathematics — electromagnetism
12118. F12118 Operating Systems — service requirement
12119. F12119 Other/Unknown — batch normalization
12120. F12120 Mathematics — society
12121. F12121 ML & AI — society of mind
12122. F12122 Mathematics — democratic
12123. F12123 Algorithms & Theory of CS — marriage theorem
12124. F12124 Curriculum-only — hall marriage theorem
12125. F12125 NLP & Speech — courtesy of acoustical society
12126. F12126 Other/Unknown — american mathematical society
12127. F12127 Cryptography & Security — proof system for iso
12128. F12128 Curriculum-only — iso clause
12129. F12129 Distributed Systems & Cloud — fifo
12130. F12130 Curriculum-only — fifo and lossy channel
12131. F12131 Distributed Systems & Cloud — deq
12132. F12132 Curriculum-only — snapshot with non-fifo channel
12133. F12133 Distributed Systems & Cloud — fifo1
12134. F12134 Curriculum-only — batch friend lookup on the same person server
12135. F12135 Data Mining & Databases — exp env
12136. F12136 Distributed Systems & Cloud — hash table
12137. F12137 Algorithms & Theory of CS — chaining
12138. F12138 Curriculum-only — chaining as the historical form
12139. F12139 Distributed Systems & Cloud — distributed hash table
12140. F12140 Computer Networks — network distributed hash table
12141. F12141 Curriculum-only — peer-to-peer network and distributed hash table
12142. F12142 Distributed Systems & Cloud — ip lookup
12143. F12143 Information Theory & Coding — Forwarding methods (e.g., forwarding tables and matching algorithms)
12144. F12144 Operating Systems — memory pipeline
12145. F12145 Other/Unknown — movement
12146. F12146 Curriculum-only — internal and external address
12147. F12147 Other/Unknown — regulatory requirement
12148. F12148 Signal/Image/Audio/Video Processing — fisher iii
12149. F12149 Curriculum-only — metadata and lookup table
12150. F12150 Signal/Image/Audio/Video Processing — massachusett institute
12151. F12151 Mathematics — touch
12152. F12152 Data Mining & Databases — finally touch
12153. F12153 Signal/Image/Audio/Video Processing — reflectance map
12154. F12154 Mathematics — registered
12155. F12155 Distributed Systems & Cloud — registered trademark
12156. F12156 Other/Unknown — image segmentation
12157. F12157 Computer Architecture — image acquisition
12158. F12158 Distributed Systems & Cloud — video codecs
12159. F12159 Information Theory & Coding — mean shift
12160. F12160 Curriculum-only — mean-shift clustering
12161. F12161 ML & AI — image feature
12162. F12162 Mathematics — level set
12163. F12163 Algorithms & Theory of CS — arg minn
12164. F12164 Mathematics — proper convex function
12165. F12165 NLP & Speech — graph cut
12166. F12166 Other/Unknown — morphological operator
12167. F12167 Signal/Image/Audio/Video Processing — active contour
12168. F12168 Mathematics — popular
12169. F12169 Algorithms & Theory of CS — aps
12170. F12170 Curriculum-only — cache popular query
12171. F12171 Information Theory & Coding — error detection
12172. F12172 Curriculum-only — error detection and correction
12173. F12173 Information Theory & Coding — checksum
12174. F12174 Curriculum-only — sequence number and checksum
12175. F12175 Information Theory & Coding — retransmission
12176. F12176 Algorithms & Theory of CS — keeping track
12177. F12177 Curriculum-only — retransmission with the rfc timer
12178. F12178 Distributed Systems & Cloud — phase commit
12179. F12179 Curriculum-only — three-phase commit
12180. F12180 Information Theory & Coding — retransmission algorithm
12181. F12181 Signal/Image/Audio/Video Processing — computational photography
12182. F12182 Curriculum-only — image de-blurring
12183. F12183 Other/Unknown — degradation
12184. F12184 Information Theory & Coding — graceful degradation
12185. F12185 Other/Unknown — corrosion
12186. F12186 Signal/Image/Audio/Video Processing — image registration ii
12187. F12187 ML & AI — factor graph
12188. F12188 Algorithms & Theory of CS — clique
12189. F12189 Algorithms & Theory of CS — tur
12190. F12190 Algorithms & Theory of CS — kst
12191. F12191 Algorithms & Theory of CS — cube stone
12192. F12192 Computer Networks — graph model
12193. F12193 Curriculum-only — kogge stone
12194. F12194 Distributed Systems & Cloud — maximal independent set
12195. F12195 Algorithms & Theory of CS — luby
12196. F12196 Cryptography & Security — luby rackoff
12197. F12197 Curriculum-only — luby rackoff three-round
12198. F12198 ML & AI — belief propagation
12199. F12199 Algorithms & Theory of CS — triangulation
12200. F12200 ML & AI — exact inference
12201. F12201 Algorithms & Theory of CS — provably intractable
12202. F12202 ML & AI — marginal distribution
12203. F12203 Algorithms & Theory of CS — original graph
12204. F12204 ML & AI — clique tree
12205. F12205 Algorithms & Theory of CS — directed and undirected
12206. F12206 ML & AI — polytree
12207. F12207 Mathematics — linear inequality
12208. F12208 Other/Unknown — chordal
12209. F12209 ML & AI — chordal graph
12210. F12210 Computer Networks — tree graph
12211. F12211 ML & AI — bethe
12212. F12212 Other/Unknown — simultaneous triangulation
12213. F12213 Curriculum-only — simultaneous triangulation and simultaneous diagonalization
12214. F12214 Other/Unknown — variational
12215. F12215 Curriculum-only — generative modelling via variational auto-encoding
12216. F12216 ML & AI — approximate inference
12217. F12217 Curriculum-only — variational characterization of eigenvalue
12218. F12218 Mathematics — importance
12219. F12219 Computer Networks — pagerank
12220. F12220 Curriculum-only — eigenvector and pagerank
12221. F12221 Distributed Systems & Cloud — importance of broker
12222. F12222 Mathematics — counterpart
12223. F12223 Algorithms & Theory of CS — exact counterpart
12224. F12224 Curriculum-only — python counterpart
12225. F12225 Mathematics — mean eld
12226. F12226 ML & AI — mean eld update
12227. F12227 Mathematics — robust counterpart
12228. F12228 Operating Systems — dst
12229. F12229 Other/Unknown — variational auto encoders
12230. F12230 Signal/Image/Audio/Video Processing — constellation model
12231. F12231 Mathematics — delta function
12232. F12232 ML & AI — surface integral equation
12233. F12233 Mathematics — positivity
12234. F12234 Other/Unknown — electromagnetic
12235. F12235 Mathematics — electromagnetic forces
12236. F12236 Other/Unknown — electromagnetic compatibility
12237. F12237 Signal/Image/Audio/Video Processing — choose test function
12238. F12238 ML & AI — spectral clustering
12239. F12239 Algorithms & Theory of CS — normalized cut
12240. F12240 Curriculum-only — similarity of matrix
12241. F12241 Data Mining & Databases — spike
12242. F12242 Curriculum-only — absorbing uneven load and spike
12243. F12243 Data Mining & Databases — spike model
12244. F12244 Software Engineering — analysis and requirement
12245. F12245 Curriculum-only — analysis and requirement analysis
12246. F12246 Software Engineering — beta score
12247. F12247 Distributed Systems & Cloud — carnivore
12248. F12248 Software Engineering — cost estimation
12249. F12249 Curriculum-only — cost estimation with cocomo
12250. F12250 Software Engineering — cutback
12251. F12251 Curriculum-only — error handling and best practice
12252. F12252 Software Engineering — estimated value
12253. F12253 Distributed Systems & Cloud — block server
12254. F12254 Software Engineering — forum
12255. F12255 Curriculum-only — separate forum
12256. F12256 Distributed Systems & Cloud — mpi forum
12257. F12257 ML & AI — online forum
12258. F12258 Operating Systems — online forum participation
12259. F12259 Software Engineering — handling error
12260. F12260 Algorithms & Theory of CS — branching
12261. F12261 ML & AI — conditional planning
12262. F12262 Mathematics — fixing
12263. F12263 Curriculum-only — relative-cost-of-fixing curve
12264. F12264 Software Engineering — branching and merging
12265. F12265 Algorithms & Theory of CS — binary node
12266. F12266 Curriculum-only — mod init
12267. F12267 Distributed Systems & Cloud — mpi init
12268. F12268 Mathematics — diff
12269. F12269 Curriculum-only — fixed-width integer wrap around on overflow
12270. F12270 Information Theory & Coding — quiet
12271. F12271 Mathematics — dinner
12272. F12272 Operating Systems — kern
12273. F12273 Software Engineering — callback
12274. F12274 Curriculum-only — callback for all item
12275. F12275 Software Engineering — diff sq
12276. F12276 Curriculum-only — life-cycle model is needed
12277. F12277 Software Engineering — linkage
12278. F12278 Curriculum-only — ward linkage
12279. F12279 Data Mining & Databases — set of object
12280. F12280 Other/Unknown — linkage analysis
12281. F12281 Software Engineering — dynamic linkage
12282. F12282 Curriculum-only — add mysql read replicas
12283. F12283 Software Engineering — non-token
12284. F12284 Curriculum-only — recent trend in deep learning
12285. F12285 Data Mining & Databases — recent trend in mining
12286. F12286 Software Engineering — recession cone
12287. F12287 Other/Unknown — economics
12288. F12288 Computer Networks — Network economics
12289. F12289 Cryptography & Security — blockchain economics
12290. F12290 Curriculum-only — deployment model and economics
12291. F12291 Distributed Systems & Cloud — cloud economics
12292. F12292 Information Theory & Coding — heat pump
12293. F12293 Mathematics — era
12294. F12294 Curriculum-only — bletchley-era cryptanalysis
12295. F12295 Mathematics — qualitative
12296. F12296 Curriculum-only — qualitative and quantitative assessment
12297. F12297 Mathematics — repeated eigenvalue
12298. F12298 Other/Unknown — capital financing
12299. F12299 Software Engineering — export
12300. F12300 Mathematics — net dollar export
12301. F12301 Operating Systems — export policy
12302. F12302 Software Engineering — requirement engineering
12303. F12303 Curriculum-only — non-functional requirement
12304. F12304 Software Engineering — safe
12305. F12305 Cryptography & Security — safe prime
12306. F12306 Curriculum-only — cache is not safe for concurrent
12307. F12307 Data Mining & Databases — ballot
12308. F12308 Distributed Systems & Cloud — ballot number
12309. F12309 Operating Systems — rcu
12310. F12310 Software Engineering — jhala
12311. F12311 Software Engineering — system dynamics model
12312. F12312 Curriculum-only — thread-safe singleton
12313. F12313 Software Engineering — trajectory data
12314. F12314 Curriculum-only — cartesian product and tuple
12315. F12315 Data Mining & Databases — heap file
12316. F12316 Distributed Systems & Cloud — catalog
12317. F12317 Curriculum-only — add catalog
12318. F12318 Software Engineering — dicsonary
12319. F12319 Curriculum-only — iterator and generator
12320. F12320 Data Mining & Databases — heapfile
12321. F12321 Mathematics — number of trial
12322. F12322 NLP & Speech — conf
12323. F12323 Mathematics — conf map data
12324. F12324 NLP & Speech — reptile
12325. F12325 Other/Unknown — voltage source
12326. F12326 Mathematics — ground
12327. F12327 Computer Architecture — ground node
12328. F12328 Computer Networks — ground stations
12329. F12329 Data Mining & Databases — sky
12330. F12330 Computer Architecture — dark silicon
12331. F12331 Curriculum-only — dennard scaling and dark silicon
12332. F12332 Mathematics — ground plane
12333. F12333 Other/Unknown — pin diode
12334. F12334 Signal/Image/Audio/Video Processing — ieee conf
12335. F12335 Software Engineering — es conf ig
12336. F12336 Curriculum-only — building typed container
12337. F12337 Software Engineering — typing rule
12338. F12338 Curriculum-only — causation warning
12339. F12339 Software Engineering — warning messages
12340. F12340 Mathematics — publishing
12341. F12341 Cryptography & Security — packt publishing
12342. F12342 Information Theory & Coding — information theory
12343. F12343 Cryptography & Security — perfect secrecy
12344. F12344 Curriculum-only — cryptanalysis and perfect secrecy
12345. F12345 Data Mining & Databases — retrieval
12346. F12346 Curriculum-only — dense retrieval
12347. F12347 Curriculum-only — sparse retrieval and dense retrieval
12348. F12348 Data Mining & Databases — document retrieval
12349. F12349 Distributed Systems & Cloud — distributed storage
12350. F12350 Data Mining & Databases — distributed storage system
12351. F12351 Distributed Systems & Cloud — implementation of web-search
12352. F12352 Information Theory & Coding — communication model
12353. F12353 Curriculum-only — activity selection and huffman coding
12354. F12354 Information Theory & Coding — code length
12355. F12355 Curriculum-only — lossless and preserve dependency
12356. F12356 Information Theory & Coding — noisy-channel coding theorem
12357. F12357 Curriculum-only — cachin relative-entropy condition
12358. F12358 Information Theory & Coding — telephone lines
12359. F12359 ML & AI — kullback-leibler divergence
12360. F12360 Mathematics — elementary number theory
12361. F12361 Algorithms & Theory of CS — freiman homomorphism
12362. F12362 Curriculum-only — biased exponent
12363. F12363 Information Theory & Coding — error exponent
12364. F12364 Mathematics — chernoff
12365. F12365 Data Mining & Databases — tilting
12366. F12366 Information Theory & Coding — chernoff regime
12367. F12367 Mathematics — chebyshev and chernoff
12368. F12368 Algorithms & Theory of CS — chernoff bounds proof
12369. F12369 Curriculum-only — chernoff-bound rounding
12370. F12370 Information Theory & Coding — iid random
12371. F12371 ML & AI — pac learning
12372. F12372 Curriculum-only — pac learning model
12373. F12373 Mathematics — deviation theory
12374. F12374 Information Theory & Coding — neyman pearson
12375. F12375 Curriculum-only — neyman pearson lemma is stated
12376. F12376 Information Theory & Coding — neyman-pearson formulation
12377. F12377 Mathematics — random walk
12378. F12378 Curriculum-only — random walk and their message cost
12379. F12379 Information Theory & Coding — queueing delay
12380. F12380 Curriculum-only — throughput and bottleneck link
12381. F12381 Information Theory & Coding — sequence of iid
12382. F12382 Mathematics — arise
12383. F12383 Curriculum-only — configuration drift
12384. F12384 Distributed Systems & Cloud — clock drift
12385. F12385 Curriculum-only — clock skew and clock drift
12386. F12386 Mathematics — drunk
12387. F12387 Data Mining & Databases — masochistic drunk
12388. F12388 Mathematics — hitting time
12389. F12389 Information Theory & Coding — random sequence
12390. F12390 Mathematics — euclidean norm
12391. F12391 Curriculum-only — database and search engine
12392. F12392 Algorithms & Theory of CS — lowest common ancestor
12393. F12393 Data Mining & Databases — search engine architecture
12394. F12394 Distributed Systems & Cloud — large-scale
12395. F12395 Curriculum-only — checkpointing in large-scale machine-learning training
12396. F12396 Mathematics — stationary measure
12397. F12397 Distributed Systems & Cloud — shuffle
12398. F12398 Curriculum-only — stage boundary at shuffle
12399. F12399 Distributed Systems & Cloud — shuffle-exchange
12400. F12400 Mathematics — eir
12401. F12401 Algorithms & Theory of CS — ball in bin
12402. F12402 Computer Networks — power law
12403. F12403 Curriculum-only — ball into bin
12404. F12404 Distributed Systems & Cloud — perfect power law
12405. F12405 Mathematics — empirical cdf
12406. F12406 Curriculum-only — stopping at the first torn or corrupt record
12407. F12407 Distributed Systems & Cloud — nonfaulty process
12408. F12408 Curriculum-only — ping sweep
12409. F12409 ML & AI — early stopping
12410. F12410 Curriculum-only — dropout and early stopping
12411. F12411 Mathematics — stopping and converging
12412. F12412 Curriculum-only — practical stopping criterion
12413. F12413 Mathematics — stopping time
12414. F12414 Curriculum-only — stopping time and optional stopping
12415. F12415 Mathematics — bounded increment
12416. F12416 Curriculum-only — log barrier function
12417. F12417 Mathematics — central path
12418. F12418 Algorithms & Theory of CS — high probability
12419. F12419 Computer Networks — ci and cj
12420. F12420 Curriculum-only — saddle-point type condition for sdp
12421. F12421 Data Mining & Databases — angular synchronization
12422. F12422 Curriculum-only — restricted isometry proof
12423. F12423 Mathematics — order to prove
12424. F12424 Curriculum-only — choice between sketching the data
12425. F12425 Distributed Systems & Cloud — linear sketching
12426. F12426 Mathematics — strictly positive
12427. F12427 Algorithms & Theory of CS — Graph drawings
12428. F12428 ML & AI — interpreting line drawing
12429. F12429 Mathematics — matrix obtained
12430. F12430 Curriculum-only — byte scanned
12431. F12431 Mathematics — stretch
12432. F12432 Curriculum-only — maximum value theorem
12433. F12433 Mathematics — closed interval
12434. F12434 Algorithms & Theory of CS — better bound
12435. F12435 Mathematics — lim inf wk
12436. F12436 ML & AI — gibb
12437. F12437 Distributed Systems & Cloud — simulation
12438. F12438 Computer Architecture — physics engine
12439. F12439 Computer Networks — model simulation
12440. F12440 Curriculum-only — ideal real simulation paradigm
12441. F12441 Data Mining & Databases — alas
12442. F12442 Distributed Systems & Cloud — backend
12443. F12443 Curriculum-only — backend and open
12444. F12444 Distributed Systems & Cloud — Distributed simulation
12445. F12445 Mathematics — chebyshev polynomial
12446. F12446 Curriculum-only — binary or ternary
12447. F12447 Mathematics — wald equality
12448. F12448 Curriculum-only — weak duality theorem and duality gap
12449. F12449 Mathematics — web graph
12450. F12450 NLP & Speech — crossing rate
12451. F12451 Other/Unknown — capacity region
12452. F12452 Information Theory & Coding — gaussian mac
12453. F12453 Other/Unknown — circuit simulation
12454. F12454 Computer Networks — dominated strategy
12455. F12455 Computer Architecture — sustain
12456. F12456 Computer Networks — congestion game
12457. F12457 Computer Networks — tipping
12458. F12458 Cryptography & Security — competitive equilibrium
12459. F12459 Curriculum-only — failure of ordinal risk matrix
12460. F12460 Data Mining & Databases — cooperation
12461. F12461 Computer Networks — prisoner
12462. F12462 Mathematics — di usion
12463. F12463 Computer Networks — agent
12464. F12464 Algorithms & Theory of CS — Agent architectures (e.g., reactive, layered, cognitive)
12465. F12465 Computer Networks — local interaction
12466. F12466 Algorithms & Theory of CS — path planner
12467. F12467 Computer Networks — rationality
12468. F12468 Cryptography & Security — action space
12469. F12469 Curriculum-only — agent and mib
12470. F12470 Curriculum-only — pipeline to agent
12471. F12471 Distributed Systems & Cloud — mobile agent
12472. F12472 ML & AI — support agent
12473. F12473 Curriculum-only — enterprise devop and support agent
12474. F12474 Mathematics — dilemma
12475. F12475 Computer Networks — prisoner dilemma
12476. F12476 Algorithms & Theory of CS — prisoner dilemma game
12477. F12477 Curriculum-only — apple dilemma
12478. F12478 Mathematics — ort
12479. F12479 NLP & Speech — agent systems
12480. F12480 Other/Unknown — agent based
12481. F12481 Algorithms & Theory of CS — path aggregate
12482. F12482 Curriculum-only — aggregate and grouping
12483. F12483 Mathematics — expected aggregate
12484. F12484 Curriculum-only — long-run average reward
12485. F12485 ML & AI — discount factor
12486. F12486 Curriculum-only — belady optimal policy
12487. F12487 Mathematics — expected aggregate reward
12488. F12488 Curriculum-only — age-based
12489. F12489 Mathematics — correlated
12490. F12490 Information Theory & Coding — correlated sources
12491. F12491 Mathematics — cor
12492. F12492 Data Mining & Databases — enable optimal decision
12493. F12493 Mathematics — renewal counting process
12494. F12494 Curriculum-only — distributed rate limiting across node
12495. F12495 Mathematics — limiting value of px
12496. F12496 Computer Networks — branching process
12497. F12497 Mathematics — countable-state markov process
12498. F12498 Algorithms & Theory of CS — formal model
12499. F12499 Computer Architecture — video generation
12500. F12500 Cryptography & Security — automatic exploit generation
12501. F12501 Curriculum-only — augmentation and generation
12502. F12502 Data Mining & Databases — fan
12503. F12503 Curriculum-only — fan and chasm trap
12504. F12504 Distributed Systems & Cloud — generation of parallel loop
12505. F12505 ML & AI — energy-based
12506. F12506 Curriculum-only — energy-based and score-based model
12507. F12507 ML & AI — energy-based model
12508. F12508 Curriculum-only — image generation model
12509. F12509 ML & AI — Text Generation
12510. F12510 Mathematics — column generation
12511. F12511 Algorithms & Theory of CS — sharp threshold
12512. F12512 Computer Architecture — noise immunity
12513. F12513 Curriculum-only — choosing the threshold
12514. F12514 Distributed Systems & Cloud — coarse
12515. F12515 Algorithms & Theory of CS — coarse threshold
12516. F12516 Distributed Systems & Cloud — coarse grained
12517. F12517 Curriculum-only — chubby coarse-grained lock service
12518. F12518 ML & AI — masking
12519. F12519 Curriculum-only — nesting and masking
12520. F12520 ML & AI — threshold function
12521. F12521 Mathematics — decision rule
12522. F12522 Curriculum-only — decision rule sign
12523. F12523 Mathematics — kingman bound
12524. F12524 Information Theory & Coding — transition probability matrix
12525. F12525 Mathematics — markov chain xn
12526. F12526 NLP & Speech — rule generation
12527. F12527 Operating Systems — aggregate count
12528. F12528 Other/Unknown — approximating aggregate
12529. F12529 Computer Architecture — design competition
12530. F12530 Computer Networks — bertrand competition
12531. F12531 Curriculum-only — lotka volterra competition
12532. F12532 Distributed Systems & Cloud — programming competition
12533. F12533 Other/Unknown — contrast agent
12534. F12534 Curriculum-only — cohesion and coupling
12535. F12535 ML & AI — cross-modal coupling
12536. F12536 Mathematics — total variation distance
12537. F12537 Other/Unknown — data generation
12538. F12538 Curriculum-only — decision process that simplify cyber operation
12539. F12539 Other/Unknown — distributed generation system
12540. F12540 Computer Networks — best response
12541. F12541 Cryptography & Security — correlated equilibria
12542. F12542 Curriculum-only — convergence to equilibria
12543. F12543 Mathematics — linearization near equilibria
12544. F12544 Other/Unknown — fault simulation
12545. F12545 Curriculum-only — markov decision process and value function
12546. F12546 ML & AI — value iteration
12547. F12547 Curriculum-only — policy and value iteration
12548. F12548 Other/Unknown — material simulation
12549. F12549 Curriculum-only — ml system and efficiency
12550. F12550 Other/Unknown — Molecular simulation
12551. F12551 Other/Unknown — teleportation
12552. F12552 Signal/Image/Audio/Video Processing — aperiodic signal
12553. F12553 Mathematics — neumann
12554. F12554 Algorithms & Theory of CS — john von neumann
12555. F12555 Computer Architecture — von neumann architecture
12556. F12556 Curriculum-only — birkhoff von neumann decomposition
12557. F12557 Information Theory & Coding — pere iterated von neumann
12558. F12558 Mathematics — mixed
12559. F12559 Algorithms & Theory of CS — Integer Linear Programming
12560. F12560 Computer Networks — form game
12561. F12561 Curriculum-only — john nash
12562. F12562 ML & AI — latent dirichlet allocation
12563. F12563 Mathematics — nash-william inequality
12564. F12564 ML & AI — tucker decomposition
12565. F12565 Mathematics — von neumann analysis
12566. F12566 Other/Unknown — bargaining
12567. F12567 Computer Networks — bargaining in stationary network
12568. F12568 Other/Unknown — extensive form
12569. F12569 Computer Networks — bayes nash equilibrium
12570. F12570 Mathematics — mixed strategy
12571. F12571 Other/Unknown — existence of nash equilibrium
12572. F12572 Signal/Image/Audio/Video Processing — dct
12573. F12573 Computer Architecture — dct data
12574. F12574 Distributed Systems & Cloud — vivek
12575. F12575 Computer Architecture — vivek shah
12576. F12576 Information Theory & Coding — dct transform
12577. F12577 Signal/Image/Audio/Video Processing — discrete fourier
12578. F12578 Algorithms & Theory of CS — lder continuous with exponent
12579. F12579 Mathematics — lder continuous of order
12580. F12580 Signal/Image/Audio/Video Processing — ho lder continuous
12581. F12581 Software Engineering — accountability
12582. F12582 Algorithms & Theory of CS — bash function
12583. F12583 Software Engineering — code generation
12584. F12584 Distributed Systems & Cloud — communication code generation
12585. F12585 Other/Unknown — instruction set
12586. F12586 Computer Architecture — beta instruction set
12587. F12587 Curriculum-only — gate through the instruction set to the operating system
12588. F12588 Operating Systems — dawn of ibm
12589. F12589 Mathematics — sixty
12590. F12590 Operating Systems — instruction set evolution
12591. F12591 Other/Unknown — performance measure
12592. F12592 Curriculum-only — ml and performance measure
12593. F12593 Software Engineering — automatic code generations
12594. F12594 Algorithms & Theory of CS — fan-in and fan-out
12595. F12595 Curriculum-only — average fan-out
12596. F12596 Software Engineering — game of life
12597. F12597 Algorithms & Theory of CS — set interface
12598. F12598 Curriculum-only — abstract class and interface
12599. F12599 Curriculum-only — interface is defined by the consumer
12600. F12600 Curriculum-only — dma and storage interface
12601. F12601 Data Mining & Databases — generic interface
12602. F12602 Curriculum-only — pre-trained application programming interface
12603. F12603 Data Mining & Databases — sql interface
12604. F12604 Distributed Systems & Cloud — asyncrom
12605. F12605 Curriculum-only — container network interface
12606. F12606 Distributed Systems & Cloud — port replicator code
12607. F12607 Curriculum-only — client stub marshalling the procedure id
12608. F12608 Distributed Systems & Cloud — system call interface
12609. F12609 Mathematics — born approximation
12610. F12610 Curriculum-only — python specifics are recalled
12611. F12611 NLP & Speech — Natural language interfaces
12612. F12612 Operating Systems — operating system interface
12613. F12613 Other/Unknown — Haptic Interfaces
12614. F12614 Signal/Image/Audio/Video Processing — Gestural Interfaces
12615. F12615 Software Engineering — computer interfaces
12616. F12616 Computer Networks — external interface file
12617. F12617 Software Engineering — human computer interaction
12618. F12618 Cryptography & Security — security mechanism
12619. F12619 Curriculum-only — accelerated decoding and memory management
12620. F12620 Data Mining & Databases — join algorithm
12621. F12621 Curriculum-only — projection and the join algorithm
12622. F12622 Distributed Systems & Cloud — cache coherence
12623. F12623 Curriculum-only — cache coherence and memory consistency
12624. F12624 Distributed Systems & Cloud — hardware cache coherence
12625. F12625 Curriculum-only — place this among the main memory
12626. F12626 Distributed Systems & Cloud — Multiprocessor cache coherence
12627. F12627 Operating Systems — directory-based cache coherence protocol
12628. F12628 Software Engineering — garbage collection
12629. F12629 Curriculum-only — garbage collection system
12630. F12630 Software Engineering — Dynamic memory
12631. F12631 Curriculum-only — device memory allocation
12632. F12632 Software Engineering — dynamic memory allocation
12633. F12633 Signal/Image/Audio/Video Processing — continuous monotone increasing function
12634. F12634 Software Engineering — msi protocol
12635. F12635 Curriculum-only — three-state msi protocol with bus read
12636. F12636 Software Engineering — multi-modal interface
12637. F12637 Cryptography & Security — verification
12638. F12638 Algorithms & Theory of CS — Program verification
12639. F12639 Computer Architecture — fingerprint verification system
12640. F12640 Computer Networks — email verification
12641. F12641 Cryptography & Security — signature verification
12642. F12642 Curriculum-only — policy verification by satisfiability solving
12643. F12643 Distributed Systems & Cloud — Analysis and verification
12644. F12644 Curriculum-only — cloud dataflow service
12645. F12645 Distributed Systems & Cloud — google dataflow
12646. F12646 Other/Unknown — automatic verification
12647. F12647 Software Engineering — algorithm for solving
12648. F12648 Distributed Systems & Cloud — program execution
12649. F12649 Mathematics — graph coloring
12650. F12650 ML & AI — empirical distribution
12651. F12651 Mathematics — upper and lower
12652. F12652 Other/Unknown — asymmetric
12653. F12653 Computer Networks — asymmetric keys
12654. F12654 Cryptography & Security — asymmetric cryptography
12655. F12655 Curriculum-only — anti-entropy by merkle tree
12656. F12656 Other/Unknown — asymmetric catalysis
12657. F12657 Signal/Image/Audio/Video Processing — r0l
12658. F12658 Software Engineering — catena
12659. F12659 ML & AI — latent semantic analysis
12660. F12660 NLP & Speech — top-down parsing
12661. F12661 Other/Unknown — Semantic Parsing
12662. F12662 Software Engineering — serial dynamic memory allocation
12663. F12663 Curriculum-only — aggressive speculation
12664. F12664 Distributed Systems & Cloud — prefetching
12665. F12665 Operating Systems — software prefetching
12666. F12666 Curriculum-only — hardware and software prefetching
12667. F12667 Software Engineering — straightforward memory allocation
12668. F12668 Data Mining & Databases — old sublist
12669. F12669 Software Engineering — merge sorted sublist
12670. F12670 Curriculum-only — python threading
12671. F12671 Distributed Systems & Cloud — cuda
12672. F12672 Curriculum-only — correspondence with cuda
12673. F12673 Distributed Systems & Cloud — cuda programming
12674. F12674 Curriculum-only — opencl and heterogeneous computing
12675. F12675 Distributed Systems & Cloud — heterogeneous computing with opencl
12676. F12676 Software Engineering — unoptimized code generation
12677. F12677 Cryptography & Security — validation process
12678. F12678 Curriculum-only — experiment and validation
12679. F12679 Data Mining & Databases — confusion table
12680. F12680 Curriculum-only — mnist data set
12681. F12681 Data Mining & Databases — model validation
12682. F12682 Distributed Systems & Cloud — type of data set
12683. F12683 Information Theory & Coding — original data
12684. F12684 Curriculum-only — generator and parity-check matrix
12685. F12685 Information Theory & Coding — low density parity check
12686. F12686 ML & AI — monte carlo sampling
12687. F12687 Other/Unknown — data source
12688. F12688 Computer Architecture — raw data
12689. F12689 Curriculum-only — analytics pipeline from raw data
12690. F12690 Other/Unknown — Process validation
12691. F12691 Software Engineering — postgre
12692. F12692 Computer Networks — strategy profile
12693. F12693 Curriculum-only — allocation profile
12694. F12694 Data Mining & Databases — intensity profiles
12695. F12695 Information Theory & Coding — complexity profile
12696. F12696 Mathematics — payo
12697. F12697 Other/Unknown — subgame
12698. F12698 Computer Networks — repeated game
12699. F12699 Data Mining & Databases — incomplete
12700. F12700 Computer Networks — incomplete information
12701. F12701 ML & AI — Incomplete data
12702. F12702 Other/Unknown — tooth profile
12703. F12703 Software Engineering — profile code
12704. F12704 Curriculum-only — error reporting and profiling
12705. F12705 Distributed Systems & Cloud — cell profiling
12706. F12706 Software Engineering — code profiling
12707. F12707 Algorithms & Theory of CS — supernode
12708. F12708 Computer Networks — cmm
12709. F12709 Curriculum-only — cmm level are described
12710. F12710 Data Mining & Databases — black box
12711. F12711 Curriculum-only — black-box and white-box test-case design
12712. F12712 Data Mining & Databases — deletion channel
12713. F12713 Distributed Systems & Cloud — data race
12714. F12714 Algorithms & Theory of CS — acm symposium
12715. F12715 Distributed Systems & Cloud — software fault tolerance
12716. F12716 Algorithms & Theory of CS — compact suffix arrays
12717. F12717 Curriculum-only — suffix tree and suffix arrays
12718. F12718 Distributed Systems & Cloud — task graph
12719. F12719 Algorithms & Theory of CS — ext3
12720. F12720 Computer Networks — exclusive lock
12721. F12721 Cryptography & Security — auditor
12722. F12722 Computer Networks — grant and revoke
12723. F12723 Cryptography & Security — siam journal on computing
12724. F12724 Cryptography & Security — verifiable
12725. F12725 Curriculum-only — active transaction table
12726. F12726 Curriculum-only — fraud in card transaction
12727. F12727 Curriculum-only — repeated-nonce catastrophe in gcm
12728. F12728 Curriculum-only — update the transaction
12729. F12729 Data Mining & Databases — bufferpool
12730. F12730 Curriculum-only — sequence of itemset
12731. F12731 Data Mining & Databases — frequent itemset
12732. F12732 Curriculum-only — purchase transaction and gps signal
12733. F12733 Data Mining & Databases — simpledb
12734. F12734 Curriculum-only — purchase transaction record
12735. F12735 Data Mining & Databases — transaction schedule
12736. F12736 Distributed Systems & Cloud — abort
12737. F12737 Curriculum-only — conflict and abort
12738. F12738 Data Mining & Databases — subordinate
12739. F12739 Distributed Systems & Cloud — aborted
12740. F12740 Curriculum-only — aborted and terminated
12741. F12741 Distributed Systems & Cloud — access constraint
12742. F12742 Curriculum-only — linearizability checker
12743. F12743 Distributed Systems & Cloud — lock-free ro transaction
12744. F12744 Curriculum-only — de morgan law
12745. F12745 Distributed Systems & Cloud — morgan and claypool
12746. F12746 Curriculum-only — query processing and transaction
12747. F12747 Distributed Systems & Cloud — quorum
12748. F12748 Curriculum-only — quorum journal
12749. F12749 Distributed Systems & Cloud — quorum-based
12750. F12750 Curriculum-only — non-token and quorum-based
12751. F12751 Distributed Systems & Cloud — quorum-based mutual exclusion
12752. F12752 Curriculum-only — early restart
12753. F12753 Data Mining & Databases — random walk with restart
12754. F12754 Distributed Systems & Cloud — rw transaction
12755. F12755 Distributed Systems & Cloud — transaction manager
12756. F12756 Information Theory & Coding — ieee transaction
12757. F12757 Distributed Systems & Cloud — ieee transaction on mobile
12758. F12758 Information Theory & Coding — ieee transaction on communication
12759. F12759 ML & AI — black-box attack
12760. F12760 Curriculum-only — black-box attack and the jailbreak taxonomy
12761. F12761 ML & AI — xie
12762. F12762 Distributed Systems & Cloud — xie yong
12763. F12763 Mathematics — euro
12764. F12764 Cryptography & Security — miner
12765. F12765 Data Mining & Databases — ability to mine
12766. F12766 Mathematics — modeling languages
12767. F12767 Computer Networks — seek to minimize
12768. F12768 Curriculum-only — hdd seek ms
12769. F12769 Mathematics — supported function
12770. F12770 NLP & Speech — language modeling
12771. F12771 ML & AI — masked language modeling
12772. F12772 NLP & Speech — lexical similarity
12773. F12773 Curriculum-only — distance and similarity measure
12774. F12774 ML & AI — cosine similarity
12775. F12775 Curriculum-only — word-count vector and cosine similarity
12776. F12776 NLP & Speech — anaphora
12777. F12777 Operating Systems — acm symposium on operating
12778. F12778 Curriculum-only — exclusive lock held
12779. F12779 Operating Systems — log for transaction
12780. F12780 Curriculum-only — cartesian product and rename
12781. F12781 Operating Systems — ld r1
12782. F12782 Curriculum-only — multi-level cache with split transaction bus
12783. F12783 Operating Systems — two-phase
12784. F12784 Curriculum-only — two-phase method ii
12785. F12785 Operating Systems — two-phase commit
12786. F12786 Curriculum-only — optional multi-shard transaction by two-phase commit
12787. F12787 Distributed Systems & Cloud — paxo
12788. F12788 Curriculum-only — consensus in cloud computing and paxo
12789. F12789 Distributed Systems & Cloud — harp
12790. F12790 Algorithms & Theory of CS — asynchronous network model
12791. F12791 Distributed Systems & Cloud — scalable lookup
12792. F12792 Curriculum-only — viewstamped replication and zab as relative
12793. F12793 Operating Systems — two-phase locking
12794. F12794 Curriculum-only — locking and two-phase locking
12795. F12795 Operating Systems — strict two-phase locking
12796. F12796 Curriculum-only — write-ahead-logged key-value store
12797. F12797 Operating Systems — write-ahead log
12798. F12798 Curriculum-only — log manager write the write-ahead log
12799. F12799 Operating Systems — write-ahead logging
12800. F12800 Other/Unknown — electronic
12801. F12801 Algorithms & Theory of CS — Electronic commerce
12802. F12802 Cryptography & Security — electronic currency
12803. F12803 Distributed Systems & Cloud — electronic designs
12804. F12804 Other/Unknown — electronic controls
12805. F12805 Curriculum-only — map of innovation
12806. F12806 Distributed Systems & Cloud — creation
12807. F12807 Curriculum-only — creation and basic query structure
12808. F12808 Distributed Systems & Cloud — owned
12809. F12809 Curriculum-only — gustafson speed-up are owned
12810. F12810 Distributed Systems & Cloud — rdd creation
12811. F12811 Other/Unknown — entrepreneur
12812. F12812 Mathematics — successful
12813. F12813 Curriculum-only — financial system depend for their successful operation
12814. F12814 Information Theory & Coding — time slot
12815. F12815 Curriculum-only — slotted-page heap file
12816. F12816 Information Theory & Coding — time division multiplexing
12817. F12817 Mathematics — stabilisation
12818. F12818 Information Theory & Coding — convolutional encoder
12819. F12819 Other/Unknown — Medical records
12820. F12820 Algorithms & Theory of CS — actuator
12821. F12821 Curriculum-only — robotics and dynamical system
12822. F12822 Data Mining & Databases — autonomous
12823. F12823 Cryptography & Security — decentralized autonomous organization
12824. F12824 Curriculum-only — autonomous linear dynamical system
12825. F12825 Data Mining & Databases — autonomous vehicle
12826. F12826 Distributed Systems & Cloud — cp system
12827. F12827 Curriculum-only — dnssec chain of trust
12828. F12828 Distributed Systems & Cloud — distributed trust
12829. F12829 Information Theory & Coding — autonomous agents
12830. F12830 Mathematics — autonomous equation
12831. F12831 Curriculum-only — explicit transaction
12832. F12832 Mathematics — conditionally stable
12833. F12833 Curriculum-only — trust-region and clipped-surrogate objective
12834. F12834 Operating Systems — trusting trust
12835. F12835 Other/Unknown — autonomous robot
12836. F12836 Mathematics — nonlinear autonomous system
12837. F12837 Other/Unknown — Cognitive robotics
12838. F12838 Algorithms & Theory of CS — disturbance rejection
12839. F12839 Computer Networks — quality of service
12840. F12840 Cryptography & Security — differential cryptanalysis
12841. F12841 Curriculum-only — linear cryptanalysis
12842. F12842 Distributed Systems & Cloud — resource provisioning
12843. F12843 Information Theory & Coding — blocking probability
12844. F12844 Other/Unknown — coordinate transformation
12845. F12845 Mathematics — euler-lagrange
12846. F12846 Curriculum-only — jacobian and hessian
12847. F12847 Data Mining & Databases — jacobian coordinate
12848. F12848 Curriculum-only — projective and jacobian coordinate
12849. F12849 Mathematics — jacobian formula
12850. F12850 Other/Unknown — electromagnetic actuators
12851. F12851 Algorithms & Theory of CS — friction coefficient
12852. F12852 Other/Unknown — guidance
12853. F12853 Computer Networks — provider
12854. F12854 Curriculum-only — classifier guidance
12855. F12855 Other/Unknown — kinematics
12856. F12856 Algorithms & Theory of CS — Forward kinematics
12857. F12857 Other/Unknown — Inverse kinematics
12858. F12858 Algorithms & Theory of CS — modeling error
12859. F12859 Computer Networks — re-planning
12860. F12860 Mathematics — real root
12861. F12861 Other/Unknown — optimal control
12862. F12862 Mathematics — minimum time optimal control
12863. F12863 Other/Unknown — path planning
12864. F12864 Algorithms & Theory of CS — global path planning
12865. F12865 Other/Unknown — private information
12866. F12866 Distributed Systems & Cloud — timed system
12867. F12867 Information Theory & Coding — rto
12868. F12868 Distributed Systems & Cloud — ack
12869. F12869 Information Theory & Coding — timeout
12870. F12870 Curriculum-only — arp cache and timeout
12871. F12871 Distributed Systems & Cloud — timeout deadline
12872. F12872 Information Theory & Coding — rtt estimation
12873. F12873 Curriculum-only — rtt estimation and timeout
12874. F12874 Information Theory & Coding — transport protocol
12875. F12875 Cryptography & Security — transport layer
12876. F12876 Curriculum-only — congestion control at the transport layer
12877. F12877 Distributed Systems & Cloud — transport layer protocol
12878. F12878 Other/Unknown — robust control
12879. F12879 Computer Architecture — additive synthesis
12880. F12880 Curriculum-only — form with the organic
12881. F12881 Distributed Systems & Cloud — physical design
12882. F12882 Curriculum-only — physical-design task of choosing organisation
12883. F12883 Information Theory & Coding — concatenative synthesis
12884. F12884 NLP & Speech — singing voice synthesis
12885. F12885 Other/Unknown — behavioral synthesis
12886. F12886 Curriculum-only — catalyst and tungsten
12887. F12887 Mathematics — lewis
12888. F12888 Computer Architecture — cameron lewis
12889. F12889 Other/Unknown — organic chemistry
12890. F12890 Curriculum-only — selectivity of equality
12891. F12891 Data Mining & Databases — selectivity estimation
12892. F12892 Other/Unknown — speech synthesis
12893. F12893 Information Theory & Coding — speech coding
12894. F12894 NLP & Speech — prosody
12895. F12895 Other/Unknown — system architecture
12896. F12896 Computer Networks — wide area network
12897. F12897 Information Theory & Coding — internet protocol
12898. F12898 Computer Networks — hypertext transfer protocol
12899. F12899 Cryptography & Security — content provider
12900. F12900 Curriculum-only — inter-domain routing protocol
12901. F12901 Computer Networks — ip service
12902. F12902 Curriculum-only — on-chip network
12903. F12903 Computer Networks — router architecture
12904. F12904 Curriculum-only — chip interconnect
12905. F12905 Distributed Systems & Cloud — ip address
12906. F12906 Curriculum-only — ip address lookup
12907. F12907 Distributed Systems & Cloud — announcement
12908. F12908 Information Theory & Coding — internet protocol version 6
12909. F12909 Computer Networks — tutorial on ipv6
12910. F12910 Information Theory & Coding — port number
12911. F12911 ML & AI — intermediate node
12912. F12912 Mathematics — cheat
12913. F12913 Algorithms & Theory of CS — alice and bob
12914. F12914 Curriculum-only — parameter cheat sheet
12915. F12915 ML & AI — cheating
12916. F12916 Distributed Systems & Cloud — cheating twice
12917. F12917 Mathematics — julia ijulia cheat-sheet
12918. F12918 Cryptography & Security — zero-knowledge
12919. F12919 Curriculum-only — honest-verifier zero knowledge
12920. F12920 Mathematics — dating
12921. F12921 Algorithms & Theory of CS — dating protocol
12922. F12922 Data Mining & Databases — online dating
12923. F12923 Mathematics — total amount
12924. F12924 Distributed Systems & Cloud — total amount of lateness
12925. F12925 Operating Systems — policy routing
12926. F12926 Computer Networks — digital subscriber line
12927. F12927 Other/Unknown — systematic sampling
12928. F12928 Computer Architecture — arithmetic structure
12929. F12929 Mathematics — building block
12930. F12930 Computer Architecture — analog building block
12931. F12931 Curriculum-only — combinational building block
12932. F12932 Mathematics — integrator
12933. F12933 Algorithms & Theory of CS — double integrator
12934. F12934 Curriculum-only — leapfrog integrator
12935. F12935 Other/Unknown — amplifier
12936. F12936 Computer Architecture — low noise
12937. F12937 Curriculum-only — destructive read and sense amplifier
12938. F12938 Other/Unknown — amplification
12939. F12939 Curriculum-only — privacy amplification
12940. F12940 Other/Unknown — current source
12941. F12941 Computer Architecture — dependent source
12942. F12942 Other/Unknown — fiber amplifiers
12943. F12943 Computer Architecture — laser systems
12944. F12944 Data Mining & Databases — led
12945. F12945 Distributed Systems & Cloud — transparent
12946. F12946 Information Theory & Coding — microwave
12947. F12947 Computer Architecture — microwave oven
12948. F12948 Mathematics — transverse
12949. F12949 Other/Unknown — cleaning
12950. F12950 Curriculum-only — cleaning tokenization stopword lemmatization feature model
12951. F12951 Other/Unknown — dbr lasers
12952. F12952 Other/Unknown — mealy
12953. F12953 Curriculum-only — mealy form
12954. F12954 Other/Unknown — microwave amplifiers
12955. F12955 Algorithms & Theory of CS — expander mixing
12956. F12956 Curriculum-only — mixing and the second eigenvalue
12957. F12957 ML & AI — impurity
12958. F12958 Mathematics — ergodicity
12959. F12959 Curriculum-only — focus and quantification
12960. F12960 Other/Unknown — mixing time
12961. F12961 Mathematics — time-reversal
12962. F12962 Other/Unknown — multiplexer
12963. F12963 HS ComputerScience Class XI / Unit 1: Computer Systems and Organisation — number system
12964. F12964 Curriculum-only — binary representation and number system
12965. F12965 Mathematics — arithmetic operation
12966. F12966 Information Theory & Coding — average energy
12967. F12967 Curriculum-only — sphere-packing and singleton bound
12968. F12968 Other/Unknown — mux
12969. F12969 Computer Architecture — dynamic voltage
12970. F12970 Curriculum-only — cache stays passive
12971. F12971 NLP & Speech — adjectival passive
12972. F12972 Other/Unknown — passive control
12973. F12973 Curriculum-only — radar for target detection
12974. F12974 Data Mining & Databases — building model
12975. F12975 Other/Unknown — doppler radar
12976. F12976 Curriculum-only — diagnostics and model building
12977. F12977 Other/Unknown — selective laser melting
12978. F12978 Signal/Image/Audio/Video Processing — control system signal processing
12979. F12979 ML & AI — object shape
12980. F12980 Mathematics — quadrics
12981. F12981 Signal/Image/Audio/Video Processing — frequency band
12982. F12982 Information Theory & Coding — gsm
12983. F12983 Signal/Image/Audio/Video Processing — mixing matrix
12984. F12984 Information Theory & Coding — tessellation
12985. F12985 Signal/Image/Audio/Video Processing — critical surface
12986. F12986 Computer Architecture — object tracking
12987. F12987 Cryptography & Security — data tracking
12988. F12988 Curriculum-only — gradient tracking
12989. F12989 Mathematics — clutter
12990. F12990 Computer Networks — positioning system
12991. F12991 Mathematics — tracking errors
12992. F12992 NLP & Speech — gesture
12993. F12993 Other/Unknown — target tracking
12994. F12994 Signal/Image/Audio/Video Processing — multi-target tracking
12995. F12995 Software Engineering — box testing
12996. F12996 Data Mining & Databases — hist
12997. F12997 ML & AI — lda
12998. F12998 Distributed Systems & Cloud — shared variable
12999. F12999 Algorithms & Theory of CS — space complexity
13000. F13000 Distributed Systems & Cloud — critical region
13001. F13001 Software Engineering — carnegie mellon university
13002. F13002 Operating Systems — maintaining coherent memory
13003. F13003 Software Engineering — competitive ratio
13004. F13004 Algorithms & Theory of CS — randomized
13005. F13005 Algorithms & Theory of CS — randomized select
13006. F13006 Curriculum-only — leader election by randomised timeout
13007. F13007 Curriculum-only — randomized-rounding ratio for facility location
13008. F13008 Distributed Systems & Cloud — distributed randomized algorithm
13009. F13009 Algorithms & Theory of CS — Dynamic graph algorithms
13010. F13010 ML & AI — randomized controlled trial
13011. F13011 Mathematics — randomized median
13012. F13012 Curriculum-only — randomized search and bayesian
13013. F13013 Other/Unknown — randomised control
13014. F13014 Signal/Image/Audio/Video Processing — randomized matrix multiplication
13015. F13015 Software Engineering — electronic mail
13016. F13016 Data Mining & Databases — informal specification
13017. F13017 Software Engineering — foundation of software engineering
13018. F13018 Curriculum-only — memory allocator are named
13019. F13019 Data Mining & Databases — bitmap
13020. F13020 Curriculum-only — bitmap and index-intersection plan are named
13021. F13021 Software Engineering — custom memory allocator
13022. F13022 Curriculum-only — integer of fixed size
13023. F13023 Software Engineering — garlan
13024. F13024 Mathematics — implicit
13025. F13025 Algorithms & Theory of CS — succinct data structure
13026. F13026 Curriculum-only — implicit and logarithmic differentiation
13027. F13027 Distributed Systems & Cloud — implicit parallelism
13028. F13028 Curriculum-only — cache way-partitioning
13029. F13029 Distributed Systems & Cloud — network processor
13030. F13030 ML & AI — implicit regularization
13031. F13031 Curriculum-only — regularization and implicit regularization
13032. F13032 Mathematics — discontinuous function
13033. F13033 Curriculum-only — curve sketching as applied optimization
13034. F13034 Mathematics — logarithm and geometry
13035. F13035 Curriculum-only — max min fair allocation by water-filling
13036. F13036 Mathematics — boundary and infinity
13037. F13037 Curriculum-only — completing the square
13038. F13038 Mathematics — demonstrated
13039. F13039 NLP & Speech — implicit bias
13040. F13040 Curriculum-only — implicit bias in deep learning
13041. F13041 Other/Unknown — implicit function
13042. F13042 Curriculum-only — derivative of composite and implicit function
13043. F13043 Other/Unknown — implicit function theorem
13044. F13044 Computer Architecture — sequencer
13045. F13045 Curriculum-only — dynamic superscalar
13046. F13046 Distributed Systems & Cloud — microprocessor evolution
13047. F13047 Software Engineering — fadd
13048. F13048 Computer Architecture — bne
13049. F13049 Distributed Systems & Cloud — add r3
13050. F13050 Software Engineering — glass box testing
13051. F13051 Computer Architecture — minus vt
13052. F13052 Distributed Systems & Cloud — naming
13053. F13053 Curriculum-only — content naming
13054. F13054 Distributed Systems & Cloud — naming service
13055. F13055 Information Theory & Coding — domain name
13056. F13056 Operating Systems — hierarchical naming
13057. F13057 Other/Unknown — signal analysis
13058. F13058 Software Engineering — flavor of naming
13059. F13059 Algorithms & Theory of CS — flanagan
13060. F13060 Distributed Systems & Cloud — java rmi
13061. F13061 Cryptography & Security — server ip
13062. F13062 Data Mining & Databases — file src
13063. F13063 Distributed Systems & Cloud — src ip
13064. F13064 Information Theory & Coding — syn
13065. F13065 Curriculum-only — syn cooky
13066. F13066 ML & AI — jin
13067. F13067 Information Theory & Coding — hui jin
13068. F13068 NLP & Speech — del
13069. F13069 Algorithms & Theory of CS — del-turing mindblower
13070. F13070 Data Mining & Databases — incompleteness theorem
13071. F13071 Algorithms & Theory of CS — computational complexity of learning
13072. F13072 Curriculum-only — lu decomposition and computational complexity
13073. F13073 Data Mining & Databases — penrose
13074. F13074 ML & AI — elimination ordering
13075. F13075 Curriculum-only — distributed spanning-tree algorithm
13076. F13076 ML & AI — junction tree algorithm
13077. F13077 Mathematics — axiomatic
13078. F13078 Curriculum-only — algebraic and axiomatic
13079. F13079 Data Mining & Databases — godel
13080. F13080 Mathematics — del operator
13081. F13081 Computer Networks — contractor
13082. F13082 Mathematics — accident
13083. F13083 Distributed Systems & Cloud — principal investigator
13084. F13084 Mathematics — organizational
13085. F13085 Cryptography & Security — provable-security
13086. F13086 Curriculum-only — aim of the provable-security course to let you read current research paper
13087. F13087 Data Mining & Databases — isn't provable
13088. F13088 Mathematics — stamp
13089. F13089 NLP & Speech — flight
13090. F13090 Algorithms & Theory of CS — itinerary
13091. F13091 Curriculum-only — drain in-flight request
13092. F13092 Data Mining & Databases — connecting flight
13093. F13093 Computer Networks — dallas
13094. F13094 Data Mining & Databases — san
13095. F13095 Computer Networks — san mateo
13096. F13096 Data Mining & Databases — san diego
13097. F13097 Distributed Systems & Cloud — san rafael
13098. F13098 Mathematics — altitude
13099. F13099 NLP & Speech — certified flight instructor
13100. F13100 Operating Systems — syn flood
13101. F13101 Curriculum-only — syn flood and syn cooky
13102. F13102 Other/Unknown — human factor
13103. F13103 Curriculum-only — assigning responsibility
13104. F13104 Other/Unknown — ethics
13105. F13105 Cryptography & Security — Codes of ethics
13106. F13106 Curriculum-only — ethics and rule of engagement
13107. F13107 Mathematics — smoothing
13108. F13108 Curriculum-only — naive bayes classifier with laplace smoothing
13109. F13109 Mathematics — prediction and smoothing
13110. F13110 Other/Unknown — Ethics in NLP
13111. F13111 ML & AI — gibb sampling
13112. F13112 Other/Unknown — mean field
13113. F13113 ML & AI — mean field update
13114. F13114 Other/Unknown — parameter estimation
13115. F13115 Curriculum-only — laplace approximation
13116. F13116 Mathematics — nonrandom parameter estimation
13117. F13117 NLP & Speech — global linear model
13118. F13118 Signal/Image/Audio/Video Processing — anti-aliasing
13119. F13119 Software Engineering — accident analysis
13120. F13120 Other/Unknown — aerospace engineering
13121. F13121 Software Engineering — axiomatic semantics
13122. F13122 Distributed Systems & Cloud — command line interface
13123. F13123 Software Engineering — compilation
13124. F13124 Curriculum-only — cross-compilation by two environment variable
13125. F13125 Distributed Systems & Cloud — fifo0
13126. F13126 Mathematics — optimise
13127. F13127 Other/Unknown — Just-in-time compilation and dynamic recompilation
13128. F13128 Computer Architecture — block ram
13129. F13129 Distributed Systems & Cloud — ipa
13130. F13130 Operating Systems — bio
13131. F13131 Distributed Systems & Cloud — bio sequence cross correlation
13132. F13132 Software Engineering — compile time
13133. F13133 Distributed Systems & Cloud — spawning
13134. F13134 Curriculum-only — spawning independent stream
13135. F13135 Distributed Systems & Cloud — type declaration
13136. F13136 Software Engineering — decaf
13137. F13137 Software Engineering — gflop
13138. F13138 Other/Unknown — dataflow analysis
13139. F13139 Software Engineering — foundation of dataflow analysis
13140. F13140 Operating Systems — volatile
13141. F13141 Computer Architecture — Non-volatile memory
13142. F13142 Mathematics — particle
13143. F13143 Curriculum-only — fault from particle strike
13144. F13144 Distributed Systems & Cloud — particle pair
13145. F13145 Information Theory & Coding — particle system
13146. F13146 ML & AI — importance sampling
13147. F13147 Curriculum-only — importance-sampling approximation
13148. F13148 ML & AI — particle filtering
13149. F13149 Mathematics — commutation
13150. F13150 Curriculum-only — cascade and commutation
13151. F13151 Mathematics — commutation with t-shift
13152. F13152 NLP & Speech — positron
13153. F13153 Operating Systems — non-volatile storage
13154. F13154 Other/Unknown — commutation relation
13155. F13155 Mathematics — canonical commutation relation
13156. F13156 Other/Unknown — confinement
13157. F13157 Curriculum-only — subgroup-confinement
13158. F13158 Other/Unknown — inertial confinement fusion
13159. F13159 HS Physics Class XI / Unit IX: Behavior of Perfect Gases and Kinetic Theory of Gases — kinetic theory
13160. F13160 ML & AI — cooking
13161. F13161 Mathematics — total thermal
13162. F13162 Other/Unknown — diffusion
13163. F13163 Curriculum-only — conditional diffusion
13164. F13164 ML & AI — denoising
13165. F13165 Curriculum-only — denoising score matching
13166. F13166 ML & AI — denoising diffusion probabilistic model
13167. F13167 Curriculum-only — forward and reverse diffusion
13168. F13168 ML & AI — stable diffusion
13169. F13169 Curriculum-only — conditional diffusion and stable diffusion
13170. F13170 Mathematics — equation with diffusion constant
13171. F13171 Other/Unknown — convection-diffusion
13172. F13172 Curriculum-only — economics of defect
13173. F13173 Information Theory & Coding — defective gene
13174. F13174 Mathematics — slip
13175. F13175 Distributed Systems & Cloud — chris
13176. F13176 Computer Architecture — chris buenrostro
13177. F13177 Distributed Systems & Cloud — chris dyer
13178. F13178 NLP & Speech — warp
13179. F13179 Curriculum-only — warp are combined into byte sector
13180. F13180 Other/Unknown — diffusion model
13181. F13181 Curriculum-only — conditional diffusion model
13182. F13182 Other/Unknown — distillation
13183. F13183 ML & AI — knowledge distillation
13184. F13184 Curriculum-only — sparsity and knowledge distillation
13185. F13185 Mathematics — food
13186. F13186 Algorithms & Theory of CS — food truck order
13187. F13187 Cryptography & Security — beer
13188. F13188 Data Mining & Databases — th food
13189. F13189 Mathematics — burger
13190. F13190 Data Mining & Databases — toconsider
13191. F13191 Mathematics — cal
13192. F13192 Information Theory & Coding — dipole
13193. F13193 Computer Networks — dpi
13194. F13194 Mathematics — dipole source
13195. F13195 Computer Networks — utility maximizations
13196. F13196 Curriculum-only — greedy marginal-utility allocator
13197. F13197 Data Mining & Databases — utility data
13198. F13198 Information Theory & Coding — sequence of state
13199. F13199 Mathematics — utility function
13200. F13200 Data Mining & Databases — seeking help
13201. F13201 Distributed Systems & Cloud — specialization
13202. F13202 Curriculum-only — specialisation pays when general-purpose scaling slow
13203. F13203 Distributed Systems & Cloud — specialization of scalable system
13204. F13204 Mathematics — warm
13205. F13205 ML & AI — warm-up
13206. F13206 Curriculum-only — learning-rate warm-up
13207. F13207 Operating Systems — sel
13208. F13208 Other/Unknown — energy conservation
13209. F13209 ML & AI — lighting
13210. F13210 Other/Unknown — food processing
13211. F13211 Information Theory & Coding — magnetic dipole
13212. F13212 Other/Unknown — electromagnetic field
13213. F13213 Mathematics — forming
13214. F13214 Other/Unknown — elastic deformation
13215. F13215 Cryptography & Security — titanium
13216. F13216 Distributed Systems & Cloud — bare metal
13217. F13217 Curriculum-only — bare metal and hosted hypervisor
13218. F13218 Other/Unknown — metal cutting
13219. F13219 Mathematics — concrete
13220. F13220 Other/Unknown — percolation
13221. F13221 Data Mining & Databases — consolidated
13222. F13222 Mathematics — shear modulus
13223. F13223 Other/Unknown — direct shear test
13224. F13224 Other/Unknown — thermal-annealing
13225. F13225 Signal/Image/Audio/Video Processing — image denoising
13226. F13226 Data Mining & Databases — irradiance
13227. F13227 Other/Unknown — photometry
13228. F13228 Signal/Image/Audio/Video Processing — binary image
13229. F13229 Mathematics — characteristics
13230. F13230 Curriculum-only — characteristics of big data
13231. F13231 Distributed Systems & Cloud — characteristics of stream data
13232. F13232 Curriculum-only — shared memory usage
13233. F13233 Distributed Systems & Cloud — peak memory usage
13234. F13234 Algorithms & Theory of CS — median finding
13235. F13235 Curriculum-only — address mapping and scheduling
13236. F13236 Curriculum-only — warp scheduling
13237. F13237 Data Mining & Databases — identity relation
13238. F13238 Distributed Systems & Cloud — dynamic scheduling
13239. F13239 Curriculum-only — dynamic scheduling with tomasulo algorithm
13240. F13240 Distributed Systems & Cloud — efficient scheduling
13241. F13241 Curriculum-only — congestion control and fairness
13242. F13242 Distributed Systems & Cloud — orchestration and scheduling
13243. F13243 Algorithms & Theory of CS — expected running time
13244. F13244 Curriculum-only — completely fair scheduler weight
13245. F13245 Distributed Systems & Cloud — cilk implementation
13246. F13246 Cryptography & Security — socket
13247. F13247 Curriculum-only — byte and socket
13248. F13248 Distributed Systems & Cloud — livelock
13249. F13249 Curriculum-only — deadlock and livelock
13250. F13250 Information Theory & Coding — channel characteristics
13251. F13251 Curriculum-only — aloha and slotted aloha
13252. F13252 ML & AI — proxy
13253. F13253 Curriculum-only — application-proxy firewall
13254. F13254 Mathematics — consumption
13255. F13255 Computer Networks — fuel consumption
13256. F13256 Information Theory & Coding — Sustainability goals, resource consumption, and economic viability
13257. F13257 Mathematics — empty relation
13258. F13258 Curriculum-only — practical-operation gap that motivate the practitioner
13259. F13259 Data Mining & Databases — gk ak
13260. F13260 Mathematics — multi-period processor speed scheduling
13261. F13261 NLP & Speech — radiation characteristics
13262. F13262 Operating Systems — bandwidth-based scheduling
13263. F13263 Curriculum-only — delay-based and model-based control
13264. F13264 Operating Systems — delay-based scheduling
13265. F13265 Curriculum-only — scheduler such as loose round-robin
13266. F13266 Operating Systems — deficit round robin
13267. F13267 Curriculum-only — load-use stall
13268. F13268 Operating Systems — weighted round-robin
13269. F13269 Other/Unknown — bonded
13270. F13270 Mathematics — bearing
13271. F13271 Cryptography & Security — seal
13272. F13272 Mathematics — cylinder
13273. F13273 Other/Unknown — bearing capacity
13274. F13274 Curriculum-only — decision-tree instability
13275. F13275 Other/Unknown — Network performance analysis
13276. F13276 Computer Architecture — comparator
13277. F13277 Curriculum-only — root of unity and phasor
13278. F13278 Operating Systems — driver
13279. F13279 Computer Architecture — flat panel displays
13280. F13280 Curriculum-only — corpus size is the main driver
13281. F13281 Mathematics — driver of duality
13282. F13282 Operating Systems — dwell time
13283. F13283 Other/Unknown — device driver
13284. F13284 Information Theory & Coding — schedulability test
13285. F13285 Other/Unknown — rolling bearings
13286. F13286 Curriculum-only — social network and traffic flow
13287. F13287 Signal/Image/Audio/Video Processing — homography
13288. F13288 Distributed Systems & Cloud — recording
13289. F13289 Computer Architecture — recording and editing
13290. F13290 Cryptography & Security — recording of transaction
13291. F13291 Distributed Systems & Cloud — snapshot recording algorithm
13292. F13292 Curriculum-only — global state and snapshot recording algorithm
13293. F13293 Mathematics — needle
13294. F13294 Curriculum-only — memory contradiction and the needle
13295. F13295 Other/Unknown — diffraction
13296. F13296 NLP & Speech — diffraction patterns
13297. F13297 Other/Unknown — crystal
13298. F13298 Computer Architecture — crystal oscillators
13299. F13299 Mathematics — reflecting
13300. F13300 Other/Unknown — crystal growth
13301. F13301 Curriculum-only — photonic and wireless link on chip
13302. F13302 Other/Unknown — optical fiber
13303. F13303 Information Theory & Coding — optical network
13304. F13304 Other/Unknown — guided wave
13305. F13305 Algorithms & Theory of CS — dynamic connectivity
13306. F13306 Computer Architecture — scope probe
13307. F13307 Curriculum-only — build and probe
13308. F13308 Other/Unknown — single crystal
13309. F13309 Computer Architecture — magnetism
13310. F13310 Curriculum-only — flash solid-state drive
13311. F13311 Other/Unknown — solid state physics
13312. F13312 Mathematics — asymptotic behavior
13313. F13313 Algorithms & Theory of CS — asymptotic behavior of function
13314. F13314 Curriculum-only — asymptotic behaviour of trajectory
13315. F13315 Mathematics — isolated
13316. F13316 Algorithms & Theory of CS — isolated vertex
13317. F13317 Curriculum-only — isolated laboratory against metasploitable-class machine
13318. F13318 Information Theory & Coding — Isolated system
13319. F13319 Mathematics — pole of order
13320. F13320 Other/Unknown — adiabatic
13321. F13321 Mathematics — adiabatic theorem
13322. F13322 Curriculum-only — dog leg
13323. F13323 Data Mining & Databases — number of leg
13324. F13324 Mathematics — perfectly matched layer
13325. F13325 Other/Unknown — cold
13326. F13326 Computer Networks — cold-start
13327. F13327 Curriculum-only — cold standby
13328. F13328 Other/Unknown — frequency analysis
13329. F13329 Curriculum-only — frequency analysis of hydrologic series
13330. F13330 Mathematics — goodness
13331. F13331 Other/Unknown — goodness of fit
13332. F13332 Curriculum-only — confidence interval and goodness of fit
13333. F13333 ML & AI — data sample
13334. F13334 Mathematics — chi-square
13335. F13335 Computer Networks — contingency
13336. F13336 Curriculum-only — chi-square and rs analysis
13337. F13337 Mathematics — anova
13338. F13338 Curriculum-only — anova on the segment
13339. F13339 Data Mining & Databases — linear regression model
13340. F13340 ML & AI — conditional mixture
13341. F13341 Mathematics — anova regression table
13342. F13342 Other/Unknown — low and high
13343. F13343 Signal/Image/Audio/Video Processing — dct coefficient
13344. F13344 Distributed Systems & Cloud — kin
13345. F13345 Information Theory & Coding — phase shift keying
13346. F13346 Signal/Image/Audio/Video Processing — higher frequency
13347. F13347 Other/Unknown — cross phase modulation
13348. F13348 Signal/Image/Audio/Video Processing — position determination
13349. F13349 Software Engineering — alignment
13350. F13350 Curriculum-only — automatic alignment
13351. F13351 Mathematics — una
13352. F13352 NLP & Speech — bof
13353. F13353 Signal/Image/Audio/Video Processing — direction histogram
13354. F13354 Software Engineering — asm volatile
13355. F13355 Distributed Systems & Cloud — analysis of cilk scheduler
13356. F13356 Computer Networks — thief
13357. F13357 Distributed Systems & Cloud — clone
13358. F13358 Curriculum-only — factory and clone
13359. F13359 Operating Systems — snoopy
13360. F13360 Distributed Systems & Cloud — competitive snoopy caching
13361. F13361 Operating Systems — snoopy cache
13362. F13362 Other/Unknown — tensor product
13363. F13363 Software Engineering — cilk runtime
13364. F13364 Curriculum-only — contingency planning and cyber crisis management
13365. F13365 Software Engineering — cpu scheduling
13366. F13366 Distributed Systems & Cloud — unrolling
13367. F13367 Curriculum-only — complete unrolling
13368. F13368 Software Engineering — code optimization
13369. F13369 Computer Architecture — lateral
13370. F13370 Curriculum-only — bulk loading
13371. F13371 Data Mining & Databases — earthquake
13372. F13372 Mathematics — process with rate
13373. F13373 Software Engineering — linking and loading
13374. F13374 Distributed Systems & Cloud — michal kapalka
13375. F13375 Software Engineering — microcode
13376. F13376 Curriculum-only — function-oriented against object-oriented development
13377. F13377 Software Engineering — optimistic
13378. F13378 Curriculum-only — amount of optimistic work
13379. F13379 Data Mining & Databases — optimistic concurrency control
13380. F13380 Distributed Systems & Cloud — fine grained
13381. F13381 Software Engineering — overloading
13382. F13382 Curriculum-only — atomic package
13383. F13383 Data Mining & Databases — machine learning package
13384. F13384 Curriculum-only — matplotlib and scipy
13385. F13385 Data Mining & Databases — numpy
13386. F13386 Curriculum-only — numpy and the floating-point model
13387. F13387 Distributed Systems & Cloud — cfd package
13388. F13388 Information Theory & Coding — numpy and matplotlib
13389. F13389 NLP & Speech — classification and regression tree
13390. F13390 ML & AI — cross-validation
13391. F13391 Curriculum-only — bootstrapping and cross-validation
13392. F13392 Data Mining & Databases — k-fold cross-validation
13393. F13393 Curriculum-only — hold-out and k-fold cross-validation
13394. F13394 ML & AI — leave-one-out cross-validation
13395. F13395 Curriculum-only — k-fold cross-validation and leave-one-out cross-validation
13396. F13396 NLP & Speech — confusion matrix
13397. F13397 Data Mining & Databases — receiver operating characteristic
13398. F13398 Other/Unknown — software package
13399. F13399 Software Engineering — packaging
13400. F13400 Curriculum-only — packaging are named
13401. F13401 Other/Unknown — electronics packaging
13402. F13402 Software Engineering — parallel storage allocation
13403. F13403 Algorithms & Theory of CS — cache-oblivious algorithm
13404. F13404 Distributed Systems & Cloud — multilevel
13405. F13405 Computer Architecture — multilevel memory
13406. F13406 Curriculum-only — multilevel index
13407. F13407 Distributed Systems & Cloud — number of cache miss
13408. F13408 Mathematics — cache obliviousness
13409. F13409 Algorithms & Theory of CS — block replacement
13410. F13410 Computer Architecture — lru replacement strategy
13411. F13411 Curriculum-only — banked last-level cache with replacement
13412. F13412 Mathematics — complex replacement
13413. F13413 Algorithms & Theory of CS — random sampling of column
13414. F13414 Mathematics — thesis
13415. F13415 Data Mining & Databases — universal machine
13416. F13416 Distributed Systems & Cloud — harald prokop
13417. F13417 Information Theory & Coding — manuscript
13418. F13418 Mathematics — total work
13419. F13419 Operating Systems — cache replacement
13420. F13420 Signal/Image/Audio/Video Processing — femoral
13421. F13421 Software Engineering — cache size
13422. F13422 Data Mining & Databases — premise set
13423. F13423 Software Engineering — preprocessor
13424. F13424 Distributed Systems & Cloud — preprocessor macro
13425. F13425 Software Engineering — privatization
13426. F13426 Algorithms & Theory of CS — quadratic probing
13427. F13427 Software Engineering — linear probing
13428. F13428 Curriculum-only — condition program order
13429. F13429 Distributed Systems & Cloud — write in program order
13430. F13430 Software Engineering — progress
13431. F13431 Computer Networks — internet access
13432. F13432 Cryptography & Security — progress in mapping
13433. F13433 Distributed Systems & Cloud — concurrent programming
13434. F13434 Curriculum-only — memory interleaving
13435. F13435 Distributed Systems & Cloud — liveness
13436. F13436 Curriculum-only — health endpoint for liveness
13437. F13437 Distributed Systems & Cloud — progress update
13438. F13438 Algorithms & Theory of CS — algorithm for processing massive
13439. F13439 Curriculum-only — massive multitask language understanding
13440. F13440 Distributed Systems & Cloud — massive data
13441. F13441 Curriculum-only — out-of-order execution break sequential consistency
13442. F13442 ML & AI — prompt
13443. F13443 Curriculum-only — instruction-centric prompt
13444. F13444 Curriculum-only — automatic prompt optimization
13445. F13445 Distributed Systems & Cloud — interactive prompt
13446. F13446 Curriculum-only — high-throughput computing on idle workstation
13447. F13447 Distributed Systems & Cloud — network of workstations
13448. F13448 ML & AI — command prompt
13449. F13449 Curriculum-only — auto-regressive model and large language model
13450. F13450 ML & AI — base llm
13451. F13451 Curriculum-only — sentence embedding from bert
13452. F13452 ML & AI — instruction tuning
13453. F13453 Curriculum-only — limitation of pure chain-of-thought reasoning
13454. F13454 ML & AI — few-shot
13455. F13455 Curriculum-only — few-shot cot
13456. F13456 ML & AI — few-shot learning
13457. F13457 Curriculum-only — directional stimulus prompting
13458. F13458 ML & AI — chain-of-thought prompting
13459. F13459 Curriculum-only — few-shot and in-context learning
13460. F13460 ML & AI — rag
13461. F13461 Curriculum-only — agentic rag
13462. F13462 Curriculum-only — rag system
13463. F13463 ML & AI — text prompt
13464. F13464 Curriculum-only — zero-shot and few-shot prompting
13465. F13465 ML & AI — zero-shot learning
13466. F13466 Mathematics — avoiding
13467. F13467 Curriculum-only — avoiding address translation during indexing
13468. F13468 Mathematics — avoiding cycling
13469. F13469 Curriculum-only — publish subscribe
13470. F13470 Mathematics — tukey
13471. F13471 NLP & Speech — language model
13472. F13472 Curriculum-only — contextual language-model training
13473. F13473 ML & AI — autoregressive language model
13474. F13474 Curriculum-only — prompting and the autoregressive language model
13475. F13475 ML & AI — gru
13476. F13476 Curriculum-only — complexity and when to use gru
13477. F13477 ML & AI — neural language model
13478. F13478 NLP & Speech — acoustic model
13479. F13479 NLP & Speech — trigram
13480. F13480 Mathematics — gram
13481. F13481 Algorithms & Theory of CS — schmidt
13482. F13482 ML & AI — gram matrix
13483. F13483 Computer Networks — anchor
13484. F13484 ML & AI — anchor word
13485. F13485 NLP & Speech — gram language model
13486. F13486 Operating Systems — snoopy protocol
13487. F13487 Other/Unknown — n-gram language model
13488. F13488 Software Engineering — atomic operation
13489. F13489 Algorithms & Theory of CS — processing massive data set
13490. F13490 Data Mining & Databases — mining massive data set
13491. F13491 Software Engineering — milestone
13492. F13492 Computer Architecture — major milestone
13493. F13493 Mathematics — span
13494. F13494 Computer Networks — icon
13495. F13495 Data Mining & Databases — prefix-span
13496. F13496 Information Theory & Coding — orthonormal set
13497. F13497 Curriculum-only — orthogonal and orthonormal set
13498. F13498 Mathematics — age and duration
13499. F13499 Curriculum-only — rao blackwell theorem
13500. F13500 Mathematics — orthogonal complement of span
13501. F13501 NLP & Speech — span task
13502. F13502 Signal/Image/Audio/Video Processing — linear span
13503. F13503 Information Theory & Coding — ideal nyquist
13504. F13504 Mathematics — locus
13505. F13505 Other/Unknown — root locus
13506. F13506 Signal/Image/Audio/Video Processing — nyquist frequency
13507. F13507 Software Engineering — pegasus
13508. F13508 Distributed Systems & Cloud — data-race detection in transaction
13509. F13509 Curriculum-only — sync and the race detector
13510. F13510 Software Engineering — renaming
13511. F13511 Curriculum-only — aliase and renaming
13512. F13512 Distributed Systems & Cloud — reordering
13513. F13513 Software Engineering — register renaming
13514. F13514 Curriculum-only — register renaming that remove war
13515. F13515 Software Engineering — replacement policy
13516. F13516 Algorithms & Theory of CS — noop
13517. F13517 Computer Architecture — alphanumeric display
13518. F13518 Computer Networks — sts
13519. F13519 Curriculum-only — multiplexed address and data line
13520. F13520 Distributed Systems & Cloud — monitor
13521. F13521 Information Theory & Coding — rcv
13522. F13522 ML & AI — font
13523. F13523 Data Mining & Databases — bold
13524. F13524 Information Theory & Coding — morse
13525. F13525 Computer Networks — establishment
13526. F13526 Cryptography & Security — key establishments
13527. F13527 Distributed Systems & Cloud — jan
13528. F13528 Data Mining & Databases — jan-07
13529. F13529 Distributed Systems & Cloud — pat
13530. F13530 Curriculum-only — nat and pat
13531. F13531 Information Theory & Coding — connection establishment
13532. F13532 Curriculum-only — connection establishment and closure
13533. F13533 Information Theory & Coding — morse code
13534. F13534 Mathematics — constructing
13535. F13535 Algorithms & Theory of CS — deduction
13536. F13536 Data Mining & Databases — trial and error
13537. F13537 Information Theory & Coding — optimal code
13538. F13538 Distributed Systems & Cloud — mapper
13539. F13539 Information Theory & Coding — efficient source coding
13540. F13540 Curriculum-only — hierarchy and layering
13541. F13541 Information Theory & Coding — lossy source coding
13542. F13542 Mathematics — edn
13543. F13543 Curriculum-only — cnn layer explained in detail with the math behind
13544. F13544 Data Mining & Databases — data mining explained
13545. F13545 Mathematics — Mathematical proof
13546. F13546 Algorithms & Theory of CS — writing mathematical proof
13547. F13547 Operating Systems — lapic
13548. F13548 Other/Unknown — image data
13549. F13549 Signal/Image/Audio/Video Processing — gaussian curvature
13550. F13550 Mathematics — revolution
13551. F13551 Computer Architecture — piano dance revolution
13552. F13552 Mathematics — volume of revolution
13553. F13553 Curriculum-only — surface and volume of revolution
13554. F13554 Software Engineering — ide
13555. F13555 Mathematics — killed
13556. F13556 Distributed Systems & Cloud — wakeup
13557. F13557 Data Mining & Databases — combinator
13558. F13558 Distributed Systems & Cloud — clock tick
13559. F13559 ML & AI — fido
13560. F13560 Mathematics — conv
13561. F13561 Information Theory & Coding — conv code
13562. F13562 ML & AI — rgmy2ornuz
13563. F13563 Mathematics — indicator function
13564. F13564 Information Theory & Coding — capacity of awgn channel
13565. F13565 Curriculum-only — interleaving for burst error
13566. F13566 Information Theory & Coding — coding gain
13567. F13567 Algorithms & Theory of CS — navigate
13568. F13568 Data Mining & Databases — csv
13569. F13569 HS ComputerScience Class XII / Unit 1: Computational Thinking and Programming – 2 — csv file
13570. F13570 Data Mining & Databases — read csv
13571. F13571 Information Theory & Coding — minimal trellis
13572. F13572 Distributed Systems & Cloud — input data
13573. F13573 Information Theory & Coding — dirty paper coding
13574. F13574 Mathematics — algebraic operation
13575. F13575 Information Theory & Coding — convolutional code
13576. F13576 ML & AI — min-sum
13577. F13577 Information Theory & Coding — min-sum
13578. F13578 Mathematics — comparing
13579. F13579 Cryptography & Security — comparing bitcoin scripting
13580. F13580 Curriculum-only — comparing several mean
13581. F13581 Mathematics — equal variance
13582. F13582 Computer Architecture — synopsys
13583. F13583 Curriculum-only — pci express lane
13584. F13584 Information Theory & Coding — long division
13585. F13585 Mathematics — closed-form expression
13586. F13586 Curriculum-only — asymptotics for cryptography
13587. F13587 Information Theory & Coding — hypothesis testing asymptotics
13588. F13588 Mathematics — Coordinate frames, translation, and rotation (2D and 3D)
13589. F13589 Algorithms & Theory of CS — binary fraction
13590. F13590 Computer Networks — node with degree
13591. F13591 Curriculum-only — amdahl bound behind the sequential fraction
13592. F13592 Data Mining & Databases — fraction of positive
13593. F13593 Information Theory & Coding — fraction error
13594. F13594 Mathematics — brahmagupta-pell equation
13595. F13595 Data Mining & Databases — grothendieck
13596. F13596 Computer Networks — bandeira
13597. F13597 Data Mining & Databases — grothendieck constant
13598. F13598 Mathematics — field of fraction
13599. F13599 Computer Networks — virus
13600. F13600 Curriculum-only — malware and virus
13601. F13601 Mathematics — informative prior
13602. F13602 Data Mining & Databases — pairing
13603. F13603 Curriculum-only — pairing and by divide and conquer
13604. F13604 Data Mining & Databases — a-list
13605. F13605 Curriculum-only — role of the bilinear pairing
13606. F13606 Data Mining & Databases — pairing-based cryptography
13607. F13607 Curriculum-only — pairing-friendly curve and their parameter ageing
13608. F13608 Data Mining & Databases — tate
13609. F13609 Curriculum-only — weil and tate pairing
13610. F13610 Data Mining & Databases — weil pairing
13611. F13611 Mathematics — one-to-one correspondence
13612. F13612 Curriculum-only — partial fraction procedure and trigonometric substitution
13613. F13613 Mathematics — parametric equation
13614. F13614 Algorithms & Theory of CS — minimization algorithm
13615. F13615 Mathematics — augmented lagrangian
13616. F13616 ML & AI — hoeffding
13617. F13617 Algorithms & Theory of CS — azuma hoeffding
13618. F13618 Curriculum-only — chernoff and hoeffding
13619. F13619 Mathematics — inner linearization of conjugate
13620. F13620 Algorithms & Theory of CS — moore
13621. F13621 Computer Architecture — state transition diagram
13622. F13622 Curriculum-only — boyer moore
13623. F13623 Information Theory & Coding — trellis diagram
13624. F13624 Mathematics — starting state
13625. F13625 Information Theory & Coding — jpeg compression
13626. F13626 Mathematics — dei
13627. F13627 Information Theory & Coding — pi dei
13628. F13628 Mathematics — dss
13629. F13629 Curriculum-only — pci dss
13630. F13630 Mathematics — irreducible markov
13631. F13631 Algorithms & Theory of CS — sano
13632. F13632 Curriculum-only — fixed-universe successor
13633. F13633 Data Mining & Databases — quantum computer
13634. F13634 Algorithms & Theory of CS — quantum algorithm
13635. F13635 ML & AI — parallel universe
13636. F13636 Mathematics — collapse
13637. F13637 Curriculum-only — collapse problem and verbalized sampling
13638. F13638 Mathematics — factoring algorithm
13639. F13639 Algorithms & Theory of CS — shor
13640. F13640 Curriculum-only — shor algorithm
13641. F13641 Mathematics — gravitational
13642. F13642 Curriculum-only — curve and arc length
13643. F13643 Mathematics — area in polar
13644. F13644 Curriculum-only — differentiability of vector function
13645. F13645 Mathematics — x2c
13646. F13646 NLP & Speech — contingency table
13647. F13647 Operating Systems — sleep and wakeup
13648. F13648 Other/Unknown — moore machine
13649. F13649 Information Theory & Coding — correcting random error
13650. F13650 Software Engineering — bang
13651. F13651 Mathematics — dat file
13652. F13652 NLP & Speech — tns
13653. F13653 Other/Unknown — scanning electron microscope
13654. F13654 Software Engineering — data file
13655. F13655 Algorithms & Theory of CS — constraint propagation
13656. F13656 Distributed Systems & Cloud — finalize
13657. F13657 Information Theory & Coding — input string
13658. F13658 Mathematics — csi
13659. F13659 NLP & Speech — num sg
13660. F13660 Software Engineering — backtracking
13661. F13661 Algorithms & Theory of CS — backtracking with forward checking
13662. F13662 Curriculum-only — armijo backtracking
13663. F13663 Mathematics — backtracking line search
13664. F13664 Software Engineering — close to square root
13665. F13665 Distributed Systems & Cloud — omp num thread
13666. F13666 Software Engineering — reused
13667. F13667 Curriculum-only — group and ring signature
13668. F13668 Software Engineering — runtime scheduler
13669. F13669 Curriculum-only — safety-critical and security-critical component
13670. F13670 Software Engineering — safety critical systems
13671. F13671 Curriculum-only — safety-critical system of the kind built for defence
13672. F13672 Software Engineering — sal
13673. F13673 Cryptography & Security — decentralized identifier
13674. F13674 Curriculum-only — identifier cve
13675. F13675 Operating Systems — address-space identifier
13676. F13676 Software Engineering — formal parameter
13677. F13677 Data Mining & Databases — environment pointer
13678. F13678 Mathematics — enclosing
13679. F13679 Algorithms & Theory of CS — clausal form
13680. F13680 ML & AI — converting to clausal form
13681. F13681 Software Engineering — global scope
13682. F13682 Cryptography & Security — legacy system
13683. F13683 Curriculum-only — legacy system and the choice
13684. F13684 Distributed Systems & Cloud — distributed software architecture
13685. F13685 NLP & Speech — sbar
13686. F13686 Mathematics — hillary
13687. F13687 NLP & Speech — headword
13688. F13688 Other/Unknown — adaptive system
13689. F13689 Software Engineering — separation of concern
13690. F13690 Algorithms & Theory of CS — software development kit
13691. F13691 Computer Architecture — machine design
13692. F13692 Cryptography & Security — collaborative software development
13693. F13693 Other/Unknown — prototyping
13694. F13694 Curriculum-only — prototyping model
13695. F13695 Other/Unknown — additive manufacturing
13696. F13696 Curriculum-only — incident lifecycle
13697. F13697 Other/Unknown — rapid prototyping
13698. F13698 Software Engineering — agile software development
13699. F13699 Curriculum-only — software maintenance and its model
13700. F13700 Software Engineering — software pipelining
13701. F13701 Curriculum-only — software pipelining and modulo scheduling
13702. F13702 Software Engineering — loop invariant code motion
13703. F13703 Mathematics — sse
13704. F13704 Software Engineering — loop test replacement
13705. F13705 Curriculum-only — software reliability compared
13706. F13706 Mathematics — non-homogeneous poisson process
13707. F13707 Curriculum-only — goel okumoto non-homogeneous poisson process
13708. F13708 Other/Unknown — system reliability
13709. F13709 Distributed Systems & Cloud — availability
13710. F13710 Computer Networks — high availability
13711. F13711 Curriculum-only — availability and partition tolerance
13712. F13712 Distributed Systems & Cloud — availability and consistency
13713. F13713 Curriculum-only — availability and consistency in practice
13714. F13714 Distributed Systems & Cloud — cyclic redundancy check
13715. F13715 Operating Systems — availability and replication
13716. F13716 Curriculum-only — externally consistent distributed transaction
13717. F13717 Data Mining & Databases — parallel database
13718. F13718 Distributed Systems & Cloud — raft
13719. F13719 Curriculum-only — raft group
13720. F13720 Distributed Systems & Cloud — paxo and raft
13721. F13721 Operating Systems — journaling
13722. F13722 Other/Unknown — statistical analysis
13723. F13723 Cryptography & Security — economic model
13724. F13724 Curriculum-only — statistical-method
13725. F13725 Computer Networks — blind source separation
13726. F13726 Curriculum-only — k-mean clustering as covered in the statistical-method
13727. F13727 Data Mining & Databases — coefficient of determination
13728. F13728 ML & AI — latent variable
13729. F13729 Curriculum-only — projected gradient algorithm
13730. F13730 Mathematics — projected gradient descent
13731. F13731 ML & AI — bregman
13732. F13732 NLP & Speech — statistical machine translation
13733. F13733 Other/Unknown — logistics
13734. F13734 Mathematics — lunar
13735. F13735 Algorithms & Theory of CS — lunar surface
13736. F13736 Mathematics — nonlinear pde
13737. F13737 Other/Unknown — reverse logistics
13738. F13738 Computer Networks — software quality assurance
13739. F13739 Curriculum-only — quality assurance and control
13740. F13740 Other/Unknown — variable model
13741. F13741 Algorithms & Theory of CS — random variable model
13742. F13742 Signal/Image/Audio/Video Processing — characteristic strip expansion
13743. F13743 Software Engineering — lockheed martin astronautics
13744. F13744 Distributed Systems & Cloud — streaming
13745. F13745 Algorithms & Theory of CS — streaming algorithm
13746. F13746 Computer Networks — streaming videos
13747. F13747 Curriculum-only — numerical care that streaming
13748. F13748 Data Mining & Databases — streaming database
13749. F13749 Distributed Systems & Cloud — data streaming
13750. F13750 Curriculum-only — data streaming platform for fast data
13751. F13751 Distributed Systems & Cloud — late data in streaming
13752. F13752 Other/Unknown — peer-to-peer streaming
13753. F13753 Software Engineering — pipeline parallelism
13754. F13754 Curriculum-only — software reliability growth model
13755. F13755 Software Engineering — software requirement
13756. F13756 Algorithms & Theory of CS — delete max
13757. F13757 Distributed Systems & Cloud — bitonic
13758. F13758 Software Engineering — bitonic sequence
13759. F13759 Distributed Systems & Cloud — indirection
13760. F13760 Software Engineering — Levels of indirection, illustrated by virtual memory for managing physical memory resources
13761. F13761 Algorithms & Theory of CS — quicksort analysis
13762. F13762 Curriculum-only — quicksort and its partition
13763. F13763 Software Engineering — source file
13764. F13764 Curriculum-only — staff estimation
13765. F13765 Distributed Systems & Cloud — administrative staff
13766. F13766 Data Mining & Databases — europe
13767. F13767 Distributed Systems & Cloud — fare fellow
13768. F13768 Curriculum-only — teaching isa
13769. F13769 Distributed Systems & Cloud — technical staff
13770. F13770 Mathematics — collaboration
13771. F13771 ML & AI — handwritten digit recognition
13772. F13772 Mathematics — policy on collaboration
13773. F13773 Curriculum-only — curriculum teach
13774. F13774 Distributed Systems & Cloud — willing to teach
13775. F13775 Mathematics — worked
13776. F13776 Curriculum-only — generic lru cache as the worked
13777. F13777 Operating Systems — supporting staff
13778. F13778 Other/Unknown — faculty
13779. F13779 Data Mining & Databases — academics
13780. F13780 Mathematics — internship
13781. F13781 Other/Unknown — faculty member
13782. F13782 Cryptography & Security — faculty member interested
13783. F13783 Mathematics — detailed
13784. F13784 Computer Networks — detailed report
13785. F13785 Data Mining & Databases — detailed syllabus
13786. F13786 ML & AI — detailed balance
13787. F13787 Mathematics — balance equation
13788. F13788 ML & AI — detailed balance equation
13789. F13789 Mathematics — habit
13790. F13790 Curriculum-only — habit of stating
13791. F13791 Other/Unknown — detailed design
13792. F13792 Computer Networks — social-media post
13793. F13793 Data Mining & Databases — Social media networks
13794. F13794 Other/Unknown — supervisor
13795. F13795 Computer Architecture — supervisor call
13796. F13796 Curriculum-only — supervisor and director
13797. F13797 Signal/Image/Audio/Video Processing — department and faculty
13798. F13798 Software Engineering — level of abstraction
13799. F13799 Algorithms & Theory of CS — total time
13800. F13800 Curriculum-only — cycle stealing
13801. F13801 Distributed Systems & Cloud — barbara
13802. F13802 Information Theory & Coding — slack stealing
13803. F13803 Software Engineering — param
13804. F13804 Curriculum-only — integration and system testing
13805. F13805 Software Engineering — team
13806. F13806 Computer Architecture — team formation
13807. F13807 Computer Networks — Team processes - responsibilities for tasks, effort estimation, meeting structure, work schedule
13808. F13808 Cryptography & Security — access team
13809. F13809 Curriculum-only — blue-team report covering prompt injection
13810. F13810 Data Mining & Databases — binary variable
13811. F13811 Curriculum-only — categorical variable with one level dropped
13812. F13812 Data Mining & Databases — form team
13813. F13813 Distributed Systems & Cloud — design team
13814. F13814 Mathematics — baseball
13815. F13815 Operating Systems — design system in team
13816. F13816 Other/Unknown — regulation
13817. F13817 Cryptography & Security — adverse
13818. F13818 Curriculum-only — adapt to adverse condition
13819. F13819 Distributed Systems & Cloud — affinity
13820. F13820 Curriculum-only — kelip affinity group with constant-hop lookup
13821. F13821 NLP & Speech — extraction
13822. F13822 Curriculum-only — model extraction
13823. F13823 Distributed Systems & Cloud — slp extraction algorithm
13824. F13824 ML & AI — text classification
13825. F13825 Mathematics — extraction of real
13826. F13826 NLP & Speech — information extraction
13827. F13827 Algorithms & Theory of CS — paragraph
13828. F13828 Computer Architecture — paragraph describing
13829. F13829 Curriculum-only — summarization of the kharagpur
13830. F13830 NLP & Speech — sentence extraction
13831. F13831 Curriculum-only — text summarization and dialog as nlp
13832. F13832 Operating Systems — institute regulation
13833. F13833 Other/Unknown — audit
13834. F13834 Curriculum-only — audit log
13835. F13835 Distributed Systems & Cloud — audit criterion
13836. F13836 Other/Unknown — energy audit
13837. F13837 Curriculum-only — india national cyber security policy
13838. F13838 Data Mining & Databases — history of india
13839. F13839 Distributed Systems & Cloud — els india
13840. F13840 Other/Unknown — indian
13841. F13841 Algorithms & Theory of CS — strictly better
13842. F13842 Computer Networks — agent observe
13843. F13843 Distributed Systems & Cloud — indian institute
13844. F13844 Curriculum-only — kanpur course close with the recap
13845. F13845 Distributed Systems & Cloud — home
13846. F13846 Computer Networks — supermarket
13847. F13847 Curriculum-only — limited-pointer directory at the home node
13848. F13848 Data Mining & Databases — home work
13849. F13849 Distributed Systems & Cloud — data center
13850. F13850 Curriculum-only — commodity cluster and the data-centre
13851. F13851 Distributed Systems & Cloud — clock synchronization in cloud data center
13852. F13852 Computer Networks — computer networking
13853. F13853 Curriculum-only — eh week and week networking
13854. F13854 Data Mining & Databases — competitor
13855. F13855 Distributed Systems & Cloud — cloud networking
13856. F13856 Curriculum-only — cloud networking on gcp
13857. F13857 Distributed Systems & Cloud — networking system
13858. F13858 Data Mining & Databases — Social networking sites
13859. F13859 Distributed Systems & Cloud — design of social networking
13860. F13860 Algorithms & Theory of CS — fault-tolerant consensus
13861. F13861 Cryptography & Security — byzantine fault-tolerant
13862. F13862 Curriculum-only — fault-tolerant cloud service
13863. F13863 Distributed Systems & Cloud — atomic object
13864. F13864 Curriculum-only — comparison with classical byzantine agreement
13865. F13865 Distributed Systems & Cloud — fault tolerant virtual machine
13866. F13866 Curriculum-only — byzantine failure and the byzantine
13867. F13867 Distributed Systems & Cloud — modeling and verification
13868. F13868 Algorithms & Theory of CS — lazy
13869. F13869 Data Mining & Databases — lazy algorithm
13870. F13870 Curriculum-only — lazy evaluation of argument
13871. F13871 Data Mining & Databases — lazy evaluator code
13872. F13872 Distributed Systems & Cloud — lazy list algorithm
13873. F13873 Information Theory & Coding — content distribution network
13874. F13874 ML & AI — hdw
13875. F13875 Distributed Systems & Cloud — exponential information gathering
13876. F13876 Mathematics — chinese
13877. F13877 Data Mining & Databases — chinese character
13878. F13878 Mathematics — lazy walk
13879. F13879 Algorithms & Theory of CS — restaurant location
13880. F13880 Computer Networks — chinese restaurant
13881. F13881 Mathematics — sell
13882. F13882 Computer Networks — buyer
13883. F13883 Cryptography & Security — invoice
13884. F13884 Data Mining & Databases — seat to sell
13885. F13885 ML & AI — peach
13886. F13886 Mathematics — profit
13887. F13887 Cryptography & Security — compliant
13888. F13888 Curriculum-only — profit scaling
13889. F13889 Data Mining & Databases — farmer
13890. F13890 Mathematics — expected profit
13891. F13891 NLP & Speech — coffee
13892. F13892 Curriculum-only — prep for the system design interview
13893. F13893 NLP & Speech — cortege
13894. F13894 NLP & Speech — underlying state
13895. F13895 Operating Systems — lazy allocation
13896. F13896 Other/Unknown — data center networking
13897. F13897 Curriculum-only — inter-data-center networking
13898. F13898 Other/Unknown — delay tolerant
13899. F13899 Curriculum-only — enhanced data model
13900. F13900 Other/Unknown — home networking
13901. F13901 Curriculum-only — real industrial data set are named
13902. F13902 Mathematics — industrial and applied
13903. F13903 Other/Unknown — bubble
13904. F13904 Operating Systems — pipeline bubble
13905. F13905 Other/Unknown — industrial automation
13906. F13906 Cryptography & Security — attack mitigation
13907. F13907 Curriculum-only — mitigation and data source
13908. F13908 Distributed Systems & Cloud — hotspot mitigation
13909. F13909 Curriculum-only — hotspot mitigation and live vm migration
13910. F13910 Distributed Systems & Cloud — hotspot mitigation for virtual machine migration
13911. F13911 Other/Unknown — phase space
13912. F13912 Curriculum-only — regional subnet with cidr
13913. F13913 Other/Unknown — regulation of gene expression
13914. F13914 Distributed Systems & Cloud — straggler mitigation strategy
13915. F13915 Other/Unknown — transportation system
13916. F13916 Computer Networks — airport
13917. F13917 Cryptography & Security — infrastructure
13918. F13918 Curriculum-only — core infrastructure
13919. F13919 Distributed Systems & Cloud — computing paradigm
13920. F13920 Mathematics — yeah
13921. F13921 NLP & Speech — mexico city
13922. F13922 Other/Unknown — mobile device
13923. F13923 Computer Networks — e-commerce
13924. F13924 Curriculum-only — routing and e-commerce
13925. F13925 Data Mining & Databases — customer relationship management
13926. F13926 Information Theory & Coding — telephone networks
13927. F13927 Other/Unknown — b2c e-commerce
13928. F13928 Computer Networks — radio frequency
13929. F13929 Data Mining & Databases — diploma
13930. F13930 Distributed Systems & Cloud — tech degree
13931. F13931 Other/Unknown — parking
13932. F13932 Curriculum-only — parking lot and chat
13933. F13933 Other/Unknown — vapor
13934. F13934 Signal/Image/Audio/Video Processing — alan
13935. F13935 Algorithms & Theory of CS — alan turing
13936. F13936 Mathematics — announced
13937. F13937 Data Mining & Databases — ceo
13938. F13938 Information Theory & Coding — reed
13939. F13939 Curriculum-only — reed and clark
13940. F13940 Information Theory & Coding — reed muller code
13941. F13941 Curriculum-only — reed solomon over gf
13942. F13942 Information Theory & Coding — list decoding of reed-solomon
13943. F13943 Signal/Image/Audio/Video Processing — alan willsky
13944. F13944 Software Engineering — better option
13945. F13945 Curriculum-only — distributed commit log
13946. F13946 Software Engineering — electronic data interchange
13947. F13947 Software Engineering — team version control
13948. F13948 Distributed Systems & Cloud — pthread
13949. F13949 Curriculum-only — exactly-once by idempotent producer
13950. F13950 Mathematics — largest producer of lightbulb
13951. F13951 Other/Unknown — aggregation
13952. F13952 Curriculum-only — aggregation and composition
13953. F13953 Curriculum-only — risk aggregation across the enterprise
13954. F13954 Data Mining & Databases — aggregation and grouping
13955. F13955 Other/Unknown — online aggregation
13956. F13956 Distributed Systems & Cloud — rdd lineage graph
13957. F13957 Curriculum-only — rank algorithm on spark with graphx
13958. F13958 Distributed Systems & Cloud — apache spark
13959. F13959 Curriculum-only — apache spark and resilient distributed dataset
13960. F13960 Distributed Systems & Cloud — learning spark
13961. F13961 Distributed Systems & Cloud — spark streaming
13962. F13962 Curriculum-only — spark streaming and its successor
13963. F13963 Distributed Systems & Cloud — stream processing
13964. F13964 Curriculum-only — stream processing and approximate algorithm
13965. F13965 Distributed Systems & Cloud — value-to-key design pattern
13966. F13966 ML & AI — training deep neural network
13967. F13967 Other/Unknown — Rank aggregation
13968. F13968 Software Engineering — intel threading building block
13969. F13969 Cryptography & Security — hash time-locked contract
13970. F13970 Software Engineering — mutex lock
13971. F13971 Curriculum-only — acid property and transaction state
13972. F13972 Software Engineering — transition system
13973. F13973 Mathematics — perm
13974. F13974 Software Engineering — spinlock
13975. F13975 Operating Systems — struct spinlock
13976. F13976 Software Engineering — superblock
13977. F13977 Curriculum-only — superblock scheduling
13978. F13978 Software Engineering — undo
13979. F13979 Curriculum-only — undo recovery
13980. F13980 Data Mining & Databases — undo and redo
13981. F13981 Curriculum-only — undo and redo information
13982. F13982 Data Mining & Databases — undo pass
13983. F13983 Curriculum-only — redo and undo pass
13984. F13984 Software Engineering — unlock
13985. F13985 Curriculum-only — unlock ns
13986. F13986 Software Engineering — pthread mutex unlock
13987. F13987 Cryptography & Security — txs
13988. F13988 Mathematics — fund
13989. F13989 Cryptography & Security — endowment
13990. F13990 ML & AI — previous state
13991. F13991 Mathematics — hedge
13992. F13992 ML & AI — bandit feedback
13993. F13993 Mathematics — revealing
13994. F13994 Signal/Image/Audio/Video Processing — endowment gift
13995. F13995 Software Engineering — added sequentially
13996. F13996 Information Theory & Coding — dlc
13997. F13997 Software Engineering — fund txout
13998. F13998 Curriculum-only — template and visitor
13999. F13999 Software Engineering — waterfall
14000. F14000 Curriculum-only — iterative waterfall
14001. F14001 Software Engineering — web crawler
14002. F14002 Curriculum-only — scalable web crawler like google
14003. F14003 Software Engineering — Web interfaces
14004. F14004 Computer Networks — wired lan
14005. F14005 Information Theory & Coding — wired and wireless
14006. F14006 Mathematics — wired magazine
14007. F14007 Software Engineering — workout
14008. F14008 Curriculum-only — wrap-up of the tcp
14009. F14009 Software Engineering — yi ai
14010. F14010 Computer Architecture — zip file contain
14011. F14011 System Design Primer / Availability patterns — active-passive
14012. F14012 Curriculum-only — active-passive or active-active pair
14013. F14013 System Design Primer / Cache — caching at the database query level
14014. F14014 System Design Primer / Communication — Hypertext transfer protocol (HTTP)
14015. F14015 System Design Primer / Consistency patterns — eventual consistency
14016. F14016 System Design Primer / Database — master-slave replication
14017. F14017 Curriculum-only — database sharding
14018. F14018 Distributed Systems & Cloud — auto sharding
14019. F14019 System Design Primer / Database — denormalisation
14020. F14020 Curriculum-only — denormalisation for performance
14021. F14021 System Design Primer / Database — graph database
14022. F14022 Curriculum-only — graph database and big data

## Noise-flagged topic appendix — retained for reconciliation

14023. N0001 NOISE APPENDIX — Mathematics — de nition
14024. N0002 NOISE APPENDIX — Information Theory & Coding — signi cant
14025. N0003 NOISE APPENDIX — Mathematics — press
14026. N0004 NOISE APPENDIX — ML & AI — di erent type
14027. N0005 NOISE APPENDIX — Software Engineering — copyright
14028. N0006 NOISE APPENDIX — Mathematics — cambridge
14029. N0007 NOISE APPENDIX — Algorithms & Theory of CS — con guration
14030. N0008 NOISE APPENDIX — Mathematics — office hour
14031. N0009 NOISE APPENDIX — Other/Unknown — crc press
14032. N0010 NOISE APPENDIX — Mathematics — th century
14033. N0011 NOISE APPENDIX — Other/Unknown — oxford university press
14034. N0012 NOISE APPENDIX — Mathematics — cambridge university press
14035. N0013 NOISE APPENDIX — Signal/Image/Audio/Video Processing — fourier coe cient
14036. N0014 NOISE APPENDIX — Software Engineering — copyright restriction
14037. N0015 NOISE APPENDIX — Mathematics — su cient
14038. N0016 NOISE APPENDIX — Other/Unknown — mcgraw hill
14039. N0017 NOISE APPENDIX — Mathematics — prentice hall
14040. N0018 NOISE APPENDIX — Other/Unknown — academic press
14041. N0019 NOISE APPENDIX — Algorithms & Theory of CS — copyright brian william
14042. N0020 NOISE APPENDIX — Mathematics — princeton university press
14043. N0021 NOISE APPENDIX — Signal/Image/Audio/Video Processing — nd order
14044. N0022 NOISE APPENDIX — Mathematics — nd edition
14045. N0023 NOISE APPENDIX — Other/Unknown — addison wesley
14046. N0024 NOISE APPENDIX — Software Engineering — ef cient
