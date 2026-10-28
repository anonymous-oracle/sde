# Part 02 · Computer Organization & Data Representation · TOPIC LIST

Rules and directives for this part: `index/part02_computer_organization.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Computer Organization & Data Representation

### Data representation

- **Number systems**
  - Bits and bytes; why computers use base 2
  - Binary and hexadecimal; positional notation (a numeral dₖ…d₀ in base b is Σ dᵢ·bⁱ)
  - Base conversion by repeated division, and why it terminates
  - Two's complement as arithmetic modulo 2ⁿ: one adder for signed and unsigned values; range −2ⁿ⁻¹ … 2ⁿ⁻¹−1; signed overflow when the carry into the sign bit differs from the carry out; sign extension
  - Bit identities: `x & (x−1)` clears the lowest set bit; power-of-two test
- **Storage units**
  - Binary versus decimal prefixes (KiB, MiB, GiB versus KB, MB, GB) and the gap that shows up on cloud storage bills
  - Powers of two to remember: 2⁷ = 128, 2⁸ = 256, 2¹⁰ ≈ 1 thousand, 2¹⁶ = 65,536, 2²⁰ ≈ 1 million, 2³⁰ ≈ 1 billion, 2³² ≈ 4.3 billion (the IPv4 address space, a 32-bit integer's range), 2⁴⁰ ≈ 1 trillion
- **Character encoding**
  - ASCII; UTF-8 as a variable-length prefix code that is ASCII-compatible and self-synchronizing
  - Why encoding matters in data pipelines
- **Data layout**
  - Endianness and network byte order
  - Alignment and padding
- **Error detection**
  - Parity
  - The cyclic redundancy check as polynomial division over GF(2)
  - What each detects, and why neither authenticates

### Digital logic

- **Boolean logic**
  - AND, OR, NOT, XOR and truth tables; the same logic in IAM policy evaluation, firewall rules and CPU design
  - Boolean algebra laws: identity, complement, distributive, De Morgan
  - Sum-of-products and product-of-sums canonical forms
  - Functional completeness of NAND alone and of NOR alone
  - Karnaugh-map minimization up to four variables
- **Combinational circuits**
  - Half and full adders
  - The n-bit ripple-carry adder (O(n) delay) and carry-lookahead (O(log n) delay)
  - Multiplexers and decoders
- **Sequential logic**
  - The SR latch, the D flip-flop and registers
  - The clock; setup and hold constraints
  - Finite-state machines, Moore versus Mealy

### Machine organization

- **Instruction set architecture**
  - The RISC-V RV32I base: 32 registers, load/store, arithmetic, branches, `jal`/`jalr`
  - How a function becomes instructions: calling convention, stack frame, caller-saved and callee-saved registers
  - The fetch–decode–execute cycle and a single-cycle datapath; the control unit that reads the opcode and function fields to set the datapath's multiplexer selects, ALU operation and memory and register-write enables, realized either as hardwired logic or as a microprogram; the multicycle datapath, which reuses one ALU and one memory port over several clock cycles per instruction, trading a longer instruction time for less hardware
- **Performance laws**
  - The iron law: CPU time = instruction count × cycles per instruction × clock period
  - Amdahl's law: speedup = 1 / ((1 − p) + p/s), bounded by 1/(1 − p)
  - The five-stage pipeline; structural, data and control hazards; forwarding; branch prediction
- **The memory hierarchy**
  - SRAM, DRAM, flash and disk
  - Temporal and spatial locality
  - Cache organization: direct-mapped, set-associative, fully associative; the tag, index and offset of an address
  - Write-through versus write-back
  - The three Cs of misses: compulsory, capacity, conflict
  - Average memory access time: AMAT = hit time + miss rate × miss penalty, level by level
  - Virtual memory and the TLB from the hardware side
- **Latency numbers**
  - L1 0.5 ns · branch mispredict 5 ns · L2 7 ns · mutex 25 ns · main memory 100 ns
  - Compress 1 KB 10 µs · send 1 KB over 1 Gbps 10 µs · random 4 KB SSD read 150 µs · 1 MB sequential from memory 250 µs
  - Round trip within a data centre 500 µs · 1 MB sequential from SSD 1 ms · disk seek 10 ms · 1 MB over 1 Gbps 10 ms · 1 MB sequential from disk 30 ms · intercontinental round trip 150 ms
  - Rates: disk 30 MB/s, 1 Gbps Ethernet 100 MB/s, SSD 1 GB/s, memory 4 GB/s
  - Why storage and caching tiers exist; same-zone, cross-zone and cross-region latency
  - How cache hit rate drives average latency, and why the miss rate dominates
- **Parallel hardware**
  - Multicore; cache coherence (MSI and MESI protocols); false sharing
  - Memory consistency models: sequential consistency, x86-TSO, the weaker RISC-V and ARM models; why languages define memory models
  - SIMD and GPUs as data parallelism; data parallelism in software: the same operation applied to each element or each batch shard on separate workers, with partial results combined by a reduction such as all-reduce
- **Performance engineering**
  - Cache-aware data layout
  - Reading hardware counters
  - Choosing machine types by memory hierarchy
- **I/O devices, interrupts and DMA**: device registers read and written by programmed I/O, where a polling loop spends cycles checking a status bit; interrupts as a hardware request that saves the program counter and jumps to a handler, with the interrupt latency and the handler's cost; direct memory access, in which a DMA controller is given a source, a destination and a byte count, moves the data while the CPU runs, and interrupts once at the end, so a 1 MB transfer costs the CPU one setup and one interrupt rather than about a million loads and stores; memory-mapped I/O as the way device registers appear in the address space
- **Superscalar and VLIW organization**: superscalar issue, in which hardware fetches and dispatches several instructions per cycle, detects dependencies by scoreboarding or register renaming, and reorders them out of order, so the issue width bounds the peak instructions per cycle; very long instruction word design, in which the compiler packs independent operations into fixed-width bundles and the hardware does no dependency checking, so the schedule's quality depends on the compiler; instructions per cycle (IPC) as the reciprocal of the iron law's cycles per instruction, so IPC above one is possible only when more than one instruction issues in a cycle

### Exercises

- From scratch: base conversion by repeated division; two's-complement encode, decode and overflow detection; sign extension
- From scratch: an IEEE 754 single- and double-precision decoder printing sign, exponent and mantissa
- From scratch: a UTF-8 encoder and decoder that rejects overlong and invalid sequences
- From scratch: parity and CRC-32 by polynomial division, shown detecting but not authenticating changes
- From scratch: gates composed into a full adder, a ripple-carry adder and a multiplexer; a Moore finite-state machine
- From scratch: an RV32I subset interpreter running a recursive function through the calling convention
- From scratch: a set-associative cache simulator with write-back and LRU, reporting hit rate, the three Cs and AMAT
- False sharing measured with and without padding
- Storage arithmetic with powers of two: the size of 10 million pastes and 360 million short links, by hand and in code
- Ping and iperf3 throughput between two VMs in different zones, compared with typical same-zone and cross-zone latencies
- **Reasoning drills**
  - Estimate how long summing a 1 GB array takes from memory bandwidth, then time it
  - Predict the speedup ceiling of a parallel program from Amdahl's law, then measure it on 1, 2, 4 and 8 cores
  - Prove that one adder serves signed and unsigned values, then derive the overflow condition from the carries
  - Choose a machine type for a cache-bound workload from its working-set size, as a decision record
