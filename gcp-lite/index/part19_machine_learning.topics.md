# Part 19 · Machine Learning, MLOps & Production ML System Design · TOPIC LIST

Rules and directives for this part: `index/part19_machine_learning.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Machine Learning, MLOps & Production ML System Design

### Foundations of AI

- **History and definitions**: the Dartmouth workshop (1956); the Turing test; four views of AI (thinking or acting, humanly or rationally); symbolic AI (logic, rules, semantic networks, expert systems); the AI winters and why rule systems failed; learning from data instead of hand-written rules; Mitchell's definition (experience E, task T, performance measure P)
- **Data types**: categorical (nominal), ordinal and continuous features; structured versus unstructured data
- **The supervised workflow**: problem first, then data, split, fit, predict and evaluate

### Classical machine learning

- **Learning paradigms**: supervised, unsupervised and reinforcement learning; regression, classification and clustering, and when to use which
- **Learning theory**
  - Empirical risk minimization
  - The bias–variance decomposition of squared error (bias² + variance + irreducible noise); overfitting and underfitting
  - Regularization as a constraint: ridge (L2, a circular constraint region, closed-form solution, shrunken weights) and lasso (L1, a diamond-shaped region whose corners give sparse weights, fitted by coordinate descent); polynomial features with ridge in one pipeline
  - Maximum likelihood; minimizing cross-entropy as maximum likelihood for a classifier
  - Train, validation and test splits; cross-validation as an estimator with its own variance; the test set touched once
  - Splits that give an honest estimate: transforms fitted on the training split only; stratified splits for skewed classes; time-based splits for temporal data; group-aware splits keeping one user, patient or device on one side; near-duplicates removed across splits
  - Generalization from a test set: Hoeffding's bound P(|test error − true error| > ε) ≤ 2e^(−2mε²) for a fixed classifier; reusing a test set for model selection spends its guarantee
- **Linear models**
  - Least squares: minimizing ‖Xθ − y‖²; normal equations XᵀXθ = Xᵀy; convexity and convergence of gradient descent
  - Logistic regression with cross-entropy loss; generalized linear models
- **Other supervised models**: k-nearest neighbours; naive Bayes; linear and quadratic discriminant analysis; support vector machines and margins; class weights
- **Trees and ensembles**: decision trees and impurity (Gini, entropy); CART; random forests; gradient boosting and boosted stumps; feature importance; monotonic constraints
- **Unsupervised learning and anomaly detection**: k-means; DBSCAN; Gaussian mixtures fitted by expectation–maximization; association rules (support, confidence, lift); robust statistics (z-score, median absolute deviation); isolation forests; reconstruction-error anomaly scores
- **Dimensionality reduction**: the curse of dimensionality; PCA to compress features, with components chosen by explained variance; t-SNE for visualization only
- **Evaluation**
  - The confusion matrix; accuracy and why it misleads on imbalanced data (base rates)
  - Precision, recall, F1, macro-F1 for multiclass problems; choosing precision or recall by the cost of false positives against false negatives
  - ROC curves and AUC as the probability a random positive outranks a random negative; PR curves and PR-AUC
  - Calibration and reliability bins
  - Ranking measures: precision@k, recall@k, MAP, MRR, nDCG@k = DCG@k ÷ IDCG@k
  - Forecast errors: MAE, percentage errors and their instability near zero, interval coverage
  - Business guardrail metrics beside model metrics
- **Feature engineering**
  - Scaling and normalization; encoding categoricals; the hashing trick; target encoding with time-aware folds
  - Missing values; imbalanced datasets (SMOTE, class weighting, focal loss, negative sampling) and the accuracy paradox, where always predicting the majority class scores high and detects nothing
  - Text, time, window, session and graph features
  - Schema validation and golden tests for feature pipelines

### Deep learning

- Biological and artificial neurons; the perceptron and its limit to linearly separable data (XOR); multilayer perceptrons; width versus depth
- Activation functions: step, sigmoid, tanh, ReLU, softmax; the forward pass
- Loss functions: mean squared error for regression, cross-entropy for classification
- Tensors and computational graphs
- Backpropagation as reverse-mode automatic differentiation over the computation graph; its cost as a small multiple of the forward pass; gradient checking by finite differences
- Vanishing and exploding gradients; residual connections; batch and layer normalization
- Optimizers: batch, mini-batch and stochastic gradient descent, momentum, RMSProp, Adam; learning-rate schedules
- **Learning-rate schedules**: large steps early and small steps late; four knobs (warmup length, peak rate, decay shape, floor); linear warmup from near zero; constant, linear decay, cosine decay, step decay and reduce-on-plateau, cosine with restarts, and warmup–stable–decay for runs of unknown length; lengthening warmup and lowering the peak before changing the shape
- **Training instability**: loss spikes, gradient explosion and divergence as one feedback loop (an oversized update raises the loss, which enlarges the next gradient); sharp minima, outlier batches and depth as causes; gradient-norm clipping that rescales to a cap and keeps the direction, with the pre-clip norm logged; float16 overflow near 65,504 turning into Inf and NaN, and bfloat16 as the remedy; alerts on the gradient norm; checkpoints every N steps
- **Batch size**: effective batch = micro-batch × gradient-accumulation steps × devices; filling device memory, then accumulating; small batches (noisy gradients, more updates, often better generalization) versus large ones (stable gradients, higher throughput, fewer updates); the linear scaling rule tying learning rate to effective batch; too few optimizer steps showing as underfitting
- **Reading loss curves**: both losses high and flat early (underfitting); training loss falling while validation loss turns up (overfitting); both flat at the starting value (nothing is updating); persistent jitter (batch too small or rate too high); both falling with a small stable gap (healthy), checkpointed at the validation minimum
- Initialization that preserves activation variance: Glorot (Xavier) initialization Var(w) = 2 ÷ (n_in + n_out); He initialization Var(w) = 2 ÷ n_in for ReLU units
- Regularization in deep networks: weight decay, dropout, data augmentation, early stopping with patience
- Architecture as inductive bias: convolutions sharing one kernel across positions, so parameter count is independent of image size; CNNs for images
- Sequence models before attention: RNNs and LSTMs; encoder–decoder (sequence-to-sequence) models and their fixed-length context bottleneck; weak long-range dependencies; no parallelism across time steps; Bahdanau (additive) attention over encoder states

### Natural language processing foundations

- NLP as the interface between people and software; tasks (classification, named entities, translation, summarization, question answering)
- The classical pipeline: cleaning and Unicode normalization, tokenization, stop-word removal, stemming and lemmatization, feature extraction, a classifier
- Representations: one-hot vectors and bag of words and their limits (sparsity, lost word order, no semantics, out-of-vocabulary words, orthogonal vectors for related words); n-gram features; TF-IDF weighting tf × log(N ÷ df)
- Distributional semantics: meaning from context windows; dense static embeddings (Word2Vec skip-gram and CBOW with negative sampling, GloVe); vector analogies; contextual embeddings (ELMo) and then transformers
- Limits of classical NLP, and the progression from rules to statistical models, deep learning, LLMs and agents

### Machine learning in Python

- scikit-learn: the estimator API (`fit`, `transform`, `predict`); `Pipeline` and `ColumnTransformer`; `StandardScaler`, `MinMaxScaler`, `OneHotEncoder`, `SimpleImputer`, `PolynomialFeatures`; `train_test_split`, `cross_val_score`, `GridSearchCV`, `RandomizedSearchCV`; metrics and classification reports
- PyTorch: tensors and autograd; `nn.Module` with `Linear`, `Embedding`, `Dropout`, `LayerNorm`; loss functions and optimizers; the training loop (forward, loss, backward, step, zero gradients); evaluation mode; devices
- NLTK for tokenizers, stop words, stemmers and lemmatizers

### Specialised learning areas

- **Reinforcement learning**: Markov decision processes, value functions, policy gradients, PPO
- **Graph learning**: PageRank, random walks and random-walk embeddings, bipartite graphs, label propagation, node and edge anomaly scores, graph neural networks
- **Entity resolution**: blocking, candidate generation, pairwise matching
- **Computer vision**: pixels and image representation, 2D convolution and image filters, image embeddings, perceptual hashing, OCR and document extraction, segmentation; vision at research depth
- **Audio and speech**: audio frames, windowing, spectrograms and MFCCs, word error rate per locale; speech at research depth
- **Multimodal retrieval** across text, image and audio embeddings
- **Contrastive (metric) learning** for retrieval; on-device models bounded by memory, power and privacy
- **Operations research**: linear and integer programming, assignment, constrained scheduling; forecasts as inputs to capacity, pricing and dispatch constraints
- **Game theory and auctions**: equilibria; second-price and generalized second-price auctions; incentive compatibility; mechanism design
- **Click models**: deep click-rate models and click-model research

### Applied problem families

- **Problem framing**: prediction, ranking, retrieval, generation and optimization problems; the target action, labels, input entities, metric and failure modes; cold start; feedback loops; delayed labels
- **The case-study method**: problem and business measure → data and labels (implicit, explicit, delayed, weak) → leakage against what is known at decision time → derived metric or estimator → offline evaluation → serving (batch or online) and latency budget → monitoring, rollback and retraining → cost → a named company's design read against the same steps
- **Leakage and point-in-time correctness**: as-of joins; leakage, training–serving skew and online–offline feature drift as three distinct failures; one feature definition for both paths with a parity test
- **Recommendation and feeds**
  - Candidate generation (two-tower retrieval, approximate nearest neighbours, judged by recall@k) separated from ranking and re-ranking
  - Collaborative filtering (item–item), matrix factorization
  - Diversity, coverage and multiple objectives; popularity feedback loops; catalogue coverage
  - Labels from impressions, plays, dwell and hides; leakage from future popularity and same-session targets
- **Search, learning to rank and ads**
  - Inverted indexes, BM25, semantic and hybrid retrieval with rank fusion
  - Learning to rank: pointwise, pairwise and listwise; sampled pairs
  - Position bias: the position-based click model; inverse-propensity scoring (Horvitz–Thompson) unbiased under positivity; propensity clipping trading bias for variance; propensities from randomized slices; off-policy evaluation of a new ranker from old logs
  - Ads ranked by bid × predicted quality; calibrated click and conversion rates
  - Wide & deep models: memorized feature crosses plus generalizing embeddings
- **Explore and exploit**
  - The K-armed bandit; regret R_T = Tμ* − E[Σ rₜ]
  - Greedy lock-in; ε-greedy's linear regret; UCB1 (x̄ᵢ + √(2 ln t ÷ nᵢ)) and Thompson sampling with logarithmic regret; the Lai–Robbins lower bound
  - Contextual and cascade bandits; offline replay evaluation; policy constraints
  - A/B test versus bandit versus feature flag
- **Forecasting, ETA, demand and availability**
  - Trend, seasonality and holiday decomposition; moving averages, exponential smoothing, autoregressive intuition; backtesting
  - Covariates as known at forecast time; censored observations
  - The pinball (quantile) loss L_τ and why its minimizer is the τ-quantile; prediction intervals judged by coverage and width together
  - Availability probabilities, calibration and the cost of a false "in stock"
- **Fraud, abuse, risk and trust and safety**
  - Cost-weighted thresholds: flag when p > C_FP ÷ (C_FP + C_FN); expected cost C_FP·FP + C_FN·FN as the measure
  - Review-queue capacity setting the threshold; recall at a fixed false-positive rate
  - Weak, delayed (chargeback) and semi-supervised labels
  - Fraud rings as connected components of shared-device and shared-card graphs
  - Synchronous scoring beside an asynchronous review queue; fail-open versus fail-closed decisions
  - Adversarial drift
- **Language and support**
  - Ticket routing and classification; macro-F1 and misroute cost; handle time and deflection
  - Sequence labelling scored by entity-level F1
  - Grammatical error correction as structured prediction
  - Suggested replies sent by a human; masking personal data before a model sees text
- **Vision, documents and speech in production**: buying a perception API versus building a model; batch versus GPU-endpoint serving; near-duplicate leakage across splits; mean average precision; image search with batch embedding and an online nearest-neighbour index
- **Marketing, churn, lifetime value and notifications**
  - Potential outcomes; randomization versus confounding; average and segment (uplift) effects; targeting the persuadable
  - Holdouts and incremental lift instead of raw click rate
  - Survival analysis and churn hazard; censoring
  - Customer lifetime value: CLV = m r ÷ (1 + d − r) for constant retention r, margin m and discount rate d
  - Lookalike audiences; send time under frequency caps; notification fatigue
- **Causal inference**: causal graphs, instrumental variables, difference in differences, synthetic control; propensity weighting; observational bias
- **Marketplace pricing** as an applied family

### MLOps

- The ML lifecycle: data → features → training → evaluation → deployment → monitoring → retraining
- **Technical debt in ML systems**: entanglement; hidden feedback loops; undeclared consumers; data dependencies; glue code and pipeline jungles; the model as a small part of the system
- **Data and feature platforms**: event contracts; batch versus streaming features; freshness and backfills; point-in-time correctness; schema evolution; feature stores with online and offline parity; fresh features streamed from user-action and inventory events; per-entity features cached with a TTL
- **Training pipelines**: dataset snapshots and versions; reproducible training (pinned data, code, environment, seeds); experiment tracking; hyperparameter search; model registries with lineage, aliases and approval status; model cards
- **Production readiness**: the ML Test Score rubric across data, model, infrastructure and monitoring
- **CI/CD/CT**: continuous training; continuous evaluation triggered from CI
- **Serving architectures**: online, batch, near-real-time, embedded, sidecar and asynchronous inference; caches, fallbacks and timeout budgets; batch scores delivered by schedulers and task queues
- **Experimentation and rollout**: A/B tests as two-sample hypothesis tests; holdouts; assignment bucketing and exposure logs; bootstrap intervals; segment analysis; metric guardrails; shadow, canary and ramp deployments of models as a dial separate from the application canary; rollback gates
- **Monitoring and drift**
  - Covariate shift (P(x) changes), prior or label shift (P(y) changes) and concept drift (P(y | x) changes)
  - Two-sample detection: the Kolmogorov–Smirnov statistic D = supₓ |F₁(x) − F₂(x)|; the population stability index PSI = Σ (aᵢ − eᵢ) ln(aᵢ ÷ eᵢ) and its conventional 0.1 and 0.25 thresholds
  - Training–serving skew as a pipeline defect that retraining does not fix
  - Calibration drift; data-quality and freshness checks; a written retraining policy; incident runbooks
- **Governance and responsible ML**: privacy and PII minimization; consent, retention and deletion; bias and fairness; explanations; human-in-the-loop review and human override; audit logs; non-destructive, undoable AI actions; abuse resistance and red-team tests; data-loss prevention on logs
- **Scale and cost**: hot keys and fan-out; approximate retrieval; request batching; concurrency limits; accelerators as remote services; cost per prediction and per successful decision; cost at ten times the traffic
- **ML platforms**: shared features, training, registry, serving and monitoring across teams; platform-enforced point-in-time joins; measured by time to train, failed deploys, skew incidents and cost per training hour

### Exercises

- From scratch in Go: a metrics library and evaluator CLI; linear and logistic regression with gradient checks; a CART tree and boosted stumps; k-means, a robust anomaly detector and a Gaussian-mixture EM trainer; BM25, item–item collaborative filtering, matrix factorization, exact k-NN with heap top-k, a pairwise ranker and a diversity re-ranker; a tokenizer, TF-IDF and edit distance; image convolution filters, a perceptual hash and spectral audio features; entity-resolution blocking, PageRank and random-walk embeddings; forecast baselines with backtests and an assignment scheduler; a bandit simulator with offline replay and propensity weighting; a tiny tensor type, an MLP forward and backward pass, optimizer variants (SGD, momentum, RMSProp, Adam), dropout and batch normalization
- From scratch: a perceptron failing on XOR and a two-layer network solving it; PCA by power iteration; a Word2Vec skip-gram trainer with negative sampling and analogy tests
- A breast-cancer classifier in scikit-learn: a scaled logistic-regression pipeline, cross-validated tuning and a confusion-matrix report, then a polynomial-ridge regression showing L1 against L2
- A text classifier comparing an NLTK and TF-IDF pipeline with sentence embeddings
- A ranker for a shop's home page and search: sampled negatives, cold-start flags, time-aware target encoding, recall@k and nDCG@k, an exploration policy, a CPU ranker served online with skew and latency monitoring
- A delivery-ETA window: quote-time features only, a quantile model fitted by gradient descent from scratch, coverage against width, residual bias by city and hour
- Fraud scoring on payment tokens: delayed chargeback labels, a cost- and capacity-set threshold, a synchronous score with a timeout and a review queue, chargebacks returned as labels
- A published ML system design redone end to end: metric derived, leakage risks listed, cost at ten times the traffic
- A feature-store facade over PostgreSQL and Redis with online and offline parity tests
- A local trainer and evaluator CLI writing artifacts, metrics, lineage and approval status
- A model served over REST and gRPC with cache, fallback, shadow mode and latency SLOs
- An experiment service: assignment bucketing, exposure logs, a CUPED and bootstrap report, a rollback gate
- A drift detector with OpenTelemetry metrics, data-quality alerts and a runbook drill
- Governance tooling: policy checks, red-team tests, reversible actions, an audit log and a review-dashboard API
- A batching, rate-limiting and caching layer comparing exact and approximate retrieval, with cost per successful decision
- **Reasoning drills**
  - Predict the bias–variance effect of a model change before training it
  - Derive a loss gradient by hand and check it numerically
  - Find the leakage in a feature set before training
  - Reproduce one result of a classic machine-learning paper at toy size and critique its evaluation
