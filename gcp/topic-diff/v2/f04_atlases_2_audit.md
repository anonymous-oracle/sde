# Topic diff: Chapter atlases part 2, institutional cross-check and audit

Source: gcp/unified-curriculum.md lines 1301-1733. Compared against: gcp-lite/index/*.topics.md and gcp-lite/Rust_Track_AI_Infrastructure.md.

Counts: 262 topics; 162 covered, 78 partial, 22 missing, 0 out of scope.

## 17.1.7 (continuation)

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Counting arguments and conditional probability | covered | part03_mathematics.topics.md › Probability | |
| Bayes' theorem | covered | part03_mathematics.topics.md › Probability | |
| Law of large numbers and central limit theorem | covered | part03_mathematics.topics.md › Probability | |
| Named distributions, expectation and variance | covered | part03_mathematics.topics.md › Probability | |
| Generating functions | partial | part03_mathematics.topics.md › Probability | named only in passing; not taught as a technique |
| Markov chains and random walks | covered | part03_mathematics.topics.md › Probability | |
| Poisson processes | covered | part03_mathematics.topics.md › Probability | |
| Markov chain Monte Carlo | covered | part19_machine_learning.topics.md › Classical machine learning | |
| Maximum likelihood estimation | covered | part03_mathematics.topics.md › Statistics and experimental design | |
| Sufficiency and data reduction | covered | part03_mathematics.topics.md › Statistics and experimental design | |
| Plausible reasoning | covered | part03_mathematics.topics.md › Probability | |
| Entropy, relative entropy and mutual information | covered | part03_mathematics.topics.md › Information theory | |
| Asymptotic equipartition property | covered | part03_mathematics.topics.md › Information theory | |
| Kolmogorov complexity | covered | part08_data_structures_algorithms.topics.md › Computability and complexity | |
| Rate distortion | covered | part03_mathematics.topics.md › Information theory | |
| Channel capacity | covered | part03_mathematics.topics.md › Information theory | |
| Maximum entropy principle | partial | part03_mathematics.topics.md › Information theory | named only |
| Turbo, fountain and convolutional codes | partial | part03_mathematics.topics.md › Information theory | LDPC codes covered; the other code families are not |

## 17.1.7.1 Probability, statistics and information audit

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Fisher information | covered | part03_mathematics.topics.md › Statistics and experimental design | |
| Cramér-Rao bound | partial | part03_mathematics.topics.md › Statistics and experimental design | Fisher information named; the bound is not stated as a topic |
| Bootstrap and jackknife | covered | part03_mathematics.topics.md › Statistics and experimental design | |
| A/B testing | covered | part03_mathematics.topics.md › Statistics and experimental design | |
| Multiple-testing correction | covered | part03_mathematics.topics.md › Statistics and experimental design | |
| CUPED variance reduction | covered | part03_mathematics.topics.md › Statistics and experimental design | |

## 17.1.8 Optimization and spectral methods

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Singular value decomposition | covered | part03_mathematics.topics.md › Linear algebra | |
| Convex sets and convex functions | covered | part03_mathematics.topics.md › Calculus and optimization | |
| Quasi-Newton methods | covered | part03_mathematics.topics.md › Calculus and optimization | |
| Conjugate gradient | covered | part03_mathematics.topics.md › Calculus and optimization | |
| Trust-region methods | missing | → suggest part03 | |
| Interior-point methods | covered | part03_mathematics.topics.md › Calculus and optimization | |
| Proximal operators and proximal gradient | covered | part03_mathematics.topics.md › Calculus and optimization | |
| Subgradients | missing | → suggest part03 | |
| Mirror descent | missing | → suggest part03 | |
| ADMM | missing | → suggest part03 | |

## 17.1.8.1 Optimization and spectral audit

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Hilbert space | covered | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis | |
| Gram-Schmidt orthogonalization | covered | part03_mathematics.topics.md › Linear algebra | |
| Spectral theorem | covered | part03_mathematics.topics.md › Linear algebra | |
| Low-rank approximation | covered | part03_mathematics.topics.md › Linear algebra | |
| Lagrange multipliers and KKT conditions | covered | part03_mathematics.topics.md › Calculus and optimization | |
| Linear programming and the assignment problem | covered | part03_mathematics.topics.md › Calculus and optimization | |
| Gradient descent variants | covered | part03_mathematics.topics.md › Calculus and optimization | |
| Momentum and adaptive optimizers | covered | part03_mathematics.topics.md › Calculus and optimization | |

## 17.1.9 Signals, image processing and vision

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Sampling and aliasing | covered | part03c_signals_systems_and_communications.topics.md › Signals and LTI systems | |
| Discrete Fourier transform | covered | part03c_signals_systems_and_communications.topics.md › Transforms | |
| Discrete cosine transform | covered | part03_mathematics.topics.md › Signals and sequences | |
| Linear time-invariant systems | covered | part03c_signals_systems_and_communications.topics.md › Signals and LTI systems | |
| The z-transform | covered | part03c_signals_systems_and_communications.topics.md › Transforms | |
| FIR and IIR filter design | covered | part03c_signals_systems_and_communications.topics.md › Digital filters | |
| Parametric signal modelling | partial | part03c_signals_systems_and_communications.topics.md › Practical spectral analysis | named only |
| Discrete Hilbert transform | partial | part03c_signals_systems_and_communications.topics.md › Signals and LTI systems | Hilbert transform named only |
| Projective geometry and planar transformations | partial | part19_machine_learning.topics.md › Classical computer vision and geometry | |
| Camera models and calibration | partial | part19_machine_learning.topics.md › Classical computer vision and geometry | |
| Epipolar geometry | covered | part19_machine_learning.topics.md › Classical computer vision and geometry | |
| Fundamental and essential matrices | partial | part19_machine_learning.topics.md › Classical computer vision and geometry | |
| Triangulation and homographies | partial | part19_machine_learning.topics.md › Classical computer vision and geometry | |
| Image formation, photometry and colour | partial | part19_machine_learning.topics.md › Classical computer vision and geometry | |
| Morphological image processing | covered | part03_mathematics.topics.md › Signals and sequences | |
| Histogram equalization | missing | → suggest part19 | |
| Image transforms and wavelets | partial | part03c_signals_systems_and_communications.topics.md › Digital filters | wavelets named only |
| Edge detection and thresholding segmentation | partial | part19_machine_learning.topics.md › Classical computer vision and geometry | |
| Image pyramids | partial | part19_machine_learning.topics.md › Classical computer vision and geometry | |
| Gradients, corners, SIFT and HOG | partial | part19_machine_learning.topics.md › Classical computer vision and geometry | |
| Hough transform, RANSAC and expectation-maximization | partial | part19_machine_learning.topics.md › Classical computer vision and geometry | |
| Kalman filters | partial | part19_machine_learning.topics.md › Classical computer vision and geometry | |
| Structure from motion | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Computer vision: images, motion and multi-view geometry | heading only |
| Stereo depth and 3D reconstruction | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Computer vision: images, motion and multi-view geometry | heading only |
| Mean shift and normalized cuts | partial | part19_machine_learning.topics.md › Classical computer vision and geometry | |
| Feature detection and matching | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Computer vision: images, motion and multi-view geometry | heading only |

## 17.1.9.1 Signals, image and vision audit

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Cepstral analysis | covered | part03c_signals_systems_and_communications.topics.md › Practical spectral analysis | |
| Two-dimensional convolution | partial | part03_mathematics.topics.md › Signals and sequences | one-dimensional convolution only |
| Pixels and image filters | partial | part19_machine_learning.topics.md › Classical computer vision and geometry | |
| OCR and document extraction | covered | part19_machine_learning.topics.md › Applied problem families | |
| Image embeddings | covered | part19_machine_learning.topics.md › Applied problem families | |
| MFCC intuition | covered | part19_machine_learning.topics.md › Applied problem families | |
| Multimodal retrieval | covered | part19_machine_learning.topics.md › Applied problem families | |

## 17.1.10 Speech, ASR and automata

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Gaussian mixture acoustic models | covered | part19_machine_learning.topics.md › Classical machine learning | |
| Hidden Markov models | covered | part19_machine_learning.topics.md › Foundations of AI | |
| Deep neural network acoustic models | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi | |
| Sequence-discriminative training | missing | → suggest part19b | |
| Speaker and environment adaptation | missing | → suggest part19b | |
| N-gram language models | partial | part19_machine_learning.topics.md › NLP foundations | not verified against the source wording |
| Coreference, discourse and sentiment lexicons | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | |
| Information extraction and semantic roles | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | |
| Text-to-speech | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech synthesis, speakers | |
| Finite automata and regular languages | covered | part07_programming_languages_typescript_wire_theory_exercises.topics.md › Language theory | |
| Decidability | covered | part07_programming_languages_typescript_wire_theory_exercises.topics.md › Language theory | |
| Church-Turing thesis | partial | part08_data_structures_algorithms.topics.md › Computability and complexity | |
| Reducibility | partial | part08_data_structures_algorithms.topics.md › Computability and complexity | |
| Time and space complexity | covered | part08_data_structures_algorithms.topics.md › Computability and complexity | |

## 17.1.10.1 Speech, ASR and automata audit

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Speech production and hearing | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech science | |
| PLP feature extraction | missing | → suggest part19b | |
| i-vectors | missing | → suggest part19b | |
| Phonetic decision trees and state clustering | missing | → suggest part19b | |
| Forward-backward algorithm | partial | part19_machine_learning.topics.md › Foundations of AI | Viterbi covered; forward-backward not named |
| Weighted finite-state transducers | partial | part08_data_structures_algorithms.topics.md › Computability and complexity | named in one line |
| Epsilon removal and disambiguation symbols | partial | part08_data_structures_algorithms.topics.md › Computability and complexity | named only |

## 17.1.11 Classical machine learning

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Survival analysis | covered | part19_machine_learning.topics.md › Applied problem families | |
| Cross-validation and model selection | covered | part19_machine_learning.topics.md › Classical machine learning | |
| Regularization and shrinkage | covered | part19_machine_learning.topics.md › Classical machine learning | |
| Logistic regression and generalized linear models | covered | part19_machine_learning.topics.md › Classical machine learning | |
| Naive Bayes, discriminant analysis and k-nearest neighbours | covered | part19_machine_learning.topics.md › Classical machine learning | |
| Support vector machines and kernels | covered | part19_machine_learning.topics.md › Classical machine learning | |
| Random forests and boosting | covered | part19_machine_learning.topics.md › Classical machine learning | |
| Monotonic constraints | covered | part19_machine_learning.topics.md › Classical machine learning | |
| Feature importance | covered | part19_machine_learning.topics.md › Classical machine learning | |
| k-means clustering | covered | part19_machine_learning.topics.md › Classical machine learning | |
| PAC learnability and VC dimension | covered | part19_machine_learning.topics.md › Foundations of AI | |
| Empirical risk minimization | partial | part19_machine_learning.topics.md › Foundations of AI | |
| Uniform convergence | partial | part19_machine_learning.topics.md › Foundations of AI | |
| Bias-complexity tradeoff | partial | part19_machine_learning.topics.md › Foundations of AI | |
| Dimensionality reduction and feature selection | partial | part19_machine_learning.topics.md › Classical machine learning | |
| Graph node embeddings and graph neural networks | partial | part19_machine_learning.topics.md › Specialised learning areas | |

## 17.1.11.1 Classical ML audit

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| DBSCAN | covered | part19_machine_learning.topics.md › Classical machine learning | |
| Isolation forests | covered | part19_machine_learning.topics.md › Classical machine learning | |
| Reconstruction-error anomaly detection | covered | part19_machine_learning.topics.md › Classical machine learning | |
| Inverted indexes and BM25 | covered | part19_machine_learning.topics.md › Applied problem families | |
| Collaborative filtering and matrix factorization | covered | part19_machine_learning.topics.md › Applied problem families | |
| Learning to rank | covered | part19_machine_learning.topics.md › Applied problem families | |
| Approximate nearest neighbour indexes | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | |
| Label propagation and entity resolution | covered | part19_machine_learning.topics.md › Applied problem families | |
| Diversity and fairness in result sets | partial | part19_machine_learning.topics.md › Applied problem families | fairness named; result diversity not taught |
| Exponential smoothing and backtesting | covered | part19_machine_learning.topics.md › Applied problem families | |
| Autoregressive forecasting models | covered | part19_machine_learning.topics.md › Applied problem families | |
| Prediction intervals | covered | part19_machine_learning.topics.md › Applied problem families | |
| Hierarchical forecast reconciliation | missing | → suggest part19 | |

## 17.1.12 Deep learning and sequence models

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Backpropagation and computational graphs | covered | part19_machine_learning.topics.md › Deep learning | |
| GELU and Swish activations | covered | part19_machine_learning.topics.md › Deep learning | |
| Dropout and regularization | covered | part19_machine_learning.topics.md › Deep learning | |
| Batch and layer normalization | covered | part19_machine_learning.topics.md › Deep learning | |
| Residual connections | covered | part19_machine_learning.topics.md › Deep learning | |
| Convolutional networks | covered | part19_machine_learning.topics.md › Deep learning | |
| Recurrent networks, LSTM and GRU | covered | part19_machine_learning.topics.md › Deep learning | |
| Encoder-decoder models | covered | part19_machine_learning.topics.md › Deep learning | |
| Autoencoders | covered | part20_generative_ai_1of3.topics.md › Generative models beyond autoregression | |
| Generative adversarial networks | covered | part20_generative_ai_1of3.topics.md › Generative models beyond autoregression | |
| Normalizing flows | covered | part20_generative_ai_1of3.topics.md › Generative models beyond autoregression | |
| Graph neural networks | partial | part19_machine_learning.topics.md › Specialised learning areas | |
| Self-attention and multi-head attention | covered | part20_generative_ai_1of3.topics.md › How LLMs work | |
| Byte-pair tokenization | covered | part20_generative_ai_1of3.topics.md › How LLMs work | |
| LoRA adapters | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | |
| Instruction fine-tuning and preference data | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | |
| Direct preference optimization | covered | part19_machine_learning.topics.md › Specialised learning areas | |
| Model-as-judge evaluation | covered | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | |
| Prompt engineering | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | |
| Retrieval augmentation and agents | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | |
| Reinforcement learning with verifiable rewards | covered | part19_machine_learning.topics.md › Specialised learning areas | |
| Group-relative policy optimization | covered | part19_machine_learning.topics.md › Specialised learning areas | |
| Distillation to smaller models | partial | part28_ml_case_studies_4of5.topics.md | named in a case study |
| Reward models and RLHF | partial | part28_ml_case_studies_4of5.topics.md | named in a case study |
| Scaling laws | partial | part20_generative_ai_1of3.topics.md › How LLMs work | |
| Context extension | covered | part20_generative_ai_1of3.topics.md › How LLMs work | |
| Quantization concept | covered | part19_machine_learning.topics.md › Specialised learning areas | |
| Flash attention | missing | → suggest part20 | |
| KV caching | covered | Rust_Track_AI_Infrastructure.md › P9. An LLM inference engine | |
| Speculative decoding | partial | Rust_Track_AI_Infrastructure.md › P9. An LLM inference engine | named without a taught mechanism |
| Mixture-of-experts routing | covered | part20_generative_ai_1of3.topics.md › How LLMs work | |
| Grouped-query attention | covered | part20_generative_ai_1of3.topics.md › How LLMs work | |
| Reasoning and tool use | covered | part22_generative_ai_3of3.topics.md › Agents and workflows | |
| Semantic search | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | |
| Text-embedding models | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | |
| Multimodal models | covered | part20_generative_ai_1of3.topics.md › Multimodal models | |

## 17.1.12.1 Deep learning audit

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Diffusion models | covered | part20_generative_ai_1of3.topics.md › Generative models beyond autoregression | |
| Variational autoencoders | covered | part20_generative_ai_1of3.topics.md › Generative models beyond autoregression | |
| RMSNorm | covered | part20_generative_ai_1of3.topics.md › How LLMs work | |
| Rotary position embeddings | covered | part20_generative_ai_1of3.topics.md › How LLMs work | |
| SwiGLU and gated linear units | covered | part20_generative_ai_1of3.topics.md › How LLMs work | |
| Multi-query attention | covered | part20_generative_ai_1of3.topics.md › How LLMs work | |
| Paged attention | missing | → suggest part20 | |
| Continuous batching | covered | Rust_Track_AI_Infrastructure.md › P9. An LLM inference engine | |
| Tensor, pipeline and data parallelism | covered | part20_generative_ai_1of3.topics.md › How LLMs work | |
| Ring all-reduce and collective latency | partial | part20_generative_ai_1of3.topics.md › How LLMs work | all-reduce named only |
| Roofline model and arithmetic intensity | covered | Rust_Track_AI_Infrastructure.md › P9. An LLM inference engine | |
| KV cache memory arithmetic | partial | Rust_Track_AI_Infrastructure.md › P9. An LLM inference engine | cache named; sizing arithmetic not taught |
| Floating-point operation accounting | missing | → suggest part20 | |
| Micro-batch sizing | partial | part20_generative_ai_1of3.topics.md › How LLMs work | micro-batch named only |
| Quantization arithmetic | partial | part19_machine_learning.topics.md › Specialised learning areas | quantization named as a concept only |
| Proximal policy optimization | partial | part19_machine_learning.topics.md › Specialised learning areas | named once in a table |
| Group sequence policy optimization | missing | → suggest part19 | |

## 17.1.13 NLP, information retrieval and GenAI systems

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Term weighting and the vector space model | covered | part19_machine_learning.topics.md › NLP foundations | |
| Text classification with naive Bayes and support vector machines | covered | part19_machine_learning.topics.md › Classical machine learning | |
| Flat and hierarchical clustering | partial | part19_machine_learning.topics.md › Classical machine learning | flat clustering covered; hierarchical not named |
| Latent semantic indexing and matrix decompositions | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Information retrieval engines | |
| Probabilistic retrieval and language models for retrieval | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Information retrieval engines | |
| Relevance feedback and query expansion | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Information retrieval engines | |
| Web search, crawling and link analysis | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Information retrieval engines | |

## 17.1.13.1 NLP, IR and GenAI audit

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Structured outputs | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | |
| Prompt injection | covered | part22_generative_ai_3of3.topics.md › Security and safety | |
| Safety filters | partial | part22_generative_ai_3of3.topics.md › Security and safety | |
| Grammar-constrained decoding | missing | → suggest part21 | |
| Chain-of-thought prompting | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | |
| Self-consistency | partial | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | |
| Tree-of-thought | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | |
| ReAct | covered | part22_generative_ai_3of3.topics.md › Agents and workflows | |
| Index internals: IVF, product quantization and HNSW | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | |
| Cross-encoder reranking | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | |
| QLoRA and four-bit quantized adaptation | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | |
| Adapter-versus-base comparison methodology | partial | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | |
| Cross-attention over text and image | partial | part20_generative_ai_1of3.topics.md › Multimodal models | |
| Vision encoders | partial | part20_generative_ai_1of3.topics.md › Multimodal models | |
| Plan-act-track agent loop | covered | part22_generative_ai_3of3.topics.md › Agents and workflows | |
| Graph orchestration | partial | part22_generative_ai_3of3.topics.md › Agents and workflows | |
| Memory across stateless endpoints | partial | part22_generative_ai_3of3.topics.md › Agents and workflows | |

## 17.1.14 Reinforcement learning, bandits and causality

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Upper confidence bound methods | covered | part19_machine_learning.topics.md › Specialised learning areas | |
| Thompson sampling | covered | part19_machine_learning.topics.md › Specialised learning areas | |
| Contextual and linear bandits | partial | part19_machine_learning.topics.md › Specialised learning areas | |
| Adversarial bandits and exponential-weight algorithms | partial | part19_machine_learning.topics.md › Specialised learning areas | |
| Lower bounds for bandits | partial | part19_machine_learning.topics.md › Specialised learning areas | lower bounds named only in the bandit material |
| Concentration inequalities | covered | part19_machine_learning.topics.md › Classical machine learning | |
| Markov decision processes | covered | part19_machine_learning.topics.md › Specialised learning areas | |
| Dynamic programming and Bellman equations | covered | part19_machine_learning.topics.md › Specialised learning areas | |
| Temporal-difference learning | covered | part19_machine_learning.topics.md › Specialised learning areas | |
| Policy gradient methods | covered | part19_machine_learning.topics.md › Specialised learning areas | |
| Monte Carlo control and off-policy learning | covered | part19_machine_learning.topics.md › Specialised learning areas | |
| Causal graphs and confounding | covered | part19_machine_learning.topics.md › MLOps | |
| Propensity scores and inverse-probability weighting | covered | part19_machine_learning.topics.md › Applied problem families | |
| Instrumental variables | covered | part19_machine_learning.topics.md › Applied problem families | |
| Difference-in-differences | covered | part19_machine_learning.topics.md › Applied problem families | |
| Uplift modelling | covered | part19_machine_learning.topics.md › Applied problem families | |
| Time-varying treatments and g-methods | partial | part19_machine_learning.topics.md › Applied problem families | |
| Target trial emulation | missing | → suggest part19 | |
| Causal mediation | missing | → suggest part19 | |

## 17.1.14.1 RL, bandits and causality audit

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Off-policy evaluation | partial | part19_machine_learning.topics.md › Specialised learning areas | off-policy learning named; evaluation not taught |
| Uplift metrics | partial | part19_machine_learning.topics.md › Applied problem families | uplift modelling covered; uplift metrics not named |

## 17.1.15 Production ML and MLOps

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Data engineering foundations | covered | part19_machine_learning.topics.md › MLOps | |
| Training data sampling and labelling strategy | partial | part19_machine_learning.topics.md › MLOps | |
| Feature engineering | covered | part19_machine_learning.topics.md › MLOps | |
| Offline evaluation | covered | part19_machine_learning.topics.md › MLOps | |
| Prediction-serving patterns | covered | part19_machine_learning.topics.md › MLOps | |
| Data distribution shift and monitoring | covered | part19_machine_learning.topics.md › MLOps | |
| Continual learning in production | partial | part19_machine_learning.topics.md › MLOps | |
| Reproducibility with pinned data, code and environment | covered | part19_machine_learning.topics.md › MLOps | |
| Resilient serving | partial | part19_machine_learning.topics.md › MLOps | |
| Responsible AI and governance | covered | part19_machine_learning.topics.md › MLOps | |
| Feature stores with online and offline parity | covered | part19_machine_learning.topics.md › MLOps | |
| Point-in-time correctness | covered | part19_machine_learning.topics.md › MLOps | |
| Dataset snapshots and experiment tracking | covered | part19_machine_learning.topics.md › MLOps | |
| Model registries with lineage | covered | part19_machine_learning.topics.md › MLOps | |
| Model cards | covered | part19_machine_learning.topics.md › MLOps | |
| Hyperparameter search | covered | part19_machine_learning.topics.md › MLOps | |
| PII minimization | covered | part19_machine_learning.topics.md › MLOps | |
| Consent, retention and deletion | partial | part19_machine_learning.topics.md › MLOps | |
| Bias and fairness | covered | part19_machine_learning.topics.md › MLOps | |
| Human-in-the-loop review | covered | part19_machine_learning.topics.md › MLOps | |
| Audit logs and non-destructive AI actions | partial | part19_machine_learning.topics.md › MLOps | |
| Abuse resistance and red-team tests | partial | part22_generative_ai_3of3.topics.md › Security and safety | |
| Model-abuse detection | missing | → suggest part22 | |

## 17.1.15.1 Production ML audit

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Metric framing | partial | part19_machine_learning.topics.md › MLOps | |
| Incident response and monitoring | covered | part19_machine_learning.topics.md › MLOps | |

## 17.1.17 IIT/IISc institutional cross-check

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Computational complexity theory (graduate) | covered | part08_data_structures_algorithms.topics.md › Computability and complexity | |
| Computer architecture and digital logic | covered | part02_computer_organization.topics.md › Digital logic | |
| Operating system theory | covered | part10_operating_systems.topics.md › Processes and threads | |
| Computer networks theory | partial | part09_networking.topics.md › Transport | |
| Compiler design and programming-language theory | partial | part07_programming_languages_typescript_wire_theory_exercises.topics.md › Language theory | |
| Abstract algebra: groups, rings, fields and Galois theory | missing | → suggest part03 | |
| Point-set and algebraic topology | missing | → suggest part03b | |
| Complex analysis | covered | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis | |
| Measure theory and functional analysis | covered | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis | |
| Differential geometry | missing | → suggest part03b | |
| Mathematical logic and axiomatic set theory | partial | part03_mathematics.topics.md › Proof and discrete mathematics | |
| Combinatorics and graph theory | covered | part03_mathematics.topics.md › Proof and discrete mathematics | |
| Theoretical foundations of cryptography | partial | part14_security.topics.md › Cryptography | |
| Partial differential equations | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | |

## Missing in this range

- Trust-region methods (→ suggest part03) — from: 17.1.8 Optimization and spectral methods
- Subgradients (→ suggest part03) — from: 17.1.8 Optimization and spectral methods
- Mirror descent (→ suggest part03) — from: 17.1.8 Optimization and spectral methods
- ADMM (→ suggest part03) — from: 17.1.8 Optimization and spectral methods
- Histogram equalization (→ suggest part19) — from: 17.1.9 Signals, image processing and vision
- Sequence-discriminative training (→ suggest part19b) — from: 17.1.10 Speech, ASR and automata
- Speaker and environment adaptation (→ suggest part19b) — from: 17.1.10 Speech, ASR and automata
- PLP feature extraction (→ suggest part19b) — from: 17.1.10.1 Speech, ASR and automata audit
- i-vectors (→ suggest part19b) — from: 17.1.10.1 Speech, ASR and automata audit
- Phonetic decision trees and state clustering (→ suggest part19b) — from: 17.1.10.1 Speech, ASR and automata audit
- Hierarchical forecast reconciliation (→ suggest part19) — from: 17.1.11.1 Classical ML audit
- Flash attention (→ suggest part20) — from: 17.1.12 Deep learning and sequence models
- Paged attention (→ suggest part20) — from: 17.1.12.1 Deep learning audit
- Floating-point operation accounting (→ suggest part20) — from: 17.1.12.1 Deep learning audit
- Group sequence policy optimization (→ suggest part19) — from: 17.1.12.1 Deep learning audit
- Grammar-constrained decoding (→ suggest part21) — from: 17.1.13.1 NLP, IR and GenAI audit
- Target trial emulation (→ suggest part19) — from: 17.1.14 Reinforcement learning, bandits and causality
- Causal mediation (→ suggest part19) — from: 17.1.14 Reinforcement learning, bandits and causality
- Model-abuse detection (→ suggest part22) — from: 17.1.15 Production ML and MLOps
- Abstract algebra: groups, rings, fields and Galois theory (→ suggest part03) — from: 17.1.17 IIT/IISc institutional cross-check
- Point-set and algebraic topology (→ suggest part03b) — from: 17.1.17 IIT/IISc institutional cross-check
- Differential geometry (→ suggest part03b) — from: 17.1.17 IIT/IISc institutional cross-check

## Partial in this range

- Generating functions — named only in passing; not taught as a technique — part03_mathematics.topics.md
- Maximum entropy principle — named only — part03_mathematics.topics.md
- Turbo, fountain and convolutional codes — LDPC codes covered; the other code families are not — part03_mathematics.topics.md
- Cramér-Rao bound — Fisher information named; the bound is not stated as a topic — part03_mathematics.topics.md
- Parametric signal modelling — named only — part03c_signals_systems_and_communications.topics.md
- Discrete Hilbert transform — Hilbert transform named only — part03c_signals_systems_and_communications.topics.md
- Projective geometry and planar transformations — partial coverage — part19_machine_learning.topics.md
- Camera models and calibration — partial coverage — part19_machine_learning.topics.md
- Fundamental and essential matrices — partial coverage — part19_machine_learning.topics.md
- Triangulation and homographies — partial coverage — part19_machine_learning.topics.md
- Image formation, photometry and colour — partial coverage — part19_machine_learning.topics.md
- Image transforms and wavelets — wavelets named only — part03c_signals_systems_and_communications.topics.md
- Edge detection and thresholding segmentation — partial coverage — part19_machine_learning.topics.md
- Image pyramids — partial coverage — part19_machine_learning.topics.md
- Gradients, corners, SIFT and HOG — partial coverage — part19_machine_learning.topics.md
- Hough transform, RANSAC and expectation-maximization — partial coverage — part19_machine_learning.topics.md
- Kalman filters — partial coverage — part19_machine_learning.topics.md
- Structure from motion — heading only — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Stereo depth and 3D reconstruction — heading only — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Mean shift and normalized cuts — partial coverage — part19_machine_learning.topics.md
- Feature detection and matching — heading only — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Two-dimensional convolution — one-dimensional convolution only — part03_mathematics.topics.md
- Pixels and image filters — partial coverage — part19_machine_learning.topics.md
- Deep neural network acoustic models — partial coverage — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- N-gram language models — not verified against the source wording — part19_machine_learning.topics.md
- Coreference, discourse and sentiment lexicons — partial coverage — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Information extraction and semantic roles — partial coverage — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Church-Turing thesis — partial coverage — part08_data_structures_algorithms.topics.md
- Reducibility — partial coverage — part08_data_structures_algorithms.topics.md
- Speech production and hearing — partial coverage — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Forward-backward algorithm — Viterbi covered; forward-backward not named — part19_machine_learning.topics.md
- Weighted finite-state transducers — named in one line — part08_data_structures_algorithms.topics.md
- Epsilon removal and disambiguation symbols — named only — part08_data_structures_algorithms.topics.md
- Empirical risk minimization — partial coverage — part19_machine_learning.topics.md
- Uniform convergence — partial coverage — part19_machine_learning.topics.md
- Bias-complexity tradeoff — partial coverage — part19_machine_learning.topics.md
- Dimensionality reduction and feature selection — partial coverage — part19_machine_learning.topics.md
- Graph node embeddings and graph neural networks — partial coverage — part19_machine_learning.topics.md
- Diversity and fairness in result sets — fairness named; result diversity not taught — part19_machine_learning.topics.md
- Graph neural networks — partial coverage — part19_machine_learning.topics.md
- Distillation to smaller models — named in a case study — part28_ml_case_studies_4of5.topics.md
- Reward models and RLHF — named in a case study — part28_ml_case_studies_4of5.topics.md
- Scaling laws — partial coverage — part20_generative_ai_1of3.topics.md
- Speculative decoding — named without a taught mechanism — Rust_Track_AI_Infrastructure.md
- Ring all-reduce and collective latency — all-reduce named only — part20_generative_ai_1of3.topics.md
- KV cache memory arithmetic — cache named; sizing arithmetic not taught — Rust_Track_AI_Infrastructure.md
- Micro-batch sizing — micro-batch named only — part20_generative_ai_1of3.topics.md
- Quantization arithmetic — quantization named as a concept only — part19_machine_learning.topics.md
- Proximal policy optimization — named once in a table — part19_machine_learning.topics.md
- Flat and hierarchical clustering — flat clustering covered; hierarchical not named — part19_machine_learning.topics.md
- Latent semantic indexing and matrix decompositions — partial coverage — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Probabilistic retrieval and language models for retrieval — partial coverage — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Relevance feedback and query expansion — partial coverage — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Web search, crawling and link analysis — partial coverage — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Safety filters — partial coverage — part22_generative_ai_3of3.topics.md
- Self-consistency — partial coverage — part21_generative_ai_2of3.topics.md
- Adapter-versus-base comparison methodology — partial coverage — part20_generative_ai_1of3.topics.md
- Cross-attention over text and image — partial coverage — part20_generative_ai_1of3.topics.md
- Vision encoders — partial coverage — part20_generative_ai_1of3.topics.md
- Graph orchestration — partial coverage — part22_generative_ai_3of3.topics.md
- Memory across stateless endpoints — partial coverage — part22_generative_ai_3of3.topics.md
- Contextual and linear bandits — partial coverage — part19_machine_learning.topics.md
- Adversarial bandits and exponential-weight algorithms — partial coverage — part19_machine_learning.topics.md
- Lower bounds for bandits — lower bounds named only in the bandit material — part19_machine_learning.topics.md
- Time-varying treatments and g-methods — partial coverage — part19_machine_learning.topics.md
- Off-policy evaluation — off-policy learning named; evaluation not taught — part19_machine_learning.topics.md
- Uplift metrics — uplift modelling covered; uplift metrics not named — part19_machine_learning.topics.md
- Training data sampling and labelling strategy — partial coverage — part19_machine_learning.topics.md
- Continual learning in production — partial coverage — part19_machine_learning.topics.md
- Resilient serving — partial coverage — part19_machine_learning.topics.md
- Consent, retention and deletion — partial coverage — part19_machine_learning.topics.md
- Audit logs and non-destructive AI actions — partial coverage — part19_machine_learning.topics.md
- Abuse resistance and red-team tests — partial coverage — part22_generative_ai_3of3.topics.md
- Metric framing — partial coverage — part19_machine_learning.topics.md
- Computer networks theory — partial coverage — part09_networking.topics.md
- Compiler design and programming-language theory — partial coverage — part07_programming_languages_typescript_wire_theory_exercises.topics.md
- Mathematical logic and axiomatic set theory — partial coverage — part03_mathematics.topics.md
- Theoretical foundations of cryptography — partial coverage — part14_security.topics.md

