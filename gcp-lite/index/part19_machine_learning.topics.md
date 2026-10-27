# Part 19 · Machine Learning, MLOps & Production ML System Design · TOPIC LIST

Rules and directives for this part: `index/part19_machine_learning.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Machine Learning, MLOps & Production ML System Design

### Foundations of AI

- **History and definitions**: the Dartmouth workshop (1956); the Turing test; four views of AI (thinking or acting, humanly or rationally); symbolic AI (logic, rules, semantic networks, expert systems); the AI winters and why rule systems failed; learning from data instead of hand-written rules; Mitchell's definition (experience E, task T, performance measure P)
- **Data types**: categorical (nominal), ordinal and continuous features; structured versus unstructured data
- **The supervised workflow**: problem first, then data, split, fit, predict and evaluate

### Classical AI: search, knowledge and reasoning

- **Philosophy of AI**: weak versus strong AI; the Chinese room; AI and the foundations of mind
- **Rational agents**: percepts, actions and the agent function versus the agent program; PEAS descriptions; task-environment properties (observable, deterministic, episodic, static, discrete, single- or multi-agent); simple reflex, model-based, goal-based, utility-based and learning agents
- **Problem solving by search**
  - State-space formulation: initial state, actions, transition model, goal test, path cost
  - Uninformed search: breadth-first, depth-first, uniform-cost, depth-limited, iterative deepening and bidirectional search; completeness, optimality, time and space
  - Informed search: best-first, greedy and A*; admissible and consistent heuristics; the optimality proof for A*; heuristics from relaxed problems and pattern databases; IDA*
- **Local search and optimization**: hill climbing and its failures (local maxima, plateaus, ridges); random walk and random restart; simulated annealing; local beam search; simulated annealing accepting a worse neighbour with probability exp(−Δ ÷ T), with the temperature T lowered on a cooling schedule
- **Evolutionary computation and swarm intelligence**: genetic algorithms (population, fitness, selection, crossover, mutation); genetic programming; ant-colony and particle-swarm optimization
- **Adversarial search**: minimax; alpha-beta pruning and the effect of move ordering; depth cutoffs, evaluation functions and the horizon effect; opening books and endgame databases; expectiminimax for chance; Monte Carlo tree search
- **Constraint satisfaction**: variables, domains, constraints and the constraint graph; backtracking with variable ordering (minimum remaining values, degree) and value ordering (least constraining); inference by forward checking and arc consistency (AC-3); min-conflicts local search; tree-structured CSPs
- **Logical agents**
  - Propositional logic: syntax, semantics, entailment, model checking; forward and backward chaining on Horn clauses; resolution on CNF; soundness and completeness
  - Reduction of problems to SAT; DPLL and WalkSAT; the satisfiability phase transition
  - First-order logic: quantifiers, unification, lifted forward chaining and resolution; Prolog's execution model
- **Knowledge representation and expert systems**: ontologies, semantic networks, frames and rules; non-monotonic reasoning (default logic, truth maintenance); expert-system architecture (knowledge base, inference engine, explanation) and applications; AI programming languages (Lisp, Prolog, CLIPS)
- **Planning**: STRIPS and PDDL; forward and backward state-space planning; planning graphs and GraphPlan; partial-order planning; planning with scheduling and resources
- **Reasoning under uncertainty**
  - Probability for AI: conditional independence and Bayes' rule
  - Bayesian networks: structure, factorization, d-separation; exact inference by enumeration and variable elimination; NP-hardness by reduction from 3-SAT
  - Approximate inference: rejection sampling, likelihood weighting, Markov chain Monte Carlo with Gibbs sampling; Metropolis–Hastings proposing x′ from q(x′ | x) and accepting with probability min(1, π(x′) q(x | x′) ÷ π(x) q(x′ | x)), which leaves the target π stationary by detailed balance
  - Learning Bayesian networks: maximum likelihood, MAP and Bayesian parameter learning; structure learning; expectation–maximization for hidden variables; MAP as the mode of the posterior, argmax over θ of log p(D | θ) + log p(θ), where a Gaussian prior gives the ridge penalty and a Laplace prior gives the lasso penalty
  - Dynamic Bayesian networks; filtering; hidden Markov models as a special case
- **Fuzzy logic**: fuzzy sets and membership functions; fuzzy operators and rules; fuzzy inference with fuzzification and defuzzification (centroid)
- **Multi-agent systems**: agent communication and negotiation; coordination (contract net); web-based and mobile agents
- **Robotics**: sensors and actuators; configuration space and motion planning; localization and mapping; the sense–plan–act loop; state estimation and control under uncertainty; learned manipulation and locomotion policies and their safety limits
- **Ethics of AI**: humans and robots; robustness and transparency; data bias and fairness; accountability; privacy; human oversight; alignment as the gap between the objective written down and the outcome intended, so that a proxy metric gets gamed (reward hacking); misuse as a use the builder did not intend, handled with a threat model and red-team tests before release
- **Data-science problem typology**: descriptive, diagnostic, predictive and prescriptive questions; a guided solution framework from framing through data, model and evaluation to deployment

### Classical machine learning

- **Learning paradigms**: supervised, unsupervised and reinforcement learning; regression, classification and clustering, and when to use which
- **Learning theory**
  - Empirical risk minimization
  - The bias–variance decomposition of squared error (bias² + variance + irreducible noise); overfitting and underfitting; double descent, where test error rises near the interpolation threshold (parameters roughly equal to training points) and falls again as the model grows past it
  - Regularization as a constraint: ridge (L2, a circular constraint region, closed-form solution, shrunken weights) and lasso (L1, a diamond-shaped region whose corners give sparse weights, fitted by coordinate descent); polynomial features with ridge in one pipeline
  - Maximum likelihood; minimizing cross-entropy as maximum likelihood for a classifier
  - Train, validation and test splits; cross-validation as an estimator with its own variance; the test set touched once
  - Splits that give an honest estimate: transforms fitted on the training split only; stratified splits for skewed classes; time-based splits for temporal data; group-aware splits keeping one user, patient or device on one side; near-duplicates removed across splits
  - Generalization from a test set: Hoeffding's bound P(|test error − true error| > ε) ≤ 2e^(−2mε²) for a fixed classifier; reusing a test set for model selection spends its guarantee
- **Linear models**
  - Least squares: minimizing ‖Xθ − y‖²; normal equations XᵀXθ = Xᵀy; convexity and convergence of gradient descent
  - Logistic regression with cross-entropy loss; generalized linear models; a GLM as an exponential-family response with a link function g(μ) = xᵀβ (identity for Gaussian, logit for Bernoulli, log for Poisson), fitted by iteratively reweighted least squares
- **Other supervised models**: k-nearest neighbours; naive Bayes; linear and quadratic discriminant analysis; support vector machines and margins; class weights; LDA's shared-covariance Gaussian class densities giving a linear boundary and QDA's class-specific covariances giving a quadratic one; the SVM dual, in which the data enter only through inner products, so a kernel k(x, x′) can replace them (the kernel trick), with the margin fixed by the support vectors
- **Trees and ensembles**: decision trees and impurity (Gini, entropy); CART; random forests; gradient boosting and boosted stumps; feature importance; monotonic constraints
- **Unsupervised learning and anomaly detection**: k-means; DBSCAN; Gaussian mixtures fitted by expectation–maximization; association rules (support, confidence, lift); robust statistics (z-score, median absolute deviation); isolation forests; reconstruction-error anomaly scores; EM for a Gaussian mixture alternating an E-step (responsibilities γᵢₖ ∝ πₖ N(xᵢ | μₖ, Σₖ)) with an M-step (weighted means, covariances and mixing weights from those responsibilities)
- **Dimensionality reduction**: the curse of dimensionality; PCA to compress features, with components chosen by explained variance; t-SNE for visualization only
- **Evaluation**
  - The confusion matrix; accuracy and why it misleads on imbalanced data (base rates)
  - Precision, recall, F1, macro-F1 for multiclass problems; choosing precision or recall by the cost of false positives against false negatives
  - ROC curves and AUC as the probability a random positive outranks a random negative; PR curves and PR-AUC
  - Calibration and reliability bins
  - Ranking measures: precision@k, recall@k, MAP, MRR, nDCG@k = DCG@k ÷ IDCG@k
  - Forecast errors: MAE, percentage errors and their instability near zero, interval coverage
  - Business guardrail metrics beside model metrics; a north-star metric that the guardrails protect, a metric tree breaking it into the drivers a model can move, and launch criteria written as thresholds on each, fixed before the test starts
- **Feature engineering**
  - Scaling and normalization; encoding categoricals; the hashing trick; target encoding with time-aware folds
  - Missing values; imbalanced datasets (SMOTE, class weighting, focal loss, negative sampling) and the accuracy paradox, where always predicting the majority class scores high and detects nothing
  - Text, time, window, session and graph features; learned embeddings for the same entities as the alternative to these hand-built features, with the data and monitoring cost each route carries
  - Schema validation and golden tests for feature pipelines
- **Regression in depth**: model assessment (R², adjusted R², residual plots, heteroscedasticity, leverage and influence); multiple regression and multicollinearity (variance inflation factor); variable and subset selection (best-subset, forward and backward stepwise, AIC and BIC)
- **Computational learning theory**: hypothesis space and inductive bias; the PAC model; sample complexity for finite hypothesis classes; VC dimension and the growth function
- **Feature selection and agreement**: filter, wrapper and embedded selection versus feature extraction; Cohen's kappa as agreement beyond chance
- **Splines and basis expansions**: fixed basis functions (piecewise polynomials, B-splines) that turn a nonlinear fit into a linear one; knots and degrees of freedom; smoothing splines minimizing Σ(yᵢ − f(xᵢ))² + λ∫f''(t)² dt, whose solution is a natural cubic spline with knots at the data; the reproducing-kernel view
- **Kernel smoothing**: local weighted averages with a kernel that decays with distance; the Nadaraya–Watson estimator; bandwidth as the bias–variance knob; local linear regression correcting boundary bias; kernel density estimation
- **Robust regression and errors-in-variables**: Huber and bisquare losses that downweight outliers; least absolute deviations; the breakdown point; errors-in-variables, where noise in the predictor attenuates the least-squares slope by the reliability ratio σ²ₓ ÷ (σ²ₓ + σ²ᵤ)
- **Model comparison and Bayes factors**: marginal likelihood as the evidence for a model; the Bayes factor P(D | M₁) ÷ P(D | M₂); Occam's factor penalizing flexible models; BIC as a large-sample approximation to the log evidence
- **Spectral clustering**: a similarity graph (k-nearest-neighbour or Gaussian affinities); the graph Laplacian L = D − W; the first k eigenvectors as an embedding, followed by k-means; why it separates non-convex clusters; normalized cut
- **Hierarchical clustering**: agglomerative merging under single, complete, average and Ward linkage; dendrograms and cutting at a height; O(n²) memory and the cost at large n; divisive clustering as the top-down reverse
- **Gaussian processes**: a distribution over functions fixed by a mean function and a kernel; posterior mean and variance from the training covariance matrix; the marginal likelihood for fitting kernel hyperparameters; O(n³) exact inference and sparse approximations
- **Undirected graphical models**: Markov random fields and factor graphs; pairwise potentials and the Gibbs form p(x) ∝ exp(−E(x)); conditional independence as graph separation; the Hammersley–Clifford theorem; pseudolikelihood as a tractable training surrogate
- **Partition function**: Z = Σₓ exp(−E(x)) as the normalizer, and why summing over exponentially many states is intractable; the log-partition gradient identity ∂ log Z ÷ ∂θ = −E[∂E ÷ ∂θ], which turns maximum likelihood into moment matching; annealed importance sampling
- **Ising model**: spins ±1 on a lattice with energy −Σ Jᵢⱼ sᵢsⱼ − Σ hᵢsᵢ; ferromagnetic versus frustrated couplings; the critical point kT ÷ J ≈ 2.269 of the two-dimensional square lattice; Gibbs sampling and mean-field approximations
- **Probabilistic programming**: models written as ordinary programs with random choices and conditioned data; inference engines (Markov chain Monte Carlo, Hamiltonian Monte Carlo, variational inference) run on any such program; posterior predictive checks; Stan, PyMC and Pyro as examples
- **Kalman filters**: the linear-Gaussian state-space model; predict and update steps with gain K = PHᵀ(HPHᵀ + R)⁻¹; the innovation; optimality among linear estimators under Gaussian noise; extended and unscented variants for nonlinear models; tracking as the canonical use

### Deep learning

- Biological and artificial neurons; the perceptron and its limit to linearly separable data (XOR); multilayer perceptrons; width versus depth
- Activation functions: step, sigmoid, tanh, ReLU, softmax; the forward pass
- Loss functions: mean squared error for regression, cross-entropy for classification
- Tensors and computational graphs; tensor contractions in einsum notation, where a repeated index is summed and the shapes must agree (X of shape b×n×d times W of shape d×k gives b×n×k)
- Backpropagation as reverse-mode automatic differentiation over the computation graph; its cost as a small multiple of the forward pass; gradient checking by finite differences
- Vanishing and exploding gradients; residual connections; batch and layer normalization; batch normalization standardizing each channel over the mini-batch, then a learned scale γ and shift β, with running statistics used at evaluation; local minima and saddle points, where saddle points rather than poor local minima are the usual obstacle in high dimension
- Optimizers: batch, mini-batch and stochastic gradient descent, momentum, RMSProp, Adam; learning-rate schedules; Nesterov momentum evaluating the gradient at the look-ahead point θ − βv, with v ← βv + η∇L(θ − βv); AdaGrad accumulating squared gradients per coordinate, so frequently updated parameters take shrinking steps
- **Learning-rate schedules**: large steps early and small steps late; four knobs (warmup length, peak rate, decay shape, floor); linear warmup from near zero; constant, linear decay, cosine decay, step decay and reduce-on-plateau, cosine with restarts, and warmup–stable–decay for runs of unknown length; lengthening warmup and lowering the peak before changing the shape
- **Training instability**: loss spikes, gradient explosion and divergence as one feedback loop (an oversized update raises the loss, which enlarges the next gradient); sharp minima, outlier batches and depth as causes; gradient-norm clipping that rescales to a cap and keeps the direction, with the pre-clip norm logged; float16 overflow near 65,504 turning into Inf and NaN, and bfloat16 as the remedy; alerts on the gradient norm; checkpoints every N steps
- **Batch size**: effective batch = micro-batch × gradient-accumulation steps × devices; filling device memory, then accumulating; small batches (noisy gradients, more updates, often better generalization) versus large ones (stable gradients, higher throughput, fewer updates); the linear scaling rule tying learning rate to effective batch; too few optimizer steps showing as underfitting; computational performance on hardware: data parallelism replicating the model on each device and all-reducing gradients every step, model and pipeline parallelism when the weights do not fit one device, and throughput bounded by memory bandwidth as often as by arithmetic
- **Reading loss curves**: both losses high and flat early (underfitting); training loss falling while validation loss turns up (overfitting); both flat at the starting value (nothing is updating); persistent jitter (batch too small or rate too high); both falling with a small stable gap (healthy), checkpointed at the validation minimum
- Initialization that preserves activation variance: Glorot (Xavier) initialization Var(w) = 2 ÷ (n_in + n_out); He initialization Var(w) = 2 ÷ n_in for ReLU units
- Regularization in deep networks: weight decay, dropout, data augmentation, early stopping with patience; ensembles of independently trained networks averaged for accuracy and uncertainty, with the variance of the averaged predictor falling as σ² ÷ M when the member errors are uncorrelated
- Architecture as inductive bias: convolutions sharing one kernel across positions, so parameter count is independent of image size; CNNs for images; convolution with padding p, stride s and dilation d giving output length ⌊(n + 2p − d(k − 1) − 1) ÷ s⌋ + 1; equivariance, so shifting the input shifts the feature map, with pooling adding local invariance; residual blocks F(x) + x with identity shortcuts; VGG's stacked 3 × 3 kernels, GoogLeNet's 1 × 1 bottleneck inception modules and DenseNet's concatenated feature reuse; the lineage from LeNet-5 (convolution, subsampling, fully connected layers on digits) to AlexNet (ReLU, dropout, data augmentation and GPU training winning ImageNet 2012), then VGG, Inception and ResNet; translation invariance from pooling versus translation equivariance from convolution
- Sequence models before attention: RNNs and LSTMs; encoder–decoder (sequence-to-sequence) models and their fixed-length context bottleneck; weak long-range dependencies; no parallelism across time steps; Bahdanau (additive) attention over encoder states; variable-length batches padded to a common length with a boolean mask, so pad positions add nothing to the loss or the pooled state, and packed sequences that skip them in the recurrence
- The perceptron learning rule and its convergence proof (the mistake bound R²/γ²); McCulloch–Pitts units; sigmoid neurons; universal approximation and the trade-off between thin deep and fat shallow networks
- Backpropagation through time: unrolling, truncated BPTT, and the gates of LSTM and GRU cells as controlled additive memory
- Visualizing convolutional networks: maximally activating patches, saliency maps and guided backpropagation; attention over image regions and hierarchical attention; Integrated Gradients averaging gradients along a straight path from a baseline input to the actual input, scaled by the input difference, with the completeness check that the attributions sum to the output difference
- **Bidirectional and deep RNNs**: a backward pass whose states are concatenated with the forward pass, so each position sees past and future context (offline tagging, not streaming generation); stacked recurrent layers whose outputs feed the next layer; gradient flow across depth and time
- **GELU and Swish activations**: GELU(x) = x·Φ(x), each input weighted by its Gaussian cumulative probability, with the tanh approximation; Swish x·σ(βx), equal to SiLU at β = 1; smooth non-monotone dips below zero against ReLU's kink at zero; their use in transformer feedforward blocks
- **Noise injection and parameter tying**: Gaussian noise on inputs, weights or activations as a regularizer, with input noise matching an L2 (Tikhonov) penalty to second order for small variance; tied parameters shared across positions or layers, as in convolutions and tied input and output embeddings; the drop in parameter count and its effect on generalization
- **Lottery ticket hypothesis**: a randomly initialized dense network contains a sparse subnetwork that, retrained alone from its original initialization, matches the full network's accuracy; iterative magnitude pruning to find winning tickets; rewinding weights to an early iteration; the contested status of the claim at scale
- **Continual learning**: learning a stream of tasks without forgetting earlier ones; the stability–plasticity trade-off; replay of stored examples; regularization that penalizes moving important weights (elastic weight consolidation's Fisher-weighted penalty); architectural isolation; average accuracy and forgetting as the measures

### Natural language processing foundations

- NLP as the interface between people and software; tasks (classification, named entities, translation, summarization, question answering)
- The classical pipeline: cleaning and Unicode normalization, tokenization, stop-word removal, stemming and lemmatization, feature extraction, a classifier; stop-word removal as a fixed-list lookup applied before counting, with the caveat that negations such as "not" and short function words carry sentiment and syntax, so the list must be tuned to the task
- Representations: one-hot vectors and bag of words and their limits (sparsity, lost word order, no semantics, out-of-vocabulary words, orthogonal vectors for related words); n-gram features; TF-IDF weighting tf × log(N ÷ df)
- Distributional semantics: meaning from context windows; dense static embeddings (Word2Vec skip-gram and CBOW with negative sampling, GloVe); vector analogies; contextual embeddings (ELMo) and then transformers
- Limits of classical NLP, and the progression from rules to statistical models, deep learning, LLMs and agents
- **Why text is hard**: ambiguity and variation; Zipf's and Heaps' laws as empirical regularities of text
- **Spelling correction**: weighted edit distance (Levenshtein, Damerau); the noisy-channel model P(w | x) ∝ P(x | w) P(w); candidate generation
- **Morphology**: inflection versus derivation; finite-state transducers; stemming versus lemmatization
- **Sequence labelling**: part-of-speech tagging with hidden Markov models (transition and emission probabilities, Viterbi decoding, Baum–Welch); maximum-entropy classifiers; conditional random fields and label bias; BIO tagging for named entities; forward and backward recursions α and β giving the state posteriors, and Baum–Welch as expectation–maximization over them that re-estimates the transition and emission probabilities; BILUO tags (Begin, Inside, Last, Unit, Outside) that mark entity ends and single-token entities; span-level F1, where an entity counts only if its type and both boundaries match exactly
- **Syntactic parsing**: constituency grammars, the CKY algorithm, probabilistic CFGs and inside–outside probabilities; dependency parsing, transition-based (arc-standard, arc-eager) and graph-based (maximum spanning tree); UAS and LAS
- **Lexical semantics**: WordNet and synsets; word-sense disambiguation (Lesk, supervised, knowledge-based); detecting novel senses; hypernym traversal up the is-a hierarchy to a common ancestor, and path similarity 1 ÷ (1 + shortest path length) between two synsets
- **Topic models**: LSA and pLSA; the LDA generative story, Dirichlet priors and collapsed Gibbs sampling; variants
- **Information extraction**: entity linking; relation extraction and distant supervision; open information extraction
- **Knowledge graphs**: triples and schemas; completion by embeddings (translation models such as TransE, rotation models such as RotatE, multiplicative models such as DistMult and ComplEx); evaluation by mean reciprocal rank and Hits@k
- **Summarization, classification and sentiment**: extractive (LexRank, centroid, optimization-based) versus abstractive summarization and ROUGE; text classification; sentiment with affective lexicons and aspect-based sentiment

### Machine learning in Python

- scikit-learn: the estimator API (`fit`, `transform`, `predict`); `Pipeline` and `ColumnTransformer`; `StandardScaler`, `MinMaxScaler`, `OneHotEncoder`, `SimpleImputer`, `PolynomialFeatures`; `train_test_split`, `cross_val_score`, `GridSearchCV`, `RandomizedSearchCV`; metrics and classification reports
- PyTorch: tensors and autograd; `nn.Module` with `Linear`, `Embedding`, `Dropout`, `LayerNorm`; loss functions and optimizers; the training loop (forward, loss, backward, step, zero gradients); evaluation mode; devices; custom layers as `nn.Module` subclasses that register parameters in `__init__` and define `forward`, with parameter management by `named_parameters()` and `state_dict()` for saving, and freezing a layer by setting `requires_grad` to False
- NLTK for tokenizers, stop words, stemmers and lemmatizers
- **LightGBM**: histogram-binned gradient boosting with leaf-wise tree growth under a leaf cap; gradient-based one-side sampling and exclusive feature bundling for large data; early stopping, categorical features and feature importance; comparison with the boosted stumps built from scratch
- **TensorFlow and Keras**: eager execution and `tf.function` graph tracing; Keras `Sequential` and functional models with compile, fit and callbacks; the explicit training loop compared with the PyTorch one; SavedModel as the serving format
- **PySpark distributed processing**: the lazy DataFrame plan executed on an action; narrow versus wide transformations and the shuffle that wide ones trigger; partitioning and key skew; the DataFrame API and SQL over the same plan; MLlib pipelines
- **Dask parallel arrays and dataframes**: lazy task graphs over chunked NumPy arrays and pandas dataframes; chunk size and partition counts; `compute()` triggering the scheduler; out-of-core work on one machine and scaling to a cluster
- **Data engineering fundamentals**: row versus columnar file formats (CSV, JSON, Parquet) and their scan costs; ETL versus ELT; batch versus streaming ingestion; partitioning and idempotent loads with backfills; schema and quality checks at pipeline boundaries
- **XGBoost**: second-order gradient boosting in which each split's gain is ½[G_L² ÷ (H_L + λ) + G_R² ÷ (H_R + λ) − (G_L + G_R)² ÷ (H_L + H_R + λ)] − γ, with L2 penalty λ on leaf weights and a per-split penalty γ; column and row subsampling; the histogram tree method; early stopping on a validation set; comparison with the LightGBM and boosted-stump builds above

### Specialised learning areas

- **Reinforcement learning**: Markov decision processes, value functions, policy gradients, PPO; GRPO, which drops the learned value function and scores each sampled answer against the mean and standard deviation of its own group of samples for the same prompt; GSPO, which applies the clipped importance ratio to the whole sequence (length-normalized) instead of per token, for stability on long generations
- **Graph learning**: PageRank, random walks and random-walk embeddings, bipartite graphs, label propagation, node and edge anomaly scores, graph neural networks; graph convolution as neighbourhood averaging with symmetric normalization, H′ = σ(D̂^(−½) Â D̂^(−½) H W) with Â = A + I, classifying nodes from a few labelled nodes by semi-supervised training
- **Entity resolution**: blocking, candidate generation, pairwise matching
- **Computer vision**: pixels and image representation, 2D convolution and image filters, image embeddings, perceptual hashing, OCR and document extraction, segmentation; vision at research depth
- **Audio and speech**: audio frames, windowing, spectrograms and MFCCs, word error rate per locale; speech at research depth
- **Multimodal retrieval** across text, image and audio embeddings
- **Contrastive (metric) learning** for retrieval; on-device models bounded by memory, power and privacy; the InfoNCE loss −log(exp(s⁺ ÷ τ) ÷ Σ exp(s ÷ τ)) over one positive and the in-batch negatives; autoencoders whose bottleneck code is a learned representation, trained by reconstruction
- **Operations research**: linear and integer programming, assignment, constrained scheduling; forecasts as inputs to capacity, pricing and dispatch constraints
- **Game theory and auctions**: equilibria; second-price and generalized second-price auctions; incentive compatibility; mechanism design
- **Click models**: deep click-rate models and click-model research
- **Reinforcement learning in detail**: policy evaluation as a linear system or by iteration; value iteration and policy iteration; passive model-based versus model-free evaluation; temporal-difference learning, Q-learning and SARSA; exploration versus exploitation
- **n-step returns and eligibility traces**: the n-step return Gₜ⁽ⁿ⁾ = rₜ₊₁ + γrₜ₊₂ + … + γⁿ⁻¹rₜ₊ₙ + γⁿV(sₜ₊ₙ), interpolating between one-step TD and Monte Carlo; the λ-return as a weighted average of n-step returns; the backward view with accumulating and replacing traces; TD(λ) and Sarsa(λ)
- **Monte Carlo methods for control**: action values estimated by averaging complete-episode returns, first-visit or every-visit; exploring starts versus ε-soft policies; generalized policy iteration; off-policy Monte Carlo with importance-sampling ratios, ordinary versus weighted
- **Planning with learned models (Dyna)**: learning a model from real transitions and replaying simulated transitions to update values (Dyna-Q); the ratio of planning steps to real steps; prioritized sweeping; model error as the failure mode
- **Function approximation in reinforcement learning**: a parametric value estimate trained by semi-gradient TD; the mean-squared value error objective; linear features and tile coding; the deadly triad of function approximation, bootstrapping and off-policy updates that can diverge; semi-gradient Sarsa for control

### Classical computer vision and geometry

- **Image processing**: sampling and quantization; histograms and equalization; spatial filtering; image transforms (Fourier, DCT)
- **Colour**: colour spaces (RGB, HSV, Lab); perception, white balance and colour constancy; colour image processing
- **2-D projective geometry**: homogeneous coordinates; points and lines at infinity; the hierarchy of similarity, affine and projective transformations; homography estimation by the direct linear transform
- **Camera geometry**: the pinhole model; intrinsics K and extrinsics [R | t]; the projection matrix P = K[R | t]; lens distortion; calibration (Zhang's method)
- **Stereo and multi-view geometry**: epipolar constraint; fundamental and essential matrices and the eight-point algorithm; rectification, disparity and triangulation; structure from motion and bundle adjustment
- **Features**: corners (Harris); scale space and blob detection (LoG, DoG); SIFT-style descriptors; matching with the ratio test
- **Model fitting**: least squares; RANSAC; the Hough transform
- **Range images**: depth sensing (structured light, time of flight, LiDAR, stereo); point clouds; normals, ICP registration and range-image processing
- **Recognition**: clustering and classification for vision (bag of visual words); dimensionality reduction and sparse representation (sparse coding, dictionary learning)
- **Deep vision**: object detection (R-CNN family, YOLO); semantic and instance segmentation (FCN, U-Net, Mask R-CNN); vision applications

### Applied problem families

- **Problem framing**: prediction, ranking, retrieval, generation and optimization problems; the target action, labels, input entities, metric and failure modes; cold start; feedback loops; delayed labels; a go or no-go test before any model (ML is warranted only when the rule is hard to write, the data and labels exist, and the cost of a model's errors is below the cost of a rule's), and a non-ML baseline (a heuristic, a popularity rule or the current process) that every model must beat on the agreed metric before training starts
- **The case-study method**: problem and business measure → data and labels (implicit, explicit, delayed, weak) → leakage against what is known at decision time → derived metric or estimator → offline evaluation → serving (batch or online) and latency budget → monitoring, rollback and retraining → cost → a named company's design read against the same steps
- **Leakage and point-in-time correctness**: as-of joins; leakage, training–serving skew and online–offline feature drift as three distinct failures; one feature definition for both paths with a parity test
- **Recommendation and feeds**
  - Candidate generation (two-tower retrieval, approximate nearest neighbours, judged by recall@k) separated from ranking and re-ranking
  - Collaborative filtering (item–item), matrix factorization; cold start for a new user or item, where no interactions exist to fit factors, answered by content features, popularity priors and a slice of exploratory traffic
  - Diversity, coverage and multiple objectives; popularity feedback loops; catalogue coverage; maximal marginal relevance re-ranking, which picks each next item to maximize λ·relevance − (1 − λ)·(maximum similarity to the items already chosen)
  - Labels from impressions, plays, dwell and hides; leakage from future popularity and same-session targets
- **Search, learning to rank and ads**
  - Inverted indexes, BM25, semantic and hybrid retrieval with rank fusion
  - Learning to rank: pointwise, pairwise and listwise; sampled pairs
  - Position bias: the position-based click model; inverse-propensity scoring (Horvitz–Thompson) unbiased under positivity; propensity clipping trading bias for variance; propensities from randomized slices; off-policy evaluation of a new ranker from old logs
  - Ads ranked by bid × predicted quality; calibrated click and conversion rates
  - Wide & deep models: memorized feature crosses plus generalizing embeddings
- **Explore and exploit**
  - The K-armed bandit; regret R_T = Tμ* − E[Σ rₜ]
  - Greedy lock-in; ε-greedy's linear regret; UCB1 (x̄ᵢ + √(2 ln t ÷ nᵢ)) and Thompson sampling with logarithmic regret; the Lai–Robbins lower bound; the minimax lower bound, under which every algorithm suffers regret of order √(KT) on some K-armed instance over T rounds, matched up to logarithmic factors by UCB-style and Exp3-style methods
  - Contextual and cascade bandits; offline replay evaluation; policy constraints; replay evaluation keeping a logged event only when the logged action equals the new policy's action, which gives an unbiased estimate of the new policy's average reward when the logging policy chose uniformly at random; the case studies of news recommendation and ad allocation read with the same replay evaluator
  - Adversarial bandits: rewards chosen by an adversary with no fixed distribution; regret against the best fixed arm in hindsight; exponential-weight algorithms (Exp3) with importance-weighted reward estimates; regret of order √(KT log K)
  - Pure exploration: identifying the best arm at a fixed confidence or within a fixed sampling budget; successive elimination and sample-complexity bounds; how it differs from regret minimization, where every pull counts
  - A/B test versus bandit versus feature flag
- **Forecasting, ETA, demand and availability**
  - Trend, seasonality and holiday decomposition; moving averages, exponential smoothing, autoregressive intuition; backtesting
  - Covariates as known at forecast time; censored observations
  - The pinball (quantile) loss L_τ and why its minimizer is the τ-quantile; prediction intervals judged by coverage and width together; quantile forecasting by fitting one model per τ (for example 0.1, 0.5 and 0.9) to get the interval directly, and repairing quantile crossing by sorting the predicted quantiles
  - Availability probabilities, calibration and the cost of a false "in stock"
- **Fraud, abuse, risk and trust and safety**
  - Cost-weighted thresholds: flag when p > C_FP ÷ (C_FP + C_FN); expected cost C_FP·FP + C_FN·FN as the measure
  - Review-queue capacity setting the threshold; recall at a fixed false-positive rate
  - Weak, delayed (chargeback) and semi-supervised labels
  - Fraud rings as connected components of shared-device and shared-card graphs
  - Synchronous scoring beside an asynchronous review queue; fail-open versus fail-closed decisions
  - Adversarial drift; adversarial test sets built by red-team generation of hard inputs (perturbed, paraphrased or boundary cases), scored apart from the random holdout, with the pass rate reported per attack family
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
- **Causal inference**: causal graphs and structural causal models (structural equations, interventions, counterfactuals); front-door adjustment for unobserved confounders; instrumental variables, difference in differences, regression discontinuity and synthetic control; propensity weighting; overlap (positivity) and its failure; sensitivity analysis for unmeasured confounding; observational bias
- **Marketplace pricing** as an applied family

### MLOps

- The ML lifecycle: data → features → training → evaluation → deployment → monitoring → retraining
- **Technical debt in ML systems**: entanglement; hidden feedback loops; undeclared consumers; data dependencies; glue code and pipeline jungles; the model as a small part of the system
- **Data and feature platforms**: event contracts; batch versus streaming features; freshness and backfills; point-in-time correctness; schema evolution; feature stores with online and offline parity; fresh features streamed from user-action and inventory events; per-entity features cached with a TTL
- **Training pipelines**: dataset snapshots and versions; reproducible training (pinned data, code, environment, seeds); experiment tracking; hyperparameter search; model registries with lineage, aliases and approval status; model cards; code, data and model as three independent change axes, so a model record pins all three and a change to any one yields a new version; hyperparameter search by random sampling over log-scaled ranges, Bayesian optimization with a Gaussian-process surrogate and expected improvement, and successive halving that stops weak trials early
- **Production readiness**: the ML Test Score rubric across data, model, infrastructure and monitoring; the Google Cloud Professional Machine Learning Engineer exam guide as a named benchmark for this part's design, build, operationalize and govern groups, with each of its sections mapped to a group above
- **CI/CD/CT**: continuous training; continuous evaluation triggered from CI
- **Serving architectures**: online, batch, near-real-time, embedded, sidecar and asynchronous inference; caches, fallbacks and timeout budgets; batch scores delivered by schedulers and task queues; a prediction service as a model server behind a load balancer, with health checks, autoscaling on concurrency and a p99 latency budget split across feature fetch, model call and post-processing; edge deployment of compressed models on phones and microcontrollers, with post-training int8 quantization and size and latency measured on the target device
- **Experimentation and rollout**: A/B tests as two-sample hypothesis tests; holdouts; assignment bucketing and exposure logs; bootstrap intervals; segment analysis; metric guardrails; shadow, canary and ramp deployments of models as a dial separate from the application canary; rollback gates; a rollback gate as a pre-registered rule that compares the candidate's guardrail metrics with control and reverts automatically when a one-sided test rejects, evaluated by a command-line evaluator that exits nonzero on failure so the pipeline stops
- **Monitoring and drift**
  - Covariate shift (P(x) changes), prior or label shift (P(y) changes) and concept drift (P(y | x) changes)
  - Two-sample detection: the Kolmogorov–Smirnov statistic D = supₓ |F₁(x) − F₂(x)|; the population stability index PSI = Σ (aᵢ − eᵢ) ln(aᵢ ÷ eᵢ) and its conventional 0.1 and 0.25 thresholds
  - Training–serving skew as a pipeline defect that retraining does not fix
  - Calibration drift; data-quality and freshness checks; a written retraining policy; incident runbooks; a retraining policy that names its trigger (a schedule, a drift threshold or a metric drop), the validation gate a candidate must pass and the rollback path; model-evaluation dashboards with per-slice metrics over time, confidence bands and alert thresholds that link to the runbook
- **Governance and responsible ML**: privacy and PII minimization; consent, retention and deletion; bias and fairness; explanations; human-in-the-loop review and human override; audit logs; non-destructive, undoable AI actions; abuse resistance and red-team tests; data-loss prevention on logs; group fairness assessment comparing selection rate, true-positive rate and false-positive rate across groups (demographic parity, equalized odds), reported per slice before launch and after each retrain; Fairness Lens, the Vertex AI tool for running this per-slice comparison on a deployed model, with its console path and command grammar learned from the product's current documentation; SHAP attributions as Shapley values φᵢ of each feature, which add with the base value E[f(X)] to the prediction f(x) (local accuracy), so one prediction's feature contributions are read directly
- **Scale and cost**: hot keys and fan-out; approximate retrieval; request batching; concurrency limits; accelerators as remote services; cost per prediction and per successful decision; cost at ten times the traffic; latency percentiles (p50, p95, p99) measured under load, and throughput as requests per second at a stated latency objective, because batching raises throughput and adds queueing delay
- **ML platforms**: shared features, training, registry, serving and monitoring across teams; platform-enforced point-in-time joins; measured by time to train, failed deploys, skew incidents and cost per training hour; shared datasets as versioned, owned assets with a schema, access control and recorded lineage, so a team reuses a published snapshot instead of copying it
- **TensorFlow Extended (TFX)**: a production pipeline of components (ExampleGen, StatisticsGen, SchemaGen, ExampleValidator, Transform, Trainer, Evaluator, Pusher); the metadata store recording artifact lineage; orchestration by Apache Beam, Apache Airflow or Kubeflow Pipelines
- **TensorFlow Data Validation (TFDV)**: per-feature statistics; schema inference from training data; validation of new batches against that schema to flag missing values, unseen categories and out-of-range values; training–serving skew checks
- **Kubeflow Pipelines**: pipelines as directed acyclic graphs of containerized components, each run as a pod on Kubernetes with declared inputs and outputs; parameters, step caching and run history; Vertex AI Pipelines executing Kubeflow pipeline definitions
- **MLflow**: runs with parameters, metrics and artifacts; a tracking server backed by a database and an artifact store; autologging; the model registry with versions, aliases and lineage back to the run
- **Weights & Biases experiment monitoring**: runs and live metric dashboards; sweeps for hyperparameter search; versioned artifacts with lineage; reports and team access; hosted versus self-hosted trade-offs against MLflow
- **Evidently drift monitoring**: reference and current windows compared column by column with drift tests (Kolmogorov–Smirnov for numeric features, chi-square for categorical) and PSI; target and prediction drift reports; threshold alerts wired to a runbook
- **Custom containers for serving**: a model image carrying its runtime and serving code, exposing a health route and a predict route on the configured port; `gcloud ai models upload` with `--container-image-uri`, `--container-health-route` and `--container-predict-route`; `gcloud ai endpoints deploy-model` to put it behind an endpoint
- **Multi-model endpoints**: several models deployed to one endpoint with a traffic split across the deployed models; `gcloud ai endpoints deploy-model` with `--traffic-split` and `gcloud ai endpoints undeploy-model`; compute shared against isolation from noisy neighbours; rollback of one model by shifting its share of the split
- **The human side of ML**: team roles across data scientists, engineers and product owners; ownership of a production model with on-call and runbooks; setting stakeholder expectations for error costs and uncertainty; user-facing design for model mistakes (fallbacks, feedback capture); labelling workforce quality and annotator agreement; responsible-AI review as a team process; a labelling workflow with written guidelines, a gold set for audits, double-labelled samples that measure agreement by Cohen's kappa, and adjudication of disagreements

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
- From scratch: a Gaussian process regressor with an RBF kernel and marginal-likelihood fitting, and spectral clustering from a graph Laplacian's eigenvectors, each checked against the library's output on the same data
- From scratch: TD(λ) with accumulating eligibility traces and Dyna-Q on a gridworld, comparing steps to goal against model-free Q-learning alone
- From scratch: an MLflow-tracked training pipeline logging parameters, metrics and artifacts for each run, then a drift report comparing a reference window with a live window by PSI and a Kolmogorov–Smirnov test
- **Reasoning drills**
  - Predict the bias–variance effect of a model change before training it
  - Derive a loss gradient by hand and check it numerically
  - Find the leakage in a feature set before training
  - Reproduce one result of a classic machine-learning paper at toy size and critique its evaluation
  - For a stated causal graph, name the adjustment set that identifies the effect and say whether back-door or front-door adjustment applies; name the assumption (positivity, or no unblocked confounding) that would break it
