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
PART 8   Master bibliography — maths, CS, systems, SWE, ML, security/privacy, per-domain
PART 9   Course index — Ivy League, peer institutions, IIT/IISc/NPTEL
PART 10  T-MLF — mathematical foundations of ML (IISc/NPTEL 106108841), derived and built in Python
```

**Part 10 is the one Python-first part.** It carries the statistical-learning and deep-learning
theory *under* the ceilings — ERM, Bayes optimality, density estimation, linear models,
regularisation, kernels/SVMs, backprop, CNNs, RNNs, Transformers, trees and boosting, EM/PCA and the
generative-model preview — at graduate depth, with a Python build for every module. §10.0 states
why it is exempt from §0.3; §10.1 audits what this file and `unified-curriculum.md` already had.

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
| `MLF-*` | one of the twelve ML-foundations modules | §10.4 |
| `PRE-*` | one of the four prerequisite bridges for Part 10 | §10.2 |
| `PY-*` | one of the thirteen Python build rungs | §10.5 |

Everything else you are asked to read is a **public book, paper or course**, linked in §8.8,
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

**The one exception.** Part 10 (T-MLF) is mathematics whose executable form is the NumPy array,
and its source course assigns Python. It is implemented in **Python with NumPy only**, under the
rules in §10.0; where a Part 10 rung overlaps a Go rung (B0, B2, B4, B11), the two are
parity-tested.

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
| **T.SysTheory** — reliability/tails, networks, distributed, storage, security & privacy, coding | UG→GRAD | T-STREAM, T-MLSYS, T-IR, T-GRAPH, §4.15 |
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
| **T-IR** §4.2 | T.Algo UG · T.Disc UG · M.ML · T.SysTheory Coding UG |
| **T-REC** §4.1 | T.LA UG · M.ML (incl. IPS) · T.MLTheory UG · T.SysTheory Coding grad (ANN/PQ, for B10b) |
| **T-AUCTION** §4.3 | T.ProbStat UG · T.Alg UG |
| **T-TS** §4.4 | M.TS · T.ProbStat UG · T.LA UG |
| **T-GRAPH** §4.5 | T.Disc UG · T.Algo UG · T.LA GRAD (spectral) · T.SysTheory Security grad (adversarial, for the 24 fraud studies) |
| **T-DL** §4.6 | T.CalcOpt UG→GRAD · T.LA UG · M.NS |
| **T-NLP** §4.7 | T.ProbStat UG · T-DL (in part) |
| **T-CV** §4.8 | T.LA UG · T-DL |
| **T-SIGNAL** §4.9 | T.CalcOpt UG · T.LA UG |
| **T-CAUSAL** §4.10 | T.ProbStat UG→GRAD · M.CAUSAL |
| **T-STREAM** §4.11 | T.SysTheory Distributed UG · T.SysTheory Storage UG→grad (WAL, LSM, CDC) · T.Disc UG |
| **T-MLSYS** §4.12 | T.SysTheory Reliability + Net UG · T.SysTheory Storage UG (point-in-time join) · M.NS |
| **T-OPT / T-ER** §4.13 | T.Alg UG · T.Disc UG · T.LA UG |
| **T-RL** §4.14 | T.ProbStat GRAD (concentration) · M.ML IPS |
| **§4.15 SWE** | T.SysTheory UG — all six subfamilies, including Security |
| **T-MLF** Part 10 | T.ProbStat UG · T.LA UG · T.CalcOpt UG · M.NS · then the §10.2 bridges (PRE-P, PRE-LA, PRE-CALC, PRE-NP) |

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

### T.SysTheory — the systems floor under the 309
Every gate below is here because a **named family of the 309 needs it**. A general systems
course teaches much more than this; what no case study in Part 1 requires has been cut, and the
cut is stated where it used to sit. Six subfamilies, each UG + grad-as-needed. Product labs stay
in Parts 4, 6 and 7.

**1 · Reliability and tail behaviour** — feeds T-MLSYS §4.12, §4.15; builds **B13, B14**.
- *UG.* (1) Series availability \(\prod A_i\), parallel \(1-\prod(1-A_i)\) from independence — and name the independence assumption out loud, because shared power, shared config push and shared model artefact all break it. (2) SLI/SLO vocabulary **without** the burn formula. (3) **Tail amplification under fan-out**: a request that fans out to \(n\) independent leaves, each slower than \(t\) with probability \(q\), is slow with probability \(1-(1-q)^n\) — at \(q=0.01, n=100\) that is **63%**. Derive it. This single line explains why a 100-shard retrieval tier has a p99 far worse than any shard's p99, and it governs every sharded ranker in families 1, 2 and 4.
- *UG.* (4) The **degradation ladder**: state, before you build, what the ranker returns when the model server times out — cached scores, then a popularity or recency baseline, then an error. Failing to a heuristic is a designed behaviour, not a bug you discover in an incident.
- *Grad.* Error-budget identity: budget \(= (1-\mathrm{SLO})\times\mathrm{window}\); multi-window burn ratio as rate-of-spend; renewal/reward MTBF vs availability, one worked numeric. Hedged and tied requests (Dean & Barroso) and the *extra load* they cost; retry budgets and jitter, and why naive retries turn a brownout into an outage; the circuit breaker as an explicit three-state machine.
- *Gate:* compute end-to-end tail amplification for a two-level fan-out (broker → 50 shards → 3 replicas each), then state which mitigation you would apply and what it costs.
- *Sources:* Google *SRE* + *SRE Workbook* **[free]**; Dean & Barroso, "The Tail at Scale" (CACM 2013); Nygard, *Release It!* 2e.

**2 · Networking, only where it moves a number** — feeds T-MLSYS §4.12 (serving economics, distributed training) and T-STREAM §4.11 (backpressure); builds **B13, B14**.
**Cut deliberately:** CIDR arithmetic, subnetting, L2-vs-L3 broadcast domains, routing tables. None of the 309 is a networking case study, and none of those facts changes a latency budget, a batch size or a training cost. What is kept is what appears inside an estimate.
- *UG.* (1) **Latency budget decomposition**: propagation (distance/\(c\)) + transmission (bytes/bandwidth) + queueing + service time. Compute all four for a 10 kB feature-vector request same-AZ and cross-region, and notice which term you cannot engineer away. (2) **Little's law** \(L=\lambda W\), derived from arrival/departure counts over \([0,T]\) — promoted to UG because every capacity estimate in Part 6 uses it: RPS × latency → in-flight concurrency. (3) **RPC cost model**: serialisation + framing + head-of-line blocking; protobuf/gRPC vs JSON measured on one real payload; connection reuse, and why a cold TLS handshake costs an extra round trip that a warm pool does not. (4) **Bandwidth–delay product** — why a large shard transfer is window-limited, not link-limited. (5) End-to-end argument, with the counterexample where a hop-by-hop checksum is insufficient. (6) AIMD: on ACK \(w\leftarrow w+1/w\), on loss \(w\leftarrow w/2\) — simulate 20 RTTs; this is the mental model you reuse for backpressure. (7) Failure domain vs trust boundary — the vocabulary for replica placement and for §4.15's threat model.
- *Grad.* The **\(\alpha\)–\(\beta\) cost model** for collective communication: one message of \(n\) bytes costs \(\alpha + \beta n\) per hop. Use it to compare a parameter server (\(2|W|\) bytes through one hotspot per step) against a ring (no hotspot, more hops) — the ring all-reduce volume itself is derived once, at **§4.12 item 2**, not here. Gradient compression and top-\(k\) sparsification as a bandwidth-versus-convergence trade. Edge/CDN caching for image and embedding payloads (the CV and speech families).
- *Gate:* given target RPS and measured p50/p99, compute required concurrency and pool size; then state what both become when you enable dynamic batching, and why the p99 moves the wrong way first.
- *Sources:* Kurose & Ross **or** Tanenbaum & Wetherall; Saltzer, Reed & Clark **[free]**; Barroso, Clidaras & Hölzle, *The Datacenter as a Computer* **[free]**.

**3 · Distributed systems** — feeds T-STREAM §4.11, T-MLSYS §4.12; builds **B13, B14**.
- *UG.* Happens-before on a 3-process timeline (prove one pair incomparable); CAP — which two you keep under a *named* partition; consensus safety vs liveness; **at-most-once / at-least-once / effectively-once**, and why a retried training-job submission or a retried payment scoring call must carry an idempotency key.
- *Grad.* Quorum intersection for majority quorums \(\lfloor n/2\rfloor+1\); FLP impossibility (async + one crash) and why production buys its way out with timeouts and partial synchrony; linearizability vs serializability — exhibit one schedule serializable but not linearizable. **Stragglers:** the slowest worker sets synchronous SGD's step time; state the three answers — backup workers, asynchronous/stale-synchronous updates, drop-and-continue — and what each costs in convergence, not just in wall-clock. **Consistent hashing with virtual nodes**: why an embedding-serving or feature-cache tier re-shards without moving every key.
- *Gate:* prove one incomparable pair on a 3-process timeline; then compute how many keys move when a 10-node consistent-hash ring gains one node, versus modulo hashing, and explain the cache-miss storm the second one causes.
- *Sources:* Kleppmann, *DDIA* Ch. 5–9; MIT **6.5840** **[free]**; Lynch, *Distributed Algorithms* as needed; Karger et al., "Consistent Hashing and Random Trees" (STOC 1997); DeCandia et al., "Dynamo" (SOSP 2007).

**4 · Storage, data layout and the data path** — feeds T-STREAM §4.11, T-MLSYS §4.12 (feature store), the dimension-modelling studies inside the **"Other" (101)** family, and the training-data pipeline of every other family. This is the subfamily the 309 lean on hardest.
- *UG.* (1) **Row vs column layout**: derive the bytes actually read for `SELECT one_column FROM a 100-column table` under each. That ratio is the whole reason training scans use Parquet/ORC while online feature lookups do not. (2) Projection and predicate pushdown; row-group/stripe min–max statistics and the skipping they enable — then the case where skipping does nothing because the data is unsorted on the predicate column. (3) **B-tree vs LSM**: write amplification against read amplification; why a streaming state store and an online feature KV tier are LSM (RocksDB) while an OLTP index is a B-tree; compaction and tombstones. (4) WAL durability argument; one dirty-read and one lost-update schedule. (5) Keys and functional dependencies → 3NF on a 4-attribute toy — *and* the deliberate denormalisation a wide feature table performs, stated as a trade in write cost and hot-key skew, not as a mistake.
- *UG.* (6) **Join execution**: hash join vs sort-merge cost. The one that matters here is the **as-of (point-in-time) join** — sort both sides by event time and merge with a backward-looking pointer. Its *semantics*, and why violating them is training/serving skew, are derived at **§4.12 item 7**; this subfamily owns its *execution and cost*.
- *Grad.* MVCC snapshot decision — given begin/commit timestamps of two writers, decide which version a reader sees and prove no dirty read under SI; selectivity-based row estimation in a cost model. **Change data capture:** derive why reading the write-ahead log yields a correct change stream where polling an `updated_at` column does not — polling misses deletes and misses second-order updates inside its own granularity. **Open table formats** (Delta/Iceberg/Hudi) reduced to one sentence: a manifest of immutable files plus snapshot isolation. The table ⟷ stream duality itself is owned by §4.11.
- *Gate:* compute bytes scanned for one query under row versus columnar layout with row-group skipping; then hand-execute a point-in-time join on a six-row toy and exhibit the label leakage a naive equi-join on entity id produces.
- *Sources:* Ramakrishnan & Gehrke; Kleppmann, *DDIA* Ch. 3; Abadi, Boncz & Harizopoulos, "The Design and Implementation of Modern Column-Oriented Database Systems" (FnT 2013) **[free]**; O'Neil et al., "The Log-Structured Merge-Tree" (1996); Melnik et al., "Dremel" (VLDB 2010); Armbrust et al., "Delta Lake" (VLDB 2020); PostgreSQL docs **[free]**; CMU **15-445** and **15-721** **[free]**; Kimball & Ross for the dimension studies.

**5 · Security, privacy and adversarial ML** — feeds **Fraud / trust & safety (24)**, the **Recommend / personalise (65)** family (which trains on individual user behaviour, and therefore inherits deletion, retention and re-identification obligations), the **LLM / genAI apps (19)** family, and §4.15.
**Recut:** the generic secure-design material that used to sit here is kept small and pointed at the system you actually build; the half the 309 genuinely need — privacy and adversarial ML — did not exist and is added below.
- *UG (secure design).* STRIDE applied to **the B14 serving diagram you built**, not a toy: client → gateway → feature store → model server → log sink. Authorisation as a predicate `allow(principal, action, resource)` with a separation-of-duties counterexample. State discrete-log / factoring hardness *as used* — **call vetted crypto, never invent it**. Treat a model artefact as a credential: weights leak training data, and a checkpoint bucket is a data breach waiting for a misconfigured ACL.
- *UG (data privacy).* PII inventory and minimisation; pseudonymisation vs anonymisation; **why "we removed the names" is not anonymity** — reconstruct the Netflix-Prize de-anonymisation argument (Narayanan & Shmatikov) on a toy ratings table, which is precisely the recommendation family's own kind of data. \(k\)-anonymity and its quasi-identifier failure mode. Deletion as a *pipeline* property: a deleted user still sits in last month's training set, in yesterday's feature snapshot, and inside the model's weights.
- *Grad (formal privacy).* State \((\varepsilon,\delta)\)-differential privacy; **prove** the Laplace mechanism gives \(\varepsilon\)-DP for a counting query of sensitivity 1; sequential and parallel composition. **DP-SGD** = per-example gradient clipping + Gaussian noise, and what spending the budget costs in accuracy. Federated averaging and secure aggregation as the *architectural* answer to the same question — marked **optional**: no study in the Part 1 catalog is an on-device or federated system, so this is here as the alternative you should be able to name and reject with a reason, not as a gate.
- *Grad (adversarial ML).* Evasion at inference (FGSM, then PGD as the honest baseline) vs poisoning at training time vs model extraction vs membership inference. Then the point that decides the fraud family: **fraud is adversarial and non-stationary** — the label distribution moves *because* your model shipped, so a static holdout overstates accuracy, blocked transactions never return labels, and drift monitoring is a control loop rather than a dashboard.
- *Grad (LLM serving).* Prompt injection as a confused-deputy problem: untrusted text entering a context that carries privilege. Why output filtering is not a fix, and why the instruction/data boundary has to be architectural.
- *Gate:* write the DP guarantee for one counting query and compute the Laplace scale for \(\varepsilon=1\). Separately, take one fraud study from Part 1, name its attacker, that attacker's cost per attempt, and the feedback loop your own blocking decisions create in next month's labels.
- *Sources:* Anderson, *Security Engineering* 3e **[free]**; Dwork & Roth, *The Algorithmic Foundations of Differential Privacy* **[free]**; Near & Abuah, *Programming Differential Privacy* **[free]**; Abadi et al., "Deep Learning with Differential Privacy" (CCS 2016); McMahan et al., FedAvg (AISTATS 2017); Bonawitz et al., "Practical Secure Aggregation" (CCS 2017); Kairouz et al., "Advances and Open Problems in Federated Learning" (FnT ML 2021); Shokri et al., membership inference (S&P 2017); Carlini et al., "Extracting Training Data from Large Language Models" (USENIX Sec 2021); Goodfellow, Shlens & Szegedy (ICLR 2015); Madry et al. (ICLR 2018); Biggio & Roli, "Wild Patterns" (2018); Narayanan & Shmatikov (S&P 2008); Sweeney, \(k\)-anonymity (2002); OWASP GenAI **LLM Top 10** **[free]**. Katz–Lindell or Goldreich **only** if you open a cryptography ceiling — none of the 309 requires one.

**6 · Information, coding and compression** — feeds T-IR §4.2 (the index), T-REC §4.1 (embedding stores and ANN), T-MLSYS §4.12 (weight quantisation); builds **B7, B10b, B14**.
**Recut:** this subfamily used to be a single line about erasure coding — the only part of it the 309 barely touch. Compression *is* required: it is what makes an index and a billion-vector store affordable.
- *UG.* Entropy \(H(X)=-\sum p\log p\) as the bound no lossless code beats; prefix codes and the Kraft inequality. Then the application: a **gap-encoded posting list** compresses because small gaps have low entropy — exactly what GO-8's varint writer exploits. The IR codecs themselves — variable-byte, Elias-γ, PForDelta/Simple-9 — are implemented at **§4.2 item 3**; what this subfamily owns is the *bound* you measure them against, plus **bitmap indexes (Roaring)** and the density crossover where a bitmap beats a list.
- *UG.* Cross-entropy and KL read as *coding* quantities: the log-loss you minimise is the excess bits your model costs per example. The derivation stays in **M.ML** (§3.5); the interpretation lives here.
- *Grad.* Rate–distortion intuition for **lossy vector compression**: scalar quantisation error versus **product quantisation** — split \(D\) dimensions into \(m\) subspaces with \(k\) centroids each, storing \(m\lceil\log_2 k\rceil/8\) bytes per vector instead of \(4D\) — at the usual \(k=256\) that is exactly one byte per subvector, so a 128-d float32 vector goes from 512 bytes to \(m\) — and the recall-versus-memory curve that decides whether an embedding index fits in RAM at all. Binary hashing / LSH as the crude end of the same trade. Weight quantisation shares this arithmetic; its affine map is derived at **§4.12 item 4**.
- *Grad (durability, one gate).* 3-way replication vs Reed–Solomon \(k\)-of-\(n\): storage overhead and surviving-failure count on a toy, and which one a training-data lake should pick.
- *Gate:* compress a 1,000-id posting list with gaps + varint, report bytes per posting against the entropy bound, and explain the gap. Then product-quantise 128-dimensional vectors to 16 bytes and measure the recall@10 you lost.
- *Sources:* MacKay, *ITILA* **[free]**; Cover & Thomas, *Elements of Information Theory* 2e; Manning, Raghavan & Schütze, *IIR* **Ch. 5** **[free]**; Jégou, Douze & Schmid, "Product Quantization for Nearest Neighbor Search" (TPAMI 2011); Malkov & Yashunin, "HNSW" (TPAMI 2018); Lemire et al., Roaring bitmaps (SPE 2016); Weatherspoon & Kubiatowicz, "Erasure Coding vs. Replication" (IPTPS 2002).

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
**T.SysTheory Reliability** owns availability algebra, SLO burn-rate and tail amplification ·
**T.SysTheory Networking** owns Little's law and the \(\alpha\)–\(\beta\) message cost ·
**T.SysTheory Storage** owns the row-vs-column scan estimate and the as-of join's *execution* ·
**T.SysTheory Security** owns \((\varepsilon,\delta)\)-DP, the Laplace mechanism and DP-SGD ·
**T.SysTheory Coding** owns entropy, Kraft and the bound a code cannot beat, plus product
quantisation; **T-IR §4.2** owns the IR codecs measured against that bound ·
**T-IR §4.2** owns BM25 and the index · **T-REC §4.1** owns MF and two-tower ·
**T-MLSYS §4.12** owns ring all-reduce volume, the affine quantisation map and the
point-in-time join's *semantics* ·
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
8. The adversary: fraud is non-stationary *because you shipped a model*. State the attacker's
   cost per attempt, which features are cheap for them to move, and why blocked transactions
   never return labels — the full treatment is at **T.SysTheory Security grad**, §3.3, and it
   is a prerequisite for this ceiling, not an optional extra.

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
   this at **T.SysTheory Networking UG**, §3.3) and state the shedding policy.

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
   \(2(p-1)/p \cdot |W|\) for ring all-reduce, on the \(\alpha\)–\(\beta\) message-cost
   primitive from **T.SysTheory Networking grad**, §3.3; the straggler problem underneath
   synchronous SGD is at **T.SysTheory Distributed grad**.
3. Mixed precision: why fp16 needs loss scaling, what bf16 changes, and where the master
   weights live.
4. Quantisation: derive the affine map \(q = \mathrm{round}(x/s) + z\), its dequantisation
   error bound, and the difference between post-training and quantisation-aware. The
   rate–distortion view of the same trade — and product quantisation for vectors rather than
   weights — sits at **T.SysTheory Coding grad**, §3.3.
5. Serving economics: build the roofline — arithmetic intensity, memory-bandwidth bound vs
   compute bound — and show that LLM decode is bandwidth-bound while prefill is compute-bound.
6. Batching: derive the latency/throughput curve for static batching, then show why continuous
   batching dominates it for variable-length generation.
7. Feature stores: derive **training/serving skew** as a definitional mismatch, not a bug; state
   the point-in-time-correct join that prevents label leakage. Its *execution* — sort both
   sides by event time, merge backwards — and its cost are at **T.SysTheory Storage UG**, §3.3.
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

## 4.16 T-MLF — mathematical foundations of machine learning (pointer)

**Covers.** No family directly — it is the floor-above-the-floor for T-REC, T-IR, T-DL, T-NLP and
T-CV: the statistical-learning and deep-learning theory those ceilings cite but do not teach.
Source syllabus: NPTEL 106108841 (Prathosh A P, IISc), 12 weeks.

**Derive.** Everything in the twelve **Derive** lists of §10.4 — from the finite-class ERM bound
and the Bayes classifier through SVM duality, BPTT, AdaBoost's training bound, XGBoost's split gain,
EM monotonicity, the GAN optimal discriminator and the DDPM forward marginal.

**Text · Course · Papers.** §10.4 per module; shelf in §10.6; course index in §10.7.

**Stop at.** Each module's own *Stop at* line. The whole part stops short of research-level learning
theory and of image-scale generative training.

**Build.** PY-0 … PY-12 (§10.5), in Python by explicit exception to §0.3.

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
| Compressed bitmaps | `github.com/RoaringBitmap/roaring` | Compare against your own posting lists in B7 (6) |
| Columnar files | `github.com/parquet-go/parquet-go` | Parquet reader/writer — the row-vs-column measurement in B14 (7) |
| Embedded LSM store | `github.com/cockroachdb/pebble` | A real LSM to measure write/read amplification against |
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
(6) You report **bytes per posting** for gap+varint against the entropy bound of your gap
distribution, explain the gap between them, and find the posting-list density at which a
Roaring bitmap beats the list (§3.3 T.SysTheory Coding). (7) Product-quantising your vectors to
16 bytes costs a stated recall@10, and you report memory-per-vector before and after.

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
feature flags, and you write down why. (5) You write the **adversary model** for that ring:
who the attacker is, what one attempt costs them, which of your features they can cheaply move,
and what your own blocking decisions do to next month's labels — the non-stationarity argument
from §3.3 T.SysTheory Security, applied to one named study in Part 1.

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
(5) You measure **tail amplification**: fan a request out to \(n\) shards, plot the service
p99 against \(n\), and show it tracking \(1-(1-q)^n\) — then demonstrate one mitigation
(hedged requests) and report the extra load it cost. (6) A **STRIDE pass** over your own
serving diagram produces at least one finding you then fix, and your deletion path is tested:
a deleted user disappears from the online store, the offline snapshot, and the next training
set — and you state plainly what remains inside already-trained weights.
(7) You report bytes scanned for one offline feature query under row versus columnar layout,
with and without row-group skipping.

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

**Where Part 10 fits.** PY-0…PY-5 run alongside B0–B4 (they share the theory; parity-test the
overlap). PY-7…PY-10 should precede B11 — build autodiff and attention once in Python where the
derivation is the focus, then again in Go where the systems work is. PY-11 is the theory under B4's
gradient-boosted trees.

**If you have limited time, do B0–B3, B7 and B14.** That combination — trustworthy numerics,
honest metrics, a real retrieval system, and a real platform — explains more of the 309 than
any amount of modelling depth.

---

# PART 7 — The Python boundary

Go is the default (§0.3). These are the cases where it is not, each with the reason and the
mitigation. **This list is exhaustive for the ladder in Part 6** — anywhere else, use Go. Part 10
is a declared exception with its own rules (§10.0) and appears as the last row.

| Where Go stops | Why | What to do |
|---|---|---|
| **Training anything large on a GPU** | No maintained CUDA-backed autodiff. Gorgonia exists and works on CPU, but the ecosystem, kernels and pretrained weights are all in PyTorch/JAX. | Train in Python, **export to ONNX**, serve in Go (GO-12). B11 explicitly does both halves. |
| **Pretrained model weights and tokenisers** | HuggingFace tooling is Python-first; tokenizer parity is hard to reproduce exactly. | Use the Rust `tokenizers` bindings or call an embedding service; never hand-port a tokeniser and hope. |
| **ARIMA/ETS model *selection*** | `statsmodels` and `forecast`/`fable` encode decades of edge cases in `auto.arima`. | Implement the estimators yourself (B9 — that is the point), but cross-check your fits against `statsmodels` or R `fable` on the same series. |
| **Advanced causal estimators** | DoubleML, EconML and DoWhy have no Go equivalent. | Implement IPW/DiD/CUPED yourself (B12); reach for Python only for DML/causal forests, and only after B12. |
| **Exploratory data analysis and plotting** | No pandas. `gonum/plot` is fine for fixed reports and bad for exploration. | Explore in a notebook; once the transform is decided, **port it to Go and parity-test it**. This is exactly the training/serving-skew discipline B14 tests. |
| **Industrial MIP/CP solvers** | OR-Tools has no official Go binding; CPLEX/Gurobi Go support is thin. | `gonum/.../lp` for LP; your own branch-and-bound for small MIPs (B5); for real routing, run OR-Tools behind a small Python or C++ service and call it. |
| **Scientific special functions, rare distributions** | `gonum/stat/distuv` covers the common ones; SciPy covers everything. | Check `distuv` first — it is better stocked than people expect. |
| **Part 10 — ML foundations (PY-0…PY-12)** | The object of study is the mathematics; its source course assigns Python, and every free companion text (*D2L*, *UDL*, *PML*) is NumPy-based. | NumPy only inside implementations; `sklearn`/`scipy`/`PyTorch`/`xgboost` only as test oracles (§10.3); parity-test against B0, B2, B4 and B11 where they overlap. |

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

**Information theory and coding.**
MacKay, *Information Theory, Inference, and Learning Algorithms* (Cambridge 2003) **[free]** —
author-hosted; Part I is the entropy/Kraft/prefix-code floor for §3.3's coding gates ·
Cover & Thomas, *Elements of Information Theory* 2e (Wiley) **[paid]** — the reference for
rate–distortion · Manning, Raghavan & Schütze, *IIR* **Ch. 5** **[free]** — index compression,
gap encoding, variable-byte and γ-codes, which is the theory directly under **GO-8** and **B7** ·
Jégou, Douze & Schmid, "Product Quantization for Nearest Neighbor Search" (TPAMI 2011) ·
Malkov & Yashunin, "Efficient and Robust Approximate Nearest Neighbor Search Using HNSW"
(TPAMI 2018) · Lemire, Ssi-Yan-Kai & Kaser, "Consistently Faster and Smaller Compressed
Bitmaps with Roaring" (SPE 2016) · Weatherspoon & Kubiatowicz, "Erasure Coding vs. Replication"
(IPTPS 2002).

**Databases.**
Ramakrishnan & Gehrke, *Database Management Systems* 3e **[paid]** ·
Silberschatz, Korth & Sudarshan, *Database System Concepts* 7e **[paid]** ·
Hellerstein & Stonebraker (eds.), *Readings in Database Systems* ("the Red Book") 5e **[free]** ·
PostgreSQL documentation **[free]** — the MVCC chapters are a primary source for §3.3's storage gates ·
Abadi, Boncz & Harizopoulos, *The Design and Implementation of Modern Column-Oriented Database
Systems* (FnT Databases 2013) **[free]** — the row-vs-column derivation in §3.3 ·
O'Neil, Cheng, Gawlick & O'Neil, "The Log-Structured Merge-Tree" (Acta Informatica 1996) ·
Melnik et al., "Dremel: Interactive Analysis of Web-Scale Datasets" (VLDB 2010) ·
Armbrust et al., "Delta Lake: High-Performance ACID Table Storage" (VLDB 2020).

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
read this one before setting any p99 budget in B14 ·
Karger et al., "Consistent Hashing and Random Trees" (STOC 1997) — the sharding argument in
§3.3 · Barroso, Clidaras & Hölzle, *The Datacenter as a Computer* (Morgan & Claypool)
**[free]** — where the latency and bandwidth numbers in §3.3's networking gates come from.

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
Narkhede, Shapira & Palino, *Kafka: The Definitive Guide* 2e **[free]** ·
Debezium documentation **[free]** — change data capture as log-reading, the §3.3 CDC gate in
practice · the Apache **Iceberg** and **Delta Lake** specifications **[free]** — read the table
spec, not the vendor page.

## 8.6 Security, privacy and adversarial ML

**Secure design.** Anderson, *Security Engineering: A Guide to Building Dependable Distributed
Systems* 3e (Wiley 2020) **[free]** — author's Cambridge page; the 2e is free in full and the
3e chapters were released free in November 2024, though the archived page's own wording still
describes the older embargo. Read the threat-modelling and access-control chapters before the
B14 STRIDE pass · Katz & Lindell, *Introduction to Modern
Cryptography* 3e **[paid]** and Goldreich, *Foundations of Cryptography* **[paid]** — only if
you open a cryptography ceiling, which **none of the 309 requires**.

**Privacy.** Dwork & Roth, *The Algorithmic Foundations of Differential Privacy* (FnT TCS 2014)
**[free]** — the definition, the Laplace and Gaussian mechanisms, composition ·
Near & Abuah, *Programming Differential Privacy* **[free]** — executable, and the gentler first
pass · Sweeney, "k-Anonymity" (IJUFKS 2002) · Narayanan & Shmatikov, "Robust De-anonymization
of Large Sparse Datasets" (IEEE S&P 2008) — the Netflix Prize; it is the recommendation
family's own data · Abadi et al., "Deep Learning with Differential Privacy" (CCS 2016) —
DP-SGD · McMahan et al., "Communication-Efficient Learning of Deep Networks from Decentralized
Data" (AISTATS 2017) — FedAvg · Bonawitz et al., "Practical Secure Aggregation for
Privacy-Preserving Machine Learning" (CCS 2017) · Kairouz et al., "Advances and Open Problems
in Federated Learning" (FnT ML 2021) **[free]** — the last two are **optional**: no study in
Part 1 is a federated or on-device system, so read them to be able to reject the architecture
with a reason, not because a case study demands them.

**Adversarial ML.** Goodfellow, Shlens & Szegedy, "Explaining and Harnessing Adversarial
Examples" (ICLR 2015) · Madry et al., "Towards Deep Learning Models Resistant to Adversarial
Attacks" (ICLR 2018) — PGD, and the honest evaluation baseline · Biggio & Roli, "Wild Patterns:
Ten Years After the Rise of Adversarial Machine Learning" (Pattern Recognition 2018) — the
history the fraud studies sit inside · Shokri et al., "Membership Inference Attacks Against
Machine Learning Models" (IEEE S&P 2017) · Carlini et al., "Extracting Training Data from Large
Language Models" (USENIX Security 2021) · Tramèr et al., "Stealing Machine Learning Models via
Prediction APIs" (USENIX Security 2016) · OWASP GenAI Security Project, **LLM Top 10**
**[free]** — the prompt-injection checklist for any LLM-serving study.

## 8.7 Go

See **§5.15** for the full Go shelf. Anchors: the Go spec and memory model **[free]**;
Donovan & Kernighan **[paid]**; *Learn Go with Tests* **[free]**; Harsanyi, *100 Go Mistakes*
**[paid]**; gonum documentation **[free]**.

## 8.8 Verified links

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
| **Security, privacy, adversarial ML** | |
| Anderson, *Security Engineering* (2e free; 3e released free 2024) | https://www.cl.cam.ac.uk/archive/rja14/book.html |
| Dwork & Roth, *Algorithmic Foundations of DP* **[free]** | https://www.cis.upenn.edu/~aaroth/privacybook.html |
| Near & Abuah, *Programming Differential Privacy* **[free]** | https://programming-dp.com/ |
| OWASP GenAI — LLM Top 10 **[free]** | https://genai.owasp.org/ |
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
| CMU **15-445/645** *Database Systems* (Pavlo) | MVCC, WAL, query processing | §3.3 T.SysTheory Storage, §4.11 |
| CMU **15-721** *Advanced Database Systems* (Pavlo) | columnar layout, Parquet/ORC, in-memory OLAP | §3.3 T.SysTheory Storage |
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
| **Mathematical Foundations of Machine Learning** — `106108841` (Prathosh A P) | IISc | ERM, Bayes optimality, density estimation, linear models, kernels/SVM, DL, trees/boosting, EM/PCA, generative preview | Part 10 |
| **Introduction to Statistical Pattern Recognition** — `117108048` (P. S. Sastry) | IISc | Bayes classifier, density estimation, EM, ERM/VC, SVMs, boosting | Part 10 |
| **Introduction to Machine Learning** — `106106139` (B. Ravindran) | IIT Madras | classical ML, mathematically motivated | Part 10 |

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
| NPTEL Mathematical Foundations of ML (Prathosh) | https://nptel.ac.in/courses/106108841 |
| NPTEL Statistical Pattern Recognition (Sastry) | https://nptel.ac.in/courses/117108048 |
| NPTEL Introduction to ML (Ravindran) | https://nptel.ac.in/courses/106106139 |
| Part 10's full link tables | §10.7 |

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
| CMU 15-721 Advanced Database Systems | https://15721.courses.cs.cmu.edu/ |
| CMU 11-711 Advanced NLP | https://phontron.com/class/anlp2024/ |
| Cornell CS 4/5780 | https://www.cs.cornell.edu/courses/cs4780/2024sp/ |
| Princeton COS 226 | https://www.cs.princeton.edu/courses/archive/fall24/cos226/ |
| Princeton COS 324 notes | https://princeton-introml.github.io/ |
| Harvard CS 181 | https://harvard-ml-courses.github.io/cs181-web-2024/ |
| Harvard Stat 110 | https://projects.iq.harvard.edu/stat110/ |
| Harvard CS 249r / MLSysBook | https://mlsysbook.ai/ |
| Penn CIS 5200 | https://machine-learning-upenn.github.io/ |

---

# PART 10 — T-MLF: mathematical foundations of machine learning, built in Python

**What this part is.** A complete, derivation-grade treatment of every topic in the IISc/NPTEL
course **Mathematical Foundations of Machine Learning** (Prof. Prathosh A P, Dept. of ECE, IISc
Bangalore; NPTEL `106108841`, SWAYAM run `noc26_cs02`; 12 weeks; senior UG + graduate EECS),
plus the prerequisite material that course assumes. It is written so that a learner working
alone can **derive every object on paper and then implement it from scratch in Python**, with
NumPy as the only numerical dependency, and prove the implementation correct with a number that
matches theory.

**Why it is a separate part.** Parts 3–6 teach ML only as far as the 309 case studies force it,
and stop deliberately (§2.3, §4.6 *Stop at*). This course sits *under* those ceilings: it is the
statistical-learning and deep-learning theory that T-REC, T-IR, T-DL, T-NLP and T-CV assume. §10.1
shows, topic by topic, that most of it was either absent from this file or present only as a name.

```
§10.0   Scope, the Python exception to §0.3, labels
§10.1   Coverage audit — the course vs unified-curriculum.md vs this file
§10.2   Prerequisite bridge — the probability, linear algebra, calculus and NumPy the course assumes
§10.3   The Python build contract — package layout, oracles, gradient checks, acceptance numbers
§10.4   MLF-01 … MLF-12 — one module per course week: theory → derive gate → algorithm → build → tests
§10.5   The PY build ladder, suggested pacing and the capstone
§10.6   Bibliography for Part 10 — texts with verified chapter maps, papers per module
§10.7   Course index for Part 10 — IISc/IIT/NPTEL, Ivy League, peer institutions, with links
```

---

## 10.0 Scope, the Python exception, and labels

**The exception to §0.3, stated once.** §0.3's Go-first law exists because the 309 case studies
are *systems*. Part 10 is not a system; it is mathematics whose executable form is the
n-dimensional array. The language rule for Part 10 is therefore:

> **Rule (Part 10 only).** Implement in **Python 3.11+ with NumPy**. No `scikit-learn`,
> `PyTorch`, `JAX`, `xgboost` or `scipy.optimize` **inside** an implementation. Those libraries
> are permitted **only as test oracles** — a test may call `sklearn.svm.SVC` to check that your
> SMO found the same support vectors; your SMO may not. `matplotlib` for figures. `scipy.special`
> (`logsumexp`, `expit`, `gammaln`) is allowed after you have written your own and tested it
> against **M.NS** (§3.4). Autodiff is built by hand in PY-7 and every later module uses *your*
> autodiff.

The Go ladder is unaffected. A learner doing both writes B2/B4/B11 in Go and PY-4/PY-7/PY-10 in
Python and parity-tests the overlap (Part 7's parity rule applies: same inputs, agreement to
tolerance).

**Level.** Senior undergraduate → first-year graduate. The **Derive** gates below are at the
level of IISc E1 213 / E0 270, Stanford CS229, Cornell CS 4780 and Berkeley CS 189 problem sets.
Proofs are given where a proof is the point (Bayes optimality, Novikoff, representer theorem, EM
monotonicity, AdaBoost's training bound, optimal GAN discriminator); elsewhere a complete
derivation is given and the measure-theoretic caveats are named, not carried.

**Labels (added to §0.1's registry).**

| Label | Means | Defined in |
|---|---|---|
| `MLF-01` … `MLF-12` | the twelve foundation modules, one per course week | §10.4 |
| `PRE-P`, `PRE-LA`, `PRE-CALC`, `PRE-NP` | the four prerequisite bridges | §10.2 |
| `PY-0` … `PY-12` | the Python build rungs | §10.3, §10.5 |

**One home per formula (§3.5) still holds.** Where a derivation already has a home in this file,
Part 10 *cites* it and adds only what is missing: log-loss gradient → **M.ML**; log-sum-exp and
softmax stability → **M.NS**; backprop as reverse-mode AD, Xavier/He, Adam, \(1/\sqrt{d_k}\),
multi-head attention → **T-DL §4.6**; conv output size, im2col, conv backward → **T-CV §4.8**;
PAC/VC statements → **T.MLTheory**; \(D_{\mathrm{KL}}\ge 0\) → **T.ProbStat** grad gate (5).
New homes created here: Bayes optimality, divergence-minimisation view of density estimation,
KDE bias–variance, Fisher's criterion, the full bias–variance decomposition, ridge/lasso/MAP
equivalences, SVM duality and KKT, the representer theorem, Novikoff, BPTT and gating,
encoder–decoder transformers, CART impurity, bagging variance, AdaBoost and XGBoost's split gain,
EM, PCA's variance-maximisation derivation, ELBO, GAN optimality, the DDPM forward marginal.

---

## 10.1 Coverage audit — the course against both files

**Method.** Every topic string in the course plan was searched in `unified-curriculum.md` (4,894
lines) and in this file (Parts 0–9, 3,090 lines before Part 10 was added), then each hit was read in context — raw counts
mislead ("ridge" matches *bridge*, "GAN" matches *organ*). Depth is graded:

- **N — named.** The topic appears in a list, a ToC or an ordering, with no content.
- **O — outlined.** A paragraph or formula *stated*, no derivation, no gate you could fail.
- **D — derivation-grade.** A derive/prove gate with the object written out, at the bar of §4.0b.

A topic counts as **present** only at **D**. Verdict: **Covered** (D exists; Part 10 cites it and
adds a Python build), **Thin** (O or partial D; Part 10 completes it), **Absent** (N or nothing;
Part 10 is its home).

| Wk | Course topic | `unified-curriculum.md` | This file (Parts 0–9) | Verdict → home |
|---|---|---|---|---|
| 1 | Supervised / unsupervised / generative setups | O — §6.3 *Paradigms*; S11 ordering | — | **Thin** → MLF-01 |
| 1 | Empirical risk minimisation | N — S11; `TB-ML-003` ToC line | D — §3.4 M.ML (risk, i.i.d. failure); T.MLTheory grad (PAC *stated*) | **Thin** (no finite-class bound, no error decomposition, no surrogate-loss theory) → MLF-01 |
| 2 | Bayes optimality | N — one "Bayes classifier" mention | — | **Absent** → MLF-02 |
| 2 | Density estimation via divergence minimisation | N — Wasserman ToC line | D — \(D_{\mathrm{KL}}\ge0\) (T.ProbStat); CE from likelihood (§3.4 table) | **Absent** (KL⇔MLE, forward/reverse KL, \(f\)-divergences missing) → MLF-02 |
| 3 | Maximum likelihood | O — M40, MML-6 | D — T.ProbStat UG: Bernoulli/Gaussian MLE; Cramér–Rao | **Thin** (multivariate Gaussian MLE, invariance, asymptotics missing) → MLF-03 |
| 3 | MAP estimation | N — M40 "prior/posterior" | — | **Absent** → MLF-03 |
| 3 | Nearest neighbours | O — S11, ML-4 | N — B4 build "k-NN with a k-d tree", no theory | **Thin** → MLF-03 |
| 3 | Parzen window | — | — | **Absent** → MLF-03 |
| 4 | Linear regression, least squares | O — S7, §6.3 | D — T.LA UG residual; M.ML MSE gradient; B2 closed form | **Covered** in part; geometry, Gaussian-noise MLE, QR/SVD solve → MLF-04 |
| 4 | Fisher discriminant | N — ML-4 "LDA/QDA intuition" | — | **Absent** → MLF-04 |
| 4 | Logistic regression | O — §6.3 sklearn walkthrough | D — M.ML gradient; B2 separable-data divergence | **Thin** (convexity, Newton/IRLS, softmax regression missing) → MLF-04 |
| 5 | Bias–variance decomposition | O — §6.3 formula stated | D — T.MLTheory UG "quadratic example" | **Thin** (decomposition over training sets, kNN/ridge closed forms missing) → MLF-05 |
| 5 | Ridge regression | O — §6.3 | D — M.ML L2 gradient only | **Thin** → MLF-05 |
| 5 | Lasso | O — §6.3 | N — "L1 sparsity cartoon" | **Absent** → MLF-05 |
| 5 | Probabilistic interpretation of regularisation | — | — | **Absent** → MLF-05 |
| 6 | Maximum-margin classifiers, dual form, KKT | O — S11 "margins/kernels/SVM"; S14 order | N — T.CalcOpt grad "KKT literacy" | **Absent** → MLF-06 |
| 6 | Kernel trick, RKHS | N — ESL ToC "RKHS" | — | **Absent** → MLF-06 |
| 7 | Perceptron | O — §6.5 | — | **Absent** (no convergence theorem) → MLF-07 |
| 7 | Neural networks, backpropagation | O — §6.5, S16 | D — T-DL §4.6 items 1–5; B11 in Go | **Covered** → MLF-07 cites; adds Python autodiff |
| 7 | Gradient-based optimisation | O — S14 order | D — T.CalcOpt UG GD on quadratic; §4.6 Adam | **Thin** (rates, SGD variance, momentum missing) → MLF-07 |
| 8 | Convolution, receptive fields | N — Tier 7 DL Module 4 | D — T-CV §4.8 items 1–3 | **Covered** → MLF-08 cites; adds equivariance proof, RF recurrence |
| 8 | Pooling | N — Tier 7 | — | **Absent** → MLF-08 |
| 8 | CNN architectures | N — Tier 7 list | N — §4.8 papers | **Thin** → MLF-08 |
| 8 | Transfer learning | — | — | **Absent** → MLF-08 |
| 9 | RNNs, BPTT, vanishing/exploding gradients | N — Tier 7 DL Module 5 | — | **Absent** → MLF-09 |
| 9 | GRU, LSTM | N — Tier 7 | — | **Absent** → MLF-09 |
| 10 | Attention, scaled dot-product, multi-head | O — §6.6, M45 formula | D — T-DL §4.6 items 6–7 | **Covered** → MLF-10 cites |
| 10 | Self-attention vs recurrence | O — §6.6 "why attention" | — | **Thin** → MLF-10 |
| 10 | Encoder–decoder Transformer | O — §6.6 block description | — (B11 is one decoder block) | **Thin** → MLF-10 |
| 11 | Decision trees | N — ML-5 | N — B4 build "Gini/entropy splitting" | **Absent** at rigour → MLF-11 |
| 11 | Bagging, random forests | N — ML-5 | — | **Absent** → MLF-11 |
| 11 | AdaBoost | — | — | **Absent** → MLF-11 |
| 11 | XGBoost | N — §4 library list (`TOOL`) | N — B4 "gradient-boosted trees" | **Absent** → MLF-11 |
| 12 | k-means | O — §6.3, ML-6 | N — B4 k-means++ build | **Thin** → MLF-12 |
| 12 | Gaussian mixtures, EM | N — ML-6; M43 (ASR context) | — | **Absent** → MLF-12 |
| 12 | PCA | O — M39 (SVD via power iteration) | D — T.LA grad: reconstruction error; B4 | **Thin** (variance-maximisation derivation, PPCA missing) → MLF-12 |
| 12 | GANs, VAEs, diffusion (high level) | N — DL Module 7; S17 item 6; Prince ToC | — | **Absent** → MLF-12 |
| pre | Probability theory | O — M40, MML-5/6 | D — T.ProbStat | **Covered**; multivariate Gaussian, Schur complement missing → PRE-P |
| pre | Linear algebra | O — M39, MML-3 | D — T.LA | **Covered**; spectral theorem for PSD, matrix calculus missing → PRE-LA |
| pre | Python | O — §4 library curriculum | — (Go law) | **Thin** for numerics → PRE-NP |

**Finding.** `unified-curriculum.md` is a *routing* document: it orders topics, maps them to
textbooks and states artefact-level gates, but carries almost no derivations — and its own
§17.1 audit already flags the gaps (`GAP:` GMM/EM "not covered", VAEs "marginal", diffusion
"postdates the confirmed record"). This file was derivation-grade but deliberately scoped to the
309, so the classical statistical-learning core (Weeks 2, 3, 5, 6, 9, 11, 12) was absent.
**Neither file, alone or together, met an IISc/Ivy graduate bar for this course.** Part 10 closes
every **Thin** and **Absent** row above.

---

## 10.2 Prerequisite bridge

The course lists "a basic course on probability theory and linear algebra" and "some background in
Python". §3.3 already gates the basics. These four bridges add **only** what this course uses and
§3.3 does not carry. Skip-test each gate cold (§3.0's rule).

### PRE-P — probability the course actually uses

1. **Random vectors.** Mean \(\mu=\mathbb{E}[X]\); covariance \(\Sigma=\mathbb{E}[(X-\mu)(X-\mu)^\top]\)
   is symmetric PSD because \(v^\top\Sigma v=\mathrm{Var}(v^\top X)\ge 0\). Affine map
   \(Y=AX+b\Rightarrow \mathbb{E}Y=A\mu+b,\ \mathrm{Cov}\,Y=A\Sigma A^\top\).
2. **Multivariate Gaussian.** \(\mathcal{N}(x\mid\mu,\Sigma)=(2\pi)^{-d/2}|\Sigma|^{-1/2}\exp\!\big(-\tfrac12(x-\mu)^\top\Sigma^{-1}(x-\mu)\big)\).
   Level sets are ellipsoids with axes along eigenvectors of \(\Sigma\), half-lengths \(\propto\sqrt{\lambda_i}\).
   Sampling: \(x=\mu+Lz\), \(LL^\top=\Sigma\) (Cholesky), \(z\sim\mathcal{N}(0,I)\).
3. **Marginals and conditionals (Schur complement).** Partition \(x=(x_a,x_b)\). Then
   \(x_a\sim\mathcal{N}(\mu_a,\Sigma_{aa})\) and
   \[
   x_a\mid x_b\sim\mathcal{N}\!\big(\mu_a+\Sigma_{ab}\Sigma_{bb}^{-1}(x_b-\mu_b),\ \Sigma_{aa}-\Sigma_{ab}\Sigma_{bb}^{-1}\Sigma_{ba}\big).
   \]
   *Derive* it by completing the square in \(x_a\) using the block inverse. It is used in
   Bayesian linear regression (MLF-05), PPCA (MLF-12) and the DDPM posterior (MLF-12).
4. **Product and composition of Gaussians.** If \(x\sim\mathcal{N}(\mu,\Lambda^{-1})\) and
   \(y\mid x\sim\mathcal{N}(Ax+b,L^{-1})\) then \(y\sim\mathcal{N}(A\mu+b,\ L^{-1}+A\Lambda^{-1}A^\top)\) and
   \(x\mid y\sim\mathcal{N}\big(S(A^\top L(y-b)+\Lambda\mu),\,S\big)\), \(S=(\Lambda+A^\top LA)^{-1}\)
   (Bishop *PRML* §2.3.3). Every conjugate-Gaussian result in Part 10 is this identity.
5. **Jensen's inequality.** For convex \(\varphi\), \(\varphi(\mathbb{E}X)\le\mathbb{E}\varphi(X)\); equality iff
   \(\varphi\) is affine on the support or \(X\) is a.s. constant. Used for \(D_{\mathrm{KL}}\ge 0\),
   the EM lower bound, the ELBO and the impurity-decrease proof (MLF-11).
6. **Concentration you will use.** Hoeffding: for i.i.d. \(Z_i\in[a,b]\),
   \(P(|\bar Z-\mathbb{E}Z|\ge t)\le 2\exp(-2nt^2/(b-a)^2)\). Union bound. Used in MLF-01.
7. **Exponential family.** \(p(x\mid\eta)=h(x)\exp(\eta^\top T(x)-A(\eta))\); \(\nabla A(\eta)=\mathbb{E}[T(X)]\),
   \(\nabla^2 A=\mathrm{Cov}[T(X)]\succeq 0\), hence the log-likelihood is concave in \(\eta\).

*Gate.* (i) Derive item 3 by completing the square. (ii) Prove \(\nabla A(\eta)=\mathbb{E}T(X)\) for the
Bernoulli in natural parameters. (iii) Sample \(10^5\) points from a 2-D Gaussian via Cholesky and
recover \(\mu,\Sigma\) to 2 decimals.
*Sources:* Bishop *PRML* §2.3 **[free]**; Murphy *PML1* Ch. 2–3 **[free]**; Deisenroth, Faisal & Ong,
*MML* Ch. 6 **[free]**; CS229 notes §4.1.1 and Appendix A **[free]**.

### PRE-LA — linear algebra the course actually uses

1. **Spectral theorem (real symmetric).** \(A=A^\top\Rightarrow A=Q\Lambda Q^\top\), \(Q\) orthogonal,
   \(\Lambda\) real. *Prove* eigenvalues are real and eigenvectors of distinct eigenvalues orthogonal.
   PSD \(\Leftrightarrow\lambda_i\ge 0\Leftrightarrow A=B^\top B\).
2. **Rayleigh quotient.** \(\max_{\|v\|=1}v^\top Av=\lambda_{\max}\), attained at the top eigenvector;
   the \(k\)-dimensional version (Ky Fan) \(\max_{V^\top V=I_k}\mathrm{tr}(V^\top AV)=\sum_{i\le k}\lambda_i\).
   This *is* PCA (MLF-12) and Fisher's multi-class LDA (MLF-04).
3. **SVD.** \(X=U\Sigma V^\top\); \(X^\top X=V\Sigma^2V^\top\); Eckart–Young: the best rank-\(k\)
   approximation in Frobenius norm keeps the top \(k\) singular triples, error \(\sum_{i>k}\sigma_i^2\).
4. **Projections.** \(P=X(X^\top X)^{-1}X^\top\) is symmetric and idempotent; \(I-P\) projects on the
   orthogonal complement. Pseudoinverse \(X^+=V\Sigma^+U^\top\) gives the minimum-norm least-squares solution.
5. **Matrix calculus (denominator layout).** \(\nabla_x a^\top x=a\); \(\nabla_x x^\top Ax=(A+A^\top)x\);
   \(\nabla_X\mathrm{tr}(AX)=A^\top\); \(\nabla_X\log|X|=X^{-\top}\);
   \(\nabla_X\,a^\top X^{-1}b=-X^{-\top}ab^\top X^{-\top}\). Needed for the multivariate Gaussian MLE (MLF-03),
   GMM M-step (MLF-12).
6. **Block inverse / Woodbury.** \((A+UCV)^{-1}=A^{-1}-A^{-1}U(C^{-1}+VA^{-1}U)^{-1}VA^{-1}\) — why kernel
   ridge regression inverts an \(n\times n\) and ridge a \(d\times d\) matrix and they agree (MLF-06).

*Gate.* (i) Prove item 2 with a Lagrange multiplier. (ii) Derive \(\nabla_\Sigma\) of the Gaussian
log-likelihood using item 5. (iii) Verify Woodbury numerically for random \(A,U,C,V\) to \(10^{-10}\).
*Sources:* Strang *Introduction to Linear Algebra* Ch. 6–7; *MML* Ch. 2–5 **[free]**; Petersen & Pedersen,
*The Matrix Cookbook* **[free]**; Parr & Howard, "The Matrix Calculus You Need for Deep Learning" **[free]**.

### PRE-CALC — convexity and constrained optimisation, as used

1. \(f\) convex \(\Leftrightarrow f(y)\ge f(x)+\nabla f(x)^\top(y-x)\Leftrightarrow\nabla^2 f\succeq 0\) (twice
   differentiable). Local minimum of a convex function is global.
2. \(L\)-smoothness: \(\|\nabla f(x)-\nabla f(y)\|\le L\|x-y\|\) ⇒ descent lemma
   \(f(y)\le f(x)+\nabla f(x)^\top(y-x)+\tfrac L2\|y-x\|^2\). This one inequality gives every GD rate in MLF-07.
3. Lagrangian, weak duality \(d^\star\le p^\star\), Slater ⇒ strong duality, and the four KKT
   conditions — derived and used in MLF-06, not here.
4. Subgradients: \(\partial|x|=\{\mathrm{sign}(x)\}\) for \(x\ne 0\), \([-1,1]\) at \(0\). Optimality
   \(0\in\partial f(x^\star)\). Used for the lasso (MLF-05) and hinge loss (MLF-06).

*Sources:* Boyd & Vandenberghe *Convex Optimization* Ch. 2–5 **[free]**; *MML* Ch. 7 **[free]**; CS229
notes §6.5 *Lagrange duality* **[free]**.

### PRE-NP — NumPy as a numerical language

The Python this course needs is not "Python"; it is array programming. Gate items:

1. **Shapes, strides, views.** Predict `a.shape`, `a.strides`, whether an op copies (`reshape` on a
   non-contiguous array, fancy indexing) — the Python mirror of **M.NS**/B1's strided array.
2. **Broadcasting.** State the rule (align trailing dims; size-1 stretches). Write pairwise squared
   distances with no loop: `D = (X**2).sum(1)[:,None] + (Y**2).sum(1)[None,:] - 2*X@Y.T`, then
   `np.maximum(D, 0)` — and explain why the clamp is needed (catastrophic cancellation, **M.NS**).
3. **Vectorisation discipline.** No Python loop over samples in any hot path. `np.einsum` for tensor
   contractions; `np.lib.stride_tricks.sliding_window_view` for convolution windows.
4. **Randomness.** `rng = np.random.default_rng(seed)` passed explicitly; never the global state.
5. **Stability primitives.** Your own `logsumexp`, `softmax`, `log_softmax`, `sigmoid` (branch on
   sign), `log1pexp` — tested against the **B0** acceptance cases from §6 in Python form.
6. **Linear solves.** Never `inv(A) @ b`; `np.linalg.solve`, `cholesky` + triangular solves,
   `lstsq`/`qr`/`svd` — and the conditioning reason (\(\kappa(X^\top X)=\kappa(X)^2\)).

*Gate.* Pairwise distances for \(10^4\times 10^4\) points in < 2 s with no loop; `softmax([1000,1001])`
finite; a function that returns a view and one that silently copies, both explained.
*Sources:* NumPy user guide, *Broadcasting* and *Indexing* **[free]**; Harris et al., "Array
programming with NumPy" (*Nature* 2020).

---

## 10.3 The Python build contract

**Package layout.** One package, grown module by module. Every file below is written by you.

```
mlf/
  core/        numerics.py (logsumexp, softmax, sigmoid)  rng.py  testing.py (grad_check, assert_close)
  data/        synthetic.py (every generator with known ground truth)  splits.py
  risk/        losses.py  erm.py  bounds.py                                   # MLF-01
  bayes/       decision.py  divergences.py                                    # MLF-02
  density/     parametric.py  kde.py  knn.py                                  # MLF-03
  linear/      ols.py  fisher.py  gda.py  logistic.py                         # MLF-04
  regularize/  ridge.py  lasso.py  bayes_linreg.py  biasvar.py  cv.py         # MLF-05
  kernels/     kernels.py  svm_primal.py  smo.py  krr.py  rff.py              # MLF-06
  autograd/    tensor.py  functional.py  nn.py  optim.py                      # MLF-07
  conv/        conv2d.py  pool.py  models.py  transfer.py                     # MLF-08
  seq/         rnn.py  lstm.py  gru.py  seq2seq.py                            # MLF-09
  attn/        attention.py  transformer.py                                   # MLF-10
  trees/       cart.py  bagging.py  forest.py  adaboost.py  gbm.py  xgb.py    # MLF-11
  unsup/       kmeans.py  gmm.py  pca.py  ppca.py                             # MLF-12
  gen/         vae.py  gan.py  ddpm.py                                        # MLF-12
tests/         mirrors mlf/, pytest, one test per acceptance item
```

**Four testing rules.**

1. **Ground truth first.** Every acceptance test runs on a generator in `data/synthetic.py` whose
   true parameter, Bayes error or density is known in closed form. Real data (named in §10.5) is for
   the capstone only.
2. **Gradient check everything differentiable.** Central differences,
   \(\frac{f(\theta+he_i)-f(\theta-he_i)}{2h}\), \(h=10^{-5}\) in float64; pass if the relative error
   \(\frac{\|g-\hat g\|}{\max(\|g\|,\|\hat g\|,10^{-12})}<10^{-6}\). (Same checker as GO-5, in Python.)
3. **Oracles, not dependencies.** `scikit-learn`, `scipy`, `PyTorch`, `xgboost` appear only under
   `tests/`, marked `@pytest.mark.oracle`, and the suite must pass with them uninstalled (oracle tests
   skip). A disagreement with an oracle is investigated and written up, never "fixed" by importing it.
4. **Theory numbers, not "it runs".** Each module's acceptance list states a number that theory
   predicts. A test that only checks shapes is not an acceptance test.

**Float discipline.** float64 everywhere until MLF-08; float32 allowed for CNN/RNN/Transformer
training after the float64 gradient checks pass.

---
## 10.4 The twelve modules

Every module has the same fields as a Part 4 ceiling (§4.0b), plus the three a Python build needs:

```
Week       the course week it covers, and the exact topic strings from the course plan
Floor      what must be closed first (Part 3, §10.2, or an earlier MLF module)
Theory     definitions, theorems, derivations — this is the teaching text
Derive     the gate: produce these on paper, unaided
Build      PY-n: files, signatures, algorithm, the numerical traps
Accept     numbers that match theory
Exercises  pen-and-paper problems at problem-set level
Text · Course · Papers · Stop at   as in §4.0b
```

---

### MLF-01 — Learning problems and empirical risk minimisation

**Week 1.** *Introduction to supervised / unsupervised / generative learning; learning via
empirical risk minimisation.*
**Floor.** PRE-P items 5–6; M.ML (§3.4); T.MLTheory UG.

**Theory.**

1. **The statistical setup.** Unknown distribution \(P\) on \(\mathcal{X}\times\mathcal{Y}\); sample
   \(S=\{(x_i,y_i)\}_{i=1}^n\) i.i.d. from \(P\); hypothesis class \(\mathcal{H}\subseteq\{h:\mathcal{X}\to\hat{\mathcal{Y}}\}\);
   loss \(\ell:\hat{\mathcal{Y}}\times\mathcal{Y}\to\mathbb{R}_{\ge 0}\).
   Risk \(R(h)=\mathbb{E}_{(X,Y)\sim P}\,\ell(h(X),Y)\); empirical risk \(\hat R_n(h)=\frac1n\sum_i\ell(h(x_i),y_i)\).
   The **Bayes risk** \(R^\star=\inf_{h\text{ measurable}}R(h)\) (characterised in MLF-02).
2. **One frame for all three paradigms.** Every week of this course is ERM with a particular loss
   and class — write this table into your notes, because it is what makes the course one subject:

   | Paradigm | Data | Loss \(\ell\) | Minimiser | Module |
   |---|---|---|---|---|
   | Classification | \((x,y)\), \(y\in[K]\) | \(\mathbf{1}[h(x)\ne y]\), or a surrogate | Bayes classifier | 02, 04, 06, 07, 11 |
   | Regression | \((x,y)\), \(y\in\mathbb{R}\) | \((h(x)-y)^2\) | \(\mathbb{E}[Y\mid X=x]\) | 02, 04, 05 |
   | Density estimation | \(x\) | \(-\log q(x)\) | \(q=p\) (risk = cross-entropy) | 02, 03, 12 |
   | Clustering | \(x\) | \(\min_j\|x-c_j\|^2\) | \(k\)-means centroids | 12 |
   | Dimensionality reduction | \(x\) | \(\|x-VV^\top x\|^2\), \(V^\top V=I_k\) | top-\(k\) eigenvectors | 12 |
   | Generative modelling | \(x\) | a divergence \(D(p\,\|\,q_\theta)\), estimated from samples | \(q_\theta=p\) | 02, 12 |

3. **Error decomposition.** Let \(\hat h\in\arg\min_{\mathcal{H}}\hat R_n\) and \(h_{\mathcal{H}}\in\arg\min_{\mathcal{H}}R\). Then
   \[
   R(\hat h)-R^\star=\underbrace{R(\hat h)-R(h_{\mathcal{H}})}_{\text{estimation}}+\underbrace{R(h_{\mathcal{H}})-R^\star}_{\text{approximation}}.
   \]
   Growing \(\mathcal{H}\) shrinks approximation error and grows estimation error — the
   *structural* bias–variance trade-off that MLF-05 makes quantitative for squared loss.
4. **The uniform-deviation lemma (derive).**
   \(R(\hat h)-R(h_{\mathcal{H}})=[R(\hat h)-\hat R_n(\hat h)]+[\hat R_n(\hat h)-\hat R_n(h_{\mathcal{H}})]+[\hat R_n(h_{\mathcal{H}})-R(h_{\mathcal{H}})]\le 2\sup_{h\in\mathcal{H}}|\hat R_n(h)-R(h)|\),
   because the middle bracket is \(\le 0\) by definition of \(\hat h\). Generalisation is therefore a
   statement about **uniform** convergence of empirical means over \(\mathcal{H}\).
5. **Finite classes, agnostic case (derive).** For \(\ell\in[0,1]\), Hoeffding for each fixed \(h\) and a
   union bound give \(P(\sup_{\mathcal{H}}|\hat R_n-R|\ge\varepsilon)\le 2|\mathcal{H}|e^{-2n\varepsilon^2}\). Setting the
   right side to \(\delta\): with probability \(\ge 1-\delta\),
   \[
   R(\hat h)\le R(h_{\mathcal{H}})+\sqrt{\frac{2\log(2|\mathcal{H}|/\delta)}{n}}.
   \]
   Sample complexity \(n=O(\varepsilon^{-2}\log(|\mathcal{H}|/\delta))\) — the rate T.MLTheory *states*.
6. **Finite classes, realisable case (derive).** If some \(h\in\mathcal{H}\) has \(R(h)=0\), any
   \(h\) with \(R(h)>\varepsilon\) survives \(n\) samples with probability \(\le(1-\varepsilon)^n\le e^{-n\varepsilon}\), so
   \(n\ge\varepsilon^{-1}(\log|\mathcal{H}|+\log(1/\delta))\) suffices: the **fast** \(1/\varepsilon\) rate. Explain in
   one sentence why noise costs the square.
7. **Why \(\mathcal{H}\) must be restricted.** The memoriser \(h_S(x)=y_i\) if \(x=x_i\), else \(0\), has
   \(\hat R_n=0\) and, for continuous \(P_X\), the risk of the constant predictor \(0\). The No-Free-Lunch
   theorem (Shalev-Shwartz & Ben-David Thm 5.1) makes this formal: without a prior restriction, no
   learner is uniformly good. For infinite classes the \(\log|\mathcal{H}|\) term becomes the VC
   dimension \(d_{\mathrm{VC}}\): \(\sup|\hat R_n-R|=O\big(\sqrt{(d_{\mathrm{VC}}\log(n/d_{\mathrm{VC}})+\log(1/\delta))/n}\big)\)
   (statement only; T.MLTheory grad gate (2) computes a VC dimension).
8. **Surrogate losses and calibration.** Binary \(y\in\{\pm1\}\), score \(f(x)\), margin \(m=yf(x)\).
   0–1 loss \(\mathbf{1}[m\le 0]\) is non-convex; ERM over it is NP-hard for halfspaces. Convex surrogates:
   hinge \(\max(0,1-m)\), logistic \(\log(1+e^{-m})\), exponential \(e^{-m}\), squared \((1-m)^2\).
   With \(\eta(x)=P(Y=1\mid x)\), minimise the **conditional** surrogate risk
   \(C_\eta(f)=\eta\,\phi(f)+(1-\eta)\,\phi(-f)\) pointwise:
   logistic \(f^\star=\log\frac{\eta}{1-\eta}\); exponential \(f^\star=\tfrac12\log\frac{\eta}{1-\eta}\);
   squared \(f^\star=2\eta-1\); hinge \(f^\star=\mathrm{sign}(2\eta-1)\). *Derive the first two* by
   setting \(dC_\eta/df=0\). All four have \(\mathrm{sign}(f^\star)=\mathrm{sign}(2\eta-1)\), the Bayes decision:
   they are **classification-calibrated**. A convex \(\phi\) is calibrated iff it is differentiable at
   \(0\) with \(\phi'(0)<0\) (Bartlett, Jordan & McAuliffe 2006). Consequence you will meet again:
   logistic and exponential scores recover \(\eta\); hinge scores do not, which is why an SVM needs
   post-hoc calibration (M.ML) before its output is a probability.

**Derive.** (i) Item 4. (ii) Item 5, including the constant. (iii) Item 6. (iv) The four
conditional minimisers in item 8. (v) Write the ERM loss and class for PCA and \(k\)-means.

**Build — PY-1** (`mlf/risk/`).
- `losses.py`: `zero_one(m)`, `hinge(m)`, `logistic(m)` (stable: `np.logaddexp(0, -m)`), `exponential(m)`,
  `squared(m)`, each with `grad(m)`.
- `erm.py`: `erm_finite(H, X, y, loss)` — exhaustive ERM over a finite class given as an array of
  predictions `H[j, i] = h_j(x_i)`; `threshold_class(grid)` for \(h_{t,s}(x)=s\cdot\mathrm{sign}(x-t)\).
- `bounds.py`: `hoeffding_finite(n, H_size, delta)`, `realisable_n(eps, H_size, delta)`.
- `data/synthetic.py`: `noisy_threshold(n, t0, noise, rng)` with \(X\sim U[0,1]\),
  \(\eta(x)=1-\text{noise}\) for \(x>t_0\), else \(\text{noise}\); its Bayes risk is `noise`, exactly.

**Accept.**
1. Over 2,000 replications with \(|\mathcal{H}|=101\) one-sided thresholds \(\mathbf{1}[x>t]\) on a grid containing \(t_0\), and \(\delta=0.05\), the event
   \(R(\hat h)\le R(h_{\mathcal{H}})+\text{bound}\) holds in \(\ge 95\%\) of runs (it will hold in ~100%; report
   how loose the bound is).
2. \(\mathbb{E}\sup_{\mathcal{H}}|\hat R_n-R|\) versus \(n\in\{50,\dots,50{,}000\}\) has log–log slope
   \(-0.5\pm0.08\). With `noise=0` (realisable), the excess risk has slope \(-1\pm0.15\). Explain both.
3. Numerically minimising \(C_\eta(f)\) on a grid of \(\eta\in(0,1)\) reproduces the four closed forms
   of item 8 to \(10^{-6}\).

**Exercises.** (a) Show the memoriser's risk equals \(P(Y\ne 0)\) when \(P_X\) has a density.
(b) For one-sided thresholds \(\mathbf{1}[x>t]\) on \(\mathbb{R}\), show the growth function is \(n+1\) and hence \(d_{\mathrm{VC}}=1\).
(c) Prove the logistic loss (base 2) upper-bounds the 0–1 loss.

**Text.** Shalev-Shwartz & Ben-David, *Understanding Machine Learning* **[free]** — **Ch. 2–6**
(ERM, PAC, uniform convergence, bias–complexity, VC). Mohri, Rostamizadeh & Talwalkar,
*Foundations of ML* 2e **[free]** — **Ch. 2–3**. Murphy *PML1* **[free]** — **§4.3, §5.4**.
**Depth.** Devroye, Györfi & Lugosi, *A Probabilistic Theory of Pattern Recognition* (Springer 1996)
**[paid]** — Ch. 12 (VC theory). Bach, *Learning Theory from First Principles* (MIT Press 2024)
**[free]** author draft — Ch. 2–4.
**Course.** Prathosh, NPTEL 106108841 Week 1. Stanford CS229 notes **§8.3** (*Sample complexity
bounds*). Cornell CS 4780 lecture notes **1** (*ML setup*) and **10** (*Empirical risk
minimisation*). Berkeley CS 189 lectures **1** and **5**. NPTEL *Introduction to Statistical Pattern
Recognition* (P. S. Sastry, IISc) — the ERM/VC lectures.
**Papers.** Valiant, "A Theory of the Learnable" (CACM 1984) · Vapnik, "Principles of Risk
Minimization for Learning Theory" (NeurIPS 1991) · Bartlett, Jordan & McAuliffe, "Convexity,
Classification, and Risk Bounds" (JASA 2006) · Zhang, "Statistical Behavior and Consistency of
Classification Methods Based on Convex Risk Minimization" (Ann. Stat. 2004).
**Stop at.** Finite classes proved, VC stated. Rademacher complexity is Mohri Ch. 3 if you want it;
the course does not require it.

---

### MLF-02 — Bayes optimality and density estimation by divergence minimisation

**Week 2.** *Bayes optimality; density estimation via divergence minimisation.*
**Floor.** MLF-01; PRE-P items 2, 5, 7; T.ProbStat grad gate (5) (\(D_{\mathrm{KL}}\ge 0\)).

**Theory — Bayes optimality.**

1. **Bayes classifier (prove).** For 0–1 loss and \(K\) classes with \(\eta_k(x)=P(Y=k\mid X=x)\),
   \(R(h)=\mathbb{E}_X\big[\sum_k\mathbf{1}[h(X)\ne k]\,\eta_k(X)\big]=\mathbb{E}_X[1-\eta_{h(X)}(X)]\). The integrand is
   minimised pointwise by \(h^\star(x)=\arg\max_k\eta_k(x)\), so \(h^\star\) is optimal over *all*
   measurable classifiers and \(R^\star=\mathbb{E}[1-\max_k\eta_k(X)]\); binary: \(R^\star=\mathbb{E}\min(\eta,1-\eta)\).
2. **Excess risk identity (derive).** Binary: \(R(h)-R^\star=\mathbb{E}\big[|2\eta(X)-1|\,\mathbf{1}[h(X)\ne h^\star(X)]\big]\).
   **Plug-in corollary:** if \(\hat h=\mathbf{1}[\hat\eta>\frac12]\) then \(R(\hat h)-R^\star\le 2\,\mathbb{E}|\hat\eta(X)-\eta(X)|\)
   (on the disagreement set \(|2\eta-1|\le 2|\hat\eta-\eta|\)). *This is the licence for every generative
   classifier in MLF-03 and MLF-04*: estimate \(\eta\) well and the classifier is near-optimal.
3. **General losses.** With cost matrix \(L_{kj}\) (truth \(k\), predict \(j\)),
   \(h^\star(x)=\arg\min_j\sum_kL_{kj}\eta_k(x)\). Binary with costs \(c_{\mathrm{FP}},c_{\mathrm{FN}}\): predict 1 iff
   \(\eta(x)>c_{\mathrm{FP}}/(c_{\mathrm{FP}}+c_{\mathrm{FN}})\). **Reject option** (Chow 1970): with rejection cost
   \(c<\frac12\), reject iff \(\max_k\eta_k(x)<1-c\).
4. **Regression (prove).** For squared loss, with \(m(x)=\mathbb{E}[Y\mid X=x]\),
   \(\mathbb{E}(Y-f(X))^2=\mathbb{E}(Y-m(X))^2+\mathbb{E}(m(X)-f(X))^2\) — the cross term vanishes by the tower
   property. So \(f^\star=m\). Absolute loss gives the conditional median; pinball loss at level \(\tau\)
   the conditional \(\tau\)-quantile (the loss B9 uses).
5. **Generative route.** Bayes' rule \(\eta_k(x)=\pi_kp_k(x)/\sum_j\pi_jp_j(x)\) turns classification into
   **density estimation of the class conditionals** — the reason Weeks 2–3 are about densities.
6. **A Bayes error you can compute (derive).** Two classes, equal priors,
   \(p_k=\mathcal{N}(\mu_k,\Sigma)\). The Bayes rule is linear and
   \(R^\star=\Phi(-\Delta/2)\), \(\Delta^2=(\mu_1-\mu_0)^\top\Sigma^{-1}(\mu_1-\mu_0)\) (the Mahalanobis distance).
   This number is the ground truth for PY-2, PY-3 and PY-4.

**Theory — density estimation as divergence minimisation.**

7. **KL minimisation *is* maximum likelihood.** For a model \(\{q_\theta\}\),
   \(D_{\mathrm{KL}}(p\,\|\,q_\theta)=\mathbb{E}_p\log p-\mathbb{E}_p\log q_\theta\). The first term does not depend on
   \(\theta\), so \(\arg\min_\theta D_{\mathrm{KL}}(p\|q_\theta)=\arg\max_\theta\mathbb{E}_p\log q_\theta(X)\), the negative
   **cross-entropy**. Replacing \(p\) by the empirical measure gives
   \(\frac1n\sum_i\log q_\theta(x_i)\): the maximum-likelihood objective. Precisely: the MLE is an
   M-estimator of the **KL projection** \(\theta^\dagger=\arg\min_\theta D_{\mathrm{KL}}(p\|q_\theta)\), and under
   regularity it converges to \(\theta^\dagger\) even when \(p\notin\{q_\theta\}\) (White 1982). The model is
   then "the closest member of the family in forward KL", not "the truth".
8. **Moment matching (derive).** For an exponential family, \(\nabla_\eta\,\mathbb{E}_p\log q_\eta=\mathbb{E}_pT(X)-\nabla A(\eta)\),
   so the KL projection satisfies \(\mathbb{E}_{q_\eta}T=\mathbb{E}_pT\). A Gaussian fitted by MLE matches the mean
   and covariance of \(p\), whatever \(p\) is.
9. **Forward vs reverse KL.** \(D_{\mathrm{KL}}(p\|q)\) is infinite if \(q=0\) where \(p>0\): minimising it forces
   \(q\) to **cover** all of \(p\)'s mass (mean-seeking). \(D_{\mathrm{KL}}(q\|p)\) is infinite if \(q>0\) where
   \(p=0\): minimising it makes \(q\) **seek a mode** (zero-forcing). Worked example: fit
   \(q=\mathcal{N}(\mu,\sigma^2)\) to \(p=\frac12\mathcal{N}(-3,1)+\frac12\mathcal{N}(3,1)\). Forward KL (moment matching):
   \(\mu=0,\ \sigma^2=1+9=10\) — a Gaussian centred where \(p\) has almost no mass. Reverse KL: \(\mu\approx\pm3\),
   \(\sigma\approx1\), \(D_{\mathrm{KL}}(q\|p)\approx\log 2\). Variational inference and the VAE (MLF-12) minimise the
   *reverse* direction; MLE minimises the forward one.
10. **\(f\)-divergences.** For convex \(f\) with \(f(1)=0\), \(D_f(P\|Q)=\int q\,f(p/q)\,dx\ge f\!\big(\int p\big)=0\) by
    Jensen. KL: \(f(t)=t\log t\); reverse KL: \(-\log t\); total variation: \(\tfrac12|t-1|\); Pearson \(\chi^2\):
    \((t-1)^2\); squared Hellinger: \((\sqrt t-1)^2\); Jensen–Shannon: \(\tfrac12\big[t\log t-(1+t)\log\frac{1+t}{2}\big]\).
    *Verify the JS entry* by expanding \(\int q f(p/q)\) into \(\tfrac12D_{\mathrm{KL}}(P\|M)+\tfrac12D_{\mathrm{KL}}(Q\|M)\), \(M=\frac{P+Q}2\).
    \(0\le\mathrm{JS}\le\log 2\).
11. **Variational (dual) representation — estimation from samples.** With the convex conjugate
    \(f^*(t)=\sup_u\{tu-f(u)\}\) and \(f=f^{**}\),
    \[
    D_f(P\|Q)\;\ge\;\sup_{T\in\mathcal{T}}\ \mathbb{E}_P[T(X)]-\mathbb{E}_Q[f^*(T(X))],
    \]
    with equality when \(T^\star=f'(p/q)\in\mathcal{T}\) (Nguyen, Wainwright & Jordan 2010). For KL,
    \(f^*(t)=e^{t-1}\) (*derive*) and \(T^\star=1+\log(p/q)\). The right side needs **only samples** from
    \(P\) and \(Q\) and a trainable critic \(T\). Minimising it over a generator \(Q\) while maximising over
    \(T\) is the \(f\)-GAN (MLF-12); with the JS choice it is the original GAN.
12. **Fisher divergence and score matching (preview).** \(D_F(p\|q)=\tfrac12\mathbb{E}_p\|\nabla_x\log p-\nabla_x\log q\|^2\).
    Integration by parts (1-D, tails vanishing) removes the unknown \(\nabla\log p\):
    \(D_F=\mathbb{E}_p\big[\tfrac12(\partial_x\log q)^2+\partial_x^2\log q\big]+\text{const}\) (Hyvärinen 2005). It fits
    unnormalised models and is the objective diffusion models inherit (MLF-12 item 14).

**Derive.** (i) Item 1 and item 2's plug-in bound. (ii) Item 4. (iii) Item 6. (iv) Item 7 in both
the population and empirical form, including why the empirical "KL" must be read as
cross-entropy. (v) Both answers in item 9's example. (vi) \(f^*\) for KL, and \(T^\star\).

**Build — PY-2** (`mlf/bayes/`).
- `decision.py`: `bayes_predict(log_priors, log_class_densities)` (log domain, **M.NS**),
  `bayes_risk_mc(sampler, eta, n)`, `cost_threshold(c_fp, c_fn)`, `chow_reject(eta, c)`.
- `divergences.py`: `kl_gauss(mu1, S1, mu2, S2)` closed form
  \(\tfrac12[\mathrm{tr}(S_2^{-1}S_1)+(\mu_2-\mu_1)^\top S_2^{-1}(\mu_2-\mu_1)-d+\log\frac{|S_2|}{|S_1|}]\) via Cholesky
  log-determinants; `f_divergence(p, q, f)` for discrete distributions; `js`, `tv`, `hellinger`;
  `fit_gauss_forward_kl(samples)`; `fit_gauss_reverse_kl(log_p, score_p, init, rng)` using the
  reparameterisation \(x=\mu+\sigma z\) — gradients
  \(\partial_\mu=-\mathbb{E}_z[\partial_x\log p(x)]\), \(\partial_{\log\sigma}=-1-\mathbb{E}_z[z\,\sigma\,\partial_x\log p(x)]\) (the \(-1\) is the
  entropy term; *derive both*) — this is the VAE's trick, met a module early; `nwj_kl(xp, xq, critic)`.

**Accept.**
1. For \(\Delta\in\{1,2,3\}\), Monte Carlo risk of the Bayes rule on \(10^6\) samples is within 3 standard
   errors of \(\Phi(-\Delta/2)\).
2. For a deliberately perturbed \(\hat\eta\), the measured excess risk never exceeds \(2\mathbb{E}|\hat\eta-\eta|\).
3. Item 9: forward fit gives \(|\hat\mu|<0.05\), \(|\hat\sigma^2-10|<0.2\) on \(10^5\) samples; reverse fit from
   \(\mu_0=0.5\) converges to \(\hat\mu\in[2.9,3.1]\), \(\hat\sigma\in[0.9,1.1]\), and from \(\mu_0=-0.5\) to the other mode.
4. NWJ estimate of \(D_{\mathrm{KL}}(\mathcal{N}(0,1)\|\mathcal{N}(1,4))=\log 2+\tfrac{2}{8}-\tfrac12\approx 0.4431\) with a quadratic critic
   \(T(x)=ax^2+bx+c\) (which contains \(T^\star\) exactly) is within 5% using \(10^5\) samples per side.
5. Property test over 1,000 random discrete pairs: every \(f\)-divergence \(\ge -10^{-12}\); \(\mathrm{JS}\le\log 2\);
   \(\mathrm{TV}\le\sqrt{\tfrac12 D_{\mathrm{KL}}}\) (Pinsker).

**Exercises.** (a) Derive the Bayes rule for two Gaussians with *unequal* covariances; show the
boundary is a quadric. (b) Show \(D_{\mathrm{KL}}\) is not symmetric with a two-point example.
(c) Show \(\mathrm{JS}(P\|Q)=\log 2\) when supports are disjoint — and read MLF-12 item 11 with that in mind.

**Text.** Duda, Hart & Stork, *Pattern Classification* 2e **[paid]** — **Ch. 2** (Bayesian decision
theory). Bishop *PRML* **[free]** — **§1.5** (decision theory), **§1.6** (information theory,
relative entropy). Murphy *PML1* **[free]** — **§5.1** (Bayesian decision theory), **Ch. 6**
(information theory, §6.2 KL), **§4.2**. Hastie, Tibshirani & Friedman *ESL* **[free]** — **§2.4**.
**Depth.** Devroye, Györfi & Lugosi **Ch. 2** (the Bayes error) **[paid]**. Cover & Thomas **Ch. 2**
**[paid]**. Murphy *PML2* **[free]** — **Ch. 5** (information theory, \(f\)-divergences, IPMs) and **Ch. 24**
(energy-based models, score matching).
**Course.** Prathosh, NPTEL 106108841 Week 2; Prathosh, *Math-ML* course notes (link §10.7).
Cornell CS 4780 lecture note **5** (*Bayes classifier*). Berkeley CS 189 lecture **6** (*Decision
theory*). NPTEL Sastry, *Statistical Pattern Recognition* — the Bayes-classifier lectures.
Stanford CS236 notes (*Deep Generative Models*) — the introductory chapters on learning as divergence
minimisation **[free]**.
**Papers.** Chow, "On Optimum Recognition Error and Reject Tradeoff" (IEEE TIT 1970) · White,
"Maximum Likelihood Estimation of Misspecified Models" (Econometrica 1982) · Csiszár, "Information-type
Measures of Difference of Probability Distributions" (1967) · Ali & Silvey (JRSS-B 1966) · Nguyen,
Wainwright & Jordan, "Estimating Divergence Functionals and the Likelihood Ratio by Convex Risk
Minimization" (IEEE TIT 2010; arXiv:0809.0853) · Nowozin, Cseke & Tomioka, "\(f\)-GAN" (NeurIPS 2016;
arXiv:1606.00709) · Hyvärinen, "Estimation of Non-Normalized Statistical Models by Score Matching"
(JMLR 2005).
**Stop at.** Radon–Nikodym formalism, Rényi divergences, and integral probability metrics beyond
naming MMD and Wasserstein (used once, in MLF-12's WGAN note).

---

### MLF-03 — Maximum likelihood, MAP, and non-parametric estimation

**Week 3.** *Maximum likelihood and MAP estimates; non-parametric estimates (nearest neighbours and
Parzen window).*
**Floor.** MLF-02; PRE-LA item 5; T.ProbStat UG (scalar MLE) and grad (Cramér–Rao).

**Theory — parametric.**

1. **MLE and its properties.** \(\hat\theta=\arg\max_\theta\sum_i\log p(x_i\mid\theta)\). *Invariance:* the MLE of
   \(g(\theta)\) is \(g(\hat\theta)\). *Consistency* and *asymptotic normality*
   \(\sqrt n(\hat\theta-\theta_0)\rightsquigarrow\mathcal{N}(0,I(\theta_0)^{-1})\) under regularity (state; Cramér–Rao is
   T.ProbStat's). Under misspecification the limit is the KL projection (MLF-02 item 7) and the
   covariance becomes the sandwich \(A^{-1}BA^{-1}\).
2. **Categorical (derive with a multiplier).** Maximise \(\sum_kn_k\log\pi_k\) s.t. \(\sum_k\pi_k=1\):
   \(\hat\pi_k=n_k/n\).
3. **Multivariate Gaussian (derive).** In precision form,
   \(\ell(\mu,\Lambda)=\tfrac n2\log|\Lambda|-\tfrac12\sum_i(x_i-\mu)^\top\Lambda(x_i-\mu)+c\).
   \(\nabla_\mu\ell=\Lambda\sum_i(x_i-\mu)=0\Rightarrow\hat\mu=\bar x\).
   With \(\sum_i(x_i-\bar x)^\top\Lambda(x_i-\bar x)=n\,\mathrm{tr}(\Lambda S)\), \(S=\frac1n\sum_i(x_i-\bar x)(x_i-\bar x)^\top\):
   \(\nabla_\Lambda\ell=\tfrac n2\Lambda^{-1}-\tfrac n2S=0\Rightarrow\hat\Sigma=S\). \(\mathbb{E}\hat\Sigma=\frac{n-1}n\Sigma\) (*derive*), and
   \(\hat\Sigma\) is singular whenever \(n\le d\) — the first place the course needs a prior.
4. **MAP.** \(\hat\theta_{\mathrm{MAP}}=\arg\max_\theta\log p(\mathcal{D}\mid\theta)+\log p(\theta)\): a likelihood plus a
   penalty. MLF-05 turns this into ridge and lasso.
5. **Beta–Bernoulli (derive).** Prior \(\mathrm{Beta}(a,b)\), \(n_1\) ones in \(n\) trials. Posterior
   \(\mathrm{Beta}(a+n_1,b+n-n_1)\); MAP \(\frac{n_1+a-1}{n+a+b-2}\); posterior mean \(\frac{n_1+a}{n+a+b}\), which is also
   the posterior predictive \(P(x_{\text{new}}=1\mid\mathcal{D})\). Laplace's rule \(\frac{n_1+1}{n+2}\) is the posterior
   **mean** under the uniform prior \(a=b=1\) and the **MAP** under \(a=b=2\) — say which, precisely.
   Dirichlet–categorical is the same computation.
6. **Gaussian mean, known variance (derive).** Prior \(\mathcal{N}(\mu_0,\tau^2)\): posterior precision
   \(\tau^{-2}+n\sigma^{-2}\); posterior mean = precision-weighted average of \(\mu_0\) and \(\bar x\) — shrinkage
   toward the prior, vanishing as \(n\to\infty\).
7. **Covariance MAP.** With known mean and an inverse-Wishart prior \(\mathcal{IW}(\Psi,\nu)\), the posterior is
   \(\mathcal{IW}(\Psi+nS,\nu+n)\) and its mode is \(\frac{\Psi+nS}{\nu+n+d+1}\): always invertible when \(\Psi\succ0\).
8. **What MAP is not.** MAP is not invariant to reparameterisation (the density picks up a Jacobian;
   exhibit it for \(\mathrm{Beta}(2,2)\) on \(p\) vs on \(\mathrm{logit}\,p\)). It is not the Bayes estimator under
   squared loss (that is the posterior mean) and it discards posterior uncertainty.

**Theory — non-parametric.**

9. **The master identity.** For a small region \(\mathcal{R}\ni x\) of volume \(V\),
   \(P_{\mathcal{R}}=\int_{\mathcal{R}}p\approx p(x)V\) and the count \(k\sim\mathrm{Bin}(n,P_{\mathcal{R}})\), so
   \(\hat p(x)=\frac{k}{nV}\). Fix \(V\), count \(k\): **Parzen**. Fix \(k\), grow \(V\): **\(k\)-NN**. Consistency needs
   \(V_n\to0\), \(k_n\to\infty\), \(k_n/n\to0\) (Duda–Hart–Stork §4.2).
10. **Parzen window / kernel density estimator.** \(\hat p_h(x)=\frac1{nh^d}\sum_iK\!\big(\frac{x-x_i}h\big)\) with
    \(K\ge0\), \(\int K=1\) — so \(\hat p_h\) is itself a density. The hypercube window recovers item 9 literally;
    the Gaussian kernel smooths it.
11. **KDE bias and variance in 1-D (derive).** With symmetric \(K\), \(\mu_2(K)=\int u^2K\), \(R(g)=\int g^2\):
    \(\mathbb{E}\hat p_h(x)=\int K(u)p(x-hu)\,du=p(x)+\tfrac{h^2}2\mu_2(K)p''(x)+o(h^2)\) (Taylor), and
    \(\mathrm{Var}\,\hat p_h(x)=\frac{p(x)R(K)}{nh}+o\big(\frac1{nh}\big)\). Integrating,
    \[
    \mathrm{AMISE}(h)=\frac{h^4}4\mu_2(K)^2R(p'')+\frac{R(K)}{nh},\qquad h^\star=\Big[\frac{R(K)}{\mu_2(K)^2R(p'')\,n}\Big]^{1/5}\propto n^{-1/5},
    \]
    and \(\mathrm{AMISE}(h^\star)\propto n^{-4/5}\) — slower than the parametric \(n^{-1}\). For a Gaussian kernel and
    Gaussian \(p\) with s.d. \(\sigma\): \(h^\star=(4/3n)^{1/5}\sigma\approx1.06\,\sigma n^{-1/5}\) (Silverman's rule; *derive* it
    from \(R(K)=\frac1{2\sqrt\pi}\), \(R(p'')=\frac{3}{8\sqrt\pi\sigma^5}\)). In \(d\) dimensions the rate is
    \(n^{-4/(4+d)}\): the curse of dimensionality, as a number.
12. **Bandwidth by cross-validation.** Leave-one-out likelihood \(\max_h\sum_i\log\hat p_{h,-i}(x_i)\).
    Never evaluate at the training point itself — \(h\to0\) then drives the likelihood to \(+\infty\).
13. **Parzen classifier and Nadaraya–Watson.** Class-conditional KDEs plus priors give a plug-in Bayes
    classifier (MLF-02 item 2). For regression,
    \(\hat m(x)=\frac{\sum_iK_h(x-x_i)y_i}{\sum_iK_h(x-x_i)}\) — a softmax-like weighted average of the \(y_i\). Keep this
    formula: MLF-10 item 1 shows attention is exactly this with learned kernels.
14. **\(k\)-NN density.** \(\hat p(x)=\frac{k}{n\,V_d\,r_k(x)^d}\), \(V_d=\frac{\pi^{d/2}}{\Gamma(d/2+1)}\). It is **not** a density:
    tails decay like \(\|x\|^{-d}\), so \(\int\hat p=\infty\) (*show it* in 1-D).
15. **\(k\)-NN classifier as Bayes plug-in (derive).** With \(k_c\) of the \(k\) neighbours in class \(c\):
    \(\hat p(x\mid c)=\frac{k_c}{n_cV}\), \(\hat\pi_c=\frac{n_c}n\), \(\hat p(x)=\frac k{nV}\) ⇒ \(\hat P(c\mid x)=\frac{k_c}k\). Majority vote *is*
    the plug-in rule.
16. **Cover–Hart (prove the binary case).** As \(n\to\infty\), the 1-NN's neighbour converges to \(x\) and its
    label is drawn independently from \(\eta(x)\), so the asymptotic conditional error is
    \(2\eta(1-\eta)=2r(1-r)\), \(r=\min(\eta,1-\eta)\). Then \(R_{\mathrm{NN}}=\mathbb{E}[2r(1-r)]=2R^\star-2\mathbb{E}r^2\le2R^\star(1-R^\star)\)
    by \(\mathbb{E}r^2\ge(\mathbb{E}r)^2\); and \(2r(1-r)\ge r\) since \(r\le\frac12\). Hence
    \(R^\star\le R_{\mathrm{NN}}\le 2R^\star(1-R^\star)\). With \(k\to\infty,\ k/n\to0\), \(k\)-NN is universally consistent
    (Stone 1977; statement).
17. **The curse, geometrically.** In \([0,1]^d\) a sub-cube holding fraction \(r\) of uniform data has edge
    \(r^{1/d}\): at \(d=10,\ r=0.01\), edge \(0.63\) — "local" neighbourhoods are not local (*ESL* §2.5). Distance
    ratios concentrate, \(\frac{\max-\min}{\min}\to0\) (Beyer et al. 1999).
18. **Computation.** Brute force \(O(nd)\) per query with the PRE-NP distance identity and
    `np.argpartition` (\(O(n)\), not a sort); \(k\)-d trees help only at low \(d\) (B4 builds one).

**Derive.** (i) Items 2, 3 (both parameters) and the bias of \(\hat\Sigma\). (ii) Item 5's four
quantities. (iii) Item 11 end to end, including Silverman's constant. (iv) Item 15. (v) Item 16.

**Build — PY-3** (`mlf/density/`).
- `parametric.py`: `mle_categorical`, `mle_gaussian(X)` (returns \(\hat\mu\), \(\hat\Sigma\), and the unbiased
  variant), `beta_bernoulli_posterior(n1, n, a, b)`, `gauss_mean_posterior`, `iw_map_cov(X, Psi, nu)`,
  `gauss_logpdf(X, mu, Sigma)` via Cholesky (never `inv`, never `det`: use \(2\sum\log L_{ii}\)).
- `kde.py`: `KDE(kernel, h).fit(X).logpdf(Q)` with `logsumexp` over training points;
  `silverman(X)`; `loo_loglik(X, hs)` vectorised with the diagonal masked to \(-\infty\) in log space.
- `knn.py`: `knn_density(X, Q, k)` (use `gammaln` for \(V_d\) in log space), `KNNClassifier(k)` with
  `argpartition`, tie-breaking stated and tested, `ParzenClassifier(h)`, `nadaraya_watson(X, y, Q, h)`.

**Accept.**
1. Over \(10^4\) datasets with \(n=5,d=2\), the mean of \(\hat\Sigma_{\mathrm{MLE}}\) equals \(\frac45\Sigma\) within Monte Carlo
   error; the unbiased version equals \(\Sigma\).
2. Beta–Bernoulli posterior-predictive probabilities are calibrated: among simulated predictions in
   the bin \([0.6,0.7)\) the empirical frequency is in \([0.6,0.7)\) (with \(\theta\) drawn from the prior).
3. KDE with \(h=(4/3n)^{1/5}\) on \(\mathcal{N}(0,1)\): MISE against the true density versus
   \(n\in\{10^2,\dots,10^5\}\) has log–log slope \(-0.80\pm0.05\). With \(h\) frozen at its \(n=100\) value, the slope
   flattens toward 0 — the bias floor, observed.
4. The MISE-minimising \(h\) (averaged over 50 replications, grid search) is within 15% of \((4/3n)^{1/5}\) at
   \(n=2000\).
5. On a synthetic problem with known \(R^\star=0.1\) and \(n=10^5\), 1-NN test error lies in
   \([R^\star,\,2R^\star(1-R^\star)]=[0.10,0.18]\) (allow 3 standard errors), and \(k\)-NN with \(k\approx\sqrt n\) is within
   0.01 of \(R^\star\).
6. \(\int_{-B}^{B}\hat p_{k\text{-NN}}\) grows like \(\log B\) as \(B\) doubles — item 14, measured.

**Exercises.** (a) Show that a histogram estimator has MISE rate \(n^{-2/3}\) and explain why KDE
beats it. (b) Derive the posterior of a Gaussian mean with unknown variance under a
Normal–Inverse-Gamma prior. (c) Prove the Parzen estimate with a Gaussian kernel is infinitely
differentiable even though the data are not.

**Text.** Bishop *PRML* **[free]** — **§2.1–2.2** (binary/multinomial, Beta/Dirichlet), **§2.3.4–2.3.6**
(Gaussian MLE, sequential and Bayesian inference), **§2.5** (non-parametric: §2.5.1 KDE, §2.5.2 nearest
neighbours). Duda, Hart & Stork **[paid]** — **Ch. 3** (§3.2 MLE, §3.3–3.5 Bayesian estimation), **Ch. 4**
(§4.2 density estimation, §4.3 Parzen windows, §4.5 \(k_n\)-NN estimation, §4.6 the NN rule). Murphy *PML1*
**[free]** — **§4.2, §4.5–4.6, §16.1, §16.3**. *ESL* **[free]** — **§2.5, §6.6, §13.3**.
**Depth.** Wasserman, *All of Nonparametric Statistics* (Springer 2006) **[paid]** — **Ch. 6** (density
estimation). Tsybakov, *Introduction to Nonparametric Estimation* (Springer 2009) **[paid]** — **Ch. 1**.
Devroye, Györfi & Lugosi **[paid]** — **Ch. 5, 10, 11** (NN rules, kernel rules, \(k\)-NN consistency).
Wasserman, CMU 36-708 lecture notes *Density Estimation* **[free]**.
**Course.** Prathosh, NPTEL 106108841 Week 3. Cornell CS 4780 lecture notes **2** (*k-NN / curse of
dimensionality*), **4** (*Estimating probabilities: MLE and MAP*). CS229 notes **§9.4** (*Bayesian
statistics and regularisation*). Berkeley CS 189 lectures **7**, **24**, **25**. NPTEL Sastry, *Statistical
Pattern Recognition* — parametric and non-parametric density estimation lectures.
**Papers.** Fix & Hodges (USAF School of Aviation Medicine report, 1951) · Rosenblatt, "Remarks on Some
Nonparametric Estimates of a Density Function" (Ann. Math. Stat. 1956) · Parzen, "On Estimation of a
Probability Density Function and Mode" (Ann. Math. Stat. 1962) · Nadaraya (1964) and Watson (1964) ·
Cover & Hart, "Nearest Neighbor Pattern Classification" (IEEE TIT 1967) · Stone, "Consistent
Nonparametric Regression" (Ann. Stat. 1977) · Silverman, *Density Estimation for Statistics and Data
Analysis* (Chapman & Hall 1986) · Beyer et al., "When Is 'Nearest Neighbor' Meaningful?" (ICDT 1999) ·
Ledoit & Wolf, "A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices" (JMVA 2004).
**Stop at.** Minimax lower bounds, adaptive bandwidths, and metric learning (Murphy *PML1* §16.2).

---

### MLF-04 — Linear models: least squares, Fisher discriminant, logistic regression

**Week 4.** *Linear regression, least squares, Fisher discriminant, logistic regression.*
**Floor.** MLF-02 items 5–6; MLF-03 item 3; PRE-LA items 1–5; M.ML log-loss gradient; M.NS.

**Theory — regression.**

1. **Least squares.** Features \(\phi(x)\in\mathbb{R}^d\) (bias included), design \(X\in\mathbb{R}^{n\times d}\).
   \(\min_w\|y-Xw\|^2\) ⇒ **normal equations** \(X^\top Xw=X^\top y\) (*derive* with PRE-LA item 5).
2. **Geometry.** \(\hat y=Hy\), \(H=X(X^\top X)^{-1}X^\top\) the orthogonal projector onto \(\mathrm{col}(X)\);
   residual \(r=(I-H)y\perp\mathrm{col}(X)\), i.e. \(X^\top r=0\). \(\mathrm{tr}H=d\) (degrees of freedom). Rank-deficient
   \(X\): infinitely many minimisers; \(X^+y\) is the one of minimum norm.
3. **Probabilistic interpretation (derive).** \(y=Xw+\varepsilon\), \(\varepsilon\sim\mathcal{N}(0,\sigma^2I)\) ⇒
   \(\log p(y\mid X,w)=-\frac n2\log(2\pi\sigma^2)-\frac{1}{2\sigma^2}\|y-Xw\|^2\): the MLE of \(w\) **is** least squares, and
   \(\hat\sigma^2_{\mathrm{ML}}=\mathrm{RSS}/n\) (biased; \(\mathrm{RSS}/(n-d)\) is unbiased). Fixed design:
   \(\hat w\sim\mathcal{N}(w,\sigma^2(X^\top X)^{-1})\). Laplace noise instead gives least **absolute** deviations — the
   noise model *is* the loss.
4. **Gauss–Markov (prove).** Any linear unbiased estimator \(Cy\) has \(CX=I\); write
   \(C=(X^\top X)^{-1}X^\top+D\) with \(DX=0\); then \(\mathrm{Cov}(Cy)=\sigma^2(X^\top X)^{-1}+\sigma^2DD^\top\succeq\sigma^2(X^\top X)^{-1}\).
   OLS is BLUE. MLF-05 shows why "unbiased" is the wrong thing to want.
5. **Computing it.** \(\kappa(X^\top X)=\kappa(X)^2\): forming the normal equations squares the condition
   number (**M.NS**). Use QR (\(X=QR\), solve \(Rw=Q^\top y\)) — \(O(nd^2)\), backward stable — or the SVD when
   rank-deficient. Gradient descent and SGD (M.ML, B2) when \(n\) or \(d\) is large.

**Theory — generative linear classifiers.**

6. **Gaussian discriminant analysis (derive).** Class conditionals \(\mathcal{N}(\mu_k,\Sigma_k)\), priors \(\pi_k\).
   Log-posterior up to a constant:
   \(\delta_k(x)=\log\pi_k-\tfrac12\log|\Sigma_k|-\tfrac12(x-\mu_k)^\top\Sigma_k^{-1}(x-\mu_k)\) — **QDA**. If \(\Sigma_k=\Sigma\) the
   quadratic term cancels between classes: \(\delta_k(x)=x^\top\Sigma^{-1}\mu_k-\tfrac12\mu_k^\top\Sigma^{-1}\mu_k+\log\pi_k\) — **LDA**,
   a linear rule. For two classes the log-odds is \(w^\top x+b\) with \(w=\Sigma^{-1}(\mu_1-\mu_0)\), so the posterior
   is **exactly a logistic sigmoid**. The converse is false: logistic posteriors arise from many
   non-Gaussian class conditionals (any exponential family with shared dispersion). MLEs: class
   frequencies, class means, pooled covariance.

**Theory — Fisher's linear discriminant.**

7. **Two classes (derive).** Project \(z=w^\top x\). Maximise between-class separation relative to
   within-class spread:
   \[
   J(w)=\frac{w^\top S_Bw}{w^\top S_Ww},\quad S_B=(m_1-m_0)(m_1-m_0)^\top,\quad S_W=\sum_k\sum_{i\in\mathcal{C}_k}(x_i-m_k)(x_i-m_k)^\top.
   \]
   Setting \(\nabla J=0\): \((w^\top S_Bw)S_Ww=(w^\top S_Ww)S_Bw\). Since \(S_Bw\propto(m_1-m_0)\) and \(J\) is scale-invariant,
   \(w\propto S_W^{-1}(m_1-m_0)\). **No Gaussian assumption was made** — yet this is LDA's direction, because
   \(S_W\) is \(n\) times the pooled covariance. Fisher gives a *direction*, not a threshold; the Gaussian
   model (item 6) or a 1-D search supplies the threshold. Least squares with targets \(n/n_1\) and
   \(-n/n_0\) also recovers this direction (Bishop *PRML* §4.1.5).
8. **\(K\) classes (derive).** \(S_B=\sum_kn_k(m_k-m)(m_k-m)^\top\). Maximise
   \(\mathrm{tr}\big((W^\top S_WW)^{-1}W^\top S_BW\big)\): the columns of \(W\) are the top generalised eigenvectors of
   \(S_Bw=\lambda S_Ww\). \(\mathrm{rank}\,S_B\le K-1\), so at most \(K-1\) directions carry signal. Solve by whitening:
   \(S_W=LL^\top\), eigendecompose the symmetric \(L^{-1}S_BL^{-\top}\), map back \(w=L^{-\top}v\). If \(n<d\), \(S_W\) is
   singular: use \(S_W+\epsilon I\) (the MAP move of MLF-03 item 7).

**Theory — logistic regression.**

9. **Model and convexity (derive).** \(p_i=\sigma(w^\top x_i)\); NLL \(J(w)=-\sum_i[y_i\log p_i+(1-y_i)\log(1-p_i)]\).
   Gradient \(X^\top(p-y)\) (the per-example derivation is M.ML's). Hessian \(H=X^\top SX\),
   \(S=\mathrm{diag}(p_i(1-p_i))\): \(v^\top Hv=\sum_ip_i(1-p_i)(x_i^\top v)^2\ge0\), so \(J\) is convex, strictly if \(X\) has full
   column rank.
10. **Newton = IRLS (derive).** \(w^+=w-H^{-1}X^\top(p-y)=(X^\top SX)^{-1}X^\top Sz\) with working response
    \(z=Xw-S^{-1}(p-y)\): each Newton step is a **weighted least-squares** solve. Quadratic local
    convergence; \(O(nd^2+d^3)\) per step. Guard with step halving when \(J\) increases.
11. **Separable data.** If a \(w\) separates the classes, \(J(tw)\to0\) as \(t\to\infty\): the MLE does not exist
    and IRLS's weights \(S\to0\) make \(H\) singular. Fixes: an L2 penalty (= Gaussian prior, MLF-05) or early
    stopping. B2 observed the divergence; here you have the reason.
12. **Softmax regression.** \(p_{ik}=\mathrm{softmax}(Wx_i)_k\); \(\nabla_WJ=(P-Y)^\top X\) with one-hot \(Y\); computed with
    `log_softmax` (**M.NS**). Parameters are identified only up to adding a common vector to every row —
    fix one row or regularise.
13. **Generative vs discriminative.** If the GDA model is right, LDA is asymptotically more efficient;
    if it is wrong, logistic regression is more robust. Ng & Jordan (2001): naive Bayes approaches its
    (higher) asymptotic error with \(O(\log d)\) samples, logistic regression needs \(O(d)\) — generative
    models win early, discriminative models win late.

**Derive.** (i) Items 1–4. (ii) LDA's linear discriminant and the sigmoid posterior in item 6.
(iii) Item 7 from \(\nabla J=0\), and item 8's whitening reduction. (iv) Items 9–10. (v) The softmax
gradient.

**Build — PY-4** (`mlf/linear/`).
- `ols.py`: `fit_normal_eq` (Cholesky), `fit_qr`, `fit_svd` (min-norm, with a relative rank tolerance),
  `hat_diagonal(X)` via \(Q\) (\(H_{ii}=\|Q_{i\cdot}\|^2\)), `lms_sgd`.
- `gda.py`: `LDA`, `QDA` with `predict_log_proba` in log space.
- `fisher.py`: `fisher_2class(X, y)`, `fisher_multiclass(X, y, n_components, eps)` via Cholesky whitening.
- `logistic.py`: `LogisticGD`, `LogisticIRLS` (step halving, stops on relative NLL change and gradient
  norm), `SoftmaxRegression` (GD, L2 optional).

**Accept.**
1. \(\|X^\top r\|/(\|X\|\|r\|)<10^{-12}\) for QR. On a consistent system (\(y=Xw\) exactly) with \(\kappa(X)=10^{7}\), the
   normal-equation solution error exceeds the QR error by a factor within two orders of magnitude of
   \(\kappa\) (\(\kappa^2\epsilon\) vs \(\kappa\epsilon\)) — you predicted the ratio first.
2. Fixed design, 2,000 replications: the empirical covariance of \(\hat w\) matches \(\sigma^2(X^\top X)^{-1}\) to 5%
   relative Frobenius error.
3. `fisher_2class` direction and LDA's \(\Sigma^{-1}(\mu_1-\mu_0)\) have \(|\cos|>1-10^{-10}\). Multiclass: generalised
   eigen-residual \(\|S_Bw-\lambda S_Ww\|<10^{-9}\), and eigenvalues beyond the \((K-1)\)-th are \(<10^{-10}\).
4. IRLS: once \(\|\nabla\|<10^{-2}\), successive gradient norms satisfy
   \(\log\|\nabla_{k+1}\|/\log\|\nabla_k\|\ge1.8\) until machine precision (quadratic convergence), and the IRLS and GD
   solutions agree to \(10^{-6}\).
5. Data from a shared-covariance GDA with \(\Delta=2\): both LDA and logistic regression approach
   \(\Phi(-1)\approx0.1587\) as \(n\) grows; at \(n=20\) LDA's mean test error is lower. Replace the class
   conditionals by multivariate-\(t_3\) with the same means: logistic regression now wins at large \(n\).
6. Softmax regression passes the gradient check; adding a constant vector to every row of \(W\) leaves
   predictions unchanged to \(10^{-12}\).

**Exercises.** (a) Show OLS with an intercept makes residuals sum to zero. (b) Show that LDA and
Fisher disagree on the *threshold* when priors are unequal, and compute both. (c) Derive the
Hessian of softmax regression and show it is PSD but singular.

**Text.** Bishop *PRML* **[free]** — **§3.1** (ML and least squares, geometry), **§4.1.4–4.1.6** (Fisher,
relation to least squares, multiple classes), **§4.2** (probabilistic generative models), **§4.3.2–4.3.4**
(logistic regression, IRLS, multiclass). *ESL* **[free]** — **§3.2** (incl. Gauss–Markov), **§4.3** (LDA,
reduced-rank LDA = Fisher), **§4.4** (logistic regression by IRLS). Murphy *PML1* **[free]** — **§9.2,
§10.2–10.3, §11.2**. Deisenroth, Faisal & Ong, *MML* **[free]** — **Ch. 9**.
**Depth.** Trefethen & Bau, *Numerical Linear Algebra* **[paid]** — Lectures on QR and least squares
and their conditioning. Duda, Hart & Stork **[paid]** — **§3.8** (Fisher linear discriminant, multiple
discriminant analysis), **Ch. 5**.
**Course.** Prathosh, NPTEL 106108841 Week 4. CS229 notes **§1.2–1.3** (normal equations,
probabilistic interpretation), **§2.1, §2.3, §2.4** (logistic, multiclass, Newton), **§4.1** (GDA, with
§4.1.3 *GDA and logistic regression*). Cornell CS 4780 lecture notes **6** and **8**. Berkeley CS 189
lectures **7, 9, 10, 11**. NPTEL *Introduction to Machine Learning* (Sudeshna Sarkar, IIT Kharagpur) —
linear and logistic regression weeks.
**Papers.** Fisher, "The Use of Multiple Measurements in Taxonomic Problems" (Annals of Eugenics
1936) · Rao, "The Utilization of Multiple Measurements in Problems of Biological Classification"
(JRSS-B 1948) · Cox, "The Regression Analysis of Binary Sequences" (JRSS-B 1958) · Nelder &
Wedderburn, "Generalized Linear Models" (JRSS-A 1972) · Ng & Jordan, "On Discriminative vs.
Generative Classifiers" (NeurIPS 2001).
**Stop at.** General GLM theory beyond logistic and softmax (Murphy *PML1* Ch. 12), robust regression.

---
### MLF-05 — Regularisation and generalisation

**Week 5.** *Bias–variance decomposition; ridge regression; lasso; probabilistic interpretation of
regularisation.*
**Floor.** MLF-03 items 4–6; MLF-04 items 1–5; PRE-P items 3–4; PRE-CALC item 4.

**Theory.**

1. **Bias–variance decomposition (derive).** \(y=f(x)+\varepsilon\), \(\mathbb{E}\varepsilon=0\), \(\mathrm{Var}\,\varepsilon=\sigma^2\). A
   training set \(\mathcal{D}\) is random, so the fitted \(\hat f_{\mathcal{D}}\) is random. At a test point \(x_0\) with fresh noise
   \(\varepsilon_0\) independent of \(\mathcal{D}\), writing \(\bar f(x_0)=\mathbb{E}_{\mathcal{D}}\hat f_{\mathcal{D}}(x_0)\):
   \[
   \mathbb{E}_{\mathcal{D},\varepsilon_0}\big(y_0-\hat f_{\mathcal{D}}(x_0)\big)^2=\underbrace{\sigma^2}_{\text{irreducible}}+\underbrace{\big(f(x_0)-\bar f(x_0)\big)^2}_{\text{bias}^2}+\underbrace{\mathbb{E}_{\mathcal{D}}\big(\hat f_{\mathcal{D}}(x_0)-\bar f(x_0)\big)^2}_{\text{variance}}.
   \]
   Add and subtract \(f(x_0)\) and \(\bar f(x_0)\); both cross terms vanish — one because \(\varepsilon_0\perp\mathcal{D}\) and
   \(\mathbb{E}\varepsilon_0=0\), one because \(\mathbb{E}_{\mathcal{D}}[\hat f_{\mathcal{D}}-\bar f]=0\). *Write every step.* The decomposition is
   **specific to squared loss**: 0–1 loss has no additive analogue (Domingos 2000), which is why
   bagging's effect on classifiers (MLF-11) needs its own argument.
2. **\(k\)-NN regression, closed form (derive).** Fixed design, neighbours \(x_{(1)},\dots,x_{(k)}\) of \(x_0\):
   \(\mathrm{bias}=f(x_0)-\frac1k\sum_\ell f(x_{(\ell)})\), \(\mathrm{variance}=\sigma^2/k\). \(k\) is the dial.
3. **OLS, in-sample (derive).** \(\mathrm{Var}(x_i^\top\hat w)=\sigma^2H_{ii}\), so the average variance over the
   training inputs is \(\sigma^2\,\mathrm{tr}H/n=\sigma^2d/n\): each parameter costs \(\sigma^2/n\).
4. **Ridge (derive).** \(\hat w_\lambda=\arg\min\|y-Xw\|^2+\lambda\|w\|^2=(X^\top X+\lambda I)^{-1}X^\top y\) — always invertible
   for \(\lambda>0\). With \(X=UDV^\top\):
   \[
   X\hat w_\lambda=\sum_ju_j\,\frac{d_j^2}{d_j^2+\lambda}\,u_j^\top y,\qquad \mathrm{df}(\lambda)=\mathrm{tr}H_\lambda=\sum_j\frac{d_j^2}{d_j^2+\lambda}.
   \]
   Ridge shrinks most along directions of **least** sample variance. Moments:
   \(\mathbb{E}\hat w_\lambda=(X^\top X+\lambda I)^{-1}X^\top Xw\) (biased),
   \(\mathrm{Cov}\,\hat w_\lambda=\sigma^2(X^\top X+\lambda I)^{-1}X^\top X(X^\top X+\lambda I)^{-1}\).
   Intercept is not penalised; standardise columns first.
5. **Ridge beats OLS for some \(\lambda>0\) (prove).** Rotate to \(\alpha=V^\top w\). Estimation MSE is
   \(\sum_j\frac{\sigma^2d_j^2+\lambda^2\alpha_j^2}{(d_j^2+\lambda)^2}\). Its derivative at \(\lambda=0\) is \(-2\sigma^2\sum_jd_j^{-4}<0\), so a small
   \(\lambda>0\) strictly improves on OLS (Hoerl & Kennard 1970). Per coordinate the minimiser is
   \(\lambda_j^\star=\sigma^2/\alpha_j^2\) — hold that number; item 8 gives it a meaning.
6. **Lasso (derive).** \(\min_w\tfrac12\|y-Xw\|^2+\lambda\|w\|_1\). Subgradient optimality (PRE-CALC item 4):
   \(X_j^\top(y-Xw)=\lambda\,\mathrm{sign}(w_j)\) if \(w_j\ne0\), \(|X_j^\top(y-Xw)|\le\lambda\) if \(w_j=0\). Consequences you derive:
   (i) \(\lambda\ge\lambda_{\max}=\|X^\top y\|_\infty\Rightarrow\hat w=0\). (ii) Orthonormal design (\(X^\top X=I\)), with
   \(z=X^\top y\): lasso \(\hat w_j=S_\lambda(z_j)=\mathrm{sign}(z_j)(|z_j|-\lambda)_+\) (soft threshold); ridge
   \(z_j/(1+\lambda)\) (proportional shrink); best-subset hard threshold. (iii) The \(\ell_1\) ball's corners
   make exact zeros likely. (iv) When \(d>n\) the solution may be non-unique, and some solution has at
   most \(n\) non-zeros.
7. **Algorithms for the lasso (derive).** *Coordinate descent:* partial residual \(r^{(j)}=y-\sum_{k\ne j}X_kw_k\),
   update \(w_j\leftarrow S_\lambda(X_j^\top r^{(j)})/\|X_j\|^2\); converges because the non-smooth part is separable
   (Tseng 2001). Solve on a log-spaced \(\lambda\) path from \(\lambda_{\max}\) downward with warm starts (glmnet).
   *Proximal gradient (ISTA):* \(w\leftarrow S_{\eta\lambda}\big(w-\eta X^\top(Xw-y)\big)\), \(\eta\le1/\sigma_{\max}(X)^2\), rate \(O(1/k)\);
   **FISTA** adds momentum for \(O(1/k^2)\). Elastic net \(\lambda_1\|w\|_1+\tfrac{\lambda_2}2\|w\|^2\) groups correlated features.
8. **Regularisation as a prior (derive).** Likelihood \(y\mid X,w\sim\mathcal{N}(Xw,\sigma^2I)\).
   - Gaussian prior \(w\sim\mathcal{N}(0,\tau^2I)\): \(-\log p(w\mid\mathcal{D})=\frac{1}{2\sigma^2}\|y-Xw\|^2+\frac{1}{2\tau^2}\|w\|^2+c\), so
     **MAP = ridge with \(\lambda=\sigma^2/\tau^2\)**. Now reread item 5: the MSE-optimal per-coordinate
     penalty \(\sigma^2/\alpha_j^2\) is exactly this \(\lambda\) when the prior variance \(\tau^2\) matches the true
     coefficients' size.
   - Laplace prior \(p(w_j)=\frac1{2b}e^{-|w_j|/b}\): MAP = **lasso with \(\lambda=\sigma^2/b\)**.
   - General rule: **penalty = −log prior**; the \(\ell_0\) penalty corresponds to a spike-and-slab prior.
   - Warning: lasso's sparsity is a property of the **mode**. The Laplace-prior posterior mean is never
     exactly sparse (Park & Casella 2008). Sparsity is a decision, not a posterior belief.
9. **Bayesian linear regression (derive with PRE-P item 4).** Posterior
   \(\mathcal{N}(m_N,S_N)\), \(S_N^{-1}=\tau^{-2}I+\sigma^{-2}X^\top X\), \(m_N=\sigma^{-2}S_NX^\top y\) — and \(m_N\) **equals the ridge
   solution**. Predictive \(y_\star\mid x_\star\sim\mathcal{N}(m_N^\top x_\star,\ \sigma^2+x_\star^\top S_Nx_\star)\): noise plus parameter
   uncertainty, the latter shrinking as data accumulate. Hyperparameters by maximising the marginal
   likelihood (empirical Bayes, Bishop *PRML* §3.5).
10. **Implicit regularisation: early stopping (derive).** GD on \(\tfrac12\|y-Xw\|^2\) from \(w_0=0\) with step \(\eta\)
    gives, after \(t\) steps, the spectral filter \(1-(1-\eta d_j^2)^t\) on each singular direction, versus ridge's
    \(\frac{d_j^2}{d_j^2+\lambda}\). Both are \(\approx1\) for large \(d_j^2\) and \(\approx0\) for small; \(\lambda\approx1/(\eta t)\) matches them.
    Training with input noise is Tikhonov regularisation to first order (Bishop 1995).
11. **Model selection (derive the shortcut).** \(K\)-fold CV; for any linear smoother \(\hat y=Hy\) fitted by
    least squares, **LOOCV** \(=\frac1n\sum_i\big(\frac{y_i-\hat y_i}{1-H_{ii}}\big)^2\) — no refits (Sherman–Morrison). GCV replaces
    \(H_{ii}\) by \(\mathrm{tr}H/n\). Nested CV when the CV score is also used to report performance.
12. **Beyond the U-curve.** Past the interpolation threshold \(d\approx n\), minimum-norm least squares shows
    test error falling again — **double descent** (Belkin et al. 2019; CS229 §8.2). The classical picture
    is correct for fixed-capacity estimators with explicit regularisation, not a universal law.

**Derive.** (i) Item 1, every line. (ii) Item 4's SVD form and \(\mathrm{df}(\lambda)\). (iii) Item 5.
(iv) Item 6 (i)–(ii). (v) Item 7's coordinate update. (vi) Item 8, both priors, with the scaling of
\(\lambda\). (vii) Item 9 and the claim \(m_N=\hat w_\lambda\). (viii) Item 11.

**Build — PY-5** (`mlf/regularize/`).
- `ridge.py`: `ridge_svd_path(X, y, lambdas)` (one SVD, whole path), `ridge_df(d, lam)`,
  `ridge_dual(X, y, lam)` via \((XX^\top+\lambda I)^{-1}\) for \(d>n\).
- `lasso.py`: `lasso_cd(X, y, lam, w0, tol)` with residual updates and a KKT-based stopping rule;
  `lasso_path(X, y, n_lambdas, eps)`; `ista`, `fista`; `soft_threshold`; `elastic_net_cd`.
- `bayes_linreg.py`: `posterior(X, y, sigma2, tau2)`, `predictive(x)`, `log_evidence(...)`.
- `biasvar.py`: `decompose(fit, f, x_test, sigma, n, reps, rng)` — draws `reps` training sets, returns
  bias², variance, noise and the directly measured test MSE.
- `cv.py`: `kfold`, `loocv_linear_smoother(H, y)`, `gcv`, `one_se_rule`.

**Accept.**
1. For \(k\)-NN regression and polynomial ridge, bias² + variance + \(\sigma^2\) equals directly measured test
   MSE within 2 Monte Carlo standard errors; measured \(k\)-NN variance is within 5% of \(\sigma^2/k\).
2. `ridge_df` equals \(\mathrm{tr}H_\lambda\) computed from the hat matrix to \(10^{-10}\); `ridge_dual` equals the primal to
   \(10^{-8}\).
3. On a 1-D orthonormal problem with known \(\alpha,\sigma\), the Monte-Carlo MSE curve over \(\lambda\) is minimised
   within one grid step of \(\sigma^2/\alpha^2\).
4. Minimising the negative log posterior by gradient descent reproduces ridge with \(\lambda=\sigma^2/\tau^2\) to
   \(10^{-8}\), and `posterior` mean equals it too.
5. Lasso KKT at the returned solution: \(\max_{j:w_j=0}|X_j^\top r|\le\lambda(1+10^{-6})\) and
   \(\max_{j:w_j\ne0}|X_j^\top r-\lambda\,\mathrm{sign}(w_j)|<10^{-6}\). \(\lambda=\lambda_{\max}\) gives exactly zero. CD and FISTA agree to
   \(10^{-6}\); on an ill-conditioned \(d>n\) design, FISTA's objective gap at iteration 200 is at least 10× smaller
   than ISTA's, and you plot both against the \(O(1/k)\) and \(O(1/k^2)\) reference lines. On an orthonormal design, one CD sweep equals the soft-threshold closed form.
6. LOOCV shortcut equals brute-force refitting to \(10^{-8}\).
7. \(n=100\), \(d=200\), 5 true non-zeros, SNR 10: some \(\lambda\) on your path recovers the exact support;
   report the \(\lambda\) interval where it does.

**Exercises.** (a) Show ridge on duplicated features splits the weight equally, while lasso picks
arbitrarily — and what elastic net does. (b) Derive the bias–variance decomposition of the ridge
estimator of \(w\) (not of predictions). (c) Show the constrained form \(\|w\|^2\le t\) and the penalised
form are equivalent, and relate \(t\) to \(\lambda\) through the KKT conditions of MLF-06.

**Text.** *ESL* **[free]** — **§3.4** (§3.4.1 ridge, §3.4.2 lasso, §3.4.3 subset vs ridge vs lasso), **§7.2–7.3**
(bias–variance), **§7.10** (cross-validation). James, Witten, Hastie & Tibshirani, *ISL* 2e **[free]** — **Ch. 5–6**.
Bishop *PRML* **[free]** — **§3.1.4** (regularised least squares), **§3.2** (bias–variance), **§3.3** (Bayesian
linear regression), **§3.5** (evidence approximation). Murphy *PML1* **[free]** — **§4.5, §11.3, §11.4, §11.7**.
**Depth.** Hastie, Tibshirani & Wainwright, *Statistical Learning with Sparsity* (CRC 2015) **[free]** —
**Ch. 2** (the lasso), **Ch. 5** (optimisation: proximal gradient, coordinate descent). Goodfellow et al.
**[free]** — **§5.4.4, §7.1, §7.8**. Prince *UDL* **[free]** — **Ch. 8–9** (incl. double descent).
**Course.** Prathosh, NPTEL 106108841 Week 5. CS229 notes **§8.1–8.2** (bias–variance, its decomposition,
double descent) and **Ch. 9** (regularisation, implicit regularisation, cross-validation, Bayesian
statistics). Cornell CS 4780 lecture notes **11** (*Model selection*) and **12** (*Bias–variance
trade-off*). Berkeley CS 189 lectures **12, 13, 22**. IIT Bombay CS 725 *Foundations of ML* (course page,
§10.7).
**Papers.** Tikhonov (1963) · Hoerl & Kennard, "Ridge Regression: Biased Estimation for Nonorthogonal
Problems" (Technometrics 1970) · Stone, "Cross-Validatory Choice and Assessment of Statistical
Predictions" (JRSS-B 1974) · Golub, Heath & Wahba, "Generalized Cross-Validation" (Technometrics 1979) ·
Geman, Bienenstock & Doursat, "Neural Networks and the Bias/Variance Dilemma" (Neural Computation 1992) ·
Bishop, "Training with Noise Is Equivalent to Tikhonov Regularization" (Neural Computation 1995) ·
Tibshirani, "Regression Shrinkage and Selection via the Lasso" (JRSS-B 1996) · Domingos, "A Unified
Bias-Variance Decomposition" (ICML 2000) · Tseng, "Convergence of a Block Coordinate Descent Method"
(JOTA 2001) · Efron, Hastie, Johnstone & Tibshirani, "Least Angle Regression" (Ann. Stat. 2004) ·
Zou & Hastie, "Regularization and Variable Selection via the Elastic Net" (JRSS-B 2005) · Park &
Casella, "The Bayesian Lasso" (JASA 2008) · Beck & Teboulle, "A Fast Iterative Shrinkage-Thresholding
Algorithm" (SIAM J. Imaging Sci. 2009) · Friedman, Hastie & Tibshirani, "Regularization Paths for
Generalized Linear Models via Coordinate Descent" (J. Stat. Software 2010) · Belkin, Hsu, Ma & Mandal,
"Reconciling Modern Machine-Learning Practice and the Classical Bias–Variance Trade-off" (PNAS 2019;
arXiv:1812.11118).
**Stop at.** High-dimensional lasso theory (restricted eigenvalue conditions, oracle inequalities —
*Statistical Learning with Sparsity* Ch. 11).

---

### MLF-06 — Kernel machines and support vector machines

**Week 6.** *Maximum-margin classifiers; dual form; KKT conditions; kernel trick and RKHS intuition.*
**Floor.** MLF-01 item 8; MLF-05 items 4, 8; PRE-CALC items 1, 3, 4; PRE-LA items 1, 6.

**Theory — margins and duality.**

1. **Margins (derive).** Labels \(y_i\in\{\pm1\}\), classifier \(\mathrm{sign}(w^\top x+b)\). The signed distance of
   \(x_i\) to the hyperplane is the **geometric margin** \(\gamma_i=y_i(w^\top x_i+b)/\|w\|\). Rescaling \((w,b)\) changes the
   functional margin \(y_i(w^\top x_i+b)\) but not \(\gamma_i\); fix the scale by \(\min_iy_i(w^\top x_i+b)=1\), so the margin is
   \(1/\|w\|\).
2. **Hard-margin primal.** \(\min_{w,b}\tfrac12\|w\|^2\) s.t. \(y_i(w^\top x_i+b)\ge1\): a convex QP with a unique \(w\).
3. **Lagrangian duality and KKT (derive).** For \(\min f_0(x)\) s.t. \(f_i(x)\le0\), \(h_j(x)=0\):
   \(\mathcal{L}=f_0+\sum_i\alpha_if_i+\sum_j\nu_jh_j\), \(\alpha\ge0\); dual function \(g(\alpha,\nu)=\inf_x\mathcal{L}\).
   **Weak duality** \(g\le p^\star\) (one line: for feasible \(x\), \(\mathcal{L}\le f_0\)). For convex problems, **Slater's
   condition** (a strictly feasible point) gives strong duality \(d^\star=p^\star\). Then the **KKT conditions**
   are necessary and sufficient:
   (1) stationarity \(\nabla f_0+\sum_i\alpha_i\nabla f_i+\sum_j\nu_j\nabla h_j=0\); (2) primal feasibility;
   (3) dual feasibility \(\alpha\ge0\); (4) **complementary slackness** \(\alpha_if_i(x^\star)=0\).
   *Prove (4):* \(f_0(x^\star)=g(\alpha^\star,\nu^\star)\le f_0(x^\star)+\sum_i\alpha_i^\star f_i(x^\star)\le f_0(x^\star)\), so the sum of non-positive
   terms is zero and each term is zero.
4. **Hard-margin dual (derive).** \(\mathcal{L}=\tfrac12\|w\|^2-\sum_i\alpha_i[y_i(w^\top x_i+b)-1]\).
   \(\nabla_w\mathcal{L}=0\Rightarrow w=\sum_i\alpha_iy_ix_i\); \(\partial_b\mathcal{L}=0\Rightarrow\sum_i\alpha_iy_i=0\). Substituting:
   \[
   \max_{\alpha\ge0,\ \sum_i\alpha_iy_i=0}\ \sum_i\alpha_i-\tfrac12\sum_{i,j}\alpha_i\alpha_jy_iy_j\,x_i^\top x_j .
   \]
   Complementary slackness: \(\alpha_i>0\Rightarrow y_i(w^\top x_i+b)=1\) — only points **on** the margin (support
   vectors) carry weight. \(b=y_s-w^\top x_s\) for any support vector (average over all for stability).
   Leave-one-out error \(\le\#\mathrm{SV}/n\) (Vapnik; statement).
5. **Soft margin (derive).** \(\min\tfrac12\|w\|^2+C\sum_i\xi_i\) s.t. \(y_i(w^\top x_i+b)\ge1-\xi_i\), \(\xi_i\ge0\). With multipliers
   \(\mu_i\) for \(\xi_i\ge0\), stationarity in \(\xi_i\) gives \(C-\alpha_i-\mu_i=0\), so the dual is item 4's with the **box**
   \(0\le\alpha_i\le C\). KKT cases: \(\alpha_i=0\Rightarrow y_if(x_i)\ge1\); \(0<\alpha_i<C\Rightarrow y_if(x_i)=1\) (free support vectors
   — compute \(b\) from these); \(\alpha_i=C\Rightarrow y_if(x_i)\le1\) (margin violators). Eliminating \(\xi\):
   \(\min_{w,b}\sum_i\max(0,1-y_if(x_i))+\frac1{2C}\|w\|^2\) — **hinge-loss ERM with an L2 penalty**, joining MLF-01
   item 8 and MLF-05.

**Theory — kernels.**

6. **The kernel trick.** The dual objective and the predictor \(f(x)=\sum_i\alpha_iy_i\,x_i^\top x+b\) touch data only
   through inner products. Replace \(x^\top z\) by \(k(x,z)=\langle\phi(x),\phi(z)\rangle\). *Derive* the explicit map for
   \(k(x,z)=(x^\top z+c)^2\) on \(\mathbb{R}^2\): \(\phi(x)=(x_1^2,\,x_2^2,\,\sqrt2x_1x_2,\,\sqrt{2c}\,x_1,\,\sqrt{2c}\,x_2,\,c)\). Degree
   \(p\) in \(d\) dimensions has \(\binom{d+p}{p}\) features but costs \(O(d)\) to evaluate. The Gaussian
   (RBF) kernel \(e^{-\|x-z\|^2/2s^2}\) has an infinite-dimensional feature map (expand \(e^{x^\top z/s^2}\) as a series).
7. **Which functions are kernels.** \(k\) is **positive definite** iff every Gram matrix \(K_{ij}=k(x_i,x_j)\) is
   symmetric PSD. *Necessity:* \(v^\top Kv=\|\sum_iv_i\phi(x_i)\|^2\ge0\). Mercer's theorem (continuous \(k\) on a compact
   domain): \(k(x,z)=\sum_j\lambda_je_j(x)e_j(z)\), \(\lambda_j\ge0\) (statement). **Closure** — prove the first two,
   state the rest: \(k_1+k_2\); \(ck_1\) (\(c>0\)); \(k_1k_2\) (Schur product theorem); \(g(x)k_1(x,z)g(z)\); polynomials
   with non-negative coefficients in \(k_1\); \(\exp(k_1)\); \(k_1(\psi(x),\psi(z))\). *Show the RBF kernel is valid*:
   \(e^{-\|x\|^2/2s^2}\cdot e^{x^\top z/s^2}\cdot e^{-\|z\|^2/2s^2}\). \(-\|x-z\|^2\) is **not** PD (only conditionally PD) — PY-6 detects it.
8. **RKHS intuition (Moore–Aronszajn).** From a PD \(k\), take \(\mathcal{H}_0=\mathrm{span}\{k(x,\cdot)\}\) with
   \(\langle\sum_ia_ik(x_i,\cdot),\sum_jb_jk(z_j,\cdot)\rangle=\sum_{ij}a_ib_jk(x_i,z_j)\), and complete it. The **reproducing
   property** \(\langle f,k(x,\cdot)\rangle_{\mathcal{H}}=f(x)\) follows. For \(f=\sum_i\alpha_ik(x_i,\cdot)\), \(\|f\|_{\mathcal{H}}^2=\alpha^\top K\alpha\).
   *Why the norm means smoothness (derive):* by Cauchy–Schwarz,
   \(|f(x)-f(x')|\le\|f\|_{\mathcal{H}}\,\sqrt{k(x,x)-2k(x,x')+k(x',x')}\) — a small RKHS norm forces \(f\) to vary slowly in the
   kernel's own geometry. Evaluation is a bounded functional, so norm convergence implies pointwise
   convergence — the property \(L^2\) lacks.
9. **Representer theorem (prove).** For \(\min_{f\in\mathcal{H}}L\big(f(x_1),\dots,f(x_n)\big)+\Omega(\|f\|_{\mathcal{H}})\) with \(\Omega\) strictly
   increasing, every minimiser has the form \(f=\sum_i\alpha_ik(x_i,\cdot)\). *Proof:* write \(f=f_\parallel+f_\perp\) with
   \(f_\parallel\in\mathrm{span}\{k(x_i,\cdot)\}\). By reproduction \(f(x_i)=\langle f,k(x_i,\cdot)\rangle=f_\parallel(x_i)\): the loss ignores \(f_\perp\).
   \(\|f\|^2=\|f_\parallel\|^2+\|f_\perp\|^2\), so \(f_\perp\ne0\) strictly increases the penalty. The SVM (with unpenalised \(b\) —
   the semiparametric version) and kernel ridge regression are instances: an infinite-dimensional
   problem becomes an \(n\)-dimensional one.
10. **Kernel ridge regression (derive).** \(\min_f\sum_i(y_i-f(x_i))^2+\lambda\|f\|_{\mathcal{H}}^2\) with item 9's form:
    \(\|y-K\alpha\|^2+\lambda\alpha^\top K\alpha\Rightarrow\alpha=(K+\lambda I)^{-1}y\). It equals ridge in feature space by the push-through
    identity \((\Phi^\top\Phi+\lambda I)^{-1}\Phi^\top=\Phi^\top(\Phi\Phi^\top+\lambda I)^{-1}\) (multiply both sides out). \(O(n^3)\) instead of \(O(d^3)\).
    With \(\lambda=\sigma^2\) it is the Gaussian-process posterior mean.
11. **SMO (derive the two-variable step).** Dual as a minimisation: \(W(\alpha)=\tfrac12\alpha^\top Q\alpha-\mathbf{1}^\top\alpha\),
    \(Q_{ij}=y_iy_jK_{ij}\), \(0\le\alpha\le C\), \(y^\top\alpha=0\). The equality constraint forbids moving one coordinate, so
    move a pair \((i,j)\) along \(y_i\alpha_i+y_j\alpha_j=\text{const}\). With \(E_k=f(x_k)-y_k\) and
    \(\eta=K_{ii}+K_{jj}-2K_{ij}>0\): unconstrained \(\alpha_j'=\alpha_j+y_j(E_i-E_j)/\eta\), clipped to \([L,H]\) where
    \(y_i\ne y_j\): \(L=\max(0,\alpha_j-\alpha_i)\), \(H=\min(C,C+\alpha_j-\alpha_i)\); \(y_i=y_j\): \(L=\max(0,\alpha_i+\alpha_j-C)\),
    \(H=\min(C,\alpha_i+\alpha_j)\). Then \(\alpha_i'=\alpha_i+y_iy_j(\alpha_j-\alpha_j')\). Threshold:
    \(b_1=b-E_i-y_i(\alpha_i'-\alpha_i)K_{ii}-y_j(\alpha_j'-\alpha_j)K_{ij}\), \(b_2=b-E_j-y_i(\alpha_i'-\alpha_i)K_{ij}-y_j(\alpha_j'-\alpha_j)K_{jj}\);
    take \(b_1\) if \(0<\alpha_i'<C\), else \(b_2\) if \(0<\alpha_j'<C\), else their mean. Pair selection: the **maximal
    violating pair** (Keerthi et al. 2001) or second-order working-set selection (Fan, Chen & Lin 2005,
    LIBSVM's default). Stop when the KKT violation is below tolerance.
12. **Scaling out.** *Pegasos* — SGD on \(\frac\lambda2\|w\|^2+\frac1n\sum_i\max(0,1-y_iw^\top x_i)\) with step \(1/(\lambda t)\), \(\tilde O(1/(\lambda\varepsilon))\)
    iterations. *Random Fourier features* (Rahimi & Recht 2007): by Bochner's theorem a shift-invariant PD
    kernel is the Fourier transform of a non-negative measure; for the RBF kernel draw \(\omega\sim\mathcal{N}(0,s^{-2}I)\),
    \(b\sim U[0,2\pi]\), \(z(x)=\sqrt{2/D}\cos(\Omega x+b)\), so \(\mathbb{E}\,z(x)^\top z(x')=k(x,x')\) with \(O(D^{-1/2})\) error — then run a
    *linear* method.
13. **Why the margin generalises (statement).** For \(\|x\|\le R\) and margin \(\gamma\), the Rademacher complexity
    of the unit-margin class is \(\le R/(\gamma\sqrt n)\) — **independent of dimension**, which is why an
    infinite-dimensional feature map does not automatically overfit (Mohri et al. Ch. 5).
14. **Practicalities.** Multiclass: one-vs-rest or one-vs-one. Probabilities: Platt scaling (a logistic
    fit on SVM scores). Choose \(C\) and \(s\) on a log grid by CV (MLF-05 item 11).

**Derive.** (i) Items 1, 3 (with the complementary-slackness proof), 4, 5. (ii) The feature map in
item 6 and the RBF validity argument in item 7. (iii) The smoothness bound in item 8. (iv) Item 9.
(v) Item 10 both ways. (vi) Item 11's clipped update from the one-dimensional constrained
quadratic.

**Build — PY-6** (`mlf/kernels/`).
- `kernels.py`: `linear`, `polynomial(degree, c)`, `rbf(s)` (Gram via the PRE-NP distance identity, clamped),
  `is_psd(K, tol)` with `eigvalsh`, `center_gram`.
- `svm_primal.py`: `pegasos(X, y, lam, epochs, rng)`, `primal_objective`.
- `smo.py`: `SMO(C, kernel, tol, max_iter)` — error cache, maximal-violating-pair selection, KKT
  stopping, `dual_objective`, `support_`, `decision_function`.
- `krr.py`: `KernelRidge(kernel, lam)` via Cholesky.
- `rff.py`: `RandomFourierFeatures(D, s, rng)`.

**Accept.**
1. Linear kernel, separable data: duality gap \(\big(P(w,b,\xi)-D(\alpha)\big)/|P|\le10^{-4}\); margin \(1/\|w\|\) equals the minimum
   geometric margin to \(10^{-6}\); every KKT condition holds to `tol=1e-3`; support set and decision values
   agree with the oracle `sklearn.svm.SVC(kernel="linear", C=C)` to \(10^{-3}\).
2. Soft margin: points with \(0<\alpha_i<C\) have \(|y_if(x_i)-1|<10^{-3}\), points with \(\alpha_i=C\) have \(y_if(x_i)\le1+10^{-3}\).
3. Pegasos's primal objective is within 1% of SMO's optimum after 100 epochs.
4. `is_psd` accepts RBF and polynomial Gram matrices on random data (min eigenvalue \(\ge-10^{-10}\lambda_{\max}\)) and
   rejects \(-\|x-z\|^2\).
5. Kernel ridge with a degree-2 polynomial kernel equals explicit-feature ridge on \(\phi(x)\) from item 6 to
   \(10^{-8}\).
6. Adding kernel centres at non-training points does not lower the regularised KRR objective (to
   \(10^{-10}\)) — the representer theorem, measured.
7. Max absolute RFF kernel-approximation error versus \(D\in\{10,\dots,10^4\}\) has log–log slope \(-0.5\pm0.1\).
8. Concentric circles: linear SVM accuracy \(\approx50\%\); RBF SVM \(>98\%\).

**Exercises.** (a) Derive the dual of the SVM **without** a bias and show the equality constraint
disappears. (b) Show the RBF kernel matrix of distinct points is strictly positive definite, hence
the RBF SVM can shatter any finite set. (c) Derive the dual of kernel ridge regression from its
primal constrained form using KKT.

**Text.** Stanford CS229 notes **[free]** — **Ch. 5** (§5.1–5.4: feature maps, kernel trick, properties of
kernels) and **Ch. 6** (§6.1–6.8: margins, optimal margin classifier, Lagrange duality, dual form,
non-separable case, SMO). Bishop *PRML* **[free]** — **§6.1–6.2** (dual representations, constructing kernels),
**§7.1** (maximum-margin classifiers), **Appendix E** (Lagrange multipliers). Deisenroth et al., *MML*
**[free]** — **Ch. 12**. *ESL* **[free]** — **§5.8** (RKHS), **§12.2–12.3**. Murphy *PML1* **[free]** — **§17.1, §17.3**.
Shalev-Shwartz & Ben-David **[free]** — **Ch. 15–16**. Mohri et al. **[free]** — **Ch. 5–6**. Boyd & Vandenberghe
**[free]** — **Ch. 5** (duality, KKT).
**Depth.** Schölkopf & Smola, *Learning with Kernels* (MIT Press 2002) **[paid]**. Steinwart & Christmann,
*Support Vector Machines* (Springer 2008) **[paid]** — the RKHS chapter. Gretton, *RKHS lecture notes*
(Gatsby/UCL) **[free]**. Bach, *Learning Theory from First Principles* **[free]** — Ch. 7 (kernel methods).
**Course.** Prathosh, NPTEL 106108841 Week 6. Stanford CS229 *SMO handout* (simplified SMO) **[free]**.
Cornell CS 4780 lecture notes **9** (*SVM*), **13–14** (*Kernels*). Berkeley CS 189 lectures **3–4**. IISc
**E0 270** (CSA). NPTEL Sastry, *Statistical Pattern Recognition* — SVM and kernel lectures; NPTEL Ravindran,
*Introduction to ML* — SVM weeks.
**Papers.** Aronszajn, "Theory of Reproducing Kernels" (Trans. AMS 1950) · Kimeldorf & Wahba, "Some
Results on Tchebycheffian Spline Functions" (J. Math. Anal. Appl. 1971) · Boser, Guyon & Vapnik, "A
Training Algorithm for Optimal Margin Classifiers" (COLT 1992) · Cortes & Vapnik, "Support-Vector
Networks" (Machine Learning 1995) · Platt, "Sequential Minimal Optimization" (MSR-TR-98-14, 1998) ·
Platt, "Probabilistic Outputs for Support Vector Machines" (1999) · Schölkopf, Herbrich & Smola, "A
Generalized Representer Theorem" (COLT 2001) · Keerthi, Shevade, Bhattacharyya & Murthy, "Improvements
to Platt's SMO Algorithm" (Neural Computation 2001) · Fan, Chen & Lin, "Working Set Selection Using
Second Order Information" (JMLR 2005) · Rahimi & Recht, "Random Features for Large-Scale Kernel
Machines" (NeurIPS 2007) · Shalev-Shwartz, Singer, Srebro & Cotter, "Pegasos" (Math. Programming 2011) ·
Chang & Lin, "LIBSVM" (ACM TIST 2011).
**Stop at.** SVR, one-class SVM, multiple-kernel learning; Gaussian processes beyond the KRR
equivalence (Cornell lecture note 15 if curious).

---

### MLF-07 — Perceptron, neural networks, gradient-based optimisation, backpropagation

**Week 7.** *Perceptron; neural networks; gradient-based optimisation; error backpropagation.*
**Floor.** MLF-01 item 8; MLF-04 items 9, 12; PRE-CALC item 2; T-DL §4.6 items 1–5; M.NS.

**Theory — the perceptron.**

1. **Algorithm.** Bias absorbed into \(x\). Predict \(\mathrm{sign}(w^\top x)\); on a mistake \(w\leftarrow w+y_ix_i\). It is SGD with
   step 1 on \(\max(0,-y\,w^\top x)\).
2. **Novikoff's theorem (prove).** Assume \(\|x_i\|\le R\) and some unit \(w^\star\) has \(y_iw^{\star\top}x_i\ge\gamma>0\). Start at
   \(w_0=0\). After \(k\) mistakes: \(w_k^\top w^\star\ge k\gamma\) (each update adds \(y_ix_i^\top w^\star\ge\gamma\)), and
   \(\|w_k\|^2\le kR^2\) (a mistake means \(y_iw^\top x_i\le0\), so \(\|w+y_ix_i\|^2\le\|w\|^2+R^2\)). Hence
   \(k\gamma\le w_k^\top w^\star\le\|w_k\|\le\sqrt kR\), i.e. **\(k\le(R/\gamma)^2\)** — independent of \(n\) and \(d\).
3. **Limits.** Non-separable data: the weights cycle (perceptron cycling theorem). **XOR** is not
   linearly separable (*prove*: the four inequalities contradict). The averaged/voted perceptron
   restores a generalisation guarantee (Freund & Schapire 1999).

**Theory — networks.**

4. **MLP.** \(a^0=x\); \(z^\ell=W^\ell a^{\ell-1}+b^\ell\); \(a^\ell=\sigma(z^\ell)\). Without \(\sigma\) the network collapses to one affine
   map. An exact XOR net: \(h_1=\mathrm{ReLU}(x_1+x_2)\), \(h_2=\mathrm{ReLU}(x_1+x_2-1)\), \(\hat y=h_1-2h_2\) (*check all four
   inputs*). **Universal approximation:** one hidden layer with a non-polynomial activation approximates
   any continuous function on a compact set to any accuracy (Cybenko 1989; Hornik, Stinchcombe &
   White 1989) — possibly with exponential width; some functions need exponentially fewer units when
   deep (Telgarsky 2016). Statements only.
5. **Backpropagation, matrix form (derive).** Let \(\delta^\ell=\partial L/\partial z^\ell\). Output: \(\delta^L=\nabla_{a^L}L\odot\sigma'(z^L)\), or
   \(p-y\) for fused softmax–cross-entropy (§4.6 item 2). Recursion \(\delta^\ell=(W^{\ell+1})^\top\delta^{\ell+1}\odot\sigma'(z^\ell)\).
   Parameters: \(\partial L/\partial W^\ell=\delta^\ell(a^{\ell-1})^\top\), \(\partial L/\partial b^\ell=\delta^\ell\). For a mini-batch with rows as
   examples, \(\nabla W^\ell=\frac1B(\Delta^\ell)^\top A^{\ell-1}\). The general reverse-mode statement and its
   \(O(1)\)-passes cost argument are §4.6 item 1's; here you derive the MLP instance line by line.
6. **Activations and saturation (derive).** \(\sigma'(z)=\sigma(z)(1-\sigma(z))\le\tfrac14\): across \(L\) sigmoid layers the
   activation-derivative factors alone shrink the gradient by up to \(4^{-L}\). With a sigmoid output and
   **squared** loss, \(\partial L/\partial z=(a-y)\sigma'(z)\) vanishes when the unit saturates at the wrong answer;
   with **cross-entropy** the \(\sigma'\) cancels to \(a-y\). ReLU: derivative 0/1, no saturation for
   \(z>0\), dead units for \(z<0\). Initialisation that keeps variance stable is §4.6 item 3's.

**Theory — optimisation.**

7. **Gradient descent on a quadratic (derive).** \(f(x)=\tfrac12x^\top Ax\), \(A\succ0\) with eigenvalues
   \(\lambda_{\min}\le\dots\le\lambda_{\max}\). GD multiplies the error along eigenvector \(i\) by \(1-\eta\lambda_i\) each step:
   converges iff \(\eta<2/\lambda_{\max}\); the best fixed step \(\eta=2/(\lambda_{\max}+\lambda_{\min})\) gives contraction
   \(\frac{\kappa-1}{\kappa+1}\), \(\kappa=\lambda_{\max}/\lambda_{\min}\). Conditioning *is* the speed limit.
8. **General rates (derive the first, state the rest).** From the descent lemma (PRE-CALC item 2) with
   \(\eta=1/L\): \(f(x_{k+1})\le f(x_k)-\frac1{2L}\|\nabla f(x_k)\|^2\). Telescoping gives, for **any** \(L\)-smooth \(f\)
   bounded below, \(\min_{k<K}\|\nabla f(x_k)\|^2\le\frac{2L(f(x_0)-f_{\inf})}K\). For convex \(f\):
   \(f(x_k)-f^\star\le\frac{L\|x_0-x^\star\|^2}{2k}\). For \(\mu\)-strongly convex \(f\): \(\|x_k-x^\star\|^2\le(1-\mu/L)^k\|x_0-x^\star\|^2\).
9. **Stochastic gradients.** A mini-batch gradient is unbiased with variance \(\propto1/B\). With constant step
   SGD converges to a neighbourhood whose size scales with \(\eta\); exact convergence needs
   \(\sum\eta_t=\infty\), \(\sum\eta_t^2<\infty\) (Robbins–Monro). Reshuffle every epoch.
10. **Momentum and adaptivity.** Heavy ball \(v\leftarrow\beta v+\nabla f,\ x\leftarrow x-\eta v\): on quadratics, tuned
    parameters give \(\frac{\sqrt\kappa-1}{\sqrt\kappa+1}\) (Polyak 1964) — at \(\kappa=100\), \(0.818\) versus GD's \(0.980\).
    Nesterov's method attains \(O(1/k^2)\) on smooth convex problems. AdaGrad → RMSProp → Adam (Adam's
    update and bias correction are §4.6 item 5's). **AdamW (derive the difference):** an L2 term adds
    \(\lambda w\) to the gradient, which Adam then divides by \(\sqrt{\hat v}\); decoupled weight decay subtracts \(\eta\lambda w\)
    directly, restoring MLF-05's meaning of \(\lambda\).
11. **Regularising networks.** Weight decay (MLF-05 item 8), early stopping (MLF-05 item 10), data
    augmentation, and dropout: *inverted* dropout multiplies kept activations by \(1/(1-p)\) so that
    \(\mathbb{E}[\text{output}]\) is unchanged and inference needs no rescaling (*derive*).

**Derive.** (i) Item 2. (ii) The XOR impossibility and the explicit XOR net. (iii) Item 5 for a
3-layer MLP with softmax output. (iv) Item 6's two claims. (v) Items 7 and the first bound in 8.
(vi) The AdamW distinction and inverted dropout's scale.

**Build — PY-7** (`mlf/autograd/`, plus `mlf/linear/perceptron.py`).
- `perceptron.py`: `Perceptron`, `AveragedPerceptron`, mistake counter, cycle detection.
- `tensor.py`: `Tensor(data, requires_grad)` holding an `np.ndarray`, `.grad`, parents, and a backward
  closure. Iterative topological sort (no recursion — deep graphs overflow Python's stack).
  **`unbroadcast(grad, shape)`**: sum over leading axes and over axes where `shape` has size 1 — the most
  common autodiff bug in NumPy. Ops: `+ - * / neg`, `**` (scalar), `@`, `sum(axis, keepdims)`, `mean`,
  `reshape`, `transpose`, `__getitem__` (backward with `np.add.at` so repeated indices accumulate), `exp`,
  `log`, `tanh`, `sigmoid` (branch on sign), `relu`, `concat`, `stack`, `where`.
- `functional.py`: fused `log_softmax`, `cross_entropy(logits, targets)`, `mse`, `dropout`.
- `nn.py`: `Module` (recursive `parameters()`, `train()`/`eval()`), `Linear` (Xavier/He init), `MLP`,
  `Dropout`, `LayerNorm`, `BatchNorm1d`.
- `optim.py`: `SGD`, `Momentum`, `Nesterov`, `AdaGrad`, `RMSProp`, `Adam`, `AdamW`; `StepLR`, `CosineLR`, warm-up.
- `mlp_manual.py`: item 5 written explicitly without the tape, as a cross-check.

**Accept.**
1. Every op passes the gradient check, including broadcasting \((3,1)+(1,4)\), `keepdims` sums, and
   `x[[0,0,1]]` (repeated indices).
2. `mlp_manual` and the autograd MLP agree to \(10^{-10}\) on weights and gradients.
3. Perceptron on data with planted \(R,\gamma\): mistakes \(\le(R/\gamma)^2\) on all of 100 seeds. On XOR, a repeated
   weight vector is detected (cycling).
4. The hand-set XOR network is exact. A 2-4-1 ReLU MLP trained with Adam from random init solves XOR on
   \(\ge90\%\) of 100 seeds; you diagnose the failures (dead ReLUs) by inspecting pre-activations.
5. Quadratic with \(\kappa=100\): \(\eta=1.9/\lambda_{\max}\) converges and \(\eta=2.1/\lambda_{\max}\) diverges; the measured
   per-step contraction equals \(\max_i|1-\eta\lambda_i|\) to \(10^{-6}\); with \(\eta=2/(\lambda_{\max}+\lambda_{\min})\) it is \(0.980\), and
   Polyak-tuned heavy ball measures \(\approx0.818\).
6. Constant-step SGD on least squares: halving \(\eta\) halves the stationary excess loss (within 20%).
7. A 10-layer sigmoid MLP with Xavier init: first-layer gradient norm is orders of magnitude below the
   last layer's; ReLU with He init keeps the ratio within one order of magnitude.
8. Two-moons (\(n=1000\), noise 0.2): a 2-hidden-layer MLP reaches \(\ge97\%\) held-out accuracy.

**Exercises.** (a) Show the perceptron is a special case of Pegasos with \(\lambda\to0\) and a particular
step. (b) Derive backprop through LayerNorm. (c) Prove that for \(L\)-smooth convex \(f\) GD with \(\eta>2/L\)
can diverge (give a quadratic).

**Text.** Bishop *PRML* **[free]** — **§4.1.7** (perceptron), **§5.1–5.3** (feed-forward networks, training,
error backpropagation). Bishop & Bishop, *Deep Learning: Foundations and Concepts* **[free online]** —
**Ch. 6–9** (deep networks, gradient descent, backpropagation, regularisation). Goodfellow et al. **[free]**
— **Ch. 6** (§6.5 back-propagation), **Ch. 7**, **Ch. 8** (§8.3 basic algorithms, §8.5 adaptive learning rates).
Prince *UDL* **[free]** — **Ch. 3–7, 9**. *D2L* **[free]** — **Ch. 5** (MLPs), **Ch. 12** (optimisation
algorithms). Murphy *PML1* **[free]** — **§8.2, §8.4, §13.2–13.4**. Shalev-Shwartz & Ben-David **[free]** —
**§9.1.2** (perceptron), **Ch. 14** (SGD), **Ch. 20** (neural networks). CS229 notes **§2.2** (perceptron),
**Ch. 7** (§7.4 backpropagation, §7.5 vectorisation).
**Depth.** Bottou, Curtis & Nocedal, "Optimization Methods for Large-Scale Machine Learning" (SIAM
Review 2018; arXiv:1606.04838) **[free]**. Bubeck, *Convex Optimization: Algorithms and Complexity* (FnT ML
2015; arXiv:1405.4980) **[free]**. Nesterov, *Lectures on Convex Optimization* 2e (Springer 2018)
**[paid]**. Baydin et al., "Automatic Differentiation in Machine Learning: A Survey" (JMLR 2018;
arXiv:1502.05767) **[free]**.
**Course.** Prathosh, NPTEL 106108841 Week 7. Cornell CS 4780 lecture notes **3** (*Perceptron*), **7**
(*Gradient descent*), **20–21** (*Neural networks*, *SGD*). Berkeley CS 189 lectures **2, 16, 17, 18**. IIT
Madras CS6910/CS7015 (Khapra) — the backprop and optimiser lectures. Karpathy's `micrograd` **[free]** —
read **after** your `tensor.py` passes its tests, and list every design difference.
**Papers.** Rosenblatt, "The Perceptron" (Psychological Review 1958) · Novikoff, "On Convergence Proofs
on Perceptrons" (1962) · Minsky & Papert, *Perceptrons* (1969) · Linnainmaa (1970; reverse-mode AD) ·
Werbos (1974 thesis) · Polyak, "Some Methods of Speeding Up the Convergence of Iteration Methods" (1964) ·
Nesterov (1983) · Robbins & Monro (1951) · Cybenko, "Approximation by Superpositions of a Sigmoidal
Function" (MCSS 1989) · Hornik, Stinchcombe & White, "Multilayer Feedforward Networks Are Universal
Approximators" (Neural Networks 1989) · Freund & Schapire, "Large Margin Classification Using the
Perceptron Algorithm" (Machine Learning 1999) · Duchi, Hazan & Singer, "Adaptive Subgradient Methods"
(JMLR 2011) · Telgarsky, "Benefits of Depth in Neural Networks" (COLT 2016) · Loshchilov & Hutter,
"Decoupled Weight Decay Regularization" (ICLR 2019; arXiv:1711.05101) · plus the §4.6 canon
(Rumelhart–Hinton–Williams, Glorot–Bengio, He et al., Kingma–Ba, Srivastava et al.).
**Stop at.** Second-order deep-learning optimisers (K-FAC), neural-tangent-kernel theory, and
convergence proofs for Adam.

---

### MLF-08 — Convolutional neural networks and transfer learning

**Week 8.** *Convolution, pooling, receptive fields, CNN architectures, transfer learning.*
**Floor.** MLF-07 (your autograd); T-CV §4.8 items 1–3; T-DL §4.6 item 4.

**Theory.**

1. **Why convolution.** A 224×224×3 image into a 1,000-unit dense layer costs \(1.5\times10^8\) weights. Images
   have **locality** (nearby pixels correlate), **stationarity** (the same pattern can appear anywhere) and
   **compositionality**. Convolution encodes the first two as hard constraints: sparse connectivity and
   weight sharing.
2. **Definitions.** Discrete 2-D convolution \((I*K)(i,j)=\sum_{m,n}I(i-m,j-n)K(m,n)\); cross-correlation
   \((I\star K)(i,j)=\sum_{m,n}I(i+m,j+n)K(m,n)\). Deep-learning "convolution" is cross-correlation; the flip
   is absorbed by learning. Multi-channel layer: input \(C_{\mathrm{in}}\times H\times W\), kernel
   \(C_{\mathrm{out}}\times C_{\mathrm{in}}\times k\times k\), output
   \(Y_{o,i,j}=b_o+\sum_{c,m,n}W_{o,c,m,n}X_{c,\,is+md,\,js+nd}\) (stride \(s\), dilation \(d\), after padding). Parameters
   \(C_{\mathrm{out}}(C_{\mathrm{in}}k^2+1)\); multiply-adds \(\approx C_{\mathrm{out}}C_{\mathrm{in}}k^2H_{\mathrm{out}}W_{\mathrm{out}}\). Output size is §4.8 item 1's.
3. **Translation equivariance (prove).** Let \((T_uX)(i)=X(i-u)\). With stride 1 and circular (or unbounded)
   padding, \(\big((T_uX)\star K\big)(i)=\sum_mX(i-u+m)K(m)=(X\star K)(i-u)=T_u(X\star K)(i)\). Stride \(s\) keeps equivariance only
   for shifts that are multiples of \(s\) — downsampling aliases (Zhang 2019).
4. **Pooling.** Max or average over \(k\times k\) windows with stride \(s\) (same size formula). A shift that
   keeps the maximiser inside its window leaves the max-pool output unchanged: **local invariance** on top
   of equivariance. Backward: average pooling spreads \(g/k^2\); max pooling routes \(g\) to the argmax (a
   subgradient; fix a tie rule). Global average pooling replaces the dense head (Network-in-Network).
5. **\(1\times1\) convolutions** are per-pixel linear maps across channels: a 256→64→256 bottleneck around a
   3×3 conv costs \(256\cdot64+64\cdot64\cdot9+64\cdot256=69{,}632\) weights versus \(256^2\cdot9=589{,}824\) (*derive*).
6. **Receptive field recurrence (derive).** Jump \(j_\ell=j_{\ell-1}s_\ell\) with \(j_0=1\); receptive field
   \(r_\ell=r_{\ell-1}+(k_\ell-1)\,d_\ell\,j_{\ell-1}\) with \(r_0=1\). Three stride-1 3×3 layers: \(r=7\). Two 3×3 layers see
   5×5 with \(18C^2\) weights instead of \(25C^2\), plus an extra non-linearity — VGG's argument. The *effective*
   receptive field is roughly Gaussian and much smaller than the theoretical one (Luo et al. 2016).
7. **Backward pass.** \(\partial L/\partial W=X\star\partial L/\partial Y\) (correlate input with upstream gradient), \(\partial L/\partial b=\sum\partial L/\partial Y\),
   \(\partial L/\partial X\) = full convolution with the flipped kernel (§4.8 item 3). In **im2col** form: forward
   \(Y_{\mathrm{col}}=W_{\mathrm{col}}\,\mathrm{cols}\); backward \(\nabla W_{\mathrm{col}}=\nabla Y_{\mathrm{col}}\,\mathrm{cols}^\top\),
   \(\nabla\mathrm{cols}=W_{\mathrm{col}}^\top\nabla Y_{\mathrm{col}}\), then **col2im** accumulating overlaps (`np.add.at`). Memory
   \(O(C_{\mathrm{in}}k^2H_{\mathrm{out}}W_{\mathrm{out}})\) per example.
8. **Residual connections (derive).** With identity skips \(x_{\ell+1}=x_\ell+F_\ell(x_\ell)\),
   \(x_L=x_\ell+\sum_{i=\ell}^{L-1}F_i(x_i)\) and
   \[
   \frac{\partial L}{\partial x_\ell}=\frac{\partial L}{\partial x_L}\Big(I+\frac{\partial}{\partial x_\ell}\sum_{i=\ell}^{L-1}F_i(x_i)\Big):
   \]
   an additive path carries the gradient unattenuated, so depth no longer multiplies Jacobians only
   (He et al. 2016b). Spatial BatchNorm normalises per channel over \((N,H,W)\) (formula §4.6 item 4).
9. **Architectures — the idea each one added.**

   | Net | Year | Idea | Scale |
   |---|---|---|---|
   | LeNet-5 | 1998 | conv–pool–conv–pool–dense, trained end to end by backprop | ≈60k params |
   | AlexNet | 2012 | ReLU, dropout, augmentation, GPU training on ImageNet | ≈60M |
   | VGG-16 | 2014 | uniform 3×3 stacks (item 6) | ≈138M |
   | GoogLeNet / Inception | 2014 | multi-branch blocks, 1×1 bottlenecks (item 5), global average pooling | an order of magnitude fewer params than AlexNet |
   | ResNet | 2015 | residual blocks (item 8) + BatchNorm, 152 layers | ResNet-50 ≈25.6M |
   | MobileNet | 2017 | depthwise-separable conv: cost ratio \(\frac1{C_{\mathrm{out}}}+\frac1{k^2}\) (*derive*) | mobile |
   | EfficientNet | 2019 | compound scaling of depth, width, resolution | — |

   Vision Transformers replace convolution by attention on patches — MLF-10.
10. **Transfer learning — definitions.** A domain \(\mathcal{D}=(\mathcal{X},P_X)\) and a task \(\mathcal{T}=(\mathcal{Y},P_{Y\mid X})\);
    transfer learning uses \((\mathcal{D}_S,\mathcal{T}_S)\) to improve learning on \((\mathcal{D}_T,\mathcal{T}_T)\) when they differ (Pan &
    Yang 2010).
11. **Why CNN features transfer.** Early layers learn generic filters (edges, Gabor-like, colour blobs);
    later layers are task-specific. Yosinski et al. (2014): transferability falls with depth and with
    task distance; freezing a split in the *middle* of co-adapted layers hurts, and fine-tuning recovers
    it.
12. **Strategies.** (a) **Linear probe** — freeze the backbone, fit a logistic head (convex: MLF-04).
    (b) **Fine-tune** everything with a small learning rate, often smaller for early layers.
    (c) **Partial freeze.** Choose by target-data size × domain similarity. Keep BatchNorm in eval mode
    when target batches are small. **L2-SP** penalises \(\|w-w_{\mathrm{pre}}\|^2\) — a Gaussian prior centred on the
    pretrained weights, i.e. MLF-05 item 8 with a non-zero prior mean.
13. **When it fails.** *Negative transfer* when source and target disagree. For domain adaptation,
    \(\epsilon_T(h)\le\epsilon_S(h)+\tfrac12d_{\mathcal{H}\Delta\mathcal{H}}(\mathcal{D}_S,\mathcal{D}_T)+\lambda^\star\) (Ben-David et al. 2010; statement): target
    error is bounded by source error, a measurable domain distance, and the error of the best joint
    hypothesis. Cross-domain generalisation is the instructor's own research area; this bound is the
    doorway to it.

**Derive.** (i) Item 3. (ii) Item 5's counts and MobileNet's ratio. (iii) Item 6's recurrence and the
VGG counts. (iv) The weight gradient in item 7 in index form, then in im2col form. (v) Item 8.

**Build — PY-8** (`mlf/conv/`).
- `conv2d.py`: `conv2d_forward(X, W, b, stride, pad, dilation)` via
  `np.lib.stride_tricks.sliding_window_view` + `np.einsum` (or im2col), `conv2d_backward`; wrapped as a
  `Tensor` op and a `Conv2d` module. A slow six-loop reference implementation, used only in tests.
- `pool.py`: `MaxPool2d` (stores argmax indices), `AvgPool2d`, `GlobalAvgPool`; `BatchNorm2d`.
- `models.py`: `LeNet5`, a small VGG-style net, a small `ResNet` (BasicBlock) for 32×32 inputs.
- `transfer.py`: `pretrain`, `linear_probe`, `finetune(lr_backbone, lr_head)`, `l2sp_penalty`.
- Data (first named datasets in this file): MNIST (OpenML 554) and Fashion-MNIST (OpenML 40996), links
  in §10.7. Train in float32 after float64 gradient checks.

**Accept.**
1. `conv2d_forward` equals the six-loop reference to \(10^{-12}\) (float64) over random stride, padding and
   dilation; conv and max-pool backward pass the gradient check.
2. With circular padding and stride 1, `conv(shift(X)) == shift(conv(X))` to \(10^{-12}\); with stride 2 the
   error is non-zero for odd shifts, and you report it.
3. For each of your models, the receptive field from item 6 equals the measured support of
   \(\partial y_{\text{centre}}/\partial X\).
4. Parameter counts of your LeNet-5 and bottleneck block match the hand counts exactly.
5. LeNet-5 reaches \(\ge98.5\%\) MNIST test accuracy in \(\le5\) epochs.
6. At initialisation, a 20-layer plain CNN's first-layer gradient norm is orders of magnitude below its
   last layer's; the same depth with residual blocks keeps them within one order of magnitude, and it
   trains to lower loss in the same number of steps.
7. Pretrain on MNIST digits 0–4; target digits 5–9 with 50 labels per class; over 5 seeds report mean ±
   s.d. for from-scratch, linear probe and fine-tune — and the ordering you observe. Repeat with
   Fashion-MNIST as the target and record whether the gain shrinks or reverses (item 13).

**Exercises.** (a) Show convolution is a linear map and write its matrix for a 1-D signal of length 5
with a width-3 kernel (§4.8 item 2's Toeplitz structure). (b) Show max pooling is not differentiable at
ties and state the subgradient your code uses. (c) Compute ResNet-18's receptive field.

**Text.** Goodfellow et al. **[free]** — **Ch. 9** (§9.1 the convolution operation, §9.2 motivation, §9.3
pooling, §9.5 variants). Prince *UDL* **[free]** — **Ch. 10–11**. *D2L* **[free]** — **Ch. 7** (§7.1–7.6:
convolutions, padding and stride, channels, pooling, LeNet), **Ch. 8** (§8.1 AlexNet, §8.2 VGG, §8.3 NiN,
§8.4 GoogLeNet, §8.5 batch norm, §8.6 ResNet, §8.7 DenseNet), **§14.2** (fine-tuning). Bishop & Bishop
**[free online]** — **Ch. 10**. Murphy *PML1* **[free]** — **§14.2–14.3**, **§19.2** (transfer learning).
**Depth.** Dumoulin & Visin, "A Guide to Convolution Arithmetic for Deep Learning" (arXiv:1603.07285)
**[free]**. Stanford CS231n notes *Convolutional Networks* and *Transfer Learning* **[free]**.
**Course.** Prathosh, NPTEL 106108841 Week 8. Stanford CS231n. Berkeley CS 189 lectures **19** (*CNNs*) and
**23** (*BatchNorm, ResNets, AdamW*). IIT Madras CS6910 (Khapra) CNN lectures. NPTEL *Deep Learning for
Computer Vision* (Vineeth N Balasubramanian, IIT Hyderabad).
**Papers.** Fukushima, "Neocognitron" (Biol. Cybernetics 1980) · LeCun et al., "Backpropagation Applied
to Handwritten Zip Code Recognition" (Neural Computation 1989) · LeCun et al. 1998 and Krizhevsky et al.
2012 (§4.8) · Lin, Chen & Yan, "Network in Network" (ICLR 2014; arXiv:1312.4400) · Zeiler & Fergus,
"Visualizing and Understanding Convolutional Networks" (ECCV 2014; arXiv:1311.2901) · Simonyan &
Zisserman, "Very Deep Convolutional Networks" (ICLR 2015; arXiv:1409.1556) · Szegedy et al., "Going
Deeper with Convolutions" (CVPR 2015; arXiv:1409.4842) · He et al., "Deep Residual Learning" (CVPR 2016;
arXiv:1512.03385) and "Identity Mappings in Deep Residual Networks" (ECCV 2016; arXiv:1603.05027) ·
Luo, Li, Urtasun & Zemel, "Understanding the Effective Receptive Field" (NeurIPS 2016; arXiv:1701.04128) ·
Howard et al., "MobileNets" (arXiv:1704.04861) · Tan & Le, "EfficientNet" (ICML 2019; arXiv:1905.11946) ·
Zhang, "Making Convolutional Networks Shift-Invariant Again" (ICML 2019; arXiv:1904.11486) · Pan & Yang,
"A Survey on Transfer Learning" (IEEE TKDE 2010) · Yosinski, Clune, Bengio & Lipson, "How Transferable
Are Features in Deep Neural Networks?" (NeurIPS 2014; arXiv:1411.1792) · Ben-David et al., "A Theory of
Learning from Different Domains" (Machine Learning 2010) · Li, Grandvalet & Davoine, "Explicit Inductive
Bias for Transfer Learning with Convolutional Networks" (ICML 2018; arXiv:1802.01483) · Kornblith,
Shlens & Le, "Do Better ImageNet Models Transfer Better?" (CVPR 2019; arXiv:1805.08974).
**Stop at.** Detection and segmentation (T-CV §4.8 owns them), neural architecture search, and
domain-adaptation algorithms beyond the Ben-David bound.

---
### MLF-09 — Sequence models: RNNs, BPTT, vanishing and exploding gradients, GRU, LSTM

**Week 9.** *RNNs; backpropagation through time; vanishing/exploding gradients; GRU; LSTM.*
**Floor.** MLF-07 (autograd, item 5, item 6); MLF-08 item 8 (additive paths); PRE-LA items 1, 3.

**Theory.**

1. **Why recurrence.** Variable-length inputs, and the same transformation applied at every position
   (parameter sharing across time). Task shapes: many-to-one (classification), aligned many-to-many
   (tagging, language modelling), unaligned many-to-many (translation — item 8).
2. **Elman RNN.** \(a_t=Wh_{t-1}+Ux_t+b\), \(h_t=\tanh(a_t)\), \(o_t=Vh_t+c\), \(\hat y_t=\mathrm{softmax}(o_t)\), \(L=\sum_tL_t\).
   Unrolled over \(T\) steps it is a \(T\)-layer feed-forward network with **tied weights**.
3. **Backpropagation through time (derive).** Output error \(e_t=\hat y_t-y_t\) (fused softmax–CE). Let
   \(g_t=\partial L/\partial h_t\) (total, through both the output and the future) and \(\delta_t=\partial L/\partial a_t\). Then, backward
   from \(t=T\) with \(\delta_{T+1}=0\):
   \[
   g_t=V^\top e_t+W^\top\delta_{t+1},\qquad \delta_t=(1-h_t^2)\odot g_t,
   \]
   \[
   \frac{\partial L}{\partial W}=\sum_t\delta_th_{t-1}^\top,\quad \frac{\partial L}{\partial U}=\sum_t\delta_tx_t^\top,\quad \frac{\partial L}{\partial b}=\sum_t\delta_t,\quad \frac{\partial L}{\partial V}=\sum_te_th_t^\top .
   \]
   Time \(O(T)\), memory \(O(T)\) (every \(h_t\) is stored). **Truncated BPTT** backpropagates only \(k\) steps: cheaper,
   and structurally blind to dependencies longer than \(k\).
4. **Vanishing and exploding gradients (derive).** The long-range term in \(\partial L_t/\partial W\) carries
   \[
   \frac{\partial h_t}{\partial h_k}=\prod_{j=k+1}^{t}\mathrm{diag}(1-h_j^2)\,W,\qquad \Big\|\frac{\partial h_t}{\partial h_k}\Big\|_2\le\big(\gamma\,\sigma_{\max}(W)\big)^{t-k},
   \]
   with \(\gamma=\sup|\tanh'|=1\). So \(\sigma_{\max}(W)<1\) is **sufficient** for geometric vanishing, and \(\sigma_{\max}(W)>1\) is
   **necessary** for explosion (Pascanu, Mikolov & Bengio 2013). Linear case: \(\partial h_t/\partial h_k=W^{t-k}\), governed by the
   eigenvalues of \(W\). Consequence: \(\partial L/\partial W\) is dominated by short-range terms, and gradient descent
   cannot assign credit across long gaps (Bengio, Simard & Frasconi 1994 show that robustly storing
   information in the dynamics *forces* this regime).
5. **Remedies.** *Exploding:* clip by norm, \(g\leftarrow g\cdot\min(1,\tau/\|g\|)\) — direction kept, step bounded.
   *Vanishing:* change the architecture so that some path has Jacobian \(\approx I\) — gating (items 6–7);
   identity/orthogonal initialisation (IRNN, Le, Jaitly & Hinton 2015); skip connections.
6. **LSTM (Hochreiter & Schmidhuber 1997; forget gate: Gers et al. 2000).** With \(u_t=[h_{t-1};x_t]\):
   \[
   f_t=\sigma(W_fu_t+b_f),\ i_t=\sigma(W_iu_t+b_i),\ o_t=\sigma(W_ou_t+b_o),\ \tilde c_t=\tanh(W_cu_t+b_c),
   \]
   \[
   c_t=f_t\odot c_{t-1}+i_t\odot\tilde c_t,\qquad h_t=o_t\odot\tanh(c_t).
   \]
   **Why it works (derive):** along the cell path \(\partial c_t/\partial c_{t-1}=\mathrm{diag}(f_t)\) plus terms routed through the
   gates. Across \(t-k\) steps the direct path contributes \(\prod_j\mathrm{diag}(f_j)\), which the network can hold near
   \(I\) by keeping \(f\approx1\) — the **constant error carousel** (the original LSTM had \(f\equiv1\)). Initialise
   \(b_f=1\) (Jozefowicz et al. 2015). Parameters: \(4\big(d_h(d_h+d_x)+d_h\big)\).
   **Backward, one step (derive):** given \(\partial L/\partial h_t\) and \(\partial L/\partial c_t\) arriving from \(t+1\):
   \(\bar o=\bar h\odot\tanh c_t\); \(\bar c\mathrel{+}=\bar h\odot o_t\odot(1-\tanh^2c_t)\); \(\bar f=\bar c\odot c_{t-1}\); \(\bar i=\bar c\odot\tilde c_t\);
   \(\bar{\tilde c}=\bar c\odot i_t\); \(\bar c_{t-1}=\bar c\odot f_t\); gate pre-activations \(\bar a_\bullet=\bar\bullet\odot\bullet(1-\bullet)\) for
   \(\bullet\in\{f,i,o\}\) and \(\bar a_c=\bar{\tilde c}\odot(1-\tilde c_t^2)\); then \(\bar u_t=\sum W_\bullet^\top\bar a_\bullet\), split into \(\bar h_{t-1}\) and \(\bar x_t\).
7. **GRU (Cho et al. 2014).** \(z_t=\sigma(W_zu_t)\), \(r_t=\sigma(W_ru_t)\),
   \(\tilde h_t=\tanh\big(W_h[r_t\odot h_{t-1};x_t]\big)\), \(h_t=(1-z_t)\odot h_{t-1}+z_t\odot\tilde h_t\) (biases omitted; *D2L* swaps the
   role of \(z\) — state which convention you implement). The direct path \(\mathrm{diag}(1-z_t)\) is a learned leaky
   integrator; there is no separate cell or output gate. Parameters \(3\big(d_h(d_h+d_x)+d_h\big)\). Empirically
   GRU and LSTM are close; the forget gate and the output non-linearity matter most (Chung et al. 2014;
   Greff et al. 2017).
8. **Deep, bidirectional, encoder–decoder.** Stacked RNNs feed \(h^{(\ell)}_t\) upward. Bidirectional
   \(h_t=[\overrightarrow{h}_t;\overleftarrow{h}_t]\) for non-causal tasks. **Seq2seq** (Sutskever et al. 2014; Cho et al. 2014): the
   encoder compresses \(x_{1:S}\) into \(c=h_S\); the decoder models \(p(y_t\mid y_{<t},c)\). Training with **teacher
   forcing** maximises \(\sum_t\log p(y_t\mid y^{\text{gold}}_{<t},x)\); at test time the model conditions on its own outputs —
   *exposure bias* (scheduled sampling, Bengio et al. 2015). Decode greedily or with beam search plus
   length normalisation. **The fixed-size \(c\) is a bottleneck** that grows worse with \(S\); MLF-10 item 2
   removes it.
9. Perplexity and its caveats are §4.7 item 2's.

**Derive.** (i) Item 3's recursion and all four parameter gradients. (ii) Item 4's bound, and the
linear case via eigen-decomposition. (iii) Item 6's direct-path Jacobian and the one-step backward
equations. (iv) GRU's \(\partial h_t/\partial h_{t-1}\) including the gate terms. (v) Both parameter counts.

**Build — PY-9** (`mlf/seq/`).
- `rnn.py`: `rnn_forward(X, h0, params) -> (H, cache)` and `rnn_backward(dH, dO, cache)` implementing item 3
  by hand; the same cell as an autograd module; `truncated_bptt(k)`.
- `lstm.py`, `gru.py`: hand-written forward/backward (item 6's equations) and autograd modules.
- `seq2seq.py`: `Encoder`, `Decoder`, teacher forcing, `greedy_decode`, `beam_search(width, alpha)`.
- `optim.py` (PY-7) gains `clip_grad_norm_`.
- Data: `data/synthetic.py` gains the **adding problem** (Hochreiter & Schmidhuber 1997: a length-\(T\)
  sequence of pairs (value \(\sim U[0,1]\), marker), exactly two markers, target = sum of the two marked values),
  a copy task and digit-sequence reversal. Tiny Shakespeare (link §10.7) for a character-level LM.

**Accept.**
1. For RNN, LSTM and GRU: hand-written BPTT = autograd = finite differences (relative error \(<10^{-8}\), float64).
2. Linear RNN with \(W=\rho Q\), \(Q\) orthogonal: \(\|\partial h_T/\partial h_k\|_2=\rho^{T-k}\) to \(10^{-10}\). For tanh with the same \(W\), the fitted
   slope of \(\log\|\partial h_T/\partial h_k\|\) against \(T-k\) is \(\le\log\rho\); report it.
3. A ReLU RNN initialised with \(W=1.5\,Q\), \(T=100\): the gradient norm at initialisation is astronomically large (you
   predict its order from \(1.5^{100}\approx4\times10^{17}\) in the linear regime, discounted by inactive units), and unclipped
   SGD produces a non-finite loss within 10 steps; with norm clipping \(\tau=1\) every step stays finite.
4. Adding problem, \(T=100\): a vanilla tanh RNN stays near the constant-predictor MSE
   \(\mathrm{Var}(U_1+U_2)=\tfrac16\approx0.167\); an LSTM with \(b_f=1\) reaches MSE \(<0.01\). You computed \(\tfrac16\) first.
5. Your modules' parameter counts equal \(4(d_h(d_h+d_x)+d_h)\) and \(3(d_h(d_h+d_x)+d_h)\).
6. Character-level LSTM on Tiny Shakespeare: validation cross-entropy is below both the unigram entropy and
   a count-based bigram model's cross-entropy (both computed by you); report perplexity.
7. Seq2seq LSTM reversing digit strings: exact match \(\ge95\%\) at length 10, and markedly lower at length
   30 — record the number; MLF-10 accept 7 fixes it.

**Exercises.** (a) Show that for a scalar linear RNN \(h_t=wh_{t-1}+ux_t\) the gradient contribution from lag
\(m\) is proportional to \(w^{m}\). (b) Derive real-time recurrent learning's cost \(O(d_h^4)\) per step and explain
why BPTT won. (c) Show an LSTM with \(f\equiv1\), \(i\equiv1\), \(o\equiv1\) is an accumulator and cannot forget.

**Text.** Goodfellow et al. **[free]** — **Ch. 10** (§10.1 unfolding, §10.2 RNNs incl. §10.2.2 computing the gradient,
§10.3 bidirectional, §10.4 encoder–decoder, §10.7 long-term dependencies, §10.10 LSTM and gated RNNs,
§10.11.1 clipping). *D2L* **[free]** — **Ch. 9** (§9.4–9.5 RNNs from scratch, §9.7 BPTT) and **Ch. 10** (§10.1
LSTM, §10.2 GRU, §10.3 deep, §10.4 bidirectional, §10.6 encoder–decoder, §10.7 seq2seq, §10.8 beam search).
Murphy *PML1* **[free]** — **§15.2**.
**Depth.** Graves, *Supervised Sequence Labelling with Recurrent Neural Networks* (Springer 2012) **[free]**
author preprint. Olah, "Understanding LSTM Networks" **[free]**. Karpathy, "The Unreasonable Effectiveness of
Recurrent Neural Networks" **[free]**.
**Course.** Prathosh, NPTEL 106108841 Week 9. Stanford CS224n — the language-model/RNN lecture and notes
**[free]**. CMU 11-785 *Introduction to Deep Learning* — recurrent-network and BPTT lectures **[free]**. IIT
Madras CS6910 (Khapra) — BPTT, vanishing gradients, LSTM/GRU lectures.
**Papers.** Elman, "Finding Structure in Time" (Cognitive Science 1990) · Werbos, "Backpropagation Through
Time: What It Does and How to Do It" (Proc. IEEE 1990) · Williams & Zipser (Neural Computation 1989; RTRL) ·
Bengio, Simard & Frasconi, "Learning Long-Term Dependencies with Gradient Descent Is Difficult" (IEEE TNN
1994) · Hochreiter & Schmidhuber, "Long Short-Term Memory" (Neural Computation 1997) · Schuster & Paliwal,
"Bidirectional Recurrent Neural Networks" (IEEE TSP 1997) · Gers, Schmidhuber & Cummins, "Learning to
Forget" (Neural Computation 2000) · Pascanu, Mikolov & Bengio, "On the Difficulty of Training Recurrent
Neural Networks" (ICML 2013; arXiv:1211.5063) · Cho et al., "Learning Phrase Representations Using RNN
Encoder–Decoder" (EMNLP 2014; arXiv:1406.1078) · Sutskever, Vinyals & Le 2014 (§4.7) · Chung et al.,
"Empirical Evaluation of Gated Recurrent Neural Networks" (arXiv:1412.3555) · Jozefowicz, Zaremba &
Sutskever, "An Empirical Exploration of Recurrent Network Architectures" (ICML 2015) · Le, Jaitly & Hinton,
"A Simple Way to Initialize Recurrent Networks of Rectified Linear Units" (arXiv:1504.00941) · Bengio et al.,
"Scheduled Sampling" (NeurIPS 2015; arXiv:1506.03099) · Greff et al., "LSTM: A Search Space Odyssey" (IEEE
TNNLS 2017; arXiv:1503.04069).
**Stop at.** RTRL, echo-state networks, and modern state-space models (S4, Mamba) — names only.

---

### MLF-10 — Attention and Transformers

**Week 10.** *Attention mechanism; self-attention vs recurrence; encoder–decoder Transformers.*
**Floor.** MLF-03 item 13 (Nadaraya–Watson); MLF-09 item 8; T-DL §4.6 items 4, 6–8; MLF-08 item 8.

**Theory.**

1. **Attention is kernel regression with learned kernels (derive).** Nadaraya–Watson predicts
   \(f(q)=\sum_i\alpha(q,k_i)v_i\) with \(\alpha(q,k_i)=K(q,k_i)/\sum_jK(q,k_j)\). With a Gaussian kernel,
   \(\alpha_i=\mathrm{softmax}_i\big(-\tfrac12\|q-k_i\|^2\big)=\mathrm{softmax}_i\big(q^\top k_i-\tfrac12\|k_i\|^2\big)\): the \(\|q\|^2\) term cancels inside
   the softmax. For equal-norm keys this **is** dot-product attention. Attention is a differentiable,
   content-addressed soft lookup whose kernel (via \(W_Q,W_K\)) is learned.
2. **Attention in seq2seq (Bahdanau et al. 2015).** Keep every encoder state \(h_i\). At decoder step \(t\):
   \(e_{t,i}=v^\top\tanh(W_ss_{t-1}+W_hh_i)\) (additive score), \(\alpha_{t,i}=\mathrm{softmax}_i(e_{t,i})\), context \(c_t=\sum_i\alpha_{t,i}h_i\),
   \(s_t=f(s_{t-1},y_{t-1},c_t)\). The bottleneck of MLF-09 item 8 is gone, and the path from \(y_t\) to any \(x_i\) has
   constant length. Luong et al. (2015): multiplicative scores \(s^\top Wh\) and dot scores.
3. **Scaled dot-product and multi-head attention.** \(\mathrm{Attn}(Q,K,V)=\mathrm{softmax}\big(QK^\top/\sqrt{d_k}+M\big)V\) with
   \(Q=XW_Q\), \(K=X'W_K\), \(V=X'W_V\) (\(X'=X\) for self-attention). The \(1/\sqrt{d_k}\) variance argument, multi-head
   projections and positional-encoding families are §4.6 items 6–7; the KV cache is §4.6 item 8.
4. **Backward through attention (derive).** \(S=QK^\top/\sqrt{d_k}\), \(A=\mathrm{softmax}_{\text{row}}(S)\), \(Z=AV\).
   \(\bar V=A^\top\bar Z\); \(\bar A=\bar ZV^\top\); the row-softmax Jacobian \(\mathrm{diag}(a)-aa^\top\) gives
   \(\bar S_{ij}=A_{ij}\big(\bar A_{ij}-\sum_l\bar A_{il}A_{il}\big)\); \(\bar Q=\bar SK/\sqrt{d_k}\); \(\bar K=\bar S^\top Q/\sqrt{d_k}\).
5. **Self-attention is permutation-equivariant (prove).** For a permutation matrix \(P\) acting on the rows
   (tokens) of \(X\): \(Q\mapsto PQ\), \(K\mapsto PK\), \(V\mapsto PV\), \(S\mapsto PSP^\top\), and row-softmax commutes with simultaneous
   row–column permutation, so \(A\mapsto PAP^\top\) and \(Z\mapsto PAP^\top PV=PZ\). Position-wise FFNs and LayerNorm are
   equivariant too, so **an encoder without positional information is a set function**. Order has to be
   injected (item 7). A causal mask breaks the symmetry by construction.
6. **Self-attention vs recurrence vs convolution (derive the first two rows).** Per layer, for length \(n\),
   width \(d\), kernel \(k\) (Vaswani et al. 2017, Table 1):

   | Layer | Compute per layer | Sequential ops | Max path length |
   |---|---|---|---|
   | Self-attention | \(O(n^2d)\) | \(O(1)\) | \(O(1)\) |
   | Recurrent | \(O(nd^2)\) | \(O(n)\) | \(O(n)\) |
   | Convolutional | \(O(knd^2)\) | \(O(1)\) | \(O(\log_kn)\) |

   Attention wins on parallelism and path length, loses on \(n^2\) memory and on built-in inductive bias
   (recurrence has a recency bias for free). Some functions — e.g. parity of long sequences — are provably
   hard for fixed-size self-attention (Hahn 2020; statement).
7. **Sinusoidal positions encode relative offsets linearly (derive).** \(PE(p,2i)=\sin(p\omega_i)\),
   \(PE(p,2i+1)=\cos(p\omega_i)\), \(\omega_i=10000^{-2i/d}\). For each frequency,
   \[
   \begin{pmatrix}\sin((p+k)\omega)\\\cos((p+k)\omega)\end{pmatrix}=\begin{pmatrix}\cos k\omega&\sin k\omega\\-\sin k\omega&\cos k\omega\end{pmatrix}\begin{pmatrix}\sin p\omega\\\cos p\omega\end{pmatrix},
   \]
   so \(PE(p+k)=M_k\,PE(p)\) with \(M_k\) independent of \(p\). RoPE applies the same rotation to \(q\) and \(k\), making
   \(q^\top k\) depend only on the offset.
8. **The encoder block.** Original **Post-LN**: \(X'=\mathrm{LN}(X+\mathrm{MHA}(X))\), \(Y=\mathrm{LN}(X'+\mathrm{FFN}(X'))\), with
   \(\mathrm{FFN}(x)=W_2\,\mathrm{ReLU}(W_1x+b_1)+b_2\), \(d_{ff}=4d\). **Pre-LN**: \(X'=X+\mathrm{MHA}(\mathrm{LN}(X))\), \(Y=X'+\mathrm{FFN}(\mathrm{LN}(X'))\) —
   an untouched residual stream (MLF-08 item 8), trainable without learning-rate warm-up (Xiong et al.
   2020). **Parameter count (derive):** MHA \(4d^2+4d\); FFN \(8d^2+5d\); two LayerNorms \(4d\); total \(12d^2+13d\).
   Sanity check: GPT-2 small (\(d=768\), 12 blocks, vocabulary 50,257) has \(\approx12\cdot12\cdot768^2+50{,}257\cdot768\approx124\)M parameters.
9. **The decoder block and the encoder–decoder Transformer.** (i) Masked self-attention with
   \(M_{ij}=-\infty\) for \(j>i\); (ii) **cross-attention** — queries from the decoder, keys and values from the
   final encoder output; (iii) FFN — each with residual + LayerNorm. The mask makes
   \(p(y\mid x)=\prod_tp(y_t\mid y_{<t},x)\) exact while all positions train in parallel under teacher forcing.
10. **Training recipe (derive the schedule's peak).** Targets shifted right; **label smoothing**
    \(\mathcal{L}=(1-\epsilon)\,\mathrm{CE}(\text{one-hot})+\epsilon\,\mathrm{CE}(\text{uniform})\); tied input/output embeddings scaled by \(\sqrt d\)
    (Press & Wolf 2017); schedule \(\mathrm{lr}=d^{-1/2}\min(s^{-1/2},\,s\cdot w^{-3/2})\), which peaks at step \(s=w\) with value
    \((dw)^{-1/2}\). Inference: greedy or beam search (MLF-09 item 8), KV cache (§4.6).
11. **Three families.** Encoder-only (BERT: bidirectional attention, masked-token objective); decoder-only
    (GPT: causal mask, next-token objective); encoder–decoder (T5: span corruption, text-to-text). Name the
    mask each uses. Vision Transformers treat image patches as tokens (MLF-08 item 9).

**Derive.** (i) Item 1. (ii) Item 4. (iii) Item 5. (iv) Item 6's first two rows. (v) Item 7. (vi) Item 8's
parameter count. (vii) Item 10's peak.

**Build — PY-10** (`mlf/attn/`).
- `attention.py`: `sdpa(Q, K, V, mask)` forward and hand-written backward (item 4) plus the autograd op;
  `MultiHeadAttention(d, h)` (split/merge heads with `reshape`/`transpose`); `AdditiveAttention`.
- `transformer.py`: `SinusoidalPE`, `EncoderBlock(pre_ln)`, `DecoderBlock(pre_ln)`, `Transformer` (encoder–decoder),
  `label_smoothed_ce`, `NoamSchedule`, `greedy_decode`, `beam_search`; `AttnSeq2Seq` — a Bahdanau-attention GRU
  built on PY-9.
- Tasks: digit reversal at length 30 (where PY-9 failed), sorting, and a synthetic date-format translation
  (`"16 September 2026" → "2026-09-16"`).

**Accept.**
1. Hand-written attention backward = autograd = finite differences (\(<10^{-8}\)).
2. Nadaraya–Watson with a Gaussian kernel equals dot-product attention on equal-norm keys to \(10^{-12}\).
3. An encoder block without PE: \(\|f(PX)-Pf(X)\|<10^{-10}\) for random permutations; with PE the equality fails and you
   report by how much.
4. Causality: perturbing decoder input \(j\) changes outputs at positions \(<j\) by less than \(10^{-12}\).
5. \(\|PE(p+k)-M_kPE(p)\|<10^{-12}\) for all tested \(p,k\).
6. Your block's parameter count equals \(12d^2+13d\) for \(d\in\{16,64,256\}\).
7. Length-30 reversal: Transformer (2+2 layers, \(d=64\)) exact match \(\ge99\%\); attention-GRU \(\ge95\%\); PY-9's plain
   seq2seq markedly lower — all three reported side by side.
8. Loss curves for Post-LN vs Pre-LN, each with and without warm-up, at 6 layers — you report which
   configuration diverges or stalls and relate it to item 8.

**Exercises.** (a) Show that multi-head attention with \(h\) heads of size \(d/h\) costs the same as one head of
size \(d\) in parameters. (b) Show that without the \(-\infty\) mask a decoder trained with teacher forcing learns to
copy the next token, and what that does to test-time generation. (c) Derive cross-attention's complexity
\(O(n_{\mathrm{dec}}n_{\mathrm{enc}}d)\).

**Text.** Vaswani et al., "Attention Is All You Need" (the paper is the primary text for the block). *D2L*
**[free]** — **Ch. 11** (§11.1 queries/keys/values, §11.2 attention pooling by similarity — item 1, §11.3 scoring
functions, §11.4 Bahdanau, §11.5 multi-head, §11.6 self-attention and positional encoding, §11.7 the
Transformer). Prince *UDL* **[free]** — **Ch. 12**. Bishop & Bishop **[free online]** — **Ch. 12**. Murphy *PML1*
**[free]** — **§15.4–15.5**. CS229 notes **[free]** — **§17.3–17.4** (Transformer architecture, variants of
attention).
**Depth.** Phuong & Hutter, "Formal Algorithms for Transformers" (arXiv:2207.09238) **[free]** — precise
pseudocode for every variant. Rush et al., *The Annotated Transformer* (Harvard NLP) **[free]**. Tay et al.,
"Efficient Transformers: A Survey" (ACM CSUR 2022; arXiv:2009.06732).
**Course.** Prathosh, NPTEL 106108841 Week 10. Stanford CS224n (attention, Transformers). CMU 11-711 (Neubig).
IIT Madras CS6910 (Khapra) — attention and Transformer lectures.
**Papers.** Bahdanau, Cho & Bengio 2015 (§4.7) · Luong, Pham & Manning, "Effective Approaches to
Attention-Based Neural Machine Translation" (EMNLP 2015; arXiv:1508.04025) · Vaswani et al. 2017 (§4.6;
arXiv:1706.03762) · Szegedy et al., "Rethinking the Inception Architecture" (CVPR 2016; label smoothing;
arXiv:1512.00567) · Press & Wolf, "Using the Output Embedding to Improve Language Models" (EACL 2017;
arXiv:1608.05859) · Lee et al., "Set Transformer" (ICML 2019; arXiv:1810.00825) · Yun et al., "Are
Transformers Universal Approximators of Sequence-to-Sequence Functions?" (ICLR 2020; arXiv:1912.10077) ·
Hahn, "Theoretical Limitations of Self-Attention in Neural Sequence Models" (TACL 2020; arXiv:1906.06755) ·
Xiong et al., "On Layer Normalization in the Transformer Architecture" (ICML 2020; arXiv:2002.04745) ·
Raffel et al., "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer" (JMLR
2020; arXiv:1910.10683) · Devlin et al. (BERT) and Dosovitskiy et al. (ViT), cited in §4.7–4.8.
**Stop at.** Efficient-attention variants, mixture-of-experts, and alignment/RLHF (names only); LLM
serving belongs to T-MLSYS §4.12.

---

### MLF-11 — Decision trees and ensembles: bagging, random forests, AdaBoost, gradient boosting, XGBoost

**Week 11.** *Ensembles and decision trees: bagging and random forests; boosting (AdaBoost, XGBoost).*
**Floor.** MLF-01 item 8; MLF-05 item 1; MLF-07 item 8 (gradient descent); PRE-P item 5 (Jensen).

**Theory — trees.**

1. **CART classification.** A node with class proportions \(p_k\). Impurities: misclassification \(1-\max_kp_k\);
   **Gini** \(\sum_kp_k(1-p_k)=1-\sum_kp_k^2\); **entropy** \(-\sum_kp_k\log p_k\). A split of \(n_t\) points into \(n_L,n_R\) has
   decrease \(\Delta I=I(t)-\frac{n_L}{n_t}I(t_L)-\frac{n_R}{n_t}I(t_R)\). Entropy's decrease is the empirical mutual information
   between the split and the label.
2. **Splits never increase impurity (prove).** The parent's proportions are the convex combination
   \(p=w_Lp_L+w_Rp_R\), and all three impurities are concave, so \(I(p)\ge w_LI(p_L)+w_RI(p_R)\) (Jensen). Gini and
   entropy are *strictly* concave: \(\Delta I>0\) whenever \(p_L\ne p_R\). Misclassification is not, and can be blind to a
   useful split. *Compute:* parent (400, 400); split A → (300, 100) | (100, 300); split B → (200, 400) | (200, 0).
   Both have misclassification 0.25; weighted Gini is 0.375 for A and 0.333 for B, so Gini prefers B, which
   has a pure node.
3. **Regression trees and the \(O(n\log n)\) split search (derive).** Minimise the summed SSE of the children.
   Since \(\mathrm{SSE}=\sum y^2-S^2/m\) for a node with sum \(S\) and count \(m\), after sorting one feature the best split
   maximises \(S_L^2/n_L+S_R^2/n_R\), computable for every threshold from **prefix sums** in one \(O(n)\) scan.
   Classification uses prefix class counts. Finding the globally optimal tree is NP-hard (Hyafil & Rivest
   1976); CART is greedy.
4. **Cost-complexity pruning (derive the weakest link).** \(R_\alpha(T)=R(T)+\alpha|\tilde T|\) (\(|\tilde T|\) = number of leaves).
   For internal node \(t\) with subtree \(T_t\), collapsing \(T_t\) pays off once \(\alpha\ge g(t)=\frac{R(t)-R(T_t)}{|\tilde T_t|-1}\). Repeatedly
   prune the node with the smallest \(g(t)\): a nested sequence of subtrees, one per \(\alpha\)-interval; pick \(\alpha\) by CV.
5. **Properties.** Invariant to monotone feature transforms; handles mixed types; for a binary label a
   categorical feature's optimal binary split is found by sorting its levels by \(\hat P(y=1)\) (\(K-1\) candidates,
   not \(2^{K-1}\)). Low bias, **high variance**: small data changes flip early splits.

**Theory — bagging and random forests.**

6. **Variance of an average (derive).** For \(B\) identically distributed predictors with variance \(\sigma^2\) and
   pairwise correlation \(\rho\):
   \(\mathrm{Var}\big(\frac1B\sum_b\hat f_b\big)=\frac1{B^2}\big[B\sigma^2+B(B-1)\rho\sigma^2\big]=\rho\sigma^2+\frac{1-\rho}{B}\sigma^2\). Averaging kills the second term;
   **\(\rho\) is the floor**.
7. **Bagging (Breiman 1996).** Fit each predictor to a bootstrap resample; average (regression) or vote
   (classification). For squared loss, the ideal aggregate \(\varphi_A(x)=\mathbb{E}_{\mathcal{D}}\varphi(x;\mathcal{D})\) satisfies
   \(\mathbb{E}(y-\varphi_A)^2\le\mathbb{E}_{\mathcal{D}}\mathbb{E}(y-\varphi(x;\mathcal{D}))^2\) by Jensen (*derive*) — the gain is exactly the variance of \(\varphi\). For 0–1 loss,
   voting can **hurt** at points where a classifier is right less than half the time (ESL §8.7.1): the
   bias–variance argument does not transfer (MLF-05 item 1).
8. **Out-of-bag (derive).** \(P(i\notin\text{bootstrap})=(1-\frac1n)^n\to e^{-1}\approx0.368\). Each point is out-of-bag for ≈37% of the
   trees; predicting it with those trees gives a nearly free CV estimate.
9. **Random forests (Breiman 2001).** Bagged deep trees **plus** a random subset of \(m_{\mathrm{try}}\) features at every
   split (\(\sqrt p\) for classification, \(p/3\) for regression): this lowers \(\rho\) in item 6 at a small cost in
   \(\sigma^2\). Importance: impurity decrease (MDI) is biased toward high-cardinality features (Strobl et al. 2007);
   prefer permutation importance on OOB data.

**Theory — boosting.**

10. **AdaBoost (Freund & Schapire 1997).** Weights \(w_i=\frac1n\). For \(t=1..T\): fit weak learner \(h_t\) to minimise
    weighted error \(\epsilon_t\); \(\alpha_t=\tfrac12\log\frac{1-\epsilon_t}{\epsilon_t}\); \(w_i\leftarrow w_ie^{-\alpha_ty_ih_t(x_i)}/Z_t\). Output
    \(H=\mathrm{sign}(F)\), \(F=\sum_t\alpha_th_t\).
11. **Training-error bound (prove).** Unrolling the updates, \(w_i^{(T+1)}=\frac{e^{-y_iF(x_i)}}{n\prod_tZ_t}\); weights sum to 1, so
    \(\frac1n\sum_ie^{-y_iF(x_i)}=\prod_tZ_t\). Since \(\mathbf{1}[H(x_i)\ne y_i]\le e^{-y_iF(x_i)}\), training error \(\le\prod_tZ_t\).
    \(Z_t=(1-\epsilon_t)e^{-\alpha_t}+\epsilon_te^{\alpha_t}\) is minimised at item 10's \(\alpha_t\), giving \(Z_t=2\sqrt{\epsilon_t(1-\epsilon_t)}=\sqrt{1-4\gamma_t^2}\le e^{-2\gamma_t^2}\)
    with edge \(\gamma_t=\tfrac12-\epsilon_t\). Hence **training error \(\le\exp(-2\sum_t\gamma_t^2)\)**: any fixed edge over random
    guessing drives training error to zero exponentially fast — weak learnability implies strong.
12. **AdaBoost is forward-stagewise exponential-loss minimisation (derive).** Minimise
    \(\sum_ie^{-y_i(F_{t-1}(x_i)+\alpha h(x_i))}=\sum_iw_ie^{-\alpha y_ih(x_i)}\) with \(w_i\propto e^{-y_iF_{t-1}(x_i)}\): for any \(\alpha>0\), \(h\) should minimise
    weighted error, and setting the \(\alpha\)-derivative of \((1-\epsilon)e^{-\alpha}+\epsilon e^{\alpha}\) to zero returns item 10's \(\alpha_t\)
    (Friedman, Hastie & Tibshirani 2000). With MLF-01 item 8, \(F\to\tfrac12\log\frac{\eta}{1-\eta}\), so
    \(\hat P(y=1\mid x)=1/(1+e^{-2F})\). Test error often keeps falling after training error hits zero; the margin
    theory explains much of it (Schapire et al. 1998; statement).
13. **Gradient boosting (Friedman 2001; derive the logistic leaf value).** Functional gradient descent on
    \(\sum_iL(y_i,F(x_i))\): \(F_0=\arg\min_c\sum_iL(y_i,c)\); at round \(m\), pseudo-residuals
    \(r_{im}=-\partial L(y_i,F)/\partial F\big|_{F_{m-1}(x_i)}\); fit a \(J\)-leaf regression tree to \(r\); set each leaf value
    \(\gamma_{jm}=\arg\min_\gamma\sum_{x_i\in R_{jm}}L(y_i,F_{m-1}(x_i)+\gamma)\); update \(F_m=F_{m-1}+\nu\sum_j\gamma_{jm}\mathbf{1}[x\in R_{jm}]\). Squared loss:
    residuals and leaf means. Absolute loss: signs and leaf medians. Logistic (\(y\in\{0,1\}\), \(F\) = log-odds):
    \(r=y-p\), and one Newton step gives \(\gamma=\sum r_i/\sum p_i(1-p_i)\). Shrinkage \(\nu\in[0.01,0.1]\) with more rounds, and row
    subsampling (Friedman 2002), are the regularisers; stop on a validation set.
14. **XGBoost's objective (derive every line).** At round \(t\):
    \(\mathcal{L}^{(t)}=\sum_il(y_i,\hat y_i^{(t-1)}+f_t(x_i))+\Omega(f_t)\), \(\Omega(f)=\gamma T+\tfrac12\lambda\sum_jw_j^2\). Second-order Taylor with
    \(g_i=\partial_{\hat y}l\), \(h_i=\partial^2_{\hat y}l\):
    \(\mathcal{L}^{(t)}\approx\sum_i[g_if_t(x_i)+\tfrac12h_if_t(x_i)^2]+\Omega(f_t)+\text{const}\). For a fixed tree structure with leaf sets \(I_j\),
    \(G_j=\sum_{I_j}g_i\), \(H_j=\sum_{I_j}h_i\):
    \[
    \mathcal{L}^{(t)}=\sum_j\big[G_jw_j+\tfrac12(H_j+\lambda)w_j^2\big]+\gamma T\ \Rightarrow\ w_j^\star=-\frac{G_j}{H_j+\lambda},\quad \mathcal{L}^\star=-\frac12\sum_j\frac{G_j^2}{H_j+\lambda}+\gamma T .
    \]
    **Split gain:** \(\frac12\Big[\frac{G_L^2}{H_L+\lambda}+\frac{G_R^2}{H_R+\lambda}-\frac{(G_L+G_R)^2}{H_L+H_R+\lambda}\Big]-\gamma\); split only if positive, so \(\gamma\) is a
    minimum-loss-reduction pruning threshold. Squared loss: \(g=\hat y-y\), \(h=1\), so \(w^\star\) is the residual mean
    shrunk by \(\lambda\) — with \(\lambda=\gamma=0\) this is exactly item 13's tree. Logistic: \(g=p-y\), \(h=p(1-p)\), i.e. item
    13's Newton leaf plus \(\lambda\). `min_child_weight` bounds \(H_j\).
15. **XGBoost's systems ideas.** *Exact greedy:* sort each feature once and scan prefix sums of \(g,h\) (item 3).
    *Approximate:* candidate splits from a **weighted quantile sketch with weights \(h_i\)** — because the
    objective equals \(\sum_i\tfrac12h_i\big(f_t(x_i)-(-g_i/h_i)\big)^2+\text{const}\), a weighted squared loss (*derive*).
    Histogram binning (LightGBM's default). *Sparsity-aware* default directions: route missing values
    left and right, keep the larger gain. Column subsampling and shrinkage \(\eta\).
16. **Roles.** Bagging and forests cut the variance of low-bias learners; boosting cuts the bias of
    weak, high-bias learners and can overfit with too many rounds. On tabular data, well-tuned boosted trees
    remain the strong default (Grinsztajn et al. 2022) — which is also B4's lesson.

**Derive.** (i) Item 2 and the A/B numbers. (ii) Item 3's prefix-sum criterion. (iii) Item 4's \(g(t)\).
(iv) Items 6–8. (v) Item 11 completely. (vi) Item 12. (vii) The logistic Newton leaf in item 13.
(viii) Item 14 end to end, and item 15's weighted-squared-loss rewrite.

**Build — PY-11** (`mlf/trees/`).
- `cart.py`: `DecisionTreeClassifier`/`Regressor` (Gini/entropy/SSE; vectorised prefix-sum split search;
  `max_depth`, `min_samples_leaf`, `min_impurity_decrease`), `cost_complexity_path`, `prune(alpha)`.
- `bagging.py`: `Bagging(base, B)` with OOB predictions and OOB error.
- `forest.py`: `RandomForest(m_try)`, permutation importance on OOB.
- `adaboost.py`: `AdaBoost(stump, T)` recording \(\epsilon_t,\alpha_t,Z_t\).
- `gbm.py`: `GradientBoosting(loss in {squared, absolute, logistic}, nu, depth, subsample)`.
- `xgb.py`: `XGBLike(lambda_, gamma, eta, max_depth, min_child_weight, method in {exact, hist})` — second-order
  gains, leaf weights, histogram splits with `n_bins`, default direction for NaNs.
- Data: Friedman #1, \(y=10\sin(\pi x_1x_2)+20(x_3-0.5)^2+10x_4+5x_5+\varepsilon\), \(x\sim U[0,1]^{10}\) (Friedman 1991) — known truth,
  five irrelevant features.

**Accept.**
1. Property test: Gini and entropy decreases are \(\ge-10^{-12}\) on 10,000 random splits; the A/B example returns
   0.375 and 0.333.
2. Prefix-sum split search returns the same threshold and gain as brute force (to \(10^{-10}\)); runtime grows as
   \(n\log n\).
3. The pruning path is nested, and the CV-chosen \(\alpha\) beats the unpruned tree on noisy Friedman #1.
4. Mean OOB fraction over 1,000 bootstraps at \(n=1000\) is \(0.3677\pm0.003\).
5. Simulated correlated predictors reproduce \(\rho\sigma^2+(1-\rho)\sigma^2/B\) within Monte Carlo error. On a problem with many
   correlated features, measured inter-tree prediction correlation is lower for \(m_{\mathrm{try}}=\sqrt p\) than for
   bagging (\(m_{\mathrm{try}}=p\)), and so is test MSE.
6. AdaBoost with stumps: at every round, training error \(\le\prod_tZ_t=\frac1n\sum_ie^{-y_iF(x_i)}\) (equality to \(10^{-10}\)) \(\le e^{-2\sum\gamma_t^2}\).
7. A numerical line search on exponential loss reproduces \(\alpha_t\) to \(10^{-8}\).
8. `XGBLike` with squared loss and \(\lambda=\gamma=0\) makes the same splits and predictions as `GradientBoosting(squared)` to
   \(10^{-10}\); its reported \(\mathcal{L}^\star\) equals the objective recomputed from scratch.
9. Oracle: on Friedman #1 (\(n=5000\)), depth 3, \(\eta=0.1\), \(\lambda=1\), 200 rounds, `method="exact"`, your test RMSE is within
   5% of `xgboost` with `tree_method="exact"` and the same hyperparameters.
10. `method="hist"` with 64 bins loses \(<2\%\) RMSE against exact and is \(\ge5\times\) faster at \(n=10^5\).

**Exercises.** (a) Show that entropy's impurity decrease equals the empirical mutual information between
the split indicator and \(y\). (b) Derive gradient boosting for the Huber loss. (c) Show AdaBoost's weights put
exactly half the mass on the points \(h_t\) got wrong after the update — why the next weak learner must
differ.

**Text.** *ESL* **[free]** — **§9.2** (trees), **§8.7** (bagging), **Ch. 10** (§10.1 AdaBoost, §10.2–10.5 additive
models, forward stagewise, exponential loss, §10.9 boosting trees, §10.10 gradient boosting, §10.12
regularisation), **Ch. 15** (random forests), **Ch. 16** (ensemble learning). *ISL* 2e **[free]** — **Ch. 8**. Murphy
*PML1* **[free]** — **Ch. 18** (§18.1 CART, §18.3 bagging, §18.4 random forests, §18.5 boosting). Bishop *PRML*
**[free]** — **§14.2–14.4**. Shalev-Shwartz & Ben-David **[free]** — **Ch. 10** (boosting), **Ch. 18** (decision trees).
Mohri et al. **[free]** — **Ch. 7** (boosting). XGBoost documentation, *Introduction to Boosted Trees* **[free]** —
the item 14 derivation in the authors' notation.
**Depth.** Breiman, Friedman, Olshen & Stone, *Classification and Regression Trees* (1984) **[paid]**. Schapire &
Freund, *Boosting: Foundations and Algorithms* (MIT Press 2012) **[paid]** — Ch. 3 (minimising training error),
Ch. 5 (margins), Ch. 7 (loss minimisation). Louppe, *Understanding Random Forests* (PhD thesis;
arXiv:1407.7502) **[free]**. Biau & Scornet, "A Random Forest Guided Tour" (TEST 2016; arXiv:1511.05741)
**[free]**.
**Course.** Prathosh, NPTEL 106108841 Week 11. Cornell CS 4780 lecture notes **17** (*Decision trees*), **18**
(*Bagging*), **19** (*Boosting*). Berkeley CS 189 lectures **14** (*Decision trees, entropy*), **15** (*Ensembles, random
forests*), **24** (*AdaBoost*). NPTEL Sastry, *Statistical Pattern Recognition* — boosting and ensembles; NPTEL
Sarkar, *Introduction to ML* — decision trees.
**Papers.** Hyafil & Rivest, "Constructing Optimal Binary Decision Trees Is NP-Complete" (IPL 1976) ·
Quinlan, "Induction of Decision Trees" (Machine Learning 1986) · Schapire, "The Strength of Weak
Learnability" (Machine Learning 1990) · Friedman, "Multivariate Adaptive Regression Splines" (Ann. Stat.
1991; Friedman #1) · Breiman, "Bagging Predictors" (Machine Learning 1996) · Freund & Schapire, "A
Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting" (JCSS 1997) · Ho,
"The Random Subspace Method" (IEEE TPAMI 1998) · Schapire, Freund, Bartlett & Lee, "Boosting the Margin"
(Ann. Stat. 1998) · Friedman, Hastie & Tibshirani, "Additive Logistic Regression: A Statistical View of
Boosting" (Ann. Stat. 2000) · Breiman, "Random Forests" (Machine Learning 2001) · Friedman, "Greedy
Function Approximation: A Gradient Boosting Machine" (Ann. Stat. 2001) · Friedman, "Stochastic Gradient
Boosting" (CSDA 2002) · Strobl et al., "Bias in Random Forest Variable Importance Measures" (BMC
Bioinformatics 2007) · Chen & Guestrin, "XGBoost: A Scalable Tree Boosting System" (KDD 2016;
arXiv:1603.02754) · Ke et al., "LightGBM" (NeurIPS 2017) · Prokhorenkova et al., "CatBoost" (NeurIPS 2018;
arXiv:1706.09516) · Grinsztajn, Oyallon & Varoquaux, "Why Do Tree-Based Models Still Outperform Deep
Learning on Tabular Data?" (NeurIPS 2022; arXiv:2207.08815).
**Stop at.** CatBoost's ordered boosting, distributed XGBoost, oblique trees, BART.

---

### MLF-12 — Unsupervised learning and EM; a preview of generative models

**Week 12.** *Clustering: k-means, Gaussian mixtures, EM algorithm; dimensionality reduction and PCA. A
preview of generative models: GANs, VAEs, diffusion models (high-level).*
**Floor.** MLF-02 items 7, 9, 11–12; MLF-03 items 3, 7; PRE-P items 3–5; PRE-LA items 2–3; MLF-07 (autograd).

**Theory — \(k\)-means.**

1. **Lloyd's algorithm is block coordinate descent (derive).** \(J(\mu,z)=\sum_i\|x_i-\mu_{z_i}\|^2\). With \(\mu\) fixed, the
   optimal \(z_i\) is the nearest centre; with \(z\) fixed, \(\nabla_{\mu_k}J=0\) gives the cluster mean. Each half-step cannot
   increase \(J\) and there are finitely many partitions, so Lloyd terminates at a fixed point — a local, not
   global, optimum. Global \(k\)-means is NP-hard (even for \(k=2\) in general dimension).
2. **\(k\)-means++.** Seed the next centre with probability \(\propto D(x)^2\), the squared distance to the nearest chosen
   centre; then \(\mathbb{E}J\le8(\ln k+2)\,J_{\mathrm{opt}}\) (Arthur & Vassilvitskii 2007; statement). Choose \(k\) by elbow,
   silhouette or the gap statistic. Failure modes: non-spherical, unequal-size or unequal-density clusters —
   every one of which a GMM with full covariances handles.
3. **\(k\)-means as a limit of EM (derive).** For a GMM with shared, fixed covariance \(\sigma^2I\), responsibilities
   \(r_{ik}\propto\pi_ke^{-\|x_i-\mu_k\|^2/2\sigma^2}\to\mathbf{1}[k=\arg\min_j\|x_i-\mu_j\|]\) as \(\sigma^2\to0\): EM's steps become Lloyd's.

**Theory — Gaussian mixtures and EM.**

4. **Model.** \(z\sim\mathrm{Cat}(\pi)\), \(x\mid z=k\sim\mathcal{N}(\mu_k,\Sigma_k)\), so \(p(x)=\sum_k\pi_k\mathcal{N}(x\mid\mu_k,\Sigma_k)\). The log-likelihood
   \(\sum_i\log\sum_k\pi_k\mathcal{N}(x_i\mid\mu_k,\Sigma_k)\) is a log of a sum: no closed form. Optima come in \(K!\) label-permuted
   copies. **The MLE does not exist (derive):** put \(\mu_k=x_1\), \(\Sigma_k=s^2I\) and let \(s\to0\); that component's
   \(-\tfrac d2\log s^2\) term diverges while another component keeps every other point's likelihood bounded
   below. Fix by flooring \(\Sigma_k\succeq\epsilon I\) or by a MAP prior (MLF-03 item 7).
5. **EM in general (derive).** For any distribution \(q(z)\):
   \[
   \log p(x\mid\theta)=\underbrace{\mathbb{E}_q\Big[\log\frac{p(x,z\mid\theta)}{q(z)}\Big]}_{\mathcal{L}(q,\theta)}+\ D_{\mathrm{KL}}\big(q(z)\,\|\,p(z\mid x,\theta)\big).
   \]
   (Take \(\mathbb{E}_q\) of \(\log p(x)=\log p(x,z)-\log p(z\mid x)\), then add and subtract \(\log q\).) As KL \(\ge0\), \(\mathcal{L}\) is a lower bound —
   the **ELBO**. **E-step:** \(q\leftarrow p(z\mid x,\theta^{\text{old}})\), making the bound tight. **M-step:**
   \(\theta^{\text{new}}=\arg\max_\theta\mathbb{E}_q\log p(x,z\mid\theta)\) (the entropy of \(q\) does not depend on \(\theta\)). **Monotonicity (prove):**
   \(\log p(x\mid\theta^{\text{new}})\ge\mathcal{L}(q,\theta^{\text{new}})\ge\mathcal{L}(q,\theta^{\text{old}})=\log p(x\mid\theta^{\text{old}})\). EM is coordinate ascent on \(\mathcal{L}\); it reaches a
   stationary point under regularity (Wu 1983), at a linear rate that slows as components overlap.
   Generalised EM only needs the M-step to increase \(\mathcal{L}\); incremental EM updates one point at a time
   (Neal & Hinton 1998).
6. **EM for the GMM (derive the M-step).** E-step
   \(r_{ik}=\frac{\pi_k\mathcal{N}(x_i\mid\mu_k,\Sigma_k)}{\sum_j\pi_j\mathcal{N}(x_i\mid\mu_j,\Sigma_j)}\), computed as `exp(log_num - logsumexp)` (**M.NS**). With \(N_k=\sum_ir_{ik}\):
   \(\mu_k=\frac1{N_k}\sum_ir_{ik}x_i\); \(\Sigma_k=\frac1{N_k}\sum_ir_{ik}(x_i-\mu_k)(x_i-\mu_k)^\top\) (MLF-03 item 3, weighted); \(\pi_k=N_k/n\) (multiplier
   on \(\sum_k\pi_k=1\): \(N_k/\pi_k+\lambda=0\Rightarrow\lambda=-n\)). Variants: diagonal and tied covariances. Choose \(K\) by BIC
   \(=-2\ell+p\log n\) with \(p=(K-1)+Kd+Kd(d+1)/2\).

**Theory — PCA.**

7. **Maximum variance (derive).** Centred data, \(S=\frac1n\sum_ix_ix_i^\top\). \(\max_{\|u\|=1}u^\top Su\): the Lagrangian gives
   \(Su=\lambda u\) with variance \(\lambda\), so \(u\) is the top eigenvector; \(k\) orthonormal directions give the top-\(k\) eigenvectors
   and retained variance \(\sum_{i\le k}\lambda_i\) (PRE-LA item 2).
8. **Minimum reconstruction error — the same problem (derive).** For orthonormal \(U_k\),
   \(\|x-U_kU_k^\top x\|^2=\|x\|^2-\|U_k^\top x\|^2\), so \(\frac1n\sum_i\|x_i-U_kU_k^\top x_i\|^2=\mathrm{tr}\,S-\mathrm{tr}(U_k^\top SU_k)\). Minimising error =
   maximising retained variance, and the minimum is \(\sum_{i>k}\lambda_i\) — the B4 acceptance number, now derived.
   Via SVD of \(X/\sqrt n\): \(\lambda_i=\sigma_i^2\) (Eckart–Young, PRE-LA item 3).
9. **Computing it.** SVD of the centred \(X\), never an explicit \(X^\top X\) when \(d\) is large (**M.NS**). If \(n\ll d\), use the
   \(n\times n\) Gram matrix: \(XX^\top v=\lambda v\Rightarrow u=X^\top v/\|X^\top v\|\). Eigenvector signs are arbitrary — tests must be sign-
   invariant. Standardise when features have incomparable units. Whitening \(y=\Lambda_k^{-1/2}U_k^\top x\) has identity
   covariance. A linear autoencoder with squared loss learns the PCA subspace (Baldi & Hornik 1989) — the
   bridge to the VAE.
10. **Probabilistic PCA (Tipping & Bishop 1999).** \(z\sim\mathcal{N}(0,I_k)\), \(x=Wz+\mu+\varepsilon\), \(\varepsilon\sim\mathcal{N}(0,\sigma^2I)\), so
    \(x\sim\mathcal{N}(\mu,WW^\top+\sigma^2I)\) (PRE-P item 4). ML solution: \(W=U_k(\Lambda_k-\sigma^2I)^{1/2}R\) for any rotation \(R\), and
    \(\sigma^2_{\mathrm{ML}}=\frac1{d-k}\sum_{i>k}\lambda_i\) — the average discarded variance. As \(\sigma^2\to0\) the posterior-mean projection becomes
    PCA. EM for PPCA costs \(O(ndk)\) per iteration and handles missing entries. Factor analysis replaces
    \(\sigma^2I\) by a diagonal \(\Psi\).

**Theory — generative models (the course's "high-level" preview, with the three identities that make it
more than a picture).**

11. **Taxonomy.** Goal: \(p_\theta\approx p_{\text{data}}\), to sample and/or to evaluate densities. *Exact likelihood:*
    autoregressive models \(p(x)=\prod_jp(x_j\mid x_{<j})\) (MLF-10's decoder is one) and normalising flows
    (\(\log p_x(x)=\log p_z(f(x))+\log|\det\partial f/\partial x|\)). *Bound on likelihood:* VAEs and diffusion models. *Implicit:* GANs
    (a sampler, trained through a critic — MLF-02 item 11). The recurring trade-off is sample quality vs mode
    coverage vs sampling speed (Xiao et al. 2022).
12. **VAE (derive the ELBO, the KL term and the gradient estimator).** \(p_\theta(x)=\int p_\theta(x\mid z)p(z)\,dz\) with a
    neural decoder: the posterior is intractable, so item 5's E-step is impossible. Replace it with an
    **amortised** encoder \(q_\phi(z\mid x)=\mathcal{N}(\mu_\phi(x),\mathrm{diag}\,\sigma_\phi^2(x))\) and maximise item 5's bound:
    \[
    \mathcal{L}(\theta,\phi;x)=\mathbb{E}_{q_\phi(z\mid x)}[\log p_\theta(x\mid z)]-D_{\mathrm{KL}}\big(q_\phi(z\mid x)\,\|\,p(z)\big).
    \]
    Maximising over \(\phi\) minimises the **reverse** KL to the true posterior (mode-seeking, MLF-02 item 9); EM is
    the special case with exact \(q\). Closed form: \(D_{\mathrm{KL}}\big(\mathcal{N}(\mu,\sigma^2)\|\mathcal{N}(0,1)\big)=\tfrac12(\mu^2+\sigma^2-\log\sigma^2-1)\), summed over
    dimensions. **Reparameterisation:** \(z=\mu_\phi+\sigma_\phi\odot\epsilon\), \(\epsilon\sim\mathcal{N}(0,I)\), so
    \(\nabla_\phi\mathbb{E}_q[f(z)]=\mathbb{E}_\epsilon[\nabla_\phi f(\mu_\phi+\sigma_\phi\odot\epsilon)]\) — far lower variance than the score-function estimator
    \(\mathbb{E}_q[f(z)\nabla_\phi\log q_\phi(z)]\). A Bernoulli decoder gives binary cross-entropy reconstruction, a Gaussian one
    scaled MSE. Known pathologies: blurry samples, posterior collapse. The importance-weighted bound
    \(\mathcal{L}_K=\mathbb{E}\log\frac1K\sum_k\frac{p(x,z_k)}{q(z_k\mid x)}\) satisfies \(\mathcal{L}=\mathcal{L}_1\le\mathcal{L}_K\le\log p(x)\) (Burda et al. 2016).
13. **GAN (derive the optimal discriminator and the JS identity).**
    \(\min_G\max_DV=\mathbb{E}_{p_d}\log D(x)+\mathbb{E}_{z}\log(1-D(G(z)))\). For fixed \(G\) with density \(p_g\), maximise
    \(p_d\log D+p_g\log(1-D)\) pointwise: \(a\log y+b\log(1-y)\) peaks at \(y=\frac a{a+b}\), so \(D^\star=\frac{p_d}{p_d+p_g}\). Substituting and
    multiplying inside each log by \(\frac22\): \(C(G)=-\log4+2\,\mathrm{JS}(p_d\|p_g)\), minimised iff \(p_g=p_d\). This is MLF-02
    item 11 with the JS generator \(f\). **Non-saturating loss (derive):** with \(D=\sigma(a)\), \(\partial_a\log(1-\sigma(a))=-\sigma(a)\to0\) when
    the discriminator confidently rejects fakes, whereas \(\partial_a[-\log\sigma(a)]=-(1-\sigma(a))\to-1\); so train \(G\) on
    \(-\mathbb{E}\log D(G(z))\). **Why training is hard:** disjoint supports make JS constant at \(\log2\) (MLF-02 exercise c);
    mode collapse; and simultaneous gradient steps on even \(\min_x\max_yxy\) multiply the state by a matrix
    with eigenvalues \(1\pm i\eta\), modulus \(\sqrt{1+\eta^2}>1\) — an outward spiral (*derive*). WGAN swaps JS for
    Wasserstein-1 through a Lipschitz critic (Arjovsky et al. 2017; name). FID is the Fréchet distance
    between Gaussians fitted to network features:
    \(\|\mu_r-\mu_g\|^2+\mathrm{tr}\big(\Sigma_r+\Sigma_g-2(\Sigma_r\Sigma_g)^{1/2}\big)\).
14. **Diffusion (DDPM; derive the forward marginal and the \(\epsilon\)-form of the mean).** Forward:
    \(q(x_t\mid x_{t-1})=\mathcal{N}(\sqrt{\alpha_t}\,x_{t-1},(1-\alpha_t)I)\), \(\alpha_t=1-\beta_t\), \(\bar\alpha_t=\prod_{s\le t}\alpha_s\).
    *Marginal, by induction:* \(x_t=\sqrt{\alpha_t}(\sqrt{\bar\alpha_{t-1}}x_0+\sqrt{1-\bar\alpha_{t-1}}\,\epsilon')+\sqrt{1-\alpha_t}\,\epsilon_t\); independent Gaussian noises add
    variances \(\alpha_t(1-\bar\alpha_{t-1})+1-\alpha_t=1-\bar\alpha_t\), so \(q(x_t\mid x_0)=\mathcal{N}(\sqrt{\bar\alpha_t}\,x_0,(1-\bar\alpha_t)I)\), i.e.
    \(x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\,\epsilon\). *Reverse posterior* (PRE-P items 3–4):
    \(q(x_{t-1}\mid x_t,x_0)=\mathcal{N}(\tilde\mu_t,\tilde\beta_tI)\) with
    \(\tilde\mu_t=\frac{\sqrt{\bar\alpha_{t-1}}\beta_t}{1-\bar\alpha_t}x_0+\frac{\sqrt{\alpha_t}(1-\bar\alpha_{t-1})}{1-\bar\alpha_t}x_t\), \(\tilde\beta_t=\frac{1-\bar\alpha_{t-1}}{1-\bar\alpha_t}\beta_t\). *Substituting*
    \(x_0=(x_t-\sqrt{1-\bar\alpha_t}\,\epsilon)/\sqrt{\bar\alpha_t}\) gives \(\tilde\mu_t=\frac1{\sqrt{\alpha_t}}\big(x_t-\frac{\beta_t}{\sqrt{1-\bar\alpha_t}}\epsilon\big)\) — check the \(x_t\) coefficient:
    \(\frac{\beta_t+\alpha_t(1-\bar\alpha_{t-1})}{(1-\bar\alpha_t)\sqrt{\alpha_t}}=\frac1{\sqrt{\alpha_t}}\). So a network \(\epsilon_\theta(x_t,t)\) that predicts the noise defines the reverse
    mean, and the ELBO's Gaussian KL terms reduce (up to weights) to
    \(L_{\text{simple}}=\mathbb{E}_{t,x_0,\epsilon}\big\|\epsilon-\epsilon_\theta(\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\,\epsilon,\ t)\big\|^2\). Sampling: \(x_T\sim\mathcal{N}(0,I)\),
    \(x_{t-1}=\frac1{\sqrt{\alpha_t}}\big(x_t-\frac{\beta_t}{\sqrt{1-\bar\alpha_t}}\epsilon_\theta\big)+\sigma_tz\). *Score view:*
    \(\nabla_{x_t}\log q(x_t\mid x_0)=-\epsilon/\sqrt{1-\bar\alpha_t}\), so \(\epsilon_\theta\approx-\sqrt{1-\bar\alpha_t}\,\nabla\log q_t\) — denoising score matching (Vincent 2011),
    i.e. MLF-02 item 12's Fisher divergence; the SDE view unifies both (Song et al. 2021). Classifier-free
    guidance and latent diffusion: names only.

**Derive.** (i) Item 1. (ii) Item 4's degeneracy. (iii) Item 5's identity and monotonicity proof. (iv) Item 6's
three updates. (v) Items 7–8. (vi) Item 10's \(\sigma^2_{\mathrm{ML}}\) given \(W\)'s form. (vii) Item 12's KL and the reparameterised
gradient. (viii) Item 13's \(D^\star\), the \(-\log4+2\,\mathrm{JS}\) identity, the non-saturating gradients and the bilinear
spiral. (ix) Item 14's marginal and \(\epsilon\)-form mean.

**Build — PY-12** (`mlf/unsup/`, `mlf/gen/`).
- `kmeans.py`: vectorised Lloyd, `kmeanspp_init`, `n_init`, objective history.
- `gmm.py`: EM with `covariance_type in {full, diag, tied}`, log-space E-step, covariance floor, BIC,
  log-likelihood history.
- `pca.py`: SVD-based `PCA` (`explained_variance_`, `transform`, `inverse_transform`, `whiten`), Gram-trick path for
  \(n<d\). `ppca.py`: closed-form ML and EM with missing values.
- `vae.py`: MLP encoder/decoder on your PY-7 autograd; reparameterised sampling; analytic KL; `iwae_bound(K)`.
- `gan.py`: MLP generator and discriminator; saturating and non-saturating losses; the 2-D ring of 8 Gaussians.
- `ddpm.py`: linear \(\beta\) schedule \(10^{-4}\to0.02\), \(T=1000\); `q_sample`; an MLP \(\epsilon_\theta\) with sinusoidal time
  embedding (MLF-10 item 7); \(L_{\text{simple}}\) training; ancestral sampling; 2-D swiss roll and 8-Gaussians data.

**Accept.**
1. \(k\)-means: \(J\) never increases across half-steps (tolerance \(10^{-12}\)). On data built with a bad local
   optimum, \(k\)-means++ (one init) achieves lower mean \(J\) than uniform random seeding over 100 seeds.
2. GMM: log-likelihood non-decreasing every iteration (relative tolerance \(10^{-9}\)). From a known 3-component
   GMM with \(n=10^4\), recovered parameters (after permutation matching) are within 0.05 of the truth.
   Responsibilities stay finite with a component \(10^3\sigma\) away. With the floor removed, a duplicated point
   drives a component's log-likelihood to \(+\infty\) — observed, then prevented by the floor.
3. Shared fixed covariance \(\sigma^2I\) with \(\sigma^2\to0\): EM's hard assignments coincide with Lloyd's at every iteration.
4. PCA: mean reconstruction error equals \(\sum_{i>k}\lambda_i\) to \(10^{-10}\); SVD and eigen routes agree up to sign; the
   Gram-trick path matches at \(n=50\), \(d=5000\).
5. PPCA: closed-form \(\sigma^2_{\mathrm{ML}}\) equals the mean discarded eigenvalue; EM's log-likelihood converges to the
   closed-form maximum (relative \(10^{-6}\)); with 20% entries missing the largest principal angle to the true
   subspace is \(<5^\circ\).
6. VAE: analytic KL equals a \(10^5\)-sample Monte Carlo estimate within 1%; the reparameterised gradient's
   variance is at least \(10\times\) below the score-function estimator's on the same objective; averaged over held-out data,
   \(\hat{\mathcal{L}}_1\le\hat{\mathcal{L}}_5\le\hat{\mathcal{L}}_{100}\), each gap larger than two standard errors.
7. GAN: with the generator frozen on a 1-D problem with known densities, the trained discriminator matches
   \(p_d/(p_d+p_g)\) with mean absolute error \(<0.05\) on a grid; \(V(D^\star,G)\) evaluated numerically equals
   \(-\log4+2\,\mathrm{JS}\) to \(10^{-3}\). On 8-Gaussians, report modes covered (a mode counts if ≥1% of samples lie within
   \(3\sigma\)) for saturating vs non-saturating losses over 10 seeds. Simultaneous GD on \(xy\) grows the radius by
   exactly \(\sqrt{1+\eta^2}\) per step.
8. DDPM: forward samples at \(t\in\{1,T/2,T\}\) match mean \(\sqrt{\bar\alpha_t}x_0\) and variance \(1-\bar\alpha_t\) within Monte Carlo
   error; step-by-step simulation matches the closed-form marginal; \(\bar\alpha_T<10^{-4}\) for this schedule
   (\(\approx e^{-10}\)); the \(\epsilon\)-form mean equals \(\tilde\mu_t\) to \(10^{-12}\) when given the true \(\epsilon\). Trained on the swiss roll, samples
   have lower RBF-MMD (median-heuristic bandwidth) to held-out data than a single Gaussian fitted by MLE.

**Exercises.** (a) Derive EM for a mixture of Bernoullis. (b) Show that for PCA on standardised data the
components are eigenvectors of the correlation matrix, and give a dataset where standardising changes the
first component. (c) Show the VAE's ELBO gap equals \(D_{\mathrm{KL}}(q_\phi(z\mid x)\|p_\theta(z\mid x))\) and explain why a more flexible
encoder can only tighten it. (d) Derive \(\tilde\beta_t\) from PRE-P item 4.

**Text.** Bishop *PRML* **[free]** — **Ch. 9** (§9.1 K-means, §9.2 mixtures of Gaussians, §9.3 an alternative view
of EM, §9.4 EM in general), **Ch. 12** (§12.1 PCA, §12.2 probabilistic PCA). Deisenroth et al., *MML* **[free]** —
**Ch. 10** (PCA), **Ch. 11** (density estimation with GMMs). CS229 notes **[free]** — **Ch. 10** (k-means), **Ch. 11**
(EM: §11.1 mixture of Gaussians, §11.2 Jensen, §11.3 general EM and the ELBO, §11.5 variational inference and
the VAE), **Ch. 12** (PCA), **Ch. 14** (diffusion models, §14.1–14.4). Murphy *PML1* **[free]** — **§8.7** (bound
optimisation / EM), **§20.1** (PCA), **§20.3** (autoencoders, incl. VAEs), **§21.3–21.4** (k-means, mixture models).
Bishop & Bishop **[free online]** — **Ch. 15–17, 19–20** (discrete and continuous latent variables, GANs,
autoencoders, diffusion). Prince *UDL* **[free]** — **Ch. 14–18**.
**Depth.** Murphy, *Probabilistic Machine Learning: Advanced Topics* (PML2) **[free]** — the generative-model
part (VAEs, autoregressive models, flows, energy-based models, diffusion, GANs); it is the primary text of
Prathosh's own generative-AI course. Kingma & Welling, "An Introduction to Variational Autoencoders" (FnT ML
2019; arXiv:1906.02691) **[free]**. Goodfellow, "NIPS 2016 Tutorial: Generative Adversarial Networks"
(arXiv:1701.00160) **[free]**. Luo, "Understanding Diffusion Models: A Unified Perspective" (arXiv:2208.11970)
**[free]**. Nakkiran et al., "Step-by-Step Diffusion: An Elementary Tutorial" (arXiv:2406.08929) **[free]**. Blei,
Kucukelbir & McAuliffe, "Variational Inference: A Review for Statisticians" (JASA 2017; arXiv:1601.00670)
**[free]**. McLachlan & Krishnan, *The EM Algorithm and Extensions* 2e (Wiley 2008) **[paid]**. Jolliffe, *Principal
Component Analysis* 2e (Springer 2002) **[paid]**.
**Course.** Prathosh, NPTEL 106108841 Week 12; Prathosh, *Generative AI & Deep Learning* (IISc/NPTEL, Aug 2026
offering) and its GenAI lecture notes (links §10.7). Stanford **CS236** *Deep Generative Models* (Ermon) notes
**[free]**. MIT **6.S978** *Deep Generative Models* (Kaiming He, Fall 2024) **[free]**. Berkeley CS 189 lectures **20**
(*PCA*) and **21** (*SVD, clustering, k-means*). NPTEL Sastry, *Statistical Pattern Recognition* — mixture
densities and EM.
**Papers.** Pearson, "On Lines and Planes of Closest Fit" (Phil. Mag. 1901) · Hotelling (J. Educ. Psych. 1933) ·
Eckart & Young (Psychometrika 1936) · MacQueen (1967); Lloyd, "Least Squares Quantization in PCM" (IEEE TIT
1982) · Dempster, Laird & Rubin, "Maximum Likelihood from Incomplete Data via the EM Algorithm" (JRSS-B 1977) ·
Wu, "On the Convergence Properties of the EM Algorithm" (Ann. Stat. 1983) · Redner & Walker, "Mixture
Densities, Maximum Likelihood and the EM Algorithm" (SIAM Review 1984) · Baldi & Hornik (Neural Networks 1989) ·
Neal & Hinton, "A View of the EM Algorithm That Justifies Incremental, Sparse, and Other Variants" (1998) ·
Tipping & Bishop, "Probabilistic Principal Component Analysis" (JRSS-B 1999) · Arthur & Vassilvitskii,
"k-means++" (SODA 2007) · Halko, Martinsson & Tropp, "Finding Structure with Randomness" (SIAM Review 2011;
arXiv:0909.4061) · Vincent, "A Connection Between Score Matching and Denoising Autoencoders" (Neural
Computation 2011) · Kingma & Welling, "Auto-Encoding Variational Bayes" (ICLR 2014; arXiv:1312.6114) · Rezende,
Mohamed & Wierstra (ICML 2014; arXiv:1401.4082) · Goodfellow et al., "Generative Adversarial Nets" (NeurIPS 2014;
arXiv:1406.2661) · Sohl-Dickstein et al., "Deep Unsupervised Learning Using Nonequilibrium Thermodynamics"
(ICML 2015; arXiv:1503.03585) · Radford, Metz & Chintala, "DCGAN" (ICLR 2016; arXiv:1511.06434) · Burda, Grosse &
Salakhutdinov, "Importance Weighted Autoencoders" (ICLR 2016; arXiv:1509.00519) · Arjovsky, Chintala & Bottou,
"Wasserstein GAN" (ICML 2017; arXiv:1701.07875) · Gulrajani et al., "Improved Training of Wasserstein GANs"
(NeurIPS 2017; arXiv:1704.00028) · Heusel et al., "GANs Trained by a Two Time-Scale Update Rule" (FID; NeurIPS
2017; arXiv:1706.08500) · Song & Ermon, "Generative Modeling by Estimating Gradients of the Data Distribution"
(NeurIPS 2019; arXiv:1907.05600) · Ho, Jain & Abbeel, "Denoising Diffusion Probabilistic Models" (NeurIPS 2020;
arXiv:2006.11239) · Song et al., "Score-Based Generative Modeling Through Stochastic Differential Equations"
(ICLR 2021; arXiv:2011.13456) · Nichol & Dhariwal, "Improved DDPM" (ICML 2021; arXiv:2102.09672) · Dhariwal &
Nichol, "Diffusion Models Beat GANs on Image Synthesis" (NeurIPS 2021; arXiv:2105.05233) · Ho & Salimans,
"Classifier-Free Diffusion Guidance" (arXiv:2207.12598) · Rombach et al., "High-Resolution Image Synthesis with
Latent Diffusion Models" (CVPR 2022; arXiv:2112.10752) · Xiao, Kreis & Vahdat, "Tackling the Generative Learning
Trilemma" (ICLR 2022; arXiv:2112.07804) · Dinh, Sohl-Dickstein & Bengio, "Real NVP" (ICLR 2017; arXiv:1605.08803)
· Papamakarios et al., "Normalizing Flows for Probabilistic Modeling and Inference" (JMLR 2021;
arXiv:1912.02762).
**Stop at.** Flows, energy-based models, score-SDE theory, guidance and latent diffusion as names; no
image-scale training. The three identities in items 12–14 are the ceiling.

---
## 10.5 The PY build ladder, pacing, and the capstone

| Rung | Module | You build | Needs | Overlaps (parity-test if you did both) |
|---|---|---|---|---|
| **PY-0** | PRE-NP, §10.3 | `core/` numerics, `testing.grad_check`, `data/synthetic.py` | — | B0 |
| **PY-1** | MLF-01 | losses, finite-class ERM, bounds | PY-0 | B2 losses |
| **PY-2** | MLF-02 | Bayes rules, divergences, forward/reverse KL fits, NWJ estimator | PY-1 | — |
| **PY-3** | MLF-03 | Gaussian MLE/MAP, KDE with LOO-CV, \(k\)-NN density and classifier | PY-2 | B4 \(k\)-NN |
| **PY-4** | MLF-04 | QR/SVD least squares, LDA/QDA, Fisher, logistic (GD, IRLS), softmax | PY-3 | B2 OLS/logistic |
| **PY-5** | MLF-05 | ridge path, lasso (CD, FISTA), Bayesian linear regression, bias–variance simulator, LOOCV | PY-4 | — |
| **PY-6** | MLF-06 | kernels, SMO, Pegasos, kernel ridge, random features | PY-5 | — |
| **PY-7** | MLF-07 | perceptron, **autograd**, MLP, optimisers | PY-4 | B11 autodiff |
| **PY-8** | MLF-08 | conv/pool layers, LeNet/VGG/ResNet-mini, transfer learning | PY-7 | — |
| **PY-9** | MLF-09 | RNN/LSTM/GRU with hand BPTT, seq2seq | PY-7 | — |
| **PY-10** | MLF-10 | attention, encoder–decoder Transformer, attention-GRU | PY-9 | B11 transformer block |
| **PY-11** | MLF-11 | CART, pruning, bagging, random forest, AdaBoost, GBM, XGBoost-style | PY-1, PY-5 | B4 trees/GBT |
| **PY-12** | MLF-12 | \(k\)-means, GMM-EM, PCA/PPCA, VAE, GAN, DDPM | PY-3, PY-7 | B4 \(k\)-means/PCA |

**Order.** The course's week order is a valid topological order of this table. Two legal shortcuts:
PY-11 may follow PY-5 directly (trees need no autograd), and the PCA/GMM half of PY-12 may follow PY-5.
The generative half of PY-12 needs PY-7.

```
PY-0 → PY-1 → PY-2 → PY-3 → PY-4 → PY-5 ─┬→ PY-6
                                        ├→ PY-11
                                        └→ PY-12a (k-means, GMM, PCA)
                          PY-4 → PY-7 ─┬→ PY-8
                                       └→ PY-9 → PY-10
                                 PY-7 + PY-12a → PY-12b (VAE, GAN, DDPM)
```

**Pacing, honestly.** At the course's own pace — 12 weeks — plan on **12–15 hours a week**: ~3 h
lectures and notes, ~4 h derivations, ~6 h build and tests. That is only realistic if the §10.2
bridges are already closed. From a T.ProbStat/T.LA UG floor, budget **20–24 weeks**. The heaviest
modules are MLF-06 (SMO), MLF-07 (autograd), MLF-11 (XGBoost-style booster) and MLF-12 (three
generative models); give each two weeks if self-paced.

**Capstone — one problem, every model, honest comparison.**

1. **Tabular.** OpenML *adult* (id 1590). Nested cross-validation (MLF-05 item 11) over: \(k\)-NN, Parzen
   classifier, LDA, logistic regression (L2), linear and RBF SVM with Platt scaling, MLP, CART, random
   forest, AdaBoost, your XGBoost-style booster. Report accuracy, log-loss, AUC and ECE (M.ML), fit and
   predict time, and a one-page error analysis. State which result the MLF-11 item 16 prior predicted.
2. **Images.** Fashion-MNIST (OpenML 40996): MLP vs LeNet-5 vs mini-ResNet vs transfer from MNIST, each
   with the learning curve at 1%, 10% and 100% of the labels.
3. **Unsupervised.** PCA to 50-D, GMM with BIC-selected \(K\) on the Fashion-MNIST embeddings, and a 2-D-latent VAE
   whose latent map you colour by the (unused) true labels.
4. **Write-up rule.** Every claimed difference comes with a confidence interval or a paired test across
   folds; every surprise is traced back to a numbered **Theory** item or reported as unexplained.

**Assessment alignment.** The NPTEL run grades weekly assignments plus a proctored exam. The **Derive**
lists are exam preparation; the **Accept** lists are the coding assignments done properly.

---

## 10.6 Bibliography for Part 10

Chapter-level pointers live inside each module; this is the shelf. Tables of contents were checked
against the author/publisher pages on 2026-09-16 (CS229 notes: 2026 edition; *PML1*: long ToC; *D2L*,
*MML*: online ToC).

**Primary texts — free, author- or publisher-hosted.**

| Text | Modules | Why it is on the shelf |
|---|---|---|
| Deisenroth, Faisal & Ong, *Mathematics for Machine Learning* (Cambridge 2020) | PRE-*, 04, 06, 12 | Chs. 8–12 are this course's regression, PCA, GMM and SVM weeks, with the maths of Chs. 2–7 underneath |
| Bishop, *Pattern Recognition and Machine Learning* (Springer 2006) | 02–07, 11, 12 | the reference for decision theory, non-parametrics, Fisher, kernels, EM, PPCA |
| Murphy, *Probabilistic Machine Learning: An Introduction* (MIT Press 2022) | 01–05, 07, 08, 10–12 | modern, section-mapped in every module |
| Murphy, *Probabilistic Machine Learning: Advanced Topics* (MIT Press 2023) | 02, 12 | divergences, VAEs, GANs, diffusion; the instructor's generative-AI text |
| Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning* 2e | 01, 03–06, 11, 12 | shrinkage, boosting, trees, forests — the statistical view |
| James, Witten, Hastie, Tibshirani & Taylor, *ISL* 2e | 05, 11 | the gentle first pass |
| Shalev-Shwartz & Ben-David, *Understanding Machine Learning* | 01, 06, 07, 11 | ERM, PAC, VC, SVM, boosting, SGD, with proofs |
| Mohri, Rostamizadeh & Talwalkar, *Foundations of ML* 2e | 01, 06, 11 | margin bounds, kernels, boosting theory |
| Hastie, Tibshirani & Wainwright, *Statistical Learning with Sparsity* | 05 | the lasso, completely |
| Goodfellow, Bengio & Courville, *Deep Learning* | 05, 07–09, 12 | RNN chapter is still the clearest BPTT treatment |
| Prince, *Understanding Deep Learning* (MIT Press 2023) | 05, 07, 08, 10, 12 | best-drawn modern DL, incl. VAEs and diffusion |
| Bishop & Bishop, *Deep Learning: Foundations and Concepts* (Springer 2024) | 07, 08, 10, 12 | free online edition |
| Zhang, Lipton, Li & Smola, *Dive into Deep Learning* | 07–10 | from-scratch code beside every derivation |
| Stanford CS229 lecture notes (Ma & Ng, 2026) | 01, 03–07, 12 | kernels, SVM/SMO, EM/VAE and diffusion chapters |
| Boyd & Vandenberghe, *Convex Optimization* | PRE-CALC, 06 | duality and KKT |
| Bach, *Learning Theory from First Principles* (MIT Press 2024) | 01, 06 | modern learning theory and kernels |

**Depth — paid, enter only when the free text is exhausted.** Duda, Hart & Stork, *Pattern
Classification* 2e (Wiley 2001) — MLF-02/03/04 · Devroye, Györfi & Lugosi, *A Probabilistic Theory of
Pattern Recognition* (Springer 1996) — MLF-01/02/03 · Wasserman, *All of Nonparametric Statistics*
(Springer 2006) and Tsybakov, *Introduction to Nonparametric Estimation* (Springer 2009) — MLF-03 ·
Schölkopf & Smola, *Learning with Kernels* (MIT Press 2002) and Steinwart & Christmann, *Support Vector
Machines* (Springer 2008) — MLF-06 · Breiman, Friedman, Olshen & Stone, *Classification and Regression
Trees* (1984) and Schapire & Freund, *Boosting: Foundations and Algorithms* (MIT Press 2012) — MLF-11 ·
McLachlan & Krishnan, *The EM Algorithm and Extensions* 2e (Wiley 2008) and Jolliffe, *Principal
Component Analysis* 2e (Springer 2002) — MLF-12 · Nesterov, *Lectures on Convex Optimization* 2e
(Springer 2018) — MLF-07 · Trefethen & Bau, *Numerical Linear Algebra* (SIAM 1997) — MLF-04.

**Free tutorials and notes that earn their place.** Gretton, *RKHS lecture notes* (Gatsby/UCL) — MLF-06 ·
Wasserman, CMU 36-708 *Density Estimation* notes — MLF-03 · Dumoulin & Visin, convolution arithmetic —
MLF-08 · Olah, *Understanding LSTM Networks* — MLF-09 · Phuong & Hutter, *Formal Algorithms for
Transformers*; Rush et al., *The Annotated Transformer* — MLF-10 · XGBoost docs, *Introduction to Boosted
Trees* — MLF-11 · Kingma & Welling, *An Introduction to VAEs*; Goodfellow, *NIPS 2016 GAN tutorial*; Luo,
*Understanding Diffusion Models*; Nakkiran et al., *Step-by-Step Diffusion*; Stanford CS236 notes — MLF-12
· Petersen & Pedersen, *The Matrix Cookbook*; Parr & Howard, *The Matrix Calculus You Need for Deep
Learning* — PRE-LA · Bottou, Curtis & Nocedal; Bubeck; Baydin et al. — MLF-07.

Papers are listed per module; arXiv identifiers were checked against arXiv's API on 2026-09-16.

---

## 10.7 Course index and verified links for Part 10

**The source course.**

| Resource | Link |
|---|---|
| NPTEL 106108841 — *Mathematical Foundations of Machine Learning* (Prathosh A P, IISc) | https://nptel.ac.in/courses/106108841 |
| SWAYAM run `noc26_cs02` (enrolment, assignments, exam) | https://onlinecourses.nptel.ac.in/noc26_cs02/preview |
| YouTube playlist *Mathematical Foundations of Machine Learning* (linked from the instructor's course page) | https://www.youtube.com/playlist?list=PLgMDNELGJ1Cay-Q9Cn8KcpUcC58NDWuiu |
| Week-1 prerequisite videos (instructor's course page) | https://www.youtube.com/playlist?list=PLZ2ps__7DhBa5xCmncgH7kPqLqMBq7xlu |
| Instructor's course page (2026 offerings, notes, reading list) | https://prathosh.in/courses-2026.html |
| Instructor's *Math-ML* classical-ML notes (Google Drive PDF) | https://drive.google.com/file/d/1D3nY_5h9s91sfLq9m7RDoewQ9uAuXgEl/view |
| Instructor's GenAI lecture notes (Google Drive PDF) | https://drive.google.com/file/d/1Kebb00VehPBMyleuw2ubp2qbvrBqyvZZ/view |
| Instructor's teaching page (IISc E1 213 *PRNN*, E9 333 *ADRL*) | https://prathosh.in/teaching.html |

> The two Drive PDFs open only in a browser session; their contents were not machine-read for this
> file and are listed as the instructor's own material, not as verified chapter maps.

**IISc / IIT / NPTEL.**

| Course | Institution | Modules | Link |
|---|---|---|---|
| *Introduction to Statistical Pattern Recognition* (P. S. Sastry) — Bayes classifier, parametric and non-parametric density estimation, mixtures and EM, linear models, ERM and VC, neural nets, SVMs and kernels, boosting | IISc (NPTEL 117108048) | 01–07, 11, 12 | https://nptel.ac.in/courses/117108048 · syllabus https://archive.nptel.ac.in/content/syllabus_pdf/117108048.pdf |
| **E0 270** *Machine Learning* | IISc CSA | 01, 05, 06 | https://sml.csa.iisc.ac.in/Courses/Spring25/E0_270/JAN-2025.html |
| **E1 213** *Pattern Recognition and Neural Networks* (Prathosh) | IISc ECE | all | teaching page above |
| *Introduction to Machine Learning* (B. Ravindran) | IIT Madras (NPTEL 106106139) | 03–07, 11, 12 | https://nptel.ac.in/courses/106106139 · https://wsai.iitm.ac.in/~ravi/nptel-courses/intro-to-machine-learning/ |
| *Introduction to Machine Learning* (Sudeshna Sarkar) | IIT Kharagpur (NPTEL 106105152) | 03, 04, 06, 07, 11 | https://nptel.ac.in/courses/106105152 |
| **CS6910/CS7015** *Deep Learning* (Mitesh Khapra) | IIT Madras | 07–10 | https://www.cse.iitm.ac.in/~miteshk/CS6910.html |
| **CS 725** *Foundations of Machine Learning* | IIT Bombay | 04–06 | https://www.cse.iitb.ac.in/~sunita/cs725/ |

**Ivy League.**

| Course | Modules | Link |
|---|---|---|
| Cornell **CS 4780** (Weinberger) — lecture notes 1–21 cited by number in the modules | 01, 03–07, 11 | https://www.cs.cornell.edu/courses/cs4780/2018fa/lectures/ |
| Columbia **COMS 4771** *Machine Learning* (Hsu) | 01, 04–06 | https://www.cs.columbia.edu/~djhsu/ML/ |
| Harvard **CS 181** *Machine Learning* | 03, 04, 12 | https://harvard-ml-courses.github.io/cs181-web-2024/ |
| Princeton **COS 324** *Introduction to Machine Learning* | 04, 07 | https://princeton-introml.github.io/ |
| Brown **CSCI 1420** *Machine Learning* | 01, 04–06 | https://cs.brown.edu/courses/csci1420/ |
| Penn **CIS 5200** *Machine Learning* | 01, 05 | https://machine-learning-upenn.github.io/ |

**Peer institutions.**

| Course | Modules | Link |
|---|---|---|
| Stanford **CS229** — main notes (2026) | 01, 03–07, 12 | https://cs229.stanford.edu/main_notes.pdf |
| Stanford CS229 — simplified SMO handout | 06 | https://cs229.stanford.edu/materials/smo.pdf |
| Berkeley **CS 189/289A** (Shewchuk) — lecture notes 1–25 cited by number | 01–08, 11, 12 | https://people.eecs.berkeley.edu/~jrs/189/ |
| MIT **6.790** *Machine Learning* (graduate) | 01–06 | https://gradml.mit.edu/ |
| CMU **10-715** *Advanced Introduction to ML* | 01, 06, 11 | https://www.cs.cmu.edu/~10715-f18/ |
| CMU **36-708** *Statistical Machine Learning* (Tibshirani) | 01, 03, 05 | https://www.stat.cmu.edu/~ryantibs/statml/ |
| CMU **11-785** *Introduction to Deep Learning* | 07–10 | https://deeplearning.cs.cmu.edu/ |
| Stanford **CS231n** — notes: *Convolutional Networks*, *Transfer Learning* | 08 | https://cs231n.github.io/convolutional-networks/ · https://cs231n.github.io/transfer-learning/ |
| Stanford **CS224n** | 09, 10 | https://web.stanford.edu/class/cs224n/ |
| Stanford **CS236** *Deep Generative Models* — notes | 02, 12 | https://deepgenerativemodels.github.io/notes/index.html |
| MIT **6.S978** *Deep Generative Models* (Kaiming He, 2024) | 12 | https://mit-6s978.github.io/ |

**Texts, notes and data.**

| Resource | Link |
|---|---|
| Deisenroth, Faisal & Ong, *MML* (PDF) | https://mml-book.com/book/mml-book.pdf |
| Murphy, *PML1* (PDF) / *PML2* | https://github.com/probml/pml-book/releases/latest/download/book1.pdf · https://probml.github.io/pml-book/book2.html |
| Bishop & Bishop, *Deep Learning: Foundations and Concepts* | https://www.bishopbook.com/ |
| Shalev-Shwartz & Ben-David (PDF) | https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf |
| Hastie, Tibshirani & Wainwright, *Statistical Learning with Sparsity* | https://hastie.su.domains/StatLearnSparsity/ |
| Bach, *Learning Theory from First Principles* (PDF) | https://www.di.ens.fr/~fbach/ltfp_book.pdf |
| Boyd & Vandenberghe (PDF) | https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf |
| Gretton, RKHS course notes | https://www.gatsby.ucl.ac.uk/~gretton/coursefiles/rkhscourse.html |
| Wasserman, *Density Estimation* notes (PDF) | https://www.stat.cmu.edu/~larry/=sml/densityestimation.pdf |
| Graves, *Supervised Sequence Labelling with RNNs* (preprint PDF) | https://www.cs.toronto.edu/~graves/preprint.pdf |
| Olah, *Understanding LSTM Networks* | https://colah.github.io/posts/2015-08-Understanding-LSTMs/ |
| *The Annotated Transformer* | https://nlp.seas.harvard.edu/annotated-transformer/ |
| XGBoost, *Introduction to Boosted Trees* | https://xgboost.readthedocs.io/en/stable/tutorials/model.html |
| Breiman, "Random Forests" (PDF) / "Bagging Predictors" (PDF) | https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf · https://www.stat.berkeley.edu/~breiman/bagging.pdf |
| Hochreiter & Schmidhuber, "LSTM" (PDF) | https://www.bioinf.jku.at/publications/older/2604.pdf |
| Arthur & Vassilvitskii, "k-means++" (PDF) | https://theory.stanford.edu/~sergei/papers/kMeansPP-soda.pdf |
| Neal & Hinton, "A View of the EM Algorithm" (PDF) | https://www.cs.toronto.edu/~hinton/absps/emk.pdf |
| Tipping & Bishop, "Probabilistic PCA" (PDF) | https://www.robots.ox.ac.uk/~cvrg/hilary2006/ppca.pdf |
| Rahimi & Recht, "Random Features" (PDF) | https://people.eecs.berkeley.edu/~brecht/papers/07.rah.rec.nips.pdf |
| Chang & Lin, "LIBSVM" (PDF) | https://www.csie.ntu.edu.tw/~cjlin/papers/libsvm.pdf |
| Friedman, "Greedy Function Approximation" (Ann. Stat.) | https://projecteuclid.org/journals/annals-of-statistics/volume-29/issue-5/Greedy-function-approximation-A-gradient-boosting-machine/10.1214/aos/1013203451.full |
| Friedman, Hastie & Tibshirani, "Additive Logistic Regression" (Ann. Stat.) | https://projecteuclid.org/journals/annals-of-statistics/volume-28/issue-2/Additive-logistic-regression--a-statistical-view-of-boosting-With/10.1214/aos/1016218223.full |
| Friedman, Hastie & Tibshirani, "Regularization Paths via Coordinate Descent" (JSS) | https://www.jstatsoft.org/article/view/v033i01 |
| Dempster, Laird & Rubin, "EM" (JSTOR) | https://www.jstor.org/stable/2984875 |
| *The Matrix Cookbook* (PDF) | https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf |
| Parr & Howard, *Matrix Calculus for Deep Learning* | https://explained.ai/matrix-calculus/ |
| NumPy — broadcasting; `sliding_window_view` | https://numpy.org/doc/stable/user/basics.broadcasting.html · https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html |
| Karpathy, `micrograd` (read after PY-7) | https://github.com/karpathy/micrograd |
| MNIST (OpenML 554) · Fashion-MNIST (OpenML 40996) · adult (OpenML 1590) | https://www.openml.org/d/554 · https://www.openml.org/d/40996 · https://www.openml.org/d/1590 |
| Tiny Shakespeare (char-rnn) | https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt |
| arXiv papers | `https://arxiv.org/abs/<id>` for every identifier given in §10.4 |

---

# Provenance and limits

**Sources.** The 309 one-liners in Part 1 are the Engineer1999 catalog, linked at the top of
that part. Everything else is either authored here or a public book, paper or course linked in
§8.8, §9.3, §9.4 or §10.7. Part 10's topic list is the course plan of NPTEL 106108841
(*Mathematical Foundations of Machine Learning*, Prathosh A P, IISc; course PDF dated Nov–Dec 2025);
its derivations are authored here from the texts cited per module. **This file has no external
dependency and no companion document.**

**What has not been done — read this before trusting the file.**

- Course numbers and terms drift. Every link was checked 2026-09-16; the *artifacts* (books,
  notes, booksites) are durable, the *course numbers* are search keys. Ivy League numbering in
  §9.1 is the least stable part of this file — §9.2 and §9.3 are better verified.
- **Coverage is per-family, not per-study.** Part 6 gives twelve builds, not 309 runbooks.
  §2.2 states exactly what is and is not claimed.
- **Parts 1–9 name no datasets.** Every build there says what to compute, not what to compute it
  on. Synthetic data is specified where an acceptance test needs known ground truth. **Part 10 is
  the exception**: it names MNIST, Fashion-MNIST, *adult* (OpenML) and Tiny Shakespeare for four
  acceptance items and the capstone, because CNN, sequence-model and tabular benchmarks have no
  honest synthetic substitute; everything else in Part 10 still runs on synthetic ground truth.
- **Part 6's and Part 10's acceptance tests are specified but not executed.** No code implements
  them yet. Part 10's numeric targets (e.g. \(\Phi(-1)\approx0.1587\), \(\tfrac16\), \(e^{-1}\), \(12d^2+13d\)) are derived in
  the text; the empirical thresholds (accuracies, tolerances) are calibrated judgements, and a
  learner who misses one should first check the threshold against the stated theory before
  doubting the code.
- **Part 10's chapter pointers** were checked against published tables of contents (CS229 2026
  notes, *PML1* long ToC, *D2L*, *MML*, Cornell CS 4780 and Berkeley CS 189 lecture lists) and its
  arXiv identifiers against the arXiv API, all on 2026-09-16. Paid books' section numbers
  (Duda–Hart–Stork, Schölkopf–Smola, Schapire–Freund) are given at chapter level where they could
  not be checked against the book itself. The instructor's two Google Drive note PDFs are linked
  but were not machine-read.
- **§3.3's T.SysTheory is cut to the 309, not to a systems syllabus.** CIDR arithmetic,
  subnetting, L2-vs-L3 and the general cryptography sequence are deliberately absent: no study
  in Part 1 needs them. Privacy, adversarial ML and storage layout are present because many
  studies do. If you want a general systems or security education, §8.2, §8.3 and §8.6 are the
  shelf — this file teaches only what a case study forces.
- **Tier 0 (§3.0) is a route, not a course.** It points at Khan Academy and OpenStax rather
  than teaching arithmetic itself, which would be a different and much longer document.
- No excluded host (Scribd, Z-Library, LibGen, Sci-Hub, Internet Archive full-text, epdf.pub,
  PDF Drive, dokumen.pub) is used as a source or linked anywhere above. Scribd appears in
  Part 1 only as a company name inside the carried catalog.
