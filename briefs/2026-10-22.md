## Section 1: Top 5 Papers

1. **When Thoughts Become Memory: Unifying In-Context Learning and Fine-Tuning**  
   **Authors:** Leon Chlon, Julie Huang  
   **Venue/source/date:** arXiv, listed October 22, 2026  
   **Link:** arXiv:2610.29419. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   This is the most conceptually useful item of the day: a proposed information-value law for deciding whether new data should live in a model’s **context** or its **weights**. The core quantity is code-length saved on held-out queries, decomposed into stored bits about the query, prior repair, and decoding loss. The authors turn this into certified one-shot and anytime-valid tests, with examples spanning transformers, TabPFN, occupancy networks, stereo models, kriging, and evidence adjudication.  
   **Why you should care:** It offers a formal language for comparing in-context learning, caching, fine-tuning, and support-set construction.

2. **SCDM: Scalable Causal Discovery in Nonlinear Temporal Systems with Meta-Learning**  
   **Authors:** Jingbo Wang, Kegeng Tang, Zihao Wang, Shaogang Ren  
   **Venue/source/date:** arXiv; accepted at NeurIPS 2026; listed October 22, 2026  
   **Link:** arXiv:2610.29992. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   SCDM tackles high-dimensional nonlinear time-series causal discovery by treating each target variable as a task in a shared-parameter meta-learning setup. Rather than fitting separate target-wise predictors or running many conditional tests, the model accumulates structural evidence in a shared temporal predictor and causal-strength matrix, then extracts directed causal scores post-training. The paper includes a finite-error recovery principle under delayed-system assumptions and evaluates on synthetic, neuroimaging-style, high-dimensional, and real-world temporal systems.  
   **Why you should care:** It is a plausible route from causal discovery as bespoke testing to causal discovery as amortized structure learning.

3. **Auditing Conformal Prediction for Language Models Under Inference-Time Model Shift**  
   **Authors:** Achref Doula, Max Mühlhäuser  
   **Venue/source/date:** arXiv; accepted at NeurIPS 2026 Evaluations & Datasets; listed October 22, 2026  
   **Link:** arXiv:2610.28937. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   This paper isolates a subtle but highly practical failure mode: conformal calibration for language-model systems can break even when the task distribution is unchanged, if inference configuration changes between calibration and deployment. Quantization mode, temperature, and serving choices induce score-distribution shifts, violating split-conformal exchangeability. The authors test 8 language models, 4 finite-label benchmarks, and 12 inference configurations, showing matched-protocol evaluation can substantially overstate deployment coverage.  
   **Why you should care:** It sharpens the reliability story for LLM systems: calibration must treat inference configuration as part of the statistical object.

4. **Building SQL Equivalence Proofs from Query Rewrite Rules**  
   **Authors:** Chunyu Chen, Xinyi Huang, Zhengjie Miao  
   **Venue/source/date:** arXiv cs.DB, October 22, 2026  
   **Link:** arXiv:2610.30100. ([arxiv.org](https://arxiv.org/list/cs.DB/new))  
   EquiTrace turns optimizer-style query rewrite rules into constructive SQL equivalence proofs, aimed at query rewriting and semantic evaluation of text-to-SQL systems. Instead of relying only on execution agreement, it aligns alternative query representations, searches rewrite derivations, and returns replayable proof traces. Reported coverage includes 648/1,106 expected-equivalent text-to-SQL pairs, 229/266 curated pairs, and 97/240 LLM-generated rewrites that execution judged equivalent.  
   **Why you should care:** It fits the emerging need for proof-carrying data-agent infrastructure: not just “the SQL ran,” but “the SQL transformation is justified.”

5. **Your Benchmark Is an Empirical Measure Over Difficulty**  
   **Authors:** Yifan Sun, Naicheng Yu, Jiawen Gong, Jingyan Shen, Huan Zhang  
   **Venue/source/date:** arXiv; accepted at NeurIPS 2026; listed October 22, 2026  
   **Link:** arXiv:2610.29927. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   The paper reframes benchmark evaluation as integration against an empirical measure over item difficulty. This yields two failure modes: measure mismatch, where the benchmark overweights the wrong difficulty region, and coverage gaps, where localized progress is invisible. The authors analyze 25 benchmarks across seven domains and propose BenchFill, a difficulty-targeted item-rewriting method to reduce coverage gaps.  
   **Why you should care:** It gives a statistical vocabulary for why leaderboards mislead, especially for agent and reasoning benchmarks with sparse or uneven task difficulty.

## Section 2: Venue Watch

**arXiv daily stream, October 22.** The October 22 crawl is unusually broad: cs.LG lists 137 new submissions out of 379 total entries; stat.ML lists 13 new submissions out of 67 total; cs.DB lists 3 new database submissions out of 10 total. The day’s strongest clusters are: context/weight tradeoffs, temporal causal discovery, conformal evaluation under deployment shift, benchmark measurement theory, vector/KV-cache systems, SQL equivalence proofs, and auditable LLM-generated records. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

**TMLR October 2026 incremental stream.** The top of the TMLR page now shows additional October acceptances including *MemoryVLN*, stochastic-source analysis in PPO, BYOL-style language adaptation, graph-free distillation equity, metric graph advection message passing, test-time scaling for text-to-image flow matching, diffusion-compressed video tokens, collinearity effects in variable importance, medical-agent surveying, TFM-based association-rule learning, probabilistic time-series flow matching, KV-cache recall locality, and in-context learning dynamics. This is a broad “systems plus representation plus reliability” batch rather than a single dominant theme. ([jmlr.org](https://jmlr.org/tmlr/papers/))

**JMLR Volume 27 visible issue stream.** JMLR’s Volume 27 page still ends at article 205, but the currently visible middle/tail contains several items worth noting for future filtering: causal falsification of digital twins, DP synthetic relational data generation, instrumental-variable testability, transfer/integrative regression, extrapolation-aware inference, concept-model leakage, causal data fusion, contrastive-learning approximability, diffusion learning of low-dimensional distributions, conformal selection, and test-time regression for associative-memory sequence models. These are not all “new today,” but they form a dense adjacent cluster around causal/statistical validity, privacy, and representation theory. ([jmlr.org](https://www.jmlr.org/papers/v27/))

## Section 3: Emerging Trends

- **Context is becoming a formally priced resource.** The strongest thread connects “thoughts vs memory,” KV/cache retention, conformal inference under inference shifts, and benchmark difficulty measures: current work is asking what information should be kept, where it should live, and how to certify that it still means the same thing after deployment changes.

- **Semantic data systems are moving from demos to proof obligations.** EquiTrace, certified semantic views, SQL equivalence refutation, semantic-query variance audits, and typed agent contracts point toward database systems that treat LLM calls as stochastic, auditable operators rather than magic black boxes.

- **Causal discovery is being amortized.** SCDM and recent causal foundation-model work suggest a shift from per-problem search/testing pipelines to learned causal scoring or representation machinery, but the good papers still attach recovery principles or identifiability assumptions.

- **Reliability evaluation is getting more distributional.** Difficulty measures, conformal model-shift audits, TabReliBench-style reliability, and prediction-powered disaggregated evaluation all push beyond average accuracy toward coverage, subgroup behavior, difficulty weighting, and deployment-protocol sensitivity.

## Section 4: Worth Watching

- **KVLearn: To Keep or Not to Keep.** A cost-aware KV-cache retention framework for disaggregated LLM serving that predicts prefix reuse and converts it into keep/admit decisions under recomputation, transfer, and storage costs. Worth suppressing because it is a concrete systems artifact for long-context/disaggregated serving. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **WaRP: Workload-Aware Request Planning for Vector Retrieval on Object Storage.** Optimizes grouping of probed vector-cluster byte ranges into object-store requests; implemented in Lance’s I/O scheduler and evaluated on AWS S3 at 100M-vector scale. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

- **BiasGuard-D / Conflicted Records.** A typed adversarial-contract system for auditing LLM-generated records using adversarial roles, quorum adjudication, and referential-plus-semantic invariants. Interesting as “LLM output quality as auditable records” rather than ordinary prompting. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

- **SCARCE: Implicit Feature Reweighting for Label-Free Graph Generalization.** A label-free graph OOD representation method using environment confusion plus reconstruction to downweight environment-discriminative directions without class labels. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **CALLIOPE: Private Insights into AI Use, Without Embeddings.** A differential-privacy framework for discovering topic hierarchies in large unstructured corpora, using LLMs directly rather than embedding clustering; especially relevant for privacy-preserving analysis of LLM interaction logs. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

## Section 5: Discord Highlights

**Oct 22 brief**

Top papers:
1. **When Thoughts Become Memory** — certified rule for whether information belongs in context or weights.  
2. **SCDM** — scalable meta-learned causal discovery for nonlinear temporal systems.  
3. **Auditing Conformal Prediction for LMs Under Inference-Time Model Shift** — calibration can fail when serving config changes.  
4. **Building SQL Equivalence Proofs from Query Rewrite Rules** — replayable SQL equivalence proofs for Text-to-SQL and query rewriting.  
5. **Your Benchmark Is an Empirical Measure Over Difficulty** — benchmark difficulty distributions explain leaderboard blind spots.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-10-22","type":"paper","title":"When Thoughts Become Memory: Unifying In-Context Learning and Fine-Tuning","authors_or_org":"Leon Chlon, Julie Huang","url":"https://arxiv.org/abs/2610.29419","memory":"Top 5 paper. Covered Oct 22 2026 arXiv/stat.ML paper giving certified information-value law for deciding whether unseen data belong in context or weights; examples include transformers, TabPFN, occupancy networks, stereo networks, kriging, and evidence adjudication. Suppress arXiv/code/venue/social reposts unless law, certificates, or empirical scope materially change."}
{"date_delivered":"2026-10-22","type":"paper","title":"SCDM: Scalable Causal Discovery in Nonlinear Temporal Systems with Meta-Learning","authors_or_org":"Jingbo Wang, Kegeng Tang, Zihao Wang, Shaogang Ren","url":"https://arxiv.org/abs/2610.29992","memory":"Top 5 paper. Covered NeurIPS 2026 arXiv paper using shared-parameter meta-learning for scalable nonlinear temporal causal discovery, shared causal-strength matrix, post-training graph readout, and finite-error recovery principle. Suppress arXiv/NeurIPS/code reposts unless assumptions, theory, or empirical scope materially expand."}
{"date_delivered":"2026-10-22","type":"paper","title":"Auditing Conformal Prediction for Language Models Under Inference-Time Model Shift","authors_or_org":"Achref Doula, Max Mühlhäuser","url":"https://arxiv.org/abs/2610.28937","memory":"Top 5 paper. Covered NeurIPS 2026 Evaluations & Datasets paper showing conformal prediction for language models can undercover when inference configuration such as quantization, temperature, or serving setup changes between calibration and deployment. Suppress arXiv/NeurIPS/code/social reposts unless evaluation protocol or theory materially changes."}
{"date_delivered":"2026-10-22","type":"paper","title":"Building SQL Equivalence Proofs from Query Rewrite Rules","authors_or_org":"Chunyu Chen, Xinyi Huang, Zhengjie Miao","url":"https://arxiv.org/abs/2610.30100","memory":"Top 5 paper and cs.DB item. Covered EquiTrace proof-producing SQL equivalence system using optimizer-style rewrite rules, replayable derivations, and text-to-SQL/query-rewrite equivalence benchmarks. Suppress arXiv/code/venue reposts unless proof coverage, system, or benchmark materially expands."}
{"date_delivered":"2026-10-22","type":"paper","title":"Your Benchmark Is an Empirical Measure Over Difficulty","authors_or_org":"Yifan Sun, Naicheng Yu, Jiawen Gong, Jingyan Shen, Huan Zhang","url":"https://arxiv.org/abs/2610.29927","memory":"Top 5 paper. Covered NeurIPS 2026 paper formalizing benchmarks as empirical measures over item difficulty, diagnosing measure mismatch and coverage gaps, and proposing BenchFill. Suppress arXiv/NeurIPS/code/benchmark reposts unless theory, diagnostics, or benchmark suite materially changes."}
{"date_delivered":"2026-10-22","type":"proceedings","title":"arXiv cs.LG/stat.ML/cs.DB new-submission stream for October 22 2026","authors_or_org":"arXiv cs.LG, stat.ML, cs.DB","url":"https://arxiv.org/list/cs.LG/new","memory":"Venue Watch. Covered Oct 22 2026 streams: cs.LG 137 new submissions out of 379 total, stat.ML 13 new out of 67, cs.DB 3 new out of 10. Themes included context-vs-weights valuation, temporal causal discovery, conformal evaluation under inference shift, benchmark difficulty measures, SQL equivalence, KV/vector systems, and auditable LLM records. Suppress repeat daily stream summary."}
{"date_delivered":"2026-10-22","type":"proceedings","title":"TMLR October 2026 accepted papers incremental update as of October 22","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered visible Oct 22 TMLR October additions/top-of-page activity including MemoryVLN, stochastic sources of PPO divergence, BYOL language adaptation, graph-free distillation equity, MeGA-MP, T2I flow-matching test-time scaling, DiCoDe, collinearity effects on variable importance, medical-agent survey, TFM association-rule learning, time-series flow matching, KV-cache recall locality, and ICL dynamics. Suppress repeat Oct 22 snapshot."}
{"date_delivered":"2026-10-22","type":"venue_issue","title":"JMLR Volume 27 visible mid/tail stream as of October 22 2026","authors_or_org":"Journal of Machine Learning Research","url":"https://www.jmlr.org/papers/v27/","memory":"Venue Watch. Covered visible JMLR Volume 27 stream through article 205, especially articles around 152-190 and tail themes: causal falsification of digital twins, DP synthetic relational data, IV testability, concept-model leakage, causal data fusion, contrastive learning approximability, diffusion low-dimensional theory, conformal selection, and associative-memory test-time regression. Suppress repeat broad JMLR snapshot unless new articles after 205 appear."}
{"date_delivered":"2026-10-22","type":"software","title":"KVLearn / To Keep or Not to Keep: Learning KV Cache Retention in Disaggregated LLM Serving Systems","authors_or_org":"Dong Liu, Yanxuan Yu, Eric Jiang, Shu Wang, Ying Nian Wu","url":"https://arxiv.org/abs/2610.28637","memory":"Worth Watching. Covered SYSTOR 2026 paper on learning-based cost-aware KV-cache retention for disaggregated LLM serving using prefix reuse prediction, cost-aware retention scores, and adaptive admission thresholds. Suppress arXiv/code/venue reposts unless system or results materially change."}
{"date_delivered":"2026-10-22","type":"software","title":"WaRP: Workload-Aware Request Planning for Vector Retrieval on Object Storage","authors_or_org":"Ruipeng Wan, Xinyu Zeng, Yiming Qiao, Huanchen Zhang","url":"https://arxiv.org/abs/2610.29689","memory":"Worth Watching and cs.DB item. Covered workload-aware request grouping for vector retrieval payloads stored in cloud object storage, implemented in Lance I/O scheduler and evaluated on AWS S3 with 100M-vector indexes. Suppress arXiv/code/venue mentions unless request-planning system or evaluation materially expands."}
{"date_delivered":"2026-10-22","type":"software","title":"Conflicted Records: Typed Adversarial Contracts for Auditable LLM Output Quality Enforcement / BiasGuard-D","authors_or_org":"Kardelen Subasi, Jarosław A. Chudziak","url":"https://arxiv.org/abs/2610.29669","memory":"Worth Watching and cs.DB item. Covered CoopIS 2026 paper using typed adversarial inter-agent records, quorum adjudication, and referential-plus-semantic invariants for auditable LLM record quality. Suppress arXiv/venue/tool reposts unless contract system or evidence materially changes."}
{"date_delivered":"2026-10-22","type":"paper","title":"Implicit Feature Reweighting for Label-Free Graph Generalization","authors_or_org":"Tianjun Yao, Chen Xi, Xinyang Li, Lixian Zhong","url":"https://arxiv.org/abs/2610.29571","memory":"Worth Watching. Covered SCARCE label-free graph OOD representation method using environment confusion and graph reconstruction to contract environment-discriminative representation directions. Suppress future arXiv/code/venue mentions unless method or benchmarks materially expand."}
{"date_delivered":"2026-10-22","type":"resource","title":"CALLIOPE: Private Insights into AI Use, Without Embeddings","authors_or_org":"Edith Cohen, Vadym Doroshenko, Badih Ghazi, Charlie Harrison, Pritish Kamath, Alexander Knop, Ravi Kumar, Ethan Leeman, Pasin Manurangsi, Mikhail Pravilov, Adam Sealfon, Yurii Sushko, Marika Swanberg, Chiyuan Zhang","url":"https://arxiv.org/abs/2610.28797","memory":"Worth Watching. Covered differential-privacy framework for discovering topic hierarchies in large unstructured corpora such as LLM conversations using LLMs directly rather than embedding clustering. Suppress arXiv/code/tool/social reposts unless privacy mechanism, system, or empirical scope materially changes."}
```