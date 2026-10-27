# Topic diff: Python and NLP libraries, statistical techniques, IIT knowledge bank

Source: gcp/unified-curriculum.md lines 3407-3789. Compared against: gcp-lite/index/*.topics.md and gcp-lite/Rust_Track_AI_Infrastructure.md.

Counts: 197 topics; 123 covered, 31 partial, 43 missing, 0 out of scope.

## Core numerical and data

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| NumPy arrays, indexing and broadcasting | covered | part05_programming_languages_python_and_shell.topics.md › Python | - |
| NumPy linear algebra (inv, det, eig, solve, norm) | partial | part05_programming_languages_python_and_shell.topics.md › Python | Linear-algebra routines named in passing only; the numpy.linalg API is not taught |
| Pandas joins, groupby and cleaning | covered | part05_programming_languages_python_and_shell.topics.md › Python | - |
| SciPy optimization, statistics and signal processing | missing | → suggest part05 | - |

## Visualization and EDA

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Matplotlib basic plots (line, bar, scatter, histogram) | covered | part05_programming_languages_python_and_shell.topics.md › Python | - |
| Matplotlib subplots, GridSpec, contour, heatmap, savefig | partial | part05_programming_languages_python_and_shell.topics.md › Python | Only line, scatter and histogram named |
| Seaborn statistical plots | missing | → suggest part05 | - |
| Plotly interactive dashboards | missing | → suggest part05 | - |

## Classical ML

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| scikit-learn estimator API and pipelines | covered | part19_machine_learning.topics.md › Machine learning in Python | - |
| scikit-learn preprocessing (scalers, one-hot, imputer, ColumnTransformer) | covered | part19_machine_learning.topics.md › Machine learning in Python | - |
| Hyperparameter search and cross-validation | covered | part19_machine_learning.topics.md › Machine learning in Python | GridSearchCV, RandomizedSearchCV, cross_val_score |
| Classification metrics (confusion matrix, ROC-AUC, PR) | covered | part19_machine_learning.topics.md › Classical machine learning | Evaluation group |
| Classical supervised models (SVM, trees, forests, k-NN) | covered | part19_machine_learning.topics.md › Classical machine learning | Other supervised models; trees and ensembles |
| Clustering and mixture models (k-means, DBSCAN, GMM) | covered | part19_machine_learning.topics.md › Classical machine learning | Unsupervised learning group |
| t-SNE visualization | covered | part19_machine_learning.topics.md › Classical machine learning | Taught for visualization only |
| XGBoost gradient boosting library | partial | part19_machine_learning.topics.md › Classical machine learning | Gradient boosting taught as a concept; XGBoost itself not named |
| LightGBM | missing | → suggest part19 | - |

## Deep learning

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| TensorFlow and Keras | missing | → suggest part19 | Named only in a case study (part29) |
| PyTorch tensors, autograd and training loop | covered | part19_machine_learning.topics.md › Machine learning in Python | - |

## NLP and transformers

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Hugging Face Transformers library | partial | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | Named as a library only; Auto classes, pipelines and the Hub are not taught |
| spaCy industrial NLP pipelines | missing | → suggest part19 | - |
| NLTK as the classical NLP library | partial | part19_machine_learning.topics.md › Machine learning in Python | Named for tokenizers, stop words and stemmers; Punkt and word_tokenize not taught |

## Data engineering

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| PySpark distributed processing | missing | → suggest part19 | Spark appears only as a managed service (part23, part24) and as a paper system (part13) |
| Dask parallel arrays and dataframes | missing | → suggest part19 | - |

## MLOps

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| MLflow experiment tracking and model registry | partial | part19_machine_learning.topics.md › MLOps | Tracking and registries taught generically; the MLflow tool is not named |
| Weights & Biases experiment monitoring | missing | → suggest part19 | - |
| Evidently drift monitoring | partial | part19_machine_learning.topics.md › MLOps | Drift types and KS and PSI tests taught; the Evidently tool is not named |

## Deployment and agentic add-ons

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| FastAPI model APIs | covered | part05_programming_languages_python_and_shell.topics.md › Python | - |
| LangChain orchestration | covered | part22_generative_ai_3of3.topics.md › Agents and workflows | LangChain and LangGraph group |
| LlamaIndex RAG pipelines | missing | → suggest part21 | - |
| vLLM paged LLM serving | covered | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | - |
| Ray distributed AI workloads | missing | → suggest part22 | - |

## Shared text-processing substrate

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Unicode code points and UTF-8 | covered | part02_computer_organization.topics.md › Data representation | - |
| Unicode normalization, case folding and mojibake | partial | part06_programming_languages_go.topics.md › Go — composite data, functions, errors and text | Normalization and case folding taught for Go strings only; mojibake and NLP text cleanup not taught |
| Raw text acquisition (HTML stripping, PDF vs OCR routing) | partial | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | Taught for RAG ingestion; the raw, token, sentence and annotated corpus forms are not |
| Regular expressions for text extraction | partial | part06_programming_languages_go.topics.md › Go — the everyday standard library | Go RE2 regexp only; anchors, greedy vs non-greedy closures and tokenizing regex not taught |
| Stemming and lemmatization | covered | part19_machine_learning.topics.md › Natural language processing foundations | - |
| Stop-word removal | partial | part19_machine_learning.topics.md › Natural language processing foundations | Named as a pipeline step only |
| Vocabulary cutoffs and UNK replacement | missing | → suggest part19 | - |
| Sentence segmentation | missing | → suggest part19 | - |
| Word and subword tokenization | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Span offsets and character alignment | missing | → suggest part19 | - |
| Span-level evaluation (precision, recall, F1) | partial | part19_machine_learning.topics.md › Classical machine learning | Classification precision, recall and F1 taught; span-level NER scoring and error propagation not |

## NLTK theory

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| NLTK corpus interfaces (raw, words, sents, tagged) | missing | → suggest part19 | - |
| Frequency distributions and conditional counts (FreqDist, ConditionalFreqDist) | missing | → suggest part19 | - |
| WordNet synsets and hypernyms | partial | part19_machine_learning.topics.md › Natural language processing foundations | WordNet and synsets named; hypernym traversal and similarity not |
| Treebanks and annotated corpora (Penn, Brown, CoNLL) | missing | → suggest part19 | - |
| POS tagging with hidden Markov models | covered | part19_machine_learning.topics.md › Natural language processing foundations | Viterbi decoding named |
| Tagsets (Universal, Penn Treebank, Brown) | missing | → suggest part19 | - |
| Baseline taggers and backoff chains | missing | → suggest part19 | Default, regex, lookup and unigram to trigram taggers |
| Brill transformation-based tagging | missing | → suggest part19 | - |
| Sequence labelling as per-token prediction | covered | part19_machine_learning.topics.md › Natural language processing foundations | CRF and BIO tagging named |

## spaCy theory

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| spaCy object model (Doc, Token, Span, Vocab) | missing | → suggest part19 | - |
| spaCy tokenizer design and exceptions | missing | → suggest part19 | - |
| Token alignment across tokenizers | missing | → suggest part19 | - |
| spaCy processing pipeline components | missing | → suggest part19 | - |
| Dependency parsing (transition-based, graph-based) | covered | part19_machine_learning.topics.md › Natural language processing foundations | UAS and LAS named |
| Noun chunks | missing | → suggest part19 | - |
| BIO and BILUO entity encodings | partial | part19_machine_learning.topics.md › Natural language processing foundations | BIO taught; BILUO not |
| Rule-based matching (Matcher, PhraseMatcher, EntityRuler) | missing | → suggest part19 | - |
| spaCy efficiency (nlp.pipe, batching, disabling components) | missing | → suggest part19 | - |
| Entity linking | covered | part19_machine_learning.topics.md › Natural language processing foundations | Information extraction group |

## Hugging Face Tokenizers theory

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Tokenizer pipeline stages (normalizer to decoder) | missing | → suggest part20 | - |
| Subword models (WordPiece, BPE, Unigram) | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Encoding outputs (attention masks, padding, truncation) | partial | part20_generative_ai_1of3.topics.md › How LLMs work | Special tokens named in the BPE bullet; masks, padding and truncation not |
| Word-to-subword label alignment | missing | → suggest part20 | - |
| Tokenizer and checkpoint mismatch | missing | → suggest part20 | - |

## Hugging Face Transformers theory

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Model inputs and outputs (token IDs, logits, hidden states) | partial | part20_generative_ai_1of3.topics.md › How LLMs work | Key–value cache covered; logits and hidden states as named outputs not |
| Task heads (classification, token classification, QA) | partial | part20_generative_ai_1of3.topics.md › How LLMs work | Pretraining heads (MLM, causal LM, span corruption) taught; fine-tuning heads not |
| Pipelines abstraction | missing | → suggest part20 | - |
| Fine-tuning workflow (collators, Trainer, dynamic padding) | partial | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | Hyperparameters, instruction data and held-out evaluation covered; Trainer, collator, dynamic padding and callbacks not |
| Generation and decoding (greedy, beam, top-k, top-p, penalties) | covered | part20_generative_ai_1of3.topics.md › How LLMs work | Includes temperature, stop sequences and max length |
| Structured output constraints | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | JSON Schema-constrained outputs |
| Chat templates | partial | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | Named in one training-data bullet only |
| LoRA, QLoRA and PEFT | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | - |
| Mixed precision training | missing | → suggest part20 | - |
| Serving concerns (quantization, GPU memory, batching) | partial | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | GPU memory budgeting in the vLLM bullet; quantization is in part20; device maps and batching not taught |
| Task evaluation harness (classification, NER, generation) | partial | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | Golden datasets and graders covered; task-specific harnesses not |

## Cross-library selection and integration

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Choosing NLTK, spaCy or Hugging Face by goal | missing | → suggest part19 | - |
| Shared contracts (tokenization, offsets, labels, splits) | partial | part19_machine_learning.topics.md › Classical machine learning | Honest splits covered; tokenization, offset and label contracts across libraries not |

## 5. Statistical techniques

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Descriptive statistics (mean, median, mode, spread) | covered | part01_school_foundations.topics.md › Probability and data (bullet; no ### group) | School-level |
| Skewness and kurtosis | missing | → suggest part03 | - |
| Quantiles and percentiles | covered | part03_mathematics.topics.md › Statistics and experimental design | IQR not named |
| Conditional probability and Bayes' theorem | covered | part03_mathematics.topics.md › Probability | - |
| Law of total probability | missing | → suggest part03 | - |
| Joint and marginal probability | covered | part03_mathematics.topics.md › Probability | - |
| Normal, Bernoulli, binomial, Poisson, uniform and exponential distributions | covered | part03_mathematics.topics.md › Probability | - |
| Log-normal and multinomial distributions | missing | → suggest part03 | - |
| Random and stratified sampling | partial | part03_mathematics.topics.md › Probability | Sampling from distributions covered; survey sampling designs (stratified, cluster) not |
| Central limit theorem | covered | part03_mathematics.topics.md › Probability | - |
| Confidence intervals | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Hypothesis testing and p-values | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Type I and Type II errors | missing | → suggest part03 | Power is covered; the error types are not named |
| Statistical power and sample size | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| One-sample and two-sample t-tests | missing | → suggest part03 | - |
| z-test | missing | → suggest part03 | - |
| Chi-square tests | partial | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | Only McNemar's chi-square test named |
| ANOVA | missing | → suggest part03 | - |
| Mann-Whitney U test | missing | → suggest part03 | - |
| Wilcoxon signed-rank test | missing | → suggest part03 | - |
| Covariance | covered | part03_mathematics.topics.md › Probability | - |
| Pearson and Spearman correlation | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Kendall tau correlation | missing | → suggest part03 | - |
| Linear and multiple linear regression | covered | part19_machine_learning.topics.md › Classical machine learning | Least squares and normal equations |
| Logistic regression | covered | part19_machine_learning.topics.md › Classical machine learning | Linear models group |
| Ridge and lasso regression | covered | part19_machine_learning.topics.md › Classical machine learning | Regularization as a constraint |
| Polynomial regression | covered | part19_machine_learning.topics.md › Classical machine learning | Polynomial features with ridge |
| Bayesian inference (prior and posterior) | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Markov chain Monte Carlo | partial | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning | Gibbs sampling named for Bayesian networks and LDA; general MCMC and Metropolis-Hastings not |

## 6.1 NLP foundations

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Text representation ladder (bag of words, TF-IDF, Word2Vec, embeddings) | covered | part19_machine_learning.topics.md › Natural language processing foundations | - |
| Language modelling and n-gram models | covered | part20_generative_ai_1of3.topics.md › How LLMs work | Autoregressive factorization; n-gram models |
| Classical NLP pipeline (clean, tokenize, stop words, lemmatize, classify) | covered | part19_machine_learning.topics.md › Natural language processing foundations | - |
| Agent loop (observe, reason, act) | covered | part22_generative_ai_3of3.topics.md › Agents and workflows | Plan, act, observe and track |

## 6.2 AI history and classical knowledge

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Dartmouth workshop and the Turing test | covered | part19_machine_learning.topics.md › Foundations of AI | - |
| Four views of AI (thinking or acting, humanly or rationally) | covered | part19_machine_learning.topics.md › Foundations of AI | - |
| Knowledge representation and expert systems | covered | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning | - |
| AI winters and boom–bust cycles | covered | part19_machine_learning.topics.md › Foundations of AI | - |
| Mitchell's learning definition (experience, task, performance) | covered | part19_machine_learning.topics.md › Foundations of AI | - |

## 6.3 Supervised / unsupervised / RL and classical ML

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Supervised, unsupervised and reinforcement learning | covered | part19_machine_learning.topics.md › Classical machine learning | Learning paradigms |
| Supervised ML workflow (features, fit, held-out test) | covered | part19_machine_learning.topics.md › Foundations of AI | The supervised workflow bullet |
| Anomaly detection and association rules | covered | part19_machine_learning.topics.md › Classical machine learning | Unsupervised learning and anomaly detection |
| Recommender systems (item-item, matrix factorization) | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Bias–variance tradeoff | covered | part19_machine_learning.topics.md › Classical machine learning | Learning theory |
| Regularization (L1, L2, dropout, early stopping) | covered | part19_machine_learning.topics.md › Classical machine learning | Ridge and lasso in learning theory; dropout and early stopping in the Deep learning group |
| Curse of dimensionality | covered | part19_machine_learning.topics.md › Classical machine learning | Dimensionality reduction group |
| Hand-crafted features vs learned embeddings | partial | part19_machine_learning.topics.md › Classical machine learning | Feature engineering taught; the contrast with learned dense embeddings not stated |

## 6.4 Embeddings and text representations

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| One-hot and bag-of-words limits | covered | part19_machine_learning.topics.md › Natural language processing foundations | Sparsity, lost order, orthogonal vectors |
| Dense embeddings and cosine similarity | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | - |
| Embedding analogies and geometry | covered | part19_machine_learning.topics.md › Natural language processing foundations | Vector analogies |
| Contextual embeddings (ELMo, then transformers) | covered | part19_machine_learning.topics.md › Natural language processing foundations | - |

## 6.5 Neural nets

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Perceptron and linear separability | covered | part19_machine_learning.topics.md › Deep learning | - |
| Multilayer perceptrons and activation functions | covered | part19_machine_learning.topics.md › Deep learning | - |
| Backpropagation and the chain rule | covered | part19_machine_learning.topics.md › Deep learning | - |
| Loss functions (MSE, cross-entropy) | covered | part19_machine_learning.topics.md › Deep learning | - |
| Gradient-descent optimizers (SGD, Adam, RMSProp) | covered | part19_machine_learning.topics.md › Deep learning | - |
| Vanishing gradients and local minima | partial | part19_machine_learning.topics.md › Deep learning | Vanishing gradients taught; local minima not named in this group |

## 6.6 Transformers

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Seq2seq fixed-length context bottleneck | covered | part19_machine_learning.topics.md › Deep learning | - |
| Bahdanau additive attention | covered | part19_machine_learning.topics.md › Deep learning | Attention over encoder states |
| Self-attention, cross-attention and multi-head attention | covered | part20_generative_ai_1of3.topics.md › How LLMs work | Scaled dot-product with Q, K, V |
| Positional encodings | covered | part20_generative_ai_1of3.topics.md › How LLMs work | Sinusoidal and learned position tables |
| Causal masking | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Transformer blocks (residual, layer norm, feed-forward) | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Autoregressive generation loop | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |

## 6.7 Foundation models, decoding, APIs

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Architecture families (encoder-only, decoder-only, encoder–decoder) | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Pretraining objectives (MLM, causal LM, span corruption) | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| In-context learning (zero-, one-, few-shot) | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Scaling laws and compute-optimal training | covered | part20_generative_ai_1of3.topics.md › How LLMs work | Chinchilla named |
| Instruction tuning and RLHF | covered | part20_generative_ai_1of3.topics.md › How LLMs work | SFT, reward model and PPO (Alignment) |
| Open-weight families and mixture of experts | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Reasoning models and inference-time compute | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Multimodal models (CLIP, ViT, Whisper) | covered | part20_generative_ai_1of3.topics.md › Multimodal models | - |
| Benchmarks (GLUE, MMLU, LAMBADA) | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Function calling and tool-use APIs | covered | part21_generative_ai_2of3.topics.md › Tools and the Model Context Protocol | - |
| Chat completion and messages APIs | covered | part21_generative_ai_2of3.topics.md › Model APIs | OpenAI-compatible chat APIs group |

## 6.8 LLM evaluation and safety

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Output quality vs system performance | covered | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | - |
| Inter-annotator agreement (Cohen's kappa, Fleiss, Krippendorff) | covered | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | - |
| ROUGE-N and ROUGE-L | covered | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | Reference-based text metrics |
| BLEU | covered | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | Reference-based text metrics |
| METEOR | covered | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | Reference-based text metrics |
| BERTScore | covered | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | Reference-based text metrics |
| LLM-as-a-judge | partial | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | Model-graded grading named; judge prompts with rationale and score not taught |
| Jailbreak taxonomy and black-box attacks | covered | part14_security.topics.md › AI and LLM application threats | Includes low-resource-language attacks |
| GCG and AutoDAN adversarial suffixes | covered | part14_security.topics.md › AI and LLM application threats | - |
| PAIR iterative black-box refinement | covered | part14_security.topics.md › AI and LLM application threats | - |
| Direct and indirect prompt injection | covered | part14_security.topics.md › AI and LLM application threats | - |
| Prompt leakage | covered | part14_security.topics.md › AI and LLM application threats | - |

## 6.9 Prompting

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Prompt elements, system and user prompts | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| Zero-shot and few-shot prompting | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| Chain-of-thought and Auto-CoT | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | Reasoning techniques group |
| Self-consistency | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| Tree of Thoughts | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| ReAct | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | Also in part22 agents |
| Meta prompting | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| Directional stimulus prompting | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |

## 6.10 Prompt optimization and security

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Verbalized sampling for mode collapse | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| Prompt compression (LLMLingua, LLMLingua-2) | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| Automatic prompt optimization (APE, ProTeGi, DSPy) | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | Manual vs automatic loops |
| Prompt scorers: statistical vs model-based | partial | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | Evals on every change covered; scorer types not distinguished |
| Prompt security defenses | partial | part22_generative_ai_3of3.topics.md › Security and safety of LLM applications | Least-privilege tools and output guardrails covered; instruction hierarchy not named |

## 6.11 Retrieval-augmented generation

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| RAG rationale (hallucination, stale knowledge, private data) | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | - |
| Naive and advanced RAG pipelines | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | - |
| Document ingestion and OCR routing | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | Document parsing group |
| Chunking strategies | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | Fixed, sentence, semantic and parent–child |
| Sparse, dense and hybrid retrieval (BM25) | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | Reciprocal rank fusion |
| Cross-encoder reranking | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | Two-stage retrieval |
| Query rewriting and conversational rewriting | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | Query transformation |
| Multi-query expansion and RAG-Fusion | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | - |
| Step-back prompting for retrieval | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | - |
| HyDE hypothetical-document retrieval | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | - |
| IVF inverted-file index | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | - |
| Product quantization | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | - |
| HNSW graph index | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | - |
| FAISS vs Chroma | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | Library vs database |
| RAG evaluation (context precision and recall, faithfulness) | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | - |
| Agentic RAG (retrieval as a tool) | covered | part22_generative_ai_3of3.topics.md › Agents and workflows | - |
| Triage agent pattern | covered | part22_generative_ai_3of3.topics.md › Agents and workflows | Specialists return to triage |
| Enterprise RAG intent routing | partial | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | Query routing covered; per-source isolation and enterprise assembly not |

## Missing in this range

- SciPy optimization, statistics and signal processing (→ suggest part05) — from: Core numerical and data
- Seaborn statistical plots (→ suggest part05) — from: Visualization and EDA
- Plotly interactive dashboards (→ suggest part05) — from: Visualization and EDA
- LightGBM (→ suggest part19) — from: Classical ML
- TensorFlow and Keras (→ suggest part19) — from: Deep learning
- spaCy industrial NLP pipelines (→ suggest part19) — from: NLP and transformers
- PySpark distributed processing (→ suggest part19) — from: Data engineering
- Dask parallel arrays and dataframes (→ suggest part19) — from: Data engineering
- Weights & Biases experiment monitoring (→ suggest part19) — from: MLOps
- LlamaIndex RAG pipelines (→ suggest part21) — from: Deployment and agentic add-ons
- Ray distributed AI workloads (→ suggest part22) — from: Deployment and agentic add-ons
- Vocabulary cutoffs and UNK replacement (→ suggest part19) — from: Shared text-processing substrate
- Sentence segmentation (→ suggest part19) — from: Shared text-processing substrate
- Span offsets and character alignment (→ suggest part19) — from: Shared text-processing substrate
- NLTK corpus interfaces (raw, words, sents, tagged) (→ suggest part19) — from: NLTK theory
- Frequency distributions and conditional counts (FreqDist, ConditionalFreqDist) (→ suggest part19) — from: NLTK theory
- Treebanks and annotated corpora (Penn, Brown, CoNLL) (→ suggest part19) — from: NLTK theory
- Tagsets (Universal, Penn Treebank, Brown) (→ suggest part19) — from: NLTK theory
- Baseline taggers and backoff chains (→ suggest part19) — from: NLTK theory
- Brill transformation-based tagging (→ suggest part19) — from: NLTK theory
- spaCy object model (Doc, Token, Span, Vocab) (→ suggest part19) — from: spaCy theory
- spaCy tokenizer design and exceptions (→ suggest part19) — from: spaCy theory
- Token alignment across tokenizers (→ suggest part19) — from: spaCy theory
- spaCy processing pipeline components (→ suggest part19) — from: spaCy theory
- Noun chunks (→ suggest part19) — from: spaCy theory
- Rule-based matching (Matcher, PhraseMatcher, EntityRuler) (→ suggest part19) — from: spaCy theory
- spaCy efficiency (nlp.pipe, batching, disabling components) (→ suggest part19) — from: spaCy theory
- Tokenizer pipeline stages (normalizer to decoder) (→ suggest part20) — from: Hugging Face Tokenizers theory
- Word-to-subword label alignment (→ suggest part20) — from: Hugging Face Tokenizers theory
- Tokenizer and checkpoint mismatch (→ suggest part20) — from: Hugging Face Tokenizers theory
- Pipelines abstraction (→ suggest part20) — from: Hugging Face Transformers theory
- Mixed precision training (→ suggest part20) — from: Hugging Face Transformers theory
- Choosing NLTK, spaCy or Hugging Face by goal (→ suggest part19) — from: Cross-library selection and integration
- Skewness and kurtosis (→ suggest part03) — from: 5. Statistical techniques
- Law of total probability (→ suggest part03) — from: 5. Statistical techniques
- Log-normal and multinomial distributions (→ suggest part03) — from: 5. Statistical techniques
- Type I and Type II errors (→ suggest part03) — from: 5. Statistical techniques
- One-sample and two-sample t-tests (→ suggest part03) — from: 5. Statistical techniques
- z-test (→ suggest part03) — from: 5. Statistical techniques
- ANOVA (→ suggest part03) — from: 5. Statistical techniques
- Mann-Whitney U test (→ suggest part03) — from: 5. Statistical techniques
- Wilcoxon signed-rank test (→ suggest part03) — from: 5. Statistical techniques
- Kendall tau correlation (→ suggest part03) — from: 5. Statistical techniques


## Partial in this range

- NumPy linear algebra (inv, det, eig, solve, norm) — Linear-algebra routines named in passing only; the numpy.linalg API is not taught — part05_programming_languages_python_and_shell.topics.md
- Matplotlib subplots, GridSpec, contour, heatmap, savefig — Only line, scatter and histogram named — part05_programming_languages_python_and_shell.topics.md
- XGBoost gradient boosting library — Gradient boosting taught as a concept; XGBoost itself not named — part19_machine_learning.topics.md
- Hugging Face Transformers library — Named as a library only; Auto classes, pipelines and the Hub are not taught — part20_generative_ai_1of3.topics.md
- NLTK as the classical NLP library — Named for tokenizers, stop words and stemmers; Punkt and word_tokenize not taught — part19_machine_learning.topics.md
- MLflow experiment tracking and model registry — Tracking and registries taught generically; the MLflow tool is not named — part19_machine_learning.topics.md
- Evidently drift monitoring — Drift types and KS and PSI tests taught; the Evidently tool is not named — part19_machine_learning.topics.md
- Unicode normalization, case folding and mojibake — Normalization and case folding taught for Go strings only; mojibake and NLP text cleanup not taught — part06_programming_languages_go.topics.md
- Raw text acquisition (HTML stripping, PDF vs OCR routing) — Taught for RAG ingestion; the raw, token, sentence and annotated corpus forms are not — part21_generative_ai_2of3.topics.md
- Regular expressions for text extraction — Go RE2 regexp only; anchors, greedy vs non-greedy closures and tokenizing regex not taught — part06_programming_languages_go.topics.md
- Stop-word removal — Named as a pipeline step only — part19_machine_learning.topics.md
- Span-level evaluation (precision, recall, F1) — Classification precision, recall and F1 taught; span-level NER scoring and error propagation not — part19_machine_learning.topics.md
- WordNet synsets and hypernyms — WordNet and synsets named; hypernym traversal and similarity not — part19_machine_learning.topics.md
- BIO and BILUO entity encodings — BIO taught; BILUO not — part19_machine_learning.topics.md
- Encoding outputs (attention masks, padding, truncation) — Special tokens named in the BPE bullet; masks, padding and truncation not — part20_generative_ai_1of3.topics.md
- Model inputs and outputs (token IDs, logits, hidden states) — Key–value cache covered; logits and hidden states as named outputs not — part20_generative_ai_1of3.topics.md
- Task heads (classification, token classification, QA) — Pretraining heads (MLM, causal LM, span corruption) taught; fine-tuning heads not — part20_generative_ai_1of3.topics.md
- Fine-tuning workflow (collators, Trainer, dynamic padding) — Hyperparameters, instruction data and held-out evaluation covered; Trainer, collator, dynamic padding and callbacks not — part20_generative_ai_1of3.topics.md
- Chat templates — Named in one training-data bullet only — part20_generative_ai_1of3.topics.md
- Serving concerns (quantization, GPU memory, batching) — GPU memory budgeting in the vLLM bullet; quantization is in part20; device maps and batching not taught — part22_generative_ai_3of3.topics.md
- Task evaluation harness (classification, NER, generation) — Golden datasets and graders covered; task-specific harnesses not — part22_generative_ai_3of3.topics.md
- Shared contracts (tokenization, offsets, labels, splits) — Honest splits covered; tokenization, offset and label contracts across libraries not — part19_machine_learning.topics.md
- Random and stratified sampling — Sampling from distributions covered; survey sampling designs (stratified, cluster) not — part03_mathematics.topics.md
- Chi-square tests — Only McNemar's chi-square test named — part22_generative_ai_3of3.topics.md
- Markov chain Monte Carlo — Gibbs sampling named for Bayesian networks and LDA; general MCMC and Metropolis-Hastings not — part19_machine_learning.topics.md
- Hand-crafted features vs learned embeddings — Feature engineering taught; the contrast with learned dense embeddings not stated — part19_machine_learning.topics.md
- Vanishing gradients and local minima — Vanishing gradients taught; local minima not named in this group — part19_machine_learning.topics.md
- LLM-as-a-judge — Model-graded grading named; judge prompts with rationale and score not taught — part22_generative_ai_3of3.topics.md
- Prompt scorers: statistical vs model-based — Evals on every change covered; scorer types not distinguished — part21_generative_ai_2of3.topics.md
- Prompt security defenses — Least-privilege tools and output guardrails covered; instruction hierarchy not named — part22_generative_ai_3of3.topics.md
- Enterprise RAG intent routing — Query routing covered; per-source isolation and enterprise assembly not — part21_generative_ai_2of3.topics.md

