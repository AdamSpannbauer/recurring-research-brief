## Section 1: Top 5 Papers

### 1. RT-J: Large-Scale Pretraining of Relational Transformers for Context-Efficient Predictions
**Authors:** Rishabh Ranjan, Vignesh Kothapalli, Harshvardan Agarwal, Charilaos Kanatsoulis, Roshan Upendra, Tom Palczewski, Carlos Guestrin, Jure Leskovec  
**Venue/source:** arXiv; accepted to NeurIPS 2026  
**Date:** submitted October 13, revised October 15, 2026  
**Link:** ([arxiv.org](https://arxiv.org/abs/2610.17867))  

RT-J is the most important structured-data item this cycle: an 86M-parameter relational foundation model trained for context-efficient prediction over multi-table databases. The paper introduces **Join**, a pretraining corpus of 639 web-crawled databases and 6,023 LLM-generated forecasting tasks, trains with contexts up to 8,192 database cells, and uses a lightweight random-walk retriever for relational context. The key result is not just accuracy but sample efficiency: on RelBench-style in-context regression, RT-J reportedly needs about **10× fewer examples** than strong feature-engineering pipelines using LLM agents/RDBLearn plus TabICLv2 or LightGBM. This directly attacks the relational-FM context bottleneck that has appeared repeatedly in recent papers. ([arxiv.org](https://arxiv.org/abs/2610.17867))  
**Why you should care:** This is a serious step from single-table PFN-style tabular FMs toward relational prediction as a pretraining problem.

### 2. SelectPFN: Amortized Bayesian Variable Selection for Sparse Nonlinear Regression with Prior-Data Fitted Networks
**Authors:** Bin Luo  
**Venue/source:** arXiv  
**Date:** submitted October 15, 2026  
**Link:** ([arxiv.org](https://arxiv.org/abs/2610.21950))  

SelectPFN turns the PFN recipe into a one-shot Bayesian sparse regression and variable-selection engine. Instead of only predicting, it outputs posterior inclusion probabilities for every covariate, samples predictive subsets, and ensures excluded variables cannot affect predictions. The pretraining prior is a group spike-and-slab sparse-input neural network; a column-permutation-equivariant construction with knockoff interleaving yields finite-sample FDR control for derived knockoff statistics, even under meta-prior misspecification. The theory includes Bayes-regret results and a negative result separating average-case amortized training from fixed-truth frequentist guarantees. Empirically, it improves precision-recall over lasso/BART/DART/LassoNet on nonlinear sparse designs up to p=500. ([arxiv.org](https://arxiv.org/abs/2610.21950))  
**Why you should care:** This is exactly the kind of “PFN + statistical validity” direction that could make tabular FMs useful for scientific modeling rather than black-box prediction.

### 3. Human Interventions as Labels: Localizing, Steering, and (Sometimes) Editing the Computations Behind LLM Agent Failures
**Authors:** Cesare Zavattari, Alessandro Tommasi, Giuseppe Prencipe  
**Venue/source:** arXiv  
**Date:** submitted October 15, 2026  
**Link:** ([arxiv.org](https://arxiv.org/abs/2610.21708))  

This paper reframes human takeover events in agent systems as supervised measurements of internal computational failure, not just behavior-cloning data. In a controlled over-asking failure mode, intervention-derived labels identify residual-stream directions that flip 72–100% of held-out erroneous “ask clarification” decisions in eligible model families. The paper’s strongest contribution is diagnostic: several models encode that the request is already unambiguous, but the belief is causally inert and orthogonal to the ask/act decision. Probe-gated steering reduces oversight burden while preserving legitimate clarification questions; weight edits sometimes consolidate the fix, but not predictably across families. ([arxiv.org](https://arxiv.org/abs/2610.21708))  
**Why you should care:** It connects agent supervision, mechanistic localization, and editability in a way that feels more actionable than most circuit papers.

### 4. Conditional Mean Flows: Few-Step Densities for Simulation-Based Inference
**Authors:** Jonas Arruda, Jan Hasenauer, Stefan T. Radev  
**Venue/source:** arXiv  
**Date:** submitted October 15, 2026  
**Link:** ([arxiv.org](https://arxiv.org/abs/2610.21657))  

Conditional Mean Flows target a practical bottleneck in simulation-based inference: flow-matching posteriors are flexible but expensive when density evaluation requires numerical integration, especially inside MCMC. The paper proposes conditional mean flows for posterior and likelihood approximation, combining few-step sampling with tractable density evaluation. The mean-flow objective identifies conditional flow maps, while independent masking enables direct marginal-likelihood estimation. Reported results suggest one-step density evaluation can match the estimation quality of 200-step flow matching while enabling roughly 200× faster downstream MCMC. This is a compelling bridge between neural SBI and reusable Bayesian computation. ([arxiv.org](https://arxiv.org/abs/2610.21657))  
**Why you should care:** If the claims hold, this reduces the operational cost of using flow-based neural posteriors inside real Bayesian workflows.

### 5. Causal Integrated Gradients: Scalable Feature Attribution Along Causal Paths
**Authors:** Joran Michiels, Anis Ismail, Maarten De Vos, Alejandro Sifrim  
**Venue/source:** arXiv  
**Date:** submitted October 15, 2026  
**Link:** ([arxiv.org](https://arxiv.org/abs/2610.22126))  

Causal Integrated Gradients and Causal Expected Gradients extend gradient attribution to account for known causal structure among inputs while preserving much of integrated gradients’ computational appeal. The central move is to route the integration path along a causal graph, decomposing each feature’s attribution into direct and mediated effects. The motivation is especially strong in high-dimensional biological settings: naïve attributions can credit downstream genes rather than upstream transcription factors. The paper evaluates on synthetic SCMs, Dyngen single-cell simulations, and interferon-β stimulation data, reporting better recovery of causal drivers than DeepSHAP and ordinary integrated gradients. ([arxiv.org](https://arxiv.org/abs/2610.22126))  
**Why you should care:** It is a pragmatic compromise between causal feature attribution and scalable gradient methods for high-dimensional scientific data.

## Section 2: Venue Watch

**arXiv October 16 stream.** The daily stream was unusually dense: 166 new cs.LG submissions, 22 new stat.ML submissions, and 5 new cs.DB submissions. The strongest clusters were relational/tabular foundation models, PFN-style statistical inference, causal attribution, simulation-based inference, agent failure localization, conformal/online prediction, private/vector search, and database-agent workflow formalization. The new cs.DB entries included SIGMOD/PACMMOD-style systems work on private ANNS, sparse Boolean matrix processing, disk-based ANNS prefetching, NL-to-SPARQL grounding, and trajectory cardinality estimation. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

**TMLR October 2026 incremental stream.** The visible October page has shifted toward reasoning and agent reliability: π-CoT for Prolog-initialized chain-of-thought, “Structure Over Scale” for RL with verifiable rewards, offline contextual bandits with new actions, causal bandits, concept attractors in LLMs, protocol–objective–resource reductions, and several calibration/explainability items. Compared with earlier October snapshots, the page is now less dominated by diffusion/transport and more by reasoning protocols, reward design, and deployment-time reliability. ([jmlr.org](https://jmlr.org/tmlr/papers/))

**SIGMOD/PACMMOD 2027 preprint trickle.** The database stream is already surfacing accepted 2027 systems papers. Amora targets private ANNS using partitioned graph indexes plus SimplePIR and reports 93–99% lower online communication than Pacmann; AdaBool focuses on sparse Boolean matrix processing; TraHist gives density-aligned histogram cardinality estimation for trajectory data and reports over 20× error reduction in regimes dominated by trajectory fragmentation. ([arxiv.org](https://arxiv.org/abs/2610.21174))

## Section 3: Emerging Trends

- **Relational foundation models are moving from “can we encode joins?” to “how do we retrieve context?”** RT-J, STEER, context-window failure papers, and relational sampling work all point to retrieval/context engineering as the dominant bottleneck for relational FMs.

- **PFNs are becoming statistical instruments, not just predictors.** SelectPFN, MatrixFormer, Marformer, and PDE-PFN suggest the PFN idea is expanding into variable selection, matrix completion, missingness, PDE solving, and off-policy evaluation.

- **Semantic query processing is converging on certification.** Recent work on semantic views, run-to-run variance, cached semantic operators, plan accuracy, and semantic query algebras shows that DB researchers are treating LLM calls as stochastic physical operators needing audits, reuse certificates, and plan-aware accuracy semantics.

- **Mechanistic interpretability is becoming intervention-oriented.** The best recent papers ask whether learned mechanisms support steering, editing, control, or failure triage—not merely whether a circuit can be extracted.

- **Flow/diffusion theory is increasingly about cost and deployment.** Conditional mean flows, FlowBudget, weighted adjoint matching, masked-diffusion rejection sampling, and discrete-diffusion minimax work all focus on the practical cost/statistical tradeoffs of sampling.

## Section 4: Worth Watching

- **Amora: Communication-Efficient Private Approximate Nearest Neighbors Search.** A SIGMOD 2027 private vector-search system that amortizes PIR over graph partitions and reports 93–99% online communication reduction versus Pacmann. ([arxiv.org](https://arxiv.org/abs/2610.21174))

- **FAOPs: Normal Forms and an Algebra for AI Agent Workflows.** A database/programming-languages-style formalism for agent operating procedures, with normal forms for decomposition, typing, factoring, scoping, plus algebraic rewrites and runtime enforcement. ([arxiv.org](https://arxiv.org/abs/2610.22061))

- **FlowBudget.** A training-free method for estimating the sampling budget needed by flow-matching models without repeated FID-vs-NFE sweeps; useful if flow models keep moving into production settings. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **Selection-Safe Conformal Early Exit.** A simple but important warning: calibrating each early-exit head separately does not preserve coverage once the exit is adaptively chosen. The proposed pathwise conformal construction supports post-calibration stopping policies. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **Query-Efficient Rejection Sampling for Parallel Masked Diffusion.** Introduces a single-increment rejection sampler for masked diffusion decoding, aiming to correct within-block dependence with far fewer score queries. ([arxiv.org](https://arxiv.org/list/stat.ML/new))

## Section 5: Discord Highlights

**Oct 16 brief — Top 5 papers**

1. **RT-J: Large-Scale Pretraining of Relational Transformers for Context-Efficient Predictions** — NeurIPS relational FM with large-scale database pretraining and 10× fewer in-context examples.
2. **SelectPFN** — PFN-style one-pass Bayesian variable selection with posterior inclusion probabilities and FDR-controlled knockoff statistics.
3. **Human Interventions as Labels** — Uses takeover events to localize, steer, and sometimes edit agent failure computations.
4. **Conditional Mean Flows** — Few-step posterior/likelihood densities for simulation-based inference with much faster MCMC use.
5. **Causal Integrated Gradients** — Scalable gradient attribution that routes credit along known causal paths.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-10-16","type":"paper","title":"RT-J: Large-Scale Pretraining of Relational Transformers for Context-Efficient Predictions","authors_or_org":"Rishabh Ranjan, Vignesh Kothapalli, Harshvardan Agarwal, Charilaos Kanatsoulis, Roshan Upendra, Tom Palczewski, Carlos Guestrin, Jure Leskovec","url":"https://arxiv.org/abs/2610.17867","memory":"Top 5 paper. Covered NeurIPS 2026 relational foundation model RT-J, Join corpus of 639 web-crawled databases and 6023 LLM-generated forecasting tasks, random-walk retriever, long contexts up to 8192 cells, context tuning/ensembling, RelBench sample-efficiency claims. Suppress arXiv, NeurIPS, STAR project, code/model-card, and social reposts unless architecture, corpus, license, or evaluation materially changes."}
{"date_delivered":"2026-10-16","type":"paper","title":"SelectPFN: Amortized Bayesian Variable Selection for Sparse Nonlinear Regression with Prior-Data Fitted Networks","authors_or_org":"Bin Luo","url":"https://arxiv.org/abs/2610.21950","memory":"Top 5 paper. Covered PFN for one-forward-pass Bayesian sparse nonlinear regression and variable selection with posterior inclusion probabilities, spike-and-slab meta-prior, knockoff statistics with finite-sample FDR control, amortized selection theory, and p up to 500 experiments. Suppress future arXiv/code/venue reposts unless method or guarantees materially change."}
{"date_delivered":"2026-10-16","type":"paper","title":"Human Interventions as Labels: Localizing, Steering, and (Sometimes) Editing the Computations Behind LLM Agent Failures","authors_or_org":"Cesare Zavattari, Alessandro Tommasi, Giuseppe Prencipe","url":"https://arxiv.org/abs/2610.21708","memory":"Top 5 paper. Covered using human/overseer interventions as labels for mechanistic localization of LLM agent failures, over-asking failure mode, residual steering directions, probe-gated steering, and mixed LoRA consolidation results. Suppress arXiv/code/venue/social repeats unless benchmark, intervention framework, or empirical scope materially expands."}
{"date_delivered":"2026-10-16","type":"paper","title":"Conditional Mean Flows: Few-Step Densities for Simulation-Based Inference","authors_or_org":"Jonas Arruda, Jan Hasenauer, Stefan T. Radev","url":"https://arxiv.org/abs/2610.21657","memory":"Top 5 paper. Covered conditional mean flows for posterior and likelihood approximation in simulation-based inference, few-step sampling, tractable density evaluation, independent masking for marginal likelihood estimation, and 200x downstream MCMC speedup claim. Suppress arXiv/code/venue reposts unless SBI framework or evidence materially changes."}
{"date_delivered":"2026-10-16","type":"paper","title":"Causal Integrated Gradients: Scalable Feature Attribution Along Causal Paths","authors_or_org":"Joran Michiels, Anis Ismail, Maarten De Vos, Alejandro Sifrim","url":"https://arxiv.org/abs/2610.22126","memory":"Top 5 paper. Covered CIG/CEG causal-path extensions of integrated gradients using known causal graphs, decomposition of direct and mediated effects, synthetic SCM, Dyngen single-cell, and interferon-beta examples. Suppress arXiv/code/venue repeats unless attribution guarantees or empirical scope materially expand."}
{"date_delivered":"2026-10-16","type":"proceedings","title":"arXiv cs.LG/stat.ML/cs.DB new-submission stream for October 16 2026","authors_or_org":"arXiv cs.LG, stat.ML, cs.DB","url":"https://arxiv.org/list/cs.LG/new","memory":"Venue Watch. Covered Oct 16 2026 streams: cs.LG 166 new submissions, stat.ML 22 new submissions, cs.DB 5 new submissions. Themes included relational/tabular FMs, PFN statistical inference, causal attribution, SBI, agent failure localization, conformal/online prediction, private/vector search, and database-agent workflow formalization. Suppress repeat daily stream summary."}
{"date_delivered":"2026-10-16","type":"proceedings","title":"TMLR October 2026 accepted papers incremental update as of October 16","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered visible Oct 16 TMLR October top-of-page activity including pi-CoT, Structure Over Scale, Offline Contextual Bandits with New Actions, causal bandits, concept attractors in LLMs, protocol-objective-resource reductions, calibration/explainability items, and ongoing October reasoning/reliability stream. Suppress repeat Oct 16 snapshot."}
{"date_delivered":"2026-10-16","type":"proceedings","title":"SIGMOD/PACMMOD 2027 preprint trickle in cs.DB as of October 16 2026","authors_or_org":"ACM SIGMOD / PACMMOD / arXiv cs.DB","url":"https://arxiv.org/list/cs.DB/new","memory":"Venue Watch. Covered October 16 database preprints with accepted SIGMOD/PACMMOD 2027 items including Amora, AdaBool, TraHist, and related systems; summarized private ANNS, sparse Boolean matrix processing, disk-based ANNS, NL-to-SPARQL grounding, and trajectory cardinality estimation. Suppress repeat broad preprint-trickle summary; cover individual papers only if materially expanded."}
{"date_delivered":"2026-10-16","type":"software","title":"Amora: Communication-Efficient Private Approximate Nearest Neighbors Search","authors_or_org":"Qiuhao Wang, Zuowei Chen, Xu Yang, Saiyu Qi, Yong Qi","url":"https://arxiv.org/abs/2610.21174","memory":"Worth Watching and SIGMOD 2027 item. Covered private approximate nearest-neighbor search with partitioned graph index, SimplePIR, dual VecPIR/NbrPIR layout, batch PIR, centroid pruning, TopCand exploration, and 93-99% communication reduction versus Pacmann. Suppress arXiv/SIGMOD/code repeats unless system or evaluation materially changes."}
{"date_delivered":"2026-10-16","type":"paper","title":"FAOPs: Normal Forms and an Algebra for AI Agent Workflows","authors_or_org":"Ali Mohammadi Shanghooshabad / JPMorgan Chase & Co.","url":"https://arxiv.org/abs/2610.22061","memory":"Worth Watching. Covered formal database/PL-style theory of Functional Agent Operating Procedures with decomposition, typing, factoring, scoping normal forms, algebraic workflow rewrites, termination/optimization/cost extensions, and SkillBase system. Suppress arXiv/tool/venue reposts unless formalism or implementation materially expands."}
{"date_delivered":"2026-10-16","type":"paper","title":"FlowBudget: Training-Free Sampling-Budget Estimation for Flow Matching Models","authors_or_org":"Zahra Dehghani, Pablo Piantanida, Mohammadhadi Shateri","url":"https://arxiv.org/abs/2610.20636","memory":"Worth Watching. Covered training-free estimator of solver-relative sampling complexity for flow-matching models, using interpolation probes and one-step discretization error to choose NFE budgets without repeated FID sweeps. Suppress future arXiv/code/venue mentions unless method or empirical scope materially changes."}
{"date_delivered":"2026-10-16","type":"paper","title":"Selection-Safe Conformal Early Exit: Distribution-Free Coverage under Adaptive Depth","authors_or_org":"Adria Binte Habib, Ibne Farabi Shihab","url":"https://arxiv.org/abs/2610.20773","memory":"Worth Watching. Covered conformal early-exit calibration using terminal path scores and prefix maxima to preserve coverage under adaptive depth/stopping policies; noted naive layerwise selection coverage failure. Suppress arXiv/code/venue repeats unless guarantees or applications materially change."}
{"date_delivered":"2026-10-16","type":"paper","title":"Query-Efficient Rejection Sampling for Parallel Masked Diffusion","authors_or_org":"Shiyuan Zhang, Xuheng Li, Qiwei Di, Quanquan Gu","url":"https://arxiv.org/abs/2610.22238","memory":"Worth Watching. Covered Single-Increment Rejection Sampler for parallel masked diffusion, using one randomly sampled increment plus Bernoulli factory/Rao-Blackwellization to reduce score-query cost while correcting within-block dependence. Suppress future arXiv/code/venue reposts unless sampling theory or empirical results materially expand."}
```