## Section 1: Top 5 Papers

1. **Why Large Language Models Fail at Tabular Prediction**  
   **Authors:** Marta Garnelo, Wojciech M. Czarnecki  
   **Venue/source/date:** arXiv, submitted August 3, 2026  
   **Link:** https://arxiv.org/abs/2608.02412  
   This is the cleanest recent diagnostic of the “why not just prompt an LLM with the table?” question. The authors test a frontier LLM in a single-pass, no-tools, no-fine-tuning regime and evaluate five plausible failure hypotheses. Four are largely falsified: noise/nonlinearity, CSV linearization, numeric tokenization, and multiple test points per query. Dimensionality is the culprit: across random projections of 31 benchmark datasets, the LLM is the only method among nine whose accuracy falls as dimension grows. In 2D it resembles local distance-based classifiers; in higher dimensions its behavior becomes unlike tuned classical learners. ([arxiv.org](https://arxiv.org/abs/2608.02412))  
   **Why you should care:** It reframes tabular foundation models as solving a genuinely different inductive-bias problem, not merely a context-window or serialization problem.

2. **Causal Inference with Unstructured Treatments**  
   **Authors:** Kevin Christian Wibisono, Yixin Wang  
   **Venue/source/date:** arXiv, submitted August 1, 2026  
   **Link:** https://arxiv.org/abs/2608.00657  
   The paper tackles causal effects where the “treatment” is not a scalar or finite action but a text, image, or clinical decision sequence. Instead of asking for the effect of setting the whole treatment to one exact value, which is usually nonrecurring and scientifically unhelpful, it defines the **maximally influential feature**: a binary feature of the treatment, chosen under population-balance constraints, that induces the largest causal effect. The authors give identification conditions, estimation algorithms, and a nudging procedure that edits a treatment along the learned causal feature direction. ([arxiv.org](https://arxiv.org/abs/2608.00657))  
   **Why you should care:** This is a strong conceptual bridge between representation learning, causal estimands, and actionable interventions on language/image/sequence objects.

3. **On the Identifiability of Masked Prediction: Mode Blindness and Mask Schedules**  
   **Authors:** Yichao Cai, Javen Qinfeng Shi  
   **Venue/source/date:** arXiv, submitted August 2, 2026  
   **Link:** https://arxiv.org/abs/2608.01383  
   This theory paper asks when masked-prediction objectives identify the underlying joint distribution. For two separated global modes, the answer can depend almost entirely on the mask schedule: masks dominated by large visible contexts can be exponentially insensitive to global mode weights, allowing constant total-variation errors despite tiny excess masked-prediction risk. The paper introduces an identifiability modulus, decomposes the relevant information terms, and shows that low-visibility masks or positive full-mask mass can restore identifiability. The experiments span enumerated laws, gradient-trained models, and natural text diagnostics. ([arxiv.org](https://arxiv.org/abs/2608.01383))  
   **Why you should care:** It gives a precise failure mode for self-supervised learning objectives that may matter for masked tabular, language, and multimodal pretraining.

4. **Private Generative Bootstrap via Blocking**  
   **Authors:** Jinwon Sohn, Veronika Ročková  
   **Venue/source/date:** arXiv, submitted August 3, 2026  
   **Link:** https://arxiv.org/abs/2608.02480  
   The paper proposes a differentially private Bayesian-bootstrap mechanism for uncertainty quantification. Instead of assigning random weights to individuals, it groups observations into blocks and assigns block-level weights, concealing individual contributions. A private amortized map from observation weights to posterior samples is learned once; subsequent posterior draws consume no additional privacy or computation budget. The authors prove a DP guarantee, convergence to the blocked-bootstrap target, discrepancy bounds relative to the ordinary Bayesian bootstrap, and a data-free tuning rule for block concentration. Applications include Census returns-to-schooling and natality quantile estimation. ([arxiv.org](https://arxiv.org/abs/2608.02480))  
   **Why you should care:** It is a rare synthesis of Bayesian nonparametric uncertainty, generative amortization, and differential privacy that could influence private synthetic-data inference.

5. **Computational and Statistical Guarantees of the c-Rectified Flow**  
   **Authors:** Leda Wang, Zhehao Xu, Qiang Liu, Harrison H. Zhou  
   **Venue/source/date:** arXiv, submitted August 3, 2026  
   **Link:** https://arxiv.org/abs/2608.02487  
   Rectified flow is now central to modern generative modeling, but its iterative guarantees remain underdeveloped. This paper studies **c-rectified flow**, a cost-aware variant that projects velocity fields onto a gradient class while preserving endpoint marginals. A Gaussian case study shows ordinary rectified flow recovers the optimal-transport coupling only when source and target covariances commute; the c-rectified variant converges to the OT coupling under compactness and uniform-integrability assumptions. The paper adds one-step contraction, exponential convergence, and minimax-optimal score-estimation rates under Hölder assumptions. ([arxiv.org](https://arxiv.org/abs/2608.02487))  
   **Why you should care:** It is the kind of foundational transport/flow result that can shape the theory of diffusion, flow matching, and synthetic-data generators.

## Section 2: Venue Watch

- **arXiv August 4 stream: tabular FMs, causal/statistical learning, and data systems.** The August 4 cs.LG page shows 340 new entries and the stat.ML page shows 31 entries; the relevant clusters are unusually aligned with Adam’s interests: LLMs on tabular prediction, few-shot tabular generation, active feature acquisition, test-time latent optimization, masked-prediction identifiability, Bayesian/private bootstrap, and transport/flow theory. The cs.DB stream has 16 entries, with a strong systems tilt: token-native storage for agents, range-filtered ANNS, Parquet datapath acceleration, dependency discovery, and time-series database benchmarking. ([arxiv.org](https://arxiv.org/list/cs.LG/recent))

- **KDD 2026 is about to enter conference mode.** The schedule-at-a-glance now exposes the event rhythm: workshops on August 9–10, opening session and awards on August 9, and main-conference programming beginning August 11 with Jeff Dean’s opening keynote, Korea Day, Data Day, dissertation awards, Test-of-Time awards, and oral sessions across Applied Data Science, AI for Science, BlueSky, and Data Benchmark & Research tracks. ([kdd2026.kdd.org](https://kdd2026.kdd.org/schedule-at-a-glance/?utm_source=openai))

- **KDD Cup 2026 Data Agents final results are out.** The DataAgent-Bench competition now reports Phase-2 final results, with awarded teams in both the leaderboard and creative tracks. Since this benchmark directly targets agents doing complex analysis over heterogeneous structured packages, the post-competition artifacts and winning reports are worth watching for reusable data-agent evaluation protocols. ([dataagent.top](https://dataagent.top/?utm_source=openai))

- **M&SOM Volume 28 Issue 4, July–August 2026.** The current issue is newly visible relative to the previously covered May–June issue. Themes include ML-guided cancer-screening outreach, volunteer retention, nonlinear delivery-time effects, contextual stochastic optimization for omnichannel fulfillment under delivery uncertainty, flexible data aggregation for retail prediction and decisions, data-driven pricing with multiple binary choice and copulas, social learning/influence, equipment rental/service design, and robust generator maintenance. ([pubsonline.informs.org](https://pubsonline.informs.org/toc/msom/current))

## Section 3: Emerging Trends

- **The “LLMs versus tables” debate is splitting into diagnosis and engineering.** One branch is showing why generic LLMs fail on tabular prediction; another is making specialized tabular models faster and more deployable.

- **Self-supervised objectives are being audited at the distributional level.** The masked-prediction identifiability paper is a reminder that low loss on conditional prediction can still hide global distributional blindness.

- **Causal ML is moving toward object-valued interventions.** Unstructured treatments, spatiotemporal proximal methods, and causal data-science agents all point to causal estimands over representations, sequences, text, and spatial graphs.

- **Private uncertainty is becoming generative.** The private generative bootstrap treats posterior simulation itself as a privatized, amortized object—an appealing pattern for private synthetic-data inference.

- **Agentic data systems are becoming a real venue theme.** KDD Cup Data Agents, token-native storage, bitemporal/graph memory, and structured-data agent workshops all converge on the same question: what database primitives should exist when agents are the primary users?

## Section 4: Worth Watching

- **LAB-Tab: LLM-Augmented Bayesian Network Adaptation for Few-Shot Tabular Generation.** Source-aware few-shot tabular synthesis: fit a source BN, let an LLM propose target-domain edges, and use PPO edge actions to calibrate the augmented structure. Promising because it makes LLM prior knowledge an explicit structural hypothesis rather than an opaque generator. ([arxiv.org](https://arxiv.org/abs/2608.01879))

- **TabDPT-Turbo / TabDPT v1.2.** A row-attention, long-context-pretrained tabular in-context learner that claims comparable default performance to TabDPT v1.1 while being orders of magnitude faster and released as TabDPT v1.2. Suppress future repeats unless the public model or benchmarks change materially. ([arxiv.org](https://arxiv.org/abs/2608.01400))

- **Token-Native Storage.** A provocative database-systems proposal: store text as BPE token IDs rather than UTF-8 for agent/LLM workloads, giving smaller storage and avoiding repeated retokenization. The standardization argument may matter more than the current prototype numbers. ([arxiv.org](https://arxiv.org/abs/2608.02376))

- **BRiG-AFA: Bellman Risk-to-Go Learning for Non-Myopic Active Feature Acquisition.** A supervised Bellman-regression alternative to greedy active feature acquisition; useful for settings where measurement costs and partially observed tabular records matter. ([arxiv.org](https://arxiv.org/abs/2608.02305))

- **RaG-Tree for multi-attribute range-filtered ANNS.** Combines R-tree partitions with partition-aware HNSW graphs for vector search under multiple attribute constraints, including adaptive search and incremental updates. Relevant to structured retrieval and semantic query systems. ([arxiv.org](https://arxiv.org/abs/2608.01255))

## Section 5: Discord Highlights

**Aug 4 brief — Top 5 papers**

1. **Why Large Language Models Fail at Tabular Prediction** — dimensionality, not CSV formatting or tokenization, explains much of generic LLM failure on tables.  
2. **Causal Inference with Unstructured Treatments** — defines actionable causal features for text/image/sequence treatments.  
3. **On the Identifiability of Masked Prediction** — mask schedules can make SSL objectives blind to global mode weights.  
4. **Private Generative Bootstrap via Blocking** — amortized private Bayesian-bootstrap sampling with reusable posterior draws.  
5. **Computational and Statistical Guarantees of the c-Rectified Flow** — convergence and minimax guarantees for a cost-aware rectified-flow variant.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-08-04","type":"paper","title":"Why Large Language Models Fail at Tabular Prediction","authors_or_org":"Marta Garnelo, Wojciech M. Czarnecki","url":"https://arxiv.org/abs/2608.02412","memory":"Top 5 paper. Covered Aug 3 2026 arXiv paper diagnosing generic LLM failure on tabular prediction; controlled tests falsify noise/nonlinearity, CSV structure, numeric tokenization, and multiple-test-point hypotheses, finding dimensionality decisive. Suppress future arXiv/repost/code/venue mentions unless materially revised."}
{"date_delivered":"2026-08-04","type":"paper","title":"Causal Inference with Unstructured Treatments","authors_or_org":"Kevin Christian Wibisono, Yixin Wang","url":"https://arxiv.org/abs/2608.00657","memory":"Top 5 paper. Covered Aug 1 2026 arXiv stat.ML paper defining maximally influential feature causal query for text/image/clinical-sequence treatments, with identification, estimation, and nudging algorithms. Suppress future versions unless theory or empirical scope materially changes."}
{"date_delivered":"2026-08-04","type":"paper","title":"On the Identifiability of Masked Prediction: Mode Blindness and Mask Schedules","authors_or_org":"Yichao Cai, Javen Qinfeng Shi","url":"https://arxiv.org/abs/2608.01383","memory":"Top 5 paper. Covered Aug 2 2026 arXiv theory paper on masked-prediction identifiability, mode blindness, epsilon-identifiability modulus, mask schedules, low-visibility masks, and full-mask anchoring. Suppress future arXiv/venue/code reposts unless materially changed."}
{"date_delivered":"2026-08-04","type":"paper","title":"Private Generative Bootstrap via Blocking","authors_or_org":"Jinwon Sohn, Veronika Ročková","url":"https://arxiv.org/abs/2608.02480","memory":"Top 5 paper. Covered Aug 3 2026 arXiv paper on differentially private generative Bayesian bootstrap using blocked weights, amortized posterior sampling, privacy guarantees, convergence/discrepancy analysis, and applications to Census/natality uncertainty. Suppress future versions unless materially revised."}
{"date_delivered":"2026-08-04","type":"paper","title":"Computational and Statistical Guarantees of the c-Rectified Flow","authors_or_org":"Leda Wang, Zhehao Xu, Qiang Liu, Harrison H. Zhou","url":"https://arxiv.org/abs/2608.02487","memory":"Top 5 paper. Covered Aug 3 2026 arXiv paper proving convergence, contraction, exponential convergence, and minimax score/OT estimation guarantees for cost-aware c-rectified flow; includes Gaussian failure case for ordinary rectified flow. Suppress future reposts unless theory materially changes."}
{"date_delivered":"2026-08-04","type":"proceedings","title":"arXiv cs.LG/stat.ML/cs.DB recent stream snapshot for August 4 2026","authors_or_org":"arXiv cs.LG, stat.ML, cs.DB","url":"https://arxiv.org/list/cs.LG/recent","memory":"Venue Watch. Covered Aug 4 2026 arXiv streams: 340 cs.LG entries, 31 stat.ML entries, 16 cs.DB entries, with clusters in tabular LLM diagnosis, tabular generation, active feature acquisition, masked-prediction identifiability, private Bayesian bootstrap, flow/transport theory, token-native storage, ANNS, Parquet datapath acceleration, and database benchmarking. Suppress this daily broad stream snapshot."}
{"date_delivered":"2026-08-04","type":"announcement","title":"KDD 2026 schedule-at-a-glance / conference-mode program awareness","authors_or_org":"ACM SIGKDD / KDD 2026","url":"https://kdd2026.kdd.org/schedule-at-a-glance/","memory":"Venue Watch. Covered KDD 2026 schedule-at-a-glance: workshops Aug 9-10, opening session and awards Aug 9, main conference Aug 11 with Jeff Dean keynote, Korea Day, Data Day, dissertation awards, Test-of-Time awards, and oral tracks. Suppress repeat schedule awareness unless awards/results/proceedings change."}
{"date_delivered":"2026-08-04","type":"benchmark","title":"KDD Cup 2026 Data Agents for Complex Data Analysis Phase-2 final results","authors_or_org":"KDD Cup 2026 / DataAgent-Bench organizers","url":"https://dataagent.top/","memory":"Venue Watch. Covered July 15 2026 Phase-2 final results release for Data Agents / DataAgent-Bench, with awarded teams in Leaderboard and Creative tracks. Suppress repeat final-results announcements; future runs may cover winning solution reports or released technical artifacts."}
{"date_delivered":"2026-08-04","type":"venue_issue","title":"Manufacturing & Service Operations Management Volume 28 Issue 4 July-August 2026","authors_or_org":"INFORMS Manufacturing & Service Operations Management","url":"https://pubsonline.informs.org/toc/msom/current","memory":"Venue Watch. Covered current M&SOM July-August 2026 issue themes: ML-guided cancer screening outreach, volunteer retention, delivery-time demand effects, contextual stochastic omnichannel fulfillment, flexible data aggregation for retail decisions, data-driven pricing with binary choice/copulas, influence/social learning, equipment rental design, robust generator maintenance. Suppress repeat issue summary."}
{"date_delivered":"2026-08-04","type":"paper","title":"LAB-Tab: LLM-Augmented Bayesian Network Adaptation for Few-Shot Tabular Generation","authors_or_org":"Zijian Shen, Taijie Chen, Bin Zhou, Ziyang Jiang, Jintao Ke","url":"https://arxiv.org/abs/2608.01879","memory":"Worth Watching. Covered Aug 3 2026 arXiv paper on source-aware few-shot tabular generation using source BN, LLM-proposed target-domain edges, PPO edge actions, and ACS distribution-shift scenarios. Suppress future arXiv/code/venue reposts unless materially revised."}
{"date_delivered":"2026-08-04","type":"software","title":"TabDPT-Turbo / TabDPT v1.2: Efficient In-Context Learning for Tabular Prediction","authors_or_org":"Rasa Hosseinzadeh, Alex Labach, Zexin Xue, Shuyi Han, Valentin Thomas, Anthony L. Caterini","url":"https://arxiv.org/abs/2608.01400","memory":"Worth Watching. Covered Aug 2 2026 arXiv / FMSD workshop paper and model release described as TabDPT v1.2: row-attention, long-context pretraining, SSL on larger real-data corpus, comparable to TabDPT v1.1 with much faster inference. Suppress future repo/model-card/repost mentions unless version or benchmark evidence materially changes."}
{"date_delivered":"2026-08-04","type":"paper","title":"Token-Native Storage: Read and Write in your Agent's Language","authors_or_org":"Kumar Shivendu","url":"https://arxiv.org/abs/2608.02376","memory":"Worth Watching. Covered Aug 3 2026 cs.DB paper proposing storage of text as BPE token IDs for LLM/agent workloads, with compression and retokenization-speed arguments plus tokenizer standardization proposal. Suppress future arXiv/repost mentions unless system or standardization artifact materially changes."}
{"date_delivered":"2026-08-04","type":"paper","title":"BRiG-AFA: Bellman Risk-to-Go Learning for Non-Myopic Active Feature Acquisition","authors_or_org":"Jiaorong Feng, Qian Li, Ying Li","url":"https://arxiv.org/abs/2608.02305","memory":"Worth Watching. Covered Aug 3 2026 arXiv paper on supervised Bellman risk-to-go learning for active feature acquisition under measurement budgets; non-myopic benchmark, Fashion-MNIST, and MiniBooNE results. Suppress future versions unless substantially expanded."}
{"date_delivered":"2026-08-04","type":"paper","title":"RaG-Tree: Combining R-Tree and HNSW for Multi-Attribute Range Filtered Approximate Nearest Neighbor Search","authors_or_org":"Jiawei Liu, Xiang Zhang, Chao Zhang, Ju Fan, Xiaoyong Du","url":"https://arxiv.org/abs/2608.01255","memory":"Worth Watching. Covered Aug 2 2026 cs.DB paper on multi-attribute range-filtered ANNS combining R-tree partitions with partition-aware HNSW graphs, adaptive search, and incremental update maintenance. Suppress future arXiv/venue/code reposts unless materially changed."}
```