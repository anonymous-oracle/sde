# Part 19b · Speech & ASR, Computer Vision, Information Retrieval & NLP Toolkits · RULES AND DIRECTIVES

Companion topic list: `index/part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md`. Ingest `index/00_learning_method.md` once per session, then this file, then the topic list. Mark the part done in `index/00_ingest_progress.md` before opening the next part.

Groups in this part: Speech science and analysis; Speech recognition: from HMMs to Kaldi; Speech synthesis, speakers and spoken-language systems; Computer vision: images, motion and multi-view geometry; Information retrieval engines; Classical NLP and toolkits; Exercises.

---

# A. Standing rules: the Learning method

The full Learning method is kept **once**, in `index/00_learning_method.md`, and applies unchanged to every part. Read it at the start of a session and again after any compaction; it governs how every topic in this part is taught. It is not repeated here.

---

# B. Directives for this domain

## Speech & ASR, Computer Vision, Information Retrieval & NLP Toolkits

**Prerequisites:** the DSP of part 03c (z-transform, filters, cepstrum, LPC); probability, statistics and linear algebra (part 03); weighted finite-state transducers (part 08); the machine-learning, NLP and classical computer-vision groups of part 19; Python (part 05).

**Depth bar:** a graduate course in each area: an HMM recognizer and an HCLG graph built and decoded by hand on a toy task before Kaldi or a neural toolkit; multi-view geometry derived and implemented; an inverted index with compression and ranking built from scratch; every toolkit used only after its algorithm has been implemented at toy size.

**Capstone:** a media search system: spoken audio transcribed by a from-scratch small-vocabulary recognizer and a toolkit baseline with word error rate measured; video keyframes tracked with camera motion estimated; transcripts and keyframes indexed in your own compressed inverted index with query-likelihood ranking, evaluated by MAP and nDCG; entities extracted with a spaCy pipeline; with a written report and an oral defence.
