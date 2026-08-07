## Section 1: Top 5 Papers

1. **SkillTFM: Gated Skill Evolution for Training-Free Adaptation of Tabular Foundation Models**  
   **Authors:** Yi He, Zhengkang Guan, Anpeng Wu, Peng Cui, Fei Wu, Kun Kuang  
   **Venue/source:** arXiv cs.LG  
   **Release date:** 2026-08-07  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   **Summary:** SkillTFM attacks a practical weakness of tabular foundation models: strong zero-shot priors still fail under distribution shift, feature-semantic heterogeneity, and task-specific boundary structure. Instead of fine-tuning, it builds a verifiable “skill bank” that identifies boundary evidence and evolves gated reusable skills, apparently in an agentic adaptation loop. The reported gains are large in simulated boundary settings and electricity-price forecasting, including nonlinear-boundary AUC improvement from 0.699 to 0.898. The idea is worth tracking because it reframes TFM adaptation as reusable, validated procedural knowledge rather than weight updates.  
   **Why you should care:** This is one of the clearest recent attempts to make tabular FMs operational under shift without paying the fine-tuning/data-labeling cost.

2. **Matrix Zonotopic Attention: A Context-Adaptive Value Projection for Set Transformers**  
   **Authors:** Zhen Zhang, Amr Alanwar  
   **Venue/source:** arXiv cs.LG  
   **Release date:** 2026-08-07  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   **Summary:** This paper isolates an under-discussed asymmetry in attention: routing is input-dependent, but the value projection is fixed across input sets. The authors define “Transformation Degrees of Freedom” as a target-complexity measure and give a depth-separation argument: standard context-rigid attention may require depth proportional to this complexity, whereas a context-adaptive value family can express the same set target in one layer. Matrix Zonotopic Attention replaces the fixed value projection with a gated matrix-zonotope family while preserving permutation equivariance. The work is especially relevant to tabular, relational, and set-valued foundation models where the target operator may depend on high-rank combinatorial structure.  
   **Why you should care:** It offers a crisp architectural diagnosis for why attention over sets/tables may need more than better routing.

3. **The Loss Does Not See the Basis, but Adam Does**  
   **Authors:** Devender Singh  
   **Venue/source:** arXiv cs.LG / stat.ML cross-list  
   **Release date:** 2026-08-07 listing  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/stat.ML/new))  
   **Summary:** The paper studies optimizer-induced implicit bias through gauge symmetry in factored models. Gradient descent on \(W=UV^\top\) inherits low-rank bias because its dynamics are gauge-equivariant; coordinate-wise optimizers such as Adam and RMSProp break that symmetry. The paper gives a structure theorem for memoryless equivariant rules, experiments on matrix sensing, and transformer diagnostics showing that Adam separates gauge-equivalent initializations immediately and leads to per-head invariant differences that rotations cannot undo. The thesis is important: basis choice is not a harmless parameterization detail when adaptive optimizers decide which interpolating solution is selected.  
   **Why you should care:** It connects optimizer geometry, representation selection, low-rank structure, and transformer head behavior in a way likely to influence future optimizer-theory discussions.

4. **Hypothesis Testing with Conditional Queries: Learnability and the Value of Interaction**  
   **Authors:** Zonghuan Xu  
   **Venue/source:** arXiv cs.LG / math.ST  
   **Release date:** 2026-08-07  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   **Summary:** This theory paper asks when adaptive interaction truly helps in statistical testing. In a finite conditional-query model, it characterizes learnability by separation in pairwise conditional probabilities; when separation is zero, the finite-query worst-case error remains exactly \(1/2\). It then shows that any adaptive \(T\)-query policy can be simulated nonadaptively with \(O(N^2(T+\log(1/\rho)))\) pair queries up to total-variation error \(\rho\), while also constructing a matching family with a quadratic adaptivity gap. The message is nuanced: interaction helps substantially, but not exponentially, for this testing model.  
   **Why you should care:** It gives useful formal language for evaluating interactive model audits, adaptive benchmarks, and agentic testing protocols.

5. **Tytan: Interactive Neurosymbolic Construction of Analytic Semantic Schemas from Relational Data**  
   **Authors:** Donna Hooshmand, Shubham Shahi, Cameron Barrie, Abhratanu Dutta, Marko Sterbentz, Harper Pack, Kristian J. Hammond  
   **Venue/source:** arXiv cs.DB  
   **Release date:** 2026-08-07  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.DB/new))  
   **Summary:** TYTAN automates a painful data-management layer: constructing analytic semantic schemas from relational databases. It combines symbolic database analysis with LLM-based inference for entity proposal, role assignment, and naming, and asks targeted natural-language questions when evidence is ambiguous. Evaluation spans eight databases, with reported full coverage of expert-corrected schema entities/features, 1,678/1,678 executable self-generated retrieval instructions, and high semantic-role agreement. This is directly relevant to data discovery, semantic layers, NL-to-data interfaces, and agentic analysis systems, where schema understanding is a bottleneck and a major source of silent errors.  
   **Why you should care:** It is a concrete neurosymbolic bridge from raw relational structure to reusable analytic metadata for data agents.

## Section 2: Venue Watch

- **arXiv cs.LG/stat.ML daily stream, 2026-08-07.** The new cs.LG listing shows 74 new submissions out of 260 total entries, and stat.ML shows 9 new submissions out of 39 entries. The most relevant clusters were: tabular-FM adaptation; attention/set-transformer architecture; optimizer implicit bias; conformal/localized inference; adaptive testing; probabilistic uncertainty heads; LLM/agent post-training; figure-reading reliability; and time-series/self-supervised representation learning. The stream is unusually aligned with Adam’s interests: several papers are not just empirical benchmark improvements but propose new conceptual objects—skills, zonotopic value maps, conditional-query testers, and semantic schemas. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **arXiv cs.DB daily stream, 2026-08-07.** The cs.DB listing shows 6 new submissions out of 18 total entries. Themes were strongly “AI-native data systems”: semantic isolation for durable AI workflows; filtered vector search inside lakehouse table formats; interactive semantic-schema construction; synthetic clinical benchmark realism; and classic database optimization such as window-function co-evaluation. The notable shift is that agent/data-management papers are becoming more transactional and systems-minded: reproducibility, semantic environment isolation, schema acquisition, and vector search are being discussed as database concerns, not just ML application glue. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

- **TMLR August 2026 accepted-paper stream, incremental watch.** The visible August TMLR page now includes a fairly broad batch: SAFT for AMR-to-text, minimax classifier rates under margin conditions, preference-model/RLHF human-influence work, natural actor-critic analysis, Transformer–SSM hybrid language models, representational consistency for disentanglement, instance-level generation for representation learning, structured set utility, a Survey-certified agent-memory survey, vector information capacity, inference-time computation benchmarks, and several governance/safety/evaluation items. Since earlier August TMLR activity was already covered, the useful signal here is the continuing concentration around representation geometry, agent memory, hybrid sequence architectures, and evaluation infrastructure. ([jmlr.org](https://jmlr.org/tmlr/papers/))

## Section 3: Emerging Trends

- **Tabular foundation models are moving from “which backbone wins?” to “how do we adapt safely under shift?”** SkillTFM, recent TFM context-sampling work, and OOD/tabular-failure diagnostics all point toward adaptation, skill reuse, boundary evidence, and deployment constraints as the next frontier.

- **Attention theory is becoming more operator-aware.** Matrix Zonotopic Attention and recent head-count/attention lower-bound work suggest a shift from generic expressivity claims toward identifying which target operators require context-adaptive transformations, multiple heads, or additional depth.

- **Evaluation is becoming interactive, but theory is catching up.** Conditional-query testing, Bayesian active model evaluation, confidence horizons, and agent-audit papers are converging on a key question: when does adaptivity buy information versus merely generate a complicated transcript?

- **Data systems for agents are acquiring transaction-like semantics.** Semantic isolation, graph/bitemporal memories, token-native storage, semantic schemas, and RAG serving stacks all treat the AI workflow’s environment as mutable state that needs contracts, provenance, and optimization.

- **Optimizer implicit bias is no longer just “SGD vs Adam.”** Gauge symmetry, Muon/SOAP analyses, and basis-dependent adaptive methods are making optimizer choice a representation-learning decision, especially in factored, low-rank, or attention-heavy models.

## Section 4: Worth Watching

- **BEGIN AI TRANSACTION: Semantic Isolation for Durable AI Workflows** — Barzan Mozafari’s short cs.DB paper defines semantic read skew, compatibility skew, context escape, and merge skew for long-lived AI workflows whose prompts, tools, indexes, policies, and model aliases can change mid-run. Worth suppressing as a concrete SemIso/semantic-transaction item. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

- **PoolBench: A Benchmark for Pooling Strategies in Concept Representation Evaluation for Decoder-Only LLMs** — a reusable protocol with 17 concepts, 19 pooling strategies, three open models, an audited corpus, pre-extracted activations, scorer models, steering vectors, and evaluation code. The negative result—detection strength does not imply steering strength—is the part to remember. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **Filtered Vector Search in a Disaggregated Lakehouse** — IBM Research paper embedding IVF indexes in Parquet footers and composing Iceberg-style file pruning with per-file ANN. This is a practical vector-search/data-lake design pattern, not just another ANN index. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

- **RENDEQ / REND-EQUIV figure-reading reliability resources** — paired papers by Khanbayov and Kurban use programmatically re-rendered scientific figures to test when agreement tracks correctness and when label-free consistency has computable blind spots. Strong benchmark-design ideas for multimodal tabular/figure reasoning. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **THBKG: Temporal Heterogeneous Biomedical Knowledge Graph** — a time-stamped biomedical KG with 110,396 entities and 11.1M edges for decision-aligned target–disease advancement prediction. Interesting as a temporal evidence graph and retrospective validation substrate. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

## Section 5: Discord Highlights

**Aug 7 brief — Top 5 papers**

1. **SkillTFM: Gated Skill Evolution for Training-Free Adaptation of Tabular Foundation Models** — training-free skill-bank adaptation for TFMs under shift.  
2. **Matrix Zonotopic Attention** — context-adaptive value projections with a set-transformer depth-separation story.  
3. **The Loss Does Not See the Basis, but Adam Does** — gauge symmetry explains why adaptive optimizers pick different interpolants.  
4. **Hypothesis Testing with Conditional Queries** — formal limits on the value of interactive/adaptive testing.  
5. **Tytan** — neurosymbolic construction of analytic semantic schemas from relational databases.  

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-08-07","type":"paper","title":"SkillTFM: Gated Skill Evolution for Training-Free Adaptation of Tabular Foundation Models","authors_or_org":"Yi He, Zhengkang Guan, Anpeng Wu, Peng Cui, Fei Wu, Kun Kuang","url":"https://arxiv.org/abs/2608.06137","memory":"Top 5 paper. Covered Aug 7 2026 arXiv cs.LG paper on training-free adaptation of tabular foundation models via verifiable skill bank, boundary evidence identification, and gated skill evolution. Suppress future arXiv/code/venue/social reposts unless the skill-bank system, benchmark scope, or evidence materially changes."}
{"date_delivered":"2026-08-07","type":"paper","title":"Matrix Zonotopic Attention: A Context-Adaptive Value Projection for Set Transformers","authors_or_org":"Zhen Zhang, Amr Alanwar","url":"https://arxiv.org/abs/2608.05472","memory":"Top 5 paper. Covered context-adaptive value projections for set transformers, Transformation Degrees of Freedom, depth-separation claim, and matrix-zonotope attention. Suppress future versions unless theory or experiments materially expand."}
{"date_delivered":"2026-08-07","type":"paper","title":"The Loss Does Not See the Basis, but Adam Does","authors_or_org":"Devender Singh","url":"https://arxiv.org/abs/2608.05136","memory":"Top 5 paper. Covered optimizer implicit bias through gauge symmetry in factored models, Adam/RMSProp basis dependence, equivariant optimizer structure theorem, matrix-sensing and transformer diagnostics. Suppress reposts unless theory or experiments materially change."}
{"date_delivered":"2026-08-07","type":"paper","title":"Hypothesis Testing with Conditional Queries: Learnability and the Value of Interaction","authors_or_org":"Zonghuan Xu","url":"https://arxiv.org/abs/2608.06262","memory":"Top 5 paper. Covered conditional-query hypothesis testing, learnability via pairwise conditional-probability separation, exact 1/2 error when separation vanishes, and quadratic adaptivity gap. Suppress future arXiv/venue versions unless results materially change."}
{"date_delivered":"2026-08-07","type":"paper","title":"Tytan: Interactive Neurosymbolic Construction of Analytic Semantic Schemas from Relational Data","authors_or_org":"Donna Hooshmand, Shubham Shahi, Cameron Barrie, Abhratanu Dutta, Marko Sterbentz, Harper Pack, Kristian J. Hammond","url":"https://arxiv.org/abs/2608.06331","memory":"Top 5 paper. Covered TYTAN neurosymbolic system for constructing analytic semantic schemas from relational data using symbolic database analysis, LLM semantic inference, and targeted user questions. Suppress future arXiv/code/venue mentions unless system or artifact materially expands."}
{"date_delivered":"2026-08-07","type":"proceedings","title":"arXiv cs.LG/stat.ML new-submission stream for August 7 2026","authors_or_org":"arXiv cs.LG and stat.ML","url":"https://arxiv.org/list/cs.LG/new","memory":"Venue Watch. Covered Aug 7 2026 arXiv cs.LG/stat.ML streams: 74 new cs.LG submissions out of 260 total entries and 9 new stat.ML submissions out of 39 total entries; themes included TFM adaptation, set attention, optimizer implicit bias, conditional-query testing, uncertainty, agent training, and representation evaluation. Suppress repeat broad daily stream summary."}
{"date_delivered":"2026-08-07","type":"proceedings","title":"arXiv cs.DB new-submission stream for August 7 2026","authors_or_org":"arXiv cs.DB","url":"https://arxiv.org/list/cs.DB/new","memory":"Venue Watch. Covered Aug 7 2026 cs.DB stream: semantic isolation for durable AI workflows, filtered vector search in lakehouses, window-function optimization, priority-aware database load balancing, TYTAN semantic schemas, and synthetic clinical benchmark realism. Suppress repeat daily cs.DB stream summary."}
{"date_delivered":"2026-08-07","type":"proceedings","title":"TMLR August 2026 accepted papers incremental update as of August 7","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered visible August 2026 TMLR accepted-paper stream as of Aug 7, including SAFT, minimax classifier rates, RLHF human-influence, natural actor-critic, Transformer-SSM hybrids, representational consistency, instance-level generation, structured set utility, Survey-certified agent memory, vector information capacity, GenAI footprint, and inference-time computation benchmark. Suppress this incremental snapshot."}
{"date_delivered":"2026-08-07","type":"paper","title":"BEGIN AI TRANSACTION: Semantic Isolation for Durable AI Workflows","authors_or_org":"Barzan Mozafari","url":"https://arxiv.org/abs/2608.05412","memory":"Worth Watching. Covered semantic isolation for durable AI workflows, including semantic read skew, compatibility skew, context escape, merge skew, isolation levels, and SemIso middleware. Suppress future arXiv/repost mentions unless prototype, formal model, or adoption materially changes."}
{"date_delivered":"2026-08-07","type":"benchmark","title":"PoolBench: A Benchmark for Pooling Strategies in Concept Representation Evaluation for Decoder-Only LLMs","authors_or_org":"Ayushi Agarwal","url":"https://arxiv.org/abs/2608.05162","memory":"Worth Watching. Covered PoolBench protocol for pooling strategies in decoder-only LLM concept representations, including corpus, activations, scorer models, steering vectors, and finding that detection strength does not imply steering strength. Suppress future benchmark/repo/repost mentions unless artifact materially expands."}
{"date_delivered":"2026-08-07","type":"paper","title":"Filtered Vector Search in a Disaggregated Lakehouse: Composing Table-Format Pruning with Per-File ANN","authors_or_org":"Rakesh Jain, Thomas Griffin, Syed Zawad; IBM Research","url":"https://arxiv.org/abs/2608.05441","memory":"Worth Watching. Covered per-file IVF indexes embedded in Parquet footers and composed with Iceberg/table-format pruning for filtered vector search over lakehouse data. Suppress future arXiv/venue/code mentions unless system or evaluation materially changes."}
{"date_delivered":"2026-08-07","type":"benchmark","title":"RENDEQ / REND-EQUIV figure-reading reliability resources","authors_or_org":"Rasul Khanbayov, Hasan Kurban","url":"https://arxiv.org/abs/2608.05670","memory":"Worth Watching. Covered paired figure re-rendering and equivariance/consistency resources for measuring when agreement tracks correctness and when label-free reliability has computable blind spots. Suppress future mentions of RENDEQ, REND-EQUIV, or same underlying figure-reading reliability artifacts unless materially expanded."}
{"date_delivered":"2026-08-07","type":"dataset","title":"THBKG: A Temporal Biomedical Knowledge Graph for Decision-Aligned Clinical Advancement Prediction","authors_or_org":"Pui Chung Siu, Claudia Cabrera, Mani Mudaliar, Arkaitz Zubiaga","url":"https://arxiv.org/abs/2608.05982","memory":"Worth Watching. Covered temporal biomedical KG with 110,396 entities and 11.1M time-stamped edges for decision-aligned target-disease Phase II to Phase III advancement prediction. Suppress future arXiv/project mentions unless dataset or benchmark materially changes."}
```