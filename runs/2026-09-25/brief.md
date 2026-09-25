## Section 1: Top 5 Papers

1. **PoEM: Predicting RL Outcomes from Existing Policies**  
   **Authors:** Kimia Hamidieh, Giannis Daras, Antonio Torralba  
   **Venue/source/date:** arXiv cs.LG, new listing on 2026-09-25  
   **Link:** ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   PoEM asks whether a new RL post-training run can be approximated without running RL. The key observation is elegant: when a new reward is a linear combination of existing rewards, the target policy’s log-probabilities can be expressed as a corresponding linear combination of already post-trained log-policies; empirically, even nonlinearly related rewards often lie in a low-rank log-policy subspace. The method estimates combination weights from reward or basis-policy outputs and applies across text and image settings.  
   **Why you should care:** This is a promising “model arithmetic” route for post-training, potentially converting expensive RL sweeps into reusable policy-basis inference.

2. **KathDB-FAO: Synthesized Query Plans in a Multimodal DBMS**  
   **Authors:** Guorui Xiao, Douglas Brown, Artur Borycki, Magdalena Balazinska  
   **Venue/source/date:** arXiv cs.DB, new listing on 2026-09-25  
   **Link:** ([arxiv.org](https://arxiv.org/list/cs.DB/new))  
   KathDB-FAO is a multimodal DBMS query-evaluation subsystem that converts natural-language queries into execution plans whose operators are synthesized functions. Rather than treating LLM calls as opaque row-wise predicates, it extracts fine-grained atomic actions, establishes input/output contracts, groups actions for efficiency, and synthesizes operator bodies during query evaluation. On SemBench, the authors report a 58.8% average execution-cost reduction at comparable or better quality.  
   **Why you should care:** It is another strong signal that the database/LLM interface is moving from prompt interpretation toward compiled, contract-checked semantic operators.

3. **Sufficiently Reduced Distributional Regression**  
   **Authors:** Alexander Henzi, Tiange Liu, Xinwei Shen  
   **Venue/source/date:** arXiv stat.ME/stat.ML/cs.LG, new listing on 2026-09-25  
   **Link:** ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   SRDR unifies conditional distribution estimation with nonlinear sufficient dimension reduction. Its core criterion is based on strictly proper scoring rules: a representation is sufficient when predicting from reduced covariates incurs no expected-score loss relative to full covariates. The proposed generative estimator minimizes the energy score, avoiding density evaluation and adversarial training, and the authors prove convergence of conditional distributions in energy distance.  
   **Why you should care:** This is a clean representation-learning formulation for tabular/scientific regression where “good representation” means preserving the full conditional law, not just point-prediction signal.

4. **Tracking States or Tracking Cosets? An Algebraic Account of Learned State Tracking**  
   **Authors:** Zhiyu Zhang, Yupeng Li  
   **Venue/source/date:** arXiv cs.LG/cs.AI, new listing on 2026-09-25  
   **Link:** ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   This paper studies neural networks trained to track products in finite groups and shows that high or partial accuracy can hide quotient-state solutions. Transformers often recover quotient classes while being nearly uniform within each class; recurrent models pass through richer right-coset stages, including non-normal cosets. The authors connect partial accuracy plateaus, order-blind limits, abelianization, low-dimensional internal subspaces, and causal state swaps.  
   **Why you should care:** It gives a precise algebraic vocabulary for a common interpretability problem: models may track the right abstraction for loss reduction, but not the full latent state we assume.

5. **Direct Message Approximation (DMA): A Consistency-Based Framework for Tractable Approximate Inference on Factor Graphs**  
   **Authors:** Ralf Herbrich, Rainer Schlosser, Jan Lemcke, Johann Ukrow, Anna Kazachkova, Nicolas Alder, Leonhard Hennicke, Theo Bardey, Nico Grimm, Luca Kleinschmidt, Philipp Kolbe, Cezary Kujath, Johanna Schlimme, Karl Matti Schütz  
   **Venue/source/date:** arXiv cs.LG/stat.ML, new listing on 2026-09-25  
   **Link:** ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   DMA revisits approximate inference on factor graphs by approximating factor-to-variable messages directly rather than local marginals. A consistency condition requires exactness when all other incoming messages are Dirac deltas, and a master theorem bounds marginal KL by message KL. The framework avoids EP-style inner loops and negative-precision messages, derives messages for product and leaky-ReLU factors, and yields a one-sweep Bayesian neural-network inference algorithm.  
   **Why you should care:** This is an unusually structural probabilistic-ML paper, relevant to scalable uncertainty methods that do not simply default to variational point estimates or black-box sampling.

## Section 2: Venue Watch

- **arXiv ML/stat/DB stream, 2026-09-25.** The Friday stream was large: cs.LG listed 119 new submissions out of 331 entries, stat.ML listed 18 new submissions out of 54 entries, and cs.DB listed two new submissions out of six entries. The most relevant clusters were post-training without fresh RL, semantic query compilation, task-conditioned observability, representation sufficiency, factor-graph inference, algebraic state tracking, LLM/agent reliability, and time-series foundation-model evaluation under data revisions. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **TMLR September 2026 accepted-paper stream, incremental update.** The top of the TMLR accepted list now shows fresh September additions beyond the last snapshot: intervention timing for always-on AI assistants; cross-layer discrete concept discovery; preference distillation for bridging offline and iterative alignment; approximate actual-cause search; AutoMIA; task-intrinsic representation geometry in modular arithmetic; artificial uncertainty induction; graph-orbit learning in Hopfield networks; MeritKV for KV-cache reuse; and inverse problems conditioned on observation ensembles. This batch continues TMLR’s September pattern: interpretability, privacy attacks, agent systems, uncertainty, and efficient serving are now central rather than peripheral. ([jmlr.org](https://jmlr.org/tmlr/papers/))

- **JASA Volume 121 Issue 554, current issue.** JASA’s current issue continues the “Statistical Science in Artificial Intelligence” special-issue arc, with articles on AI-powered Bayesian generative modeling for causal inference, mini-batch estimation for deep Cox models, low-rank contextual RL from heterogeneous human feedback, active learning for data labeling, EHR phenotyping, network regression, individualized variable selection, network interference, and a review article on physics-informed neural networks. ([tandfonline.com](https://www.tandfonline.com/toc/uasa20/current/?utm_source=openai))

## Section 3: Emerging Trends

- **Semantic databases are becoming compilation systems.** KathDB-FAO, plus the recent run of AI-query compilation and semantic-operator papers, suggests the field is converging on contract extraction, operator synthesis, and cost-aware execution rather than row-wise LLM invocation.

- **Post-training is shifting from “run another RL job” to “reuse geometry.”** PoEM predicts target RL policies from existing post-trained policies; MISVO uses local Fisher/KL geometry for steering; TMLR now has multiple alignment, uncertainty, and function-calling security items in the same stream.

- **Representation evaluation is becoming more algebraic and task-conditional.** Coset-tracking, SRDR, FBDM, task-conditioned observability, and modular-arithmetic geometry all ask: which equivalence classes or sufficient quotients does the model actually learn?

- **Time-series foundation-model evaluation is getting more realistic.** VINTAGE-TS emphasizes observation time versus information-availability time; SGA targets multi-step forecast-branch uncertainty; recent TSFM work increasingly treats leakage, revisions, and multivariate dependence as first-order issues.

## Section 4: Worth Watching

- **VINTAGE-TS: Time-Series Foundation Models That Understand Data Revisions.** A revision-aware TSFM evaluation/adaptation framework for ALFRED-style macroeconomic data that separates observation time from availability time and audits hindsight contamination; no real Chronos-2 experiment is claimed yet. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **LIMBO / “Where Does Exactly-Once Live?”** A deterministic sandbox for duplicate side effects in tool-using agents, spanning six services, twelve fault modes, nine models, and production harnesses; useful for agent transaction semantics and write-safety benchmarks. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **Minimally Invasive Steering of Language Models.** MISVO optimizes pre-logit interventions with a Fisher/KL penalty and reports reward gains while preserving diversity/coherence; relevant to inference-time alignment and steering without parameter updates. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **Flow-Based Distribution Matching for SSL representations.** FBDM replaces adversarial distribution matching with spherical conditional velocity regression toward explicit geometric references, with downstream error bounds tied to pretraining loss. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **Sequential Confidence Sets for Coverage-Constrained Conformal Model Selection.** CC-SMCS gives finite-sample, anytime-valid confidence sets for selecting efficient conformal pipelines subject to coverage constraints, including delayed multi-horizon feedback. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

## Section 5: Discord Highlights

**Sep 25 brief — Top 5 papers**

1. **PoEM: Predicting RL Outcomes from Existing Policies** — approximates new RL post-training outcomes from a basis of already post-trained policies.  
2. **KathDB-FAO** — synthesizes contract-checked semantic query plans inside a multimodal DBMS.  
3. **Sufficiently Reduced Distributional Regression** — learns sufficient representations for full conditional distributions via proper scoring rules.  
4. **Tracking States or Tracking Cosets?** — shows models may track quotient/coset abstractions rather than full latent state.  
5. **Direct Message Approximation** — new factor-graph inference framework approximating messages directly with KL guarantees.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-09-25","type":"paper","title":"PoEM: Predicting RL Outcomes from Existing Policies","authors_or_org":"Kimia Hamidieh, Giannis Daras, Antonio Torralba","url":"https://arxiv.org/abs/2609.30226","memory":"Top 5 paper. Covered Sep 25 2026 arXiv paper predicting RL post-training outcomes from existing post-trained policies via low-rank/log-policy combination across rewards. Suppress future arXiv/code/venue/social reposts unless method or empirical scope materially changes."}
{"date_delivered":"2026-09-25","type":"paper","title":"KathDB-FAO: Synthesized Query Plans in a Multimodal DBMS","authors_or_org":"Guorui Xiao, Douglas Brown, Artur Borycki, Magdalena Balazinska","url":"https://arxiv.org/abs/2609.28761","memory":"Top 5 paper. Covered multimodal DBMS subsystem that converts natural-language queries into synthesized function-operator execution plans with contracts and grouped atomic actions; SemBench cost reduction claims. Suppress arXiv/code/venue reposts unless system or evaluation materially expands."}
{"date_delivered":"2026-09-25","type":"paper","title":"Sufficiently Reduced Distributional Regression","authors_or_org":"Alexander Henzi, Tiange Liu, Xinwei Shen","url":"https://arxiv.org/abs/2609.29291","memory":"Top 5 paper. Covered SRDR, a conditional distribution estimation plus nonlinear sufficient dimension reduction framework using proper scoring rules and energy-score training, with convergence in energy distance. Suppress future arXiv/code/venue versions unless theory or empirical scope materially changes."}
{"date_delivered":"2026-09-25","type":"paper","title":"Tracking States or Tracking Cosets? An Algebraic Account of Learned State Tracking","authors_or_org":"Zhiyu Zhang, Yupeng Li","url":"https://arxiv.org/abs/2609.29951","memory":"Top 5 paper. Covered algebraic account of state tracking in finite groups, quotient/coset solutions, Transformers versus recurrent networks, abelianization plateaus, and causal state swaps. Suppress arXiv/code/venue/social reposts unless theory or experiments materially expand."}
{"date_delivered":"2026-09-25","type":"paper","title":"Direct Message Approximation (DMA): A Consistency-Based Framework for Tractable Approximate Inference on Factor Graphs","authors_or_org":"Ralf Herbrich, Rainer Schlosser, Jan Lemcke, Johann Ukrow, Anna Kazachkova, Nicolas Alder, Leonhard Hennicke, Theo Bardey, Nico Grimm, Luca Kleinschmidt, Philipp Kolbe, Cezary Kujath, Johanna Schlimme, Karl Matti Schütz","url":"https://arxiv.org/abs/2609.29466","memory":"Top 5 paper. Covered direct factor-to-variable message approximation framework for factor graphs, consistency condition, master KL theorem, no EP inner loop, product/leaky-ReLU messages, and one-sweep BNN inference. Suppress future arXiv/code/venue versions unless inference framework materially changes."}
{"date_delivered":"2026-09-25","type":"proceedings","title":"arXiv cs.LG/stat.ML/cs.DB new-submission stream for September 25 2026","authors_or_org":"arXiv cs.LG, stat.ML, cs.DB","url":"https://arxiv.org/list/cs.LG/new","memory":"Venue Watch. Covered Sep 25 2026 streams: cs.LG 119 new submissions out of 331 entries, stat.ML 18 new out of 54, cs.DB two new out of six; themes in post-training, semantic query compilation, observability, representation sufficiency, probabilistic inference, algebraic state tracking, and agent reliability. Suppress repeat daily stream summary."}
{"date_delivered":"2026-09-25","type":"proceedings","title":"TMLR September 2026 accepted papers incremental update as of September 25","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered visible Sep 25 TMLR top-of-page additions including always-on assistant intervention timing survey, cross-layer discrete concept discovery, preference distillation, actual-cause search, AutoMIA, modular-arithmetic representation geometry, artificial uncertainty, graph-orbit Hopfield learning, MeritKV, and observation-conditioned inverse problems. Suppress repeat Sep 25 incremental snapshot."}
{"date_delivered":"2026-09-25","type":"venue_issue","title":"Journal of the American Statistical Association Volume 121 Issue 554","authors_or_org":"Journal of the American Statistical Association / Taylor & Francis / ASA","url":"https://www.tandfonline.com/toc/uasa20/current","memory":"Venue Watch. Covered current JASA Vol 121 Issue 554, continuing Statistical Science in AI special-issue content: Bayesian generative causal inference, deep Cox mini-batch theory, low-rank contextual RL from heterogeneous feedback, active learning, EHR phenotyping, network regression/interference, individualized variable selection, and PINN review. Suppress repeat issue summary."}
{"date_delivered":"2026-09-25","type":"resource","title":"VINTAGE-TS: Time-Series Foundation Models That Understand Data Revisions","authors_or_org":"Taimoor Ahmad","url":"https://arxiv.org/abs/2609.28576","memory":"Worth Watching. Covered revision-aware TSFM evaluation/adaptation framework distinguishing observation time from information-availability time, ALFRED rolling evaluation plan, delayed-label filtering, and hindsight-contamination audit; no real ALFRED/Chronos-2 results claimed. Suppress future arXiv/code reposts unless real experiments or framework materially expand."}
{"date_delivered":"2026-09-25","type":"benchmark","title":"LIMBO / Where Does Exactly-Once Live? Model, Harness, and Tool-Contract Effects on Duplicate Side Effects in LLM Agents","authors_or_org":"Jiapeng Li","url":"https://arxiv.org/abs/2609.29095","memory":"Worth Watching. Covered deterministic sandbox for duplicate side effects in tool-using agents with six services, twelve fault modes, nine models, three harnesses, and contract variants; relevant to exactly-once semantics and agent transactions. Suppress future arXiv/code/benchmark mentions unless artifact or results materially expand."}
{"date_delivered":"2026-09-25","type":"paper","title":"Minimally Invasive Steering of Language Models","authors_or_org":"Taha Entesari, Jingyu Zhang, Daniel Khashabi, Mahyar Fazlyab","url":"https://arxiv.org/abs/2609.30218","memory":"Worth Watching. Covered MISVO, Fisher/KL-regularized pre-logit steering of frozen language models with analytic gradient/surrogate decomposition and preference/code-generation experiments. Suppress future arXiv/code/venue/social reposts unless method or empirical evidence materially changes."}
{"date_delivered":"2026-09-25","type":"paper","title":"Learning a Flow to Self-Supervised Representations","authors_or_org":"Yuling Jiao, Wensen Ma, Houduo Qi, Defeng Sun","url":"https://arxiv.org/abs/2609.29350","memory":"Worth Watching. Covered Flow-Based Distribution Matching for SSL, a non-adversarial spherical conditional velocity regression approach to explicit geometric representation references with downstream error bounds. Suppress future arXiv/code/venue reposts unless theory or experiments materially expand."}
{"date_delivered":"2026-09-25","type":"paper","title":"Sequential Confidence Sets for Coverage-Constrained Conformal Model Selection","authors_or_org":"Jing Li, Haibin Zhu","url":"https://arxiv.org/abs/2609.28522","memory":"Worth Watching. Covered CC-SMCS for anytime-valid sequential selection of efficient conformal forecasting pipelines under prefix-average conditional miscoverage constraints, delayed feedback, and coverage-boundary impossibility. Suppress future arXiv/code/venue mentions unless guarantees or applications materially change."}
```