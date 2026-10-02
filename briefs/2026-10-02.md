## Section 1: Top 5 Papers

1. **STEER: Reducing Inference Cost in Relational Foundation Models through Semantically Informed Sampling**  
   **Authors:** Abdalla Mohamed, Ashraf Aboulnaga  
   **Venue/source:** arXiv cs.DB/cs.LG  
   **Release date:** October 1, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2610.00907))  
   **Summary:** STEER attacks a practical bottleneck in relational foundation models: inference contexts are built by traversing foreign-key neighborhoods, so cost grows with sampled relational context. Instead of dropping rows blindly, STEER asks an LLM to rank schema foreign-key edges by task relevance, converts those tiers into traversal probabilities, and reuses the schema-level ranking across predictions. Evaluated on RT, RT-J, and Griffin, it reports roughly 40% average context-size reduction while preserving or improving accuracy. This is exactly the kind of systems-method interface that relational FMs need: inference-time structure selection without retraining the model.  
   **Why you should care:** Relational FMs are moving from benchmark novelty to deployment bottlenecks; schema-aware context selection may become the relational analogue of retrieval optimization for RAG.

2. **The hidden advantage of mask resampling: a theory of masked autoencoders**  
   **Authors:** Jorge Medina Moreira, Lorenzo Bardone, Lenka Zdeborová  
   **Venue/source:** arXiv stat.ML/cs.LG  
   **Release date:** October 1, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2610.01578))  
   **Summary:** This paper gives a clean high-dimensional theory for why masked prediction can recover latent structure when unmasked reconstruction—essentially PCA in their linear setting—fails. The key new point is mask diversity: using multiple masks per sample can lower sample complexity, but standard image augmentations can obscure this effect by renewing the task even under fixed masks. The authors connect theory to experiments in CNN/ViT autoencoders and a BERT pilot. It is valuable because it separates “masked objective” from “mask resampling,” a design knob often treated as implementation detail rather than statistical signal.  
   **Why you should care:** This is a rare SSL theory result that directly suggests pretraining-protocol experiments, including for tabular or structured masking.

3. **Transferable Graph Metanetworks**  
   **Authors:** Yuxin Ma, Adir Dayan, Yam Eitan, Haggai Maron, Soledad Villar  
   **Venue/source:** arXiv stat.ML/cs.LG  
   **Release date:** September 30, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2610.00420))  
   **Summary:** Weight-space networks promise to predict properties of neural networks from their parameters, but size generalization has been weak. This paper proposes graph metanetwork modifications aimed at width transfer, using invariance to different width-dependent representations of the same function and continuity in function space. Empirically, the approach transfers up to 42× the training width for networks trained under μP, and the authors back this with infinite-width limit theory explaining when transfer should or should not work. It is interesting for model-analysis, weight-space representation learning, and eventual “foundation models over models.”  
   **Why you should care:** If weight-space models are to audit, compress, route, or predict behavior of future models, width transfer is a make-or-break property.

4. **Are We Recovering Mechanisms? Objective-Level Recovery Gaps in Mechanistic Interpretability**  
   **Authors:** Chuqin Geng, Li Zhang, Haolin Ye, Mark Zhang, Luke Zhang, Xujie Si  
   **Venue/source:** arXiv cs.LG  
   **Release date:** October 1, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2610.02098))  
   **Summary:** The paper argues that circuit-discovery failures are not only search failures: the objective itself can prefer circuits that are less behaviorally faithful. Across four human-reference tasks and InterpBench, intervention-defined faithfulness metrics misrank candidate circuits under ordinary resampling; KL misranks 9.4%–41.2% of candidate pairs for several methods. The proposed diagnosis is context distortion: excluded signals alter the inputs seen by retained components. Restoring selected recipient-side signals repairs most persistent misrankings. The contribution is methodological, but important: better attribution algorithms may not help if the validation objective rewards the wrong intervention.  
   **Why you should care:** It raises the bar for mechanistic-interpretability benchmarks by making objective design, not just circuit search, the failure mode.

5. **TabJoinBench: A Benchmark for Joinable Table Discovery**  
   **Authors:** Sandipan De, Jin Wang, Vivek Gupta  
   **Venue/source:** arXiv cs.DB/cs.AI/cs.CL/cs.IR  
   **Release date:** September 30, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2610.00817))  
   **Summary:** Join discovery is central to data lakes, feature augmentation, and BI agents, but evaluations have been fragmented and method-specific. TabJoinBench builds query-candidate pairs across semantic, relational, and hybrid data-lake scenarios, introduces controlled structural/representation/semantic perturbations, and releases processed datasets, ground truth, and generation pipeline. It evaluates set-based, feature-based, learned, and general-purpose LM embedding baselines. The value is not a new model but a reusable stress test for whether table discovery systems survive realistic schema and semantic drift.  
   **Why you should care:** This is likely to become a suppress-and-track benchmark for data integration, table retrieval, and agentic BI systems.

## Section 2: Venue Watch

**TMLR October 2026 opening batch.** The first visible October TMLR items include multi-agent prompt optimization, geometry-aware MCTS for combinatorial geometry with J2C certification, forward target propagation, memory-augmented attention, positional realizability for length generalization, adaptive denoising diffusions, frozen-LLM controllable generation, temporal counterfactual estimation with SSL, orthogonal LoRA for retrieval, and multi-marginal Schrödinger bridge matching. The batch is broad but has a clear thread: credit assignment, search/planning, diffusion/transport theory, and representation/control mechanisms for LLM-era systems. COSTAR is especially relevant to temporal causal estimation; Multi-Marginal Schrödinger Bridge Matching is worth tracking for generative modeling and simulation-based inference. ([jmlr.org](https://jmlr.org/tmlr/papers/))

**Operations Research, Volume 74 Issue 5, September–October 2026.** This new issue is broad operations-methodology rather than ML-centric, but several themes are adjacent: online mirror descent for multiproduct inventory, learning in Stackelberg games with non-myopic agents, sequential price competition, data-driven piecewise affine decision rules with covariates, sparse PCA, factored MDP solution schemes, online fair allocation, and nested CoVaR estimation. The issue is a useful reminder that online learning, contextual stochastic programming, strategic learning, and fairness/resource-allocation methods are continuing to develop outside mainstream ML venues. ([pubsonline.informs.org](https://pubsonline.informs.org/toc/opre/current))

**October 2 arXiv database / structured-data stream.** The cs.DB stream is unusually aligned with Adam’s interests: TabJoinBench and JoinGR attack table discovery/retrieval; STEER and DIADA target relational-FM context and data-lake composition; JEVDB proposes typed decision models plus selective LLM escalation for semantic query processing; HakiCC uses LLM agents to design and verify concurrency-control protocols; BudgetSchemaBench focuses on schema-context budgets for Text-to-SQL. This is another signal that DB research is converging on “semantic operators + structured context + verification/cost control” rather than generic agent wrappers. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

## Section 3: Emerging Trends

- **Structured-data foundation models are hitting systems constraints.** The last few days added TabPFN-3.5, Causilo, RefineICL, QUARTET, STEER, and attention/context-compression papers; the frontier is shifting from “can it work?” to “how do we fit, sample, cache, and route the right structured context?”

- **Benchmarks are moving from static prediction to data work.** TabJoinBench, BI-Bench, SQL/AI-operator evaluation, Text-to-SQL schema-budget diagnostics, and table-retrieval work all test components of an end-to-end data workflow rather than a single supervised task.

- **SSL theory is getting more operational.** Recent work on semantic recoverability, masked-pretraining theory, and now mask-resampling advantage is starting to identify which design choices preserve downstream information rather than merely improve proxy loss.

- **Interpretability evaluation is under pressure.** The recovery-gap paper, recent SAE phase-diagram work, ObserverBench, and circuit-granularity papers all point to the same issue: interpretability claims depend heavily on evaluation objectives and intervention semantics.

- **Database systems are becoming semantic-execution systems.** JEVDB, KathDB-FAO, Concord, AI query compilation, semantic-operator compilation, and JEVDB-like selective escalation suggest a more mature architecture: typed cheap models for most rows/pairs, LLMs only for uncertainty or synthesis.

## Section 4: Worth Watching

- **HakiCC: LLM-Driven Multi-Agent Design and Optimization of Concurrency Control Protocols.** Worth tracking as an ambitious example of LLM agents generating, repairing, verifying, and workload-optimizing core database protocols; all reported generated protocols are conflict-serializable, with large throughput gains after optimization. ([arxiv.org](https://arxiv.org/abs/2610.00889))

- **DIADA: Automatic Data Composition in Data Lakes.** A task-agnostic data-lake composition system using multivariate dependence over predicate-set lattices to group scattered attributes into meaningful relations; potentially complementary to join discovery and feature-discovery systems. ([arxiv.org](https://arxiv.org/abs/2610.01646))

- **JEVDB: Prune First, Decide Fast.** A semantic database architecture that combines relational semijoin reduction, Semantic Bloom Filters, typed decision models, and selective LLM escalation; the released simulator/code/benchmarks could be influential for semantic operator systems. ([arxiv.org](https://arxiv.org/abs/2610.02046))

- **JoinGR: Learning to Traverse Join Graphs for Table Retrieval.** A join-graph traversal method for retrieving tables not mentioned in the question but required by foreign-key paths; especially relevant to enterprise Text-to-SQL and BI agents. ([arxiv.org](https://arxiv.org/abs/2610.01064))

- **Nous: Learning and Certifying Memory Decisions Before Source Calibration.** A statistical framework for agent memory showing useful decisions can be learned and certified before full source calibration, with finite-sample policy-improvement receipts and MiniGrid memory tests. ([arxiv.org](https://arxiv.org/abs/2610.00094))

- **Learning Commute-Time-Preserving World Models for Planning.** CTWM gives a self-supervised route to latent distances that preserve graph commute times, with a log-determinant anti-collapse regularizer and theory under reversible deterministic dynamics. ([arxiv.org](https://arxiv.org/abs/2610.01373))

## Section 5: Discord Highlights

**Oct 2 research brief**

Top papers:
1. **STEER: Reducing Inference Cost in Relational Foundation Models through Semantically Informed Sampling** — schema-aware sampling cuts relational-FM context cost.
2. **The hidden advantage of mask resampling** — theory shows mask diversity can lower SSL sample complexity.
3. **Transferable Graph Metanetworks** — weight-space networks that transfer across model widths, especially under μP.
4. **Are We Recovering Mechanisms?** — circuit objectives can prefer worse mechanisms before search even begins.
5. **TabJoinBench** — reproducible benchmark for joinable-table discovery across semantic/relational/hybrid lakes.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-10-02","type":"paper","title":"STEER: Reducing Inference Cost in Relational Foundation Models through Semantically Informed Sampling","authors_or_org":"Abdalla Mohamed, Ashraf Aboulnaga","url":"https://arxiv.org/abs/2610.00907","memory":"Top 5 paper. Covered schema-aware sampling for relational foundation models using LLM-ranked foreign-key edges to reduce context size about 40% across RT, RT-J, and Griffin while preserving/improving accuracy. Suppress arXiv/code/venue/social reposts unless method or evaluation materially changes."}
{"date_delivered":"2026-10-02","type":"paper","title":"The hidden advantage of mask resampling: a theory of masked autoencoders","authors_or_org":"Jorge Medina Moreira, Lorenzo Bardone, Lenka Zdeborová","url":"https://arxiv.org/abs/2610.01578","memory":"Top 5 paper. Covered high-dimensional theory showing masked linear reconstruction can recover latent features when unmasked/PCA fails, and mask resampling/diversity can reduce sample complexity; includes CNN/ViT and BERT pilots. Suppress future versions unless theory or experiments materially expand."}
{"date_delivered":"2026-10-02","type":"paper","title":"Transferable Graph Metanetworks","authors_or_org":"Yuxin Ma, Adir Dayan, Yam Eitan, Haggai Maron, Soledad Villar","url":"https://arxiv.org/abs/2610.00420","memory":"Top 5 paper. Covered graph metanetworks over neural-network weights with width-transfer modifications, μP-dependent 42x width generalization, and infinite-width theory. Suppress arXiv/code/venue reposts unless weight-space transfer theory or evidence materially changes."}
{"date_delivered":"2026-10-02","type":"paper","title":"Are We Recovering Mechanisms? Objective-Level Recovery Gaps in Mechanistic Interpretability","authors_or_org":"Chuqin Geng, Li Zhang, Haolin Ye, Mark Zhang, Luke Zhang, Xujie Si","url":"https://arxiv.org/abs/2610.02098","memory":"Top 5 paper. Covered objective-level recovery gaps in mechanistic interpretability where intervention faithfulness metrics can misrank circuits; context distortion explanation and recipient-signal restoration repair many KL misrankings. Suppress future arXiv/code/benchmark mentions unless objectives or results materially change."}
{"date_delivered":"2026-10-02","type":"benchmark","title":"TabJoinBench: A Benchmark for Joinable Table Discovery","authors_or_org":"Sandipan De, Jin Wang, Vivek Gupta","url":"https://arxiv.org/abs/2610.00817","memory":"Top 5 benchmark/paper. Covered reproducible benchmark for joinable table discovery across semantic, relational, and hybrid data-lake scenarios with perturbations, ground truth, and generation pipeline. Suppress arXiv/code/dataset/venue reposts unless benchmark materially expands."}
{"date_delivered":"2026-10-02","type":"proceedings","title":"TMLR October 2026 opening accepted-papers batch","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered opening October 2026 TMLR stream: MAPGD, Geometry-Aware MCTS, Forward Target Propagation, MANAR, positional realizability for length generalization, adaptive denoising diffusions, COSTAR, Orthogonal LoRA for retrieval, Multi-Marginal Schrödinger Bridge Matching. Suppress repeat opening-batch summary."}
{"date_delivered":"2026-10-02","type":"venue_issue","title":"Operations Research Volume 74 Issue 5 September-October 2026","authors_or_org":"INFORMS Operations Research","url":"https://pubsonline.informs.org/toc/opre/current","memory":"Venue Watch. Covered Sep-Oct 2026 OR issue themes: multimodularity, online mirror descent inventory, Stackelberg learning, sequential price competition, Whittle scheduling, contextual stochastic programming, sparse PCA, factored MDPs, fair allocation, CoVaR estimation, assortment and online selection. Suppress repeat issue summary."}
{"date_delivered":"2026-10-02","type":"proceedings","title":"arXiv cs.LG/stat.ML/cs.DB new-submission stream for October 2 2026","authors_or_org":"arXiv cs.LG, stat.ML, cs.DB","url":"https://arxiv.org/list/cs.LG/new","memory":"Venue Watch. Covered Oct 2 2026 streams: 270 new cs.LG submissions, 18 stat.ML submissions, and 10 cs.DB submissions; themes in relational FMs, join discovery, semantic DBs, SSL theory, mechanistic interpretability objectives, agent memory, and LLM-designed DB protocols. Suppress repeat daily stream summary."}
{"date_delivered":"2026-10-02","type":"software","title":"HakiCC: LLM-Driven Multi-Agent Design and Optimization of Concurrency Control Protocols","authors_or_org":"Farzad Habibi, Juncheng Fang, Faisal Nawab","url":"https://arxiv.org/abs/2610.00889","memory":"Worth Watching. Covered LLM multi-agent pipeline for generating, repairing, verifying, and optimizing workload-specific concurrency-control protocols with conflict-serializability and throughput gains. Suppress future arXiv/code/venue mentions unless system or evidence materially changes."}
{"date_delivered":"2026-10-02","type":"paper","title":"DIADA: Automatic Data Composition in Data Lakes","authors_or_org":"Marc Maynou, Albert Martin, Sergi Nadal, Anna Queralt, Oscar Romero","url":"https://arxiv.org/abs/2610.01646","memory":"Worth Watching. Covered task-agnostic data-lake composition using multivariate dependence over predicate lattices to form meaningful relations from scattered attributes. Suppress future arXiv/code/venue reposts unless algorithm or evaluation materially changes."}
{"date_delivered":"2026-10-02","type":"software","title":"Prune First, Decide Fast: Scalable Semantic Query Processing with JEVDB","authors_or_org":"Zhengle Wang, Hanxu Yan, Fuheng Zhao, Chunwei Liu","url":"https://arxiv.org/abs/2610.02046","memory":"Worth Watching. Covered semantic database system using typed decision models, Semantic Bloom Filters, semijoin reduction, and selective LLM escalation for semantic filters/joins/classification/ranking. Suppress arXiv/code/benchmark reposts unless system or evaluation materially changes."}
{"date_delivered":"2026-10-02","type":"paper","title":"JoinGR: Learning to Traverse Join Graphs for Table Retrieval","authors_or_org":"Sandipan De, Abhijit Chakraborty, Sambaran Bandyopadhyay, Vivek Gupta","url":"https://arxiv.org/abs/2610.01064","memory":"Worth Watching. Covered join-aware table retrieval for Text-to-SQL using query-conditioned traversal over database join graphs, improving multi-hop table recall on enterprise benchmark BEAVER. Suppress arXiv/code/venue reposts unless method or benchmark materially expands."}
{"date_delivered":"2026-10-02","type":"paper","title":"Nous: Learning and Certifying Memory Decisions Before Source Calibration","authors_or_org":"Pranav Singh","url":"https://arxiv.org/abs/2610.00094","memory":"Worth Watching. Covered statistical framework for learning and certifying agent-memory decisions before full source calibration, with policy-bound receipts and MiniGrid memory experiments. Suppress arXiv/code/repost versions unless certification framework or evidence materially changes."}
{"date_delivered":"2026-10-02","type":"paper","title":"Learning Commute-Time-Preserving World Models for Planning","authors_or_org":"Michael Hauri, Peter Buttaroni, Fabian A. Mikulasch, Friedemann Zenke","url":"https://arxiv.org/abs/2610.01373","memory":"Worth Watching. Covered self-supervised commute-time-preserving latent world models using displacement predictor and log-determinant anti-collapse regularizer, with Laplacian representation theory and planning benchmarks. Suppress future arXiv/code/venue mentions unless selected for Top 5 or materially expanded."}
```