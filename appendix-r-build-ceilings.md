# The 309 — a from-scratch build curriculum (standalone)

**Status.** Self-contained. This file has no external dependencies: everything it refers to is
either defined inside it or is a public book, paper or course with a link in Part 8 or Part 9.
Curated and link-checked **2026-09-16**.

**What this file is.** Everything a learner working alone needs to take the 309 production ML
system-design case studies from *"I can read this blog post"* to *"I can build this"* — the
catalog itself, the mathematics, the computer science, the software-engineering and
system-design theory, the academic bibliography, the university course material (Ivy League,
Stanford/MIT/CMU peers, IIT/IISc/NPTEL), **and** a from-zero Go track so the learner can
implement all of it in Go rather than reading about it in Python.

**How to read this file.**

```
PART 0   The contract — learner model, language law, how to use the ladder
PART 1   The catalog — all 309 studies, 12 families (carried in full)
PART 2   The finding — what "from scratch" actually requires, and why it is rare
PART 3   The floor — Tier 0 remedial math, then the nine theory families
PART 4   The ceilings — per-family theory, derivations, texts, courses, papers
PART 5   Go from zero — GO-0…GO-14, taught, not just referenced
PART 6   The build ladder — B0…B14, what you implement in Go, in order
PART 7   The Python boundary — where Go stops, and why
PART 8   Master bibliography — mathematics, CS, systems, SWE, ML, per-domain
PART 9   Course index — Ivy League, peer institutions, IIT/IISc/NPTEL
```

---

# PART 0 — The contract

## 0.1 Self-containment

This file depends on nothing outside itself. Every label it uses — `T.Quant`, `M.NS`, `T-REC`,
`GO-7`, `B12` — is **defined in this file** and means nothing outside it:

| Label | Means | Defined in |
|---|---|---|
| `T.*` | one of the nine theory-floor families | §3.3 |
| `M.*` | one of the four quantitative kits | §3.4 |
| `T-*` | one of the fifteen build ceilings | Part 4 |
| `GO-*` | one of the fifteen Go language rungs | Part 5 |
| `B*` | one of the fifteen build rungs | Part 6 |

Everything else you are asked to read is a **public book, paper or course**, linked in §8.7,
§9.3 or §9.4. There is no companion document, no prerequisite syllabus, and nothing you need
permission to open.

## 0.2 The learner model

Assume the reader:

- **is a beginner in Go** — has never written a `go.mod`, does not know what a slice header is,
  has not used `context.Context`. Part 5 teaches the language from zero and Part 6 never uses
  a Go construct that Part 5 has not already unlocked.
- **works alone** — no TA, no study group, no institutional library. Every primary source below
  is therefore either **[free]** (author- or publisher-hosted, legally, at no cost) or flagged
  as paid so the choice is explicit.
- **has the floor, or can skip-test it.** Part 3 is the floor. Part 4 assumes it. If a gate in
  Part 3 is open, close it before opening the matching ceiling in Part 4 (§3.2 is the map).
- **is not doing a PhD.** Every ceiling below has a stated stopping point. "From scratch" means
  *you can derive the object and implement it correctly*, not *you can extend the research*.

## 0.3 Language law — Go first, Python only where forced

> **Rule.** If the concept can be implemented in Go, it is implemented in Go. Python appears
> only where Go has no usable path, and every such case is named explicitly in **Part 7** with
> the reason. "It's easier in Python" is not a reason. "The only maintained tokenizer /
> autodiff / solver is a Python C-extension" is.

This inverts the usual ML-teaching default, and that is deliberate: the learner is building
*systems*, and the systems in these 309 case studies are overwhelmingly served, indexed,
streamed and orchestrated in compiled languages. Writing the numerics yourself in Go is also
the fastest way to stop treating `model.fit()` as magic.

Practical consequence: you will implement matrix multiply, gradient descent, BM25, HNSW,
connected components, ARIMA, IPS estimators and a streaming watermark **by hand**, in Go, with
tests. That is the point.

## 0.4 How the three ladders interlock

| Ladder | Rungs | What it gives you | Gate to advance |
|---|---|---|---|
| **Theory** (Parts 3–4) | T.\* floor → T-\* ceilings | The derivation | You can derive the object on paper |
| **Go** (Part 5) | GO-0 … GO-14 | The language | Artifact compiles, tests pass, `go vet` clean |
| **Build** (Part 6) | B0 … B14 | The implementation | Property test + a numeric that matches theory |

Read across, not down. **B7 (learning-to-rank) needs T-IR §4.2 for the objective, GO-4
generics and GO-7 concurrency for the code.** Part 6 states that triple for every rung.

## 0.5 Access and citation rules

**[free]** = author- or publisher-hosted at no cost, link-checked 2026-09-16.
**[paid]** = commercial book or paywalled course; listed when it is genuinely the best source.

No Scribd, Z-Library, LibGen, Sci-Hub, epdf.pub, PDF Drive, dokumen.pub or scan mirrors are
used as sources or linked anywhere in this file, though several surfaced during research.
Papers are cited by arXiv, ACM/IEEE DOI, or author-hosted PDF only. (Scribd appears once in
Part 1 as a *company name* in the carried catalog — that is a case study, not a source.)

---

# PART 1 — The catalog (all 309)

Source: [Engineer1999/A-Curated-List-of-ML-System-Design-Case-Studies](https://github.com/Engineer1999/A-Curated-List-of-ML-System-Design-Case-Studies)
— 309 studies, 84 companies. Format is `Company — description (year)`.

**Do not re-implement 309 blog posts.** The catalog is an *index of forces*: you read it to
learn which problems recur, then you build the **family**, once, properly. Part 6 gives you
twelve builds, not 309. The families and their counts:

| # | Family | n | Ceiling (Part 4) | Build (Part 6) |
|---|---|---|---|---|
| 1 | Recommend / personalize / feed | 65 | T-REC §4.1 | B6 |
| 2 | Search / rank / ads | 36 | T-IR §4.2, T-AUCTION §4.3 | B7, B8 |
| 3 | Forecast / ETA / demand | 27 | T-TS §4.4 | B9 |
| 4 | Fraud / trust & safety | 24 | T-GRAPH §4.5 | B10 |
| 5 | LLM / genAI apps | 19 | T-DL §4.6 | B11 |
| 6 | NLP / text / support | 7 | T-NLP §4.7 | B11 |
| 7 | CV / video / OCR | 6 | T-CV §4.8 | — (buy; see §4.8) |
| 8 | Speech / audio | 3 | T-SIGNAL §4.9 | — (buy; see §4.9) |
| 9 | Marketing / churn / CLV / notify | 14 | T-CAUSAL §4.10 | B12 |
| 10 | Availability / inventory | 5 | T-STREAM §4.11 | B13 |
| 11 | ML platform / infra | 2 | T-MLSYS §4.12 | B14 |
| 12 | Other (pricing, routing, ER, dims) | 101 | T-OPT / T-ER §4.13 | B5, B10b |

## 1.1 The twelve families, in full

### Recommend / personalize / feed (65)

- Walmart — Recommend complementary items (2023)
- Swiggy — Recommend items to order (2023)
- Lyft — Recommend content in app (2023)
- Etsy — Recommend relevant marketplace items (2023)
- Airbnb — Personalized listing search (2023)
- Twitter — Recommend interesting tweets (2023)
- Linkedin — Personalize the homepage feed (2023)
- Netflix — Personalize video clips (2023)
- Instacart — Personalize user experience by recommending relevant products (2023)
- Pinterest — Recommend similar visual content (2023)
- Spotify — Recommend new complementary music (2023)
- Dailymotion — Recommend diversified video content (2023)
- New York Times — Recommend recipes to readers (2023)
- Expedia — Suggest diverse travel recommendations (2023)
- Stitch Fix — Personalize styling recommendations (2023)
- Netflix — Generate content recommendations for users (2023)
- Delivery Hero — Recommend restaurants for new customers (2023)
- Salesforce — Recommend apps in the marketplace (2023)
- Delivery Hero — Recommend restaurants (2023)
- Ebay — Recommend relevant e-commerce items (2022)
- Doordash — Recommend substitute items (2022)
- Pinterest — Personalize homepage contents (2022)
- Expedia — Categorize customer feedback (2022)
- Ebay — Recommend products and content (2022)
- Yelp — Personalize recommendations (2022)
- Gousto — Recommend food items and recipes (2022)
- Meta — Personalize daily digest notifications (2022)
- Instacart — Recommend relevant food items (2022)
- Doordash — Personalize recommendations on homepage (2022)
- Autotrader — Personalize automotive search results (2022)
- Peloton — Recommend fitness training videos (2022)
- New York Times — Personalize paywall limits (2022)
- Netflix — Recommend content to view (2022)
- Stitch Fix — Recommend e-commerce items (2022)
- Walmart — Curate e-commerce product recommendations (2022)
- Twitter — Recommend accounts to follow (2022)
- Glassdoor — Recommend interesting posts to users (2022)
- Glassdoor — Recommend interesting posts to users (2022)
- Dailymotion — Recommend diversified video content (2022)
- Linkedin — Deliver more relevant job recommendations (2022)
- Cookidoo — Personalize recipe recommendations (2022)
- Pinterest — Recommend bids for advertizers (2021)
- OLX — Recommend e-commerce items (2021)
- Stitch Fix — Recommend e-commerce inventory (2021)
- Gousto — Recommend food items and recipes (2021)
- Spotify — Personalize homepage content (podcasts, playlist, music) (2021)
- Stitch Fix — Recommend looks (2021)
- Walmart — Recommend learning content (2021)
- New York Times — Recommend content to read (2021)
- PayPal — Recommend financial products (2021)
- Scribd — Recommend content to read (2021)
- Wayfair — Recommend furniture items (2021)
- Zillow — Recommend similar homes (2021)
- Spotify — Personalize homepage content (podcasts, playlist, music) (2021)
- Expedia — Personalize travel search results (2021)
- Meta — Personalize the newsfeed content (2021)
- Linkedin — Serve personalized learning recommendations (2020)
- Linkedin — Serve personalized learning recommendations (2020)
- Etsy — Personalize e-commerce search (2020)
- Zynga — Personalize push notification timing (2020)
- Spotify — Recommend shortcuts for homepage (2020)
- Wayfair — Recommend complementary products (2020)
- Airbnb — Recommend marketplace items (2019)
- Gojek — Personalize search results (2019)
- Lyft — Personalize marketing offers (2018)

### Search / rank / ads (36)

- Pinterest — Prevent advertiser churn (2023)
- Airbnb — Improve travel search experience (2023)
- Algolia — Suggest relevant search queries (2023)
- Netflix — In-video search (2023)
- Etsy — Show relevant ads (2023)
- Swiggy — Сonversational and open-ended search (2023)
- Etsy — Search by image (2023)
- Linkedin — Show relevant jobs in search (2023)
- Instacart — Search food and grocery items (2022)
- Spotify — Search for podcasts (2022)
- PayPal — Prioritize sales leads (2022)
- Trivago — Optimize accommodation ranking (2022)
- Airbnb — Improve travel search experience (2022)
- Expedia — Rank relevant travel deals (2022)
- Linkedin — Improve post search functionality (2022)
- Snap — Rank relevant ads (2022)
- Instacart — Autocomplete user searches in e-commerce (2022)
- Doordash — Search food and grocery items (2022)
- Faire — Rank e-commerce items (feature store) (2022)
- Linkedin — Predict ad click-through rate (2022)
- Etsy — Rank marketplace search results (2022)
- Faire — Search and navigate marketplace items (2021)
- Dropbox — Search by image content (2021)
- Microsoft — Rank customer support cases (2021)
- Swiggy — Rank restaurants in search (2021)
- Swiggy — Rank food dishes in search (2021)
- Wayfair — Automate ads placement and bidding (2021)
- Dailymotion — Target contextual advertising (2021)
- Wayfair — Optimize digital ads (2021)
- Airbnb — Rank travel search results (2020)
- Wayfair — Improve search experience for new customers (2020)
- Zillow — Rank homes to buy (2020)
- Doordash — Search for restaurants and dishes (2020)
- Dropbox — Predict files users search for (2019)
- Gojek — Analyse the relevance of search results (2019)
- Airbnb — ML Powered search ranking (2019)

### Forecast / ETA / demand (27)

- Uber — Forecast demand for airport rides (2023)
- Wayfair — Predict delivery times (2023)
- Zalando — Forecast demand in fashion e-commerce (2023)
- Doordash — Forecast order volumes and deliveries (2023)
- Expedia — Forecast flight prices (2023)
- Doordash — Accurately forecast demand during holidays (2023)
- Swiggy — Predict food delivery time (2023)
- Swiggy — Predict food delivery time (2023)
- Swiggy — Predict food delivery time (2023)
- OLX — Predict order delivery time (2023)
- Grubhub — Forecast order volume (2022)
- Gojek — Predict food delivery times (2022)
- Uber — Predict estimated time of arrival (2022)
- Spotify — Forecast user activity metrics (2022)
- Walmart — Forecast anomalies in refrigeration (2022)
- Gojek — Predict estimated time of delivery (2022)
- Lyft — Make causally valid forecasts (2022)
- Lyft — Make causally valid forecasts (2022)
- Grubhub — Forecast volume order (2021)
- Doordash — Predict delivery supply and demand (2021)
- Scribd — Extract metadata from documents (2021)
- Twitter — Forecast resource usage and cost (2021)
- Ocado — Forecast e-commerce grocery demand (2021)
- Mercado Libre — Forecast demand for e-commerce items (2021)
- Instacart — Spot lost demand (2019)
- Gojek — Accurately forecast demand (2019)
- Uber — 100+ Petabytes with Minute Latency (2018)

### Fraud / trust & safety (24)

- Stripe — Prevent fraudelent transactions (2023)
- Linkedin — Detect viral spam (2023)
- Wayfair — Detect fraud with embeddings (2023)
- Zillow — Identify and block unwanted callers (2023)
- BlaBlaCar — Prevent phishing and payment fraud (2023)
- Uber — Detect potential fraudulent entities (2023)
- Grab — Automatically detect new fraud types (2023)
- Whatnot — Detect marketplace spam (2023)
- BlaBlaCar — Prevent phishing and payment fraud (2023)
- Uber — Detect payment fraud (2022)
- Netflix — Detect account or content fraud (2022)
- Grab — Detect fraud with graph models (2022)
- Slack — Detect spam invites (2021)
- Pinterest — Detect spam users (2021)
- PayPal — Detect payment fraud (2021)
- Swiggy — Detect fraud in online food delivery (2021)
- Stripe — Detect fraud in online payments (2021)
- PayPal — Prevent repeated payment fraud (2021)
- Wayfair — Detect payment fraud (2020)
- PayPal — Detect payment fraud (2020)
- Stripe — Detect fraud in online payments (2020)
- Lyft — Predict fraudulent activity (2018)
- Lyft — Identify user fraud (2018)
- Lyft — Shallow to deep learning in fraud (2018)

### LLM / genAI apps (19)

- Stitch Fix — Generate ad headlines (2023)
- Microsoft — Diagnose production incidents with LLM (2023)
- GitHub — Generate code and code suggestions (2023)
- Honeycomb — Generate queries with natural language (2023)
- Spotify — Automatically generate ad content (2023)
- Nextdoor — Generate engaging email subject lines (2023)
- Meta — Generate code with LLM (2023)
- GitHub — AI copilot for code generation (2023)
- Doordash — Areas for using Generative AI (2023)
- Spotify — Generate audio podcast previews (2023)
- Thoughtworks — AI copilot for product strategy (2023)
- Salesforce — Summarize Slack conversations (2023)
- Instacart — Build an internal AI assistant (2023)
- Vimeo — Customer support AI assistant (2023)
- Google — Generate summaries (2022)
- Google — Summarize conversations (2022)
- Nordstrom — Generate outfit combinations (2021)
- Gojek — Generate names for pickup points (2020)
- Zillow — Generate floor plans from photos (2020)

### NLP / text / support (7)

- Grab — Automatically tag sensitive data (2023)
- Salesforce — Extract relevant information from a knowledge article (2023)
- Dropbox — Identify date formats in file names (2023)
- Meta — Translate and transcribe across speech and text (2023)
- Nextdoor — Predict harmful comments (2022)
- Wayfair — Predict intent in customer support messages (2022)
- Pinterest — Detect policy-violating comments (2021)

### CV / video / OCR (6)

- Apple — Identify objects on images (2023)
- Netflix — Improve video quality at scale (2022)
- Doordash — Extract information from images (2021)
- Bumble — Derive information from images (2020)
- Dailymotion — Automatically categorize videos (2020)
- Dropbox — Modern OCR with CV and DL (2017)

### Speech / audio (3)

- Netflix — Detect speech and music in audio (2023)
- Walmart — Fill shopping cart via voice dialog (2022)
- Amazon — Suggest music to listen to (2022)

### Marketing / churn / CLV / notify (14)

- Monzo — Select relevant marketing messages (2023)
- Expedia — Predict Customer Lifetime Value (CLV) (2023)
- Grab — Сreate scalable lookalike audiences (2023)
- Grab — Optimize promotional campaigns (2023)
- Gousto — Predict subscription churn (2022)
- Uber — Send timely push notifications (2022)
- Artefact — Evaluate success of past promotions (2022)
- Linkedin — Predict churn and upsell products (2022)
- Wayfair — Optimize email sending time and frequency (2022)
- Netflix — Apply causality in experiments and marketing (2022)
- Pinterest — Find lookalike users for ad targeting (2021)
- Wayfair — Optimize paid media marketing (2021)
- Doordash — Optimize marketing spending (2020)
- Lyft — Build a marketing automation platform (2019)

### Availability / inventory (5)

- DoorDash — Predict if a store is open (2023)
- Instacart — Predict availability of food items (2023)
- Instacart — Predict grocery item availability (2023)
- Instacart — Predict availability of food items (2023)
- Instacart — Predict grocery item availability (2018)

### ML platform / infra (2)

- King — Automate playtesting pipeline (2019)
- Uber — Scaling ML with Michelangelo (2019)

### Other (pricing, classification, routing, dimensions, …) (101)

- Foodpanda — Optimize menu sorting order (2023)
- Zillow — Estimate the house market value (2023)
- Airbnb — Identify user interests (2023)
- DoorDash — Optimize courier waiting time (2023)
- Linkedin — Select best payment gateway (2023)
- Yelp — Organize e-commerce content using embeddings (2023)
- Monzo — Detect patterns in text data (2023)
- Wayfair — Predict new product’s sales potential (2023)
- Wayfair — Identify business customers (2023)
- Criteo — Figure out users' preferences (2023)
- Grammarly — Suggest gender-inclusive grammatical error corrections (2023)
- Delivery Hero — Better understand user behavior (2023)
- Expedia — Alert users about optimal deals (2023)
- Walmart — Resolve entities and detect relationships (2023)
- Wayfair — Send relevant communications to customers (2023)
- Meta — Show users relevant content at scale (2023)
- GitHub — Automated code reviews and PR tagging (2023)
- Spotify — Target in-app messaging (2023)
- Nubank — Automatically route customer phone calls (2023)
- Mercado Libre — Predict product dimensions for delivery (2022)
- Walmart — Assist in e-commerce shopping (2022)
- Foodpanda — Classify restaurants and cuisines (2022)
- Github — Detect vulnerabilities in code (2022)
- Doordash — Find high-value merchants (2022)
- Grammarly — Suggest text edits (2022)
- Zillow — Select tags for product listings (2022)
- Airbnb — Improve customer support (2022)
- Walmart — Categorize e-commerce products (2022)
- Zillow — Identify customers that are likely to convert (2022)
- Zillow — Extract text features (2022)
- Lyft — Optimize trip price (2022)
- Grammarly — Correct grammatical errors (2022)
- Airbnb — Improve customer travel experience (2022)
- Swiggy — Flag incorrectly captured locations (2022)
- Uber — Verify documents (2022)
- Didact AI — Predict stock prices (2022)
- Wayfair — Identify specific entities within a text (2022)
- Oda — Predict driver's non-driving time (2022)
- Linkedin — Estimate the impact of product changes (2022)
- Siemens Healthineers — Optimize software testing (2022)
- Linkedin — Improve ML model performance with multitask learning (2022)
- Google — Suggest past photos to look at (2021)
- Uber — Identify cash intermediaries (2021)
- Microsoft — Cluster customer support issues by similarity (2021)
- Apple — Recognize people in photos (2021)
- Datto — Predict hard drive failures (2021)
- Bumble — Detect rude messages (2021)
- Nextdoor — Send relevant and timely updates (2021)
- Dropbox — Identify best time for renewal charge (2021)
- Brex — Classify bank transactions (2021)
- Grammarly — Capture what readers pay attention to (2021)
- Apple — Identify best user experience (2021)
- Airbnb — Data privacy and security (2021)
- Capital One — Identify suspicious account activity (2021)
- Wayfair — Assign color names to products (2021)
- Capital One — Automate incident management (2021)
- Walmart — Categorize e-commerce products (2021)
- Walmart — Identify refrigeration defrost (2021)
- Capital One — Improve cardholder experience (2021)
- Shopify — Categorize e-commerce products (2021)
- Amazon — Predict coordinates of delivery location (2021)
- PayPal — Predict declined transactions (2021)
- Slack — Predict Slack connect invites (2021)
- Grammarly — Detect grammatical errors (2021)
- Doordash — Deliver orders on time (2021)
- Lifen — Recognize PDF layout (2021)
- Bumble — Detect rude messages (2021)
- Swiggy — Estimate travel distance (2021)
- Scribd — Classify documents (2021)
- Google — Correct grammatical errors (2021)
- Nubank — Predict conversions and attract new customers (2021)
- Grammarly — Correct grammatical errors (2021)
- Scribd — Classify user-uploaded documents (2021)
- Oda — Predict driver's non-driving time (2021)
- Mercado Libre — Predict customer engagement and LTV (2021)
- Wayfair — Show relevant content to new customers (2021)
- Microsoft — Classify cloud workload types (2021)
- Github — Help users find contribution opportunities (2020)
- Mozilla — Predict the outcome of software tests (2020)
- Adyen — Predict probability of transaction success (2020)
- Lyft — Provide location suggestions (2020)
- Twitter — Predict value of ad requests (2020)
- Picnic — Predict delivery drop times (2020)
- Shopify — Categorize e-commerce products (2020)
- Gojek — Target cross-sell to existing users (2020)
- OLX — Detect stolen photos (2020)
- Duolingo — Teaching foreign languages (2020)
- Firefox — Automatically assign new untriaged bugs (2019)
- Zoominfo — Predict data accuracy (2019)
- Lyft — Predict location of traffic control elements (2019)
- Apple — Identify text language (2019)
- Stitch Fix — Extract information from customer notes (2019)
- Lyft — Detect errors in maps (2019)
- Wayfair — Model uplift (2019)
- Lyft — Predict rides and driver hours (2019)
- Netflix — Improve streaming quality (2018)
- Instacart — Optimize food delivery logistics (2017)
- Airbnb — Predict Value of Homes (2017)
- Netflix — Improve Streamning Quality (2018)
- Booking.com — 150 Successful Machine Learning Models (2019)
- Chicisimo — Grow User base using vertical ML approch (2019)
---

# PART 2 — The finding

## 2.1 Literacy is not buildability

Almost all public material about these case studies stops at **literacy**: you can follow the
architecture diagram, name the components, and hold an opinion about the trade-offs. That is
genuinely useful — it is most of what an interview tests. It is **not** enough to build one
unaided, and the gap is structural, not a matter of trying harder:

1. **The write-ups are published after the fact.** A production blog post reports the design
   that shipped. It omits the four that did not, the derivation that ruled them out, and the
   parameter that took a quarter to tune. You cannot reconstruct a system from its changelog.
2. **The textbooks and the systems never meet.** Academic sources are organised by *method*
   (matrix factorisation, ARIMA, GNNs); the case studies are organised by *problem* (why did
   this feed collapse onto head items). Nobody publishes the join. **Part 4 is that join** —
   one ceiling per family, carrying the derivation the blog post skipped.
3. **The largest families have the thinnest teaching material.** Recommend/feed (65) +
   Search/rank/ads (36) + "Other" (101) = **202 of 309 studies, 65% of the catalog** — and
   those three are exactly where the public curriculum is least coherent. There are excellent
   books on deep learning, which covers 19 studies. Retrieval, ranking economics, pricing,
   routing and entity resolution — two thirds of the real work — are scattered across
   conference papers, one-off course notes and vendor documentation.

## 2.2 What "from scratch" actually means here

Not "reproduce Netflix." Concretely, for each family, it means you can do all five:

| # | Capability | Test |
|---|---|---|
| 1 | **Derive** the core objective | Write the loss and its gradient on paper, no notes |
| 2 | **Implement** the estimator or index | Go code, property-tested, no ML framework |
| 3 | **Evaluate** it honestly | Offline metric + the bias it hides + the online check |
| 4 | **Scale** it | State the complexity, the sharding key, the failure mode |
| 5 | **Serve** it | Latency budget, staleness window, rollback plan |

Most curricula give you 1 and 3. Most bootcamps give you 2 with a framework and skip 1. The
309 case studies are almost entirely about 4 and 5. **A build curriculum has to hold all five
at once** — which is why Part 4 (theory), Part 5 (language) and Part 6 (implementation) are
braided rather than sequential.

## 2.3 Scope warning — read before opening Part 4

This is a multi-year programme if you open all of it, and **you are not supposed to open all of
it.** Every ceiling in Part 4 ends with an explicit **Stop at** line for exactly this reason.
Two failure modes to avoid:

- **Breadth-first collapse.** Reading the first three chapters of fifteen books teaches you
  nothing. One ceiling closed properly beats five left open.
- **Depth without a build.** A ceiling read but never implemented does not survive contact with
  the next problem. Part 6 is not optional homework; it is where the reading becomes yours.

**Recommended:** open **two** ceilings in your first year — one covering a large family
(T-IR or T-REC) and one cross-cutting (T-MLSYS). §6.15 gives the minimum viable path.

## 2.4 What is out of scope even with Part 4 open

Kaldi/OpenFst tooling courses · computer vision beyond Szeliski's recognition chapters ·
convex analysis at PhD depth · mechanism design beyond the auction chapters · training a
frontier-scale LLM · re-implementing the 309 blog posts individually. Part 4 **stocks the
shelf**; it does not add 309 lessons.

---

# PART 3 — The floor

Part 4's ceilings assume a floor. This part **is** that floor, and §3.0 starts it at genuine
zero — arithmetic — because a learner shaky on high-school algebra cannot bluff past §3.3 and
will simply stall in Part 4 without understanding why.

Three tiers, and **you climb only as far as the ceiling you are opening needs**:

```
TIER 0   Remedial — arithmetic → algebra → functions → precalculus      §3.0
HS       High-school gates inside each family                           §3.3
UG       Undergraduate gates — where most of Part 4 sits                 §3.3
GRAD     Graduate gates — needed by four ceilings only                   §3.3
```

**Skip-testing.** Every gate below is written as something you *do*, not something you *read*.
If you can do it cold, skip the tier — do not re-read the chapter to feel safe. If you cannot,
that is your tier, regardless of what your transcript says.

## 3.0 Tier 0 — the remedial on-ramp

**Read this section if** you would hesitate at *"solve 3x + 7 = 22"*, *"what is 15% of 80"*,
*"what does log₂(1024) mean"*, or *"sketch y = x²"*. That is a common and completely fixable
starting point. It is also **disqualifying for Part 4 if left alone** — every ceiling there
rests on algebra you can manipulate without thinking about it.

The order matters; each rung is load-bearing for the next.

| # | Rung | You can… | Free source |
|---|---|---|---|
| **0.1** | Arithmetic, fractions, percentages | add/multiply fractions; convert %↔fraction↔decimal; estimate without a calculator | Khan Academy *Arithmetic* → *Pre-algebra* |
| **0.2** | Negatives, exponents, roots | simplify \(x^a x^b\), \((x^a)^b\), \(x^{-1}\), \(\sqrt{x}=x^{1/2}\) | Khan *Pre-algebra*; OpenStax *Prealgebra* |
| **0.3** | Algebra I — linear equations | solve for \(x\); rearrange a formula; solve two equations in two unknowns | Khan *Algebra 1*; OpenStax *Elementary Algebra* |
| **0.4** | Inequalities, absolute value | solve \(|x-3|<5\); read \(\le\) as a ceiling on a resource | OpenStax *Elementary Algebra* |
| **0.5** | Functions | say what \(f(x)\) *is*; find domain/range; compose \(f(g(x))\); spot a non-invertible function | Khan *Algebra 2*; OpenStax *Algebra and Trigonometry* Ch. 1–3 |
| **0.6** | Exponentials and logarithms | convert \(2^{10}=1024 \leftrightarrow \log_2 1024 = 10\); explain why logs turn products into sums | OpenStax *Algebra and Trigonometry* Ch. 6 |
| **0.7** | Sequences, sums, sigma notation | expand \(\sum_{i=1}^{n} x_i\); write a mean as a sum over \(n\) | OpenStax *Algebra and Trigonometry* Ch. 13 |
| **0.8** | Coordinate geometry, slope | slope as rise/run; slope as a rate of change | Khan *Algebra 1* |
| **0.9** | Trigonometry, lightly | sin/cos on the unit circle — genuinely all you need until §4.9 | OpenStax *Precalculus* Ch. 5 |
| **0.10** | Counting and basic probability | permutations vs combinations; \(P\) as favourable/total; read a two-way table | Khan *Statistics and Probability*, intro units |
| **0.11** | Precalculus wrap-up | limits informally; how functions behave at scale | OpenStax *Precalculus* |

**Then, and only then, a first calculus pass.** You need derivatives before §3.3's `T.CalcOpt`
and before anything in Part 4 involving a gradient: OpenStax *Calculus* Vol. 1 Ch. 1–4, or
MIT **18.01SC** (OCW, free, with full problem sets), or Khan *Calculus 1*.

**Tier 0 exit gate — all five, cold, no notes:**

1. Solve \(3x + 7 = 22\), then rearrange \(A = \pi r^2\) for \(r\).
2. Given \(f(x) = 2x+1\) and \(g(x) = x^2\), write \(f(g(x))\) and \(g(f(x))\) and show they differ.
3. Explain in one sentence why \(\log(ab) = \log a + \log b\), and compute \(\log_2 1024\).
4. Expand \(\sum_{i=1}^{4} i^2\) to a number.
5. Differentiate \(f(x) = x^2\) from the definition \(\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}\).

If #5 is out of reach today, **the rest of this file still works**: do Part 5 (Go) and **B0,
B1 and B7** from Part 6 while you close Tier 0. Programming and mathematics genuinely run in
parallel, and B7 — a search engine — needs almost no calculus.

**Supplements worth the time.** 3Blue1Brown's *Essence of Calculus* and *Essence of Linear
Algebra* (YouTube, free) — watch them before, not instead of, the exercises; they build the
intuition that stops the algebra feeling arbitrary. Professor Leonard's full lecture recordings
(YouTube, free) if you want a real classroom pace. Paul's Online Math Notes
(`tutorial.math.lamar.edu`) is the best free worked-example reference from algebra through
multivariable calculus.

**The honest timeline.** Tier 0 from a genuinely shaky start is **4–8 months** at 6–10 hours a
week. That is not a detour from this curriculum — for a learner in that position it *is* its
first phase, and skipping it is the most reliable way to fail Part 4.

## 3.1 How the floor maps to the ceilings

| Floor family (§3.3–3.4) | Tier needed | Feeds which ceiling |
|---|---|---|
| **T.Quant** — units, magnitudes | HS | every capacity estimate in Part 6 |
| **T.Alg** — algebra, functions | HS→UG | all of Part 4 |
| **T.Disc** — logic, proof, counting, graphs | HS→UG | T-GRAPH, T-OPT, T-ER |
| **T.LA** — vectors, matrices, SVD | UG→GRAD | T-REC, T-GRAPH, T-DL |
| **T.CalcOpt** — derivatives, gradients, convexity | UG→GRAD | T-DL, T-OPT |
| **T.ProbStat** — probability, estimation, information | HS→GRAD | T-CAUSAL, T-RL, T-MLSYS |
| **T.Algo** — data structures, complexity, hashing | UG→GRAD | T-IR, T-GRAPH, T-ER |
| **T.SysTheory** — reliability, networks, distributed, DB, security | UG→GRAD | T-STREAM, T-MLSYS, §4.15 |
| **T.MLTheory** — generalisation, PAC/VC, calibration | UG→GRAD | T-REC, T-IR, T-DL |
| **M.NS** — floating point, conditioning | — | T-DL, T-MLSYS · build **B0** |
| **M.ML** — empirical risk, losses, metrics, IPS | — | T-REC, T-IR, T-RL · builds **B2, B3** |
| **M.TS** — decomposition, time cuts | — | T-TS · build **B9** |
| **M.CAUSAL** — potential outcomes | — | T-CAUSAL · build **B12** |

## 3.2 Minimum floor per ceiling

Open a ceiling in Part 4 only when its row's floor is closed. This is the entire dependency
graph — nothing else gates anything.

| Ceiling | Floor required first |
|---|---|
| **T-IR** §4.2 | T.Algo UG · T.Disc UG · M.ML |
| **T-REC** §4.1 | T.LA UG · M.ML (incl. IPS) · T.MLTheory UG |
| **T-AUCTION** §4.3 | T.ProbStat UG · T.Alg UG |
| **T-TS** §4.4 | M.TS · T.ProbStat UG · T.LA UG |
| **T-GRAPH** §4.5 | T.Disc UG · T.Algo UG · T.LA GRAD (spectral) |
| **T-DL** §4.6 | T.CalcOpt UG→GRAD · T.LA UG · M.NS |
| **T-NLP** §4.7 | T.ProbStat UG · T-DL (in part) |
| **T-CV** §4.8 | T.LA UG · T-DL |
| **T-SIGNAL** §4.9 | T.CalcOpt UG · T.LA UG |
| **T-CAUSAL** §4.10 | T.ProbStat UG→GRAD · M.CAUSAL |
| **T-STREAM** §4.11 | T.SysTheory Distributed UG · T.Disc UG |
| **T-MLSYS** §4.12 | T.SysTheory Reliability + Net UG · M.NS |
| **T-OPT / T-ER** §4.13 | T.Alg UG · T.Disc UG · T.LA UG |
| **T-RL** §4.14 | T.ProbStat GRAD (concentration) · M.ML IPS |
| **§4.15 SWE** | T.SysTheory UG |

## 3.3 The nine theory families

`T.*` are this file's own labels, defined here. Each family lists gates by tier; a
**derive/prove gate** is what you must be able to *do* to claim that tier.

### T.Quant — quantities, units, orders of magnitude
*Feeds:* every capacity and cost estimate in Part 6; the latency budgets in B14.

- **HS gate.** SI prefixes n…G; scientific notation; order-of-magnitude *class*; unit cancel in `qty × rate`; reject `ms + MB`. → `to_seconds`, `sci`, napkin helpers → Go `units`.
- **UG gate.** Dimensional homogeneity; GiB vs GB disclosure; latency ≈ distance/speed + RTT class labels. → `rtt_ms` + order-band asserts.
- **Grad-as-needed.** Uncertainty propagation for FinOps/SLO numerics beyond M.NS tolerance — rare.
- *Sources:* OpenStax *Prealgebra* / quantitative literacy.

### T.Alg — algebra through inequalities, functions, composition
*Feeds:* all modelling notation; M.ML's \(f\); every ceiling in Part 4.

- **HS gate.** Linear solve; proportions; % ↔ fraction; inequalities as ceilings; function = unique output; rise/run.
- **UG gate.** Domain/codomain/range; false-inverse counterexample; composition on finite maps; logs/exponents for orders; piecewise defs.
- **Grad-as-needed.** Abstract-algebra slogans only if a force needs pipeline monoid rigor.
- *Sources:* OpenStax *Algebra and Trigonometry* / *Precalculus*; Hall & Knight as used.

### T.Disc — logic, sets, proofs, counting, graphs, invariants, asymptotics
*Feeds:* T-GRAPH §4.5, T-OPT §4.13 (NP-hardness), T-ER §4.13; hashing and Bloom-filter intuition in B7.

- **HS gate.** Sets ∪∩∖⊆; Boolean ∧∨¬ + truth table; row predicates; product rule; \(2^w\); pigeonhole; binary/hex/bit vs byte.
- **UG gate.** Direct/contrapositive/contradiction/induction; relations; counting as used; graph BFS/DFS literacy; representation invariants; big-O from a loop. → proof portfolio + tested structure with named invariant.
- **Grad-as-needed (T-TOC lite).** Automata/complexity literacy only when a main-track force needs it.
- *Sources:* Rosen *Discrete Mathematics*; Hammack *Book of Proof*; MIT 6.042J.

### T.LA — vectors, matrices, norms, least squares, eigen/SVD as used
*Feeds:* T-REC §4.1 (embeddings, two-tower), T-GRAPH §4.5 (spectral), T-DL §4.6; builds B1, B4.

- **UG gate.** \(\mathbb{R}^n\) as used; norms; dot → cosine; matrix–vector; least squares + residual \(\|Ax-b\|\); rank/nullity on small examples. → NumPy-free kernels then NumPy compare; cosine degenerates.
- **Grad gate.** Four subspaces; QR idea; eigen/SVD; PCA reconstruction error; \(\kappa_2=\sigma_{\max}/\sigma_{\min}\). → power iteration / PCA residual.
- *Sources:* Strang *Introduction to Linear Algebra*; MIT 18.06; Trefethen & Bau / Golub & Van Loan as used.

### T.CalcOpt — limits, derivatives, gradients, convexity, GD/Lagrange
*Feeds:* M.ML gradient descent, T-DL §4.6 (backprop), T-OPT §4.13; builds B2, B11.

- **UG gate.** Derivative as local linearization; chain rule on scalar losses; \(\nabla\frac12\|Ax-b\|^2\); convexity cartoon; GD with chosen step; Lagrange slogan for one equality. → FD gradient checker vs analytic; tiny GD on quadratic.
- **Grad gate.** Jacobian/Hessian as used; KKT literacy; convex vs nonconvex failure modes; duality as used by T-OPT.
- *Sources:* MIT 18.01SC/18.02SC; OpenStax *Calculus*; Nocedal & Wright / Boyd & Vandenberghe at grad; Stanford EE364A/B as used.

### T.ProbStat — probability spaces, RVs, estimation, tests, information
*Feeds:* M.ML metrics, M.CAUSAL conditionals, T-CAUSAL §4.10, T-RL §4.14 (concentration), drift detection in B14.

- **HS gate.** Sample space; equally likely \(P\); disjoint additivity; independence cartoon; conditional-by-table; mean/median/percentile; rates; \(\sum\) / mean of indicators.
- **UG gate.** RV, \(\mathbb{E}\), Var; LLN/CLT statement + simulation check; MLE on Bernoulli/Gaussian; CI/test literacy; entropy/CE/KL **definitions**.
- **Grad gate.** (1) a.s. vs in-probability convergence on a concrete sequence. (2) Sufficiency: sample mean sufficient for Bernoulli \(p\) via factorization. (3) State Cramér–Rao and check a Bernoulli MLE numerically. (4) Bonferroni on a 5-test toy + one sequential-testing caveat (used by B12). (5) Prove \(D_{\mathrm{KL}}(p\|q)\ge 0\) via Jensen; use CE/KL to explain a calibration/drift alarm.
- *Sources:* MIT 6.041SC; Wasserman *All of Statistics*; Casella–Berger; Grinstead & Snell; Cover & Thomas for info.

### T.Algo — data structures, invariant-based algorithms, complexity, hashing
*Feeds:* T-IR §4.2 (index construction), T-GRAPH §4.5, T-ER §4.13; builds B7, B10, B10b.

- **UG gate.** Array/slice/map/heap/tree/union-find contracts; loop invariants; amortized growth; hash families + collision *language*; sorting lower-bound intuition; BFS/DFS/Dijkstra as used; Master theorem on one recurrence. → **Go-first** for structures; property tests; complexity argument before code.
- **Grad-as-needed.** External-memory and cache-aware structures — needed once B7's index stops fitting in RAM.
- *Sources:* CLRS; Sedgewick & Wayne; MIT 6.006.

### T.SysTheory — formal models behind the main track
Product labs stay in Parts 2/4/6/7/8/10. Five subfamilies, each UG + grad-as-needed:

**Reliability** — feeds T-MLSYS §4.12 and B14's SLO and rollback logic.
- *UG.* Series availability \(\prod A_i\), parallel \(1-\prod(1-A_i)\) from independence; name the independence assumption; SLI/SLO vocabulary **without** burn formula.
- *Grad.* Error-budget identity: budget = \((1-\mathrm{SLO})\times\mathrm{window}\); multi-window burn ratio as rate-of-spend; renewal/reward MTBF vs availability, one worked numeric.

**Networking** — feeds T-MLSYS §4.12 (serving economics) and T-STREAM §4.11 (backpressure).
- *UG.* (1) Encapsulation — payload wrapped by successive headers. (2) L2 vs L3 with one counterexample where broadcast domain ≠ L3 subnet. (3) Address + mask → network ID and host range; prove two addresses share a partition or not. (4) Subnet as address partition — not a virtual network, a region, or a firewall. (5) Routing as graph path — longest-prefix next hop; show a blackhole. (6) Failure domain vs trust boundary. (7) End-to-end argument + counterexample where hop-by-hop checksum is insufficient. (8) AIMD: on ACK \(w\leftarrow w+1/w\), on loss \(w\leftarrow w/2\) — simulate 20 RTTs.
- *Grad.* Little's law \(L=\lambda W\) derived from arrival/departure counts over \([0,T]\); apply to RPS × latency → concurrency. One fairness/stability trade-off of a TCP variant.
- *Sources:* Kurose/Ross or Tanenbaum & Wetherall; Saltzer–Reed–Clark.

**Distributed systems.**
- *UG.* Happens-before on a 3-process timeline (prove one pair incomparable); CAP — which two you keep under a named partition; consensus safety vs liveness.
- *Grad.* Quorum intersection for majority quorums \(\lfloor n/2\rfloor+1\); FLP impossibility (async + one crash) and why production adds timeouts/partial synchrony; linearizability vs serializability — one schedule serializable but not linearizable.
- *Sources:* DDIA + Lynch-lite / MIT 6.5840 as used.

**DB theory** — feeds T-STREAM §4.11 (exactly-once, checkpoints) and §4.15.
- *UG.* Push a selection through a join; keys/FDs justifying 3NF on a 4-attribute toy; one dirty-read and one lost-update schedule; WAL durability argument.
- *Grad.* MVCC snapshot — given begin-ts/commit-ts of two writers, decide which version a reader sees, prove no dirty read under SI; cost-model row estimation given selectivity.
- *Sources:* Ramakrishnan/Gehrke; PostgreSQL docs; CMU 15-445.

**Security theory.**
- *UG.* STRIDE-as-used on a toy HTTP+DB diagram; authz as predicate `allow(principal, action, resource)` with a SoD counterexample; state discrete-log / factoring hardness *as used* — no cipher design.
- *Grad.* Sketch one reduction shape ("if adversary breaks X then oracle Y breaks hardness Z") for a stdlib primitive you **call**. **Never invent ciphers.**
- *Sources:* Katz–Lindell / Goldreich only if T-CRYPTO ceiling opened.

**Information & coding lite.**
- *UG/Grad.* Erasure vs replication: 3-way replication vs Reed–Solomon k-of-n — storage overhead and surviving-failure count on a toy.

### T.MLTheory — statistical learning theory
*Feeds:* T-REC §4.1, T-IR §4.2 (LTR objectives), T-DL §4.6 (generalisation). Implementations
and the IPS derivation live in **M.ML** §3.4, not here.

- **UG gate.** Train/test rationale; bias–variance with a derive-able quadratic example; overfitting vs generalization gap; ranking utility foundations without stealing IPS.
- **Grad gate.** (1) PAC: state \((\varepsilon,\delta)\)-learnability; sample-size bound \(m \gtrsim \frac{1}{\varepsilon^2}\log\frac{1}{\delta}\) for a finite class. (2) VC-dimension of thresholds on \(\mathbb{R}\). (3) Relate train–test gap to a complexity term. (4) ECE on a 3-bin reliability diagram. (5) Pairwise logistic/hinge ranking loss; show how a score swap changes it. (6) Covariate/label shift — broken assumption + monitoring signal.
- *Sources:* ISL 2e; Wasserman ML chapters; Shalev-Shwartz & Ben-David as used.

## 3.4 The four quantitative kits (M.*)

Four kits sitting between the theory families and the builds. Each owns a specific set of
derivations, so that no formula has two homes (§3.5).

| Topic | Complete means |
|---|---|
| Bits, integers, floats, error, tolerance | Full IEEE/conditioning/Kahan/logsumexp in **M.NS** → build **B0** |
| Functions, composition, inverse | Counterexample to a false inverse claim |
| Vectors, norms, dot, cosine | Derive cosine; degenerate cases |
| Matrices, least squares, SVD/PCA as used | Residual and reconstruction error |
| Probability: sample space, conditional-by-table | T.ProbStat owns language; M.ML owns ERM/metrics/IPS |
| Entropy, cross-entropy, KL as used | Derive CE from likelihood |
| Recurrences, Master theorem | Match a loop to a recurrence |
| Limits, derivatives, integrals as used | Derive the move; numerics with tolerance |
| Convex sets/functions, GD, Lagrange | KKT as used; not a convex-analysis PhD unless T-OPT opened |
| Sampling theorem / DFT as used | Predict aliasing (T-SIGNAL §4.9) |
| Strided arrays (`ndarray`-style) | Predict shape/dtype/strides/broadcast; copy vs view → build **B1** |
| Ranking / IPS / position bias | Derive propensity + Horvitz–Thompson IPS on synthetic click logs |
| Classical time series | Decompose tiny series; when BQML ARIMA/seasonal beats DL |
| Causal / uplift lite | Two-arm toy; uplift = treatment effect |

**M.NS — numerical stability.** IEEE-754 binary64/32 (sign, biased exponent, significand, subnormals, ±0/±∞/NaN); rounding modes, machine ε, ulp, \(fl(x)=x(1+\delta)\); absolute vs relative, forward vs backward error; **condition number of a problem κ vs stability of an algorithm**; catastrophic cancellation; FP add non-associativity; overflow/underflow; FMA; reformulation (`log1p`, `expm1`, `hypot`, two-sum/Kahan); \(\kappa_2(A)=\sigma_{\max}/\sigma_{\min}\), residual vs true error, Hilbert trap; **softmax overflow, log-sum-exp, scaled dot-product attention \(1/\sqrt d\)**; never `==` on computed floats; Python unbounded ints vs Go `int64` wrap (GO-1); money as integer cents.
*Gate:* derive κ vs stability; predict a cancellation failure, then exhibit it in code (build **B0**).

**M.ML — empirical risk, losses, metrics (+ IPS).**
- Empirical risk \(\hat{R}(f)=\frac1n\sum_i \ell(f(x_i),y_i)\); i.i.d. fails under time/group/target leakage. A random 80/20 on time-ordered events is a defect until proven otherwise.
- MSE: \(\nabla_w \hat{R}(w)=\frac{2}{n}X^\top(Xw-y)\); GD step \(w \leftarrow w-\eta\nabla\).
- Logistic from likelihood: \(\ell=-y\log p-(1-y)\log(1-p)\), derive \(\partial\ell/\partial w=(p-y)x\).
- L2: \(\hat{R}_\lambda=\hat{R}+\frac{\lambda}{2}\|w\|_2^2\); L1 sparsity cartoon.
- Metrics implemented, not imported: precision, recall, F1, ROC/AUC as pairwise ranking probability, PR curve, **calibration / reliability / ECE**.
- **IPS / position bias:** \(\mathbb{E}[c_{i,k}]=p_k\cdot r_i\); \(\hat{R}_{\mathrm{IPS}}(f)=\frac1n\sum_i \frac{c_i}{\hat p_{k(i)}}\ell(f(x_i),\tilde y_i)\); clip propensities, report effective sample size.
*Gate:* derive log-loss gradient for one example and match code; compute P/R/F1 and one ROC point by hand; name a metric that would hide a failure in fraud vs catalog rank.

**M.TS — classical time series.** \(y_t=T_t+S_t+R_t\) (multiplicative when amplitude scales); residual ACF; **time cut only**, never a shuffle. *Gate:* decompose one series; state when classical seasonal beats DL.

**M.CAUSAL — causal / uplift lite.** Potential outcomes \(Y_i(1), Y_i(0)\); ATE \(=\mathbb{E}[Y(1)-Y(0)]\); randomization → difference in means unbiased (SUTVA caveat); observational confounding; **uplift = conditional treatment effect**, not high baseline \(Y\). *Gate:* two-arm delta by hand and in code; write "an experiment is not a causal model" in your notes whenever a case study claims causality from observational data.

## 3.5 One home per formula

Every formula has exactly **one** home, so revising it revises it everywhere:

**M.NS** owns IEEE-754, machine ε, Kahan, log-sum-exp, money-as-integer ·
**M.ML** owns empirical risk, losses, P/R/F1, ROC/AUC, calibration, IPS ·
**M.TS** owns trend/seasonality decomposition · **M.CAUSAL** owns potential outcomes ·
**T.Algo** owns hashing and the Bloom FPR \((1-e^{-kn/m})^k\) ·
**T.SysTheory Reliability** owns availability algebra and SLO burn-rate ·
**T-IR §4.2** owns BM25 and the index · **T-REC §4.1** owns MF and two-tower ·
**T-RL §4.14** owns regret. **Never invent ciphers** — call a vetted library.

---

# PART 4 — The ceilings

## 4.0 Bridge — which floor family feeds which ceiling

Part 3 is the **floor**; the ceilings are what each family needs *above* it to build unaided.
This is the join that the textbooks and the case studies never make for you.

| Floor family (Part 3) | Already sufficient for | Ceiling it feeds |
|---|---|---|
| T.LA UG→grad | embeddings, cosine, PCA residual | **T-REC** (MF/two-tower), **T-GRAPH** (spectral/node embeddings) |
| T.CalcOpt UG→grad | one GD step, convexity cartoon, KKT literacy | **T-DL** (backprop), **T-OPT** (LP/duality, solvers) |
| T.ProbStat grad | MLE, CLT, KL ≥ 0, multiple comparison | **T-CAUSAL** (identification), **T-RL** (regret proofs) |
| T.MLTheory grad | PAC/VC, ECE, pairwise ranking loss, shift | **T-REC**/**T-IR** (LTR objectives), **T-DL** (generalization) |
| T.Algo UG→grad | hashing, heaps, BFS/DFS/Dijkstra, external memory | **T-IR** (index construction), **T-GRAPH** (CC at scale), **T-ER** (blocking) |
| T.Disc UG | invariants, counting, graph literacy | **T-GRAPH**, **T-OPT** (combinatorial formulation) |
| T.SysTheory Distributed + DB | quorums, linearizability, MVCC, WAL | **T-MLSYS** (parallel training), **T-STREAM** (exactly-once) |
| T.SysTheory Reliability + Net | availability algebra, Little's law | **T-MLSYS** (serving economics, concurrency) |
| M.ML (+ IPS) | ERM, metrics, off-policy weighting | **T-REC**, **T-RL** (off-policy eval), **T-IR** |
| M.TS | decomposition, time cut | **T-TS** (ETS/ARIMA/hierarchical) |
| M.CAUSAL | potential outcomes, two-arm delta | **T-CAUSAL** (DAGs, IV/DiD, CUPED) |
| M.NS | LSE, softmax, \(1/\sqrt d\), tolerance | **T-DL** (stable training), **T-MLSYS** (quantization) |

**Read this as:** every ceiling below already has its floor built in Part 3. Nothing in Part 4
asks you to start from zero — it asks you to climb from a gate you have already passed.
## 4.0b How to read a ceiling entry

Each entry below has the same six fields. **Derive** is the contract — if you cannot produce
those objects on paper, the reading did not land, regardless of how much of it you finished.

```
Covers   which families and how many of the 309
Derive   the objects you must be able to produce unaided — this is the gate
Text     primary reading, with the chapters that matter
Depth    secondary sources, entered only when the primary is exhausted
Course   lecture material: Ivy League, peer institution, IIT/IISc/NPTEL
Papers   the canon — read after the text, not instead of it
Stop at  the explicit upper bound, so the ceiling stays finite
Build    the Part 6 rung this stocks
```

---

## 4.1 T-REC — recommendation

**Covers.** Recommend / personalize / feed (65) — the largest family in the catalog, and the
one with the least coherent public teaching path.

**Derive.**
1. Implicit-feedback ALS: from \(\min_{X,Y}\sum_{u,i} c_{ui}(p_{ui} - x_u^\top y_i)^2 + \lambda(\|X\|^2+\|Y\|^2)\),
   derive the closed-form alternating update \(x_u = (Y^\top C^u Y + \lambda I)^{-1} Y^\top C^u p(u)\)
   and explain why the \(Y^\top Y\) precompute makes it \(O(f^2 n_u + f^3)\) per user, not \(O(f^2 |I|)\).
2. BPR: write the pairwise objective \(\sum \ln\sigma(\hat{x}_{uij}) - \lambda\|\Theta\|^2\) and its
   SGD update; explain why it optimizes AUC and not RMSE.
3. Two-tower: write the sampled-softmax loss, then the **logQ correction**
   \(s^{c}(x,y) = s(x,y) - \log p(y)\), and say what breaks without it (popularity collapse).
4. Show that a random 80/20 split on time-ordered interaction logs leaks the future, and give
   the leave-one-last-item or time-cut alternative.
5. NDCG@k from first principles; then show a case where NDCG improves and satisfaction drops.
6. Cold start: write the content-feature fallback as a rank-1 prior on the item factor.

**Text.** Aggarwal, *Recommender Systems: The Textbook* (Springer 2016) — **Ch. 2–3** (neighbourhood
+ model-based CF), **Ch. 7** (evaluation), **Ch. 13** (bandits / LTR). Author-hosted PDF **[free]**.
Leskovec, Rajaraman & Ullman, *Mining of Massive Datasets* 3e **[free]** — **Ch. 9** (recsys),
**Ch. 3** (LSH/near-neighbour), **Ch. 11** (dimensionality reduction), **Ch. 12** (large-scale ML).

**Depth.** Ricci, Rokach & Shapira (eds.), *Recommender Systems Handbook* 3e (Springer 2022) **[paid]**
— the reference, not a read-through. Falk, *Practical Recommender Systems* (Manning 2019) **[paid]**
for the plumbing view.

**Course.** Stanford **CS246** *Mining Massive Data Sets* (MMDS is its text; slides + assignments
public). Cornell **CS 4/5780** for the supervised-learning half. NPTEL **Data Mining**
(Pabitra Mitra, IIT Kharagpur, `106105174`).

**Papers.**
Koren, Bell & Volinsky, "Matrix Factorization Techniques for Recommender Systems" (IEEE Computer 2009) ·
Hu, Koren & Volinsky, "Collaborative Filtering for Implicit Feedback Datasets" (ICDM 2008) ·
Rendle et al., "BPR: Bayesian Personalized Ranking from Implicit Feedback" (UAI 2009) ·
Covington, Adams & Sargin, "Deep Neural Networks for YouTube Recommendations" (RecSys 2016) ·
Yi et al., "Sampling-Bias-Corrected Neural Modeling for Large Corpus Item Recommendations" (RecSys 2019) ·
Cheng et al., "Wide & Deep Learning for Recommender Systems" (2016) ·
Kang & McAuley, "Self-Attentive Sequential Recommendation" (ICDM 2018) ·
Ying et al., "Graph Convolutional Neural Networks for Web-Scale Recommender Systems" (PinSage, KDD 2018) ·
Dacrema, Cremonesi & Jannach, "Are We Really Making Much Progress?" (RecSys 2019 — read this one **before** the deep-learning papers) ·
Krichene & Rendle, "On Sampled Metrics for Item Recommendation" (KDD 2020).

**Stop at.** No survey of every neural architecture. Two-tower + MF + one sequential model is
the whole ceiling. Graph-based recs hand off to **T-GRAPH §4.5**; bandit re-ranking hands off
to **§4.14**.

**Build.** B6.

---

## 4.2 T-IR — search, indexing and learning-to-rank

**Covers.** Search / rank / ads (36), plus the retrieval half of every RAG study in family 5.

**Derive.**
1. The inverted index as a data structure: posting-list layout, skip pointers, the
   \(O(\sum |p_t|)\) cost of an AND query, and why document-ordered beats impact-ordered for
   conjunctions but not for top-k.
2. BM25 from the probabilistic relevance framework:
   \(\sum_t \mathrm{IDF}(t)\cdot\frac{f_{t,d}(k_1+1)}{f_{t,d}+k_1(1-b+b\cdot |d|/\overline{|d|})}\)
   — explain each of \(k_1\), \(b\), and why raw TF saturates.
3. Compression: variable-byte and PForDelta on a gap-encoded posting list; compute the
   bits/posting you actually achieved.
4. WAND / block-max WAND: prove that skipping a document whose upper bound is below the
   current threshold cannot change top-k.
5. HNSW: state the layer-assignment geometric distribution, the greedy-descent search
   invariant, and the recall/`efSearch` trade-off curve you measured.
6. LTR: write the pairwise logistic (RankNet) loss and derive its gradient; then state the
   LambdaRank λ-gradient and why it optimises a non-differentiable metric.
7. Position bias: derive \(\mathbb{E}[c_{i,k}] = p_k\cdot r_i\) under the examination model and
   the IPS estimator \(\hat{R}_{\mathrm{IPS}} = \frac1n\sum_i \frac{c_i}{\hat p_{k(i)}}\ell(\cdot)\);
   show what propensity clipping does to bias and variance.

**Text.** Manning, Raghavan & Schütze, *Introduction to Information Retrieval* (Cambridge 2008)
**[free]** — **Ch. 1–2** (index, tokenisation), **4** (construction), **5** (compression),
**6–7** (scoring, efficient top-k), **8** (evaluation), **11** (probabilistic / BM25 roots),
**19–21** (web, crawling, link analysis). Büttcher, Clarke & Cormack, *Information Retrieval:
Implementing and Evaluating Search Engines* (MIT Press 2010) **[paid]** — the implementation
companion; **Ch. 4–6** are what you code against.

**Depth.** Liu, *Learning to Rank for Information Retrieval* (Springer 2011) **[paid]** ·
Robertson & Zaragoza, *The Probabilistic Relevance Framework: BM25 and Beyond* (FnTIR 2009) —
the definitive BM25 derivation · Lin, Nogueira & Yates, *Pretrained Transformers for Text
Ranking: BERT and Beyond* (Morgan & Claypool 2021, arXiv **[free]**).

**Course.** Stanford **CS276** *Information Retrieval and Web Search* (Manning's own course;
IIR is its text). NPTEL **Introduction to Information Retrieval** (SWAYAM). Stanford CS246 for
the LSH/ANN half. CMU **11-642** *Search Engines* for the implementation-heavy variant.

**Papers.**
Robertson & Zaragoza (FnTIR 2009) · Burges, "From RankNet to LambdaRank to LambdaMART: An
Overview" (MSR-TR-2010-82) · Malkov & Yashunin, "Efficient and Robust Approximate Nearest
Neighbor Search Using Hierarchical Navigable Small World Graphs" (TPAMI 2018) ·
Johnson, Douze & Jégou, "Billion-Scale Similarity Search with GPUs" (FAISS, 2017) ·
Guo et al., "Accelerating Large-Scale Inference with Anisotropic Vector Quantization" (ScaNN, ICML 2020) ·
Huang et al., "Learning Deep Structured Semantic Models…" (DSSM, CIKM 2013) ·
Karpukhin et al., "Dense Passage Retrieval for Open-Domain QA" (EMNLP 2020) ·
Khattab & Zaharia, "ColBERT" (SIGIR 2020) ·
Joachims, Swaminathan & Schnabel, "Unbiased Learning-to-Rank with Biased Feedback" (WSDM 2017) ·
Broder et al., "Efficient Query Evaluation Using a Two-Level Retrieval Process" (WAND, CIKM 2003).

**Stop at.** No neural-IR survey, no crawler at web scale. You build one lexical index, one
vector index, one hybrid fusion rule, one LTR objective.

**Build.** B7.

---

## 4.3 T-AUCTION — ads, auctions and mechanism design

**Covers.** The ads half of family 2 (a substantial share of the 36), plus every "select best
payment gateway / bid optimisation" study in family 12.

**Derive.**
1. Second-price (Vickrey) auction: prove truthful bidding is a dominant strategy.
2. GSP: show it is **not** truthful, construct the two-bidder counterexample, and locate the
   envy-free equilibrium that makes it work in practice anyway.
3. VCG payment rule; compute it on a three-slot toy and compare revenue to GSP.
4. eCPM ranking: \(\text{rank score} = \text{bid} \times \text{pCTR} \times \text{quality}\) —
   show how miscalibrated pCTR distorts allocation, not just revenue.
5. Reserve prices: derive the optimal reserve for a single bidder with uniform value
   (Myerson's virtual value \(\psi(v)=v-\frac{1-F(v)}{f(v)}\)).
6. Budget pacing as a control problem: state it, and name the feedback signal.

**Text.** Narahari, *Game Theory and Mechanism Design* (IISc Press / World Scientific 2014)
**[paid]** — the auction and mechanism-design chapters are exactly the right depth; written by
the IISc course's own instructor. Easley & Kleinberg, *Networks, Crowds, and Markets*
(Cambridge 2010) **[free]** — **Ch. 9** (auctions), **Ch. 15** (sponsored search markets), and
**Ch. 10** (matching markets).

**Depth.** Nisan, Roughgarden, Tardos & Vazirani (eds.), *Algorithmic Game Theory* (Cambridge
2007) **[free]** — **Ch. 9, 11, 28**. Roughgarden, *Twenty Lectures on Algorithmic Game
Theory* (Cambridge 2016) **[paid]**; his lecture videos and notes are **[free]**.

**Course.** **IISc E1 254** *Game Theory* (Narahari, CSA). NPTEL **Game Theory and Mechanism
Design** (`noc22_cs77`). Cornell **INFO 2040 / CS 2850** *Networks* — Easley & Kleinberg is
literally that course's textbook. Stanford CS246 covers computational advertising as a unit.

**Papers.**
Vickrey, "Counterspeculation, Auctions, and Competitive Sealed Tenders" (J. Finance 1961) ·
Myerson, "Optimal Auction Design" (Math. OR 1981) ·
Edelman, Ostrovsky & Schwarz, "Internet Advertising and the Generalized Second-Price Auction"
(AER 2007) · Varian, "Position Auctions" (IJIO 2007) ·
McMahan et al., "Ad Click Prediction: a View from the Trenches" (KDD 2013) — read with §4.12 ·
He et al., "Practical Lessons from Predicting Clicks on Ads at Facebook" (ADKDD 2014).

**Stop at.** Narahari's auction chapters. No mechanism-design PhD, no general equilibrium.

**Build.** B8.

---

## 4.4 T-TS — forecasting, ETA and demand

**Covers.** Forecast / ETA / demand (27), plus the demand half of family 10.

**Derive.**
1. Decomposition \(y_t = T_t + S_t + R_t\) (additive) vs \(T_t\cdot S_t\cdot R_t\) (multiplicative);
   state the test that tells you which.
2. ETS state-space form: write Holt–Winters additive as its recursions
   \(\ell_t, b_t, s_t\) and identify each smoothing parameter's role.
3. ARIMA: stationarity, the ACF/PACF identification rules, and why differencing changes the
   meaning of the forecast interval. Derive the one-step-ahead forecast for AR(1).
4. Quantile / pinball loss \(L_\tau(y,\hat y) = \max(\tau(y-\hat y), (\tau-1)(y-\hat y))\) and
   why an ETA system optimises \(\tau=0.9\), not the mean.
5. Hierarchical reconciliation: write the summing matrix \(S\), state the coherence constraint,
   and derive the OLS/MinT projection \(\tilde y = S(S^\top W^{-1}S)^{-1}S^\top W^{-1}\hat y\).
6. Backtesting: rolling-origin evaluation; prove a single random split is meaningless here.
7. Intermittent demand: Croston's method and why MAPE is undefined on zeros.

**Text.** Hyndman & Athanasopoulos, *Forecasting: Principles and Practice* 3e (**FPP3**)
**[free]**, author-hosted — **Ch. 3** (decomposition), **5** (toolbox, backtesting), **8** (ETS),
**9** (ARIMA), **11** (hierarchical), **13** (practical issues). A Python edition (**FPPPy**)
is also **[free]**.

**Depth.** Box, Jenkins, Reinsel & Ljung, *Time Series Analysis: Forecasting and Control* 5e
(Wiley) **[paid]** — the source. Hamilton, *Time Series Analysis* (Princeton 1994) **[paid]**
for the econometric treatment. Brockwell & Davis, *Introduction to Time Series and Forecasting*
(Springer) **[paid]**.

**Course.** Monash (Hyndman's own, author-hosted materials). NPTEL **Applied Time-Series
Analysis** (Arun K. Tangirala, IIT Madras) — unusually rigorous and free. Cornell
**ORIE 5740 / STSCI** for the statistics-department framing.

**Papers.**
Hyndman et al., "A State Space Framework for Automatic Forecasting Using Exponential Smoothing
Methods" (IJF 2002) · Wickramasuriya, Athanasopoulos & Hyndman, "Optimal Forecast
Reconciliation… (MinT)" (JASA 2019) · Salinas et al., "DeepAR" (IJF 2020) ·
Oreshkin et al., "N-BEATS" (ICLR 2020) · Lim et al., "Temporal Fusion Transformers" (IJF 2021) ·
Makridakis, Spiliotis & Assimakopoulos, "The M4/M5 Competition" results papers — the empirical
check on every claim above.

**Stop at.** ETS + ARIMA + quantile + hierarchical + one deep baseline. No spectral analysis,
no full econometrics sequence (that belongs to **T-SIGNAL §4.9** and a different degree).

**Build.** B9.

---

## 4.5 T-GRAPH — graphs, communities and fraud rings

**Covers.** Fraud / trust & safety (24), the graph half of Recommend (PinSage-class), and the
entity-network studies inside family 12.

**Derive.**
1. Connected components by union-find with path compression + union by rank; prove the
   \(O(\alpha(n))\) amortised bound's shape (you may cite Tarjan rather than reprove it).
2. PageRank as the stationary distribution of a random walk with restart; prove existence via
   Perron–Frobenius on the damped matrix; derive the power-iteration update.
3. Spectral clustering: normalised Laplacian \(L = I - D^{-1/2}AD^{-1/2}\), the relationship
   between its second eigenvector and the normalised cut, and the \(k\)-means step.
4. Modularity \(Q = \frac{1}{2m}\sum_{ij}\left(A_{ij}-\frac{k_ik_j}{2m}\right)\delta(c_i,c_j)\);
   derive the Louvain ΔQ for moving one node.
5. node2vec: write the biased-walk transition with \(p,q\) and the skip-gram-with-negative-sampling
   objective; say what \(p<1, q>1\) buys you (BFS-like, structural equivalence).
6. GNN message passing: \(h_v^{(k)} = \sigma\!\left(W^{(k)}\cdot\mathrm{AGG}(\{h_u^{(k-1)}\})\right)\);
   derive GraphSAGE mean-aggregation and state the over-smoothing failure at large \(k\).
7. Fraud-specific: why a ring is a **dense subgraph**, not an outlier, and why per-account
   features cannot find it.

**Text.** Hamilton, *Graph Representation Learning* (Morgan & Claypool 2020) **[free]**,
author-hosted — **Ch. 2–3** (node embeddings), **Ch. 5–6** (GNNs, expressivity).
Easley & Kleinberg **[free]** — **Ch. 2–5** (graph structure), **Ch. 13–14** (web graph, PageRank).

**Depth.** Newman, *Networks* 2e (OUP 2018) **[paid]** — the statistical-physics treatment;
**Ch. 6, 11, 14**. Barabási, *Network Science* (Cambridge 2016) **[free]** online.
Leskovec/Rajaraman/Ullman MMDS **Ch. 5** (link analysis), **Ch. 10** (social-network graphs).

**Course.** Stanford **CS224W** *Machine Learning with Graphs* — slides, videos, Colabs all
public. Cornell **INFO 2040** for the network-science half. NPTEL **Social Network Analysis**
(IIT Kharagpur / IIT Ropar offerings).

**Papers.**
Page, Brin, Motwani & Winograd, "The PageRank Citation Ranking" (1999) ·
Blondel et al., "Fast Unfolding of Communities in Large Networks" (Louvain, JSTAT 2008) ·
Perozzi, Al-Rfou & Skiena, "DeepWalk" (KDD 2014) · Grover & Leskovec, "node2vec" (KDD 2016) ·
Kipf & Welling, "Semi-Supervised Classification with Graph Convolutional Networks" (ICLR 2017) ·
Hamilton, Ying & Leskovec, "Inductive Representation Learning on Large Graphs" (GraphSAGE, NeurIPS 2017) ·
Veličković et al., "Graph Attention Networks" (ICLR 2018) ·
Akoglu, Tong & Koutra, "Graph-Based Anomaly Detection and Description: A Survey" (DMKD 2015) ·
Pandit et al., "NetProbe: A Fast and Scalable System for Fraud Detection in Online Auction
Networks" (WWW 2007).

**Stop at.** One embedding method, one GNN layer type, one community algorithm, implemented.
No spectral graph theory course, no full GNN survey.

**Build.** B10.

---

## 4.6 T-DL — deep learning and the transformer

**Covers.** LLM / genAI apps (19); the encoder half of families 6–8; the ranking models of
families 1–2 once they go neural.

> This is the most expensive ceiling on the list, and §2.3's warning applies here more than
> anywhere. Budget a full term, not a weekend.

**Derive.**
1. Backpropagation as reverse-mode automatic differentiation: derive it for a two-layer MLP by
   hand, then state the general rule \(\bar{x} = \left(\frac{\partial y}{\partial x}\right)^\top\bar{y}\)
   and why reverse mode costs \(O(1)\) forward passes for scalar outputs.
2. Softmax + cross-entropy: show \(\partial \mathcal{L}/\partial z = p - y\) and why fusing the
   two is both a numerical and a performance decision (log-sum-exp; see **M.NS** in §3.4).
3. Initialisation: derive the Xavier/He variance conditions from "keep activation variance
   constant across layers."
4. Normalisation: write BatchNorm's train/eval discrepancy and LayerNorm's formula; explain why
   transformers use the latter.
5. Adam: write the update with bias correction; show what \(\hat m/\sqrt{\hat v}\) does to a
   badly scaled coordinate; state one failure case (Adam vs SGD generalisation gap).
6. Scaled dot-product attention: \(\mathrm{softmax}(QK^\top/\sqrt{d_k})V\) — derive the
   \(1/\sqrt{d_k}\) from the variance of a dot product of unit-variance vectors; write the
   causal mask; count the \(O(n^2 d)\) cost.
7. Multi-head attention and positional encoding (sinusoidal, then RoPE as used).
8. KV cache: derive its memory as \(2\cdot L\cdot n_{\text{layers}}\cdot n_{\text{heads}}\cdot d_{\text{head}}\cdot \text{bytes}\)
   and show why it, not parameters, bounds serving concurrency.

**Text.** Prince, *Understanding Deep Learning* (MIT Press 2023) **[free]**, author-hosted —
**Ch. 6–7** (fitting, backprop), **Ch. 9–10** (regularisation, convolution), **Ch. 12**
(transformers). The best-drawn modern treatment. Zhang, Lipton, Li & Smola, *Dive into Deep
Learning* (**D2L**, Cambridge 2023) **[free]** — the runnable companion; every chapter has
from-scratch and framework implementations side by side.

**Depth.** Goodfellow, Bengio & Courville, *Deep Learning* (MIT Press 2016) **[free]** — still
the reference for **Part II**, dated on architectures. Bishop & Bishop, *Deep Learning:
Foundations and Concepts* (Springer 2024) **[free]** online. Murphy, *Probabilistic Machine
Learning: Advanced Topics* (MIT Press 2023) **[free]** for the probabilistic framing.

**Course.** NPTEL **Deep Learning** — Mitesh Khapra, IIT Madras (**CS6910/CS7015**); genuinely
one of the best free lecture series on backprop mechanics. Stanford **CS224n** (NLP with deep
learning) and **CS231n** (vision). Harvard **CS 181** *Machine Learning* for the probabilistic
foundation. Princeton **COS 324** *Introduction to Machine Learning*.
Penn **CIS 5200** *Machine Learning* for the statistical-foundations framing.

**Papers.**
Rumelhart, Hinton & Williams, "Learning Representations by Back-Propagating Errors" (Nature 1986) ·
Glorot & Bengio (AISTATS 2010); He et al. (ICCV 2015) — initialisation ·
Ioffe & Szegedy, "Batch Normalization" (ICML 2015); Ba, Kiros & Hinton, "Layer Normalization" (2016) ·
Kingma & Ba, "Adam" (ICLR 2015) · Srivastava et al., "Dropout" (JMLR 2014) ·
He et al., "Deep Residual Learning" (CVPR 2016) ·
Vaswani et al., "Attention Is All You Need" (NeurIPS 2017) ·
Kaplan et al., "Scaling Laws for Neural Language Models" (2020); Hoffmann et al., "Training
Compute-Optimal Large Language Models" (Chinchilla, 2022) ·
Hu et al., "LoRA" (ICLR 2022) · Dao et al., "FlashAttention" (NeurIPS 2022) ·
Su et al., "RoFormer" (RoPE, 2021).

**Stop at.** One MLP, one transformer block, one training loop — **written by you**. No
architecture zoo, no distributed pretraining, no frontier-scale run. Serving and quantisation
hand off to **T-MLSYS §4.12**.

**Build.** B11.

---

## 4.7 T-NLP — text, sequence labelling and RAG

**Covers.** NLP / text / support (7), the generation half of family 5, and the query-understanding
layer of family 2.

**Derive.**
1. Tokenisation: implement BPE's merge loop; explain the vocabulary-size ↔ sequence-length
   trade-off and why it changes your serving cost.
2. Language-model evaluation: derive perplexity as \(\exp(-\frac1N\sum\log p(w_i\mid w_{<i}))\)
   and state exactly when comparing perplexities across tokenisers is invalid.
3. Word2vec skip-gram with negative sampling: write the objective, derive the gradient, and
   explain the \(p(w)^{3/4}\) noise distribution.
4. CRF: write the linear-chain conditional \(p(y\mid x) \propto \exp\sum_t(\psi(y_t,x)+\psi(y_{t-1},y_t))\),
   derive the forward algorithm, and run Viterbi by hand on a 3-token toy.
5. Sequence-labelling evaluation: entity-level precision/recall, and why token accuracy is a
   lie on any imbalanced tagging task.
6. RAG: write the retrieve-then-read decomposition, derive why chunk size trades recall against
   precision-in-context, and state the two failure modes (retrieval miss vs faithful-to-wrong-context).

**Text.** Jurafsky & Martin, *Speech and Language Processing* 3e (**SLP3**) **[free]**,
author-hosted (current release Jan 2026) — **Ch. 2** (regex/tokenisation), **3** (n-grams),
**5–6** (logistic regression, vector semantics), **8** (sequence labelling), **9–10**
(transformers, LLMs), **14–15** (QA/RAG). Eisenstein, *Introduction to Natural Language
Processing* (MIT Press 2019) **[free]** draft — stronger on structured prediction and CRFs.

**Depth.** Goldberg, *Neural Network Methods for NLP* (Morgan & Claypool 2017) **[paid]** ·
Manning & Schütze, *Foundations of Statistical NLP* (MIT Press 1999) **[paid]** for the
pre-neural statistical core that still runs in production.

**Course.** Stanford **CS224n** *NLP with Deep Learning*. CMU **11-711** *Advanced NLP*
(Neubig; videos public). Cornell **CS 4740** *Natural Language Processing*. NPTEL **Natural
Language Processing** (Pawan Goyal, IIT Kharagpur).

**Papers.**
Mikolov et al., "Efficient Estimation of Word Representations" + "Distributed Representations"
(2013) · Pennington, Socher & Manning, "GloVe" (EMNLP 2014) ·
Lafferty, McCallum & Pereira, "Conditional Random Fields" (ICML 2001) ·
Sutskever, Vinyals & Le, "Sequence to Sequence Learning" (NeurIPS 2014) ·
Bahdanau, Cho & Bengio, "Neural Machine Translation by Jointly Learning to Align and Translate" (ICLR 2015) ·
Sennrich, Haddow & Birch, "Neural Machine Translation of Rare Words with Subword Units" (BPE, ACL 2016) ·
Devlin et al., "BERT" (NAACL 2019) ·
Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (NeurIPS 2020) ·
Gao et al., "Retrieval-Augmented Generation for Large Language Models: A Survey" (2023).

**Stop at.** SLP3 plus one structured-prediction implementation. No linguistics sequence, no
multilingual MT programme.

**Build.** B11.

---

## 4.8 T-CV — vision, video and OCR

**Covers.** CV / video / OCR (6) — the smallest family with a genuine ceiling, and the one
where **buy-before-build is usually correct**.

**Derive.**
1. Discrete 2-D convolution and cross-correlation; derive output size
   \(\lfloor (n + 2p - k)/s\rfloor + 1\) and the receptive field after \(L\) layers.
2. Convolution as a Toeplitz matrix multiply — this is what makes im2col work.
3. Backprop through a conv layer: show the gradient w.r.t. input is a full convolution with the
   flipped kernel.
4. IoU, non-max suppression, and mAP at a given IoU threshold — computed by hand on five boxes.
5. Metric learning: triplet loss \(\max(0, d(a,p)-d(a,n)+\alpha)\); explain hard-negative mining
   and why random triplets stall.
6. OCR pipeline decomposition: detect → rectify → recognise → post-correct, and which stage
   dominates error in practice.

**Text.** Szeliski, *Computer Vision: Algorithms and Applications* 2e (Springer 2022) **[free]**,
author-hosted — **Ch. 3** (image processing), **5** (deep learning), **6** (recognition),
**7** (features and alignment). Prince (§4.6) **Ch. 10** for the convolution derivation.

**Depth.** Hartley & Zisserman, *Multiple View Geometry* (Cambridge) **[paid]** — only if
geometry is the actual problem. Forsyth & Ponce, *Computer Vision: A Modern Approach* **[paid]**.

**Course.** Stanford **CS231n** *Deep Learning for Computer Vision* — notes and assignments
public and still the best on-ramp. NPTEL **Deep Learning for Computer Vision**
(Vineeth Balasubramanian, IIT Hyderabad). IIT Madras **Computer Vision** (NPTEL, Vineeth N B).

**Papers.**
LeCun et al., "Gradient-Based Learning Applied to Document Recognition" (LeNet, Proc. IEEE 1998) ·
Krizhevsky, Sutskever & Hinton, "ImageNet Classification with Deep CNNs" (NeurIPS 2012) ·
Ren et al., "Faster R-CNN" (NeurIPS 2015) · Redmon et al., "You Only Look Once" (CVPR 2016) ·
Ronneberger, Fischer & Brox, "U-Net" (MICCAI 2015) ·
Schroff, Kalenichenko & Philbin, "FaceNet" (CVPR 2015) ·
Dosovitskiy et al., "An Image Is Worth 16x16 Words" (ViT, ICLR 2021) ·
Radford et al., "Learning Transferable Visual Models from Natural Language Supervision" (CLIP, ICML 2021) ·
Graves et al., "Connectionist Temporal Classification" (ICML 2006) — shared with §4.9, and the
reason OCR and ASR are the same problem.

**Stop at.** Szeliski's recognition chapters. **Six of 309 studies do not justify a vision
career.** For most of these the correct engineering answer is a managed vision API; you open
this ceiling to know *when* that answer is wrong (on-device latency, data residency,
domain-specific documents).

**Build.** No dedicated Go rung. If forced, the serving path is ONNX Runtime via cgo (Part 7).

---

## 4.9 T-SIGNAL — speech and audio

**Covers.** Speech / audio (3).

**Derive.**
1. Nyquist–Shannon sampling theorem: state it, and construct the aliasing counterexample
   numerically (sample a 7 kHz tone at 8 kHz, predict what you hear).
2. DFT \(X_k = \sum_n x_n e^{-2\pi i kn/N}\); derive the radix-2 FFT recursion and its
   \(O(N\log N)\).
3. STFT and the window-length ↔ time/frequency-resolution trade-off; mel-filterbank and MFCC as
   a perceptual re-binning.
4. CTC: derive the forward–backward over the extended (blank-interleaved) label sequence and
   explain why it removes the need for frame-level alignment.
5. WER as edit distance; show why it is unbounded above and what that does to your dashboards.

**Text.** Jurafsky & Martin **SLP3** **[free]** — the ASR/TTS chapters are sufficient at this
ceiling. Oppenheim & Schafer, *Discrete-Time Signal Processing* 3e (Pearson) **[paid]** — only
the sampling and DFT chapters; do not read it cover to cover for this.
Smith, *The Scientist and Engineer's Guide to Digital Signal Processing* **[free]**,
author-hosted — the gentler on-ramp.

**Course.** MIT **6.003** *Signals and Systems* **[free]** (OCW) for sampling and transforms.
NPTEL **Digital Signal Processing** (IIT Kharagpur / IIT Madras) — open only the sampling/DFT
weeks. Stanford CS224S if a speech-specific course is genuinely needed.

**Papers.**
Graves et al., "Connectionist Temporal Classification" (ICML 2006) ·
Graves, "Sequence Transduction with Recurrent Neural Networks" (RNN-T, 2012) ·
Baevski et al., "wav2vec 2.0" (NeurIPS 2020) ·
Radford et al., "Robust Speech Recognition via Large-Scale Weak Supervision" (Whisper, 2022).

**Stop at.** **No Kaldi, no OpenFst, no DSP degree.** Three studies. You need sampling, the
STFT, CTC, and the serving path — nothing else.

**Build.** No dedicated Go rung; FFT in Go is a good GO-11 benchmarking exercise if you want one.

---

## 4.10 T-CAUSAL — causal inference, uplift and experimentation

**Covers.** Marketing / churn / CLV / notify (14), plus the experimentation layer that every
other family depends on to know whether it worked.

**Derive.**
1. Potential outcomes \(Y_i(1), Y_i(0)\); ATE \(= \mathbb{E}[Y(1)-Y(0)]\); prove randomisation
   makes the difference in means unbiased, and name the SUTVA violation that breaks it in a
   two-sided marketplace.
2. Confounding on a DAG: read off a backdoor path, apply the backdoor criterion, and construct
   the collider example where *conditioning creates* bias.
3. Identification vs estimation — state the difference precisely; most production "causal"
   mistakes are conflating the two.
4. IPW estimator \(\hat\tau = \frac1n\sum\left(\frac{T_iY_i}{e(X_i)} - \frac{(1-T_i)Y_i}{1-e(X_i)}\right)\);
   show positivity failure blowing up the variance.
5. DiD: write the two-way fixed-effects estimator and state the parallel-trends assumption as a
   testable-in-pre-period claim.
6. IV: derive the Wald estimator; state relevance + exclusion; show what a weak instrument does.
7. CUPED: derive \(\hat Y_{cv} = \bar Y - \theta(\bar X - \mathbb{E}[X])\) with
   \(\theta^\* = \mathrm{Cov}(Y,X)/\mathrm{Var}(X)\) and compute the variance reduction \(1-\rho^2\).
8. Uplift: show that \(\tau(x) = \mathbb{E}[Y(1)-Y(0)\mid X=x]\) is **not** \(\mathbb{E}[Y\mid X=x, T=1]\)
   ranked — the "persuadables vs sure things" confusion that wastes most marketing budgets.
9. Sequential testing: why peeking inflates type-I error, and one correct alternative
   (alpha-spending or always-valid confidence sequences).

**Text.** Hernán & Robins, *Causal Inference: What If* (CRC 2020) **[free]**, author-hosted at
Harvard — **Part I Ch. 1–3** (no models), **Ch. 6–7** (DAGs, confounding), **Ch. 12–13**
(IPW, standardisation), **Ch. 14–16** (IV, and what to do when identification fails).
Kohavi, Tang & Xu, *Trustworthy Online Controlled Experiments* (Cambridge 2020) **[paid]** —
the industrial counterpart; CUPED, guardrail metrics, twyman's law, sample-ratio mismatch.

**Depth.** Pearl, Glymour & Jewell, *Causal Inference in Statistics: A Primer* (Wiley 2016)
**[paid]** — the shortest correct route into DAGs. Angrist & Pischke, *Mostly Harmless
Econometrics* (Princeton 2009) **[paid]** for IV/DiD/RD craft. Imbens & Rubin, *Causal
Inference for Statistics, Social, and Biomedical Sciences* (Cambridge 2015) **[paid]** for the
design-based treatment. Facure, *Causal Inference for the Brave and True* **[free]**, online —
the practical bridge.

**Course.** Harvard **Causal Diagrams: Draw Your Assumptions Before Your Conclusions**
(Hernán, edX) **[free]** to audit. MIT **14.387** *Applied Econometrics* (OCW) **[free]**.
Stanford **STATS 361** *Causal Inference* (Wager's notes **[free]**). Cornell **ECON 3120 /
PAM 3100** for the applied-econometrics framing.

**Papers.**
Rubin, "Estimating Causal Effects of Treatments" (J. Educ. Psych. 1974) ·
Pearl, "Causal Diagrams for Empirical Research" (Biometrika 1995) ·
Deng, Xu, Kohavi & Walker, "Improving the Sensitivity of Online Controlled Experiments by
Utilizing Pre-Experiment Data" (CUPED, WSDM 2013) ·
Chernozhukov et al., "Double/Debiased Machine Learning" (Econometrics J. 2018) ·
Wager & Athey, "Estimation and Inference of Heterogeneous Treatment Effects Using Random
Forests" (JASA 2018) · Gutierrez & Gérardy, "Causal Inference and Uplift Modelling: A Review"
(PMLR 2017) · Johari et al., "Always Valid Inference: Continuous Monitoring of A/B Tests"
(Operations Research 2022).

**Stop at.** *What If* Parts I–II plus Kohavi. No structural-econometrics sequence, no
do-calculus completeness proofs.

**Build.** B12.

---

## 4.11 T-STREAM — streaming, event time and exactly-once

**Covers.** Availability / inventory (5), and the ingestion layer of essentially every other
family — this is the ceiling with the widest indirect reach.

**Derive.**
1. Event time vs processing time vs ingestion time; construct the skew example that makes a
   processing-time window silently wrong.
2. Watermarks: define a watermark as a monotone lower bound on event time; derive what
   "allowed lateness" costs you in state size.
3. Windowing: fixed, sliding, session — and the trigger/accumulation matrix (discarding vs
   accumulating vs accumulating-and-retracting) from the Dataflow model.
4. Exactly-once: prove that exactly-once *delivery* is impossible over an unreliable channel,
   then show how exactly-once *effect* is achieved (idempotent writes + deduplication keys +
   transactional sinks). This distinction is the single most-confused point in streaming.
5. Chandy–Lamport snapshots and how Flink's aligned barriers turn them into checkpoints.
6. Log compaction and the "table ⟷ stream" duality.
7. Backpressure: derive the queue growth from Little's law \(L = \lambda W\) (you already have
   this at **T.SysTheory Networking grad**, §3.3) and state the shedding policy.

**Text.** Akidau, Chernyak & Lax, *Streaming Systems* (O'Reilly 2018) **[paid]** —
**Ch. 1–4** are the core; the *Streaming 101 / 102* articles that became Ch. 1–2 are **[free]**.
Kleppmann, *Designing Data-Intensive Applications* (O'Reilly 2017) **[paid]** — **Ch. 11**
(stream processing) and **Ch. 7–9** for the transaction/consensus floor underneath it.

**Depth.** Kleppmann, *Making Sense of Stream Processing* (O'Reilly report) **[free]** ·
Narkhede, Shapira & Palino, *Kafka: The Definitive Guide* 2e **[free]** (Confluent-hosted).

**Course.** CMU **15-445/645** *Database Systems* **[free]** (Pavlo; videos public) for the
transactional floor. MIT **6.5840** *Distributed Systems* **[free]** for consensus and
fault-tolerance. Berkeley **CS186** for query processing.

**Papers.**
Akidau et al., "The Dataflow Model" (VLDB 2015) — **read this one twice** ·
Akidau et al., "MillWheel" (VLDB 2013) ·
Carbone et al., "Lightweight Asynchronous Snapshots for Distributed Dataflows" (Flink, 2015) ·
Chandy & Lamport, "Distributed Snapshots" (TOCS 1985) ·
Kreps, "The Log: What Every Software Engineer Should Know About Real-Time Data's Unifying
Abstraction" (2013) **[free]** · Zaharia et al., "Discretized Streams" (SOSP 2013).

**Stop at.** The Dataflow model and one hand-built watermark. No query-optimiser theory, no
distributed-systems research programme.

**Build.** B13.

---

## 4.12 T-MLSYS — ML platform, training scale and serving economics

**Covers.** ML platform / infra (2) by count, but in practice the **non-modelling 80%** of
every one of the 309 studies. If you read only one ceiling, read this one.

**Derive.**
1. Training-step arithmetic: FLOPs ≈ \(6ND\) for a dense transformer (params × tokens); derive
   the factor 6 (2 forward + 4 backward) and use it to estimate a run's cost before launching it.
2. Data vs model vs pipeline parallelism: for each, state what is split, what is
   communicated, and the communication volume per step. Derive the all-reduce cost
   \(2(p-1)/p \cdot |W|\) for ring all-reduce.
3. Mixed precision: why fp16 needs loss scaling, what bf16 changes, and where the master
   weights live.
4. Quantisation: derive the affine map \(q = \mathrm{round}(x/s) + z\), its dequantisation
   error bound, and the difference between post-training and quantisation-aware.
5. Serving economics: build the roofline — arithmetic intensity, memory-bandwidth bound vs
   compute bound — and show that LLM decode is bandwidth-bound while prefill is compute-bound.
6. Batching: derive the latency/throughput curve for static batching, then show why continuous
   batching dominates it for variable-length generation.
7. Feature stores: derive **training/serving skew** as a definitional mismatch, not a bug; state
   the point-in-time-correct join that prevents label leakage.
8. Monitoring: distinguish data drift, concept drift and label delay; give the statistic for
   each (PSI/KL for the first — you proved \(D_{KL}\ge 0\) at **T.ProbStat grad**, §3.3).

**Text.** Harvard **CS249r** *Machine Learning Systems* (Janapa Reddi et al.), **MLSysBook.ai**
**[free]** — the training, optimisation, serving and ops chapters; the only open textbook that
covers this whole surface. Huyen, *Designing Machine Learning Systems* (O'Reilly 2022)
**[paid]** — the best single book on the non-modelling decisions.

**Depth.** Huyen, *AI Engineering* (O'Reilly 2025) **[paid]** for the LLM-serving era ·
Google, *Site Reliability Engineering* + *The SRE Workbook* **[free]** — SLOs, error budgets,
the on-call reality these systems land in · Lakshmanan, Robinson & Munn, *Machine Learning
Design Patterns* (O'Reilly 2020) **[paid]**.

**Course.** Stanford **CS329S** *Machine Learning Systems Design* **[free]** notes ·
MIT **6.5940** *TinyML and Efficient Deep Learning Computing* **[free]** (Han) — quantisation,
pruning, distillation, done properly · CMU **11-667 / 15-849** systems-for-ML offerings ·
Harvard CS249r itself (lectures public).

**Papers.**
Sculley et al., "Hidden Technical Debt in Machine Learning Systems" (NeurIPS 2015) — **start here** ·
Zinkevich, "Rules of Machine Learning: Best Practices for ML Engineering" (Google) **[free]** ·
Breck et al., "The ML Test Score" (IEEE Big Data 2017) ·
Baylor et al., "TFX: A TensorFlow-Based Production-Scale ML Platform" (KDD 2017) ·
Li et al., "Scaling Distributed Machine Learning with the Parameter Server" (OSDI 2014) ·
Rajbhandari et al., "ZeRO" (SC 2020) · Shoeybi et al., "Megatron-LM" (2019) ·
Kwon et al., "Efficient Memory Management for LLM Serving with PagedAttention" (vLLM, SOSP 2023) ·
Dettmers et al., "LLM.int8()" (NeurIPS 2022); Frantar et al., "GPTQ" (ICLR 2023) ·
Crankshaw et al., "Clipper: A Low-Latency Online Prediction Serving System" (NSDI 2017).

**Stop at.** You are building the platform's *arithmetic and contracts*, not a competitor to
Kubeflow. One feature-store schema, one serving benchmark, one drift monitor.

**Build.** B14.

---

## 4.13 T-OPT and T-ER — optimisation, routing and entity resolution

**Covers.** The **"Other" (101)** bucket — pricing, dispatch, routing, inventory allocation,
record linkage, dimension modelling. A third of the catalog, and the part of it with the
least public teaching material relative to its commercial weight.

### T-OPT — mathematical optimisation

**Derive.**
1. LP standard form; the simplex pivot as a change of basic feasible solution; why it
   terminates (with Bland's rule) despite exponential worst case.
2. LP duality: state weak duality and prove it in two lines; state strong duality and
   complementary slackness; **interpret the dual variable as a shadow price** — this is the
   part that actually matters for pricing.
3. Integer programming: LP relaxation, the integrality gap, branch-and-bound's bounding
   argument; why a "just round it" heuristic can be arbitrarily bad.
4. Assignment problem via Hungarian algorithm / min-cost flow; recognise dispatch as this.
5. VRP with time windows: state it, prove it is NP-hard by reduction from TSP, and implement
   one metaheuristic (2-opt or guided local search) so you know what a solver buys you.
6. Revenue management: derive Littlewood's rule for two-class protection levels
   (\(P(D_1 > y) = p_2/p_1\)) — the foundation of every dynamic-pricing system in family 12.
7. Prediction-then-optimisation: state why minimising forecast MSE is *not* the same as
   minimising decision regret.

**Text.** Bertsimas & Tsitsiklis, *Introduction to Linear Optimization* (Athena 1997)
**[paid]** — **Ch. 1–4** (geometry, simplex, duality) is the whole floor.
Boyd & Vandenberghe, *Convex Optimization* (Cambridge 2004) **[free]**, author-hosted — **Ch.
2–5** for the convex framing and Lagrange duality. Williams, *Model Building in Mathematical
Programming* 5e (Wiley) **[paid]** — the art of formulation, which is where beginners actually fail.

**Depth.** Nocedal & Wright, *Numerical Optimization* 2e (Springer) **[paid]** for the
continuous/nonlinear side · Wolsey, *Integer Programming* 2e (Wiley 2020) **[paid]** ·
Toth & Vigo (eds.), *Vehicle Routing* 2e (SIAM 2014) **[paid]** · Talluri & van Ryzin,
*The Theory and Practice of Revenue Management* (Springer 2004) **[paid]**.

**Course.** MIT **15.053 / 15.071** *Optimization Methods* (OCW) **[free]** ·
Stanford **EE364A/B** *Convex Optimization* **[free]** (Boyd; videos + homework public) ·
NPTEL **Fundamentals of Operations Research** (G. Srinivasan, IIT Madras) **[free]** ·
IISc **E1 251 / Optimization** offerings via the CSA department.

**Tooling.** Google **OR-Tools** documentation (routing, CP-SAT) — read the routing guide even
if you solve with your own code, because it names the constraints practitioners actually hit.

### T-ER — entity resolution / record linkage

**Derive.**
1. Fellegi–Sunter: write the likelihood ratio \(\frac{m(\gamma)}{u(\gamma)}\) for an agreement
   pattern and derive the two thresholds from target error rates.
2. Blocking: compute pairs-completeness and reduction ratio; show that the quadratic
   comparison space is the real problem and blocking is the only answer.
3. MinHash + LSH for approximate Jaccard: derive \(P(\text{collision}) = 1-(1-s^r)^b\), plot the
   S-curve, and tune \((b,r)\) to a target threshold.
4. Transitive closure of match decisions, and why it produces absurd clusters without a
   canonicalisation step.
5. Evaluation: pairwise vs cluster-level F1, and why they disagree.

**Text.** Christen, *Data Matching* (Springer 2012) **[paid]** — the reference.
Leskovec/Rajaraman/Ullman MMDS **Ch. 3** **[free]** for MinHash/LSH derived properly.
Kimball & Ross, *The Data Warehouse Toolkit* 3e (Wiley 2013) **[paid]** for the dimension-modelling
studies in the same bucket (slowly-changing dimensions, conformed dimensions, grain).

**Papers.** Fellegi & Sunter, "A Theory for Record Linkage" (JASA 1969) ·
Elmagarmid, Ipeirotis & Verykios, "Duplicate Record Detection: A Survey" (TKDE 2007) ·
Papadakis et al., "Blocking and Filtering Techniques for Entity Resolution: A Survey" (CSUR 2020) ·
Mudgal et al., "Deep Learning for Entity Matching" (SIGMOD 2018).

**Stop at.** One LP solved by your own simplex, one routing heuristic, one blocking scheme, one
Fellegi–Sunter scorer. No OR degree, no combinatorial-optimisation research.

**Build.** B5 (numerics/LP), B10b (ER).

---

## 4.14 T-RL — bandits, then reinforcement learning

**Covers.** Cross-cutting: the exploration layer of Recommend (65), Search/ads (36) and
dynamic pricing inside "Other" (101). Bandits are where production exploration actually lives;
full RL is where most tutorials wrongly start.

**Derive.**
1. Regret: define pseudo-regret \(R_T = T\mu^\* - \mathbb{E}\sum_t \mu_{A_t}\); state the
   \(\Omega(\sqrt{KT})\) minimax lower bound so you know what "good" means.
2. Hoeffding's inequality → the UCB1 index \(\hat\mu_i + \sqrt{2\ln t / n_i}\); reproduce the
   \(O(\log T)\) gap-dependent regret bound's skeleton.
3. Thompson sampling for Bernoulli arms: the Beta–Bernoulli conjugate update, and why sampling
   the posterior *is* the exploration.
4. Contextual bandits: LinUCB's ridge solution \(\hat\theta = (X^\top X + \lambda I)^{-1}X^\top y\)
   and its confidence ellipsoid.
5. Off-policy evaluation: IPS, self-normalised IPS, and the doubly-robust estimator; state the
   bias/variance trade-off. **This connects back to M.ML IPS (§3.4) — the derivation gate stays
   there; here you use it.**
6. MDPs: Bellman expectation and optimality equations; prove the Bellman operator is a
   \(\gamma\)-contraction and that value iteration therefore converges.
7. Policy gradient / REINFORCE: derive \(\nabla_\theta J = \mathbb{E}[\nabla_\theta\log\pi_\theta(a\mid s)\,Q^\pi(s,a)]\)
   and explain the baseline's variance reduction.

**Text.** Lattimore & Szepesvári, *Bandit Algorithms* (Cambridge 2020) **[free]**,
author-hosted — **Ch. 4–9** (stochastic bandits, UCB), **Ch. 18–19** (contextual, linear).
Sutton & Barto, *Reinforcement Learning: An Introduction* 2e (MIT Press 2018) **[free]**,
author-hosted — **Ch. 2** (bandits), **3–4** (MDPs, DP), **5–6** (MC, TD), **13** (policy gradient).

**Depth.** Szepesvári, *Algorithms for Reinforcement Learning* **[free]** · Agarwal, Jiang,
Kakade & Sun, *Reinforcement Learning: Theory and Algorithms* **[free]** draft · Puterman,
*Markov Decision Processes* (Wiley) **[paid]** for the operations-research treatment.

**Course.** **IISc E1 245** *Online Prediction and Learning* (ECE) — uses Lattimore as its text ·
NPTEL **Reinforcement Learning** (B. Ravindran, IIT Madras, `106106143`) **[free]** ·
Stanford **CS234** *Reinforcement Learning* **[free]** · UCL/DeepMind RL lectures (Silver) **[free]**.

**Papers.**
Auer, Cesa-Bianchi & Fischer, "Finite-time Analysis of the Multiarmed Bandit Problem" (ML 2002) ·
Li et al., "A Contextual-Bandit Approach to Personalized News Article Recommendation" (LinUCB, WWW 2010) ·
Chapelle & Li, "An Empirical Evaluation of Thompson Sampling" (NeurIPS 2011) ·
Dudík, Langford & Li, "Doubly Robust Policy Evaluation and Learning" (ICML 2011) ·
Swaminathan & Joachims, "Counterfactual Risk Minimization" (JMLR 2015) ·
Schulman et al., "Proximal Policy Optimization" (2017) — read only if RLHF is on your path.

**Stop at.** Bandits properly; RL to the value-iteration and REINFORCE level. **Full deep RL
stays out of scope** — it is a research programme and almost none of the 309 studies deploy it.

**Build.** B6 (the exploration layer of the recommender).

---

## 4.15 The software-engineering and system-design ceiling

Every one of the 309 studies is a **software system** before it is a model. This ceiling is
cross-cutting rather than family-specific, which is exactly why it is usually left implicit —
and why a learner building alone needs it named in one place.

**Derive / be able to argue.**
1. When a modular monolith beats microservices, with the coupling and deploy-frequency
   argument, not the fashion argument.
2. Transaction boundary = consistency boundary = ownership boundary; where the saga goes when
   they cannot coincide.
3. Idempotency keys and exactly-once *effect* (shared with §4.11).
4. Backpressure, bulkheads, circuit breakers, and the retry-storm you cause without jitter.
5. The SLO → error-budget → burn-rate chain, computed on a real window.
6. Why a feature pipeline is a **data contract** and what breaks when it is implicit.

**Text.**
Kleppmann, *Designing Data-Intensive Applications* (O'Reilly 2017) **[paid]** — still the single
highest-value book on this list · Newman, *Building Microservices* 2e (O'Reilly 2021) **[paid]** ·
Nygard, *Release It!* 2e (Pragmatic 2018) **[paid]** — the failure-mode catalogue ·
Richards & Ford, *Fundamentals of Software Architecture* (O'Reilly 2020) **[paid]** ·
Evans, *Domain-Driven Design* (Addison-Wesley 2003) **[paid]** · Hohpe & Woolf, *Enterprise
Integration Patterns* (2003) **[paid]** · Fowler, *Patterns of Enterprise Application
Architecture* (2002) **[paid]** · Google, *Site Reliability Engineering* and *The SRE Workbook*
**[free]** · Winters, Manshreck & Wright, *Software Engineering at Google* (O'Reilly 2020)
**[free]** online · Bass, Clements & Kazman, *Software Architecture in Practice* 4e **[paid]**.

**Testing and craft.** Beck, *Test-Driven Development by Example* **[paid]** · Feathers,
*Working Effectively with Legacy Code* **[paid]** · Fowler, *Refactoring* 2e **[paid]** ·
Ousterhout, *A Philosophy of Software Design* 2e **[paid]** — short, and the best thing written
on module depth.

**Course.** MIT **6.5840** *Distributed Systems* **[free]** (labs in **Go** — directly reusable
here) · CMU **15-445** *Database Systems* **[free]** · Cambridge **Distributed Systems**
(Kleppmann's lecture notes + videos) **[free]** · MIT **6.031** *Software Construction* **[free]** ·
Berkeley **CS 169** *Software Engineering* **[free]**.

**Stop at.** DDIA + Release It! + the SRE workbook is a complete working floor. The rest is
reference.

**Build.** Woven through B7–B14; there is no separate rung because there is no separate phase.

---

# PART 5 — Go from zero

## 5.0 Why Go for this, honestly

Go is not the language ML research is written in, and this file does not pretend otherwise.
It is chosen here for four reasons that hold specifically for **building the 309**:

1. **The systems in these case studies are Go-shaped.** Indexes, feature services, streaming
   consumers, rankers behind a p99 budget, fraud scorers on a hot path. Go's deployment story
   (one static binary), its concurrency model, and its scheduler are a direct fit.
2. **No framework to hide behind.** There is no `sklearn.fit` in Go. If you want logistic
   regression you write the gradient. That is exactly the pedagogy this file is for.
3. **The language is small enough to learn while learning something else.** The whole spec is
   readable in an afternoon. That is the property that makes "teach Go in parallel" feasible
   at all; it would not be with C++ or Rust.
4. **Profiling is first-class.** `pprof`, the race detector, `testing.B`, and escape analysis
   are in the toolchain. Part 6 asks you to *measure*, and Go makes measuring cheap.

**The honest cost:** no autodiff ecosystem, no GPU story worth using, no pandas. Part 7 is the
complete list of where that bites and what to do about it.

## 5.1 The rungs

| Rung | Teaches | Unlocks in Part 6 |
|---|---|---|
| **GO-0** | toolchain, modules, `go test`, `go vet`, `gofmt` | B0 |
| **GO-1** | types, numerics, control flow, functions, errors-as-values | B0, B1 |
| **GO-2** | slices, arrays, maps, strings/runes, aliasing | B1, B2 |
| **GO-3** | structs, methods, pointers, interfaces, embedding | B2, B3 |
| **GO-4** | generics, constraints, `slices`/`maps`/`cmp` | B3, B7 |
| **GO-5** | table tests, fuzzing, benchmarks, property tests | all |
| **GO-6** | error wrapping, `errors.Is/As`, panic boundaries | B9+ |
| **GO-7** | goroutines, channels, `select`, `sync`, `context`, race detector | B6, B7, B13 |
| **GO-8** | `io`, `bufio`, binary encoding, file formats, `encoding/json` | B7, B13 |
| **GO-9** | `net/http`, servers, middleware, timeouts, graceful shutdown | B14 |
| **GO-10** | protobuf + gRPC, streaming RPC, interceptors | B14 |
| **GO-11** | `pprof`, escape analysis, allocation, `benchstat`, PGO | B7, B11 |
| **GO-12** | cgo boundary, ONNX Runtime, when to leave Go | B11, Part 7 |
| **GO-13** | modules/versioning, Docker, OpenTelemetry, `govulncheck` | B14 |
| **GO-14** | synthesis — an unseen system end to end | B14 |

---

## GO-0 — toolchain and the first module

**Teaches.** `go mod init`, package layout, `go build` / `go test` / `go vet` / `gofmt`,
`GOPATH` is not a thing you need any more, semantic import paths.

```bash
mkdir -p the309/numkit && cd the309
go mod init example.com/the309
go test ./...          # no tests yet, and that is a passing state
go vet ./...
```

**Layout that scales to Part 6.** Flat is fine until it isn't; then:

```
the309/
  go.mod
  numkit/        // B0: floats, Kahan, logsumexp
  linalg/        // B1: Vec, Mat
  learn/         // B2-B4: ERM, losses, metrics
  index/         // B7: inverted index, HNSW
  rec/           // B6
  stream/        // B13
  cmd/serve/     // B14: main package
```

**Python contrast.** There is no `__init__.py`, no virtualenv, and no runtime import path. A
directory *is* a package; the module path in `go.mod` *is* the import prefix. Dependencies are
recorded in `go.mod`/`go.sum` and vendored on demand — there is no activate step.

**Gotcha.** An identifier is exported iff it starts with a capital letter. `func dot()` is
invisible outside its package; `func Dot()` is your API. This is the entire access-control
system — there is no `private`.

**Artifact.** A module that builds, vets clean, and has one passing test.

---

## GO-1 — types, numerics and errors as values

**Teaches.** Sized integers, `float64`/`float32`, no implicit conversion, `const` and untyped
constants, `for` as the only loop, `switch`, multiple returns, the error convention.

```go
package numkit

import (
	"errors"
	"math"
)

var ErrEmpty = errors.New("numkit: empty input")

// KahanSum sums xs with compensated summation, recovering most of the
// precision that naive float64 accumulation loses.
func KahanSum(xs []float64) (float64, error) {
	if len(xs) == 0 {
		return 0, ErrEmpty
	}
	var sum, c float64
	for _, x := range xs {
		y := x - c      // c carries the error from the previous step
		t := sum + y    // low-order bits of y are lost here...
		c = (t - sum) - y // ...and recovered here
		sum = t
	}
	return sum, nil
}

// LogSumExp computes log(sum(exp(x))) without overflowing.
func LogSumExp(xs []float64) float64 {
	if len(xs) == 0 {
		return math.Inf(-1)
	}
	m := xs[0]
	for _, x := range xs[1:] {
		if x > m {
			m = x
		}
	}
	if math.IsInf(m, -1) {
		return m
	}
	var s float64
	for _, x := range xs {
		s += math.Exp(x - m)
	}
	return m + math.Log(s)
}
```

**Python contrast.** Three things will bite a Python programmer immediately:

| Python | Go |
|---|---|
| `int` is arbitrary precision | `int` is 64-bit on modern platforms and **wraps silently** |
| `3 / 2 == 1.5` | `3 / 2 == 1` for ints; you must convert explicitly |
| exceptions propagate | errors are **returned values**; ignoring one is a bug `errcheck` will find |

**Gotcha.** `float64(a) / float64(b)` — Go will not convert for you, ever. And
`x == y` on computed floats is a defect in this domain; compare against a tolerance. This is
the **M.NS** material from §3.4, and Go makes it concrete because the conversions are visible.

**Exercise (ties to M.NS).** Write a test that demonstrates `0.1 + 0.2 != 0.3`. Then add
`0.1` to itself 10 000 times: naive summation is off by ≈1.6e-10, `KahanSum` is **exact**.
Then try `[1e16, 1, 1, -1e16]` — naive returns `0`, Kahan returns `2`.

Then try `[1e16, 1, -1e16]` and watch Kahan return `0` too. Compensated summation recovers the
*compensation term*, and here the single `1` is entirely below the ulp of `1e16` (which is 2),
so there is nothing left to recover. Finding the case where your fix does **not** help is worth
more than the case where it does.

**Artifact.** `numkit` with `KahanSum`, `LogSumExp`, `AlmostEqual`, all tested.

---

## GO-2 — slices, maps, strings

**Teaches.** The slice header (`ptr, len, cap`), aliasing, `append` reallocation semantics,
`copy`, maps with non-deterministic iteration order, `byte` vs `rune`.

```go
// A posting list: doc IDs, ascending. This is the core of B7.
type Postings []uint32

// Intersect returns the sorted intersection of a and b in O(len(a)+len(b)).
// Allocating into dst lets the caller reuse buffers across queries.
func Intersect(dst, a, b Postings) Postings {
	dst = dst[:0]
	i, j := 0, 0
	for i < len(a) && j < len(b) {
		switch {
		case a[i] < b[j]:
			i++
		case a[i] > b[j]:
			j++
		default:
			dst = append(dst, a[i])
			i++
			j++
		}
	}
	return dst
}
```

**The aliasing lesson — this is the one that catches everyone.**

```go
a := []int{1, 2, 3, 4, 5}
b := a[1:3]        // len 2, cap 4 — b shares a's backing array
b = append(b, 99)  // fits in cap, so this writes a[3]
// a is now [1 2 3 99 5]  <-- a was mutated by appending to b
```

Use `a[1:3:3]` (the three-index slice) to cap the capacity and force `append` to copy. In
Part 6 this bug silently corrupts a feature vector and the model just gets slightly worse —
the worst kind of bug. Assume nothing; test aliasing explicitly.

**Python contrast.** `b = a[1:3]` in Python **copies**. In Go it **views**. This single
difference is responsible for most of the Go bugs a Python programmer writes in month one.

**Gotcha.** Map iteration order is randomised *deliberately*. Never build a feature vector by
ranging over a map — sort the keys first, or your model's input ordering changes per process.

**Artifact.** `Postings` with `Intersect`, `Union`, `Difference`, property-tested against a
naive set implementation.

---

## GO-3 — structs, methods, pointers, interfaces

**Teaches.** Value vs pointer receivers, embedding (not inheritance), interface satisfaction
being structural and implicit, the nil-interface trap.

```go
package linalg

// Mat is a dense row-major matrix. Stride allows sub-matrix views
// without copying — the same idea as NumPy strides.
type Mat struct {
	Rows, Cols int
	Stride     int
	Data       []float64
}

func NewMat(r, c int) *Mat {
	return &Mat{Rows: r, Cols: c, Stride: c, Data: make([]float64, r*c)}
}

func (m *Mat) At(i, j int) float64     { return m.Data[i*m.Stride+j] }
func (m *Mat) Set(i, j int, v float64) { m.Data[i*m.Stride+j] = v }

// Scorer is the seam every ranking model in Part 6 implements.
// Note: no "implements" keyword. Satisfying the method set is enough.
type Scorer interface {
	Score(features []float64) float64
}
```

**Value vs pointer receiver.** `func (m Mat) At(...)` copies the struct header on every call
(cheap) but cannot mutate. `func (m *Mat) Set(...)` can. Rule: if any method needs a pointer
receiver, give **all** of them pointer receivers, so the method set is consistent.

**The nil-interface trap.**

```go
type MyErr struct{}
func (e *MyErr) Error() string { return "boom" }

func bad() error {
	var e *MyErr = nil
	return e          // an interface holding a (type=*MyErr, value=nil) pair
}
// bad() != nil  --  the interface is NOT nil, because its type word is set.
```

Return a literal `nil`, never a typed nil pointer. This bug has taken down real services.

**Python contrast.** Go has no classes and no inheritance. Embedding (`struct{ Base }`)
promotes methods but does **not** create an is-a relationship or a vtable you can override.
Composition is the only tool, which is why "accept interfaces, return structs" is the idiom.

**Artifact.** `linalg` with `Mat`, `MatMul`, `MatVec`, `Transpose`; a `Scorer` interface with
two implementations.

---

## GO-4 — generics

**Teaches.** Type parameters, constraints, `cmp.Ordered`, the `slices` and `maps` packages,
and — importantly — when *not* to reach for generics.

```go
import "container/heap"

// topK is a min-heap of the best k items seen. Pushing the (k+1)-th item
// and popping the minimum keeps the k largest, in O(n log k) for n items.
type topK[T any] struct {
	items []T
	worse func(a, b T) bool // true when a is the worse of the two
}

func (h *topK[T]) Len() int           { return len(h.items) }
func (h *topK[T]) Less(i, j int) bool { return h.worse(h.items[i], h.items[j]) }
func (h *topK[T]) Swap(i, j int)      { h.items[i], h.items[j] = h.items[j], h.items[i] }
func (h *topK[T]) Push(x any)         { h.items = append(h.items, x.(T)) }
func (h *topK[T]) Pop() any {
	old := h.items
	n := len(old)
	v := old[n-1]
	h.items = old[:n-1]
	return v
}

// TopK returns the k best elements of xs under worse(), unsorted.
func TopK[T any](xs []T, k int, worse func(a, b T) bool) []T {
	if k <= 0 {
		return nil
	}
	h := &topK[T]{worse: worse}
	heap.Init(h)
	for _, x := range xs {
		if h.Len() < k {
			heap.Push(h, x)
			continue
		}
		if worse(h.items[0], x) { // x beats the current worst
			h.items[0] = x
			heap.Fix(h, 0)
		}
	}
	return h.items
}
```

This one function is used by **every retrieval and ranking rung in Part 6**. Write it once.

**Gotcha.** Generics in Go do not give you operator overloading — you cannot write `a + b` for
a type parameter unless the constraint is numeric, and even then there is no `Matrix * Matrix`.
Numerical code stays explicit.

**Also learn here:** `slices.Sort`, `slices.SortFunc`, `slices.BinarySearch`, `slices.Max`,
`maps.Keys` (returns an iterator since Go 1.23 — pair with `slices.Sorted`).

**Artifact.** Generic `TopK`, `Reduce`, and a `Set[T comparable]`, all benchmarked against
the sort-everything baseline so you can state the crossover.

---

## GO-5 — testing, fuzzing, benchmarking

**Teaches.** Table-driven tests, subtests, `testing.F` fuzzing, `testing.B`, and property
testing — which matters more here than anywhere, because numerical bugs are silent.

```go
func TestIntersect(t *testing.T) {
	tests := []struct{ name string; a, b, want Postings }{
		{"disjoint", Postings{1, 3}, Postings{2, 4}, Postings{}},
		{"identical", Postings{1, 2}, Postings{1, 2}, Postings{1, 2}},
		{"empty", nil, Postings{1}, Postings{}},
	}
	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			got := Intersect(nil, tc.a, tc.b)
			if !slices.Equal(got, tc.want) {
				t.Errorf("Intersect(%v, %v) = %v, want %v", tc.a, tc.b, got, tc.want)
			}
		})
	}
}

// Property: intersection is commutative and a subset of both inputs.
func FuzzIntersect(f *testing.F) {
	f.Add([]byte{1, 2, 3}, []byte{2, 3, 4})
	f.Fuzz(func(t *testing.T, ab, bb []byte) {
		a, b := sortedUnique(ab), sortedUnique(bb)
		ab1 := Intersect(nil, a, b)
		ba1 := Intersect(nil, b, a)
		if !slices.Equal(ab1, ba1) {
			t.Fatalf("not commutative: %v vs %v", ab1, ba1)
		}
	})
}
```

**The rule for this file.** Every numerical function in Part 6 ships with:
a **table test** (known values), a **property test** (an invariant that must hold for all
inputs), and a **tolerance** (never `==` on floats). A gradient implementation additionally
ships with a **finite-difference check** — this is the single highest-value test in ML code:

```go
// central difference: (f(x+h) - f(x-h)) / 2h should match the analytic gradient
// to ~sqrt(machine epsilon) relative error for h ≈ 1e-5.
```

**Artifact.** Finite-difference gradient checker, reused by B2, B4, B6, B11.

---

## GO-6 — errors, wrapping and panic boundaries

**Teaches.** `fmt.Errorf("...: %w", err)`, `errors.Is`, `errors.As`, sentinel vs typed errors,
when `panic` is correct (never across a package boundary; yes for "impossible" invariant
violations), `defer`/`recover` at the server edge.

```go
var ErrDimMismatch = errors.New("linalg: dimension mismatch")

func Dot(a, b []float64) (float64, error) {
	if len(a) != len(b) {
		return 0, fmt.Errorf("dot %d vs %d: %w", len(a), len(b), ErrDimMismatch)
	}
	b = b[:len(a)] // hint to the compiler: eliminates the bounds check in the loop
	var s float64
	for i, x := range a {
		s += x * b[i]
	}
	return s, nil
}
```

**Gotcha.** `defer` arguments are evaluated immediately; the *call* is deferred. And deferred
functions run at **function** exit, not block exit — a `defer` inside a loop accumulates.

---

## GO-7 — concurrency

**Teaches.** Goroutines, channels, `select`, `context.Context`, `sync.Mutex`/`RWMutex`,
`sync.WaitGroup`, `errgroup`, `atomic`, and the race detector. This is Go's reason to exist and
the rung that makes B7 and B13 possible.

```go
import (
	"context"
	"runtime"
	"golang.org/x/sync/errgroup"
)

// BuildIndex shards the corpus and builds postings in parallel.
// Every goroutine respects cancellation; none leaks.
func BuildIndex(ctx context.Context, shards [][]Doc) ([]*Index, error) {
	g, ctx := errgroup.WithContext(ctx)
	g.SetLimit(runtime.GOMAXPROCS(0))

	out := make([]*Index, len(shards))
	for i, shard := range shards {
		g.Go(func() error {
			// Go 1.22+: i and shard are per-iteration; no `i := i` shadow needed.
			idx, err := buildShard(ctx, shard)
			if err != nil {
				return fmt.Errorf("shard %d: %w", i, err)
			}
			out[i] = idx // distinct index per goroutine: no mutex required
			return nil
		})
	}
	return out, g.Wait()
}
```

**The three rules that prevent every concurrency bug in Part 6.**

1. **A goroutine you cannot cancel is a leak.** Every long-running goroutine takes a `ctx` and
   selects on `ctx.Done()`.
2. **Do not communicate by sharing memory; share memory by communicating** — but a `sync.Mutex`
   around a map is often the right, boring answer. Channels are not always the tool.
3. **Run `go test -race` on every concurrent test, every time.** The race detector finds real
   races only on code paths it actually executes, so your tests have to exercise contention.

**Python contrast.** There is no GIL. Two goroutines genuinely run on two cores, so data races
are real and silent — the thing Python's GIL was accidentally protecting you from.

**Artifact.** Parallel index build + a concurrent-safe feature cache, both `-race` clean.

---

## GO-8 — I/O, encoding and file formats

**Teaches.** `io.Reader`/`io.Writer` composition, `bufio`, `encoding/binary`, `encoding/json`,
`encoding/csv`, `os.File`, and designing an on-disk format.

```go
// WriteVarint writes a gap-encoded posting list. Compression is not an
// optimisation here: it is what makes the index fit in page cache (§4.2).
func WritePostings(w io.Writer, p Postings) error {
	bw := bufio.NewWriter(w)
	buf := make([]byte, binary.MaxVarintLen64)
	var prev uint32
	for _, id := range p {
		n := binary.PutUvarint(buf, uint64(id-prev)) // store the gap, not the id
		if _, err := bw.Write(buf[:n]); err != nil {
			return err
		}
		prev = id
	}
	return bw.Flush()
}
```

**Gotcha.** An unbuffered `os.File` write per posting is a syscall per posting. `bufio` is not
a nicety; it is the difference between a 40-second and a 0.4-second index build. Measure it —
that is a GO-11 exercise waiting to happen.

**Artifact.** On-disk inverted index with a header, a term dictionary, and gap+varint postings;
round-trip tested.

---

## GO-9 — HTTP services

**Teaches.** `net/http`, `http.ServeMux` with method+path patterns (Go 1.22+), middleware as
`func(http.Handler) http.Handler`, timeouts, graceful shutdown, `httptest`.

```go
srv := &http.Server{
	Addr:              ":8080",
	Handler:           mux,
	ReadHeaderTimeout: 5 * time.Second,  // never omit: this is the slowloris fix
	ReadTimeout:       10 * time.Second,
	WriteTimeout:      15 * time.Second,
	IdleTimeout:       60 * time.Second,
}
```

**Gotcha.** `http.ListenAndServe` with the default `http.DefaultServeMux` and no timeouts is
the single most common production Go mistake. Always construct `http.Server` explicitly.

**Artifact.** A `/rank` endpoint serving B7, with a p99 latency histogram and load-shedding
above a configured inflight count.

---

## GO-10 — protobuf and gRPC

**Teaches.** `.proto` schemas, `protoc-gen-go` / `protoc-gen-go-grpc`, unary and streaming
RPCs, interceptors, deadline propagation, and schema evolution rules (never reuse a field
number; reserve it).

**Why it belongs here.** Feature services and model servers in these case studies are almost
universally gRPC. The deadline-propagation semantics — a client deadline becoming a server
`ctx` — is the mechanism that makes a multi-hop ranking funnel respect one latency budget.

**Artifact.** A feature-fetch service with a streaming batch endpoint, deadline-aware.

---

## GO-11 — performance

**Teaches.** `go test -bench`, `benchstat`, `pprof` (CPU, heap, block, mutex), escape analysis
(`go build -gcflags=-m`), allocation reduction, `sync.Pool`, bounds-check elimination, and
profile-guided optimisation (`go build -pgo`).

```bash
go test -bench=Dot -benchmem -count=10 ./linalg > new.txt
benchstat old.txt new.txt
go test -bench=Dot -cpuprofile=cpu.out ./linalg && go tool pprof -http=: cpu.out
```

**The exercise that teaches the most.** Take `Dot` from GO-6 and make it 4× faster without
changing its signature: eliminate bounds checks, unroll by four to break the dependency chain
on the accumulator, and confirm with `benchstat` at `-count=10` that the difference is real and
not noise. Then check `-gcflags=-m` to prove nothing escaped to the heap.

**Gotcha.** A benchmark whose result is unused gets optimised away. Assign to a package-level
sink variable.

**Artifact.** A benchmarked, profiled `linalg` with a documented before/after and the
`benchstat` output in the README.

---

## GO-12 — the cgo boundary

**Teaches.** When to leave Go, and how to do it without wrecking the build. `cgo` basics, the
cost of a cgo call (roughly tens of nanoseconds — negligible per inference, fatal per scalar
op), and ONNX Runtime from Go for models you did not train yourself.

**The rule.** You cross the boundary **once per request**, never inside a loop. A cgo call per
matrix element is slower than pure Go by an order of magnitude.

**Primary use in Part 6.** `github.com/yalue/onnxruntime_go` — load an ONNX-exported model and
run inference from Go. This is the supported path for B11's serving half: train in Python (or
anywhere), export to ONNX, serve in Go. See Part 7.

---

## GO-13 — shipping

**Teaches.** Module versioning and `/v2` paths, `go.sum` and `GONOSUMCHECK`, `govulncheck`,
multi-stage `Dockerfile` on `distroless`/`scratch` with a non-root user, `CGO_ENABLED=0` static
builds, structured logging with `log/slog`, OpenTelemetry traces and metrics, and `GOMEMLIMIT`.

```dockerfile
FROM golang:1.24 AS build
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -trimpath -ldflags="-s -w" -o /out/serve ./cmd/serve

FROM gcr.io/distroless/static-debian12:nonroot
COPY --from=build /out/serve /serve
USER nonroot:nonroot
ENTRYPOINT ["/serve"]
```

**Artifact.** The B14 service, containerised, traced, vulnerability-scanned.

---

## GO-14 — synthesis

No new language features. You are handed an **unseen** problem from the catalog in Part 1 and
build it end to end: data structure + concurrency + service + tests + benchmark + trace, using
only tools unlocked above. If you reach for something you have not unlocked, that is the signal
to go back a rung rather than to copy from a tutorial.

---

## 5.15 Go reference shelf

**Official and free.**
*A Tour of Go* (`go.dev/tour`) — do it in one sitting, before GO-1 ·
*Effective Go* (`go.dev/doc/effective_go`) — read once at GO-3, again at GO-7 ·
*The Go Programming Language Specification* (`go.dev/ref/spec`) — short, and the only
authority · *The Go Memory Model* (`go.dev/ref/mem`) — read at GO-7, it is what "race" means ·
*Go Blog* (`go.dev/blog`) — the slice-internals, strings/bytes/runes, error-handling, generics
and pprof posts specifically · *Go Wiki: Code Review Comments* — the idiom checklist ·
*Go by Example* (`gobyexample.com`) — the lookup table you will actually use daily ·
*Learn Go with Tests* (Chris James, `quii.gitbook.io/learn-go-with-tests`) **[free]** — the
best match for this file's testing-first stance; work it alongside GO-1…GO-7.

**Books.**
Donovan & Kernighan, *The Go Programming Language* (Addison-Wesley 2015) **[paid]** — pre-generics
but still the best single book on the language's semantics ·
Harsanyi, *100 Go Mistakes and How to Avoid Them* (Manning 2022) **[paid]** — read the slices,
concurrency and optimisation sections after GO-7; it is a list of the bugs you are about to
write · Cox-Buday, *Concurrency in Go* (O'Reilly 2017) **[paid]** ·
Bodner, *Learning Go* 2e (O'Reilly 2024) **[paid]** — the best modern (generics-aware) intro.

**Courses using Go.** MIT **6.5840** *Distributed Systems* **[free]** — the labs are in Go and
build Raft and a sharded KV store; doing them after GO-7 is the highest-leverage systems work
on this entire list.

## 5.16 The Go numerical and systems stack

| Need | Package | Note |
|---|---|---|
| Matrices, BLAS/LAPACK | `gonum.org/v1/gonum/mat`, `/blas`, `/lapack` | The "NumPy of Go". Write your own first (B1), then compare. |
| Statistics, distributions | `gonum.org/v1/gonum/stat`, `/stat/distuv` | |
| Optimisation (nonlinear) | `gonum.org/v1/gonum/optimize` | BFGS, L-BFGS, Nelder–Mead |
| Linear programming | `gonum.org/v1/gonum/optimize/convex/lp` | `lp.Simplex` — used by B5 (§4.13) |
| Graphs | `gonum.org/v1/gonum/graph` | Topo sort, shortest paths, community detection |
| Plotting | `gonum.org/v1/plot` | For the residual/ACF plots M.TS asks for |
| Autodiff / tensors | `gorgonia.org/gorgonia` | Real autodiff in Go; small community — see Part 7 |
| Full-text search | `github.com/blevesearch/bleve` | Read its source **after** B7, as a comparison |
| ONNX inference | `github.com/yalue/onnxruntime_go` | The GO-12 serving path |
| Concurrency helpers | `golang.org/x/sync/errgroup`, `/semaphore` | |
| Benchmark stats | `golang.org/x/perf/cmd/benchstat` | Required by GO-11 |

---

# PART 6 — The build ladder

Fifteen rungs. Each one names the theory it needs (Part 4 or Part 3), the Go it needs (Part 5),
what you write, and the **acceptance test** that says you are done. The acceptance test is
always a *number that matches theory*, never "it runs."

**The discipline.** No ML framework below B11. No `gonum` until you have written the same
thing yourself and can explain the difference. Every rung ships tests, a benchmark, and a
one-page write-up naming the failure mode you found.

| Rung | Builds | Theory | Go |
|---|---|---|---|
| **B0** | numerics kit | M.NS §3.4 | GO-0, GO-1 |
| **B1** | linear algebra kit | T.LA §3.3 | GO-2, GO-3 |
| **B2** | ERM, losses, gradient descent | M.ML §3.4, T.CalcOpt §3.3 | GO-3, GO-5 |
| **B3** | metrics and calibration | M.ML §3.4, T.MLTheory §3.3 | GO-4, GO-5 |
| **B4** | classical models from scratch | M.ML, T.MLTheory | GO-4, GO-5 |
| **B5** | optimisation: simplex + duality | T-OPT §4.13 | GO-3, GO-4 |
| **B6** | recommender + bandit exploration | T-REC §4.1, T-RL §4.14 | GO-4, GO-7 |
| **B7** | search: index, BM25, ANN, LTR | T-IR §4.2 | GO-2, GO-4, GO-7, GO-8, GO-11 |
| **B8** | ad auction and pacing | T-AUCTION §4.3 | GO-3, GO-4 |
| **B9** | forecasting: ETS, ARIMA, quantile | T-TS §4.4 | GO-1, GO-6 |
| **B10** | graphs: CC, PageRank, Louvain, node2vec | T-GRAPH §4.5 | GO-2, GO-4, GO-7 |
| **B10b** | entity resolution: MinHash/LSH + Fellegi–Sunter | T-ER §4.13 | GO-2, GO-4 |
| **B11** | autodiff, MLP, transformer block | T-DL §4.6, T-NLP §4.7 | GO-3, GO-11, GO-12 |
| **B12** | causal: IPW, DiD, CUPED, uplift | T-CAUSAL §4.10 | GO-1, GO-5 |
| **B13** | streaming: watermarks, windows, exactly-once | T-STREAM §4.11 | GO-7, GO-8 |
| **B14** | the platform: features, serving, drift | T-MLSYS §4.12, §4.15 | GO-9…GO-13 |

---

### B0 — `numkit`: floating point you can trust

**Build.** `KahanSum`, `LogSumExp`, `Softmax` (max-shifted), `AlmostEqual(a, b, relTol)`,
`Hypot`, `Log1p` wrappers, and a money type in integer cents.

**Acceptance.** (1) Summing `0.1` ten thousand times: naive is off by ≈1.6e-10, yours is exact;
and on `[1e16, 1, 1, -1e16]` naive gives 0 while yours gives 2. (2) `Softmax([1000, 1001])` does
not produce `NaN`, and `LogSumExp([1000, 1001]) ≈ 1001.3133`. (3) You can state the condition
number of `x - y` for nearby `x, y` and demonstrate the cancellation it predicts. (4) You can
name one input where Kahan does **not** help, and say why (see the GO-1 exercise).

**Why it is first.** Every later rung produces a number you must trust. In this domain, wrong
numbers do not crash — they slightly degrade a metric, and you ship them.

---

### B1 — `linalg`: vectors and matrices

**Build.** `Vec` ops (`Dot`, `Norm`, `Cosine`, `Axpy`), `Mat` with strides, `MatMul` (naive,
then cache-blocked), `MatVec`, `Transpose`, Gaussian elimination with partial pivoting, then
QR by Householder, then power iteration for the dominant eigenpair.

**Acceptance.** (1) Blocked `MatMul` beats naive by ≥2× at n=512, proven with `benchstat`.
(2) Your solver's residual `‖Ax−b‖/‖b‖` on a Hilbert matrix degrades as the condition number
predicts — you have now *seen* §3.4's κ. (3) Power iteration recovers the top eigenvector of a
symmetric matrix to 1e-8. (4) `Cosine` returns a documented sentinel, not `NaN`, on a zero vector.

**Then** compare against `gonum/mat` and explain every difference in speed you find.

---

### B2 — `learn`: empirical risk and gradient descent

**Build.** The ERM loop: `Loss` interface (`Value`, `Grad`), squared loss, logistic loss, L1/L2
regularisers, batch GD, SGD with shuffling, mini-batch, learning-rate schedules, and the
finite-difference gradient checker from GO-5.

**Acceptance.** (1) FD check passes at `1e-6` relative for every loss. (2) Closed-form OLS and
GD agree to 1e-6 on a well-conditioned problem, and you can explain the gap when it is
ill-conditioned. (3) Logistic regression on a synthetic separable set diverges in the weights —
you observe it, and fix it with L2, having predicted it first.

---

### B3 — `metrics`: honest evaluation

**Build.** Confusion matrix, precision/recall/F1, ROC and PR curves with proper tie handling,
AUC by the rank-sum identity (**not** by trapezoid — then verify they agree), NDCG@k, MRR,
MAP, reliability diagram and ECE, and leak-free splitters: random, grouped, and **time-cut**.

**Acceptance.** (1) Your AUC matches the pairwise-ranking-probability definition computed by
brute force on 200 points. (2) On an imbalanced synthetic set you produce a model with 99%
accuracy and 0.0 recall, and you write the paragraph explaining why that is the default outcome
in fraud. (3) The time-cut splitter refuses a shuffled split on timestamped data.

---

### B4 — classical models, no framework

**Build.** k-NN with a k-d tree, Naive Bayes, linear + logistic regression (from B2), k-means
with k-means++ init, PCA via your B1 power iteration or SVD, a decision tree with Gini/entropy
splitting, then gradient-boosted trees.

**Acceptance.** (1) Your GBT beats your single tree on a held-out set and you can state which
hyperparameter controls the bias/variance trade-off and why. (2) k-means++ beats random init on
a dataset where you constructed the bad local optimum deliberately. (3) PCA reconstruction error
equals the sum of discarded eigenvalues, to tolerance.

**Covers.** A surprising share of the "Other" family (101) is a well-tuned GBT behind a good
feature pipeline. Knowing that is worth more than knowing another architecture.

---

### B5 — optimisation

**Build.** Simplex for LP in standard form (Bland's rule for anti-cycling), the dual and a
shadow-price readout, branch-and-bound over your LP for small MIPs, the Hungarian algorithm for
assignment, and 2-opt for a small VRP.

**Acceptance.** (1) Your simplex and `gonum/optimize/convex/lp` agree on 100 random feasible
LPs. (2) You read a shadow price off the dual and correctly predict the objective change from a
unit relaxation of that constraint. (3) On a 30-city TSP, 2-opt gets within a stated percentage
of the best known tour, and you report the gap honestly.

**Covers.** Pricing, dispatch, courier-wait optimisation, menu ordering, inventory allocation —
much of family 12.

---

### B6 — the recommender

**Build.** Implicit ALS (the closed-form update from §4.1), BPR-SGD, a two-tower scorer with
sampled softmax and the logQ correction, brute-force retrieval, then ANN from B7. Add an
ε-greedy and a Thompson-sampling re-ranker, and an IPS off-policy evaluator.

**Acceptance.** (1) ALS objective decreases monotonically every half-iteration — if it does not,
your update derivation is wrong, and this is how you find out. (2) Removing the logQ correction
visibly collapses recommendations onto head items, measured by catalog coverage. (3) Your IPS
estimate on logged data with known propensities recovers the true policy value within its
confidence interval; with clipping, you can plot the bias/variance trade-off.
(4) A random split beats a time-cut split on offline NDCG — you show the leak numerically.

**Covers.** Family 1 (65 studies) — Netflix, Spotify, Instacart, Pinterest, Etsy, LinkedIn.

---

### B7 — the search engine

**Build.** Tokeniser + normaliser, in-memory then on-disk inverted index (gap + varint from
GO-8), boolean retrieval with the GO-2 intersection, TF-IDF then BM25, WAND / block-max WAND
top-k, a term dictionary with a skip structure, HNSW built by hand, hybrid lexical+vector
fusion (reciprocal rank fusion), and a pairwise LambdaRank-style reranker on your B2 machinery.

**Acceptance.** (1) BM25 scores match a hand-computed value on a three-document toy, exactly.
(2) WAND returns identical top-10 to exhaustive scoring while touching ≥5× fewer postings —
both numbers reported. (3) HNSW recall@10 vs `efSearch` traces the expected curve, and you can
state your index's memory per vector. (4) The LTR reranker improves NDCG@10 over BM25 on a
held-out query set, and you name the position bias you did **not** correct for and what it cost.
(5) Index build is parallel (GO-7), `-race` clean, and 10× faster buffered than unbuffered.

**Covers.** Family 2 (36 studies), the retrieval half of family 5, and every "search food and
grocery items" study in the catalog.

---

### B8 — the ad auction

**Build.** Second-price and GSP allocation, VCG payments, eCPM ranking with a calibrated pCTR
from B3, reserve prices, budget pacing with a PID-ish controller, and a pacing simulator.

**Acceptance.** (1) Your Vickrey implementation is truthful under a brute-force search over
misreports on a 4-bidder toy; your GSP is not, and you exhibit the profitable deviation.
(2) VCG revenue ≤ GSP revenue on your generated instances, matching theory.
(3) With a deliberately miscalibrated pCTR (multiply by 1.5), allocation changes and you
quantify the advertiser harm.

**Covers.** The ads studies in family 2, plus payment-gateway and bid-optimisation studies in
family 12.

---

### B9 — forecasting

**Build.** STL-style decomposition, simple/Holt/Holt–Winters exponential smoothing, AR/MA/ARMA
with Yule–Walker then conditional-sum-of-squares ARIMA, ACF/PACF, rolling-origin backtesting,
pinball loss and quantile forecasts, hierarchical reconciliation (bottom-up, then OLS/MinT),
and Croston for intermittent series.

**Acceptance.** (1) On a synthetic AR(1) with known φ, your estimate recovers φ within its
standard error. (2) Holt–Winters beats seasonal-naïve on a seasonal series and loses to it on a
random walk — you predicted both before running. (3) Reconciled hierarchical forecasts are
coherent (children sum to parent) to machine precision. (4) Your p90 ETA forecast has ~90%
empirical coverage on holdout; if not, you diagnose why.

**Covers.** Family 3 (27 studies) — Uber ETA, Ocado/Zalando demand, DoorDash delivery times.

---

### B10 — graphs

**Build.** CSR adjacency, BFS/DFS, union-find connected components, PageRank by power iteration
(reusing B1), Louvain modularity optimisation, triangle counting, node2vec biased walks +
skip-gram with negative sampling (reusing B2's SGD), and a GraphSAGE mean-aggregation layer.

**Acceptance.** (1) PageRank sums to 1 and matches a hand-solved 4-node chain. (2) Louvain finds
the planted communities in an LFR-style synthetic benchmark at a stated mixing parameter.
(3) Your node2vec embeddings separate the planted communities under k-means better than random,
measured with NMI. (4) You detect a planted fraud ring — a dense subgraph — that no per-node
feature flags, and you write down why.

**Covers.** Family 4 (24 studies) — Stripe Radar-class, Swiggy/Grab/Zillow trust-and-safety.

---

### B10b — entity resolution

**Build.** Normalisation, standard blocking + sorted-neighbourhood, MinHash signatures, banded
LSH with the \((b,r)\) tuning from §4.13, Jaro–Winkler and Levenshtein comparators,
Fellegi–Sunter scoring with EM-estimated m/u probabilities, transitive closure with
canonicalisation.

**Acceptance.** (1) Your LSH S-curve matches \(1-(1-s^r)^b\) empirically. (2) Pairs-completeness
and reduction ratio reported together — improving one at the other's expense is the whole game.
(3) Cluster-level F1 and pairwise F1 disagree on your data and you explain which one the
business cares about.

---

### B11 — deep learning, by hand

**Build.** A reverse-mode autodiff tape (`Value` nodes with `grad` and a topological backward
pass), an MLP with He init, SGD → momentum → Adam, dropout, layer norm, then a single
transformer block: scaled dot-product attention, multi-head, causal mask, residual + LayerNorm,
feed-forward. Train a character-level language model on a small corpus. Then export a
Python-trained model to ONNX and serve it from Go via GO-12.

**Acceptance.** (1) Every backward op passes the FD gradient check from GO-5. (2) Your
attention output matches a `gonum` reference implementation to 1e-10. (3) Removing the
\(1/\sqrt{d_k}\) scale measurably degrades training, as the variance argument in §4.6 predicts.
(4) Training loss on the char-LM falls below the unigram-entropy baseline, which you computed
first. (5) The ONNX-served model's outputs match the Python original to 1e-5.

**Scope honesty.** This is the most expensive rung on the ladder, and the one most in tension
§2.3's warning. It is also the one that permanently ends treating attention as magic. Budget
accordingly — and if you skip it, skip it *deliberately* and use the ONNX path (Part 7) for
family 5 instead.

**Covers.** Families 5–6 (26 studies), and the neural half of families 1–2.

---

### B12 — causal inference

**Build.** Two-arm A/B with correct variance and sample-ratio-mismatch check, propensity
estimation (from B2 logistic), IPW and self-normalised IPW, standardisation/g-formula,
difference-in-differences with clustered standard errors, CUPED variance reduction, a two-model
and a transformed-outcome uplift estimator, and a sequential-testing guard.

**Acceptance.** (1) On simulated data with a known ATE and a known confounder, naive difference
in means is biased and IPW recovers the truth — you show both numbers. (2) CUPED reduces
variance by \(1-\rho^2\), matching theory to within Monte Carlo error. (3) Your uplift model
ranks *persuadables* above *sure things* on data where you planted both. (4) Peeking 20 times
at α=0.05 gives a false-positive rate well above 5%, measured, and your guard fixes it.

**Covers.** Family 9 (14 studies), plus the experimentation layer every other family needs.

---

### B13 — streaming

**Build.** An event-time pipeline: source with out-of-order events, a watermark generator,
fixed/sliding/session windows, triggers with discarding vs accumulating panes, allowed lateness
with a dropped-record counter, an idempotent sink with dedup keys, and checkpoint/restore.

**Acceptance.** (1) Replaying the same input twice produces identical sink state —
exactly-once **effect** demonstrated, not claimed. (2) Session windows correctly merge on a
late event that bridges two sessions. (3) You can state, from measurement, the state-size cost
of extending allowed lateness from 1 minute to 1 hour. (4) Under induced backpressure, the
pipeline sheds according to policy instead of growing an unbounded queue — and you relate the
queue growth to Little's law (§3.3).

**Covers.** Family 10 (5 studies) and the ingestion layer of everything else.

---

### B14 — the platform

**Build.** A feature store with point-in-time-correct joins and an offline/online parity test;
a model server (GO-9/GO-10) with batching, timeouts, and shadow traffic; a drift monitor
computing PSI and KL between reference and live distributions; an evaluation harness; canary
deployment with automatic rollback on an SLO burn-rate alert; OpenTelemetry traces end to end.

**Acceptance.** (1) A deliberately introduced training/serving skew (a feature transformed
differently in the two paths) is **caught by the parity test**, not by a metric regression
weeks later. (2) Your drift monitor fires on an injected covariate shift and does not fire on
resampled in-distribution data — both false-positive and false-negative rates reported.
(3) The canary rolls back automatically when the fast burn-rate window is exceeded.
(4) One trace spans retrieval → features → model → response with a latency breakdown that sums.

**Covers.** Family 11 by count, and the real content of nearly all 309.

---

## 6.15 Suggested order

There is no single correct path, but this one has the fewest blocked dependencies:

```
B0 → B1 → B2 → B3 → B4          the floor; nothing below works without it
   → B7                          search first: the richest systems payoff per hour
   → B6 → B8                     the ranking family and its economics
   → B9 → B12                    forecasting and the causal layer that validates it
   → B10 → B10b                  graphs and identity
   → B5                          optimisation (independent; can move earlier)
   → B13 → B14                   the platform, once there is something to serve
   → B11                         deep learning last, or deliberately skipped
```

**If you have limited time, do B0–B3, B7 and B14.** That combination — trustworthy numerics,
honest metrics, a real retrieval system, and a real platform — explains more of the 309 than
any amount of modelling depth.

---

# PART 7 — The Python boundary

Go is the default (§0.3). These are the cases where it is not, each with the reason and the
mitigation. **This list is exhaustive for the ladder in Part 6** — anywhere else, use Go.

| Where Go stops | Why | What to do |
|---|---|---|
| **Training anything large on a GPU** | No maintained CUDA-backed autodiff. Gorgonia exists and works on CPU, but the ecosystem, kernels and pretrained weights are all in PyTorch/JAX. | Train in Python, **export to ONNX**, serve in Go (GO-12). B11 explicitly does both halves. |
| **Pretrained model weights and tokenisers** | HuggingFace tooling is Python-first; tokenizer parity is hard to reproduce exactly. | Use the Rust `tokenizers` bindings or call an embedding service; never hand-port a tokeniser and hope. |
| **ARIMA/ETS model *selection*** | `statsmodels` and `forecast`/`fable` encode decades of edge cases in `auto.arima`. | Implement the estimators yourself (B9 — that is the point), but cross-check your fits against `statsmodels` or R `fable` on the same series. |
| **Advanced causal estimators** | DoubleML, EconML and DoWhy have no Go equivalent. | Implement IPW/DiD/CUPED yourself (B12); reach for Python only for DML/causal forests, and only after B12. |
| **Exploratory data analysis and plotting** | No pandas. `gonum/plot` is fine for fixed reports and bad for exploration. | Explore in a notebook; once the transform is decided, **port it to Go and parity-test it**. This is exactly the training/serving-skew discipline B14 tests. |
| **Industrial MIP/CP solvers** | OR-Tools has no official Go binding; CPLEX/Gurobi Go support is thin. | `gonum/.../lp` for LP; your own branch-and-bound for small MIPs (B5); for real routing, run OR-Tools behind a small Python or C++ service and call it. |
| **Scientific special functions, rare distributions** | `gonum/stat/distuv` covers the common ones; SciPy covers everything. | Check `distuv` first — it is better stocked than people expect. |

**The one rule that keeps this honest:** whenever a transform is computed in Python for
training and in Go for serving, it gets a **parity test** that runs both and asserts agreement
to tolerance on a fixed sample. Training/serving skew is the most common silent failure in the
309 case studies, and a cross-language boundary is where it breeds.

---

# PART 8 — Master bibliography

Organised by discipline rather than by family, so it works as a shelf. **[free]** entries are
author- or publisher-hosted at no cost. Every link was checked 2026-09-16. Where a book appears
in a Part 4 ceiling it is not repeated in full here — the ceiling has the chapter map.

## 8.1 Mathematics

**Foundations and proof.**
Hammack, *Book of Proof* 3e **[free]** — `richardhammack.github.io/BookOfProof/` ·
Velleman, *How to Prove It* 3e (Cambridge) **[paid]** ·
Rosen, *Discrete Mathematics and Its Applications* 8e (McGraw-Hill) **[paid]** ·
Lehman, Leighton & Meyer, *Mathematics for Computer Science* **[free]** — MIT 6.042J's text,
the single best free discrete-maths book · Graham, Knuth & Patashnik, *Concrete Mathematics*
2e (Addison-Wesley) **[paid]** — for generating functions and asymptotics when you need them.

**Linear algebra.**
Strang, *Introduction to Linear Algebra* 6e (Wellesley-Cambridge) **[paid]**; MIT **18.06**
video lectures **[free]** · Axler, *Linear Algebra Done Right* 4e (Springer) **[free]** —
author-hosted; the proof-first route · Trefethen & Bau, *Numerical Linear Algebra* (SIAM 1997)
**[paid]** — the right book for conditioning and QR/SVD as engineering · Golub & Van Loan,
*Matrix Computations* 4e (JHU Press) **[paid]** — the reference ·
Horn & Johnson, *Matrix Analysis* 2e (Cambridge) **[paid]** — only when you need the theorem.

**Calculus, analysis and optimisation.**
OpenStax *Calculus* Vols 1–3 **[free]** · MIT **18.01SC / 18.02SC** (OCW) **[free]** ·
Abbott, *Understanding Analysis* 2e (Springer) **[paid]** — if the ε-δ layer is missing ·
Boyd & Vandenberghe, *Convex Optimization* (Cambridge 2004) **[free]** —
`stanford.edu/~boyd/cvxbook/` · Nocedal & Wright, *Numerical Optimization* 2e (Springer)
**[paid]** · Bertsimas & Tsitsiklis, *Introduction to Linear Optimization* (Athena) **[paid]**.

**Probability, statistics and information.**
Blitzstein & Hwang, *Introduction to Probability* 2e (CRC) **[free]** — Harvard's Stat 110 text,
author-hosted, with the best free problem set on this list ·
Grinstead & Snell, *Introduction to Probability* (AMS) **[free]** ·
Wasserman, *All of Statistics* (Springer 2004) **[paid]** — the fastest complete route for an
engineer · Casella & Berger, *Statistical Inference* 2e **[paid]** — the reference ·
Durrett, *Probability: Theory and Examples* 5e **[free]** author-hosted — measure-theoretic,
open only if a gate demands it · Cover & Thomas, *Elements of Information Theory* 2e (Wiley)
**[paid]** · MacKay, *Information Theory, Inference, and Learning Algorithms* (Cambridge 2003)
**[free]** — author-hosted; idiosyncratic and excellent ·
Vershynin, *High-Dimensional Probability* (Cambridge 2018) **[free]** — concentration
inequalities, which is what bandit regret proofs (§4.14) actually run on.

**Numerical computing.**
Higham, *Accuracy and Stability of Numerical Algorithms* 2e (SIAM) **[paid]** — the authority
behind **M.NS** · Goldberg, "What Every Computer Scientist Should Know About Floating-Point
Arithmetic" (ACM CSUR 1991) **[free]** — read before B0 · IEEE 754-2019 standard.

## 8.2 Computer science core

**Algorithms and data structures.**
Cormen, Leiserson, Rivest & Stein, *Introduction to Algorithms* 4e (MIT Press) **[paid]** ·
Sedgewick & Wayne, *Algorithms* 4e (Addison-Wesley) **[paid]**; the **algs4 booksite** is
**[free]** — `algs4.cs.princeton.edu` · Kleinberg & Tardos, *Algorithm Design* **[paid]** —
the best book on *designing* rather than cataloguing · Mitzenmacher & Upfal, *Probability and
Computing* 2e (Cambridge) **[paid]** — hashing, Bloom filters, Chernoff bounds ·
Motwani & Raghavan, *Randomized Algorithms* (Cambridge) **[paid]** ·
Blum, Hopcroft & Kannan, *Foundations of Data Science* (Cambridge 2020) **[free]** —
author-hosted; the theory layer directly under this whole file.

**Theory of computation and complexity.**
Sipser, *Introduction to the Theory of Computation* 3e **[paid]** ·
Arora & Barak, *Computational Complexity: A Modern Approach* (Cambridge) **[free]** draft ·
Garey & Johnson, *Computers and Intractability* **[paid]** — the reduction catalogue you use
when proving your routing problem is NP-hard (§4.13).

**Systems, architecture, OS, networks.**
Hennessy & Patterson, *Computer Architecture: A Quantitative Approach* 6e **[paid]** —
read the memory-hierarchy and roofline material before B1's cache-blocking and §4.12's
arithmetic intensity · Bryant & O'Hallaron, *Computer Systems: A Programmer's Perspective* 3e
**[paid]** — the single best bridge from code to machine ·
Silberschatz, Galvin & Gagne, *Operating System Concepts* 10e **[paid]** ·
Arpaci-Dusseau & Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* **[free]** —
author-hosted, and better than its price suggests ·
Kurose & Ross, *Computer Networking: A Top-Down Approach* 8e **[paid]** ·
Tanenbaum & Wetherall, *Computer Networks* 6e **[paid]** ·
Saltzer, Reed & Clark, "End-to-End Arguments in System Design" (TOCS 1984) **[free]**.

**Databases.**
Ramakrishnan & Gehrke, *Database Management Systems* 3e **[paid]** ·
Silberschatz, Korth & Sudarshan, *Database System Concepts* 7e **[paid]** ·
Hellerstein & Stonebraker (eds.), *Readings in Database Systems* ("the Red Book") 5e **[free]** ·
PostgreSQL documentation **[free]** — the MVCC chapters are a primary source for §3.3's DB gates.

## 8.3 Distributed systems and software engineering

Kleppmann, *Designing Data-Intensive Applications* (O'Reilly 2017) **[paid]** ·
Tanenbaum & Van Steen, *Distributed Systems* 4e **[free]** — author-hosted ·
Lynch, *Distributed Algorithms* (Morgan Kaufmann) **[paid]** — the formal treatment behind
FLP and quorum arguments · Newman, *Building Microservices* 2e **[paid]** ·
Nygard, *Release It!* 2e **[paid]** · Evans, *Domain-Driven Design* **[paid]** ·
Hohpe & Woolf, *Enterprise Integration Patterns* **[paid]** ·
Fowler, *Patterns of Enterprise Application Architecture* **[paid]** ·
Richards & Ford, *Fundamentals of Software Architecture* **[paid]** ·
Bass, Clements & Kazman, *Software Architecture in Practice* 4e **[paid]** ·
Beyer et al. (eds.), *Site Reliability Engineering* and *The SRE Workbook* (Google/O'Reilly)
**[free]** — `sre.google/books/` · Winters, Manshreck & Wright, *Software Engineering at
Google* **[free]** · Ousterhout, *A Philosophy of Software Design* 2e **[paid]** ·
Beck, *Test-Driven Development by Example* **[paid]** · Fowler, *Refactoring* 2e **[paid]** ·
Feathers, *Working Effectively with Legacy Code* **[paid]**.

**Foundational papers.** Lamport, "Time, Clocks, and the Ordering of Events" (CACM 1978) ·
Fischer, Lynch & Paterson, "Impossibility of Distributed Consensus with One Faulty Process"
(JACM 1985) · Brewer's CAP + Gilbert & Lynch's proof (SIGACT News 2002) ·
Ongaro & Ousterhout, "In Search of an Understandable Consensus Algorithm" (Raft, USENIX ATC 2014) ·
DeCandia et al., "Dynamo" (SOSP 2007) · Chang et al., "Bigtable" (OSDI 2006) ·
Corbett et al., "Spanner" (OSDI 2012) · Dean & Barroso, "The Tail at Scale" (CACM 2013) —
read this one before setting any p99 budget in B14.

## 8.4 Machine learning and statistics

**Core.**
James, Witten, Hastie, Tibshirani & Taylor, *An Introduction to Statistical Learning* 2e
(ISLR/ISLP) **[free]** — `statlearning.com` ·
Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning* 2e **[free]** —
Stanford-hosted · Murphy, *Probabilistic Machine Learning: An Introduction* (MIT Press 2022)
and *Advanced Topics* (2023) **[free]** drafts — `probml.github.io` ·
Bishop, *Pattern Recognition and Machine Learning* (Springer 2006) **[free]** —
Microsoft-hosted · Shalev-Shwartz & Ben-David, *Understanding Machine Learning: From Theory to
Algorithms* (Cambridge 2014) **[free]** — author-hosted; the PAC/VC source for §3.3 ·
Mohri, Rostamizadeh & Talwalkar, *Foundations of Machine Learning* 2e (MIT Press) **[free]** ·
Géron, *Hands-On Machine Learning* 3e (O'Reilly) **[paid]** — the practitioner's counterweight.

**Applied practice.**
Huyen, *Designing Machine Learning Systems* (O'Reilly 2022) **[paid]** ·
Burkov, *Machine Learning Engineering* **[paid]** ·
Zinkevich, "Rules of Machine Learning" (Google) **[free]** — 43 rules, all correct, free, and
worth more than most courses · Zheng & Casari, *Feature Engineering for Machine Learning*
(O'Reilly) **[paid]**.

## 8.5 Data engineering and warehousing

Kimball & Ross, *The Data Warehouse Toolkit* 3e (Wiley 2013) **[paid]** — grain, conformed and
slowly-changing dimensions; the "dimensions" studies in family 12 are literally this book ·
Inmon, *Building the Data Warehouse* **[paid]** ·
Reis & Housley, *Fundamentals of Data Engineering* (O'Reilly 2022) **[paid]** ·
Akidau, Chernyak & Lax, *Streaming Systems* **[paid]** ·
Narkhede, Shapira & Palino, *Kafka: The Definitive Guide* 2e **[free]**.

## 8.6 Go

See **§5.15** for the full Go shelf. Anchors: the Go spec and memory model **[free]**;
Donovan & Kernighan **[paid]**; *Learn Go with Tests* **[free]**; Harsanyi, *100 Go Mistakes*
**[paid]**; gonum documentation **[free]**.

## 8.7 Verified links

| Resource | Link |
|---|---|
| **Mathematics & CS theory** | |
| Book of Proof **[free]** | https://richardhammack.github.io/BookOfProof/ |
| MIT 6.042J *Mathematics for CS* **[free]** | https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/ |
| Axler, *Linear Algebra Done Right* **[free]** | https://linear.axler.net/ |
| MIT 18.06 Linear Algebra **[free]** | https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/ |
| Boyd & Vandenberghe, *Convex Optimization* **[free]** | https://web.stanford.edu/~boyd/cvxbook/ |
| Blitzstein & Hwang, *Introduction to Probability* **[free]** | https://projects.iq.harvard.edu/stat110/ |
| MacKay, *ITILA* **[free]** | https://www.inference.org.uk/mackay/itila/ |
| Vershynin, *High-Dimensional Probability* **[free]** | https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-book.html |
| Blum, Hopcroft & Kannan, *Foundations of Data Science* **[free]** | https://www.cs.cornell.edu/jeh/book.pdf |
| Arora & Barak, *Computational Complexity* **[free]** | https://theory.cs.princeton.edu/complexity/ |
| Goldberg, floating-point paper **[free]** | https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html |
| algs4 booksite (Sedgewick & Wayne) **[free]** | https://algs4.cs.princeton.edu/home/ |
| *Operating Systems: Three Easy Pieces* **[free]** | https://pages.cs.wisc.edu/~remzi/OSTEP/ |
| *Readings in Database Systems* **[free]** | http://www.redbook.io/ |
| Tanenbaum & Van Steen, *Distributed Systems* **[free]** | https://www.distributed-systems.net/index.php/books/ds4/ |
| Google SRE books **[free]** | https://sre.google/books/ |
| *Software Engineering at Google* **[free]** | https://abseil.io/resources/swe-book |
| **Machine learning** | |
| ISL 2e (R and Python) **[free]** | https://www.statlearning.com/ |
| ESL 2e **[free]** | https://hastie.su.domains/ElemStatLearn/ |
| Murphy, *Probabilistic ML* **[free]** | https://probml.github.io/pml-book/ |
| Bishop, *PRML* **[free]** | https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/ |
| Shalev-Shwartz & Ben-David **[free]** | https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/ |
| Mohri et al., *Foundations of ML* **[free]** | https://cs.nyu.edu/~mohri/mlbook/ |
| Zinkevich, *Rules of ML* **[free]** | https://developers.google.com/machine-learning/guides/rules-of-ml |
| **Per-domain ceilings** | |
| Mining of Massive Datasets **[free]** | http://mmds.org |
| Aggarwal, *Recommender Systems* | https://www.charuaggarwal.net/Recommender-Systems.pdf |
| Manning et al., *Introduction to Information Retrieval* **[free]** | https://nlp.stanford.edu/IR-book/ |
| Easley & Kleinberg, *Networks, Crowds, and Markets* **[free]** | https://www.cs.cornell.edu/home/kleinber/networks-book/ |
| Nisan et al., *Algorithmic Game Theory* **[free]** | https://www.cs.cmu.edu/~sandholm/cs15-892F13/algorithmic-game-theory.pdf |
| Hyndman & Athanasopoulos, *FPP3* **[free]** | https://otexts.com/fpp3/ |
| FPP — Python edition **[free]** | https://otexts.com/fpppy/ |
| Hamilton, *Graph Representation Learning* **[free]** | https://www.cs.mcgill.ca/~wlh/grl_book/ |
| Barabási, *Network Science* **[free]** | http://networksciencebook.com/ |
| Prince, *Understanding Deep Learning* **[free]** | https://udlbook.github.io/udlbook/ |
| *Dive into Deep Learning* **[free]** | https://d2l.ai/ |
| Goodfellow et al., *Deep Learning* **[free]** | https://www.deeplearningbook.org/ |
| Jurafsky & Martin, *SLP3* **[free]** | https://web.stanford.edu/~jurafsky/slp3/ |
| Eisenstein, *Introduction to NLP* **[free]** | https://github.com/jacobeisenstein/gt-nlp-class |
| Szeliski, *Computer Vision* 2e **[free]** | https://szeliski.org/Book/ |
| Smith, *DSP Guide* **[free]** | https://www.dspguide.com/ |
| Hernán & Robins, *Causal Inference: What If* **[free]** | https://miguelhernan.org/whatifbook |
| *Causal Inference for the Brave and True* **[free]** | https://matheusfacure.github.io/python-causality-handbook/ |
| Lattimore & Szepesvári, *Bandit Algorithms* **[free]** | https://tor-lattimore.com/downloads/book/book.pdf |
| Sutton & Barto, *RL: An Introduction* 2e **[free]** | http://incompleteideas.net/book/the-book-2nd.html |
| Harvard CS249r *MLSysBook* **[free]** | https://mlsysbook.ai/ |
| Google OR-Tools | https://developers.google.com/optimization |
| Christen, *Data Matching* | https://link.springer.com/book/10.1007/978-3-642-31164-2 |
| Talluri & van Ryzin, *Revenue Management* | https://link.springer.com/book/10.1007/b139000 |
| **Go** | |
| A Tour of Go **[free]** | https://go.dev/tour/ |
| Effective Go **[free]** | https://go.dev/doc/effective_go |
| Go spec **[free]** | https://go.dev/ref/spec |
| Go memory model **[free]** | https://go.dev/ref/mem |
| Go by Example **[free]** | https://gobyexample.com/ |
| Learn Go with Tests **[free]** | https://quii.gitbook.io/learn-go-with-tests |
| Gonum **[free]** | https://www.gonum.org/ |
| gonum `lp` (simplex) | https://pkg.go.dev/gonum.org/v1/gonum/optimize/convex/lp |
| Gorgonia | https://gorgonia.org/ |
| Bleve (Go full-text search) | https://blevesearch.com/ |
| onnxruntime_go | https://github.com/yalue/onnxruntime_go |

---

# PART 9 — Course index

Lecture material only. A course earns a place here by having **public notes, slides or video**
— an entry you cannot open is useless to a learner working alone.

## 9.1 Ivy League

| Institution | Course | Covers | Ceiling |
|---|---|---|---|
| **Cornell** | **CS 4/5780** *Machine Learning for Intelligent Systems* (Weinberger) — notes + full video series public | supervised learning, kernels, bias–variance, boosting | §3.3 T.MLTheory, §4.1 |
| **Cornell** | **INFO 2040 / CS 2850** *Networks* — Easley & Kleinberg is the course text | graphs, auctions, market design, cascades | §4.3, §4.5 |
| **Cornell** | **CS 4740** *Natural Language Processing* | sequence models, semantics | §4.7 |
| **Cornell** | **CS 4820** *Introduction to Analysis of Algorithms* | design + NP-completeness | §8.2, §4.13 |
| **Princeton** | **COS 226** *Algorithms and Data Structures* — the **algs4** booksite is free and enormous | the DS/algo floor, implementation-first | §3.3 T.Algo, B1/B7 |
| **Princeton** | **COS 324** *Introduction to Machine Learning* — public notes | linear models → deep nets → MDPs | §4.6, §4.14 |
| **Princeton** | **COS 418** *Distributed Systems* | consensus, consistency, fault tolerance | §4.11, §4.15 |
| **Harvard** | **CS 181** *Machine Learning* — public site | probabilistic ML, graphical models | §4.6 |
| **Harvard** | **CS 124** *Data Structures and Algorithms* | algorithms + intractability | §8.2 |
| **Harvard** | **CS 249r** *Machine Learning Systems* — **MLSysBook.ai** is the open textbook | the entire §4.12 surface | §4.12 |
| **Harvard** | **Stat 110** *Probability* (Blitzstein) — full video + free book | probability floor | §3.3 T.ProbStat |
| **Harvard** | **Causal Diagrams** (Hernán, edX, free to audit) | DAGs, confounding | §4.10 |
| **Penn** | **CIS 5200** *Machine Learning* | statistical foundations of ML | §3.3, §4.6 |
| **Columbia** | **COMS W4995** *Applied / Topics in ML* (section-dependent) | applied ML | §4.6 |
| **Brown** | **CSCI 1951-A** *Data Science* | pipelines, evaluation | §4.12 |
| **Yale** | **CPSC 477** *Natural Language Processing* | NLP sequence | §4.7 |

> Ivy course numbering and content vary by term and section. Treat the numbers as search keys,
> not guarantees; the **linked artifacts** (algs4, MLSysBook, Stat 110, Easley & Kleinberg,
> Weinberger's notes) are the durable part.

## 9.2 Peer institutions (Stanford / MIT / CMU / Berkeley)

| Course | Covers | Ceiling |
|---|---|---|
| Stanford **CS246** *Mining Massive Data Sets* | MMDS: LSH, recsys, large-scale ML, advertising | §4.1, §4.2, §4.13 |
| Stanford **CS276** *Information Retrieval and Web Search* | IIR: indexing, ranking, evaluation | §4.2 |
| Stanford **CS224W** *Machine Learning with Graphs* | node embeddings, GNNs | §4.5 |
| Stanford **CS224n** *NLP with Deep Learning* | transformers, LLMs | §4.6, §4.7 |
| Stanford **CS231n** *Deep Learning for Computer Vision* | CNNs, detection | §4.8 |
| Stanford **CS234** *Reinforcement Learning* | MDPs, policy gradient | §4.14 |
| Stanford **CS329S** *Machine Learning Systems Design* | serving, monitoring, platform | §4.12 |
| Stanford **EE364A/B** *Convex Optimization* (Boyd) | LP/QP, duality, solvers | §4.13 |
| Stanford **STATS 361** *Causal Inference* (Wager) | identification, DML | §4.10 |
| MIT **6.006 / 6.046** *Algorithms* | the DS/algo floor | §3.3 T.Algo |
| MIT **6.041SC** *Probabilistic Systems Analysis* | probability floor | §3.3 T.ProbStat |
| MIT **18.06 / 18.01SC / 18.02SC** | linear algebra, calculus | §3.3 T.LA, T.CalcOpt |
| MIT **6.5840** *Distributed Systems* — **labs in Go** | Raft, sharded KV, linearizability | §4.15, GO-7 |
| MIT **6.5940** *TinyML and Efficient Deep Learning* (Han) | quantisation, pruning, distillation | §4.12 |
| MIT **15.053** *Optimization Methods* | LP, IP, modelling | §4.13 |
| MIT **6.003** *Signals and Systems* | sampling, transforms | §4.9 |
| CMU **15-445/645** *Database Systems* (Pavlo) | MVCC, WAL, query processing | §3.3 T.SysTheory DB, §4.11 |
| CMU **11-711** *Advanced NLP* (Neubig) | structured prediction, LLMs | §4.7 |
| CMU **11-642** *Search Engines* | index + ranking implementation | §4.2 |
| Berkeley **CS186** *Database Systems* | query processing, transactions | §4.11 |
| Berkeley **CS169** *Software Engineering* | SWE practice | §4.15 |

## 9.3 IIT / IISc / NPTEL

Free, and in several cases the *best* available treatment — not a second-tier substitute.

| Course | Institution | Covers | Ceiling |
|---|---|---|---|
| **Deep Learning** — `CS6910/CS7015` (Mitesh Khapra) | IIT Madras | backprop mechanics, optimisation, attention | §4.6 |
| **Reinforcement Learning** — `106106143` (B. Ravindran) | IIT Madras | bandits, MDPs, TD, policy gradient | §4.14 |
| **Applied Time-Series Analysis** (Arun K. Tangirala) | IIT Madras | ARIMA, spectral, state space | §4.4 |
| **Deep Learning for Computer Vision** (Vineeth N Balasubramanian) | IIT Hyderabad | CNNs, detection, segmentation | §4.8 |
| **Natural Language Processing** (Pawan Goyal) | IIT Kharagpur | sequence labelling, parsing | §4.7 |
| **Data Mining** — `106105174` (Pabitra Mitra) | IIT Kharagpur | association rules, clustering, classification | §4.1, §4.13 |
| **Social Network Analysis** | IIT Kharagpur / Ropar | community detection, centrality | §4.5 |
| **Introduction to Information Retrieval** (SWAYAM) | NPTEL | indexing, ranking, evaluation | §4.2 |
| **Fundamentals of Operations Research** (G. Srinivasan) | IIT Madras | LP, simplex, duality, transportation | §4.13 |
| **Digital Signal Processing** | IIT Kharagpur / Madras | sampling, DFT, filters | §4.9 |
| **Game Theory and Mechanism Design** — `noc22_cs77` (Y. Narahari) | IISc | auctions, VCG, GSP, mechanism design | §4.3 |
| **E1 254** *Game Theory* (Narahari, CSA) | IISc | same, at graduate depth | §4.3 |
| **E1 245** *Online Prediction and Learning* (ECE) | IISc | bandits; uses Lattimore as text | §4.14 |
| **E0 270** *Machine Learning* (CSA) | IISc | statistical ML | §3.3 T.MLTheory |
| **Discrete Mathematics / Theory of Computation** | IIT Madras / Kanpur | proofs, automata, complexity | §3.3 T.Disc |

**Institutional links.**

| Resource | Link |
|---|---|
| NPTEL (all courses) | https://nptel.ac.in/ |
| NPTEL online courses portal | https://onlinecourses.nptel.ac.in/ |
| NPTEL Deep Learning (Khapra) | https://onlinecourses.nptel.ac.in/noc19_cs85/preview |
| IIT Madras CS6910/CS7015 | https://www.cse.iitm.ac.in/~miteshk/CS6910.html |
| NPTEL Reinforcement Learning (Ravindran) | https://nptel.ac.in/courses/106106143 |
| NPTEL Data Mining (Mitra) | https://nptel.ac.in/courses/106105174 |
| NPTEL Game Theory & Mechanism Design | https://onlinecourses.nptel.ac.in/noc22_cs77/preview |
| IISc E1 254 Game Theory | https://iisc.ac.in/wp-content/uploads/2017/12/E1254.pdf |
| Narahari — IISc Game Theory Lab | https://gtl.csa.iisc.ac.in/hari/ |
| IISc E1 245 Online Prediction and Learning | https://ece.iisc.ac.in/~aditya/E1245_Online_Prediction_Learning_F2018/ |
| IISc E0 270 Machine Learning | https://sml.csa.iisc.ac.in/Courses/Spring25/E0_270/JAN-2025.html |

## 9.4 Peer course links

| Resource | Link |
|---|---|
| Stanford CS246 | https://web.stanford.edu/class/cs246/ |
| Stanford CS276 | https://web.stanford.edu/class/cs276/ |
| Stanford CS224W | https://cs224w.stanford.edu/ |
| Stanford CS224n | https://web.stanford.edu/class/cs224n/ |
| Stanford CS231n | https://cs231n.stanford.edu/ |
| Stanford CS234 | https://web.stanford.edu/class/cs234/ |
| Stanford CS329S | https://stanford-cs329s.github.io/ |
| Stanford EE364A | https://web.stanford.edu/class/ee364a/ |
| MIT 6.5840 Distributed Systems (Go labs) | https://pdos.csail.mit.edu/6.824/ |
| MIT 6.5940 Efficient ML | https://efficientml.ai/ |
| MIT OpenCourseWare | https://ocw.mit.edu/ |
| CMU 15-445 Database Systems | https://15445.courses.cs.cmu.edu/ |
| CMU 11-711 Advanced NLP | https://phontron.com/class/anlp2024/ |
| Cornell CS 4/5780 | https://www.cs.cornell.edu/courses/cs4780/2024sp/ |
| Princeton COS 226 | https://www.cs.princeton.edu/courses/archive/fall24/cos226/ |
| Princeton COS 324 notes | https://princeton-introml.github.io/ |
| Harvard CS 181 | https://harvard-ml-courses.github.io/cs181-web-2024/ |
| Harvard Stat 110 | https://projects.iq.harvard.edu/stat110/ |
| Harvard CS 249r / MLSysBook | https://mlsysbook.ai/ |
| Penn CIS 5200 | https://machine-learning-upenn.github.io/ |

---

# Provenance and limits

**Sources.** The 309 one-liners in Part 1 are the Engineer1999 catalog, linked at the top of
that part. Everything else is either authored here or a public book, paper or course linked in
§8.7, §9.3 or §9.4. **This file has no external dependency and no companion document.**

**What has not been done — read this before trusting the file.**

- Course numbers and terms drift. Every link was checked 2026-09-16; the *artifacts* (books,
  notes, booksites) are durable, the *course numbers* are search keys. Ivy League numbering in
  §9.1 is the least stable part of this file — §9.2 and §9.3 are better verified.
- **Coverage is per-family, not per-study.** Part 6 gives twelve builds, not 309 runbooks.
  §2.2 states exactly what is and is not claimed.
- **No datasets are named.** Every build says what to compute, not what to compute it on.
  Synthetic data is specified where an acceptance test needs known ground truth; real public
  datasets are not listed.
- **Part 6's acceptance tests are specified but not executed.** No code implements them yet.
- **Tier 0 (§3.0) is a route, not a course.** It points at Khan Academy and OpenStax rather
  than teaching arithmetic itself, which would be a different and much longer document.
- No excluded host (Scribd, Z-Library, LibGen, Sci-Hub, Internet Archive full-text, epdf.pub,
  PDF Drive, dokumen.pub) is used as a source or linked anywhere above. Scribd appears in
  Part 1 only as a company name inside the carried catalog.
