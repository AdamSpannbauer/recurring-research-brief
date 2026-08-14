## Section 1: Top 5 Papers

1. **Interpretable Causal Discovery via Causal-Effect Constraints**  
   **Authors:** Cixuan Zhang, Guy Van den Broeck, Benjie Wang  
   **Venue/source:** arXiv; accepted by UAI 2026  
   **Date:** submitted August 12, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2608.12640))  
   This is the strongest causal paper in the fresh set. Instead of treating causal discovery as “find the DAG,” it asks for a posterior over graphs and parameters *conditional on an explanatory event*—for example, a large causal effect. The technical move is to import rare-event estimation into Bayesian causal discovery, gradually steering particles toward graph/parameter regions satisfying the causal-effect constraint while retaining a usable approximation to the conditional posterior. The Sachs protein case study is exactly the right kind of example: pathway-level causal summaries rather than another edge-F1 leaderboard.  
   **Why you should care:** It reframes causal discovery around explanation-targeted posterior conditioning, which is closer to how scientists actually use causal graphs.

2. **Incremental Evaluation and Training in Relational Deep Learning**  
   **Authors:** Jakub Peleška, Gustav Šír  
   **Venue/source:** arXiv; cs.LG/cs.DB  
   **Date:** submitted August 13, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2608.13023))  
   Relational Deep Learning treats multi-table databases as temporal heterogeneous graphs, but most evaluations still freeze them into one static snapshot. This paper argues that this is the wrong unit of evaluation: real relational databases evolve, concept drift appears, and models need to adapt over episodes. The authors introduce an incremental, multi-episode evaluation and training paradigm, show that concept drift occurs in most predictive tasks they examine, and report that incremental fine-tuning can beat expensive from-scratch retraining. The contribution is partly methodological, but important: RDL and relational foundation models need temporal benchmarks, not only schema benchmarks.  
   **Why you should care:** It pushes relational/tabular foundation-model evaluation toward realistic database lifecycle behavior.

3. **Black-Box Knowledge Transfer across Distinct Feature Sets**  
   **Authors:** Oh-Ran Kwon, Daeyoung Ham  
   **Venue/source:** arXiv; stat.ML  
   **Date:** submitted August 10, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2608.12403))  
   This paper studies a common but under-theorized deployment problem: you have a strong black-box predictor trained on one feature space, but your target setting has different features. The proposed method decomposes the target regression function into a transferable component, informed through abundant unlabeled bridge pairs, and a non-transferable component learned from scarce target labels. The authors give risk bounds showing when black-box transfer improves over learning from labels alone, and extend the framework to multiple source black boxes. This is relevant to model reuse, data integration, and tabular/enterprise ML where feature schemas rarely align cleanly.  
   **Why you should care:** It gives a statistical foundation for reusing predictive systems across heterogeneous schemas without opening the black box.

4. **Balanced Adaptive Prototype Selection for Scalable TabPFN Inference on Large-Scale Tabular Data**  
   **Authors:** Mahboobe Jadid, Melika Rezaye Garkani, Ali Mousavi  
   **Venue/source:** arXiv  
   **Date:** submitted August 13, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2608.12989))  
   This is a practical paper, but it targets a central bottleneck for in-context tabular foundation models: context length. BAPS constructs a compact set of prototypes for TabPFN inference while preserving representative structure, decision-boundary information, local density, class balance, and feature diversity. On HIGGS and SUSY, the authors report that 512 prototypes can represent million-row datasets with strong performance and calibration, corresponding to roughly 1,953× context compression, even on CPU-only hardware. The key question is whether these heuristics hold beyond two large binary datasets, but the problem is exactly right.  
   **Why you should care:** Context construction is becoming the hidden systems layer of tabular foundation-model deployment.

5. **Training Under Challenge: Executable Certificates and Challenge-Closed Optimality for Neural Networks**  
   **Authors:** Farhang Yeganegi, Arian Eamaz, Mojtaba Soltanalian  
   **Venue/source:** arXiv  
   **Date:** submitted August 12, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2608.12655))  
   This paper proposes executable certificates for neural-network training outcomes. A “challenge” is a predeclared architecture-valid procedure that constructs an alternative model in the same certified class and reevaluates the objective; if the alternative is better, it witnesses an empirical optimality gap. The paper introduces a challenge-power modulus, gives coverage-based results for squared loss, and uses certificates to distinguish decoder under-use from representation insufficiency. It is long and likely uneven, but the idea is notable: replace vague convergence stories with replayable, scope-limited falsification of training optimality.  
   **Why you should care:** It is a useful lens for diagnosing representation limits versus optimizer/training failure.

## Section 2: Venue Watch

- **arXiv ML/stat/DB stream for August 14, 2026.** The cs.LG new-submission page lists 92 new submissions out of 268 total entries; stat.ML lists 8 new submissions out of 51 total entries; cs.DB lists 8 new submissions out of 15 total entries. The strongest clusters are: tabular/RDL scaling, causal discovery and counterfactual evaluation, agentic research systems, representation diagnostics, memory systems for agents, and correctness-oriented data engineering. The stream is unusually aligned with Adam’s interests: several papers treat structured data not as a benchmark format but as a live system with evolving schemas, long-term memory, temporal drift, and executable semantics. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **TMLR August 2026 accepted-paper stream, incremental update.** The TMLR page now shows a substantial August batch beyond the items already covered earlier this week. Newly visible or still-noteworthy items include *Weaves, Wires, and Morphisms* on algebraic formalization of deep learning, *Generative Modeling with Bayesian Sample Inference*, *The Intrinsic Dimension of Prompts in Internal Representations of LLMs*, *Variational Set Operator Networks*, *Few Contrastive Attention Heads Enable Visual Grounding* with J2C certification, *Online Learning and Unlearning*, *Invariant Causal Set Covering Machine*, *Learning with Local Search MCMC Layers* with Featured/J2C certification, and *Lost in Aggregation* on message-passing GNN expressivity. This month’s TMLR stream is heavy on representation formalism, uncertainty/meta-learning, agent/LLM evaluation, causal invariance, and learning/unlearning theory. ([jmlr.org](https://jmlr.org/tmlr/papers/))

- **Database/data-systems watch: agent memory and pipeline correctness.** The cs.DB August 14 stream is small but thematically coherent. *StreamReason-Bench* probes whether LLMs understand event-time stream-processing semantics, with poor exact-match performance on out-of-order/late-data cases. *FluctlightDB* proposes long-term agent memory as a distinct embedded data model with write/read semantics and released artifacts. *Pipeline Denotational Design* argues for grain-correct-by-construction data pipelines, motivated by AI-generated pipeline code and silent aggregate inflation. These are not all mature systems papers, but they indicate a shift from “LLM over databases” to database abstractions designed for agents, provenance, and correctness. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

## Section 3: Emerging Trends

- **Structured-data foundation models are moving from accuracy to lifecycle constraints.** The fresh RDL and TabPFN prototype-selection papers focus on evolving databases, context compression, and deployment cost—not just benchmark wins.

- **Causal ML is becoming query-conditional.** Recent causal work is converging on “given a scientific or operational question, condition inference around the relevant causal event,” rather than producing a generic graph or effect estimate.

- **Representation evaluation is getting measurement-theoretic.** Papers on training certificates, prompt-internal dimension, probe fragility, and concept geometry are increasingly asking whether our diagnostic instruments measure stable properties or artifacts of prompt/design choices.

- **Agentic data systems need first-class semantics.** Stream-processing semantics, memory models, and correct-by-construction pipelines are recurring in DB-adjacent work; the data-management community is beginning to define what agents are allowed to remember, query, and certify.

- **Benchmarking is shifting toward hidden operational failure modes.** Event-time reasoning, synthetic medical-data fidelity, offline top-k allocation, and replication agents all evaluate failures that ordinary aggregate scores obscure.

## Section 4: Worth Watching

- **Training AI Scientists to Replicate Research** — Damon Falck et al. introduce Replica, a scalable task space for paper replication, and post-train a 27B “AI Scientist” agent claimed to outperform Claude Opus 4.8 and GPT-5.5 on held-out replication tasks. Worth tracking less for the headline model claim than for the replication-task environment and rubric-based judge. ([arxiv.org](https://arxiv.org/abs/2608.13331))

- **StreamReason-Bench** — Zhuoxi Wang’s benchmark asks LLMs to reason exactly about event-time stream-processing semantics, including watermarks, late data, tumbling/hopping/session windows, and aggregate firing. This is a clean data-systems benchmark for tool-using agents that claim to write or debug streaming pipelines. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

- **FluctlightDB** — Ganesh S proposes an embedded long-term memory engine for agents, with `experience()`/`activate()`-style semantics, provenance-aware linked memory, and released frozen benchmark artifacts. Treat claims cautiously, but suppress future repeats unless the engine gains adoption or a stronger evaluation. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

- **CoMedBench** — Akanta Das et al. introduce a multi-source benchmark for synthetic medical data fidelity and downstream utility across static tabular and temporal clinical tasks. This is relevant to synthetic-data evaluation design even if the first version is domain-specific. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **Pipeline Denotational Design** — Nikos Karayannidis’s PDD proposal is an early but useful artifact for agent-generated data pipelines: verify grain and behavioral correctness at design time, leaving only input-boundary/data-quality checks for runtime. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

## Section 5: Discord Highlights

**Aug 14 — Research brief highlights**

Top papers:
1. **Interpretable Causal Discovery via Causal-Effect Constraints** — Bayesian causal discovery conditioned on explanatory effect events.
2. **Incremental Evaluation and Training in Relational Deep Learning** — evaluates relational models as evolving databases, not frozen snapshots.
3. **Black-Box Knowledge Transfer across Distinct Feature Sets** — statistical transfer from black-box predictors across heterogeneous schemas.
4. **Balanced Adaptive Prototype Selection for Scalable TabPFN Inference** — compresses million-row TabPFN contexts into small prototype sets.
5. **Training Under Challenge** — executable certificates for diagnosing training optimality and representation insufficiency.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-08-14","type":"paper","title":"Interpretable Causal Discovery via Causal-Effect Constraints","authors_or_org":"Cixuan Zhang, Guy Van den Broeck, Benjie Wang","url":"https://arxiv.org/abs/2608.12640","memory":"Top 5 paper. Covered Aug 12 2026 arXiv / UAI 2026 paper on conditional Bayesian causal discovery under causal-effect constraints using rare-event estimation over graph-parameter space; Sachs protein pathway summaries. Suppress arXiv/UAI/code/repost versions unless method or empirical scope materially changes."}
{"date_delivered":"2026-08-14","type":"paper","title":"Incremental Evaluation and Training in Relational Deep Learning","authors_or_org":"Jakub Peleška, Gustav Šír","url":"https://arxiv.org/abs/2608.13023","memory":"Top 5 paper and cs.DB/cs.LG Venue Watch item. Covered Aug 13 2026 arXiv paper proposing incremental multi-episode evaluation and training for relational deep learning on evolving multi-table databases, concept drift, temporal metrics, and incremental fine-tuning. Suppress future arXiv/venue/code mentions unless benchmark or results materially expand."}
{"date_delivered":"2026-08-14","type":"paper","title":"Black-Box Knowledge Transfer across Distinct Feature Sets","authors_or_org":"Oh-Ran Kwon, Daeyoung Ham","url":"https://arxiv.org/abs/2608.12403","memory":"Top 5 paper. Covered Aug 10 2026 stat.ML arXiv paper on transferring predictive knowledge from black-box models across heterogeneous feature spaces using unlabeled bridge pairs, transferable/non-transferable decomposition, and risk bounds. Suppress future versions unless theory or applications materially change."}
{"date_delivered":"2026-08-14","type":"paper","title":"Balanced Adaptive Prototype Selection for Scalable TabPFN Inference on Large-Scale Tabular Data","authors_or_org":"Mahboobe Jadid, Melika Rezaye Garkani, Ali Mousavi","url":"https://arxiv.org/abs/2608.12989","memory":"Top 5 paper. Covered BAPS for constructing compact information-preserving contexts for TabPFN inference on million-row HIGGS/SUSY, with 512 prototypes and reported 1953x context compression. Suppress arXiv/code/repost versions unless benchmark scope or method materially expands."}
{"date_delivered":"2026-08-14","type":"paper","title":"Training Under Challenge: Executable Certificates and Challenge-Closed Optimality for Neural Networks","authors_or_org":"Farhang Yeganegi, Arian Eamaz, Mojtaba Soltanalian","url":"https://arxiv.org/abs/2608.12655","memory":"Top 5 paper. Covered executable challenge certificates for neural-network empirical optimality gaps, challenge-power modulus, coverage-based squared-loss results, and representation insufficiency vs decoder under-use diagnostics. Suppress arXiv/ancillary/venue reposts unless certification framework materially changes."}
{"date_delivered":"2026-08-14","type":"proceedings","title":"arXiv cs.LG/stat.ML/cs.DB new-submission stream for August 14 2026","authors_or_org":"arXiv cs.LG, stat.ML, cs.DB","url":"https://arxiv.org/list/cs.LG/new","memory":"Venue Watch. Covered Aug 14 2026 arXiv streams: 92 new cs.LG submissions out of 268 entries, 8 new stat.ML submissions out of 51 entries, and 8 new cs.DB submissions out of 15 entries; themes in tabular/RDL scaling, causal discovery, agentic research, representation diagnostics, agent memory, and data-pipeline correctness. Suppress repeat broad daily stream summary."}
{"date_delivered":"2026-08-14","type":"proceedings","title":"TMLR August 2026 accepted papers incremental update as of August 14","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered visible Aug 14 TMLR August 2026 additions and themes including Weaves/Wires/Morphisms, Generative Modeling with Bayesian Sample Inference, prompt intrinsic dimension, Behavioral Data Representation Learning survey, Variational Set Operator Networks, Few Contrastive Attention Heads with J2C, Online Learning and Unlearning, Invariant Causal Set Covering Machine, Learning with Local Search MCMC Layers Featured/J2C, and Lost in Aggregation. Suppress this incremental snapshot."}
{"date_delivered":"2026-08-14","type":"benchmark","title":"StreamReason-Bench: Can Large Language Models Reason about Event-Time Stream-Processing Semantics?","authors_or_org":"Zhuoxi Wang","url":"https://arxiv.org/abs/2608.12348","memory":"Worth Watching and cs.DB Venue Watch. Covered benchmark of 600 generated event-time stream-processing items over tumbling, hopping, session, and processing-time windows, testing LLM reasoning about watermarks, late events, window firing, and aggregates. Suppress future arXiv/repo/repost mentions unless benchmark materially expands."}
{"date_delivered":"2026-08-14","type":"software","title":"FluctlightDB: A Memory Model of Data for AI Agents","authors_or_org":"Ganesh S","url":"https://arxiv.org/abs/2608.12365","memory":"Worth Watching and cs.DB Venue Watch. Covered embedded long-term agent-memory engine with experience/activate semantics, provenance-weighted linked recall, CHORUS/PRISM evaluation claims, MIT-licensed harnesses and frozen benchmark artifacts. Suppress future arXiv/repo/tool mentions unless adoption, artifact, or evaluation materially changes."}
{"date_delivered":"2026-08-14","type":"benchmark","title":"CoMedBench: A Multi-Source Benchmark of Synthetic Medical Data Fidelity and Downstream Utility","authors_or_org":"Akanta Das, Al Amin Farhad, Mrinmoy Sarkar Anto, David Rehkopf, Ayin Vala, Tanmoy Sarkar Pias","url":"https://arxiv.org/abs/2608.12805","memory":"Worth Watching. Covered benchmark for evaluating synthetic medical data fidelity and downstream utility across static tabular and temporal critical-care tasks. Suppress future arXiv/repo/repost mentions unless benchmark or generator suite materially expands."}
{"date_delivered":"2026-08-14","type":"resource","title":"Pipeline Denotational Design: Correct-by-Construction Data Pipelines at Zero Cost","authors_or_org":"Nikos Karayannidis","url":"https://arxiv.org/abs/2608.12375","memory":"Worth Watching and cs.DB Venue Watch. Covered design-first methodology for grain-correct-by-construction data pipelines using typed pipeline design algebra, proof-carrying composition, and SQL/PySpark boundary checks, motivated by AI-generated pipeline verification. Suppress future versions unless formal system or evaluation materially changes."}
{"date_delivered":"2026-08-14","type":"paper","title":"Training AI Scientists to Replicate Research","authors_or_org":"Damon Falck, Samer Sabri, Anja Surina, Thom Foster, Anya Sims, Sam Devlin, Dylan Rogers, Tantum Collins, Kaloyan Aleksiev, Louis Kirsch, Edward Hughes","url":"https://arxiv.org/abs/2608.13331","memory":"Worth Watching. Covered Replica task space for paper replication, rubric-based judge, and Faraday 27B AI Scientist agent claims. Suppress future arXiv/project/social mentions unless benchmark/artifact/model or results materially expand."}
```