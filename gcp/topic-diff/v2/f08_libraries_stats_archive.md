# Topic diff f08: Libraries, statistics, knowledge bank and archive inventory

Curriculum range: `gcp/unified-curriculum.md` lines 3407-3847 (§4, §4A, §5, §6, §7, the §17.1 research-addition block).
Compared against: `gcp-lite/index/*.topics.md` and `gcp-lite/Rust_Track_AI_Infrastructure.md`.

Counts: covered 195 | partial 44 | missing 23 | out of scope 8 | total 270

Rust track notes: the Rust track builds several of these from scratch (P7 tensor library and autograd, P8 byte-level BPE tokenizer, P9 LLM inference engine, P10 continuous batching, P11 vector database). Those projects are cited in notes only; the status column reflects the Python-side topic files, which the curriculum names directly.

## Core numerical and data

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| NumPy arrays, broadcasting, masks, reshape, save/load | covered | part05_programming_languages_python_and_shell.topics.md › Python | ndarray and broadcasting named |
| NumPy linear algebra (linalg.inv, det, eig, norm, solve) | covered | part05_programming_languages_python_and_shell.topics.md › Python | linalg, eig and solve named |
| Pandas joins, groupby and cleaning | covered | part05_programming_languages_python_and_shell.topics.md › Python | DataFrames, grouping, joins, missing values |
| SciPy optimization and statistics | covered | part05_programming_languages_python_and_shell.topics.md › Python | scipy.optimize and scipy.stats |
| SciPy signal processing | partial | part05_programming_languages_python_and_shell.topics.md › Python | scipy.signal not named; signal processing taught in part03c_signals_systems_and_communications.topics.md › Signals and linear time-invariant systems |

## Visualization and EDA

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Matplotlib line, scatter, histogram, contour, heatmap | covered | part05_programming_languages_python_and_shell.topics.md › Python | subplots and GridSpec named |
| Matplotlib 3D plots and savefig | partial | part05_programming_languages_python_and_shell.topics.md › Python | not named in the Python section |
| Seaborn statistical plots | covered | part05_programming_languages_python_and_shell.topics.md › Python | distribution, categorical and regression plots |
| Plotly interactive dashboards | covered | part05_programming_languages_python_and_shell.topics.md › Python | interactive figures with hover and zoom |

## Classical ML

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| scikit-learn estimator protocol (fit, transform, predict) and Pipeline | covered | part19_machine_learning.topics.md › Machine learning in Python | ColumnTransformer and Pipeline named |
| Preprocessing: StandardScaler, MinMaxScaler, OneHotEncoder, imputer | covered | part19_machine_learning.topics.md › Machine learning in Python | all named |
| SVM, k-NN, linear and logistic regression | covered | part19_machine_learning.topics.md › Classical machine learning | SVM margins; k-NN; logistic with cross-entropy |
| Decision trees, random forests and boosting models | covered | part19_machine_learning.topics.md › Classical machine learning | trees and forests named |
| XGBoost gradient boosting | covered | part19_machine_learning.topics.md › Machine learning in Python | second-order gain, regularized leaves |
| LightGBM gradient boosting | covered | part19_machine_learning.topics.md › Machine learning in Python | histogram binning, leaf-wise growth |
| Unsupervised: k-means, DBSCAN, PCA, t-SNE, GMM | covered | part19_machine_learning.topics.md › Classical machine learning | t-SNE named for visualization only |
| Selection: CV, GridSearchCV and RandomizedSearchCV | covered | part19_machine_learning.topics.md › Machine learning in Python | GridSearch and RandomizedSearch named |
| Selection: ROC-AUC, PR, confusion matrix | covered | part19_machine_learning.topics.md › Classical machine learning | confusion matrix; ROC and PR curves |

## Deep learning

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| TensorFlow | covered | part19_machine_learning.topics.md › Machine learning in Python | eager execution and tf.function |
| Keras high-level API | covered | part19_machine_learning.topics.md › Machine learning in Python | Sequential and functional models |
| PyTorch tensors, autograd and nn.Module | covered | part19_machine_learning.topics.md › Machine learning in Python | nn.Module with Linear, Embedding, Dropout, LayerNorm |

## NLP and transformers

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Hugging Face Transformers for pretrained BERT and GPT-class models | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | Auto classes and Trainer |
| spaCy industrial NLP pipelines | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | pipeline and components |
| NLTK tokenization, stemming and classical pipeline | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | Punkt sentence segmentation; stemming in part19 › Natural language processing foundations |

## Data engineering

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| PySpark distributed processing | covered | part19_machine_learning.topics.md › Machine learning in Python | lazy plans, shuffles, partitioning |
| Dask parallel arrays and dataframes | covered | part19_machine_learning.topics.md › Machine learning in Python | lazy task graphs over chunks |

## MLOps

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| MLflow experiment tracking and model registry | covered | part19_machine_learning.topics.md › MLOps | runs, metrics, artifacts and the registry |
| Weights & Biases experiment monitoring | covered | part19_machine_learning.topics.md › MLOps | named in the MLOps bullets |
| Evidently drift and model monitoring | covered | part19_machine_learning.topics.md › MLOps | drift tests on reference and current windows |

## Deployment and agentic add-ons

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| FastAPI model APIs | covered | part05_programming_languages_python_and_shell.topics.md › Python | async endpoints, Pydantic models, streaming |
| LangChain orchestration | covered | part22_generative_ai_3of3.topics.md › Agents and workflows | LangChain and LangGraph |
| LlamaIndex RAG pipelines | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | documents, nodes, ingestion pipelines |
| vLLM paged serving | covered | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | PagedAttention; Rust track P10 covers continuous batching |
| Ray distributed AI workloads | covered | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | tasks and actors |

## Shared text-processing substrate

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Unicode, UTF-8, encodings and normalization | covered | part19_machine_learning.topics.md › Natural language processing foundations | Unicode normalization in the classical pipeline; UTF-8 in Rust track P8 |
| Raw text acquisition and PDF versus OCR routing | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | PDF and HTML ingestion; OCR routing |
| Regular expressions for tokenizing and extraction | partial | part06_programming_languages_go.topics.md › Go — the everyday standard library | regexp as RE2 only; NLP regex tokenizers not taught |
| Normalization: stop words, stemming, lemmatization, OOV and UNK | covered | part19_machine_learning.topics.md › Natural language processing foundations | stemming versus lemmatization; UNK replacement in part19b › Classical NLP and toolkits |
| Sentence, word and subword segmentation; span offsets | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | Punkt; character offsets across tokenizers |
| Subword segmentation: BPE, WordPiece, SentencePiece | covered | part20_generative_ai_1of3.topics.md › How LLMs work | Rust track P8 builds a byte-level BPE |
| Evaluation: inter-annotator agreement (kappa) | covered | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | Cohen's kappa, Fleiss' kappa, Krippendorff's alpha |
| Span-level precision, recall and F1 | partial | part19_machine_learning.topics.md › Natural language processing foundations | F1 named for classification; span-level scoring not taught |
| Confusion matrices and error analysis for taggers | covered | part19_machine_learning.topics.md › Classical machine learning | confusion matrix named |
| Concordance and frequency-distribution tools | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | FreqDist covered; concordance view not named |

## NLTK theory

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Corpus interfaces: raw, words, sents, tagged_words, tagged_sents | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | corpus readers and file identifiers |
| FreqDist and ConditionalFreqDist | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | most-common lists and conditional counts |
| Core data structures: defaultdict, Index, sorted vocabulary | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | defaultdict not named |
| WordNet synsets, lemmas, hypernyms and similarity | covered | part19_machine_learning.topics.md › Natural language processing foundations | WordNet named |
| Treebanks and annotated corpora: Penn, Brown, CoNLL | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | Penn Treebank and CoNLL formats |
| Tokenization and normalization: Punkt, collocations, concordance | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | Punkt and collocations covered; concordance not named |
| POS tagsets: Universal, Penn, Brown | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | Universal and Penn tagsets |
| Baseline taggers and backoff chains | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | default, lookup, unigram, bigram and backoff |
| Brill transformation-based tagging | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | ordered rule lists |
| Sequence-labelling bridge (HMM, CRF) | covered | part19_machine_learning.topics.md › Natural language processing foundations | Viterbi decoding; conditional random fields |

## spaCy theory

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| spaCy object model: Doc, Token, Span, Vocab | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | Doc, Span and Vocab named; StringStore and Lexeme not named |
| Tokenizer design: exceptions, prefixes, suffixes, infixes | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | non-destructive tokenization |
| Token alignment with NLTK corpora and Hugging Face subwords | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | offsets preserved across libraries |
| Pipeline architecture and components | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | ordered components; custom components |
| Linguistic annotations: POS, morphology, lemmas, dependencies, noun chunks, NER | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | noun chunks; dependency parsing at line 104 |
| Rule-based matching: Matcher, PhraseMatcher, EntityRuler | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | named |
| Batching with nlp.pipe and disabling components | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | nlp.pipe named; disabling components not confirmed |

## Hugging Face Tokenizers theory

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Tokenizer pipeline: normalizer, pre-tokenizer, model, post-processor, decoder | covered | part20_generative_ai_1of3.topics.md › How LLMs work | stages named |
| Subword models and special-token inventory | partial | part20_generative_ai_1of3.topics.md › How LLMs work | WordPiece, BPE, SentencePiece named; full special-token inventory not listed |
| Encoding outputs: attention_mask, token_type_ids, offsets, word IDs | partial | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | attention masks and padding named; token_type_ids and word IDs not named |
| Word-level label alignment to subword pieces | covered | part20_generative_ai_1of3.topics.md › How LLMs work | label handling in the tokenizer bullets |
| Tokenizer and checkpoint mismatch | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | Auto classes read the checkpoint's configuration to pick the matching tokenizer |

## Hugging Face Transformers theory

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Core abstractions: checkpoint, config, Auto classes | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | AutoTokenizer and AutoModelForCausalLM |
| Hub revisions, local cache and model cards | partial | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | Hub and model cards named; revisions and local cache not named |
| Model outputs: logits, hidden states, past_key_values | covered | part20_generative_ai_1of3.topics.md › How LLMs work | logits and hidden states; KV cache in part22 › Application architecture and LLMOps |
| Task heads: MLM, CLM, seq2seq, sequence and token classification, QA | covered | part20_generative_ai_1of3.topics.md › How LLMs work | masked and causal objectives; token classification; question answering |
| Embedding and feature-extraction outputs | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | dense embeddings from encoders |
| ASR, image-to-text and VLM heads | covered | part20_generative_ai_1of3.topics.md › Multimodal models | captioning; Whisper and CTC/Conformer in part19b › Speech recognition |
| Pipelines abstraction | partial | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | pipeline named; hidden pre- and post-processing not explained |
| Fine-tuning workflow: Trainer, data collator, dynamic padding, callbacks, checkpoints | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | Trainer wraps the training loop; collator; padding |
| Gradient accumulation | covered | part19_machine_learning.topics.md › Deep learning | effective batch equals micro-batch times accumulation steps |
| Mixed precision training | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | float32 master weights; float16 and bfloat16 |
| Distributed training | covered | part20_generative_ai_1of3.topics.md › How LLMs work | data and tensor parallelism |
| PEFT, LoRA and QLoRA | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | LoRA and QLoRA named |
| Decoding: greedy, beam, sampling, temperature, top-k, top-p, penalties, stop sequences | covered | part20_generative_ai_1of3.topics.md › How LLMs work | repetition and presence penalties; stop sequences |
| Streaming tokens and KV cache | covered | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | streaming; key-value cache |
| Chat templates | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | instruction-response pairs in the template |
| Structured output constraints | covered | part21_generative_ai_2of3.topics.md › Model APIs | structured outputs; no prefilled assistant turns |
| Weight quantization (8-bit, 4-bit) | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | 4-bit and 8-bit named |
| Device maps and multi-GPU placement | partial | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | GPU memory named; device maps not explained |
| GPU memory budgeting, latency and throughput | covered | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | weights plus KV cache; throughput versus latency |
| Evaluation harness for classification, NER and generation | partial | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | graders and eval design; NER and generation harness not named |

## Cross-library selection and integration

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Choosing NLTK, spaCy or Hugging Face by goal | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | choosing by goal |
| Shared contracts: tokenization, offsets, labels, splits, metrics | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | offsets and tokenization named; labels, splits and metrics contracts not stated together |

## 5. Statistical techniques

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Descriptive statistics: mean to kurtosis, percentiles | covered | part03_mathematics.topics.md › Statistics and experimental design | skewness, kurtosis, quantiles, IQR |
| Conditional probability, Bayes and total probability | covered | part03_mathematics.topics.md › Probability | Bayes' theorem; law of total probability; independence |
| Common distributions: Normal, Bernoulli, Binomial, Poisson, Uniform, Exponential, Log-normal, Multinomial | covered | part03_mathematics.topics.md › Probability | all named |
| Sampling: random and stratified | covered | part03_mathematics.topics.md › Statistics and experimental design | stratified sampling named |
| Central limit theorem | covered | part03_mathematics.topics.md › Statistics and experimental design | central limit theorem named |
| Confidence intervals | covered | part03_mathematics.topics.md › Statistics and experimental design | intervals and standard error |
| Hypothesis testing: p-values, Type I and II errors, power | covered | part03_mathematics.topics.md › Statistics and experimental design | Type I errors and power |
| One- and two-sample t-tests | covered | part03_mathematics.topics.md › Statistics and experimental design | Welch's t-test |
| z-test | covered | part03_mathematics.topics.md › Statistics and experimental design | z-test named |
| Chi-square test | partial | part03_mathematics.topics.md › Statistics and experimental design | chi-square distribution taught; chi-square tests not named |
| ANOVA | covered | part03_mathematics.topics.md › Statistics and experimental design | named |
| Mann-Whitney U test | covered | part03_mathematics.topics.md › Statistics and experimental design | rank test for two independent samples |
| Wilcoxon signed-rank test | covered | part03_mathematics.topics.md › Statistics and experimental design | paired differences ranked |
| Covariance and Pearson correlation | covered | part03_mathematics.topics.md › Statistics and experimental design | correlation matrix |
| Spearman and Kendall tau | covered | part03_mathematics.topics.md › Statistics and experimental design | Spearman and Kendall tau named |
| Bayesian inference: prior and posterior | covered | part03_mathematics.topics.md › Statistics and experimental design | prior and posterior |
| Regression: linear, multiple, logistic, ridge, lasso | covered | part19_machine_learning.topics.md › Classical machine learning | ridge and lasso as constraint regions |
| Polynomial regression | partial | part19_machine_learning.topics.md › Machine learning in Python | PolynomialFeatures named; polynomial regression not taught as a model |
| MCMC | covered | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning | Markov chain Monte Carlo with Gibbs sampling |

## 6.1 NLP foundations

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Representation ladder: bag of words, TF-IDF, Word2Vec, embeddings | covered | part19_machine_learning.topics.md › Natural language processing foundations | bag of words, TF-IDF, Word2Vec |
| Language modelling and next-word prediction | covered | part20_generative_ai_1of3.topics.md › How LLMs work | language model as a distribution over the vocabulary |
| Agent loop: observe, reason, act | partial | part22_generative_ai_3of3.topics.md › Agents and workflows | agent loops with tools; the observe-reason-act loop is named only in the exercises |

## 6.2 AI history and classical knowledge

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Dartmouth workshop and the Turing test | covered | part19_machine_learning.topics.md › Foundations of AI | history and definitions |
| ELIZA and early chatbots | missing | → suggest part19 | |
| Four views of AI | covered | part19_machine_learning.topics.md › Foundations of AI | thinking or acting, humanly or rationally |
| Knowledge representation: logic, production rules, semantic networks | covered | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning | expert systems; semantic networks |
| AI winters and boom-bust cycles | covered | part19_machine_learning.topics.md › Foundations of AI | AI winters named |
| Mitchell's definition of machine learning | covered | part19_machine_learning.topics.md › Foundations of AI | experience E, task T, performance P |

## 6.3 Supervised / unsupervised / RL and classical ML

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Supervised, unsupervised and reinforcement learning paradigms | covered | part19_machine_learning.topics.md › Classical machine learning | paradigms named |
| Train/test split and fit-transform-predict workflow | covered | part19_machine_learning.topics.md › Machine learning in Python | estimator protocol |
| Association rules | covered | part19_machine_learning.topics.md › Classical machine learning | support, confidence and lift |
| Recommender systems | covered | part19_machine_learning.topics.md › Applied problem families | recommendation named |
| Bias-variance decomposition | covered | part19_machine_learning.topics.md › Classical machine learning | bias and variance |
| Under- and overfitting diagnosis and fixes | covered | part19_machine_learning.topics.md › Classical machine learning | bias and variance diagnosis |
| Dropout and early stopping | covered | part19_machine_learning.topics.md › Deep learning | dropout and early stopping named |

## 6.4 Embeddings and text representations

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| One-hot encoding and orthogonality of word vectors | covered | part19_machine_learning.topics.md › Natural language processing foundations | one-hot and orthogonal named |
| Dense embeddings | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | learned dense vectors |
| Cosine similarity | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | cosine named for Rocchio classification |
| Vector analogies (king minus man plus woman) | partial | part19_machine_learning.topics.md › Natural language processing foundations | distributional semantics named; analogy example not confirmed |
| Evolution of representations: static to contextual embeddings | covered | part19_machine_learning.topics.md › Natural language processing foundations | ELMo named |

## 6.5 Neural nets

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Perceptron and linear separability | covered | part19_machine_learning.topics.md › Deep learning | XOR limitation |
| Activation functions and multilayer perceptrons | covered | part19_machine_learning.topics.md › Deep learning | sigmoid, softmax; MLP named |
| Backpropagation and the chain rule | covered | part19_machine_learning.topics.md › Deep learning | backprop named |
| Mean squared error and cross-entropy losses | covered | part19_machine_learning.topics.md › Deep learning | cross-entropy named |
| Gradient descent variants: SGD, mini-batch, Adam, RMSProp | covered | part19_machine_learning.topics.md › Deep learning | optimizers and learning-rate schedules |
| Vanishing and exploding gradients | covered | part19_machine_learning.topics.md › Deep learning | vanishing gradients named |

## 6.6 Transformers

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Seq2seq bottleneck and Bahdanau attention | covered | part19_machine_learning.topics.md › Deep learning | Bahdanau named |
| Self-attention with queries, keys and values | covered | part20_generative_ai_1of3.topics.md › How LLMs work | self-attention |
| Transformer encoder and decoder blocks: residuals, LayerNorm, FFN | covered | part20_generative_ai_1of3.topics.md › How LLMs work | residuals and feed-forward blocks |
| Cross-attention | covered | part20_generative_ai_1of3.topics.md › How LLMs work | decoder queries over encoder keys and values |
| Causal mask | covered | part20_generative_ai_1of3.topics.md › How LLMs work | causal mask named |
| Multi-head attention | covered | part20_generative_ai_1of3.topics.md › How LLMs work | multi-head named |
| Positional encodings | covered | part20_generative_ai_1of3.topics.md › How LLMs work | sinusoidal encodings |
| Autoregressive generation loop | covered | part20_generative_ai_1of3.topics.md › How LLMs work | autoregressive decoding |

## 6.7 Foundation models, decoding, APIs

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Encoder-only, decoder-only and encoder-decoder architectures | covered | part20_generative_ai_1of3.topics.md › How LLMs work | BERT, GPT, T5 and BART |
| GPT-style pretraining and in-context learning | covered | part20_generative_ai_1of3.topics.md › How LLMs work | zero-shot, few-shot and in-context learning |
| T5 span corruption and BART denoising | covered | part20_generative_ai_1of3.topics.md › How LLMs work | span corruption and denoising named |
| Chinchilla compute-optimal scaling | covered | part20_generative_ai_1of3.topics.md › How LLMs work | Chinchilla named |
| InstructGPT alignment: SFT, reward model, PPO | covered | part20_generative_ai_1of3.topics.md › How LLMs work | InstructGPT, reward model and PPO |
| Open-weight model families and mixture-of-experts | covered | part20_generative_ai_1of3.topics.md › How LLMs work | LLaMA, Mixtral; mixture-of-experts routing |
| Multimodal and reasoning models | covered | part20_generative_ai_1of3.topics.md › How LLMs work | reasoning models named; multimodal in part20 › Multimodal models |
| Inference-time compute and reasoning cost | covered | part20_generative_ai_1of3.topics.md › How LLMs work | inference-time compute |
| GLUE, MMLU and LAMBADA benchmarks | covered | part20_generative_ai_1of3.topics.md › How LLMs work | GLUE, MMLU across 57 subjects, LAMBADA |
| Vision and speech transformers: ViT, CLIP, Whisper | covered | part20_generative_ai_1of3.topics.md › Multimodal models | ViT and CLIP; Whisper named in How LLMs work |
| Structured outputs and tool calling | covered | part21_generative_ai_2of3.topics.md › Model APIs | structured outputs; tools |
| Hallucination and grounding | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | hallucination named |

## 6.8 LLM evaluation and safety

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Quality versus system metrics: latency, cost, reliability | covered | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | latency and token cost |
| ROUGE | covered | part19_machine_learning.topics.md › Natural language processing foundations | ROUGE named |
| BLEU with brevity penalty | covered | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | clipped n-gram precision; brevity penalty |
| METEOR | covered | part20_generative_ai_1of3.topics.md › Multimodal models | METEOR named in the captioning metrics |
| BERTScore | covered | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | contextual embedding matching |
| LLM-as-a-judge | covered | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | model-graded evaluation |
| Jailbreaks and automated attacks: GCG, PAIR, AutoDAN | covered | part14_security.topics.md › AI and LLM application threats | GCG, PAIR and AutoDAN named |
| Adversarial text attacks: HotFlip, TextFooler | covered | part14_security.topics.md › AI and LLM application threats | white-box attacks |
| Low-resource language jailbreaks | covered | part14_security.topics.md › AI and LLM application threats | translation into low-resource languages |
| Indirect prompt injection | covered | part14_security.topics.md › AI and LLM application threats | injection named |
| Prompt leakage | covered | part14_security.topics.md › AI and LLM application threats | leakage named |
| Data poisoning and backdoors | covered | part14_security.topics.md › AI and LLM application threats | poisoning, backdoor and trojan named |

## 6.9 Prompting

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Zero-shot and few-shot prompting | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | few-shot exemplars |
| Chain-of-thought prompting | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | think step by step |
| Self-consistency | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | named |
| Tree of Thoughts | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | self-evaluated thoughts |
| ReAct | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | named |
| Meta prompting | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | named |
| Directional stimulus prompting | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | named |
| Auto-CoT | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | clustered demonstrations |

## 6.10 Prompt optimization and security

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Verbalized sampling | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | mode collapse |
| Prompt compression: LLMLingua | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | LLMLingua named |
| Prompt optimization: manual versus automatic search | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | APE, ProTeGi and DSPy named |
| Prompt defenses: instruction hierarchy, least privilege | covered | part22_generative_ai_3of3.topics.md › Security and safety of LLM applications | instruction hierarchy and least privilege |
| Prompt evaluation: statistical versus model-based scorers | partial | part22_generative_ai_3of3.topics.md › Evaluation, testing and debugging | graders named; statistical versus model-based scorers not contrasted |

## 6.11 Retrieval-augmented generation

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Why RAG: hallucination, staleness, private data | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | hallucination named |
| Naive RAG and multi-hop limits | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | multi-hop named |
| Six-stage retrieval pipeline | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | ingest, chunk, rerank |
| Chunking strategies: fixed-size, semantic, parent-child | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | fixed, semantic and parent chunking |
| Sparse retrieval (BM25, TF-IDF) and dense retrieval | covered | part19_machine_learning.topics.md › Applied problem families | BM25; hybrid retrieval |
| Cross-encoder reranking | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | bi-encoder versus cross-encoder |
| Query rewriting and query transformation | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | rewrite and multi-query |
| Step-back prompting and HyDE | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | step-back and HyDE named |
| IVF indexing | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | IVF cells and probes; Rust track P11 builds a vector index |
| Product quantization | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | product quantization named |
| HNSW graph indexing | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | HNSW named |
| FAISS versus Chroma | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | library versus database |
| RAG evaluation: context precision, faithfulness | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | RAGAS and faithfulness named |
| Agentic RAG and triage pattern | partial | part22_generative_ai_3of3.topics.md › Agents and workflows | triage named; the plan-act-observe agentic RAG loop not confirmed in part21 |
| Intent routing across sources | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | route profiles and routers |

## 7. Inventory retained but out of teaching scope

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| GST and VAT (CGST, SGST, IGST, ITC) | out of scope | - | ARCHIVE (M18) |
| Banking recurring deposits | out of scope | - | ARCHIVE (M18) |
| Shares and dividends | out of scope | - | ARCHIVE (M18) |
| Clinical and medical suites (AccessMedicine) | out of scope | - | ARCHIVE; clinical |
| Research-level number theory (Serre, Lang, analytic NT, elliptic-curve research) | out of scope | - | ARCHIVE |
| React and TypeScript web-stack destination | out of scope | - | ARCHIVE |
| Game engines and real-time rendering as a track | out of scope | - | ARCHIVE |
| Mechanical, fluid and aerospace modules | out of scope | - | ARCHIVE |

## §17.1 IIT/IISc BTech-MTech CS and Math institutional cross-check

| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Undecidability beyond Rice's theorem | partial | part08_data_structures_algorithms.topics.md › Computability and complexity | halting problem and undecidability taught; Rice's theorem named |
| Cook-Levin theorem | partial | part08_data_structures_algorithms.topics.md › Computability and complexity | NP-completeness via SAT and 3-SAT; Cook-Levin not named |
| Polynomial hierarchy | missing | → suggest part08 | |
| Space-bounded computation (PSPACE, L, NL) | missing | → suggest part08 | |
| Circuit complexity | missing | → suggest part08 | |
| Probabilistically checkable and interactive proofs | missing | → suggest part08 | |
| CPU datapath and control-unit design | partial | part02_computer_organization.topics.md › Machine organization | single-cycle datapath; control unit and multicycle not named |
| Instruction-set architecture | covered | part02_computer_organization.topics.md › Machine organization | RISC-V RV32I base |
| Pipelining and hazards | covered | part02_computer_organization.topics.md › Machine organization | pipeline, forwarding, hazards and branch prediction |
| Cache hierarchies and coherence | covered | part02_computer_organization.topics.md › Machine organization | MSI and MESI |
| Memory systems and virtual memory | covered | part02_computer_organization.topics.md › Machine organization | TLB and virtual memory |
| I/O devices and DMA | missing | → suggest part02 | interrupts are in part10 › Processes and threads; DMA not named |
| Superscalar and VLIW organization | missing | → suggest part02 | |
| Multicore organization | covered | part02_computer_organization.topics.md › Machine organization | multicore; cache coherence |
| OS process and thread models | covered | part10_operating_systems.topics.md › Processes and threads | |
| CPU scheduling | covered | part10_operating_systems.topics.md › CPU scheduling | CFS and EEVDF |
| Synchronization primitives and classical concurrency problems | covered | part10_operating_systems.topics.md › Concurrency | semaphores, monitors, readers-writers |
| Deadlock: avoidance and detection | covered | part10_operating_systems.topics.md › Concurrency | Coffman conditions; banker's algorithm |
| Paging, segmentation and virtual memory | partial | part10_operating_systems.topics.md › Virtual memory | paging and demand paging; segmentation not named |
| File systems | covered | part10_operating_systems.topics.md › Persistence | file system, inodes |
| Data-link layer and MAC protocols | partial | part09_networking.topics.md › Addressing and the link layer | Ethernet, switches, ARP, VLANs; CSMA and ALOHA not named |
| Layered network architectures: OSI, TCP/IP | covered | part09_networking.topics.md › Architecture principles | OSI and TCP/IP named |
| Routing algorithms | covered | part09_networking.topics.md › Routing | link-state with Dijkstra and OSPF; distance-vector |
| Transport-layer congestion control | covered | part09_networking.topics.md › Transport | AIMD, congestion control, BBR |
| Lexing, parsing and abstract syntax trees | partial | part07_programming_languages_typescript_wire_theory_exercises.topics.md › Language theory | compiler pipeline named; lexing and parsing not confirmed |
| Intermediate representations, optimization and code generation | covered | part07_programming_languages_typescript_wire_theory_exercises.topics.md › Language theory | IR and SSA; optimisation; code generation; linking |
| Register allocation | missing | → suggest part07 | |
| Formal operational and denotational semantics | partial | part07_programming_languages_typescript_wire_theory_exercises.topics.md › Language theory | Hoare triples named; operational and denotational not named |
| Type systems | covered | part07_programming_languages_typescript_wire_theory_exercises.topics.md › Language theory | type systems |
| Group theory through Sylow's theorems and the structure theorem | partial | part03b_analysis_calculus_and_number_theory.topics.md › Number theory | groups and Lagrange named; Sylow and structure theorem not named |
| Ring and module theory | partial | part03b_analysis_calculus_and_number_theory.topics.md › Number theory | rings named; modules not named |
| Field extensions and Galois theory | partial | part03b_analysis_calculus_and_number_theory.topics.md › Number theory | finite fields only; Galois theory not named |
| Representation theory of finite groups | missing | → suggest part03b | |
| Point-set topology: continuity, connectedness, compactness, separation | partial | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis | compactness and connectedness; separation axioms and quotient topology not named |
| Fundamental group and homology | missing | → suggest part03b | |
| Holomorphic functions, Cauchy integral formula, Taylor and Laurent series | covered | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis | Cauchy, Taylor and Laurent named |
| Residue theorem | covered | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis | residues named |
| Conformal mapping and the Riemann mapping theorem | partial | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis | Möbius maps and conformal geometry named; Riemann mapping theorem not named |
| Sigma-algebras and Lebesgue measure | partial | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis | Lebesgue measure named; sigma-algebras not named |
| Lebesgue integral and convergence theorems | partial | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis | monotone convergence named; dominated convergence not named |
| Lp spaces | missing | → suggest part03b | |
| Banach and Hilbert spaces | partial | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis | Hilbert spaces and the Hahn-Banach setting; Banach spaces not named |
| Hahn-Banach, closed-graph and open-mapping theorems | partial | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis | Hahn-Banach named; closed-graph and open-mapping not named |
| Spectral theory of operators | covered | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis | spectral theorem |
| Curves and the Frenet-Serret frame | missing | → suggest part03b | |
| Surfaces, fundamental forms, geodesics and Gauss-Bonnet | missing | → suggest part03b | |
| Propositional logic | covered | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning | propositional logic |
| First-order logic | covered | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning | first-order logic and unification |
| Soundness and completeness | partial | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning | resolution named; soundness and completeness not confirmed |
| Zermelo-Fraenkel axioms, cardinals and ordinals | partial | part03_mathematics.topics.md › Proof and discrete mathematics | cardinality by bijections; ZF axioms and ordinals not named |
| Compactness and Löwenheim-Skolem | missing | → suggest part03 | |
| Gödel's incompleteness theorems | missing | → suggest part03 | |
| Enumeration and generating functions | covered | part03_mathematics.topics.md › Proof and discrete mathematics | permutations, combinations, inclusion-exclusion; generating functions in part03b › Number theory |
| Ramsey theory | missing | → suggest part03 | |
| Extremal graph theory | missing | → suggest part03 | |
| Matchings and network flows | partial | part08_data_structures_algorithms.topics.md › Graph algorithms | max-flow min-cut covered; bipartite matching and Hall's theorem not named |
| Planarity and graph colourings | partial | part03_mathematics.topics.md › Proof and discrete mathematics | bipartite 2-colouring only |
| Design theory | missing | → suggest part03 | |
| Computational hardness assumptions | missing | → suggest part14 | |
| Pseudorandom generators and functions | covered | part14_security.topics.md › Cryptography | PRGs, PRFs and PRPs |
| Semantic security and indistinguishability | partial | part14_security.topics.md › Cryptography | adversarial advantage and negligible functions named; semantic security not named |
| Provable-security reductions | covered | part14_security.topics.md › Cryptography | reductions and the hybrid argument |
| Zero-knowledge proofs | partial | part14_security.topics.md › Cryptography | named in a privacy-enhancing survey line only |
| Classification of second-order linear PDEs | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | elliptic, parabolic, hyperbolic |
| Existence and uniqueness theory for PDEs | missing | → suggest part03b | |
| Sobolev-space methods | missing | → suggest part03b | |
| Maximum principle (PDE) | missing | → suggest part03b | Pontryagin's principle in part03 is a different topic |
| Green's functions | missing | → suggest part03b | |

## Missing in this range

- ELIZA and early chatbots → suggest part19
- Register allocation → suggest part07
- Polynomial hierarchy → suggest part08
- Space-bounded computation (PSPACE, L, NL) → suggest part08
- Circuit complexity → suggest part08
- Probabilistically checkable and interactive proofs → suggest part08
- I/O devices and DMA → suggest part02
- Superscalar and VLIW organization → suggest part02
- Representation theory of finite groups → suggest part03b
- Fundamental group and homology → suggest part03b
- Lp spaces → suggest part03b
- Curves and the Frenet-Serret frame → suggest part03b
- Surfaces, fundamental forms, geodesics and Gauss-Bonnet → suggest part03b
- Compactness and Löwenheim-Skolem → suggest part03
- Gödel's incompleteness theorems → suggest part03
- Ramsey theory → suggest part03
- Extremal graph theory → suggest part03
- Design theory → suggest part03
- Computational hardness assumptions → suggest part14
- Existence and uniqueness theory for PDEs → suggest part03b
- Sobolev-space methods → suggest part03b
- Maximum principle (PDE) → suggest part03b
- Green's functions → suggest part03b

## Partial in this range

- SciPy signal processing → part05 Python; DSP taught in part03c
- Matplotlib 3D plots and savefig → part05 Python
- Polynomial regression → part19 Machine learning in Python
- Regular expressions for tokenizing and extraction → part06 Go standard library
- Span-level precision, recall and F1 → part19 NLP foundations
- Concordance and frequency-distribution tools → part19b Classical NLP and toolkits
- Core data structures: defaultdict, Index, sorted vocabulary → part19b Classical NLP and toolkits
- Tokenization and normalization: Punkt, collocations, concordance → part19b Classical NLP and toolkits
- spaCy object model: Doc, Token, Span, Vocab → part19b Classical NLP and toolkits
- Batching with nlp.pipe and disabling components → part19b Classical NLP and toolkits
- Subword models and special-token inventory → part20 How LLMs work
- Encoding outputs: attention_mask, token_type_ids, offsets, word IDs → part20 Fine-tuning and adaptation
- Hub revisions, local cache and model cards → part20 Fine-tuning and adaptation
- Pipelines abstraction → part20 Fine-tuning and adaptation
- Device maps and multi-GPU placement → part22 Application architecture and LLMOps
- Evaluation harness for classification, NER and generation → part22 Evaluation, testing and debugging
- Shared contracts: tokenization, offsets, labels, splits, metrics → part19b Classical NLP and toolkits
- Chi-square test → part03 Statistics and experimental design
- Vector analogies (king minus man plus woman) → part19 Natural language processing foundations
- Agent loop: observe, reason, act → part22 Agents and workflows
- Prompt evaluation: statistical versus model-based scorers → part22 Evaluation, testing and debugging
- Agentic RAG and triage pattern → part22 Agents and workflows
- Undecidability beyond Rice's theorem → part08 Computability and complexity
- Cook-Levin theorem → part08 Computability and complexity
- CPU datapath and control-unit design → part02 Machine organization
- Paging, segmentation and virtual memory → part10 Virtual memory
- Data-link layer and MAC protocols → part09 Addressing and the link layer
- Lexing, parsing and abstract syntax trees → part07 Language theory
- Formal operational and denotational semantics → part07 Language theory
- Group theory through Sylow's theorems and the structure theorem → part03b Number theory
- Ring and module theory → part03b Number theory
- Field extensions and Galois theory → part03b Number theory
- Point-set topology: continuity, connectedness, compactness, separation → part03b Real analysis
- Conformal mapping and the Riemann mapping theorem → part03b Complex and functional analysis
- Sigma-algebras and Lebesgue measure → part03b Real analysis
- Lebesgue integral and convergence theorems → part03b Real analysis
- Banach and Hilbert spaces → part03b Complex and functional analysis
- Hahn-Banach, closed-graph and open-mapping theorems → part03b Complex and functional analysis
- Soundness and completeness → part19 Classical AI: search, knowledge and reasoning
- Zermelo-Fraenkel axioms, cardinals and ordinals → part03 Proof and discrete mathematics
- Matchings and network flows → part08 Graph algorithms
- Planarity and graph colourings → part03 Proof and discrete mathematics
- Semantic security and indistinguishability → part14 Cryptography
- Zero-knowledge proofs → part14 Cryptography
