## Section 1: Top 5 Papers

1. **Learning to Fluctuate: Statistical Foundations for Causal Tabular Pretraining**  
   **Authors:** Zhiheng Zhang  
   **Venue/source:** arXiv stat.ML/cs.LG  
   **Publication/release date:** Submitted September 22, 2026  
   **Link:** arXiv record. ([arxiv.org](https://arxiv.org/abs/2609.26290))  
   **Summary:** This is the most directly relevant new paper: it attacks a subtle failure mode in causal tabular foundation models. Standard synthetic-pretraining labels encourage posterior shrinkage toward latent effects, but deployment often needs the finite-sample response of an estimator in a fixed population. The paper proposes **fluctuation-supervised pretraining**, labeling synthetic tables by both the ATE and efficient-influence-function fluctuation. The theory separates endpoint observability, finite-pretraining error, and irreducible deployment risk; experiments report large RMSE reductions under effect shift and expose weak-overlap failures.  
   **Why you should care:** It reframes causal tabular FM pretraining as learning the sampling law, not merely the latent estimand.

2. **xWhyL: Causal Interactive Learning**  
   **Authors:** Nicholas Tagliapietra, Florian Peter Busch, Moritz Willig, Matej Zečević, Lavdim Halilaj, Juergen Luettin, Kristian Kersting  
   **Venue/source:** arXiv cs.LG/stat.ML  
   **Publication/release date:** Submitted September 22, 2026  
   **Link:** arXiv record. ([arxiv.org](https://arxiv.org/abs/2609.26037))  
   **Summary:** xWhyL proposes a formal route from **explanations to causal learning**: expert explanations are treated as abductive signals that complement observational data for causal discovery. The appealing part is the “causal tug-of-war” framing—explanations can be wrong, so the learner must know when to reject rather than absorb them. This sits at an interesting intersection of XAI, causal discovery, weak supervision, and human-in-the-loop data science. If it holds up, it could give a principled interface for domain experts to guide causal structure learning without requiring them to specify full graphs.  
   **Why you should care:** It turns explanations from post-hoc artifacts into statistically meaningful causal evidence.

3. **Matryoshka Attribution: Learning to Attribute Language Model Outputs to Representations and Weights**  
   **Authors:** Aryaman Arora, Kirill Acharya, Nathan Hu, Yanzhe Zhang, Noah Goodman, Dan Jurafsky, Christopher Potts  
   **Venue/source:** arXiv cs.CL/cs.LG  
   **Publication/release date:** Submitted September 22, 2026  
   **Link:** arXiv record. ([arxiv.org](https://arxiv.org/abs/2609.25518))  
   **Summary:** MAttr formulates attribution as learning nested subsets of internal components that minimize downstream loss across sparsity levels. A differentiable sigmoid top-k mask learns an ordering of components by causal usefulness. The headline claims are strong: top leaderboard result on the Mechanistic Interpretability Benchmark, sparse transferable circuits across bases, and RL-trained masks that identify finetuning weight changes responsible for behavior. The refusal example—restoring 1% of Llama 3.1 8B Instruct weights toward base to remove refusals while maintaining capabilities—is provocative and likely to draw scrutiny.  
   **Why you should care:** It pushes interpretability toward trainable, objective-driven attribution rather than hand-designed circuit extraction.

4. **Databases with Missing Values that are Governed by Missingness Mechanisms**  
   **Authors:** Leopoldo Bertossi, Farouk Toumani  
   **Venue/source:** arXiv cs.DB  
   **Publication/release date:** Submitted September 22, 2026  
   **Link:** arXiv record. ([arxiv.org](https://arxiv.org/abs/2609.26692))  
   **Summary:** This paper gives relational databases with missing values a semantics in which missingness is governed by an explicit Bayesian-network “missingness graph” over database attributes. Rather than treating NULLs as isolated markers, the observed database plus missingness mechanism induces a block-independent probabilistic database. The authors define optimal possible-world classes for query answering that jointly capture probabilistic uncertainty and statistical plausibility, then study tractability and complexity. For data integration, record linkage, causal inference, and tabular ML, this is a useful reminder that missingness mechanisms belong in the data model, not just preprocessing.  
   **Why you should care:** It bridges database semantics, probabilistic databases, and statistically meaningful missing-data mechanisms.

5. **Interweaving Marginals into Multivariate Sample Paths: Training-Free Dependence Construction for Probabilistic Time Series Foundation Models**  
   **Authors:** Jinmyeong Choi, Jinkwan Jang, Seul Lee, Taesup Kim  
   **Venue/source:** arXiv cs.LG  
   **Publication/release date:** Submitted September 22, 2026  
   **Link:** arXiv record. ([arxiv.org](https://arxiv.org/abs/2609.25980))  
   **Summary:** Probabilistic time-series foundation models often produce coordinate-wise marginal predictive distributions, but downstream planning and risk tasks need coherent multivariate future sample paths. This paper isolates the dependence-construction problem: holding the empirical marginal sample multiset fixed at each channel-horizon coordinate, it studies training-free ways to weave marginals into joint trajectories. Historical temporal and channel relations improve dependence diagnostics, and the effect persists beyond the fixed-marginal constraint. The core insight is modular: a frozen TSFM may be good at marginal uncertainty while still needing a separate dependence-reconstruction layer.  
   **Why you should care:** It identifies a clean postprocessing problem for probabilistic structured-data FMs: restoring joint dependence without retraining.

## Section 2: Venue Watch

- **arXiv cs.LG/stat.ML/cs.DB new submissions for September 23, 2026.** The cs.LG page lists **118 new submissions** within **325 total entries** for the day; the cs.DB new page highlights enterprise agent memory, generated relational query context, auditable data sharing, and missingness-mechanism database semantics. The strongest clusters for Adam’s interests are causal-tabular pretraining, explanation-driven causal discovery, probabilistic time-series dependence reconstruction, mechanistic attribution, Bayesian optimization, and database governance/provenance for AI data workflows. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **JRSS B Volume 88, Issue 4, September 2026.** This is a dense statistics issue worth tracking broadly: particle filtering, sensitivity analysis combining randomized and nonrandomized studies, Bayesian quantile estimation with martingale posteriors, sparse causal instruments, high-dimensional Bayesian MCMC scalability, online kernel CUSUM, distribution-free changepoint detection, principal stratification, anytime-valid sequential tests, proximal causal inference, network interference, and double cross-fit doubly robust estimation. The causal/statistical inference concentration is unusually high and adjacent to several recent arXiv causal-ML threads. ([academic.oup.com](https://academic.oup.com/jrsssb/issue))

- **TMLR September 2026 status.** The visible TMLR September page remains dominated by items already tracked in the September 21–22 briefs: time-series modeling strategies, Stacked Feynman–Kac sampling for diffusion, priority-constrained descent, dimension-free self-normalized concentration, and later blocks on graph/LLM evaluation and RAG. I did not see a new bounded TMLR batch beyond the already-delivered September 22 snapshot in today’s crawl. ([jmlr.org](https://jmlr.org/tmlr/papers/))

## Section 3: Emerging Trends

- **Causal foundation models are moving from point estimands to sampling behavior.** FSP is notable because it asks pretrained causal tabular models to learn estimator fluctuations and coverage behavior, not just latent effects.

- **Human or model explanations are becoming training signals.** xWhyL is part of a broader shift from explanations-as-audit to explanations-as-data, with explicit concern for rejecting misspecified rationales.

- **Structured-data systems are absorbing governance.** Proof-of-retention, governed agent memory, and missingness-mechanism databases all treat provenance, policy, and uncertainty as executable data-system properties rather than documentation.

- **Foundation-model outputs increasingly need statistical postprocessing layers.** Time-series FMs need dependence reconstruction; tabular FMs need calibrated causal fluctuations; text-to-SQL with AI operators needs stochastic semantic evaluation.

- **Interpretability is becoming optimization-driven.** MAttr, recent SAE phase-diagram work, and circuit benchmarks all suggest a move away from static decompositions toward learned, task-scored attribution objects.

## Section 4: Worth Watching

- **Proof-of-Retention: A Framework for Auditable Cross-Organization Data Sharing** — Kyle MacMillan and Sanjay Krishnan propose an interactive protocol combining query witness generation and cryptographic proof-of-possession to make cross-organization data sharing auditable without full replication. This is highly relevant to data marketplaces, provenance, and regulated AI training-data pipelines. ([arxiv.org](https://arxiv.org/abs/2609.26654))

- **Generating Query Context for Relational Databases** — Alekh Jindal et al. automate generation of question–data-model pairs for natural-language database interfaces and report deployment across more than 50 real-world databases connected to Tursio. It is a concrete artifact direction for cold-start NL2SQL and BI agents. ([arxiv.org](https://arxiv.org/abs/2609.26200))

- **BOBA: Dynamic Bayesian Optimization through Bayesian Active Inference** — Merlin Angel Kelly et al. propose a free-energy-inspired acquisition function for nonstationary Bayesian optimization that explicitly reasons about uncertainty over future objective states. Worth tracking if dynamic BO and adaptive experimentation recur in Adam’s work. ([arxiv.org](https://arxiv.org/abs/2609.26021))

- **AkasicMEM: Governed Enterprise Memory for Agents** — The cs.DB stream describes an enterprise memory architecture with transitive lineage, policy composition during memory formation, and policy re-evaluation during retrieval over a vector–graph–relational substrate. This is another sign that agent memory is becoming a database-governance problem. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

## Section 5: Discord Highlights

**Sep 23 — Research brief highlights**

Top papers:
1. **Learning to Fluctuate** — causal tabular pretraining learns efficient-influence-function fluctuations, not just ATE labels.
2. **xWhyL** — expert explanations become formal causal-discovery signals, with rejection of misspecified beliefs.
3. **Matryoshka Attribution** — learned nested masks attribute LM outputs to representations and weights.
4. **Databases with Missing Values Governed by Missingness Mechanisms** — Bayesian missingness graphs give probabilistic semantics to incomplete relational DBs.
5. **Interweaving Marginals into Multivariate Sample Paths** — training-free dependence reconstruction for probabilistic time-series FMs.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-09-23","type":"paper","title":"Learning to Fluctuate: Statistical Foundations for Causal Tabular Pretraining","authors_or_org":"Zhiheng Zhang","url":"https://arxiv.org/abs/2609.26290","memory":"Top 5 paper. Covered Sep 22 2026 arXiv stat.ML/cs.LG paper on fluctuation-supervised pretraining for causal tabular foundation models using ATE plus efficient-influence-function fluctuations, endpoint observability theory, finite-pretraining bounds, and RMSE gains versus latent supervision/CausalPFN. Suppress future arXiv/code/venue/social reposts unless causal tabular pretraining framework or evidence materially expands."}
{"date_delivered":"2026-09-23","type":"paper","title":"xWhyL: Causal Interactive Learning","authors_or_org":"Nicholas Tagliapietra, Florian Peter Busch, Moritz Willig, Matej Zečević, Lavdim Halilaj, Juergen Luettin, Kristian Kersting","url":"https://arxiv.org/abs/2609.26037","memory":"Top 5 paper. Covered Sep 22 2026 arXiv paper formalizing learning causal models from explanations, causal tug-of-war rejection of misspecified explanations, and Causal Interactive Learning. Suppress future arXiv/code/venue/repost mentions unless theory or empirical system materially changes."}
{"date_delivered":"2026-09-23","type":"paper","title":"Matryoshka attribution: Learning to attribute language model outputs to representations and weights","authors_or_org":"Aryaman Arora, Kirill Acharya, Nathan Hu, Yanzhe Zhang, Noah Goodman, Dan Jurafsky, Christopher Potts","url":"https://arxiv.org/abs/2609.25518","memory":"Top 5 paper. Covered Sep 22 2026 arXiv cs.CL/cs.LG paper introducing MAttr, learned nested sigmoid-top-k masks for attribution across sparsities, Mechanistic Interpretability Benchmark leaderboard claim, sparse transferable circuits, and finetuning/refusal weight attribution. Suppress arXiv/code/project/venue/social reposts unless attribution method or evidence materially expands."}
{"date_delivered":"2026-09-23","type":"paper","title":"Databases with Missing Values that are Governed by Missingness Mechanisms","authors_or_org":"Leopoldo Bertossi, Farouk Toumani","url":"https://arxiv.org/abs/2609.26692","memory":"Top 5 paper and cs.DB item. Covered relational-database semantics for missing values governed by Bayesian-network missingness mechanisms, block-independent probabilistic DB construction, optimal possible-world classes for query answering, and tractability/complexity results. Suppress future arXiv/venue/repost mentions unless theory or implementation materially expands."}
{"date_delivered":"2026-09-23","type":"paper","title":"Interweaving Marginals into Multivariate Sample Paths: Training-Free Dependence Construction for Probabilistic Time Series Foundation Models","authors_or_org":"Jinmyeong Choi, Jinkwan Jang, Seul Lee, Taesup Kim","url":"https://arxiv.org/abs/2609.25980","memory":"Top 5 paper. Covered Sep 22 2026 arXiv paper on training-free coupling of frozen probabilistic TSFM coordinate-wise marginals into multivariate future sample paths, isolating dependence construction under fixed marginal sample multisets. Suppress future arXiv/code/venue/social reposts unless method or benchmark materially expands."}
{"date_delivered":"2026-09-23","type":"proceedings","title":"arXiv cs.LG/stat.ML/cs.DB new-submission stream for September 23 2026","authors_or_org":"arXiv cs.LG, stat.ML, cs.DB","url":"https://arxiv.org/list/cs.LG/new","memory":"Venue Watch. Covered Sep 23 2026 arXiv streams, especially 118 new cs.LG submissions out of 325 total and cs.DB items on governed enterprise memory, generated relational query context, proof-of-retention, and missingness-mechanism database semantics. Suppress repeat daily stream summary."}
{"date_delivered":"2026-09-23","type":"venue_issue","title":"Journal of the Royal Statistical Society Series B Volume 88 Issue 4 September 2026","authors_or_org":"Royal Statistical Society / Oxford Academic","url":"https://academic.oup.com/jrsssb/issue","memory":"Venue Watch. Covered September 2026 JRSSB issue themes: particle filtering, randomized/nonrandomized sensitivity analysis, Bayesian quantile martingale posteriors, sparse causal instruments, high-dimensional Bayesian MCMC, online kernel CUSUM, distribution-free changepoints, principal stratification, anytime-valid tests, proximal causal inference, network interference, and double cross-fit DR estimation. Suppress repeat issue summary."}
{"date_delivered":"2026-09-23","type":"resource","title":"Proof-of-Retention: A Framework for Auditable Cross-Organization Data Sharing","authors_or_org":"Kyle MacMillan, Sanjay Krishnan","url":"https://arxiv.org/abs/2609.26654","memory":"Worth Watching. Covered protocol for auditable cross-organization data sharing combining query witness generation and cryptographic proof-of-possession to verify retained provenance without full replication. Suppress future arXiv/code/venue mentions unless protocol, implementation, or evaluation materially changes."}
{"date_delivered":"2026-09-23","type":"paper","title":"Generating Query Context for Relational Databases","authors_or_org":"Alekh Jindal, Jyoti Pandey, Christina Pavlopoulou, Ronith PR, Sharath Prakash, Shi Qiao, Shivani Tripathi, Wangda Zhang","url":"https://arxiv.org/abs/2609.26200","memory":"Worth Watching. Covered automated generation of question-data-model context pairs for natural-language relational database interfaces, using query flows and weighted sampling, with reported deployment across more than 50 Tursio-connected databases. Suppress future arXiv/tool/venue reposts unless system or deployment evidence materially changes."}
{"date_delivered":"2026-09-23","type":"paper","title":"BOBA: Dynamic Bayesian Optimization through Bayesian Active Inference","authors_or_org":"Merlin Angel Kelly, Rishan Patel, Alexander Thomas, Ziyue Zhu, Zikun Quan, Tom Carlson, Youngjun Cho","url":"https://arxiv.org/abs/2609.26021","memory":"Worth Watching. Covered free-energy-inspired acquisition function for dynamic Bayesian optimization that reasons about uncertainty over future objective states in nonstationary environments. Suppress future arXiv/code/venue mentions unless BO theory, experiments, or applications materially expand."}
{"date_delivered":"2026-09-23","type":"software","title":"AkasicMEM: Governed Enterprise Memory for Agents","authors_or_org":"Jeongmin Bae, Yongjae Kim, Kyoung Hur, Donghyoung Han, Min-Soo Kim","url":"https://arxiv.org/abs/2609.25563","memory":"Worth Watching / cs.DB stream item. Covered governed enterprise agent memory with authorization continuity, transitive lineage, policy composition during memory formation, policy re-evaluation during retrieval, and vector-graph-relational substrate. Suppress future arXiv/tool/venue mentions unless system, artifact, or evaluation materially expands."}
```