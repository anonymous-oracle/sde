# Ingestion note 2: computer-architecture source (`cloud-computing2.txt`), for the unified cloud curriculum

**Status:** ingested and analysed on 2026-11-04 (UTC); **not yet authored into units**. This note holds everything needed to resume: the cell table, the overlap analysis, the planned domain D14 with its units, source cells and assignment focus, the open decisions and the anomalies. The unified file `unified_cloud_curriculum.md` is unchanged (13 domains, 138 units, 132 assignments).

**Source:** `cloud-computing2.txt`, 247 lines, **6 NPTEL course outlines, all on computer architecture** (the file name says cloud computing; the content is not). 78 cells (6 outlines and 72 weeks), every one mapped to at least one planned unit (checked by script).

## 1. Source course index

| Key | Course | Instructor / institution (course id) | Source lines | Cells |
|---|---|---|---|---|
| MCA | Multi-Core Computer Architecture | John Jose, IIT Guwahati (NPTEL 106103184) | 18–41 | 13 |
| CAO | Computer Architecture and Organization | Indranil Sengupta and Kamalika Datta, IIT Kharagpur (NPTEL 106105163) | 64–88 | 13 |
| CA | Computer Architecture | Smruti Ranjan Sarangi, IIT Delhi (NPTEL 106102157) | 113–136 | 13 |
| ACA | Advanced Computer Architecture | Smruti R. Sarangi, IIT Delhi | 151–169 | 13 |
| PCA | Parallel Computer Architecture | Hemangee K. Kapoor, IIT Guwahati | 179–215 | 13 |
| GPU | GPU Architectures and Programming | Soumyajit Dey, IIT Kharagpur | 225–247 | 13 |

The keys do not clash with the 13 existing keys (ACA is Advanced Computer Architecture and ADS stays Advanced Distributed Systems).

## 2. What the six courses cover, and how they overlap

- **Three layers of the same subject.** Introductory (CA, CAO): number systems, assembly, arithmetic, datapath and control, pipelining, caches, virtual memory, I/O. Advanced (MCA, ACA, PCA): out-of-order cores and speculation, cache design and coherence, memory models and synchronisation, DRAM, on-chip networks, power and reliability. Accelerators (GPU, plus MCA weeks 5 and 12): SIMT, CUDA, OpenCL, neural-network kernels.
- **Heaviest overlaps (merge into one unit each, every week cited):** pipelining and hazards (MCA 2–3, CAO 11, CA 9–10, ACA 1–3, GPU 1); caches (MCA 6–7, CAO 5–6, CA 11, ACA 7, PCA 3); cache coherence (MCA 8, ACA 10, PCA 4–9); memory consistency (ACA 9, PCA 10, MCA 8); on-chip networks (MCA 10–12, ACA 8, PCA 12); ISA and assembly (MCA 1, CAO 2, CA 4–5); GPU architecture (MCA 5, GPU 2, 5).
- **Already partly in the unified file** (the new units extend or link, not repeat): U4.1 (operating systems and architecture bridge, with the TLB and effective-access-time formula), U3.3 (switch fabrics), U3.10 (fat trees and Clos), U9.9 and U9.16 (distributed shared memory and consistency), U10.6 (cache hit ratio under Zipf), U11.1 (Amdahl and Gustafson), U6.9 and U5.20 (hardware and side-channel security), U3.6 (QoS), U12.3 (machine learning on the cloud).
- **Where it belongs.** Appending as **D14** (Part F) keeps every existing identifier stable. Read it after U4.1; the on-chip-network unit reuses U2.7 and U3.3, the coherence and consistency units pair with U9.16, and the GPU units pair with U11.9 and U12.3. If you prefer it beside compute, the same units can move into Part A at the next merge.

## 3. Cell table (line ranges in `cloud-computing2.txt`)

| Cell | Lines | Text (first words) | Planned unit(s) |
|---|---|---|---|
| MCA:o | 18 | The use of mobile gadgets and applications is crucial to maintaining c | U14.13 |
| MCA:W1 | 30 | Week 1	Basic Computer Organization: Review of Basic Computer Organizat | U14.2 |
| MCA:W2 | 31 | Week 2	Instruction Pipeline Principles: Performance Evaluation Methods | U14.3, U14.6 |
| MCA:W3 | 32 | Week 3	Pipeline Hazards and Branch Prediction Techniques: Pipeline Haz | U14.6, U14.7 |
| MCA:W4 | 33 | Week 4	Pipeline Scheduling and Speculative execution: Compiler Techniq | U14.7 |
| MCA:W5 | 34 | Week 5	Superscalar Processors and GPU architectures: Advanced Pipelini | U14.8, U14.17 |
| MCA:W6 | 35 | Week 6	Cache Memory Principles Introduction to Cache Memory, Block Rep | U14.9 |
| MCA:W7 | 36 | Week 7	Cache Memory Optimizations Design issues for improving memory a | U14.9 |
| MCA:W8 | 37 | Week 8	Cache Coherence Protocols Cache coherence and memory consistenc | U14.14, U14.15 |
| MCA:W9 | 38 | Week 9	Primary Storage Systems Introduction to DRAM System, DRAM organ | U14.11 |
| MCA:W10 | 39 | Week 10	Tiled Chip Multi-Core Processors & Network-on-Chip Tiled Chip  | U14.16 |
| MCA:W11 | 40 | Week 11	Energy Efficient NoCs Introduction to deflection routing, Ener | U14.16 |
| MCA:W12 | 41 | Week 12	Quality of Service for TCMPs QoS of NoC and Caches in TCMPs, E | U14.20, U14.21 |
| CAO:o | 64–65 | This course will discuss the basic concepts of computer architecture a | U14.2 |
| CAO:W1 | 77 | Week 1	Evolution of Computer Systems | U14.1 |
| CAO:W2 | 78 | Week 2	Instruction Set Architecture | U14.2 |
| CAO:W3 | 79 | Week 3	Quantitative Principles of Computer Design | U14.3 |
| CAO:W4 | 80 | Week 4	Control Unit Design | U14.5 |
| CAO:W5 | 81 | Week 5	Memory System Design | U14.9 |
| CAO:W6 | 82 | Week 6	Design of Cache Memory Systems | U14.9 |
| CAO:W7 | 83 | Week 7	Design of Arithmetic Unit | U14.4 |
| CAO:W8 | 84 | Week 8	Design of Arithmetic Unit (contd.) | U14.4 |
| CAO:W9 | 85 | Week 9	Input-Output System Design | U14.12 |
| CAO:W10 | 86 | Week 10	Input-Output System Design (contd.) | U14.12 |
| CAO:W11 | 87 | Week 11	Instruction Set Pipelining | U14.6 |
| CAO:W12 | 88 | Week 12	Parallel Processing Architectures | U14.13 |
| CA:o | 113 | This is an introductory computer architecture course for beginners. We | U14.1 |
| CA:W1 | 125 | Week 1	Introduction to Computing | U14.1 |
| CA:W2 | 126 | Week 2	Number Systems | U14.1 |
| CA:W3 | 127 | Week 3	Floating Point Numbers | U14.4 |
| CA:W4 | 128 | Week 4	Assembly Language – I | U14.2 |
| CA:W5 | 129 | Week 5	Assembly Language – II | U14.2 |
| CA:W6 | 130 | Week 6	Algorithms for Binary Addition | U14.4 |
| CA:W7 | 131 | Week 7	Algorithms for Multiplication and Division | U14.4 |
| CA:W8 | 132 | Week 8	Processor Design | U14.5 |
| CA:W9 | 133 | Week 9	Pipelining – I | U14.6 |
| CA:W10 | 134 | Week 10	Pipelining – II | U14.6 |
| CA:W11 | 135 | Week 11	Memory Systems – Caches | U14.9 |
| CA:W12 | 136 | Week 12	Virtual Memory | U14.10 |
| ACA:o | 151–156 | This course is on Advanced Computer Architecture. It will introduce st | U14.11, U14.21, U14.22 |
| ACA:W1 | 158 | Week 1: In-order pipelines overview | U14.6 |
| ACA:W2 | 159 | Week 2: Out-of-order pipelines, Branch prediction | U14.6, U14.7 |
| ACA:W3 | 160 | Week 3: Advanced branch prediction techniques | U14.6 |
| ACA:W4 | 161 | Week 4: Issue, select, and commit | U14.7 |
| ACA:W5 | 162 | Week 5: Aggressive speculation | U14.7 |
| ACA:W6 | 163 | Week 6: Compiler techniques for enhancing ILP | U14.7 |
| ACA:W7 | 164 | Week 7: Caches: Design, modeling, and optimizations | U14.9 |
| ACA:W8 | 165 | Week 8: On-chip networks | U14.16 |
| ACA:W9 | 166 | Week 9: Theory of memory models | U14.15 |
| ACA:W10 | 167 | Week 10: Coherence Protocols | U14.14 |
| ACA:W11 | 168 | Week 11: Low power design | U14.22 |
| ACA:W12 | 169 | Week 12: Reliability and Hardware Security | U14.22 |
| PCA:o | 179–189 | With the emergence of application domains requiring large data process | U14.13 |
| PCA:W1 | 203 | Week 1 : Introduction to Parallel Architectures | U14.13 |
| PCA:W2 | 204 | Week 2 : Parallel Programming models and Architectures | U14.13 |
| PCA:W3 | 205 | Week 3 : Memory Hierarchy-Cache and Virtual memory | U14.9, U14.10 |
| PCA:W4 | 206 | Week 4 : Overview of Cache coherence, Coherence Protocols- Snooping, D | U14.14 |
| PCA:W5 | 207–208 | Week 5 : MSI, MESI, Dragon protocol and Correctness of coherence proto | U14.14 |
| PCA:W6 | 209 | Week 6 : Snoop based muliprocessor design, Single and multi-level cach | U14.14 |
| PCA:W7 | 210 | Week 7 : Snoop based muliprocessor design, Single and multi-level cach | U14.14 |
| PCA:W8 | 211 | Week 8 : Scalable shared memory systems: Directory coherence protocols | U14.14 |
| PCA:W9 | 212 | Week 9 : Case study: Origin- Architecture, protocol, correctness; Sequ | U14.14 |
| PCA:W10 | 213 | Week 10 : Memory consistency models- Sequential, Relaxed consistency m | U14.15 |
| PCA:W11 | 214 | Week 11 : Synchronization- LL-SC, point to point, barrier synchronizat | U14.15 |
| PCA:W12 | 215 | Week 12 : Interconnects- Introduction, Topologies, routing, flow contr | U14.16 |
| GPU:o | 225–233 | The course covers basics of conventional CPU architectures, their exte | U14.18 |
| GPU:W1 | 235–236 | Week 1: Review of Traditional Computer Architecture – Basic five stage | U14.2, U14.8 |
| GPU:W2 | 237 | Week 2: GPU architectures - Streaming Multi Processors, Cache Hierarch | U14.17 |
| GPU:W3 | 238 | Week 3: Introduction to CUDA programming | U14.18 |
| GPU:W4 | 239 | Week 4: Multi-dimensional mapping of dataspace, Synchronization | U14.18 |
| GPU:W5 | 240 | Week 5: Warp Scheduling, Divergence | U14.17 |
| GPU:W6 | 241 | Week 6: Memory Access Coalescing | U14.18 |
| GPU:W7 | 242 | Week 7: Optimization examples : optimizing Reduction Kernels | U14.18 |
| GPU:W8 | 243 | Week 8: Optimization examples : Kernel Fusion, Thread and Block | U14.18 |
| GPU:W9 | 244 | Week 9: OpenCL basics | U14.19 |
| GPU:W10 | 245 | Week 10: OpenCL for Heterogeneous Computing | U14.19 |
| GPU:W11 | 246 | Week 11: Application Design : Efficient Neural Network Training/Infere | U14.20 |
| GPU:W12 | 247 | Week 12: Application Design : Efficient Neural Network Training/Infere | U14.20 |

## 4. Planned domain D14: Computer architecture and parallel hardware

**Aim:** from the gate and the instruction to the multicore chip, the memory system, the on-chip network, the GPU and the accelerator, with every mechanism built as a simulator in Python and checked against hand calculation or a library. Benchmarks (recalled, not checked), taken from the sources' own lists: Hennessy and Patterson, *Computer Architecture: A Quantitative Approach* (5th ed.) and *Computer Organization and Design*; Jacob, Ng and Wang, *Memory Systems*; Dally and Towles, *Principles and Practices of Interconnection Networks*; Stallings; Hamacher, Vranesic and Zaky; Hayes; Sarangi, *Computer Organisation and Architecture*.

**Assignments:** every unit below except the capstone will carry the same five-question NPTEL-style assignment as the existing 132 (MCQ, multiple select, numerical computed by script, prove or derive, programming; 10 marks; pass at 7/10; key collapsed), numbered A14.1 to A14.22. The assignment focus for each unit is fixed in the table so the authoring can start directly.

| Unit | Title | Type | Source cells | Links | Assignment focus (A14.n) | Build (all [local] unless stated) |
|---|---|---|---|---|---|---|
| U14.1 | Bridge: binary representation, number systems and digital logic | bridge | CA:o,W1,2;CAO:W1 | builds on U5.2 (mod n arithmetic), U2.11 (GF(2)) | two's and one's complement, overflow, gates to adders, state machines; numerical: range and overflow cases | bit-level ALU and a gate-level simulator in Python, checked against Python integers |
| U14.2 | Instruction set architecture: addressing modes, encoding, CISC versus RISC, assembly | unit | MCA:W1;CAO:o,W2;CA:W4,5;GPU:W1 | extends U4.1 | encoding and decoding by hand, assembler arithmetic; programming: an assembler and emulator for a small RISC ISA | assembler plus emulator for a MIPS- or RISC-V-like subset, tested on small programs |
| U14.3 | Performance evaluation and the quantitative principles of design | unit | MCA:W2;CAO:W3 | Amdahl already in U11.1; reuses U2.1 | CPI, MIPS, speed-up, Amdahl and Gustafson cases, benchmark means (arithmetic, harmonic, geometric) | a performance calculator and a trace-driven CPI estimator |
| U14.4 | Computer arithmetic: IEEE 754 floating point, adders, multipliers and dividers | unit | CA:W3,6,7;CAO:W7,8 | builds on U14.1 | carry-lookahead depth, Booth recoding, IEEE rounding cases; programming: floating-point add and multiply from scratch checked against NumPy | soft-float add, multiply and divide with all rounding modes against hardware floats |
| U14.5 | Processor datapath and control unit design: single-cycle, multi-cycle and microprogrammed | unit | CA:W8;CAO:W4 | builds on U14.2 | control-signal tables, CPI of multi-cycle design; programming: datapath simulator with hard-wired and microcoded control | datapath simulator running the emulator's programs with cycle counts |
| U14.6 | Instruction pipelining: hazards, forwarding, stalls and branch prediction | unit | MCA:W2,3;CAO:W11;CA:W9,10;ACA:W1,2,3 | uses U2.1 (Markov view of predictors) | hazard classification, speed-up with stalls, predictor accuracy on a trace; programming: five-stage pipeline simulator with forwarding and a two-bit, gshare and tournament predictor | pipeline simulator, branch-predictor suite compared on synthetic and recorded traces |
| U14.7 | Instruction-level parallelism: scoreboarding, Tomasulo, speculation, reorder buffer, compiler techniques | unit | MCA:W3,4;ACA:W2,4,5,6 | none new | Tomasulo trace by hand, ROB recovery, loop unrolling and software pipelining gains; programming: Tomasulo with reorder buffer | out-of-order core simulator with precise exceptions checked against the in-order one |
| U14.8 | Superscalar, multithreading, hyperthreading and SIMD | unit | MCA:W5;GPU:W1 | none new | issue-width limits, SMT throughput, vector-length arithmetic; programming: a superscalar issue model and a SIMD kernel in NumPy | issue-width and SMT experiments on synthetic instruction mixes |
| U14.9 | Memory hierarchy I: cache principles, replacement, write policies, design and optimisation | unit | MCA:W6,7;CAO:W5,6;CA:W11;ACA:W7;PCA:W3 | links to U10.6 (cache hit-ratio model) and U3.11 | AMAT, miss classification, associativity trade-off; programming: a configurable cache simulator with LRU, FIFO, random, write-back and write-through, prefetch, victim cache | cache simulator validated on hand-computed traces and a Zipf workload against the analytic model |
| U14.10 | Virtual memory: page tables, TLBs, protection and the hardware-software boundary | unit | CA:W12;PCA:W3 | extends U4.1 and U4.2 | multi-level table walk cost, TLB reach, page-fault service time; programming: MMU and TLB simulator with demand paging | MMU simulator reproducing the U4.1 effective-access-time formula |
| U14.11 | Main memory: DRAM organisation, controllers, address mapping and scheduling | unit | MCA:W9;ACA:o | none new | row-buffer hit-rate arithmetic, address-mapping bit slicing, bank-level parallelism; programming: DRAM controller simulator with FR-FCFS scheduling | DRAM timing simulator and address-mapping explorer |
| U14.12 | Input-output system design: buses, interrupts, DMA and storage interfaces | unit | CAO:W9,10 | none new | bus bandwidth, DMA versus programmed I/O cost, interrupt latency; programming: a bus-and-DMA simulator | device, DMA controller and interrupt model driving the emulator |
| U14.13 | Parallel architectures and programming models: shared memory, message passing and data parallel | unit | PCA:o,W1,2;CAO:W12;MCA:o | links to U9.9 (distributed shared memory) | Flynn taxonomy, speed-up and efficiency, scaling laws; programming: shared-memory and message-passing versions of a kernel with multiprocessing | parallel kernels with measured speed-up against Amdahl |
| U14.14 | Cache coherence: snooping, directory protocols, MSI, MESI, Dragon, split-transaction buses, Origin and NUMA-Q | unit | MCA:W8;ACA:W10;PCA:W4,5,6,7,8,9 | links to U9.16 and U9.9 | protocol state traces, directory storage cost, correctness invariants; programming: protocol state machines checked by an exhaustive model checker on two and three cores | MSI, MESI and a directory protocol with an invariant checker and false-sharing experiment |
| U14.15 | Memory consistency models and synchronisation primitives | unit | ACA:W9;PCA:W10,11;MCA:W8 | links to U9.1 (partial orders), U9.16 | litmus tests, which outcomes each model allows; programming: a litmus-test enumerator for SC, TSO and a relaxed model, LL/SC and barrier implementations | litmus enumerator reproducing the allowed-outcome tables |
| U14.16 | On-chip networks and interconnects: topologies, routing, flow control, router microarchitecture, deflection and bufferless routing | unit | MCA:W10,11;ACA:W8;PCA:W12 | reuses U2.7 (graphs), U3.3 (switch fabrics), U3.10 (Clos and fat tree), U4.5 (flows) | diameter and bisection of topologies, deadlock freedom by turn model, latency model; programming: cycle-accurate mesh NoC simulator with XY, adaptive and deflection routing | NoC simulator with latency-versus-load curves and a deadlock checker |
| U14.17 | GPU architecture: streaming multiprocessors, SIMT execution, warp scheduling and divergence, cache hierarchy, graphics pipeline | unit | MCA:W5;GPU:W2,5 | none new | warp occupancy arithmetic, divergence cost; programming: SIMT execution simulator with a reconvergence stack | SIMT simulator showing divergence cost on branching kernels |
| U14.18 | GPU programming and optimisation: CUDA, thread mapping, synchronisation, coalescing, reductions, kernel fusion | unit | GPU:o,W3,4,6,7,8 | none new | index mapping, coalescing efficiency, reduction step counts; programming: kernels in Numba CUDA or a CPU emulator, with a coalescing analyser | reduction and matrix-multiply kernels with a memory-transaction model; GPU runs optional [credit] |
| U14.19 | OpenCL and heterogeneous computing | unit | GPU:W9,10 | none new | work-item and work-group mapping, data-transfer cost; programming: PyOpenCL kernels on CPU runtimes | the same kernels run through OpenCL on the CPU device and compared with the CUDA versions |
| U14.20 | Domain-specific accelerators and efficient neural-network training and inference | unit | MCA:W12;GPU:W11,12 | links to U11.8 and U12.3 | roofline model, arithmetic intensity, systolic-array utilisation, quantisation error; programming: a systolic-array simulator and a roofline analyser | accelerator simulator mapped to a small CNN layer, with energy and throughput model |
| U14.21 | Quality of service for caches and networks on chip, and emerging directions | unit | MCA:W12;ACA:o | links to U3.6 (QoS) | way-partitioning and weighted arbitration arithmetic, fairness metrics; programming: a QoS arbiter for the NoC simulator | latency isolation shown on a mixed workload |
| U14.22 | Low-power design, reliability and hardware security | unit | ACA:W11,12;ACA:o | links to U6.9 (hardware security), U5.20 (side channels) | dynamic power CV^2 f and DVFS arithmetic, ECC and MTTF; programming: Hamming ECC for a cache line and a power-model explorer; hardware-security items are defensive models only | ECC and power model; a cache side-channel model in simulation only, never against real systems |
| U14.23 | Capstone: a multicore simulator (pipeline, caches, coherence and a NoC) running a parallel kernel | capstone | none (assembles earlier units) | assembles U14.2 to U14.16 | project with acceptance criteria, no assignment | integration of the earlier simulators |

Totals: 23 units (1 bridge, 21 content, 1 capstone) and 22 assignments planned. After authoring the corpus becomes 14 domains, 161 units and 154 assignments.

Just-in-time bridges: U14.1 (binary and logic) before the first unit; probability for predictors and performance reuses U2.1; graph facts for topologies reuse U2.7; partial orders for memory models reuse U9.1. No further bridge is expected.

## 5. Safety, tooling and cost

- All builds are simulators in Python (the default toolbox), so **[local]** throughout. CUDA and OpenCL units run through Numba's CUDA simulator or PyOpenCL on a CPU device; a real GPU is optional and tagged **[credit]**, with a budget alert and the teardown written first.
- Hardware security in U14.22 is defensive: cache side channels and fault models appear as simulations only, never against real hardware or any system you do not own (Master Rules 11). No exploit code.
- The sources list C or C++ as a prerequisite; the builds use Python, and CUDA units use Python bindings (inferred, as for the earlier DS source).

## 6. Anomalies in the source (kept visible)

| Where | Issue | Handling |
|---|---|---|
| File name | `cloud-computing2.txt` holds computer-architecture courses, not cloud courses | Treated as the architecture extension of the cloud curriculum; confirm the placement in section 7. |
| MCA:W5 | Week 5 mentions GPU architectures; the GPU course also covers them | Merged in U14.17 with both cited. |
| CAO:W11 | Titled 'Instruction Set Pipelining'; instruction pipelining is meant | Taught in U14.6; the source wording is quoted. |
| PCA:W6, W7 | 'muliprocessor' typo | Meaning taken from context. |
| PCA outline | 'networkon-chip', 'specically' (typos) and an instructor biography at lines 190–201 that is not course content | Biography not cited as content; typos read from context. |
| CAO books | 'Morgan Koffman' for Morgan Kaufmann | Spelled correctly in the unit; source spelling noted. |
| ACA prerequisites | Lists Python, Java and generic data-structures NPTEL courses as prerequisites | Recorded in the prerequisite map; Python is the build language here. |
| GPU:W11, W12 | Same title twice ('contd.') | One unit, both weeks cited. |

## 7. Decisions I need from you

1. **Placement:** append as D14 (recommended, keeps IDs stable), or move beside Part A at the next merge.
2. **Scope of the GPU units:** simulator-only (recommended, no spend), or include optional real-GPU labs on credit.
3. **Assembly language:** MIPS-like, RISC-V-like or a custom small ISA for U14.2 and the simulators (the sources use a generic RISC; the IIT Kharagpur course says a popular RISC platform without naming it).
4. **Authoring:** unit files, the 22 assignments with scripted numerical keys, and the final coverage check are the remaining work; they were deferred because of your usage limit.

## 8. Weekly assignments: how the cadence works

NPTEL sets one assignment per week. Here each unit carries one assignment, and a unit spans one to several source weeks, so every source week is covered by at least one assignment: Appendix B of the unified file maps each source week to its units, and each unit ends with its assignment. For this source, section 3 above gives the same map in advance (cell to unit; assignment A14.n for unit U14.n). If you want a strict one-assignment-per-week layout for any course, say which and it can be generated from the cell table without changing the units.

