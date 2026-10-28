# Part 09 · Computer Networking & Web Protocols · TOPIC LIST

Rules and directives for this part: `index/part09_networking.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Computer Networking & Web Protocols

### Architecture principles

- The OSI and TCP/IP models and what lives at each layer
- Layering and encapsulation; the end-to-end argument
- Packet versus circuit switching; statistical multiplexing
- The four delays: transmission L/R, propagation d/s, queueing, processing
- The bandwidth–delay product as data in flight
- Network performance theory: Little's law L = λW for packets in flight; the mean queueing delay of an M/M/1 queue at utilization ρ, W_q = ρ / (μ(1 − ρ)), which grows without bound as ρ approaches 1; and the Shannon capacity C = B log₂(1 + S/N), the highest rate at which a channel of bandwidth B and signal-to-noise ratio S/N can carry data with arbitrarily small error

### Addressing and the link layer

- IPv4 structure, subnetting and CIDR arithmetic; private ranges
- IPv6: 128-bit addresses, stateless autoconfiguration, neighbour discovery in place of ARP, dual stack
- Ethernet framing, self-learning switches, ARP and VLANs
- DHCP and why it needs UDP broadcast
- NAT and source-port exhaustion; port numbers as 16-bit demultiplexing keys, with well-known ports such as 53 for DNS and 443 for HTTPS and ephemeral ports chosen by the client, and the 4-tuple of source address, source port, destination address and destination port that identifies a TCP connection
- Multiple access and MAC protocols: pure ALOHA with throughput S = G·e^(−2G), maximal at G = 1/2 with S = 1/(2e) ≈ 0.184; slotted ALOHA with S = G·e^(−G), maximal at G = 1 with S = 1/e ≈ 0.368; CSMA, which senses the carrier before sending, with a collision window of one propagation delay; CSMA/CD as Ethernet's collision detection with binary exponential backoff over 512-bit slot times; and CSMA/CA in Wi-Fi, with random backoff and optional RTS/CTS reservation

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
  - 429 and 503 with `Retry-After` as back-pressure signals; idempotency keys for non-idempotent requests; the error taxonomy: 4xx client errors that a retry will not fix, 503, 429 and 504 as transient errors that retry with backoff, and 500 as a server bug to alert on; an error envelope in RFC 9457 problem details carrying a stable machine-readable code, the request ID and the per-field errors, with the cause logged on the server and never returned to the client as a stack trace
  - HTTP caching headers: `Cache-Control`, `Age`, `Via`, validators; freshness from `max-age` compared with `Age` (a response is fresh while Age is below max-age), revalidation with `ETag` and `Last-Modified` answered by 304 Not Modified; conditional requests with `If-None-Match` for cached reads and `If-Match` on writes, where a stale ETag returns 412 Precondition Failed so a lost update is refused; freshness monitoring: the cache hit ratio and the age distribution of served responses read from the `Age` header, the `stale-while-revalidate` and `stale-if-error` directives that serve a stale response while refreshing or during an origin failure, and an alert when the share of responses served past max-age crosses a set budget
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
- **Redirection status codes**: 301 and 302 as permanent and temporary redirects, which clients have historically rewritten to GET; 303 See Other, sent after a POST to redirect to a result page with GET so that a refresh does not resubmit; 307 and 308, which preserve the method and body, with 308 the permanent form of 307; the `Location` header; and clients that cap a redirect chain at a small number of hops
- **WebDAV and publishing with PUT**: PUT replaces the entire resource at the target URI and is idempotent, so a retry is safe; WebDAV extends HTTP with PROPFIND to read collection properties, MKCOL to create a collection, COPY and MOVE, and LOCK and UNLOCK with lock tokens for concurrent editors; a conditional PUT with `If-Match` refuses a lost update; OPTIONS advertises the allowed methods and the DAV compliance class
- **Representations, content negotiation and entities**: the entity headers `Content-Type` (with its charset) and `Content-Length` (counted in bytes after content coding), with `Content-Encoding` applied to the representation and distinct from the transfer coding applied on one hop, so that a body is the entity with the transfer coding removed; server-driven negotiation with `Accept`, `Accept-Language` and `Accept-Encoding`, quality values such as `q=0.8` ranking the options, and 406 Not Acceptable only when no representation is acceptable; `Vary` naming each request header that the chosen representation depends on; and range requests with `Range`, answered by 206 Partial Content and `Content-Range`, for resumable downloads

### TLS mechanics

- The TLS handshake; certificates and certificate authorities; chains of trust
- TLS termination at proxies and load balancers; managed certificates

### Middleboxes, proxies and load balancing

- **Firewalls and proxies**
  - Stateful firewalls
  - Forward versus reverse proxies
  - Reverse-proxy roles: hiding backends, IP blocking, connection limits, TLS termination, compression, caching, static content; compression negotiated by `Accept-Encoding` with gzip or br as the content coding, and `Vary: Accept-Encoding` so a cache stores one entry per encoding
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
- From scratch: a slotted ALOHA simulation that measures throughput against G·e^(−G) across offered loads, and a content-negotiation handler that picks a representation by quality values and returns 406 only when none fits
- **Reasoning drills**
  - Estimate a page's minimum load time from round trips, bandwidth and handshakes before measuring it
  - Derive a throughput ceiling from the bandwidth-delay product and the Mathis approximation, then observe it under `tc netem`
  - Explain from first principles why HTTP/2 over TCP suffers head-of-line blocking and HTTP/3 does not
  - Place a service's regions and CDN from a latency budget, as a decision record
  - Predict the offered load that maximizes slotted ALOHA throughput, then measure the peak in a simulation
  - Predict which redirect code keeps a POST body intact for a given client flow, then check the prediction against the specification of each code
