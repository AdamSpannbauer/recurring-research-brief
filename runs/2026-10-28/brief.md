## Section 1: Top 5 Papers

1. **Recall or Relearn? A Mixture of In-Context Experts for Recurring Concept Drift**  
   **Authors:** Zhangkai Wu, Xu Zhang, Zhihong Cui, Yiqi Wang, Yi Zhang  
   **Venue/source/date:** arXiv, listed 2026-10-28. **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   This is the most directly useful new tabular-foundation-model paper in today’s stream. It studies TFMs in streaming settings where concepts disappear from the context window and later recur. The proposed **MICE** method segments streams at detected changes, stores closed segments as in-context “experts,” and chooses between recalling prior contexts and relearning from fresh labels. The paper gives regret-style guarantees and a useful empirical lesson: learning curves measured in advance can predict when recall will beat relearning.  
   **Why you should care:** It treats TFM context as a managed memory system, not just a prompt, which is likely to matter for real deployments.

2. **GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting**  
   **Authors:** Joseph Natter, Long Vu, Yifan Zhang, Bobin Deng, Kun Suo, Rui Wu  
   **Venue/source/date:** arXiv, listed 2026-10-28. **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   GAS-PFN extends the PFN idea from tabular priors into graph-coupled spatiotemporal forecasting. The model’s synthetic prior samples road topology via random-walk diffusion, and its inference architecture separates sensor-specific temporal dynamics from neighborhood interactions before integrating them. The result is a zero-shot forecaster that uses target-network structure and recent history without gradient updates, reporting large gains over TimePFN and general-purpose zero-shot forecasters across six traffic benchmarks.  
   **Why you should care:** It is a clean example of “structured PFNs”: synthetic priors plus architecture co-designed around the relational structure of the domain.

3. **LinMix: Data Mixing as Linear Domain Attribution**  
   **Authors:** Hubert Baniecki, Przemyslaw Biecek, Martin Pawelczyk  
   **Venue/source/date:** arXiv / NeurIPS 2026 Workshop on Attributing Model Behavior at Scale, listed 2026-10-28. **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   LinMix reframes pretraining data-mixture search as an experimental-design problem. Instead of random Dirichlet mixtures followed by nonlinear regression, it samples vertices of a capped simplex so that each domain is either absent or at cap, yielding a linear domain-attribution model. The paper proves why Dirichlet designs inflate attribution error and reports proxy-to-large-model gains on OLMo2 and Qwen3.5.  
   **Why you should care:** It is a crisp bridge between data valuation, mixture optimization, and interpretable attribution of pretraining behavior.

4. **Calibrated for Which Policy? Conformal Uncertainty for Fixed World Models Under Intervention**  
   **Authors:** Ayush Mittal, Dhruv Gupta  
   **Venue/source/date:** arXiv, listed 2026-10-28. **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   This paper makes a precise point that should generalize beyond robotics: uncertainty calibration is relative to a deployment law. A fixed world model can lose coverage when the policy changes, even if the transition mechanism is unchanged. The authors use weighted conformal calibration with state-occupancy/action-propensity ratios, bound coverage degradation by ratio-estimation error, and machine-check key identities in Lean. On Franka trajectories, ordinary 90% sets collapse to 55% under strong shift, while learned-ratio calibration restores about 91% coverage.  
   **Why you should care:** It is a useful template for conformal evaluation when agents, policies, or logging distributions change after calibration.

5. **When the Application Layer Is Disposable: Putting Integrity Constraints Back in the Database**  
   **Authors:** Hasara Kalumin, Amol Deshpande  
   **Venue/source/date:** arXiv cs.DB, listed 2026-10-28. **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.DB/new))  
   The paper argues that LLM-generated application code makes durable database-level invariants newly urgent: agents may issue queries and updates directly, while the application layer that once enforced business rules is transient. The proposed **constraint indexes** represent multi-relation constraints as transactional access paths in PostgreSQL, enforcing constraints arising from mapped E/R and property-graph structures at modest overhead. The paper also reports that LLM-driven writers violate unenforced constraints and behave erratically when merely told the constraints.  
   **Why you should care:** It is a concrete systems response to agentic data management: put invariants where generated code cannot forget them.

## Section 2: Venue Watch

- **arXiv ML/stat/DB stream, 2026-10-28.** Today’s cs.LG page shows 149 new submissions out of 437 total entries, stat.ML shows 15 new submissions out of 72, and cs.DB shows three new database submissions out of 11 total entries. The strongest clusters for Adam’s interests are: tabular/structured PFNs, streaming TFM memory, data-mixture attribution, policy-shift conformal calibration, agent execution control, semantic/document-backed databases, vector-search variants, and database-level integrity constraints for LLM/agent writers. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **TMLR October 2026 late-month stream.** The accepted-papers page continues to fill in beyond the October 27 snapshot. Newly visible items worth tracking include **Minerva: Reinforcement Learning with Verifiable Rewards for Cyber Threat Intelligence LLMs**, **Leadership as Coordination Control**, **Cognitive Episodes in LLM Reasoning Traces Enable Interpretable Human Item Difficulty Prediction**, **Prover Agent**, and **Routing Beats Latency**. The broad theme is still evaluation and control of agents/LLMs, with a secondary stream in graph learning, attribution, retrieval, and risk/decision methods. ([jmlr.org](https://jmlr.org/tmlr/papers/))

- **cs.DB: agent-era database semantics are consolidating.** Today’s DB submissions are unusually aligned: one argues for first-class database constraints because generated application layers are disposable; another proposes an **Evolving Universal Relation** for query-first document-backed analytics; a third extends ANN search to line queries where a query specifies an invariant direction rather than a point. Together they point toward databases becoming persistent semantic state, not just storage behind RAG. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

## Section 3: Emerging Trends

- **Context is becoming a managed statistical resource.** MICE, GAS-PFN, TFM context compression/adaptation work from earlier briefings, and today’s policy-calibration paper all treat deployment context as something to store, retrieve, weight, certify, or recalibrate—not merely concatenate.

- **Structured PFNs are spreading beyond classic tabular prediction.** Traffic forecasting, causal perturbation mapping, PDEs, matrix completion, OPE, and transcriptomics all now use variants of “synthetic prior + in-context inference” as an organizing recipe.

- **Agentic systems are pushing database invariants down-stack.** The constraint-index paper, EUR, semantic views, SQL proof systems, and recent agent-transaction work share the same message: when code is generated, durable correctness must live in data systems, typed traces, proofs, or transaction semantics.

- **Data mixture and data provenance are shifting from heuristics to experimental design.** LinMix is part of a broader move from “try mixtures and fit a black box” toward attributable, estimable, and auditable data portfolios.

- **Calibration is increasingly deployment-law-specific.** Conformal and uncertainty methods are now being stress-tested under policy changes, inference-time configuration shifts, sequential model updates, partial verification, and adaptive logging.

## Section 4: Worth Watching

- **TACO-Graph: text-attributed graph construction from tabular data.** It enumerates valid graph constructions from multi-attribute tabular data, scores them on small samples, and learns interpretable decision trees predicting graph-construction quality for GNN and GraphRAG tasks. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **Base Models Can Detect Hidden Intentions that Prompted Classifiers Miss.** Persona-header likelihood evaluation uses base-model likelihoods to decode subliminal signals in outputs that prompted classifiers miss, including cross-family signal persistence. Useful for the growing “subliminal learning / hidden objective” audit line. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **Back to the Future: The Evolving Universal Relation Model.** Query-first document analytics where each query may evolve schema and materialized state, turning messy document corpora into gradually constructed database state. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

- **Pneuma benchmark.** A public commercial-aircraft predictive-maintenance time-series benchmark with more than 920M multivariate time steps, four aircraft types, and nine verified fault scenarios; likely useful for evaluating time-series FMs under realistic imbalance and subtle fault signatures. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **KORA: Deterministic-First Execution Control for AI Workloads.** A pre-inference routing layer that validates deterministic/structured routes before escalating to model calls; notable as another “don’t call the model unless necessary” systems pattern. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

## Section 5: Discord Highlights

**Oct 28 brief — Top 5 papers**

1. **Recall or Relearn? A Mixture of In-Context Experts for Recurring Concept Drift** — manages TFM context as reusable memory for drifting streams.  
2. **GAS-PFN** — graph-aware PFN for zero-shot spatiotemporal forecasting.  
3. **LinMix** — turns data-mixture optimization into linear domain attribution.  
4. **Calibrated for Which Policy?** — conformal world-model calibration under deployment-policy shift.  
5. **When the Application Layer Is Disposable** — database constraint indexes for LLM/agent-era integrity.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-10-28","type":"paper","title":"Recall or Relearn? A Mixture of In-Context Experts for Recurring Concept Drift","authors_or_org":"Zhangkai Wu, Xu Zhang, Zhihong Cui, Yiqi Wang, Yi Zhang","url":"https://arxiv.org/abs/2610.36587","memory":"Top 5 paper. Covered MICE, a training-free mixture of in-context experts for tabular foundation models under recurring concept drift, including segment storage, recall-vs-relearn decision, regret-style guarantees, and web-stream experiments. Suppress future arXiv/code/venue/social reposts unless method or benchmarks materially expand."}
{"date_delivered":"2026-10-28","type":"paper","title":"GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting","authors_or_org":"Joseph Natter, Long Vu, Yifan Zhang, Bobin Deng, Kun Suo, Rui Wu","url":"https://arxiv.org/abs/2610.37609","memory":"Top 5 paper. Covered graph-aware spatiotemporal PFN with random-walk topology synthetic prior, two-pass Transformer inference architecture, and zero-shot traffic forecasting gains. Suppress future arXiv/code/model/venue reposts unless architecture, prior, or evaluation materially changes."}
{"date_delivered":"2026-10-28","type":"paper","title":"LinMix: Data Mixing as Linear Domain Attribution","authors_or_org":"Hubert Baniecki, Przemyslaw Biecek, Martin Pawelczyk","url":"https://arxiv.org/abs/2610.37390","memory":"Top 5 paper. Covered NeurIPS 2026 workshop paper reframing data mixture search as linear domain attribution via capped-simplex vertex sampling, with theory against Dirichlet sampling and OLMo2/Qwen3.5 pretraining experiments. Suppress future arXiv/workshop/code/social repeats unless theory or large-scale evidence materially changes."}
{"date_delivered":"2026-10-28","type":"paper","title":"Calibrated for Which Policy? Conformal Uncertainty for Fixed World Models Under Intervention","authors_or_org":"Ayush Mittal, Dhruv Gupta","url":"https://arxiv.org/abs/2610.35877","memory":"Top 5 paper. Covered weighted conformal calibration for fixed world models under deployment-policy intervention, state-occupancy/action-propensity ratios, Lean formalization, and Franka trajectory coverage recovery. Suppress arXiv/code/venue reposts unless calibration theory or applications materially expand."}
{"date_delivered":"2026-10-28","type":"paper","title":"When the Application Layer Is Disposable: Putting Integrity Constraints Back in the Database","authors_or_org":"Hasara Kalumin, Amol Deshpande","url":"https://arxiv.org/abs/2610.36418","memory":"Top 5 paper and cs.DB item. Covered constraint indexes for multi-relation database invariants in LLM/agent-generated application settings, PostgreSQL prototype, mapped E/R/property-graph constraints, and LLM writer constraint violations. Suppress future arXiv/code/venue reposts unless system or enforcement model materially changes."}
{"date_delivered":"2026-10-28","type":"proceedings","title":"arXiv cs.LG/stat.ML/cs.DB new-submission stream for October 28 2026","authors_or_org":"arXiv cs.LG, stat.ML, cs.DB","url":"https://arxiv.org/list/cs.LG/new","memory":"Venue Watch. Covered Oct 28 2026 streams: cs.LG 149 new submissions out of 437 entries, stat.ML 15 new out of 72, cs.DB 3 new out of 11. Themes included TFM context memory, graph-aware PFNs, data-mixture attribution, policy-shift conformal calibration, agent execution control, semantic/document-backed databases, and integrity constraints. Suppress repeat daily stream summary."}
{"date_delivered":"2026-10-28","type":"proceedings","title":"TMLR October 2026 accepted papers late-month update as of October 28","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered newly visible late-October TMLR items including Minerva, Leadership as Coordination Control, Cognitive Episodes in LLM Reasoning Traces, Prover Agent, Routing Beats Latency, and related agent/LLM evaluation-control papers. Suppress repeat Oct 28 TMLR snapshot."}
{"date_delivered":"2026-10-28","type":"paper","title":"TACO-Graph: Learning How to Construct Text-Attributed Graphs from Tabular Data","authors_or_org":"TACO-Graph authors as listed on arXiv","url":"https://arxiv.org/abs/2610.36655","memory":"Worth Watching. Covered interpretable decision-tree framework for choosing graph constructions from multi-attribute tabular data for GNN and GraphRAG tasks. Suppress arXiv/code/venue reposts unless method or benchmark materially expands."}
{"date_delivered":"2026-10-28","type":"paper","title":"Base Models Can Detect Hidden Intentions that Prompted Classifiers Miss","authors_or_org":"Oz Amram","url":"https://arxiv.org/abs/2610.36202","memory":"Worth Watching. Covered persona-header likelihood evaluation using base-model likelihoods to decode hidden/subliminal objectives in generated outputs where prompted classifiers remain near chance. Suppress arXiv/code/social/venue repeats unless audit method or evidence materially expands."}
{"date_delivered":"2026-10-28","type":"paper","title":"Back to the Future: The Evolving Universal Relation Model","authors_or_org":"Nan Tang, Haixun Wang","url":"https://arxiv.org/abs/2610.36833","memory":"Worth Watching and cs.DB item. Covered query-first evolving universal relation model for document-backed analytics where queries drive schema and database-state evolution. Suppress future arXiv/venue/repost mentions unless formalism, system, or evaluation materially expands."}
{"date_delivered":"2026-10-28","type":"benchmark","title":"Pneuma: A Large-Scale Real-World Time Series Benchmark for Commercial Aircraft Predictive Maintenance","authors_or_org":"Jiafeng Lin, Yutian Zhang, Huan Zhang, Yuxuan Wang, Jinyan Feng, Yuhui Liu, Zhongyi Pei, Jianmin Wang","url":"https://arxiv.org/abs/2610.37563","memory":"Worth Watching benchmark. Covered commercial-aircraft predictive-maintenance time-series benchmark with 920M+ multivariate time steps, four aircraft types, nine fault scenarios, and forecasting/classification/anomaly tasks. Suppress future arXiv/dataset/code reposts unless benchmark materially expands."}
{"date_delivered":"2026-10-28","type":"software","title":"KORA: Deterministic-First Execution Control for AI Workloads","authors_or_org":"Albert Heekwan Kim","url":"https://arxiv.org/abs/2610.35869","memory":"Worth Watching. Covered deterministic-first execution-control layer that routes structured/verifiable tasks before model invocation, with reproducible deterministic-heavy benchmark and telemetry. Suppress arXiv/code/tool repeats unless system or evidence materially changes."}
```