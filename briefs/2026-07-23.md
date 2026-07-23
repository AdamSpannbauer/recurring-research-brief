## Section 1: Top 5 Papers

1. **Auto-Fill: Learning to Predict Missing Values Accurately with Specialist Language Models**  
   **Authors:** Yurong Liu, Yeye He, Haoyu Dong, Junjie Xing, Shi Han, Dongmei Zhang, Surajit Chaudhuri  
   **Venue/source:** arXiv; comments indicate VLDB 2026  
   **Release date:** July 22, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2607.19847))  
   **Summary:** Auto-Fill targets a practically important but under-theorized tabular problem: predicting missing cells in real tables with high precision rather than merely plausible completions. The paper’s core judgment is that frontier reasoning models are too costly and too overconfident for data-cleaning deployment. It decomposes the task into three capabilities—world knowledge, text reasoning, and code reasoning—and post-trains specialist small language models for each, then uses a calibrated ensemble that can abstain. Across 11 benchmarks and 2,200 real tables, it reports better accuracy than o3-pro, Gemini 3 Pro, and DeepSeek R1 at under 1% of their cost.  
   **Why you should care:** This is a strong data-management counterpoint to “just use a frontier model”: specialization plus abstention may be the right abstraction for reliable tabular AI.

2. **Data-Poisoning Audits for Causal Effect Estimation**  
   **Authors:** Kwangho Kim  
   **Venue/source:** arXiv  
   **Release date:** July 22, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2607.19692))  
   **Summary:** This paper asks a sharp question for observational causal pipelines: how much can an attacker move an estimated treatment effect by appending plausible-looking records? For augmented inverse-propensity-weighted estimation, the analyst specifies feasible record catalogs, append budgets, and source capacities; the adversary chooses records to maximize directional movement. With nuisance fits fixed, the paper gives an exact finite-sample greedy scan over append budgets; with refitting, it derives a total-influence score and conservative finite-budget bounds. The result is an audit curve for causal estimates, not merely a generic robustness metric.  
   **Why you should care:** It reframes causal sensitivity analysis around data-composition attacks, directly relevant to pooled multi-site observational studies and synthetic/public-data augmentation.

3. **Total Variation Distance Estimation in Autoregressive Models**  
   **Authors:** Eric Price, Kevin Tian, Zhiyang Xun, Yusong Zhu  
   **Venue/source:** arXiv  
   **Release date:** July 21, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2607.19510))  
   **Summary:** The paper studies how to estimate total variation distance between two length-\(n\) autoregressive distributions under sample, logit, and noisy-logit access. Motivation is concrete: two serving stacks with the “same” weights can differ because of batching, kernels, quantization, or inference optimizations. The authors improve sample-access complexity over prior estimators, prove tight \(O(n/\epsilon^2)\) logit-access bounds, and give a noisy-logit interpolation. Empirically, they estimate distances between systems such as SGLang and vLLM serving identical weights, arguing TV remains useful when KL is infinite.  
   **Why you should care:** This is a credible evaluation primitive for model-serving reproducibility and distributional equivalence, not just another benchmark score.

4. **Bayesian Wind Tunnels for Model Selection**  
   **Authors:** Siddhartha R. Dalal, Vishal Misra, Abhay Parekh  
   **Venue/source:** arXiv  
   **Release date:** July 1, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2607.19379))  
   **Summary:** This paper builds controlled “wind tunnels” where exact Bayesian posteriors over hypothesis classes are available, then tests whether transformers can do Bayesian model selection rather than merely filtering within a fixed class. A small transformer closely matches the Bayesian posterior for relational hypotheses such as fixed-point-free involutions and non-nested alternatives like involutions versus 3-cycles. The key negative result is equally interesting: when model selection requires arithmetic over opaque symbols, scaling from 2.8M to 316M parameters does not fix the failure; stable semantics enable circuit compilation.  
   **Why you should care:** It gives a crisp experimental grammar for studying in-context Bayesian reasoning, representation access, and what “model selection” means inside transformers.

5. **Statistical Inference for Rank Allocation in Low-Rank Adaptation**  
   **Authors:** Yihang Gao, Vincent Y. F. Tan  
   **Venue/source:** arXiv  
   **Release date:** July 22, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2607.20205))  
   **Summary:** StatLoRA turns LoRA rank allocation into a hypothesis-testing problem. Instead of heuristic gradient-sensitivity scores, each LoRA component receives a statistic and p-value used to retain or prune components under a rank budget. The technical contribution is central-limit theory for stochastic optimizer trajectories, including AdamW, enabling asymptotic distributions for component scores. Experiments on DeBERTaV3-base, BART-Large, and Qwen2.5-7B show comparable or better performance than vanilla LoRA, AdaLoRA, and IGU-LoRA under matched budgets, with diagnostics supporting the asymptotic score theory.  
   **Why you should care:** It is a rare attempt to put statistical inference back into parameter-efficient adaptation decisions.

## Section 2: Venue Watch

- **AISTATS 2026 awards and program closure.** AISTATS 2026 was held May 2–5 in Tangier, and the virtual site now foregrounds the award winners: Best Paper went to **“EventFlow: Forecasting Temporal Point Processes with Flow Matching”**; Best Student Paper to **“We Still Don’t Understand High-Dimensional Bayesian Optimization”**; Test of Time to Jamieson and Talwalkar’s **“Non-stochastic Best Arm Identification and Hyperparameter Optimization”**; and Test-of-Time Honorable Mention to **“Deep Kernel Learning.”** This is a useful signal that the statistics/ML community is still rewarding temporal point processes, Bayesian optimization skepticism, and older Bayesian deep-learning bridges. ([virtual.aistats.org](https://virtual.aistats.org/))

- **TMLR July 2026 accepted-paper stream continued to fill in after the earlier July snapshot.** New visible July entries include **Synth-FAR** for synthetic frequency-autoregressive time-series forecasting, a mechanistic analysis of low-precision microscaling-format instabilities, generalized Dirichlet energy and graph Laplacians for clustering, scalable concept-driven question generation, and low-dimensional sign-activation networks as convex lasso models. Treat this as an incremental TMLR update, not a repeat of the earlier July batch: the notable shift is toward time-series generation, numerical representation/precision analysis, and graph spectral methods. ([jmlr.org](https://jmlr.org/tmlr/papers/))

- **arXiv cs.LG/stat.ML July 23 stream: evaluation, adaptation, and reliability-heavy.** The July 23 cs.LG stream listed 160 new entries; among the relevant clusters were tabular missing-value prediction, LoRA rank inference, causal audits, TV-distance evaluation for autoregressive models, time-series foundation-model post-training, local causal discovery under latent variables/selection bias, and online Bayesian expert aggregation. The stat.ML slice was smaller but concentrated around Bayesian online learning, LoRA inference, causal-effect poisoning audits, optimal recalibration, and SGLD variants. ([arxiv.org](https://arxiv.org/list/cs.LG/recent))

- **arXiv cs.DB July 23 stream: benchmarking full data-system pipelines.** The database stream was compact but high-signal: Auto-Fill for tabular missing values; GouDa for controlled-error synthetic data-quality benchmarks; an end-to-end materialized-view rewriting benchmark; Hollywood as a movie dataset for database benchmarking; and a VLDB 2026 extended version on worst-case optimal basic graph patterns over temporal graphs. The common theme is less “new model” and more **testable infrastructure for data agents and database optimizers**. ([arxiv.org](https://arxiv.org/list/cs.DB/recent?show=100&skip=0))

## Section 3: Emerging Trends

- **Abstention and calibration are moving into data-management tasks.** Auto-Fill’s calibrated specialist ensemble and the TV-distance paper’s serving-stack equivalence tests both prioritize knowing when outputs are trustworthy over maximizing raw completion accuracy.

- **Causal ML is getting adversarial and operational.** The causal-effect poisoning audit and LoCaLS both assume real pipelines violate clean textbook assumptions: pooled data can be strategically contaminated, and observational discovery often has latent variables and selection bias.

- **Foundation-model adaptation is becoming statistical again.** StatLoRA and time-series post-training work suggest a shift from heuristic adaptation recipes toward inferential allocation, uncertainty control, and explicit post-training taxonomies.

- **Benchmarks are becoming pipeline-aware.** The materialized-view rewriting benchmark and GouDa emphasize end-to-end behavior, controlled errors, and cross-engine comparability—exactly the kind of design pressure data-agent evaluations need.

- **In-context Bayesian reasoning is being tested under controlled semantics.** Bayesian wind tunnels show that transformers may match Bayesian posteriors in some relational settings but fail when the discriminative statistic requires inaccessible arithmetic over opaque symbols.

## Section 4: Worth Watching

- **Local Causal Structure Learning in the Presence of Latent Variables and Selection Bias / LoCaLS.** A target-specific causal discovery algorithm that avoids learning the full global graph while allowing latent variables and selection bias; worth tracking if it gets code or stronger biological case studies. ([arxiv.org](https://arxiv.org/abs/2607.19866))

- **Post-Training in Time Series Foundation Models: A Unifying Framework.** A useful taxonomy of TSFM post-training interventions: parameter adaptation, context augmentation, model composition, output processing/uncertainty control, and compression/specialization. ([arxiv.org](https://arxiv.org/abs/2607.20002))

- **Extending GouDa.** A synthetic data generator for data-quality benchmarking that supports multiple data formats, controlled error insertion, and ground truth; relevant to entity resolution, data cleaning, and synthetic tabular evaluation. ([arxiv.org](https://arxiv.org/abs/2607.20165))

- **Benchmarking the Full Pipeline of Materialized-View-Based Query Rewriting.** Valuable because it evaluates enumeration, selection, and optimizer rewriting jointly, exposing interaction effects and regressions that component-only benchmarks miss. ([arxiv.org](https://arxiv.org/abs/2607.19679))

- **Air Quality Arena.** A large multi-country, multi-pollutant benchmark for evaluating time-series foundation models on 14,000+ station-pollutant series across seven countries and four continents. ([arxiv.org](https://arxiv.org/abs/2607.19381))

## Section 5: Discord Highlights

**Research brief — Jul 23**

Top papers:
1. **Auto-Fill** — specialist SLMs plus calibrated abstention for high-precision tabular missing-value prediction.
2. **Data-Poisoning Audits for Causal Effect Estimation** — adversarial append-budget sensitivity curves for AIPW causal estimates.
3. **Total Variation Distance Estimation in Autoregressive Models** — practical distributional equivalence testing for LLM serving stacks.
4. **Bayesian Wind Tunnels for Model Selection** — controlled tests of whether transformers perform Bayesian model selection.
5. **Statistical Inference for Rank Allocation in LoRA** — hypothesis-testing view of adaptive LoRA rank pruning/allocation.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-07-23","type":"paper","title":"Auto-Fill: Learning to Predict Missing Values Accurately with Specialist Language Models","authors_or_org":"Yurong Liu, Yeye He, Haoyu Dong, Junjie Xing, Shi Han, Dongmei Zhang, Surajit Chaudhuri","url":"https://arxiv.org/abs/2607.19847","memory":"Top 5 paper. Covered July 22 2026 arXiv / VLDB 2026 paper on tabular missing-value prediction using three specialist small language models for world knowledge, text reasoning, and code reasoning plus calibrated ensemble abstention; compared against frontier reasoning models at <1% cost. Suppress future arXiv/VLDB/code/repost versions unless materially changed."}
{"date_delivered":"2026-07-23","type":"paper","title":"Data-Poisoning Audits for Causal Effect Estimation","authors_or_org":"Kwangho Kim","url":"https://arxiv.org/abs/2607.19692","memory":"Top 5 paper. Covered append-only adversarial data-poisoning audits for augmented inverse-propensity-weighted causal effect estimation, exact finite-sample worst-case movement with fixed nuisance fits, total-influence scores under refitting, and critical append-budget curves. Suppress future versions unless theory or empirical scope materially expands."}
{"date_delivered":"2026-07-23","type":"paper","title":"Total Variation Distance Estimation in Autoregressive Models","authors_or_org":"Eric Price, Kevin Tian, Zhiyang Xun, Yusong Zhu","url":"https://arxiv.org/abs/2607.19510","memory":"Top 5 paper. Covered TV-distance estimation between length-n autoregressive distributions under sample, logit, and noisy-logit access; motivation includes serving-stack differences for identical model weights such as SGLang vs vLLM. Suppress future arXiv/code/venue reposts unless materially changed."}
{"date_delivered":"2026-07-23","type":"paper","title":"Bayesian Wind Tunnels for Model Selection","authors_or_org":"Siddhartha R. Dalal, Vishal Misra, Abhay Parekh","url":"https://arxiv.org/abs/2607.19379","memory":"Top 5 paper. Covered controlled Bayesian model-selection environments for transformers, exact posteriors over hypothesis classes, involutions vs 3-cycles, opaque-symbol arithmetic failures, and scaling from 2.8M to 316M not fixing lack of perceptual access. Suppress future reposts unless substantially expanded."}
{"date_delivered":"2026-07-23","type":"paper","title":"Statistical Inference for Rank Allocation in Low-Rank Adaptation","authors_or_org":"Yihang Gao, Vincent Y. F. Tan","url":"https://arxiv.org/abs/2607.20205","memory":"Top 5 paper. Covered StatLoRA, a hypothesis-testing and p-value framework for LoRA component retention/pruning under rank budgets, with CLT for stochastic optimizer trajectories including AdamW and experiments on DeBERTaV3, BART-Large, and Qwen2.5-7B. Suppress future versions unless theory or experiments materially change."}
{"date_delivered":"2026-07-23","type":"announcement","title":"AISTATS 2026 paper awards announcement","authors_or_org":"AISTATS 2026","url":"https://virtual.aistats.org/","memory":"Venue Watch. Covered AISTATS 2026 awards: Best Paper EventFlow; Best Student Paper We Still Don’t Understand High-Dimensional Bayesian Optimization; Test of Time Non-stochastic Best Arm Identification and Hyperparameter Optimization; Honorable Mention Deep Kernel Learning. Suppress repeat award summaries."}
{"date_delivered":"2026-07-23","type":"proceedings","title":"TMLR July 2026 accepted papers incremental update as of July 23","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered incremental July 2026 TMLR visible additions beyond earlier July snapshot, including Synth-FAR, low-precision microscaling instability analysis, generalized Dirichlet energy/graph Laplacians, Savaal, and sign-activation low-dimensional convex lasso view. Suppress this incremental snapshot; do not repeat full July 2026 batch."}
{"date_delivered":"2026-07-23","type":"proceedings","title":"arXiv cs.LG/stat.ML recent stream snapshot for July 23 2026","authors_or_org":"arXiv cs.LG/stat.ML","url":"https://arxiv.org/list/cs.LG/recent","memory":"Venue Watch. Covered July 23 2026 cs.LG/stat.ML stream with clusters in tabular missing-value prediction, LoRA rank inference, causal poisoning audits, autoregressive TV-distance estimation, time-series FM post-training, local causal discovery, Bayesian online learning, and recalibration. Suppress this daily stream snapshot."}
{"date_delivered":"2026-07-23","type":"proceedings","title":"arXiv cs.DB recent stream snapshot for July 23 2026","authors_or_org":"arXiv cs.DB","url":"https://arxiv.org/list/cs.DB/recent","memory":"Venue Watch. Covered July 23 2026 database stream: Auto-Fill, GouDa, materialized-view rewriting benchmark, Hollywood database benchmark dataset, and worst-case optimal BGPs on temporal graphs. Suppress this daily stream snapshot."}
{"date_delivered":"2026-07-23","type":"paper","title":"Local Causal Structure Learning in the Presence of Latent Variables and Selection Bias","authors_or_org":"Zheng Li, Hao Zhang, Ruxin Wang, Ruichu Cai, Kun Zhang, Feng Xie","url":"https://arxiv.org/abs/2607.19866","memory":"Worth Watching. Covered LoCaLS for target-specific causal discovery under latent variables and selection bias, sound/complete under assumptions, avoiding full global structure learning, with gene-expression applications. Suppress future arXiv/code/repost unless selected for deeper Top 5 or materially changed."}
{"date_delivered":"2026-07-23","type":"paper","title":"Post-Training in Time Series Foundation Models: A Unifying Framework","authors_or_org":"Shifeng Xie, Ambroise Odonnat, Zehao Xiao, Lei Zan, Malik Tiomoko, Lujia Pan, Themis Palpanas, Boris N. Oreshkin, Chenghao Liu, Keli Zhang","url":"https://arxiv.org/abs/2607.20002","memory":"Worth Watching. Covered taxonomy of post-training methods for time-series foundation models: parameter adaptation, context augmentation, model composition, output processing and uncertainty control, and compression/specialization. Suppress future versions unless substantially expanded."}
{"date_delivered":"2026-07-23","type":"software","title":"Extending GouDa: Generation of Universal Datasets with (and without) Errors for Data Quality Benchmarking","authors_or_org":"Valerie Restat, André Conrad, Kevin M. Kramer, Uta Störl","url":"https://arxiv.org/abs/2607.20165","memory":"Worth Watching. Covered GouDa synthetic data generator for data-quality benchmarking across tabular and NoSQL formats, controlled error insertion, error-free ground truth, and extensible generation functions. Suppress future arXiv/tool mentions unless artifact materially changes."}
{"date_delivered":"2026-07-23","type":"benchmark","title":"Benchmarking the Full Pipeline of Materialized-View-Based Query Rewriting","authors_or_org":"Xinjie Hu, Zhengjie Miao","url":"https://arxiv.org/abs/2607.19679","memory":"Worth Watching. Covered end-to-end benchmark for materialized-view-based query rewriting evaluating enumeration, selection, and optimizer rewriting jointly, with cross-engine protocol and failure-mode analysis. Suppress future mentions unless benchmark/artifact materially expands."}
{"date_delivered":"2026-07-23","type":"benchmark","title":"Air Quality Arena: A Large-Scale Multi-Region Ground Monitoring Dataset and Benchmark for Air Quality Forecasting with Time-Series Foundation Models","authors_or_org":"Rishi Bharadwaj, Manik Gupta, Pandarasamy Arjunan","url":"https://arxiv.org/abs/2607.19381","memory":"Worth Watching. Covered AQA/AQA-Bench for time-series foundation model evaluation on 6 pollutants over 3 years across 7 countries, 4 continents, and 14,000+ station-pollutant series. Suppress future arXiv/project/dataset mentions unless public resource materially expands."}
```