# Part 10 · Operating Systems & Linux · TOPIC LIST

Rules and directives for this part: `index/part10_operating_systems.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Operating Systems & Linux

### Linux practice

- The filesystem hierarchy; navigation and the shell
- Users, groups and permissions (`chmod`, `chown`); `sudo`
- Package managers
- systemd units and services; journald
- SSH, keys and remote access
- Observing a live system: `/proc`, `ps`, `top`, `ss`, `lsof`, `vmstat`, `iostat`
- The OOM killer and cgroup memory limits (why a container instance is killed)
- Tracing and profiling: `strace` for system calls, `perf` and flame graphs for CPU time, eBPF tools such as `bpftrace` for kernel events

### Processes and threads

- Kernel structure: monolithic kernels, microkernels and unikernels; loadable modules; boot from firmware through the bootloader and kernel to init
- User and kernel mode; system calls, traps and interrupts
- `fork`, `exec` and `wait`; process states
- The cost of a context switch
- Threads versus processes
- The address-space layout: code, data, heap, stack
- Signals: delivery and masking, async-signal-safe handlers, SIGTERM then SIGKILL, graceful shutdown inside containers

### CPU scheduling

- FIFO, shortest-job-first and shortest-time-to-completion-first (optimal mean turnaround by an exchange argument)
- Round robin: the time quantum trades response time against context-switch overhead
- The multi-level feedback queue
- Proportional share: lottery and stride scheduling
- Linux's fair schedulers: CFS, and EEVDF since Linux 6.6
- cgroup CPU shares and quotas; CPU throttling behind container CPU limits

### Virtual memory

- Address translation, paging and multi-level page tables; page-table size arithmetic
- The TLB and its reach
- Page faults and demand paging
- Copy-on-write and why `fork` is cheap
- Replacement policies: optimal, LRU, CLOCK
- Thrashing and working sets
- Memory-mapped files
- Heap allocation: free lists, splitting and coalescing, first fit versus best fit, fragmentation; `malloc` over `brk` and `mmap`

### Concurrency

- Race conditions and critical sections
- Mutual exclusion from atomic instructions: test-and-set, compare-and-swap
- Spinlocks versus blocking locks; futexes, which keep an uncontended lock out of the kernel
- Memory barriers and fences; read-copy-update for read-mostly data
- Condition variables and the producer–consumer problem
- Semaphores; readers–writers locks
- Deadlock: the four Coffman conditions; prevention by a global lock order
- Livelock and priority inversion
- Progress conditions: blocking, obstruction-free, lock-free, wait-free
- The ABA problem in compare-and-swap loops

### Persistence

- The device interface and I/O scheduling
- The file-system abstraction: inodes, directories, hard and symbolic links, file descriptors
- The on-disk layout of a simple file system
- Crash consistency: `fsck` versus journaling (data, metadata, ordered mode) versus copy-on-write file systems
- What `fsync` promises and what databases rely on
- Flash translation layers and write amplification
- RAID 0, 1 and 5 and their failure arithmetic

### Isolation

- Linux namespaces and what each isolates
- cgroups and what they limit
- seccomp filters and capabilities
- Containers versus virtual machines: the shared kernel as a weaker boundary

### I/O models and performance

- The cost of system calls and copies
- Thread-per-connection versus event-driven I/O; `epoll` and `io_uring`
- The C10k problem
- Zero-copy transfer with `sendfile`
- Why NGINX and Go's network poller are built as they are

### Exercises

- From scratch: a shell with pipes, redirection, background jobs and signal handling, built on `fork`, `exec` and `wait`
- From scratch: a scheduler simulator comparing FIFO, SJF, round robin, MLFQ and stride scheduling on turnaround and response time
- From scratch: a page-table walker and TLB-reach calculator; a replacement simulator comparing optimal, LRU and CLOCK
- From scratch: a spinlock from compare-and-swap; a producer–consumer queue with condition variables and a deadlock demonstration; a readers–writers lock
- From scratch: a free-list memory allocator with splitting and coalescing
- From scratch: a container started with namespaces and a cgroup memory limit, without a container runtime
- From scratch: an `epoll` echo server compared with thread-per-connection under load
- An OOM kill and a cgroup CPU throttle predicted, then observed, on your own VM
- A process inspected through `/proc` and its open sockets with `ss`
- A crash-consistency experiment comparing `fsync` behaviours
- **Reasoning drills**
  - Predict context-switch and system-call costs, then measure them
  - Choose which deadlock condition a design breaks and prove its lock order admits no cycle
  - Estimate TLB reach and page-fault rates for a working set before measuring them
  - Diagnose a slowdown from `vmstat`, `iostat` and `/proc` output alone, writing one hypothesis per step
