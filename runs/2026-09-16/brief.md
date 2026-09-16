## Section 1: Top 5 Papers

1. **Beyond Distribution Matching: Semantics-Consistent Tabular Diffusion with Weak Semantic Priors**  
   **Authors:** Yili Wang, Ruxue Shi, Mengnan Du, Hangting Ye, Yi Chang, Xin Wang  
   **Venue/source:** arXiv cs.LG  
   **Release date:** September 13, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2609.16069))  
   This is the strongest structured-data item in today’s scan. The paper targets a real weakness in synthetic tabular generation: matching marginal/joint distributions is not enough if generated rows violate schema semantics or cross-column business rules. The proposed framework extracts weak intra-column and inter-column semantic priors with LLM assistance, validates them on the real training split, embeds values/columns/rules into a unified semantic space, and conditions the diffusion reverse process on those priors rather than using them as post-hoc filters. Experiments across six tabular benchmarks report gains in fidelity, semantic consistency, and downstream utility.  
   **Why you should care:** This is a useful step toward “semantics-aware” tabular generators that treat metadata and constraints as part of the generative object, not decoration.

2. **Agentic Search Spaces for Tabular Machine Learning**  
   **Authors:** Renat Sergazinov, Artem Chistyakov, Sergey Pankevich, Artem Babenko  
   **Venue/source:** arXiv cs.LG  
   **Release date:** September 14, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2609.16309))  
   Rather than asking agents to train tabular models directly, this paper asks whether LLM agents can expand the *search space* for established tabular learners. The authors decompose model families into modular pipelines—preprocessing, embeddings, architecture, training, inference—have agents propose candidate code modules, then let a conventional HPO routine optimize over both default hyperparameters and agent-proposed components. The results are modest but broad: improved performance for nearly every model family across 45 datasets, larger gains on small-to-medium regression, and transfer to TabArena Elo scores, with two agentic ensembles beating a conventional AutoGluon ensemble under the same tuning budget.  
   **Why you should care:** It suggests a pragmatic role for LLM agents in tabular ML: not replacing HPO, but enlarging the design space that HPO can search.

3. **Causal Discovery via Transformed Low-Rank Quantile Surfaces**  
   **Authors:** Ryo Kamimura, Thong Pham  
   **Venue/source:** arXiv stat.ME / cs.LG / stat.ML  
   **Release date:** September 15, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2609.16931))  
   This paper proposes Low-Rank Quantile Surfaces for bivariate causal discovery. The key assumption is asymmetric: in the causal direction, after an unknown monotone transformation, the conditional quantile surface has a low-rank functional decomposition; in the reverse direction, satisfying the same constraint is generically exceptional. This subsumes location-scale and post-nonlinear heteroscedastic noise models while allowing richer distributional-shape changes. The estimator alternates rank-constrained quantile-surface approximation with isotonic estimation of the transformation, yielding a causal score. The value is less in yet another benchmark score and more in broadening identifiability beyond mean/noise-shape assumptions.  
   **Why you should care:** Quantile-surface structure is a promising language for causal asymmetry when mechanisms affect more than conditional means or variances.

4. **Conformal Policy Learning with Distribution-Free Safety Guarantees**  
   **Authors:** Ying Jin, Naoki Egami  
   **Venue/source:** arXiv stat.ME / cs.LG / stat.ML  
   **Release date:** September 15, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2609.17296))  
   This paper reframes policy learning as a safety-constrained decision problem: maximize welfare while controlling the probability of assigning treatment to someone who would be harmed relative to control. The method tests counterfactual harm with conformal p-values, using observable proxies and selective calibration to handle the missing-potential-outcome problem. In randomized settings, it gives finite-sample distribution-free safety guarantees without outcome-model assumptions; with consistent outcome models it approaches optimal welfare under the safety constraint. For observational studies, the authors combine conformal policy learning with learn-then-balance weights for doubly robust safety guarantees.  
   **Why you should care:** This is a sharp bridge between conformal inference and causal policy learning, especially relevant for high-stakes HTE deployment.

5. **Verbalizing Subliminal Learning Effects Using Text Optimization**  
   **Authors:** Nathan Hu, Sanmi Koyejo, Christopher Potts  
   **Venue/source:** arXiv cs.LG / cs.CL  
   **Release date:** September 15, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2609.16927))  
   The paper addresses subliminal learning: traits transmitted through distillation data even when the dataset does not legibly encode them. The authors connect prompted subliminal learning to context distillation, show theoretically that the generated dataset can identify the teacher’s prompt, and introduce SALVE, which optimizes a soft prompt and then verbalizes it through the model with beam search. Empirically, SALVE recovers legible prompts naming teacher traits in standard subliminal-learning settings and detects effects in mixtures, activation-steered teacher data, and preference-data subsets selected by logit-linear criteria.  
   **Why you should care:** This gives a concrete auditing tool for hidden trait transfer in synthetic/distilled data pipelines—directly adjacent to data poisoning, privacy, and representation leakage.

## Section 2: Venue Watch

**arXiv cs.LG/stat.ML/cs.DB — September 16 new-submission stream.** The September 16 cs.LG page lists **98 new submissions** out of 277 total entries, stat.ML lists **8 new submissions**, and cs.DB lists **1 new database submission** plus cross-lists/replacements. The day’s strongest clusters are tabular synthesis with semantic constraints, agent-designed tabular search spaces, causal and conformal policy learning, flow-matching optimization, LLM/agent verification environments, KV-cache reliability, and query-containment theory. The noteworthy database-theory item is **How Can We Shrink the Family of Test Databases?**, which attacks containment/equivalence for conjunctive queries with SQL nulls and order comparisons by reducing the family of test databases to FPT-sized families under local parameters. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

**TMLR September 2026 incremental activity.** TMLR’s top-of-page September stream has moved again since the September 15 brief. New visible items include **Reinforcement Learning for LLM Post-Training: A Survey**, **Low-Rank Geometry for Zeroth-Order Fine-Tuning of Black-Box LLMs** with J2C certification, **Vector Memory and Role-Conditioned Multi-Agent Systems**, **EEG-EyeTrack** as a time-series/functional-data benchmark, **R3: Robust Rubric-Agnostic Reward Models**, **LLM-guided Hierarchical Search for End-to-end Reasoning Intensive Retrieval**, and **Pathway to O(√d) Complexity Bound under Wasserstein Metric of Flow-Based Models**. The current TMLR September issue-stream remains unusually agent-heavy, with parallel threads in retrieval, reward modeling, zeroth-order adaptation, benchmarks, diffusion/flow theory, and memory mechanisms. ([jmlr.org](https://jmlr.org/tmlr/papers/))

**Database theory and query verification.** The cs.DB stream is quiet but high-signal: the new Sternbach–Cohen query-containment paper is a reminder that LLM-assisted SQL rewriting, semantic query compilation, and database-agent correctness still depend on hard classical equivalence machinery. Its focus on null semantics and comparisons is especially relevant because these are precisely the SQL details that agentic data-analysis systems tend to erase when they reason at the natural-language or relational-algebra sketch level. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

## Section 3: Emerging Trends

- **Tabular generation is shifting from distributional fidelity to semantic validity.** Recent work is converging on the idea that synthetic tabular rows must satisfy weak metadata-derived rules, domain constraints, and task-specific query behavior—not just two-sample or downstream metrics.

- **LLM agents are becoming design-space expanders rather than end-to-end learners.** The stronger agentic tabular result today uses agents to propose modules/search spaces, then lets classical HPO do the optimization. This is a healthier division of labor than asking an agent to own the whole modeling loop.

- **Causal ML is absorbing conformal and representation tools.** Conformal policy learning, low-rank quantile-surface causal discovery, and recent CATE representation papers all point toward causal procedures with explicit safety, identifiability, or compression guarantees.

- **Interpretability is moving from detecting hidden states to verbalizing hidden training signals.** SALVE fits a growing line of work that asks whether latent or subliminal model properties can be made legible enough to audit.

- **Flow/diffusion theory is getting more optimization-aware.** The “same objective, different path” result for flow matching reinforces a broader theme: schedule/path/design choices can change optimization variance and convergence even when the population objective is unchanged.

## Section 4: Worth Watching

- **Same Flow, Different Paths: Variance Reduction in Flow Matching** — Alexander Tyurin. Worth suppressing and revisiting if code or follow-up experiments appear: it shows that different coupling paths with the same marginal flow-matching objective can yield different SGD convergence rates, and formulates path selection as a constrained variance-minimization problem. ([arxiv.org](https://arxiv.org/abs/2609.17287))

- **Differentially Private Semantic Plans for Aggregate Insight Generation** — Behrooz Razeghi. DP-SPIN releases noisy semantic plans over predefined concepts and has an LLM produce only post-processed summaries checked by a verifier; relevant to private data analysis agents and DP reporting from unstructured records. ([arxiv.org](https://arxiv.org/abs/2609.16283))

- **How Can We Shrink the Family of Test Databases? Query Containment with Nulls and Comparisons** — Helen Sternbach, Sara Cohen. Important for future SQL-agent verification and semantic-query rewriting; the paper reduces otherwise exponential containment tests using structure in null variables and comparison conflicts. ([arxiv.org](https://arxiv.org/abs/2609.16218))

- **EEG-EyeTrack: A Benchmark for Time Series and Functional Data Analysis with Open Challenges and Baselines** — Florian Heinrichs, Tiago Vasconcelos Afonso. A new TMLR benchmark likely to be useful for time-series foundation-model evaluation beyond standard forecasting. ([jmlr.org](https://jmlr.org/tmlr/papers/))

- **Low-Rank Geometry for Zeroth-Order Fine-Tuning of Black-Box Large Language Models** — Zichen Song, Weijia Li. TMLR September item with J2C certification; likely relevant to black-box adaptation, LoRA geometry, and optimizer-free/gradient-free fine-tuning. ([jmlr.org](https://jmlr.org/tmlr/papers/))

## Section 5: Discord Highlights

**Sep 16 brief — Top 5 papers**

1. **Beyond Distribution Matching: Semantics-Consistent Tabular Diffusion with Weak Semantic Priors** — tabular diffusion conditioned on LLM-extracted semantic rules, not just post-hoc filtering.  
2. **Agentic Search Spaces for Tabular Machine Learning** — LLM agents expand tabular HPO design spaces; classical HPO does the optimization.  
3. **Causal Discovery via Transformed Low-Rank Quantile Surfaces** — new causal asymmetry assumption based on transformed low-rank conditional quantile surfaces.  
4. **Conformal Policy Learning with Distribution-Free Safety Guarantees** — finite-sample safety control for treatment policies via conformal p-values.  
5. **Verbalizing Subliminal Learning Effects Using Text Optimization** — SALVE turns hidden distillation traits into legible prompts for auditing.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-09-16","type":"paper","title":"Beyond Distribution Matching: Semantics-Consistent Tabular Diffusion with Weak Semantic Priors","authors_or_org":"Yili Wang, Ruxue Shi, Mengnan Du, Hangting Ye, Yi Chang, Xin Wang","url":"https://arxiv.org/abs/2609.16069","memory":"Top 5 paper. Covered Sep 13 2026 arXiv paper on semantics-consistent tabular diffusion using LLM-extracted intra-column semantics and inter-column symbolic rules as generation conditions rather than post-hoc filters. Suppress arXiv/code/venue/social reposts unless semantic-prior framework, benchmark, or artifact materially expands."}
{"date_delivered":"2026-09-16","type":"paper","title":"Agentic Search Spaces for Tabular Machine Learning","authors_or_org":"Renat Sergazinov, Artem Chistyakov, Sergey Pankevich, Artem Babenko","url":"https://arxiv.org/abs/2609.16309","memory":"Top 5 paper. Covered Sep 14 2026 arXiv paper using LLM agents to propose modular tabular ML pipeline components/search spaces, then classical HPO optimizes them; evaluated on 45 datasets and TabArena. Suppress future arXiv/code/venue reposts unless search-space design or empirical scope materially changes."}
{"date_delivered":"2026-09-16","type":"paper","title":"Causal Discovery via Transformed Low-Rank Quantile Surfaces","authors_or_org":"Ryo Kamimura, Thong Pham","url":"https://arxiv.org/abs/2609.16931","memory":"Top 5 paper. Covered Sep 15 2026 arXiv stat.ME/cs.LG paper proposing LRQS for bivariate causal discovery via transformed low-rank conditional quantile surfaces, generic identifiability, isotonic transformation estimation, and nonparametric causal score. Suppress future versions unless causal identifiability, algorithm, or evaluations materially expand."}
{"date_delivered":"2026-09-16","type":"paper","title":"Conformal Policy Learning with Distribution-Free Safety Guarantees","authors_or_org":"Ying Jin, Naoki Egami","url":"https://arxiv.org/abs/2609.17296","memory":"Top 5 paper. Covered Sep 15 2026 arXiv paper on treatment policy learning with conformal p-values for counterfactual harm, finite-sample distribution-free safety guarantees in randomized experiments, and doubly robust observational extension. Suppress arXiv/code/venue reposts unless safety guarantee or causal policy framework materially changes."}
{"date_delivered":"2026-09-16","type":"paper","title":"Verbalizing Subliminal Learning Effects Using Text Optimization","authors_or_org":"Nathan Hu, Sanmi Koyejo, Christopher Potts","url":"https://arxiv.org/abs/2609.16927","memory":"Top 5 paper. Covered Sep 15 2026 arXiv paper introducing SALVE for recovering legible prompts/traits transmitted through subliminal learning or context distillation datasets using soft-prompt optimization and verbalization. Suppress future arXiv/code/venue/social repeats unless auditing method or empirical settings materially expand."}
{"date_delivered":"2026-09-16","type":"proceedings","title":"arXiv cs.LG/stat.ML/cs.DB new-submission stream for September 16 2026","authors_or_org":"arXiv cs.LG, stat.ML, cs.DB","url":"https://arxiv.org/list/cs.LG/new","memory":"Venue Watch. Covered Sep 16 2026 arXiv streams: cs.LG 98 new submissions out of 277 total, stat.ML 8 new submissions out of 37, and cs.DB 1 new submission out of 6 total; themes in tabular semantic synthesis, agentic tabular search spaces, causal/conformal policy learning, flow-matching optimization, KV-cache reliability, and query containment. Suppress repeat daily broad stream summary."}
{"date_delivered":"2026-09-16","type":"proceedings","title":"TMLR September 2026 accepted papers incremental update as of September 16","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered visible Sep 16 TMLR September top-of-page additions beyond Sep 15 snapshot: Reinforcement Learning for LLM Post-Training survey, Low-Rank Geometry for Zeroth-Order Fine-Tuning with J2C, Vector Memory and Role-Conditioned Multi-Agent Systems, EEG-EyeTrack, R3 reward models, LLM-guided hierarchical search, complex symbolic regression, and Wasserstein flow-model complexity. Suppress repeat Sep 16 incremental snapshot."}
{"date_delivered":"2026-09-16","type":"paper","title":"How Can We Shrink the Family of Test Databases? Query Containment with Nulls and Comparisons","authors_or_org":"Helen Sternbach, Sara Cohen","url":"https://arxiv.org/abs/2609.16218","memory":"Venue Watch and Worth Watching. Covered Sep 14 2026 cs.DB paper on query containment/equivalence for conjunctive queries with SQL nulls and order comparisons, shrinking exponential test-database families via local parameters and canonical values. Suppress future arXiv/venue/tool reposts unless theory or implementation materially expands."}
{"date_delivered":"2026-09-16","type":"paper","title":"Same Flow, Different Paths: Variance Reduction in Flow Matching","authors_or_org":"Alexander Tyurin","url":"https://arxiv.org/abs/2609.17287","memory":"Worth Watching. Covered Sep 15 2026 arXiv paper showing flow-matching path choice can change SGD variance and convergence while preserving the same marginal objective; introduces PathOpt_theta constrained variance-minimization formulation. Suppress future versions unless theory, algorithms, or experiments materially expand."}
{"date_delivered":"2026-09-16","type":"paper","title":"Differentially Private Semantic Plans for Aggregate Insight Generation","authors_or_org":"Behrooz Razeghi","url":"https://arxiv.org/abs/2609.16283","memory":"Worth Watching. Covered DP-SPIN framework for differentially private aggregate semantic measurement and LLM summarization from released semantic plans with public verification of mentions, values, comparisons, and rank claims. Suppress arXiv/code/venue reposts unless privacy mechanism, verifier, or applications materially change."}
{"date_delivered":"2026-09-16","type":"benchmark","title":"EEG-EyeTrack: A Benchmark for Time Series and Functional Data Analysis with Open Challenges and Baselines","authors_or_org":"Florian Heinrichs, Tiago Vasconcelos Afonso; TMLR","url":"https://jmlr.org/tmlr/papers/","memory":"Worth Watching TMLR September 2026 benchmark/resource item. Covered as newly visible TMLR benchmark for time-series and functional-data analysis with EEG and eye-tracking data. Suppress TMLR/OpenReview/code reposts unless benchmark artifact or results materially expand."}
{"date_delivered":"2026-09-16","type":"paper","title":"Low-Rank Geometry for Zeroth-Order Fine-Tuning of Black-Box Large Language Models","authors_or_org":"Zichen Song, Weijia Li; TMLR","url":"https://jmlr.org/tmlr/papers/","memory":"Worth Watching TMLR September 2026 item with J2C certification. Covered as black-box LLM adaptation / zeroth-order fine-tuning paper likely relevant to low-rank geometry and PEFT without gradients. Suppress TMLR/OpenReview/code reposts unless selected for deeper coverage or materially revised."}
```