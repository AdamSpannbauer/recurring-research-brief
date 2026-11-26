## Section 1: Top 5 Papers

1. **When to Trust a PFN: Detecting Harmful Shift in Tabular Foundation Models**  
   **Authors:** Viet Nguyen, Herman Bergström, Stephan Rabanser, Rahul G. Krishnan  
   **Venue/source:** arXiv; NeurIPS 2026  
   **Release date:** November 25, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2611.34767))  
   This is the most directly relevant new paper: it attacks a central deployment weakness of tabular prior-fitted networks—silent failure under distribution shift. The proposed monitor, **CALD** (Calibrated Anchor-Loss Disagreement), uses decoder fine-tuning to create disagreement with test-batch predictions while maintaining performance on an in-distribution anchor set. The resulting anchor loss becomes an unsupervised harmful-shift alarm. The paper reports tests across 14 tabular/structured-shift datasets on TabPFN and TabICL, with better resilience to benign-shift false alarms than baselines. The framing is especially useful because TFMs increasingly look strong on static benchmarks but remain under-instrumented in deployment.  
   **Why you should care:** Reliability monitors may become as important as raw TabArena accuracy for the next generation of tabular foundation models.

2. **Data Agents Need a Map: Evolving, Demand-Driven Knowledge of Large Collections**  
   **Authors:** Christos Koutras, Yurong Liu, Laura Haas, Juliana Freire  
   **Venue/source:** arXiv cs.DB  
   **Release date:** November 25, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2611.33763))  
   This is a strong database-systems position paper for persistent semantic infrastructure around data agents. The core argument is that current agents repeatedly rediscover dataset semantics, joins, implicit context, profiles, and relationships, then discard the work. The proposed **semantic atlas** stores dataset-level descriptions offline and builds relationship/integration knowledge on demand, with provenance and confidence attached to every item. The proof of concept on DAB suggests that even a partial atlas can reduce coding-agent token consumption by roughly one-fifth to one-third while preserving accuracy. This is a natural continuation of recent data-agent, semantic-query, and data-lake work, but with a stronger “persistent institutional memory” design principle.  
   **Why you should care:** It reframes data-agent progress away from one-off tool use and toward durable, evolving data-management assets.

3. **Single-Database Rewards Are Hackable: Counterfactual Execution for Trustworthy Text-to-SQL RL**  
   **Authors:** Shreshth Rai, Rishii Kumar Singh, Aksh Aggarwal  
   **Venue/source:** arXiv cs.LG/cs.DB  
   **Release date:** November 25, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2611.34363))  
   The paper identifies a concrete reward-hacking failure in Text-to-SQL reinforcement learning: a wrong query can receive full reward if it happens to match the reference answer on a single database instance. The fix is counterfactual execution—run candidate SQL on hidden generated database copies and reward only if results remain correct. On 1,302 synthetic audit questions, strict counterfactual reward reduces fully rewarded buggy queries from 29.5% to 16.8% and reward hacks from 54.1% to 1.9%, while rejecting none of 2,847 correct queries. The RL gains are more nuanced, but the evaluation result is important for database-grounded agent training.  
   **Why you should care:** For semantic/database agents, reward correctness increasingly depends on counterfactual data generation, not just execution on a benchmark instance.

4. **Put the World Back: Timestamps Matter in Time Series Reasoning**  
   **Authors:** Tingrui Huang, Yuanyuan Deng, Qingren Yao, Joaquin Vanschoren, Mykola Pechenizkiy, Songgaojun Deng  
   **Venue/source:** arXiv; NeurIPS 2026 Workshop on Foundation Models for Temporal Systems  
   **Release date:** November 25, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2611.34848))  
   This paper is a careful evaluation critique for time-series reasoning with LLMs and temporal foundation models. It argues that many evaluations pre-align events and observations, making it impossible to know whether a model uses timestamps or merely exploits ordered input and correlations. The authors propose a “world-to-series projection” view in which timestamps connect external events and numerical observations to shared latent world states. Controlled interventions on 310 questions show that accuracy can remain high when timestamps are replaced or removed, but failures appear when event-series alignment is broken. The paper is less about a new model than about making temporal evaluation causally meaningful.  
   **Why you should care:** It gives a clean diagnostic vocabulary for separating genuine temporal grounding from shortcut-based time-series reasoning.

5. **Mixture-of-Loops Transformer**  
   **Authors:** Lianghui Zhu, Shijie Wang, Xinggang Wang, Jinze Bai, Bo Wang, Xiang Bai  
   **Venue/source:** arXiv  
   **Release date:** November 25, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2611.34923))  
   MoLT pushes the looped-Transformer line by asking what should be carried across repeated layer traversals. Its **Mixture-of-Loops Attention** treats keys and values as memory for selective reuse across depth/loops, with variants that preserve residual streams or restart from embeddings while reusing loop-local KV. The U-shaped MoLT design separates memory construction from prediction readout and skips unused decoder traversals without changing predictions. The paper reports 400B-token pretraining evidence, including token-efficiency and perplexity/accuracy gains against OLMo3-style baselines, plus continued pretraining gains on Qwen3.5-0.8B.  
   **Why you should care:** Parameter reuse, KV memory, and looped depth are converging into a serious alternative to simply scaling depth/width.

## Section 2: Venue Watch

**arXiv cs.LG/stat.ML fresh stream, November 26.** The November 26 cs.LG page shows 271 new entries, with dense activity in tabular foundation-model reliability, looped/parameter-reuse architectures, world-model uncertainty, time-series reasoning, model-routing audits, and decision-model simulation. The most relevant cluster is no longer “yet another TFM,” but **TFM deployment instrumentation**: harmful-shift detection for PFNs, decision-focused tabular fine-tuning, timestamp-grounding diagnostics, and uncertainty behavior in world models. A second cluster revisits looped and repeated-parameter architectures: MoLT proposes cross-loop KV reuse, while LoopTitan argues much of the reported looped-MoE gain may come from architecture shape, optimizer, residual scaling, or added compute rather than parameter revisit itself. ([arxiv.cnoctave.top](https://arxiv.cnoctave.top/list/cs.LG/recent))

**arXiv cs.DB fresh stream, November 26.** The database stream has a strong agentic-data flavor: semantic atlases for data agents, embodied multimodal analytics, counterfactual Text-to-SQL rewards, RDF/KG merge semantics, and Lean-based SQL verification. The notable shift is from “LLM as query interpreter” toward **verification, persistence, and reuse**: semantic maps that survive across questions, counterfactual database copies for reward validation, schema-aware merge operators, and proof challenges for SQL equivalence. ([arxiv.cnoctave.top](https://arxiv.cnoctave.top/list/cs.DB/recent))

**TMLR November 2026 stream.** The visible November TMLR page continues to be broad and noisy, but useful for venue awareness: rare-event LM evaluation, diffusion autoencoders, unlearning, reward-hacking mitigation, fairness/privacy reproductions, PEFT, agent evidence tracing, foundation-model control surveys, and local conformal prediction for trees all appear in the November stream. The top-of-page items are not all core to Adam’s interests, but the venue is clearly absorbing work on robust evaluation, provenance, unlearning, and inference-time control. ([jmlr.org](https://jmlr.org/tmlr/papers/))

**NeurIPS 2026 program status.** The NeurIPS 2026 downloads/program index is visible with 9,276 events, while the main conference remains distributed across Sydney, Atlanta, and Paris; official awards still do not appear to be stably posted in the crawl. The program index is now useful for mining paper titles, but not yet a clean proceedings/award source. ([neurips.cc](https://neurips.cc/Downloads/2026?utm_source=openai))

## Section 3: Emerging Trends

- **Tabular foundation models are entering the reliability phase.** New work is less about proving that TFMs can beat GBDTs and more about when to trust them: shift detection, context uncertainty, weighted samples, privacy, calibration, reliability benchmarks, and deployment-time adaptation.

- **Semantic query processing is becoming statistical systems engineering.** Recent database papers increasingly treat LLM calls as stochastic, reusable, auditable operators: counterfactual execution, semantic views, semantic tags, approximate semantic counts, and verification/provenance layers are converging.

- **Looped/reused-parameter architectures are being deconfounded.** MoLT pushes practical loop/KV reuse, while LoopTitan asks whether parameter revisit itself causes gains. Expect more papers separating architecture shape, optimizer, residual scaling, KV cache behavior, and actual recurrence.

- **Temporal and world-model evaluation is shifting from accuracy to alignment with latent world state.** Timestamp grounding, epistemic uncertainty propagation, and causal response recovery are becoming central diagnostics for time-series and world-model FMs.

- **Agent memory is moving from context stuffing to persistent, typed infrastructure.** Semantic atlases, RDF/KG merge semantics, agent maps, and Lean/SQL verification all point toward database-backed memory and correctness contracts rather than larger prompts alone.

## Section 4: Worth Watching

- **LoopTitan: What Does Parameter Revisit Buy a Mixture-of-Experts?** A valuable controlled study arguing that looped-MoE gains may largely come from architecture shape, residual scaling, optimizer effects, and compute—not parameter revisit per se. It releases 17 pretrained models and a public experiment record. ([arxiv.org](https://arxiv.org/abs/2611.34821))

- **Not all world models can doubt.** Compares JEPA-style and RSSM/DreamerV3-style world models, finding that reconstruction and recurrent averaging can attenuate epistemic-uncertainty signals before they reach the estimator. Worth tracking for causal/world-model uncertainty. ([arxiv.org](https://arxiv.org/abs/2611.34830))

- **DecisionReplay.** A released corpus and deterministic simulator containing probability vectors, cost, and latency for 17 commercial decision models over 35 benchmarks; useful for studying routers, cascades, early exits, and ensemble economics without fresh model calls. ([arxiv.org](https://arxiv.org/abs/2611.34627))

- **EMMA.** A database-style operator framework for multimodal embodied-AI data—video, LiDAR, GPS—using staged predicate evaluation, temporal co-location indexing, shared world stores, and offline-learned execution policies. ([arxiv.org](https://arxiv.org/abs/2611.33765))

- **Shape-aware RDF/KG merge.** A practical three-way merge operator where SHACL shapes define semantic conflicts; useful for multi-agent data stores and evolving knowledge graphs. ([arxiv.org](https://arxiv.org/abs/2611.34870))

- **SeQLean.** Uses Lean proof challenges to verify SQL translations, including equivalence of independently generated queries and database-specific properties. Worth suppressing for future repeats because it fits the growing SQL-verification thread. ([arxiv.org](https://arxiv.org/abs/2611.33181))

## Section 5: Discord Highlights

**Nov 26, 2026**

Top papers:
1. **When to Trust a PFN** — unsupervised harmful-shift alarms for TabPFN/TabICL.
2. **Data Agents Need a Map** — persistent semantic atlas for data lakes and agent workflows.
3. **Single-Database Rewards Are Hackable** — counterfactual execution exposes Text-to-SQL RL reward hacks.
4. **Put the World Back** — timestamp-grounded diagnostics for time-series reasoning.
5. **Mixture-of-Loops Transformer** — loop/KV memory reuse for efficient repeated-depth transformers.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-11-26","type":"paper","title":"When to Trust a PFN: Detecting Harmful Shift in Tabular Foundation Models","authors_or_org":"Viet Nguyen, Herman Bergström, Stephan Rabanser, Rahul G. Krishnan","url":"https://arxiv.org/abs/2611.34767","memory":"Top 5 paper. Covered NeurIPS 2026 paper CALD for unsupervised harmful-shift detection in tabular PFNs/TFMs, using calibrated anchor-loss disagreement on TabPFN and TabICL. Suppress arXiv, code, project, and NeurIPS reposts unless method or evaluation materially changes."}
{"date_delivered":"2026-11-26","type":"paper","title":"Data Agents Need a Map: Evolving, Demand-Driven Knowledge of Large Collections","authors_or_org":"Christos Koutras, Yurong Liu, Laura Haas, Juliana Freire","url":"https://arxiv.org/abs/2611.33763","memory":"Top 5 paper. Covered semantic atlas vision for data agents over large table/data-lake collections, persisting dataset semantics, profiles, relationships, provenance, confidence, and on-demand integrated views. Suppress arXiv/venue/repost versions unless prototype or evaluation materially expands."}
{"date_delivered":"2026-11-26","type":"paper","title":"Single-Database Rewards Are Hackable: Counterfactual Execution for Trustworthy Text-to-SQL RL","authors_or_org":"Shreshth Rai, Rishii Kumar Singh, Aksh Aggarwal","url":"https://arxiv.org/abs/2611.34363","memory":"Top 5 paper. Covered counterfactual database execution reward for Text-to-SQL RL, reducing rewarded buggy queries and reward hacks from single-database execution; includes code/data/models. Suppress arXiv/code/HF/venue reposts unless reward method or results materially change."}
{"date_delivered":"2026-11-26","type":"paper","title":"Put the World Back: Timestamps Matter in Time Series Reasoning","authors_or_org":"Tingrui Huang, Yuanyuan Deng, Qingren Yao, Joaquin Vanschoren, Mykola Pechenizkiy, Songgaojun Deng","url":"https://arxiv.org/abs/2611.34848","memory":"Top 5 paper. Covered timestamp-grounded diagnostic protocol for time-series reasoning and world-to-series projection; NeurIPS 2026 Foundation Models for Temporal Systems workshop item. Suppress arXiv/workshop/code/repost versions unless diagnostics or benchmark materially expand."}
{"date_delivered":"2026-11-26","type":"paper","title":"Mixture-of-Loops Transformer","authors_or_org":"Lianghui Zhu, Shijie Wang, Xinggang Wang, Jinze Bai, Bo Wang, Xiang Bai","url":"https://arxiv.org/abs/2611.34923","memory":"Top 5 paper. Covered MoLT/MoLA looped Transformer architecture using KV memory across loops, U-MoLT, 400B-token pretraining, Qwen3.5 continued pretraining, and latency/token-efficiency claims. Suppress arXiv/code/social/venue reposts unless architecture or evidence materially changes."}
{"date_delivered":"2026-11-26","type":"proceedings","title":"arXiv cs.LG/stat.ML fresh stream for November 26 2026","authors_or_org":"arXiv cs.LG/stat.ML","url":"https://arxiv.cnoctave.top/list/cs.LG/recent","memory":"Venue Watch. Covered Nov 26 2026 arXiv ML stream with 271 new cs.LG entries, emphasizing TFM reliability, looped/reused-parameter architectures, world-model uncertainty, time-series reasoning, routing audits, and decision-model simulation. Suppress repeat daily stream summary."}
{"date_delivered":"2026-11-26","type":"proceedings","title":"arXiv cs.DB fresh stream for November 26 2026","authors_or_org":"arXiv cs.DB","url":"https://arxiv.cnoctave.top/list/cs.DB/recent","memory":"Venue Watch. Covered Nov 26 database stream with data-agent semantic maps, embodied multimodal analytics, counterfactual Text-to-SQL rewards, RDF/KG merge semantics, and Lean SQL verification. Suppress repeat daily stream summary."}
{"date_delivered":"2026-11-26","type":"proceedings","title":"TMLR November 2026 accepted papers stream status as of November 26","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered current visible November 2026 TMLR stream themes: rare-event LM evaluation, diffusion autoencoders, unlearning, reward-hacking mitigation, fairness/privacy reproductions, PEFT, agent evidence tracing, foundation-model control surveys, and local conformal prediction for trees. Suppress repeat broad November TMLR stream summaries unless new late-November additions are materially different."}
{"date_delivered":"2026-11-26","type":"announcement","title":"NeurIPS 2026 program/downloads status as of November 26","authors_or_org":"NeurIPS 2026","url":"https://neurips.cc/Downloads/2026","memory":"Venue Watch. Noted NeurIPS 2026 Downloads/program index visible with 9276 events and three-site Sydney/Atlanta/Paris structure; no stable official awards found. Suppress repeat program-index/status notes unless official proceedings, awards, or materially different program metadata appears."}
{"date_delivered":"2026-11-26","type":"paper","title":"LoopTitan: What Does Parameter Revisit Buy a Mixture-of-Experts?","authors_or_org":"Zichen Tian, Yudong Lu, Xuansheng Wu, Na Zou, Xia Hu, Guanchu Wang, Qianru Sun","url":"https://arxiv.org/abs/2611.34821","memory":"Worth Watching. Covered controlled study arguing looped-MoE gains largely come from architecture shape, residual scaling, optimizer effects, and added compute rather than parameter revisit itself; releases LoopTitan models and experiment record. Suppress arXiv/code/model/social repeats unless conclusions materially change."}
{"date_delivered":"2026-11-26","type":"paper","title":"Not all world models can doubt: how training objective and architecture shape epistemic uncertainty in JEPA and RSSM world models","authors_or_org":"Simon Baur, Wojciech Samek, Jackie Ma","url":"https://arxiv.org/abs/2611.34830","memory":"Worth Watching. Covered comparison of JEPA and RSSM/DreamerV3 epistemic uncertainty propagation, showing reconstruction/recurrent mechanisms can attenuate state perturbations before uncertainty estimation. Suppress arXiv/code/venue reposts unless uncertainty framework or experiments materially expand."}
{"date_delivered":"2026-11-26","type":"dataset","title":"DecisionReplay: A Corpus and Offline Simulator for Ensembling Decision Models","authors_or_org":"Dean Ariel, Seffi Cohen","url":"https://arxiv.org/abs/2611.34627","memory":"Worth Watching. Covered corpus/simulator with probability vectors, costs, and latencies for 17 commercial decision models on 35 benchmarks, enabling router/cascade/ensemble evaluation without new model calls. Suppress arXiv/dataset/code reposts unless corpus materially expands."}
{"date_delivered":"2026-11-26","type":"software","title":"EMMA: Efficient and Effective Cooperative Multi-Modal Analytics over Embodied AI Data","authors_or_org":"Jiangneng Li, Jie Wang, Ziqi Yin, Zheng Wang, Gao Cong","url":"https://arxiv.org/abs/2611.33765","memory":"Worth Watching. Covered operator-oriented query-processing framework for embodied AI multimodal data using staged predicate evaluation, temporal co-location indexing, shared world store, and offline-learned execution policies. Suppress arXiv/code/venue reposts unless system or evaluation materially changes."}
{"date_delivered":"2026-11-26","type":"software","title":"Shape-Aware Three-Way Merge for RDF Knowledge Graphs","authors_or_org":"Steve Brown","url":"https://arxiv.org/abs/2611.34870","memory":"Worth Watching. Covered SHACL/shape-aware RDF KG merge where schema defines semantic conflicts, reducing human questions while avoiding silent data loss in tested cardinality-conflict cases. Suppress arXiv/artifact/venue reposts unless merge semantics or deployment evidence materially expands."}
{"date_delivered":"2026-11-26","type":"software","title":"SeQLean: Verifying SQL queries using Lean","authors_or_org":"Siddhartha Gadgil, Anirudh Gupta, Ajay Kumar Nair","url":"https://arxiv.org/abs/2611.33181","memory":"Worth Watching. Covered Lean-based SQL verification via proof challenges, query equivalence, database-specific properties, and JSON API for agentic integration. Suppress arXiv/code/venue reposts unless SQL coverage or proof system materially expands."}
```