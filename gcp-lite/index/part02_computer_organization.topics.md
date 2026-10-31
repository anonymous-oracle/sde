# Part 02 · Computer Organization & Data Representation · TOPIC LIST

Rules and directives for this part: `index/part02_computer_organization.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Computer Organization & Data Representation

### Data representation

- **Number systems**
  - Bits and bytes; why computers use base 2; a bit holds one of two values, and a byte is eight bits, so it holds one of 256 patterns; a two-state signal such as high or low voltage can be told apart reliably in hardware, and an n-bit pattern has 2ⁿ distinct values, which is why binary counts and addresses grow by powers of two
  - Binary and hexadecimal; positional notation (a numeral dₖ…d₀ in base b is Σ dᵢ·bⁱ)
  - Base conversion by repeated division, and why it terminates: to convert N to base b, divide N by b, record the remainder, and repeat on the quotient until it reaches 0; the remainders read from last to first are the digits, so 45 gives remainders 1, 0, 1, 1, 0, 1, which reads as 101101 in base 2; the loop terminates because the quotient shrinks at every step, and the number of digits is ⌊log_b N⌋ + 1
  - Two's complement as arithmetic modulo 2ⁿ: one adder for signed and unsigned values; range −2ⁿ⁻¹ … 2ⁿ⁻¹−1; signed overflow when the carry into the sign bit differs from the carry out; sign extension
  - Bit identities: `x & (x−1)` clears the lowest set bit; power-of-two test; a nonzero x is a power of two exactly when `x & (x − 1)` is 0, because a power of two has a single set bit, and subtracting 1 flips that bit and every bit below it; for x = 12 (binary 1100), x − 1 is 1011 and the AND is 1000, so the lowest set bit is cleared; the lowest set bit itself is isolated by `x & -x` in two's complement
- **Storage units**
  - Binary versus decimal prefixes (KiB, MiB, GiB versus KB, MB, GB) and the gap that shows up on cloud storage bills
  - Powers of two to remember: 2⁷ = 128, 2⁸ = 256, 2¹⁰ ≈ 1 thousand, 2¹⁶ = 65,536, 2²⁰ ≈ 1 million, 2³⁰ ≈ 1 billion, 2³² ≈ 4.3 billion (the IPv4 address space, a 32-bit integer's range), 2⁴⁰ ≈ 1 trillion
- **Character encoding**
  - ASCII; UTF-8 as a variable-length prefix code that is ASCII-compatible and self-synchronizing
  - Why encoding matters in data pipelines: bytes mean nothing until a reader knows their encoding, so a UTF-8 file read as Latin-1 turns each multi-byte character into several wrong characters; a pipeline that mixes encodings, or that counts characters where it should count bytes, corrupts or truncates data without raising an error, so every boundary states its encoding and the length units it uses
- **Data layout**
  - Endianness and network byte order: little-endian stores the least significant byte at the lowest address, as x86 and most ARM configurations do, and big-endian stores the most significant byte first; network byte order is big-endian, so the 32-bit value 0x12345678 is sent as the bytes 12 34 56 78; `htonl` and `ntohl` convert between host and network order, and Python's `struct` format with a `!` prefix packs in network order
  - Alignment and padding: a value of size s is aligned when its address is a multiple of its alignment requirement, which is often s, and misaligned access is slow or faults on some CPUs; a compiler inserts padding bytes so each field is aligned, so a struct holding a 1-byte field, a 4-byte field and a 1-byte field occupies 12 bytes on a typical 64-bit ABI rather than 6; ordering fields from largest to smallest reduces the padding
- **Error detection**
  - Parity: a parity bit is the XOR of the data bits, so an even-parity word has an even count of ones, and any single flipped bit makes the count odd and is detected; two flipped bits cancel and go unnoticed, and parity cannot say which bit flipped, so it detects an error but does not correct it
  - The cyclic redundancy check as polynomial division over GF(2): the message is read as a polynomial whose coefficients are its bits, padded with zeros and divided by a fixed generator polynomial, with XOR in place of subtraction, and the remainder is the check value appended to the message; the receiver repeats the division, and a zero remainder means no error was found; CRC-32 uses a degree-32 generator, and a CRC of degree k detects every burst error no longer than k bits
  - What each detects, and why neither authenticates: parity catches every odd number of flipped bits and misses even ones, and a CRC catches every burst up to its degree, but both are fixed public functions, so anyone who alters the data can recompute the check; only a keyed message authentication code or a digital signature authenticates a message, because it needs a secret or a private key that the attacker lacks

### Digital logic

- **Boolean logic**
  - AND, OR, NOT, XOR and truth tables; the same logic in IAM policy evaluation, firewall rules and CPU design
  - Boolean algebra laws: identity, complement, distributive, De Morgan; x AND 1 = x and x OR 0 = x, x AND NOT x = 0 and x OR NOT x = 1, and AND and OR each distribute over the other; De Morgan's laws, NOT (x AND y) = NOT x OR NOT y and NOT (x OR y) = NOT x AND NOT y, let a negation be pushed through a gate, which is how a circuit's logic is rewritten into a cheaper form
  - Sum-of-products and product-of-sums canonical forms: a sum of products is an OR of AND terms with one minterm per row where the function is 1, and a product of sums is an AND of OR clauses with one maxterm per row where it is 0; for n variables each canonical form has at most 2ⁿ terms, and it is usually simplified afterwards with a Karnaugh map or the Quine–McCluskey method
  - Functional completeness of NAND alone and of NOR alone: a set of gates is functionally complete when it can express every Boolean function; NOT is NAND(x, x), AND is NOT of NAND, and OR is NAND of the two negated inputs, so NAND alone is complete, and by duality NOR alone is complete; NAND and NOR are simple to build in CMOS, which is why chips are built from them
  - Karnaugh-map minimization up to four variables: the map lays the truth table out in Gray-code order so that adjacent cells differ in one variable, and a group of 1, 2, 4 or 8 adjacent ones, wrapping at the edges, gives one product term with the changing variables dropped; a four-variable map has 16 cells, and the method becomes unwieldy beyond about six variables, where Quine–McCluskey is used
- **Combinational circuits**
  - Half and full adders: a half adder computes sum = a XOR b and carry = a AND b; a full adder adds a carry-in, with sum = a XOR b XOR c and carry-out = (a AND b) OR (c AND (a XOR b)), so two half adders and an OR gate make one full adder
  - The n-bit ripple-carry adder (O(n) delay) and carry-lookahead (O(log n) delay); a ripple-carry adder chains n full adders, so the carry out of bit i waits for the carry out of bit i − 1 and the delay grows linearly in n; carry-lookahead computes generate g = a AND b and propagate p = a XOR b for each bit and combines them in a tree, so every carry is a function of the lower bits, settled in about log₂ n gate levels, at the cost of more gates
  - Multiplexers and decoders: a 2ⁿ-to-1 multiplexer passes one of 2ⁿ data inputs to its output, chosen by n select lines; an n-to-2ⁿ decoder turns an n-bit value into a single active output, which selects one register or memory row; a multiplexer whose data inputs are tied to 0 and 1 can realize any Boolean function of its select lines
- **Sequential logic**
  - The SR latch, the D flip-flop and registers: two cross-coupled NOR gates form an SR latch, whose S and R inputs set and reset the stored bit and which holds its value when both are inactive; a D flip-flop samples D on the clock edge and holds it until the next edge, which removes the race through the latch; a register is n flip-flops sharing one clock, storing an n-bit word
  - The clock; setup and hold constraints; a synchronous circuit changes state only on clock edges, and the logic between two registers must settle within one clock period, so the longest such path sets the maximum clock frequency; setup time is how long D must be stable before the edge and hold time how long it must stay stable after, and a violation of either makes the sampled value wrong or metastable
  - Finite-state machines, Moore versus Mealy: a finite-state machine has a set of states, an input alphabet, a transition function and outputs, and its state is stored in flip-flops; in a Moore machine the outputs depend only on the state, while in a Mealy machine they depend on the state and the current input, so a Mealy output can respond to an input within the same cycle; a turnstile or a vending controller is a standard example of each

### Machine organization

- **Instruction set architecture**
  - The RISC-V RV32I base: 32 registers, load/store, arithmetic, branches, `jal`/`jalr`
  - How a function becomes instructions: calling convention, stack frame, caller-saved and callee-saved registers
  - The fetch–decode–execute cycle and a single-cycle datapath; the control unit that reads the opcode and function fields to set the datapath's multiplexer selects, ALU operation and memory and register-write enables, realized either as hardwired logic or as a microprogram; the multicycle datapath, which reuses one ALU and one memory port over several clock cycles per instruction, trading a longer instruction time for less hardware
- **Performance laws**
  - The iron law: CPU time = instruction count × cycles per instruction × clock period
  - Amdahl's law: speedup = 1 / ((1 − p) + p/s), bounded by 1/(1 − p); p is the fraction of the work that can be sped up and s the speedup of that fraction, so a program that is 90% parallel on 8 cores gets 1 / (0.1 + 0.9/8) ≈ 4.7 times the speed, and as s grows without limit the serial fraction 1 − p sets the ceiling; Gustafson's law takes the opposite view, asking how much more work fits in the same time
  - The five-stage pipeline; structural, data and control hazards; forwarding; branch prediction
  - Pipeline mechanism: each clock cycle moves one instruction into each stage (fetch, decode, execute, memory, write-back), so a full pipeline completes one instruction per cycle; a data hazard is an instruction that needs a result not yet written, resolved by forwarding (bypassing) the ALU output to the next instruction's input, while a load whose value is used by the very next instruction needs a one-cycle stall, since the loaded value exists only after the memory stage; after a taken branch the instructions fetched behind it are discarded, so the branch penalty is the number of stages between fetch and branch resolution, which branch prediction reduces
- **The memory hierarchy**
  - SRAM, DRAM, flash and disk: SRAM holds each bit in six transistors, is fast and costly, and is used for caches; DRAM holds each bit as charge in one capacitor that leaks and must be refreshed, so it is denser and cheaper; flash keeps its contents without power and is read in pages and erased in larger blocks; disk stores bits magnetically, so a read waits for a seek and a rotation first
  - Temporal and spatial locality: temporal locality is reuse of an address soon after it was last used, and spatial locality is use of addresses near a recent one, so a 64-byte cache line brings in neighbours that a loop over an array reads next; programs with strong locality hit the cache far more often, and caches exist only because of it
  - Cache organization: direct-mapped, set-associative, fully associative; the tag, index and offset of an address
  - Write-through versus write-back: write-through sends every store to the next level at once, which is simple and always consistent but slow; write-back updates only the cached line, marks it dirty and writes it out on eviction, so many stores to one line cost one memory write; write-back needs a dirty bit per line, and a write miss is usually handled by fetching the line first, a policy called write-allocate
  - The three Cs of misses: compulsory, capacity, conflict; a compulsory miss is the first access to a block ever, a capacity miss happens because the working set is larger than the cache even under fully associative placement, and a conflict miss happens because too many blocks map to one set of a direct-mapped or set-associative cache; a larger block size lowers compulsory misses through spatial locality but raises the miss penalty
  - Average memory access time: AMAT = hit time + miss rate × miss penalty, level by level
  - Virtual memory and the TLB from the hardware side: the MMU translates each virtual address to a physical one through a page table, and with 4 KB pages the low 12 bits are the offset within the page while the upper bits select the page; the translation lookaside buffer caches recent translations, so a TLB hit avoids a page-table walk, and a miss pays for the walk, which on x86-64 reads up to four table levels
- **Latency numbers**
  - L1 0.5 ns · branch mispredict 5 ns · L2 7 ns · mutex 25 ns · main memory 100 ns
  - Compress 1 KB 10 µs · send 1 KB over 1 Gbps 10 µs · random 4 KB SSD read 150 µs · 1 MB sequential from memory 250 µs
  - Round trip within a data centre 500 µs · 1 MB sequential from SSD 1 ms · disk seek 10 ms · 1 MB over 1 Gbps 10 ms · 1 MB sequential from disk 30 ms · intercontinental round trip 150 ms
  - Rates: disk 30 MB/s, 1 Gbps Ethernet 100 MB/s, SSD 1 GB/s, memory 4 GB/s
  - Why storage and caching tiers exist; same-zone, cross-zone and cross-region latency
  - How cache hit rate drives average latency, and why the miss rate dominates
- **Parallel hardware**
  - Multicore; cache coherence (MSI and MESI protocols); false sharing; MSI gives each cache line the states Modified, Shared and Invalid, and MESI adds Exclusive, so a core holding the only clean copy can write it without a bus transaction; a write to a line that other cores hold invalidates their copies; false sharing is two cores writing different variables that sit in one 64-byte line, so the line bounces between caches although no data is shared
  - Memory consistency models: sequential consistency, x86-TSO, the weaker RISC-V and ARM models; why languages define memory models
  - SIMD and GPUs as data parallelism; data parallelism in software: the same operation applied to each element or each batch shard on separate workers, with partial results combined by a reduction such as all-reduce
- **Performance engineering**
  - Cache-aware data layout: an array of structs versus a struct of arrays matters because a loop that reads one field of many records touches fewer cache lines when that field is stored contiguously, and sequential access lets the hardware prefetcher run ahead; tiling, or blocking, reuses a small block of a matrix while it is still in cache, as in a blocked matrix multiply
  - Reading hardware counters: performance counters such as cycles, instructions retired, cache misses and branch mispredictions are read with a tool like `perf stat` on Linux, and instructions per cycle is the first ratio to compute: low IPC with many cache misses points at memory, and low IPC with many mispredictions points at branches; each reading must be repeated over enough runs to average out noise
  - Choosing machine types by memory hierarchy: a workload whose working set fits in a given cache level is limited by that level's size, so the choice follows from measuring the working set and comparing it with each cache size and with memory capacity; memory-optimized machine families on Compute Engine offer more memory per vCPU for a working set that overflows the cache; the decision is written as a record with the measured working set and the numbers that justify the choice
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
