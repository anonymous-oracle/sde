# Topic diff: Teaching spine and folded modules

Source: gcp/unified-curriculum.md lines 2864-3406. Compared against: gcp-lite/index/*.topics.md and gcp-lite/Rust_Track_AI_Infrastructure.md.

Counts: 349 topics; 311 covered, 28 partial, 6 missing, 4 out of scope.

## IIT Kharagpur EPGC — official map
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Transformer architecture (attention, tokenisation, embeddings, positional encoding) | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Foundation models (GPT, Gemini, LLaMA, Mistral) | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| LoRA and QLoRA parameter-efficient fine-tuning | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | - |
| Fine-tune versus prompt versus RAG decision | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Chunking strategies (overlapping spans, semantic and hierarchical chunks) | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | - |
| Retrieval architectures (naive, advanced, modular pipelines) | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | - |
| Vector databases and vector stores | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | - |
| Hybrid search (dense plus sparse, reciprocal rank fusion) | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | - |
| Reranking with cross-encoders | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | - |
| RAG evaluation metrics (faithfulness, answer relevancy, context precision and recall) | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | - |
| Debugging retrieval | partial | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | Only retrieval health counters in monitoring; no retrieval debugging method. |
| Tool calling and structured JSON returns | covered | part21_generative_ai_2of3.topics.md › Model APIs | - |
| Safety prompts, retrieval-aware prompts and failure handling | partial | part22_generative_ai_3of3.topics.md › Agents and workflows | Per-agent system prompts and verifiers only; no safety-prompt or failure-handling design. |
| SQL querying (SELECT, WHERE, JOIN, GROUP BY, aggregates, subqueries) | covered | part12_databases.topics.md › The SQL language | - |
| Connecting Python to a SQL database for extraction | covered | part05_programming_languages_python_and_shell.topics.md › Shell and working with APIs from code | - |
| Vision encoders (ViT, CLIP) feeding token generation | covered | part20_generative_ai_1of3.topics.md › Multimodal models | - |
| Vision-language models | covered | part20_generative_ai_1of3.topics.md › Multimodal models | - |
| Text-to-image diffusion and image generation | partial | part20_generative_ai_1of3.topics.md › Generative models beyond autoregression | Diffusion taught generically; text-to-image conditioning (DALL·E, Stable Diffusion) not named. |
| Cross-attention for joint text and image | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Agent planning, tools and memory (Plan-Act-Track loops) | covered | part22_generative_ai_3of3.topics.md › Agents and workflows | - |
| LangGraph-style graph orchestration | covered | part22_generative_ai_3of3.topics.md › Agents and workflows | - |
| Multi-agent workflows | covered | part22_generative_ai_3of3.topics.md › Agents and workflows | - |
| Production RAG and agent deployment | covered | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | - |
| FastAPI serving | covered | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | - |
| Containers for model APIs (Docker) | covered | part18_devops_sre.topics.md › Docker | - |
| Monitoring LLM services | covered | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | - |
| Latency and token-cost monitoring | covered | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | - |
| Guardrails for agents and LLM applications | covered | part22_generative_ai_3of3.topics.md › Agents and workflows | - |
| Hallucination handling | partial | part22_generative_ai_3of3.topics.md › Exercises | Groundedness filter appears only in an exercise; no hallucination-handling method taught. |
| Privacy and data protection | covered | part14_security.topics.md › Privacy | - |
| AI governance documents (model cards, risk documentation) | partial | part19_machine_learning.topics.md › MLOps | Governance and responsible ML named; model cards and governance documents not taught. |
| Industry capstone (business problem to deployed solution) | missing | → suggest part22 | - |

## Foundational papers (cite; not textbooks)
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| RMSNorm and gated linear units (SwiGLU) | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Rotary position embeddings | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Multi-query and grouped-query attention | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Flash attention | missing | → suggest part20 | - |
| Sparse mixture-of-experts routing | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Paged memory management for serving (PagedAttention) | covered | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | - |
| Speculative decoding | covered | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | - |
| Tensor and pipeline parallelism | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Optimizer-state sharding | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Post-training quantization | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | - |
| Compute-optimal scaling | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Proximal policy optimization (PPO) | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Group relative policy optimization (GRPO) | covered | part19_machine_learning.topics.md › Specialised learning areas | Described in the reinforcement-learning line (group-relative scoring). |
| Group sequence policy optimization (GSPO) | covered | part19_machine_learning.topics.md › Specialised learning areas | Described in the reinforcement-learning line (sequence-level clipped ratio). |

## M1 Foundational arithmetic and bases
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Number bases and base conversion | covered | part02_computer_organization.topics.md › Data representation | - |
| Place value | partial | part01_school_foundations.topics.md › domain list (no group heading) | Place value not named; integers and decimals are taught. |
| Rounding and estimation | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Prime factorization, GCD and LCM | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Divisibility | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Order of operations (BODMAS) | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M2 Rational fields and the real line
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Rational numbers as a field | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis | - |
| Repeating decimals to fractions | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Absolute value | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Exponent laws | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Real-line mappings and the number sets | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M3 Set-theoretic foundations · also IIT Module 1 discrete math
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Set-builder notation, subsets and Cartesian products | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Empty, finite and infinite sets | partial | part03_mathematics.topics.md › Proof and discrete mathematics | Not named; set-builder notation and power sets are. |
| Set operations and Venn diagrams (union, intersection, complement, symmetric difference) | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| De Morgan's laws | covered | part02_computer_organization.topics.md › Digital logic | - |
| Propositional logic gates and truth tables | covered | part02_computer_organization.topics.md › Digital logic | - |

## M4 Ratios, proportions, scales
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Ratio, proportion and continued proportion | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Unitary method | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Compounding ratios | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Direct and inverse variation | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Componendo, dividendo, alternendo and invertendo | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Scale factors | partial | part01_school_foundations.topics.md › domain list (no group heading) | Scale factors not named; area ratios of similar figures are. |

## M5 Foundational algebra
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Polynomial identities | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Substitution | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Linear equations and translating word problems | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M6 Linear inequations in one variable
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Linear inequalities and multiplying by negatives | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Interval notation and solution sets | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M7 Quadratic equations
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Quadratic formula, discriminant and nature of roots (Shridharacharya's method) | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Splitting the middle term | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Equations reducible to quadratics | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M8 Polynomial factors and remainder theorems
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Remainder and factor theorems | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Polynomial long division (division algorithm) | partial | part01_school_foundations.topics.md › domain list (no group heading) | Only synthetic division is taught. |
| Synthetic division | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Factoring cubics | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M9 Matrices and 2D linear systems · also IIT Module 2 primitives
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Matrix order, addition, multiplication and transpose | covered | part03_mathematics.topics.md › Linear algebra | - |
| Two-by-two determinants | covered | part03_mathematics.topics.md › Linear algebra | - |
| Linear mappings by row substitution (Gaussian elimination) | covered | part03_mathematics.topics.md › Linear algebra | - |
| Two-variable linear systems | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| NumPy arrays | covered | part05_programming_languages_python_and_shell.topics.md › Python | - |

## M10 Arithmetic progressions
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Arithmetic progressions and their sums | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Arithmetic mean | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M11 Geometric progressions
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Geometric progressions, finite and infinite sums | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Geometric mean | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M12 Foundational coordinate geometry · IIT Module 1 coordinate maps
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Section and midpoint formulas | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Centroid | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Distance metrics (Euclidean, Manhattan, cosine) | covered | part03_mathematics.topics.md › Linear algebra | - |

## M13 Linear equations in two variables · IIT Module 1 linear systems
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Slope and line forms | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Parallel and perpendicular lines | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Intersection of lines | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M14 Euclidean geometry of triangles (JEE aptitude)
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Triangle congruence and similarity | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Thales and basic proportionality theorem | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Midpoint theorem | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Area ratios of similar figures | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M15 Circle geometry and tangents (JEE aptitude)
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Circle theorems (angles at the centre and in a segment) | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Cyclic quadrilaterals and concyclic points | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Tangents, secants and intersecting chords | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M16 Classical mensuration
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Plane areas, surface areas and volumes of solids | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M17 Foundational trigonometry
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Six trigonometric ratios and the Pythagorean identity | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Heights and distances (elevation and depression) | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M18 Commercial arithmetic
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| VAT and GST | out of scope | - | ARCHIVE item. |
| Recurring deposits | out of scope | - | ARCHIVE item. |
| Shares and dividends | out of scope | - | ARCHIVE item. |
| Percentages, markup and interest | out of scope | - | ARCHIVE item. |

## M19 Relations, equivalence, functions
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Equivalence relations and classes | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Injective, surjective and bijective functions | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Composition and inverse functions | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Floor, fractional part and signum functions | partial | part01_school_foundations.topics.md › domain list (no group heading) | Floor and fractional part taught; signum not named. |

## M20 Complex fields and roots of unity
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Complex numbers and the complex field | covered | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis | - |
| Polar and Euler form, modulus and argument | covered | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis | - |
| De Moivre's theorem and n-th roots of unity | covered | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis | - |
| Triangle inequalities for complex numbers | covered | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis | - |
| Argand plane and geometric maps | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M21 Combinatorics and permutations
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Counting principle (sum and product rules) | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Permutations and combinations | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Circular permutations | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Stars and bars for identical objects | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |

## M22 Binomial and multinomial theorems
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Binomial theorem and general term | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Middle term of an expansion | partial | part03_mathematics.topics.md › Proof and discrete mathematics | Middle term not taught; general term is. |
| Multinomial theorem and expansion | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |

## M23 Plane trigonometry and equations
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Periodic functions and graphs | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Addition, multiple and half-angle formulas | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| General solutions of trigonometric equations | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Inverse trigonometric functions and principal values | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M24 Advanced coordinate geometry: circle
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| General second-degree equation and tracing of conics | covered | part03b_analysis_calculus_and_number_theory.topics.md › Coordinate geometry and conics | - |
| Parametric form of the circle | partial | part01_school_foundations.topics.md › domain list (no group heading) | Centre-radius and general forms only; parametric form not named. |
| Tangent and normal to a conic | covered | part03b_analysis_calculus_and_number_theory.topics.md › Coordinate geometry and conics | - |
| Chord of contact, director circle and orthogonal circles | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Pole and polar | covered | part03b_analysis_calculus_and_number_theory.topics.md › Coordinate geometry and conics | - |

## M25 Conic sections
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Eccentricity, focus and directrix | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Parabola, ellipse and hyperbola | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Auxiliary circles and asymptotes | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M26 Matrices, determinants, Cramer's rule
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Three-by-three determinants, adjoint and inverse | partial | part03_mathematics.topics.md › Linear algebra | Determinant ratios and Gaussian elimination only; adjugate and inverse formula not taught. |
| Row and column operations | covered | part03_mathematics.topics.md › Linear algebra | - |
| Symmetric and skew-symmetric matrices | covered | part03_mathematics.topics.md › Linear algebra | - |
| Simultaneous linear systems and Cramer's rule | covered | part03_mathematics.topics.md › Linear algebra | - |

## M27 Vector algebra and triple products
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Direction cosines and direction ratios | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Dot and cross products | covered | part03_mathematics.topics.md › Linear algebra | - |
| Scalar triple product | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Vector triple product | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |

## M28 Three-dimensional coordinate space
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Skew lines, line forms and their distance | partial | part01_school_foundations.topics.md › domain list (no group heading) | Skew lines and line forms covered; distance between skew lines not taught. |
| Planes and point-to-plane distance | covered | part01_school_foundations.topics.md › domain list (no group heading) | - |
| Angles between lines and planes | covered | part03b_analysis_calculus_and_number_theory.topics.md › Coordinate geometry and conics | - |
| Quadric surfaces | missing | → suggest part03b | - |
| Cylindrical and spherical coordinates | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |

## M29 Real limits and continuity
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Epsilon-delta limits and limit laws | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis | - |
| Intermediate value theorem | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis | - |
| Indeterminate forms and L'Hôpital's rule | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Continuity | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis | - |

## M30 Differential calculus
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| First-principles derivatives, product, quotient and chain rules | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Implicit and parametric differentiation | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Higher-order derivatives | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Finite-difference gradient kernels | covered | part03_mathematics.topics.md › Numerical computing | - |

## M31 Applications of derivatives
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Rates of change and related rates | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Tangents and normals | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Rolle's theorem and mean value theorems | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis | - |
| Monotonicity | partial | part01_school_foundations.topics.md › domain list (no group heading) | Named in a list only; no derivative-sign monotonicity test. |
| Local and absolute extrema | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Gradient descent as the first optimization habit | covered | part03_mathematics.topics.md › Calculus and optimization | - |

## M32 Indefinite and definite integration
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Antiderivatives and integration techniques (substitution, parts) | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Partial fractions | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Riemann sums and Darboux integrals | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis | - |
| Fundamental theorem of calculus | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Properties of definite integrals | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |

## M33 Applications of integrals
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Area under and between curves | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Symmetry in integration | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |

## M34 Ordinary differential equations
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Order, degree and formation of ODEs | partial | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | Order and degree not named; solution methods are. |
| Separable and homogeneous first-order equations | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Linear first-order equations and integrating factors | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Numerical IVP solvers (Euler, RK4) | covered | part03_mathematics.topics.md › Calculus and optimization | - |

## M35 ODE and PDE systems
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Linear ODEs with constant coefficients | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Series solutions, Bessel and Legendre functions | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Beta and Gamma functions | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |
| Partial differential equations | covered | part03b_analysis_calculus_and_number_theory.topics.md › Calculus and differential equations | - |

## M36 Advanced transform calculus · feeds DSP
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Laplace transform and its inverse | covered | part03c_signals_systems_and_communications.topics.md › Transforms and system analysis | - |
| Convolution theorem | covered | part03_mathematics.topics.md › Signals and sequences | - |
| Fourier series, integrals and transforms | covered | part03c_signals_systems_and_communications.topics.md › Transforms and system analysis | - |
| z-transform and region of convergence | covered | part03c_signals_systems_and_communications.topics.md › Transforms and system analysis | - |
| Transfer functions | covered | part03c_signals_systems_and_communications.topics.md › Transforms and system analysis | - |

## M37 Numerical methods and difference equations
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Curve fitting and interpolation | covered | part03_mathematics.topics.md › Numerical computing | - |
| Finite differences and numerical differentiation and integration | covered | part03_mathematics.topics.md › Numerical computing | - |
| Difference equations | covered | part03_mathematics.topics.md › Proof and discrete mathematics | - |
| Error propagation | covered | part03_mathematics.topics.md › Numerical computing | - |
| SciPy | covered | part05_programming_languages_python_and_shell.topics.md › Python | - |

## M38 Topological real analysis (ceiling: undergraduate analysis, not research)
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Metric spaces, open and closed sets, limit points | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis | - |
| Cauchy sequences and completeness | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis | - |
| Compactness and Heine-Borel | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis | - |
| Continuous maps, uniform continuity and uniform convergence | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis | - |
| Stone-Weierstrass theorem | covered | part03b_analysis_calculus_and_number_theory.topics.md › Real analysis | - |

## M39 Spectral theory and matrix decompositions
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Inner products and Hilbert spaces | covered | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis | - |
| Orthonormal bases and Gram-Schmidt | covered | part03_mathematics.topics.md › Linear algebra | - |
| Self-adjoint operators and the spectral theorem | covered | part03b_analysis_calculus_and_number_theory.topics.md › Complex and functional analysis | - |
| Singular value decomposition and low-rank approximation | covered | part03_mathematics.topics.md › Linear algebra | - |
| Matrix norms | partial | part03_mathematics.topics.md › Numerical computing | Norms appear only inside the condition number. |
| Power iteration and Hotelling deflation | covered | part03_mathematics.topics.md › Linear algebra | - |
| Eigendecomposition | covered | part03_mathematics.topics.md › Linear algebra | - |
| Principal component analysis | covered | part03_mathematics.topics.md › Linear algebra | - |

## M40 Mathematical statistics and inference · absorbs IIT Module 3 and STAT 1–9
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Joint, marginal and conditional distributions | covered | part03_mathematics.topics.md › Probability | - |
| Parameter estimation and maximum likelihood | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Fisher information and the Cramér-Rao bound | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Hypothesis testing | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Confidence intervals | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Bayesian inference (prior and posterior) | covered | part03_mathematics.topics.md › Statistics and experimental design | - |
| Markov chain Monte Carlo | partial | part19_machine_learning.topics.md › Classical AI: search, knowledge and reasoning | Named with Metropolis-Hastings and Gibbs in one line; no MCMC treatment in the statistics group. |
| Bayes' theorem | covered | part03_mathematics.topics.md › Probability | - |
| Expectation and variance | covered | part03_mathematics.topics.md › Probability | - |

## M41 Digital signal processing
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Sampling theorem and aliasing | covered | part03c_signals_systems_and_communications.topics.md › Signals and linear time-invariant systems | - |
| Discrete-time LTI systems | covered | part03c_signals_systems_and_communications.topics.md › Signals and linear time-invariant systems | - |
| DFT and FFT | covered | part03_mathematics.topics.md › Signals and sequences | - |
| FIR and IIR filter design | covered | part03c_signals_systems_and_communications.topics.md › Digital filters and multirate processing | - |
| Cepstral analysis | covered | part03c_signals_systems_and_communications.topics.md › Practical spectral analysis | - |
| Short-time Fourier transform | covered | part03_mathematics.topics.md › Signals and sequences | - |
| Linear predictive coding (LPC) | covered | part03c_signals_systems_and_communications.topics.md › Practical spectral analysis | - |
| Filter banks | covered | part03c_signals_systems_and_communications.topics.md › Digital filters and multirate processing | - |

## M42 Digital image processing · Computer vision entry
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| 2D sampling and quantization | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Computer vision: images, motion and multi-view geometry | - |
| 2D discrete convolution | partial | part19_machine_learning.topics.md › Specialised learning areas | Named in one line; no discrete 2D convolution treatment. |
| Spatial filters (smoothing, sharpening, Sobel, Laplacian of Gaussian) | partial | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Computer vision: images, motion and multi-view geometry | Smoothing and sharpening taught; Sobel named once in part03; Laplacian of Gaussian absent. |
| Morphological operations | partial | part03_mathematics.topics.md › Signals and sequences | Named once; erosion, dilation and opening not taught. |
| Frequency-domain filtering | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Computer vision: images, motion and multi-view geometry | - |
| Image restoration and noise models | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Computer vision: images, motion and multi-view geometry | - |
| Histogram equalization | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Computer vision: images, motion and multi-view geometry | - |
| Structure from motion and SLAM | missing | → suggest part19b | - |
| Depth and stereo | covered | part19_machine_learning.topics.md › Classical computer vision and geometry | - |
| 3D reconstruction and image-based rendering | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Computer vision: images, motion and multi-view geometry | - |
| Multi-view geometry | covered | part19_machine_learning.topics.md › Classical computer vision and geometry | - |
| Entropy | covered | part03_mathematics.topics.md › Information theory | - |
| Mutual information | covered | part03_mathematics.topics.md › Information theory | - |
| KL divergence and cross-entropy | covered | part03_mathematics.topics.md › Information theory | - |
| Shannon's source and channel coding theorems | covered | part03_mathematics.topics.md › Information theory | - |

## M43 Kaldi-level acoustic modeling
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Speech production and human hearing | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech science and analysis | - |
| MFCC and PLP features | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech science and analysis | - |
| i-vectors | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech synthesis, speakers and spoken-language systems | - |
| Hidden Markov models | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi | - |
| Gaussian mixture models and the EM algorithm | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Forward-backward recursion | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi | - |
| State clustering and phonetic decision trees | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi | - |
| Speech coding (PCM, µ-law, CELP) | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech science and analysis | - |
| Robustness to noise and channel | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech science and analysis | - |
| Neural ASR (CTC, Conformer, self-supervised speech) | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi | - |
| Text-to-speech synthesis | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech synthesis, speakers and spoken-language systems | - |
| Spoken language understanding and dialogue | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech synthesis, speakers and spoken-language systems | - |
| Kaldi recipes, scripting and deployment | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi | - |
| DNN-HMM hybrid systems | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi | - |

## M44 OpenFst-based automata
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Weighted finite-state transducers | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi | - |
| Word and phone symbol tables | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi | - |
| Transducer composition of H, C, L and G | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi | - |
| Determinization and minimization | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi | - |
| Epsilon removal | missing | → suggest part19b | - |
| Disambiguation symbols and self-loop addition | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi | - |
| Viterbi decoding graphs | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi | - |
| N-gram language models, perplexity and Kneser-Ney smoothing | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Classical NLP and toolkits | - |
| Lexicon and context-dependency transducers | covered | part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md › Speech recognition: from HMMs to Kaldi | - |
| OpenFst library and composition simulation | missing | → suggest part19b | - |

## Folded DL Module 1 — Math and ML primitives
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Tensors and computational graphs | covered | part19_machine_learning.topics.md › Deep learning | - |
| Partial derivatives and Hessians | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Model capacity, over- and underfitting, bias-variance | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Logistic regression | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Support vector machines | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| Naive Bayes, k-nearest neighbours and discriminant analysis | covered | part19_machine_learning.topics.md › Classical machine learning | - |

## Folded DL Module 2–3 and IIT Module 4 — Neural nets
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Perceptron and multilayer perceptrons | covered | part19_machine_learning.topics.md › Deep learning | - |
| Activation functions (sigmoid, tanh, ReLU, GELU, Swish) | covered | part19_machine_learning.topics.md › Deep learning | - |
| Cost functions and output units | covered | part19_machine_learning.topics.md › Deep learning | - |
| Backpropagation | covered | part19_machine_learning.topics.md › Deep learning | - |
| Layer width versus depth; universal approximation | covered | part19_machine_learning.topics.md › Deep learning | - |
| L1 and L2 regularization | covered | part03_mathematics.topics.md › Calculus and optimization | - |
| Data augmentation, noise injection and early stopping | covered | part19_machine_learning.topics.md › Deep learning | - |
| Parameter tying and dropout | covered | part19_machine_learning.topics.md › Deep learning | - |
| Ensembles | covered | part19_machine_learning.topics.md › Classical machine learning | - |
| SGD, mini-batch, momentum and Nesterov | covered | part19_machine_learning.topics.md › Deep learning | - |
| AdaGrad, RMSProp and Adam | covered | part19_machine_learning.topics.md › Deep learning | - |
| BatchNorm and LayerNorm | covered | part19_machine_learning.topics.md › Deep learning | - |

## Folded DL Module 4 — CNNs / CV
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Convolution with padding, stride and dilation | covered | part19_machine_learning.topics.md › Deep learning | - |
| Pooling and translation invariance | covered | part19_machine_learning.topics.md › Deep learning | - |
| LeNet, AlexNet, VGG, Inception and ResNet | covered | part19_machine_learning.topics.md › Deep learning | - |
| Object detection (R-CNN, YOLO) and segmentation | covered | part19_machine_learning.topics.md › Classical computer vision and geometry | - |
| Visualizing convolutional networks | covered | part19_machine_learning.topics.md › Deep learning | - |

## Folded DL Module 5 — Sequence models
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| RNN unrolling and backpropagation through time | covered | part19_machine_learning.topics.md › Deep learning | - |
| Vanishing and exploding gradients | covered | part19_machine_learning.topics.md › Deep learning | - |
| LSTM and GRU | covered | part19_machine_learning.topics.md › Deep learning | - |
| Bidirectional and deep RNNs | covered | part19_machine_learning.topics.md › Deep learning | - |
| Encoder-decoder sequence-to-sequence models | covered | part19_machine_learning.topics.md › Deep learning | - |
| Time-series forecasting | partial | part19_machine_learning.topics.md › Applied problem families | Forecast intervals and quantile forecasting only; no time-series models such as ARIMA. |

## M45 Attention and transformers · IIT Module 5–6, DL Module 6
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Tokenization (BPE, WordPiece) | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Token embeddings and sinusoidal positional encoding | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Scaled dot-product and multi-head attention | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Residual connections and layer normalization | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Decoder causal masking | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Unembedding and softmax normalization | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| BERT, GPT and T5 model families | covered | part20_generative_ai_1of3.topics.md › How LLMs work | - |
| Instruction tuning, RLHF and DPO | covered | part20_generative_ai_1of3.topics.md › How LLMs work | DPO is taught under Fine-tuning and adaptation. |

## Folded DL Module 7 — Generative models (to industry competence, not research depth)
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Autoencoders (undercomplete, sparse, denoising) | partial | part19_machine_learning.topics.md › Specialised learning areas | Autoencoders named once with a bottleneck; sparse and denoising variants not taught. |
| Representation and manifold learning | covered | part20_generative_ai_1of3.topics.md › Generative models beyond autoregression | - |
| Variational autoencoders | covered | part20_generative_ai_1of3.topics.md › Generative models beyond autoregression | - |
| Generative adversarial networks | covered | part20_generative_ai_1of3.topics.md › Generative models beyond autoregression | - |
| Diffusion models and normalizing flows | covered | part20_generative_ai_1of3.topics.md › Generative models beyond autoregression | - |
| Graph neural networks | covered | part19_machine_learning.topics.md › Specialised learning areas | - |

## Folded IIT Module 7 / Lecture prompting — Prompt engineering
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| System and user prompts, system routing tokens | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| Zero-shot and few-shot prompting | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| Chain-of-thought prompting | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| Self-consistency | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| Tree of Thoughts | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| ReAct | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| Meta-prompting | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| Directional stimulus prompting | covered | part21_generative_ai_2of3.topics.md › Prompt, context and output engineering | - |
| Structural boundary checking | partial | part22_generative_ai_3of3.topics.md › Agents and workflows | Per-agent typed hand-offs and verifiers only; boundary checks not taught. |

## Folded IIT Module 8 / RAG lectures — RAG
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Document parsing and structural parsing blocks | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | - |
| k-NN and approximate nearest-neighbour vector indexes | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | - |
| IVF, product quantization, HNSW and FAISS versus Chroma | covered | part20_generative_ai_1of3.topics.md › Embeddings and retrieval | - |
| Agentic RAG | covered | part21_generative_ai_2of3.topics.md › Retrieval-augmented generation | - |
| BM25 and inverted indexes | covered | part19_machine_learning.topics.md › Applied problem families | - |

## Folded IIT Module 9 — PEFT
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Adapter-only optimization | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | - |
| Comparing adapters to the base model | partial | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | Adapters start at the base model; no comparison methodology. |

## Folded IIT Modules 10–11 — Multimodal and agents
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| Audio encoders (Whisper) feeding token generation | partial | part20_generative_ai_1of3.topics.md › How LLMs work | Whisper named in passing; no audio-to-token design taught. |

## Folded IIT Modules 12–13 and DL Module 8 — Serving, safety, hardware
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| GPUs and TPUs | covered | part02_computer_organization.topics.md › Machine organization | - |
| TensorFlow and PyTorch | covered | part19_machine_learning.topics.md › Machine learning in Python | - |
| Edge and on-device model deployment | covered | part19_machine_learning.topics.md › Specialised learning areas | - |
| Pruning | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | - |
| Distillation | covered | part20_generative_ai_1of3.topics.md › Fine-tuning and adaptation | - |

## M46 Enterprise production MLOps / GCP PMLE
| Topic | Status | gcp-lite location | Note |
|---|---|---|---|
| BigQuery ML | partial | part23_cloud_providers_1of2.topics.md › Google Cloud — storage and databases | BigQuery named; BigQuery ML not taught. |
| AutoML and Vizier hyperparameter tuning | covered | part23_cloud_providers_1of2.topics.md › Google Cloud — AI and ML | - |
| Gemini Enterprise Agent Platform (formerly Vertex AI) | covered | part23_cloud_providers_1of2.topics.md › Google Cloud — AI and ML | - |
| Feature stores with point-in-time correctness | covered | part19_machine_learning.topics.md › MLOps | - |
| ML metadata and artifact lineage | covered | part19_machine_learning.topics.md › MLOps | - |
| Batch and online inference | covered | part19_machine_learning.topics.md › Applied problem families | - |
| Endpoints, multi-model endpoints and custom containers | covered | part19_machine_learning.topics.md › MLOps | - |
| Vertex Pipelines and Kubeflow Pipelines | covered | part19_machine_learning.topics.md › MLOps | - |
| TFX components | covered | part19_machine_learning.topics.md › MLOps | - |
| Experiment tracking (MLflow, Weights and Biases) | covered | part19_machine_learning.topics.md › MLOps | - |
| Apache Beam on Dataflow | covered | part23_cloud_providers_1of2.topics.md › Google Cloud — data and analytics | - |
| Preemptible and spot capacity | covered | part16_cloud_core.topics.md › Cloud economics and FinOps | - |
| Cloud Composer | covered | part23_cloud_providers_1of2.topics.md › Google Cloud — data and analytics | - |
| Cloud Build | covered | part23_cloud_providers_1of2.topics.md › Google Cloud — operations, DevOps and cost | - |
| Drift detection and Model Monitoring | covered | part19_machine_learning.topics.md › MLOps | - |
| Population stability index | covered | part19_machine_learning.topics.md › MLOps | - |
| TensorFlow Data Validation | covered | part19_machine_learning.topics.md › MLOps | - |
| Explainable AI (Integrated Gradients, SHAP) | covered | part19_machine_learning.topics.md › Deep learning | - |
| Fairness Lens and fairness evaluation | covered | part19_machine_learning.topics.md › MLOps | - |
| Retraining policy | covered | part19_machine_learning.topics.md › MLOps | - |
| Responsible AI | covered | part19_machine_learning.topics.md › MLOps | - |
| Troubleshooting ML pipelines and deployments | partial | part19_machine_learning.topics.md › MLOps | Incident runbooks only; no troubleshooting method. |
| Ray distributed workloads | covered | part22_generative_ai_3of3.topics.md › Application architecture and LLMOps | - |
| PySpark | covered | part19_machine_learning.topics.md › Machine learning in Python | - |
| Dask | covered | part19_machine_learning.topics.md › Machine learning in Python | - |
| Evidently drift monitoring | covered | part19_machine_learning.topics.md › MLOps | - |

## Missing in this range
- Flash attention (→ suggest part20) — from: Foundational papers (cite; not textbooks)
- Industry capstone (business problem to deployed solution) (→ suggest part22) — from: IIT Kharagpur EPGC — official map
- Quadric surfaces (→ suggest part03b) — from: M28 Three-dimensional coordinate space
- Structure from motion and SLAM (→ suggest part19b) — from: M42 Digital image processing · Computer vision entry
- Epsilon removal (→ suggest part19b) — from: M44 OpenFst-based automata
- OpenFst library and composition simulation (→ suggest part19b) — from: M44 OpenFst-based automata

## Partial in this range
- Debugging retrieval — Only retrieval health counters in monitoring; no retrieval debugging method. — part22_generative_ai_3of3.topics.md
- Safety prompts, retrieval-aware prompts and failure handling — Per-agent system prompts and verifiers only; no safety-prompt or failure-handling design. — part22_generative_ai_3of3.topics.md
- Text-to-image diffusion and image generation — Diffusion taught generically; text-to-image conditioning (DALL·E, Stable Diffusion) not named. — part20_generative_ai_1of3.topics.md
- Hallucination handling — Groundedness filter appears only in an exercise; no hallucination-handling method taught. — part22_generative_ai_3of3.topics.md
- AI governance documents (model cards, risk documentation) — Governance and responsible ML named; model cards and governance documents not taught. — part19_machine_learning.topics.md
- Place value — Place value not named; integers and decimals are taught. — part01_school_foundations.topics.md
- Polynomial long division (division algorithm) — Only synthetic division is taught. — part01_school_foundations.topics.md
- Empty, finite and infinite sets — Not named; set-builder notation and power sets are. — part03_mathematics.topics.md
- Scale factors — Scale factors not named; area ratios of similar figures are. — part01_school_foundations.topics.md
- Middle term of an expansion — Middle term not taught; general term is. — part03_mathematics.topics.md
- Floor, fractional part and signum functions — Floor and fractional part taught; signum not named. — part01_school_foundations.topics.md
- Parametric form of the circle — Centre-radius and general forms only; parametric form not named. — part01_school_foundations.topics.md
- Three-by-three determinants, adjoint and inverse — Determinant ratios and Gaussian elimination only; adjugate and inverse formula not taught. — part03_mathematics.topics.md
- Skew lines, line forms and their distance — Skew lines and line forms covered; distance between skew lines not taught. — part01_school_foundations.topics.md
- Monotonicity — Named in a list only; no derivative-sign monotonicity test. — part01_school_foundations.topics.md
- Order, degree and formation of ODEs — Order and degree not named; solution methods are. — part03b_analysis_calculus_and_number_theory.topics.md
- Matrix norms — Norms appear only inside the condition number. — part03_mathematics.topics.md
- Markov chain Monte Carlo — Named with Metropolis-Hastings and Gibbs in one line; no MCMC treatment in the statistics group. — part19_machine_learning.topics.md
- 2D discrete convolution — Named in one line; no discrete 2D convolution treatment. — part19_machine_learning.topics.md
- Spatial filters (smoothing, sharpening, Sobel, Laplacian of Gaussian) — Smoothing and sharpening taught; Sobel named once in part03; Laplacian of Gaussian absent. — part19b_speech_vision_retrieval_and_nlp_toolkits.topics.md
- Morphological operations — Named once; erosion, dilation and opening not taught. — part03_mathematics.topics.md
- Time-series forecasting — Forecast intervals and quantile forecasting only; no time-series models such as ARIMA. — part19_machine_learning.topics.md
- Autoencoders (undercomplete, sparse, denoising) — Autoencoders named once with a bottleneck; sparse and denoising variants not taught. — part19_machine_learning.topics.md
- Comparing adapters to the base model — Adapters start at the base model; no comparison methodology. — part20_generative_ai_1of3.topics.md
- Audio encoders (Whisper) feeding token generation — Whisper named in passing; no audio-to-token design taught. — part20_generative_ai_1of3.topics.md
- BigQuery ML — BigQuery named; BigQuery ML not taught. — part23_cloud_providers_1of2.topics.md
- Troubleshooting ML pipelines and deployments — Incident runbooks only; no troubleshooting method. — part19_machine_learning.topics.md
- Structural boundary checking — Per-agent typed hand-offs and verifiers only; boundary checks not taught. — part22_generative_ai_3of3.topics.md
