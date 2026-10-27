# Part 20 · Generative AI, LLMs, Agents & Claude Applications (part 1 of 3) · TOPIC LIST

Rules and directives for this part: `index/part20_generative_ai_1of3.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Generative AI, LLMs, Agents & Claude Applications (part 1 of 3)

### How LLMs work

- **Language modelling as probability**
  - Autoregressive factorization P(x₁ … x_T) = Πₜ P(xₜ | x₁ … xₜ₋₁); next-token cross-entropy as the training loss
  - Perplexity; bits per byte for comparing models with different tokenizers
- **Tokenization**
  - Characters versus subwords versus bytes; subwords removing out-of-vocabulary words
  - Byte-pair encoding as a greedy dictionary compressor: training (count pairs, merge the most frequent, record merges) and encoding in learned merge order; special tokens; the round-trip property
  - WordPiece (likelihood-scored merges, continuation markers, used by BERT); SentencePiece (language-independent tokenization of raw text with whitespace as a symbol, by BPE or a unigram language model)
  - Why token counts vary by language, code and numbers; tokens as the unit of price, limits and latency
  - Tokenizer pipeline stages: normalizer (Unicode and case rules), pre-tokenizer (splitting text into word-like units before the model), tokenization model (BPE, WordPiece or Unigram), post-processor (special tokens, truncation and padding) and decoder back to text; each stage changes the offsets that later stages depend on
  - Word-to-subword label alignment: word-level NER or POS labels propagated to subword pieces through word IDs; labelling the first piece of each word and masking the rest in the loss; answer spans mapped from character offsets to token positions
  - Tokenizer and checkpoint mismatch: a checkpoint is valid only with the exact vocabulary, merge rules, normalizer and special-token IDs it was trained with; a mismatch silently remaps IDs, so the model answers fluently from the wrong tokens; checked by round-trip tests against the tokenizer files shipped with that checkpoint
- **N-gram and bigram models**: counting, smoothing, sampling; the same model as a trained linear layer
- **Statistical alignment and machine translation**: the noisy-channel decomposition, choosing the English sentence e that maximizes P(f | e)P(e), with a language model for fluency; IBM word-alignment models estimated by expectation–maximization over sentence pairs; phrase tables and beam-search decoding; the pre-neural baseline that sequence-to-sequence translation replaced
- **The Transformer**
  - Attention as a soft lookup table: queries, keys and values as learned projections of each token; a worked Q, K, V example
  - Scaled dot-product attention softmax(QKᵀ ÷ √d_k)V and why √d_k keeps logits at unit variance
  - Self-attention versus cross-attention (queries from the decoder, keys and values from the encoder output, a target × source weight matrix)
  - Multi-head attention: h heads of width d_k = d_model ÷ h, concatenated and projected by Wᴼ
  - Multi-query and grouped-query attention: query heads sharing one key–value head (multi-query) or one per group of query heads (grouped-query); the key–value cache shrinks by the sharing factor, with a small quality cost at moderate sharing
  - Token embeddings; positional information by sinusoidal encodings (deterministic, unique per position, offsets as linear maps, extending beyond trained lengths) or by learned position tables
  - The causal mask: a lower-triangular mask setting future positions to −∞ before the softmax
  - The residual stream with add-and-norm; layer normalization; the position-wise feed-forward block with inner width about 4 × d_model
  - RMS normalization and GLU variants: RMSNorm rescales by the root mean square without subtracting the mean, saving one pass; gated linear units replace the feed-forward's single activation with an elementwise product of two projections, SwiGLU using a Swish activation; both are standard in LLaMA-family decoders
  - The autoregressive loop: begin- and end-of-sequence tokens, each output fed back as input
  - Unembedding (projection to vocabulary logits): the final linear map from d_model to the vocabulary size, one logit per token; softmax over the logits gives the next-token distribution; often tied to the input embedding matrix so one table serves both ends
  - Encoder-only (BERT), decoder-only (GPT) and encoder–decoder (T5, BART) architectures; the same blocks over image patches and audio (Vision Transformer, Whisper); pre-training as learning the projections
  - The context window as the fixed length of the position table; O(n²d) attention cost per layer
  - The key–value cache during generation
  - IO-aware attention kernels (FlashAttention): attention computed in tiles held in on-chip memory with an online softmax, so the n × n score matrix is never written to high-bandwidth memory; exact results with memory linear in n rather than quadratic; the gain comes from cutting memory traffic, not arithmetic
- **Model lineage and benchmarks**
  - BERT: masked language modelling over 15% of tokens and next-sentence prediction; fine-tuning for downstream tasks; the GLUE tasks (CoLA, SST-2, MRPC, STS-B, QQP, MNLI, QNLI, RTE, WNLI)
  - GPT-1 pre-training then fine-tuning; GPT-2 zero-shot task transfer measured on LAMBADA; T5 text-to-text training by span corruption on C4; BART as a denoising autoencoder
  - GPT-3 and in-context learning (zero-, one- and few-shot); abilities that emerge with scale
  - Open-weight families (LLaMA, Mistral, Mixtral, Falcon, Qwen, DeepSeek); mixture-of-experts layers routing each token to a few experts; MMLU across 57 subjects
  - Reasoning models trained to think before answering, and inference-time compute as a scaling axis
- **Decoding**
  - Greedy decoding as locally rather than globally optimal; beam search keeping the best partial sequences
  - Temperature softmax(z ÷ T): entropy rising with T, T → 0 as greedy; top-k; nucleus (top-p) sampling as a dynamic cutoff; avoiding extreme top-k and top-p together
  - Repetition, frequency and presence penalties; stop sequences and maximum length; seeded reproducibility
  - Why sampling makes answers vary and lets a model state falsehoods fluently
- **Scaling**: training compute ≈ 6ND FLOPs; power-law loss in parameters, data and compute; compute-optimal training (Chinchilla: 70B parameters on 1.4T tokens, about 20 tokens per parameter)
- **Distributed training**: memory for weights, gradients and optimizer states set against one device's memory; data parallelism with gradients all-reduced each step; tensor parallelism splitting each matrix multiply across devices and pipeline parallelism splitting layers into stages fed with micro-batches; optimizer-state, gradient and parameter sharding that removes replicated copies; the communication volume and pipeline bubble each strategy pays
- **Alignment**: instruction tuning by supervised fine-tuning, a reward model from pairwise human preferences and PPO with a KL penalty for drifting from the tuned model (RLHF, the InstructGPT recipe); Constitutional AI and AI feedback against written principles
- **Frontier model behaviour**: thinking before answering (adaptive thinking controlled by an effort setting); multimodal inputs (images and PDFs); latency ≈ time to first token + output tokens ÷ throughput; larger models are slower per token; streaming changes perceived, not total, latency
- **Long context**: the hard limit of the window versus degraded retrieval inside it ("lost in the middle"); quality falling as irrelevant context grows
- **Choosing an approach**: prompt engineering versus retrieval-augmented generation versus fine-tuning
- **Responsible AI**: bias, fairness, safety evaluation; explainability through attention visualization and feature attributions (LIME, SHAP)
- **Interpretability**: the residual stream as a shared channel to which attention heads and MLP blocks add; induction heads and circuits; the logit lens, probing classifiers, activation patching and sparse autoencoders

### Fine-tuning and adaptation

- Full fine-tuning versus parameter-efficient fine-tuning; memory for weights, gradients and optimizer states; one full copy of the model per task
- Cheaper full fine-tuning: layer-wise, block-wise and progressive unfreezing; tuning only the top blocks with embeddings and lower blocks frozen
- Fine-tuning hyperparameters: a peak learning rate near 1e-5 to 2e-5 for full fine-tuning and 1e-4 to 2e-4 for LoRA; one or two epochs; a few percent of warmup with cosine decay; early stopping on held-out task and general evaluations, not on training loss
- **Mixed precision training**: half-precision forward and backward passes with float32 master weights and loss scaling; float16's narrow exponent overflowing near 65,504 while bfloat16 keeps float32's range at lower mantissa precision; memory and throughput gains on matrix units against underflow in small gradients
- **Catastrophic forgetting**
  - Why it happens: knowledge superimposed in shared weights, a narrow gradient signal, drift away from the pretrained optimum, and no replay of old data
  - Measuring it: a fixed general suite (reasoning, code, mathematics, instruction following) run before and after every fine-tune, since task metrics rise while general ability falls silently
  - Rehearsal: mixing 1–10% general instruction data into every batch
  - Regularizing toward the pretrained weights: L2-SP with penalty λ‖θ − θ₀‖²; elastic weight consolidation weighting each parameter's penalty by its Fisher information
  - Weight interpolation after training, θ = (1 − α)·θ_base + α·θ_tuned, with α chosen at the knee of the task-versus-general curve (WiSE-FT)
  - Choosing mitigations by cause: conservative hyperparameters always; rehearsal when general data exists; penalties when it does not; interpolation for a model already degraded; freezing for small data or tight compute
- **Fine-tuning data**
  - Quality: extraction boilerplate, spam and machine-generated text, OCR errors; wrong content learned as fact; duplicates driving memorization; benchmark test sets leaking into training data; inconsistent formatting, encodings and whitespace; stale and contradictory snapshots
  - Too little data: augmentation by back-translation and paraphrase; synthetic data that is validated before use; a smaller model with stronger regularization
  - Missing edge cases and narrow coverage: targeted collection, simulation, active learning on uncertain production samples, stratified sourcing, metrics reported per subgroup, datasheets and model cards
  - Shift between training and deployment: usage shift (documents to dialogue), temporal shift (the world after the cutoff) and domain shift (general to specialist), met by instruction tuning, domain-adaptive pre-training with replay, retrieval and production monitoring
- **LoRA**: frozen weights plus a trainable low-rank update ΔW = BA of rank r much smaller than the layer width, scaled by α ÷ r; B initialized to zero so training starts from the base model; choosing target modules (attention and MLP projections); merging adapters into the weights or swapping adapters per task
- **QLoRA**: a frozen base quantized to 4-bit NormalFloat (NF4); double quantization of the quantization constants; paged optimizers absorbing memory spikes; adapters trained in higher precision
- **The PEFT families**: additive (adapters), reparameterized (LoRA, QLoRA), soft prompts, and selective tuning of existing weights (BitFit training only biases; diff pruning learning a sparse difference)
- **Adapters**
  - A bottleneck block with a residual connection, h′ = h + f(h): down-projection from width d to m, a non-linearity, up-projection back to d; 2dm + m + d added parameters per adapter
  - Near-identity initialization so the adapted model starts as the base model; the base frozen and only adapters trained
  - Sequential adapters after each sub-layer versus parallel (residual) adapters beside the feed-forward block; added inference latency that a merged LoRA update avoids
  - One adapter per task as a defence against forgetting; routing among adapters by task; AdapterFusion combining several task adapters with learned attention
- **Soft prompts**
  - Trainable virtual-token embeddings in place of hand-written discrete prompts; prompt tuning at the input layer versus prefix tuning, which prepends trainable key and value vectors at every attention layer
  - Cost: longer sequences in every layer; refinements that choose shorter prompts through a router (SMoP), vary prefix length by layer with gates (adaptive prefix tuning), generate the prompt from each input (instance-dependent prompts), or insert prompts only at selected layers
- Training data as instruction–response pairs in the model's chat template; held-out evaluation of the tuned model against the base model for gains and regressions
- Weight quantization (8-bit, 4-bit) for inference and its accuracy cost
- **Pruning**: unstructured magnitude pruning zeroing the smallest weights and structured pruning removing whole heads, neurons or blocks; sparsity traded against accuracy on held-out tasks; unstructured zeros give no speed-up on dense hardware unless the kernels exploit them; fine-tuning after pruning to recover accuracy
- Knowledge distillation: a small student trained on a large teacher's outputs or soft labels
- **Direct preference optimization (DPO)**: the RLHF objective of the alignment bullet rewritten as a classification loss on preference pairs, with a frozen reference model as the anchor; loss −log σ(β[(log π(y_w | x) − log π_ref(y_w | x)) − (log π(y_l | x) − log π_ref(y_l | x))]), where y_w is the preferred and y_l the rejected response; no reward model and no PPO loop, at the cost of depending on pair quality; β sets how far the policy may move from the reference
- Libraries: Hugging Face Transformers, PEFT, bitsandbytes and TRL
- **Pipelines abstraction**: a pipeline as preprocessing, batching, the model's forward pass, postprocessing and output formatting in one call; what it hides (tokenizer choice, truncation, padding, device placement, generation defaults) and the same steps written out by hand against the model and tokenizer classes before the convenience is trusted

### Multimodal models

- **Foundations**
  - Three paradigms by input and output: contrastive (image and text to a similarity score), generative (image and instruction to free text) and promptable dense prediction (image and spatial prompt to a mask)
  - The shared anatomy: a vision encoder, a connector, and a consumer of the fused representation; where fusion happens (a final dot product between two towers, self-attention over mixed tokens, or a dedicated cross-attention module)
  - Vision Transformer: an image cut into 16 × 16 patches, each flattened and linearly projected like a word embedding, with position embeddings and a [CLS] token whose output summarizes the image
- **CLIP**
  - Two independent encoders (a ResNet with attention pooling or a ViT; a text Transformer read at its end-of-sequence token), each linearly projected and L2-normalized into one space
  - The symmetric InfoNCE loss: an N × N similarity matrix with matching pairs on the diagonal, cross-entropy over rows and over columns, and a learned temperature controlling the softmax's sharpness
  - Very large batches as the source of in-batch negatives; training on hundreds of millions of noisy web image–text pairs
  - Zero-shot classification by embedding one sentence per class name; template ensembling; linear probing versus zero-shot transfer as two ways to judge an encoder
  - Limits: counting, spatial relations, fine text, prompt sensitivity, web-data bias, and no text generation
- **LLaVA-style generative models**
  - A frozen CLIP vision tower whose patch features pass through a projector (one linear layer, later a two-layer MLP) into the language model's embedding space; visual tokens placed in the sequence as a foreign language, fused by ordinary self-attention
  - Why a projector is needed: two embedding spaces of equal width with unrelated geometry
  - Instruction data produced by a text-only model from captions and bounding boxes: conversation, detailed description and complex reasoning
  - Two-stage training: projector-only feature alignment with both towers frozen, then instruction tuning of projector and language model, with the loss on assistant tokens only
  - Higher resolution by tiling an image, encoding each tile and adding a downsampled global view, at the cost of more visual tokens
  - Limits: object hallucination, a resolution bottleneck, weak localization and counting, inherited encoder blind spots
- **Grounded models (Qwen-VL)**
  - A cross-attention adapter in which a fixed set of learnable queries attends over all patch features, giving a constant visual-token budget at any resolution; 2D position encodings preserving layout
  - Grounding as generated text: reference phrases and bounding boxes wrapped in special tokens, with coordinates normalized to a fixed range; several images in one sequence
  - Three-stage training: low-resolution pre-training on weak pairs with the language model frozen, higher-resolution multi-task pre-training (captioning, question answering, grounding, OCR), then instruction tuning
  - Successors: dynamic resolution with a variable token count, and rotary position embeddings unified across text, space and time
- **Promptable segmentation (SAM)**
  - The task: any point, box or rough mask returns a valid mask
  - A heavy masked-autoencoder-pretrained ViT run once per image and cached; a light prompt encoder (positional encodings for points and boxes, convolutions for masks); a small mask decoder with two-way attention between prompt and image tokens
  - Ambiguity resolved by three candidate masks (whole, part, sub-part) ranked by a predicted-IoU head
  - Mask loss as focal loss (pixel imbalance) plus Dice loss, 1 − 2|X∩Y| ÷ (|X| + |Y|) (region overlap)
  - The data engine: assisted-manual, semi-automatic, then fully automatic labelling from a grid of point prompts, yielding over a billion masks
  - No class labels or language; composition with a detector that names and boxes objects; extension to video with a memory of earlier frames
- **Design trade-offs**: frozen versus fine-tuned vision backbones; visual-token count versus spatial fidelity; web-scale noisy data versus small engineered datasets; one task done very well versus breadth; self-supervised (DINO-family) and sigmoid-loss contrastive (SigLIP) encoders as alternatives to CLIP
- **Applications**
  - Captioning: a contrastive model for tags, a generative one for sentences; fixed, scoped, length-limited templates at catalogue scale; n-gram metrics (BLEU, ROUGE, METEOR, CIDEr), scene-graph SPICE and CLIPScore, and their weak agreement with human judgment; cleaning noisy web captions with a jointly trained captioner and filter
  - Visual question answering: yes/no, multiple-choice, counting and open-ended forms; listing objects before counting; presupposition hallucination and an explicit "not present" answer; testing whether answers depend on the image by blurring it; strict-match accuracy penalizing correct verbose answers
  - Document intelligence: OCR precision, layout understanding and relations between fields together; the exact JSON schema shown in the prompt, with every field named and nulls for missing values; resolution as the largest lever; dedicated OCR pipelines for bulk text versus a vision-language model for layout-aware extraction; document-specific vision encoders and OCR-plus-layout encoders compressed into learned queries; human verification of financial and legal fields
  - Visual reasoning and chart questions: reasoning strength set mostly by the language model; observations listed before conclusions; values extracted before reasoning; compounding errors and a self-check pass
  - Preference tuning against hallucination with synthetic negatives: random answers, mismatched questions, and images with the relevant objects masked
  - Benchmarks by task: COCO Captions and NoCaps; VQAv2, GQA, OK-VQA, TextVQA and VizWiz; DocVQA (scored by normalized edit similarity), FUNSD and ChartQA; POPE for object hallucination; MMMU, MathVista, ScienceQA, NLVR2 and Winoground; contamination as a caveat on reported gains

### Generative models beyond autoregression

- **Generative modelling**: density estimation versus sampling; explicit versus implicit models; a taxonomy of autoregressive, latent-variable, adversarial, flow and diffusion models
- **Representation and manifold learning**: the manifold hypothesis, that high-dimensional data lie near a low-dimensional manifold; undercomplete, sparse and denoising autoencoders as learned encoders and decoders; latent codes as coordinates on the manifold; nonlinear embeddings compared with linear PCA
- **Variational autoencoders**: the latent-variable model, the ELBO and the reparameterization trick; β-VAE and disentanglement; VQ-VAE with a discrete codebook and the straight-through estimator; posterior collapse
- **Generative adversarial networks**
  - The minimax game; the optimal discriminator and the Jensen–Shannon divergence; the non-saturating loss
  - DCGAN, conditional GANs, Wasserstein GAN with weight clipping and gradient penalty
  - Mode collapse and unstable training; GAN inversion; evaluation by Inception score and FID
- **f-divergences**: KL, reverse KL, Jensen–Shannon and total variation; variational divergence minimization (f-GAN)
- **Diffusion models**: the forward noising process; DDPM training by predicting noise; noise schedules (linear, cosine); reverse sampling and DDIM; conditional generation and classifier-free guidance; the score-based and stochastic-differential-equation view; latent diffusion
- **Flow models**: normalizing flows; conditional flow matching and rectified flow; comparison with diffusion
- **Evaluating generative models**: likelihood, FID, precision and recall of distributions, human evaluation

### Embeddings and retrieval

- Embeddings as vectors whose geometry encodes similarity; embedding models from a provider
- Cosine, dot product and Euclidean distance agree on unit vectors (‖a − b‖² = 2 − 2 cos θ); normalizing once; an index metric that must match the metric the model was trained for
- Lexical retrieval: the vector-space model; BM25 with term-frequency saturation k₁ and length normalization b; IDF
- Hybrid retrieval: reciprocal rank fusion RRF(d) = Σ 1 ÷ (k + rank_r(d)) with k = 60
- Why embedding search misses exact codes that BM25 finds; negation and numbers that embed deceptively alike; topical relevance that does not answer the question
- Retrieval benchmarks: MS MARCO for passage ranking, BEIR for zero-shot transfer across domains
- **Training embedding models**
  - Why raw BERT [CLS] or mean-pooled vectors are poor for cosine similarity; Sentence-BERT siamese training
  - Contrastive and margin losses; in-batch negatives; hard negatives mined with BM25
  - Bi-encoders (texts encoded independently, so documents can be indexed) versus cross-encoders (query and document encoded jointly, accurate but not indexable); ColBERT late interaction scoring per-token maximum similarity
  - Small encoders distilled from large ones (MiniLM)
  - Matryoshka representation learning: a loss on nested prefixes so vectors can be truncated to fewer dimensions
- **Choosing an embedding model**: measuring on your own queries rather than trusting a public leaderboard (MTEB); hosted APIs versus open-weight models (BGE, E5, Nomic, MiniLM); dimensions and storage cost; multilingual coverage; code and logs that need hybrid search; maximum sequence length against document length; truncatable embeddings for very large corpora; asymmetric query and passage prefixes; corpora small enough to need no retrieval
- **Vector-database internals**
  - Exact search at O(n·d) per query; the curse of dimensionality for tree indexes
  - IVF: k-means centroids partition the space into Voronoi cells with inverted lists; `nlist` near √N as a starting point; `nprobe` cells searched, costing about `nprobe` × N ÷ `nlist` comparisons; training on many points per centroid
  - Product quantization: a vector split into m sub-vectors, each replaced by a one-byte code from a 256-centroid codebook (768 float32 dimensions to 8 bytes); asymmetric distance computation from per-query lookup tables; IVF-PQ coding residuals from the cell centroid
  - HNSW layered proximity graphs: greedy descent from sparse upper layers; `M`, `efConstruction`, `efSearch`; roughly logarithmic search with memory growing with N·M
  - Scalar and binary quantization; ScaNN and DiskANN for collections larger than memory
  - The recall–latency–memory trade-off tuned against a flat baseline
  - Filtered search: pre-filter, post-filter, filter during traversal; selective filters collapsing recall
  - Inserts and deletes on a built index; rebuilds and compaction; sharding and replication; hybrid dense-plus-sparse search; multi-tenancy by namespace or partition
  - Embedding versioning: a new embedding model means re-embedding and re-indexing
  - FAISS index types (flat L2 and inner product, IVF-Flat, IVF-PQ, HNSW) as a library without a document store, so the application keeps the ID-to-text map; Chroma storing documents, metadata and embeddings together with metadata `where` filters over an HNSW index
  - Store selection: pgvector in PostgreSQL versus dedicated vector stores (Qdrant, Weaviate, Chroma, Vespa, Pinecone) versus libraries (FAISS) versus managed indexes
