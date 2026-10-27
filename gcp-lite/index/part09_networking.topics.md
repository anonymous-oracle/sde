# Part 09 · Computer Networking & Web Protocols · TOPIC LIST

Rules and directives for this part: `index/part09_networking.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Computer Networking & Web Protocols

### Architecture principles

- The OSI and TCP/IP models and what lives at each layer
- Layering and encapsulation; the end-to-end argument
- Packet versus circuit switching; statistical multiplexing
- The four delays: transmission L/R, propagation d/s, queueing, processing
- The bandwidth–delay product as data in flight

### Addressing and the link layer

- IPv4 structure, subnetting and CIDR arithmetic; private ranges
- IPv6: 128-bit addresses, stateless autoconfiguration, neighbour discovery in place of ARP, dual stack
- Ethernet framing, self-learning switches, ARP and VLANs
- DHCP and why it needs UDP broadcast
- NAT and source-port exhaustion

### Routing

- Default gateways and routing tables; longest-prefix match implemented with tries
- Link-state routing (Dijkstra; OSPF)
- Distance-vector routing (Bellman–Ford; RIP); count-to-infinity and poisoned reverse
- Hierarchical routing and autonomous systems
- BGP as path-vector policy routing: eBGP and iBGP, route selection, slow convergence, route hijacks
- Anycast: one address announced from many sites and reached at the nearest by BGP

### Transport

- **UDP**
  - Connectionless datagrams; no ordering, delivery or congestion guarantees
  - When to choose it: VoIP, video, real-time games, custom error correction, broadcast
- **TCP**
  - The three-way handshake and teardown
  - Sequence numbers, checksums, acknowledgements and retransmission
  - Per-connection memory and file-descriptor limits; connection pooling
  - Connection budgets: instance count × pool size against a database's connection limit
  - Idle timeouts on load balancers and NAT
- **Reliable transfer, formally**
  - Building reliability from checksums, ACKs, sequence numbers and timeouts
  - Stop-and-wait utilization U = (L/R) / (RTT + L/R)
  - Go-Back-N versus selective repeat; the selective-repeat window limit (half the sequence space)
  - Cumulative ACKs; RTT estimation by EWMA; RTO = estimated RTT + 4 × deviation; fast retransmit
  - Flow control by the receive window
- **Congestion control**
  - AIMD and its convergence toward fairness (Chiu–Jain)
  - Slow start; Reno, CUBIC and model-based BBR
  - The Mathis approximation: throughput ≈ (MSS/RTT) × 1.22/√p
  - Bufferbloat; explicit congestion notification
- **Modern transport**
  - QUIC over UDP: independent streams without head-of-line blocking, combined transport and TLS 1.3 handshake, 0-RTT resumption and its replay risk, connection migration
  - The socket API: `socket`, `bind`, `listen`, `accept`, `connect`

### DNS

- Resolution: recursive resolvers, the hierarchy, authoritative servers
- Record types: A, AAAA, CNAME, MX, TXT, NS
- Caching and TTLs; lowering TTLs a full old-TTL before a migration; DNS as an eventually consistent database
- Routing policies: weighted round robin, latency, geolocation, failover
- Public and private zones; DNSSEC
- DNS as a DDoS target and single point of failure (the 2016 Dyn outage)
- Kubernetes cluster DNS (CoreDNS)

### HTTP and the web

- **URL and URI structure**: scheme, authority, path, query and fragment; URI versus URL; percent-encoding of reserved characters; relative reference resolution; normalisation before comparison
- **HTTP semantics**
  - The request/response cycle; methods, status codes, headers, cookies
  - Safe, idempotent and cacheable methods (GET, POST, PUT, PATCH, DELETE)
  - 429 and 503 with `Retry-After` as back-pressure signals; idempotency keys for non-idempotent requests
  - HTTP caching headers: `Cache-Control`, `Age`, `Via`, validators
- **HTTP versions**
  - HTTP/1.1 persistent connections and chunked bodies
  - HTTP/2 stream multiplexing over one TCP connection
  - HTTP/3 over QUIC
- **Request smuggling and desync**: ambiguous message framing when `Content-Length` and `Transfer-Encoding` disagree or are malformed; a front end and a back end reading different request boundaries (CL.TE and TE.CL); obfuscated `Transfer-Encoding` headers; rejecting ambiguous framing at the server boundary
- **The web platform**
  - HTML, CSS and the DOM
  - Browser rendering
  - The JavaScript event loop in the browser
  - The same-origin policy and its fundamentals

### TLS mechanics

- The TLS handshake; certificates and certificate authorities; chains of trust
- TLS termination at proxies and load balancers; managed certificates

### Middleboxes, proxies and load balancing

- **Firewalls and proxies**
  - Stateful firewalls
  - Forward versus reverse proxies
  - Reverse-proxy roles: hiding backends, IP blocking, connection limits, TLS termination, compression, caching, static content
  - NGINX and HAProxy as reverse proxies and load balancers
- **Load balancing**
  - L4 (transport information, NAT forwarding) versus L7 (terminates, reads headers and cookies, content routing)
  - Algorithms: random, round robin, weighted round robin, least connections, least loaded, consistent hashing
  - Health checks; session persistence and affinity; SSL termination
  - Active-passive and active-active load balancers; the load balancer as a single point of failure
- **Content delivery networks**
  - Edge proxies close to users; DNS or anycast steering
  - Push versus pull CDNs; TTLs, cache keys, invalidation; signed URLs and cookies
  - When each fits; cost and staleness trade-offs

### Private connectivity

- VPNs (IPsec site-to-site, client VPNs)
- Dedicated interconnects and private peering
- Private access to provider services

### Data-centre networks

- Clos and fat-tree topologies
- Equal-cost multipath (ECMP) and oversubscription
- Google's Jupiter fabric

### IoT and constrained-device networking

- **Architecture**: sensing and actuation; devices, gateways, connectivity, platform and application layers; why constrained devices change protocol design (memory, power, duty cycle)
- **Connectivity technologies**: short-range and low-power links (BLE, ZigBee, Z-Wave, Thread, NFC, RFID); LPWAN (LoRa and LoRaWAN, NB-IoT, Sigfox); the range, data-rate and power trade-off; 6LoWPAN and IPv6 on constrained links; RPL routing
- **Application protocols**
  - MQTT: broker, topics and wildcards, QoS 0, 1 and 2, retained messages, last will
  - CoAP: REST over UDP, confirmable messages, observe; compared with HTTP and AMQP
- **Sensor, UAV and machine-to-machine networks**: topology and energy-aware routing; data aggregation; flying ad-hoc networks; M2M communication and interoperability standards (oneM2M)
- **Software-defined networking**: control-plane and data-plane separation; OpenFlow match-action tables and the controller; SDN for IoT (flow rules, slicing, centralized management)
- **Embedded platforms**: Arduino and Raspberry Pi; GPIO, ADC, PWM, I2C, SPI and UART; interfacing sensors and actuators; sampling and debouncing
- **IoT data and verticals**: ingestion, time-series storage, edge pre-processing and stream analytics; smart homes and cities, connected vehicles, smart grid, industrial IoT, precision agriculture, healthcare

### Measurement

- `ping`, `traceroute` (TTL expiry), `dig +trace`, `curl -v`, `ss`
- Packet capture with `tcpdump` on your own host
- Throughput measurement with `iperf3`
- Simulated loss with `tc netem`

### Exercises

- From scratch: a DNS stub resolver over UDP that builds queries, parses answers and follows CNAMEs; TTLs watched as they decay
- From scratch: an HTTP/1.1 server on raw sockets with keep-alive, chunked transfer encoding and request-size limits
- From scratch: a TCP echo server and client; a stop-and-wait and then a sliding-window reliable protocol over UDP with simulated loss
- From scratch: a layer-7 reverse proxy with round-robin and least-connections balancing and health checks; consistent hashing with virtual nodes
- An NGINX reverse proxy with gzip, caching and connection limits, mapped to managed load-balancer equivalents
- A TCP handshake watched with `tcpdump`; a connection budget for autoscaled instances against a database limit
- UDP loss without retransmission observed under `tc netem`
- Caching headers inspected on a CDN-fronted site; HTTP/2 and HTTP/3 compared against a public site
- **Reasoning drills**
  - Estimate a page's minimum load time from round trips, bandwidth and handshakes before measuring it
  - Derive a throughput ceiling from the bandwidth-delay product and the Mathis approximation, then observe it under `tc netem`
  - Explain from first principles why HTTP/2 over TCP suffers head-of-line blocking and HTTP/3 does not
  - Place a service's regions and CDN from a latency budget, as a decision record
