## Section 1: Top 5 Papers

1. **Topological Signatures of Context-Level Reliability in TabPFN**  
   **Authors:** James Hu, Mahdi Ghelichi  
   **Venue/source/date:** arXiv, submitted July 20, 2026.  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2607.17962))  
   This is the most directly relevant new tabular-foundation-model paper: it treats TabPFN layer states as evolving point clouds and applies zigzag persistent homology to diagnose when in-context tabular inference is geometrically stressed. The authors build controlled synthetic tasks with known probabilities and nontrivial topology—warped circles, tori, spheres, Hopf links, trefoil knots, Swiss rolls—and report that representation-topology descriptors correlate with reliability, Bayes error, residuals, and overconfidence. The key idea is not another leaderboard but a context-level reliability signal for TFM inference.  
   **Why you should care:** This is an unusually concrete bridge between tabular FM interpretability, uncertainty, and dataset geometry.

2. **Scalable Causal Imitation Learning**  
   **Authors:** Eylam Tagor, Mingxuan Li, Elias Bareinboim  
   **Venue/source/date:** arXiv, submitted July 18, 2026; Reinforcement Learning Journal / RLC 2026.  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2607.17003))  
   This paper extends causal imitation learning from short-horizon toy regimes to high-dimensional continuous control. Existing causal behavioral cloning and causal GAIL become unstable or impractical under long horizons, observation mismatch, and confounded expert demonstrations. The paper introduces Causal SQIL and Causal IQ-Learn, combining causal adjustment with stronger off-policy inverse-RL objectives and an efficient sliding-window approximation to the sequential π-backdoor criterion. Experiments in confounded environments show large gains over causally unaware imitation methods and earlier CIL baselines.  
   **Why you should care:** It is a credible step toward making causal ML operational inside sequential decision systems rather than only in static prediction.

3. **Uncovering Latent Reasoning Strategies in Language Models**  
   **Authors:** Awni Altabaa, John Lafferty  
   **Venue/source/date:** arXiv, submitted July 20, 2026.  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2607.17674))  
   This paper studies how to factor a pretrained LM’s response distribution into latent strategy-conditioned components without changing the base distribution. The central technical obstacle is posterior collapse: if the initialized generator already models \(p_\theta(y \mid x)\), a latent strategy variable is ignored. The authors propose a variational objective based on fractional information gain relative to the base model’s response loss, emphasizing high-surprisal tokens where strategy choice matters. On multi-strategy algorithmic tasks, the learned latent codes align with reference strategies.  
   **Why you should care:** It offers a principled route from behavioral traces to decomposed reasoning mechanisms, adjacent to representation interpretability and causal mediation.

4. **Causal Discovery on Irregular Time Series**  
   **Authors:** Martim Penim, Ricardo Ribeiro Pereira, Jacopo Bono, Hugo Ferreira, Mário A. T. Figueiredo, Pedro Bizarro  
   **Venue/source/date:** arXiv, submitted July 20, 2026.  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2607.18226))  
   Many causal discovery methods assume regular sampling and discrete lag structure, which makes them brittle for healthcare, sensors, finance, and event streams. This work extends PCMCI+ to irregular time series by aggregating causal influence over predefined temporal windows rather than fixed lags. The evaluation uses synthetic irregular event streams with known causal structure and varying noise, where the windowed method substantially outperforms standard PCMCI+ under irregular sampling. The method is conceptually simple, but the target problem is important and under-served.  
   **Why you should care:** Irregular event streams are the default in operational data; causal discovery methods that ignore sampling irregularity often solve the wrong problem.

5. **Optimizing the Preconditioner: A Black-box Online-to-Nonconvex Conversion with Static Regret Minimization Oracles**  
   **Authors:** Haichen Hu, David Simchi-Levi  
   **Venue/source/date:** arXiv, submitted July 20, 2026.  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2607.17607))  
   This is a clean optimization-theory contribution: stochastic nonconvex optimization is reduced to ordinary static-regret minimization in online convex optimization. The reduction maintains a predictable gradient tracker while a black-box online learner selects the preconditioner. With square-root static regret, the framework recovers the classical \(O(T^{-1/2})\) rate for smooth nonconvex objectives and extends to Lipschitz nonsmooth objectives, achieving the optimal Goldstein-stationarity rate. The paper frames adaptive optimizers such as AdaGrad and Shampoo as preconditioner-selection procedures under static regret.  
   **Why you should care:** It gives a modular theoretical language for adaptive optimizer design, separating gradient prediction from preconditioner learning.

## Section 2: Venue Watch

- **KDD 2026 proceedings / program activity.** ACM has a KDD ’26 proceedings volume corresponding to Cycle 1, while the official KDD site confirms the two-cycle structure, Jeju dates of August 9–13, 2026, and publication through ACM DL; Cycle 2 notifications were May 16 with camera-ready due June 1. The visible arXiv trickle around KDD now includes time-series foundation-model adaptation, node representation “beyond datasets,” and applied data-mining systems. The notable shift is KDD’s broadening from classic graph/data-mining topics into foundation models for structured data, scientific forecasting, agentic systems, and artifact-conscious publication norms. ([doi.org](https://doi.org/10.1145/3770854?utm_source=openai))

- **RLC 2026 / Reinforcement Learning Journal causal-RL cluster.** Two Bareinboim-lab papers now visible in the RLC/RLJ stream—*Scalable Causal Imitation Learning* and *Counterfactual Shapley Credit Assignment*—push causal reasoning into imitation learning and temporal credit assignment. The latter introduces counterfactual Shapley values for separating skill from luck and preserving optimal policies while redistributing rewards for sparse, stochastic, delayed settings. This is worth tracking because RLC is becoming a natural venue for causal sequential-decision work that is too RL-specific for mainstream causal ML venues. ([arxiv.org](https://arxiv.org/abs/2607.17003))

- **Database / data-systems arXiv stream, July 21 snapshot.** The cs.DB recent list shows a dense batch around LLM/data systems, temporal benchmark generation, browser-native GPU query processing, DBMS tuning, inference-aware privacy guidance, recursive Datalog causality, SQL debugging, and transaction-isolation verification. Especially relevant items include SAGA for synthetic temporal graph benchmarks, EvoTune for LLM-assisted memory-aware DBMS tuning, WGLog for WebGPU recursive query processing, and Datalog minimal-support causality. This is not a formal proceedings release, but it is a useful watch signal for where database systems are absorbing ML/agent ideas. ([arxiv.org](https://arxiv.org/list/cs.DB/recent))

## Section 3: Emerging Trends

- **Reliability diagnostics are becoming geometric.** TabPFN topology, multimodal contrastive Jacobian conditioning, KV-cache geometry, and persistent SAE timescales all point to a shift from scalar uncertainty scores toward representation-geometry diagnostics. ([arxiv.org](https://arxiv.org/abs/2607.17962))

- **Causal methods are moving into sequential and operational settings.** Recent papers address causal imitation, counterfactual credit assignment, irregular-time causal discovery, and database-level causality for recursive Datalog. The common thread is causal structure under temporality, feedback, or recursion—not just static treatment effects. ([arxiv.org](https://arxiv.org/abs/2607.17003))

- **Synthetic data is becoming benchmark infrastructure, not only augmentation.** SAGA’s agentic temporal graphs and SGN’s target-guided generation under distribution shift both treat synthetic generation as a way to stress and transfer models under controlled structure. ([arxiv.org](https://arxiv.org/abs/2607.17288))

- **LLMs are entering data management as optimizers, compilers, and metadata/query interfaces.** The database stream now includes LLM-assisted DBMS tuning, semantic operator compilation, natural-language metadata access, and agentic graph generation, suggesting the DB community is moving from “LLM as text-to-SQL” toward deeper system roles. ([arxiv.org](https://arxiv.org/list/cs.DB/recent))

## Section 4: Worth Watching

- **SAGA: Synthetic Agentic Graph Architecture for Temporal Benchmark Generation.** Generates semantically rich temporal graphs with anomaly labels via a skeleton-first, semantics-second pipeline using LLM agents, RAG rule bases, causal time-block partitioning, and temporal replay. Useful for graph anomaly and structured-agent benchmarks. ([arxiv.org](https://arxiv.org/abs/2607.17288))

- **SGN: A Similarity-based Generative Network for Data Generation under Distribution Shift.** A reusable generator trained once on labeled source data and adapted at generation time via a small labeled target representative set, with experiments on image and tabular datasets. Worth suppressing now because it may reappear as a tabular augmentation method. ([arxiv.org](https://arxiv.org/abs/2607.18072))

- **Persistent Sparse Autoencoders.** Adds feature-specific persistence coefficients to SAEs, separating fast local detectors from slow topic-level or monitoring features; the prompt-injection case study makes it relevant to long-context interpretability. ([arxiv.org](https://arxiv.org/abs/2607.17117))

- **EvoTune for DBMS tuning.** Combines lightweight diagnosis, LLM reasoning, utility-aware retrieval, and hierarchical memory for multi-component DBMS tuning, reporting faster convergence and up to 44.5% improvement under the same tuning budget. ([arxiv.org](https://arxiv.org/abs/2607.17841))

- **WGLog browser-native GPU recursive query engine.** A WebGPU system for recursive database queries, using atomic-free sorted-array joins and indirect-dispatch asynchronous execution; surprising because browser execution is beating some native GPU baselines in the reported workloads. ([arxiv.org](https://arxiv.org/abs/2607.17571))

## Section 5: Discord Highlights

**Jul 21 brief**

Top papers:
1. **Topological Signatures of Context-Level Reliability in TabPFN** — persistent homology as a reliability diagnostic for tabular foundation models.
2. **Scalable Causal Imitation Learning** — causal adjustment plus off-policy IRL for long-horizon confounded imitation.
3. **Uncovering Latent Reasoning Strategies in Language Models** — latent-variable factorization of LM reasoning strategies without posterior collapse.
4. **Causal Discovery on Irregular Time Series** — PCMCI+-style causal discovery adapted to irregular event streams.
5. **Optimizing the Preconditioner** — static-regret view of adaptive preconditioning for nonconvex optimization.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-07-21","type":"paper","title":"Topological Signatures of Context-Level Reliability in TabPFN","authors_or_org":"James Hu, Mahdi Ghelichi","url":"https://arxiv.org/abs/2607.17962","memory":"Top 5 paper. Covered July 20 2026 arXiv paper using zigzag persistent homology on TabPFN layer representations to diagnose context-level reliability, topology-induced stress, Bayes error, residuals, and overconfidence on synthetic tabular manifolds/knots/rolls. Suppress arXiv revisions, code, venue versions, or project reposts unless materially expanded."}
{"date_delivered":"2026-07-21","type":"paper","title":"Scalable Causal Imitation Learning","authors_or_org":"Eylam Tagor, Mingxuan Li, Elias Bareinboim","url":"https://arxiv.org/abs/2607.17003","memory":"Top 5 paper and RLC/RLJ 2026 item. Covered causal SQIL and causal IQ-Learn for long-horizon continuous-control imitation learning under observation mismatch and confounded expert demonstrations, using approximate sequential pi-backdoor sliding-window adjustment. Suppress RLC proceedings, RLJ, arXiv revisions, code, and lab-page repeats unless materially changed."}
{"date_delivered":"2026-07-21","type":"paper","title":"Uncovering Latent Reasoning Strategies in Language Models","authors_or_org":"Awni Altabaa, John Lafferty","url":"https://arxiv.org/abs/2607.17674","memory":"Top 5 paper. Covered latent-variable factorization of a pretrained LM response distribution into strategy router and strategy-conditioned generator, using fractional information gain and high-surprisal token reconstruction pressure to avoid posterior collapse. Suppress future versions unless substantially expanded."}
{"date_delivered":"2026-07-21","type":"paper","title":"Causal Discovery on Irregular Time Series","authors_or_org":"Martim Penim, Ricardo Ribeiro Pereira, Jacopo Bono, Hugo Ferreira, Mário A.T. Figueiredo, Pedro Bizarro","url":"https://arxiv.org/abs/2607.18226","memory":"Top 5 paper. Covered July 20 2026 arXiv paper extending PCMCI+ to irregular time series by aggregating causal influence over temporal windows rather than fixed lags; evaluated on synthetic irregular event streams. Suppress revisions/reposts unless materially changed."}
{"date_delivered":"2026-07-21","type":"paper","title":"Optimizing the Preconditioner: A Black-box Online-to-Nonconvex Conversion with Static Regret Minimization Oracles","authors_or_org":"Haichen Hu, David Simchi-Levi","url":"https://arxiv.org/abs/2607.17607","memory":"Top 5 paper. Covered black-box reduction from stochastic nonconvex optimization to ordinary static regret minimization for preconditioner selection, with smooth and Lipschitz nonsmooth rates and adaptive-optimizer interpretation. Suppress future versions unless theory materially changes."}
{"date_delivered":"2026-07-21","type":"proceedings","title":"KDD 2026 ACM proceedings Volume 1 / Cycle 1 publication activity","authors_or_org":"ACM SIGKDD / KDD 2026","url":"https://doi.org/10.1145/3770854","memory":"Venue Watch. Covered ACM DL proceedings Volume 1 for KDD 2026 Cycle 1 and KDD 2026 two-cycle publication context, plus visible arXiv trickle of KDD accepted papers. Suppress repeat broad proceedings awareness; future briefs may cover awards, Volume 2, or specific newly important papers."}
{"date_delivered":"2026-07-21","type":"proceedings","title":"RLC 2026 / Reinforcement Learning Journal causal-RL publication cluster","authors_or_org":"Reinforcement Learning Conference / Reinforcement Learning Journal / Columbia CausalAI Lab","url":"https://www.causalai.net/","memory":"Venue Watch. Covered RLC/RLJ 2026 causal-RL cluster including Scalable Causal Imitation Learning and Counterfactual Shapley Credit Assignment. Suppress repeat cluster summaries; cover new proceedings/awards only if released."}
{"date_delivered":"2026-07-21","type":"proceedings","title":"cs.DB recent database arXiv stream as of July 21 2026","authors_or_org":"arXiv cs.DB","url":"https://arxiv.org/list/cs.DB/recent","memory":"Venue Watch. Covered July 21 cs.DB stream: natural-language metadata access, EvoTune DBMS tuning, WGLog browser GPU recursive queries, SAGA synthetic temporal graph benchmarks, inference-aware privacy, recursive Datalog causality, SQL debugging, isolation checking. Suppress this broad stream snapshot."}
{"date_delivered":"2026-07-21","type":"paper","title":"Counterfactual Shapley Credit Assignment","authors_or_org":"Mingxuan Li, Kaizhan-Lee, Elias Bareinboim","url":"https://arxiv.org/abs/2607.16999","memory":"Individually mentioned in Venue Watch as RLC/RLJ 2026 causal-RL paper using counterfactual Shapley values for RL credit assignment, phi-PPO, and prioritized trajectory replay. Suppress repeat mentions unless selected for Top 5 or materially revised."}
{"date_delivered":"2026-07-21","type":"benchmark","title":"SAGA: Synthetic Agentic Graph Architecture for Temporal Benchmark Generation","authors_or_org":"Jiacheng Ding, Xiaofei Zhang","url":"https://arxiv.org/abs/2607.17288","memory":"Worth Watching. Covered synthetic temporal graph benchmark generation with skeleton-first semantics-second LLM/RAG pipeline, causal time-block partitioning, temporal replay, and anomaly labels for Finance/AML, Network/IDS, Cyber/APT, Transportation. Suppress future arXiv/code/repost unless artifact materially changes."}
{"date_delivered":"2026-07-21","type":"paper","title":"SGN: A Similarity-based Generative Network for Data Generation under Distribution Shift","authors_or_org":"Jiaqi Zhu, Xincheng Chen, Yuncheng Wu, Zhaojing Luo, Beng Chin Ooi","url":"https://arxiv.org/abs/2607.18072","memory":"Worth Watching. Covered reusable target-guided data generator trained once on source labels and applied to shifted domains using a small labeled target representative set, with image and tabular experiments. Suppress future versions unless materially expanded."}
{"date_delivered":"2026-07-21","type":"paper","title":"Persistent Sparse Autoencoders: Learning Feature Timescales in Language Models","authors_or_org":"Haoyan Luo, Mateo Espinosa Zarlenga, Mateja Jamnik","url":"https://arxiv.org/abs/2607.17117","memory":"Worth Watching. Covered SAE variant with learned feature persistence coefficients, separating fast local features from slow topic/monitoring features and prompt-injection long-context case study. Suppress future reposts unless selected for Top 5 or materially changed."}
{"date_delivered":"2026-07-21","type":"software","title":"EvoTune: From Blind Search to Memory-Aware Evolution for DBMS Tuning","authors_or_org":"Zhaoyan Hong, Yishen Sun, Xinyi Zhang, Zhentao Han, Jinhao Dong, Wei Lu, Kai Xu, Liu Tang, Qi Liu, Xiaoyong Du","url":"https://arxiv.org/abs/2607.17841","memory":"Worth Watching and cs.DB Venue Watch. Covered memory-aware evolution framework for multi-component DBMS tuning using collaborative diagnosis, LLM reasoning, utility-aware retrieval, and hierarchical tuning memory. Suppress future arXiv/code/repost unless materially changed."}
{"date_delivered":"2026-07-21","type":"software","title":"WGLog: Terascale Query Processing in the Browser: Rethinking GPU Acceleration","authors_or_org":"Jiaxin Lu, Landon Dyken, Yihao Sun, Kristopher Micinski, Thomas Gilray, Sidharth Kumar","url":"https://arxiv.org/abs/2607.17571","memory":"Worth Watching and cs.DB Venue Watch. Covered browser-native WebGPU engine for recursive database queries using atomic-free sorted-array joins and indirect-dispatch asynchronous execution. Suppress future arXiv/code/venue repeats unless system or evaluation materially changes."}
```