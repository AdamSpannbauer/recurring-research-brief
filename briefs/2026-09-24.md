## Section 1: Top 5 Papers

1. **What Do Tabular Foundation Models Compute In Context? In-Situ Representation Refinement through Attention-Gated Updates**  
   **Authors:** Tian Zhou, Beverly Jin, Linxiao Yang, Xue Wang, Wenwei Wang, Bingqing Peng, Mengni Ye, Jinjie Gu, Liang Sun  
   **Venue/source:** arXiv cs.LG  
   **Date:** submitted September 23, 2026; visible in September 24 arXiv new listings  
   **Link:** arXiv.  
   This is the most directly relevant item today: a mechanistic/methodological account of what tabular foundation models should compute during in-context prediction. The paper frames support labels as inducing *in-situ representation refinement* rather than merely supplying labels for nearest-neighbor-like reading. The resulting RefineICL architecture is attention-gated, FFN-free, and uses typed memory plus selected low-rank feature interactions. The empirical claims are strong—better TabArena Elo than TabPFN-3 under a matched snapshot, better TabZilla metrics than TabPFN-v3, and interventions showing intermediate support updates causally matter.  
   **Why you should care:** This is a concrete hypothesis about the reusable computation inside tabular FMs, not just another benchmark entry. ([arxiv.org](https://arxiv.org/abs/2609.27679))

2. **QUARTET: Quad-branch cross-Attention and Random-walk Traces for Enhancing Transformers on Relational Graphs**  
   **Authors:** Kyaw Hpone Myint, Nan Jiang, Xiang Li, Zhe Wu, Alexandre G. R. Day, Pranab Mohanty, Giri Iyengar  
   **Venue/source:** arXiv cs.LG; accepted to Learning on Graphs 2026 main track  
   **Date:** submitted September 22, 2026  
   **Link:** arXiv.  
   QUARTET targets relational deep learning over multi-table databases, where RelBench-style tasks expose the limits of random local sampling and shallow global memories. The method replaces loose subgraph sampling with a temporally safe causal random walk based on recency-truncated personalized PageRank, then augments local full-attention with four global cross-attention views: seed feature, seed topology, temporal dynamics, and collaborative dynamics. It reportedly matches or exceeds HGT and RelGT across RelBench v1 classification tasks.  
   **Why you should care:** Relational foundation modeling is rapidly becoming “tabular FM, but with joins,” and QUARTET attacks the neighborhood-construction bottleneck head-on. ([arxiv.org](https://arxiv.org/abs/2609.26855))

3. **Rolling Conformal Prediction in Sequential Model Training**  
   **Authors:** Chen Cheng, Ruiting Liang, Rina Foygel Barber  
   **Venue/source:** arXiv math.ST / stat.ML / cs.LG  
   **Date:** submitted September 22, 2026  
   **Link:** arXiv.  
   Rolling-CP addresses a problem that will matter for deployed foundation models and adaptive agents: how to maintain distribution-free predictive inference when the model is continually trained or adapted on the stream it is also being calibrated against. Instead of splitting off a permanent calibration set, each observation is calibrated against the current predictor and then rolled into future training. The guarantee is conservative but strikingly assumption-light: marginal coverage at a universal factor-two level for exchangeable data without model stability assumptions, with sharper training-conditional validity under i.i.d. streams and stability.  
   **Why you should care:** It gives a clean inferential primitive for continual fine-tuning, online tabular learning, and test-time adaptation regimes. ([arxiv.org](https://arxiv.org/abs/2609.26951))

4. **Artificial intelligence surrogates for treatment effect estimation with before-and-after data**  
   **Authors:** Frances Dean, Anna Neufeld, Joshua Barrios, Geoffrey H. Tison, Ahmed Alaa  
   **Venue/source:** arXiv stat.ML  
   **Date:** submitted September 23, 2026  
   **Link:** arXiv.  
   This paper formalizes a timely causal-inference pattern: use pretrained AI predictions on cheap, high-dimensional measurements as surrogate outcomes when clinical endpoints are slow or expensive. The setup uses paired pre/post-treatment measurements for treated individuals, applies an AI model to both, and estimates treatment effects through the within-person change in predicted outcome. The authors state assumptions for identifying the average treatment effect on the treated even without observed clinical outcomes for treated units, and add prediction-powered inference when a small labeled outcome sample is available for bias correction.  
   **Why you should care:** It connects black-box predictive models, surrogate endpoints, and valid causal inference in a way likely to recur in medical and operational ML. ([arxiv.org](https://arxiv.org/abs/2609.27180))

5. **WTF?! Simulation-Free Reinforcement Learning with Wasserstein-Tilted Flow Maps**  
   **Authors:** Abbas Mammadov, Jerry Y. Huang, Justin Lin, Partha Kaushik, Sheel Shah, Kartik Nair, Yee Whye Teh, Nicholas M. Boffi  
   **Venue/source:** arXiv cs.LG / stat.ML  
   **Date:** submitted September 22, 2026  
   **Link:** arXiv.  
   WTF revisits reward fine-tuning for flow-based generative models. Instead of KL reward tilting, which reweights the base distribution, it uses an optimal-transport regularizer tied to the pretrained drift so individual samples are transported toward higher reward. The authors show an equivalence to deterministic optimal control over the flow map, yielding a simulation-free RL recipe for generative-flow fine-tuning. The reported gains include reward-aligned few-step inference without post-hoc distillation and up to 280× less training compute in ImageNet/text-to-image experiments.  
   **Why you should care:** It is a credible alternative geometry for post-training generative models, adjacent to recent Newton/flow-matching fine-tuning work. ([arxiv.org](https://arxiv.org/abs/2609.27033))

## Section 2: Venue Watch

- **arXiv cs.LG/stat.ML/cs.DB, September 24 new-submission stream.** Today’s stream is large: 115 new cs.LG entries, 12 new stat.ML entries, and one new cs.DB entry, plus cross-lists and replacements. The strongest clusters are tabular/relational foundation models, sequential calibration and anytime inference, generative flow/diffusion theory, agent-training infrastructure, and knowledge-graph/data-management evaluation. Especially notable: RefineICL and Support-Compiled Feature Folding for tabular FMs, QUARTET for RelBench-style relational graphs, rolling conformal prediction, AI-surrogate causal estimation, Wasserstein-tilted flow maps, and a semi-structured KG-construction benchmark. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **TMLR September 2026 accepted papers: incremental top-of-page update.** New visible additions since the last covered September snapshot include papers on weakly supervised segmentation priors, fairness in link prediction beyond homophily, function-space diversity for uncertainty via repulsive last-layer ensembles, robust sparse PCA, and Bayesian DNN compression via sparse quantized sub-distributions. The broader September batch continues to emphasize uncertainty, graph learning, compression/quantization, RAG verification, tabular foundation-model density estimation, and agent/model-evaluation infrastructure. ([jmlr.org](https://jmlr.org/tmlr/papers/))

## Section 3: Emerging Trends

- **Tabular FMs are shifting from leaderboard races to internal computation and systems constraints.** RefineICL asks what computation is reusable in-context, while SCFF attacks wide-table memory scaling without changing frozen backbones.

- **Relational learning is converging with database query structure.** QUARTET, recent RelArena/TabPFN-Rel work, and data-agent systems all point toward learned models that need temporally valid sampling, join-aware context, and explicit global memory.

- **Calibration/inference is being rebuilt for adaptive systems.** Rolling-CP, noisy-label tabular calibration, conformal shift work, and prediction-powered evaluation all assume models are updated, reused, or label-constrained after deployment.

- **Agent infrastructure is becoming statistical infrastructure.** Tool caches, benchmark validity screens, KG construction benchmarks, trace databases, and provenance systems are increasingly framed as sources of bias, not just engineering conveniences.

- **Generative-model fine-tuning is moving beyond KL tilting.** Wasserstein-tilted flows and diffusion robustness theory suggest a broader search over geometries for post-training and distribution-shift control.

## Section 4: Worth Watching

- **Support-Compiled Feature Folding: More Evidence at Lower Memory Across Tabular Foundation Models** — training-free inference-time feature folding for frozen tabular FMs; reports 2×+ median GPU-memory savings and gains on wide-table strata. Treat as a systems companion to RefineICL, but suppress separately because it is a distinct artifact. ([arxiv.org](https://arxiv.org/abs/2609.28208))

- **Benchmarking Automated Knowledge Graph Construction from Semi-Structured Data** — a cs.DB benchmark/evaluation pipeline for KG construction from semi-structured inputs, with ten expert-curated datasets and metrics spanning syntax, semantic accuracy, consistency, conciseness, completeness, and downstream competency questions. ([arxiv.org](https://arxiv.org/abs/2609.26985))

- **Robustness of Diffusion Models under Distribution Shift** — minimax theory for score estimation under Wasserstein perturbations, decomposing statistical cost from intrinsic shift cost and adapting to unknown low-dimensional subspaces. ([arxiv.org](https://arxiv.org/abs/2609.27546))

- **Marginally Correct Tool Caches Can Reverse Group-Normalized Policy Updates** — a concise warning that stochastic tool-result caching can preserve marginal reward distributions while reversing group-normalized policy-gradient direction; relevant to agent RL systems. ([arxiv.org](https://arxiv.org/abs/2609.26866))

- **The Type-II Error of Test Supermartingales: e-Power versus the Chernoff-Stein Exponent** — a sharp technical note showing that e-power alone does not control finite-horizon type-II error, while a Chernoff-Stein exponent does. Worth tracking for anytime-valid inference and e-value methodology. ([arxiv.org](https://arxiv.org/abs/2609.27765))

## Section 5: Discord Highlights

**Sep 24 — research brief highlights**

1. **What Do Tabular Foundation Models Compute In Context?** — RefineICL turns support labels into in-situ representation updates for tabular FM prediction.  
2. **QUARTET** — relational graph transformer improves RelBench-style learning with causal random walks and quad-branch global context.  
3. **Rolling Conformal Prediction in Sequential Model Training** — distribution-free calibration for models that keep training on the stream.  
4. **AI surrogates for treatment effect estimation** — pretrained predictors become causal surrogates, with prediction-powered bias correction.  
5. **WTF?! Simulation-Free RL with Wasserstein-Tilted Flow Maps** — flow-map-native reward fine-tuning via OT rather than KL tilting.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-09-24","type":"paper","title":"What Do Tabular Foundation Models Compute In Context? In-Situ Representation Refinement through Attention-Gated Updates","authors_or_org":"Tian Zhou, Beverly Jin, Linxiao Yang, Xue Wang, Wenwei Wang, Bingqing Peng, Mengni Ye, Jinjie Gu, Liang Sun","url":"https://arxiv.org/abs/2609.27679","memory":"Top 5 paper. Covered RefineICL, an attention-gated FFN-free contextual stack for tabular foundation models motivated by in-situ support-label representation refinement, with TabArena/TabZilla claims and causal interventions on support updates. Suppress arXiv/code/venue/repost versions unless architecture, benchmark, or mechanistic evidence materially changes."}
{"date_delivered":"2026-09-24","type":"paper","title":"QUARTET: Quad-branch cross-Attention and Random-walk Traces for Enhancing Transformers on Relational Graphs","authors_or_org":"Kyaw Hpone Myint, Nan Jiang, Xiang Li, Zhe Wu, Alexandre G.R. Day, Pranab Mohanty, Giri Iyengar","url":"https://arxiv.org/abs/2609.26855","memory":"Top 5 paper. Covered LoG 2026 main-track paper for relational deep learning over multi-table databases: causal random-walk sampler, quad-branch cross-attention over seed features/topology/temporal/collaborative context, and RelBench v1 claims. Suppress arXiv/LoG/code/repost versions unless method or evaluation materially changes."}
{"date_delivered":"2026-09-24","type":"paper","title":"Rolling Conformal Prediction in Sequential Model Training","authors_or_org":"Chen Cheng, Ruiting Liang, Rina Foygel Barber","url":"https://arxiv.org/abs/2609.26951","memory":"Top 5 paper. Covered rolling conformal prediction for sequentially trained or continually adapted models, calibrating each incoming observation before rolling it into future training with distribution-free coverage guarantees. Suppress arXiv/code/venue versions unless guarantees or scope materially expand."}
{"date_delivered":"2026-09-24","type":"paper","title":"Artificial intelligence surrogates for treatment effect estimation with before-and-after data","authors_or_org":"Frances Dean, Anna Neufeld, Joshua Barrios, Geoffrey H Tison, Ahmed Alaa","url":"https://arxiv.org/abs/2609.27180","memory":"Top 5 paper. Covered causal treatment-effect estimation using pretrained AI outcome predictions as surrogates on paired pre/post measurements, plus prediction-powered correction with small labeled outcome samples. Suppress future arXiv/venue/code mentions unless assumptions, estimators, or empirical scope materially change."}
{"date_delivered":"2026-09-24","type":"paper","title":"WTF?! Simulation-Free Reinforcement Learning with Wasserstein-Tilted Flow Maps","authors_or_org":"Abbas Mammadov, Jerry Y. Huang, Justin Lin, Partha Kaushik, Sheel Shah, Kartik Nair, Yee Whye Teh, Nicholas M. Boffi","url":"https://arxiv.org/abs/2609.27033","memory":"Top 5 paper. Covered Wasserstein-Tilted Flow Maps for reward fine-tuning flow-based generative models using OT regularization tied to pretrained drift and deterministic optimal-control equivalence. Suppress future arXiv/code/venue/social reposts unless algorithm, theory, or experiments materially change."}
{"date_delivered":"2026-09-24","type":"proceedings","title":"arXiv cs.LG/stat.ML/cs.DB new-submission stream for September 24 2026","authors_or_org":"arXiv cs.LG, stat.ML, cs.DB","url":"https://arxiv.org/list/cs.LG/new","memory":"Venue Watch. Covered Sep 24 2026 streams: 115 new cs.LG entries, 12 new stat.ML entries, and one new cs.DB entry; themes included tabular/relational foundation models, sequential conformal inference, generative flow/diffusion theory, agent-training infrastructure, and KG/data-management evaluation. Suppress repeat daily stream summary."}
{"date_delivered":"2026-09-24","type":"proceedings","title":"TMLR September 2026 accepted papers incremental update as of September 24","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered new visible top-of-page September 2026 additions including instance priors for weakly supervised semantic segmentation, fairness in link prediction beyond homophily, function-space diversity for uncertainty with repulsive last-layer ensembles, robust sparse PCA, and Bayesian DNN compression via sparse quantized sub-distributions. Suppress repeat Sep 24 incremental snapshot."}
{"date_delivered":"2026-09-24","type":"paper","title":"Support-Compiled Feature Folding: More Evidence at Lower Memory Across Tabular Foundation Models","authors_or_org":"Tian Zhou, Beverly Jin, Xue Wang, Linxiao Yang, Wenwei Wang, Bingqing Peng, Mengni Ye, Jinjie Gu, Liang Sun","url":"https://arxiv.org/abs/2609.28208","memory":"Worth Watching. Covered SCFF as a training-free inference framework for frozen tabular foundation models that folds support-ranked features through bounded leaves to reduce wide-table memory while preserving evidence. Suppress arXiv/code/venue repeats unless system or benchmarks materially expand."}
{"date_delivered":"2026-09-24","type":"benchmark","title":"Benchmarking Automated Knowledge Graph Construction from Semi-Structured Data","authors_or_org":"Tarek Al Mustafa, Birgitta König-Ries","url":"https://arxiv.org/abs/2609.26985","memory":"Worth Watching. Covered benchmark/evaluation pipeline for KG construction from semi-structured data with ten expert-curated datasets and metrics for syntactic validity, semantic accuracy, consistency, conciseness, completeness, and competency-question utility. Suppress future arXiv/code/benchmark reposts unless dataset or evaluation suite materially changes."}
{"date_delivered":"2026-09-24","type":"paper","title":"Robustness of Diffusion Models under Distribution Shift","authors_or_org":"Wei Luo, Neil K. Chada, Shijie Zhang, Lu Yu","url":"https://arxiv.org/abs/2609.27546","memory":"Worth Watching. Covered minimax theory for score-based diffusion under Wasserstein distribution shift, decomposing statistical learning cost and intrinsic shift cost, with intrinsic-dimension adaptation. Suppress future arXiv/venue/repost versions unless theory materially expands."}
{"date_delivered":"2026-09-24","type":"paper","title":"Marginally Correct Tool Caches Can Reverse Group-Normalized Policy Updates","authors_or_org":"Shivam Gupta","url":"https://arxiv.org/abs/2609.26866","memory":"Worth Watching. Covered finite-group analysis showing stochastic tool-result caching can preserve marginal reward distributions while reversing expected group-normalized policy updates; includes TVCache audit. Suppress arXiv/code/social/venue repeats unless agent-training cache theory or evidence materially changes."}
{"date_delivered":"2026-09-24","type":"paper","title":"The Type-II Error of Test Supermartingales: e-Power versus the Chernoff-Stein Exponent","authors_or_org":"Patrick Forré","url":"https://arxiv.org/abs/2609.27765","memory":"Worth Watching. Covered safe-testing/e-value theory showing e-power alone does not give finite-horizon type-II error guarantees, while a Chernoff-Stein exponent controls power. Suppress future arXiv/repost/venue mentions unless theory materially changes."}
```