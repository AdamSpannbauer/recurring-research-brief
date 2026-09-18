## Section 1: Top 5 Papers

1. **Parallelism, critical windows, and separations among diffusion language models**  
   **Authors:** Sitan Chen, Liye Wang  
   **Venue/source:** arXiv  
   **Release date:** September 18, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   This is the strongest theory item in today’s stream. The paper gives a fine-grained comparison of masked, uniform, and Gaussian diffusion language models through the lens of parallel sampling complexity. The key object is *dual total correlation*, which can make the number of required forward passes far smaller than context length. More strikingly, the authors prove a separation: for some random empirical measures, uniform/Gaussian diffusion need roughly \(\sqrt d\) passes, while masked diffusion can need \(\Omega(d)\), due to narrower critical sampling windows. This sharpens the usually hand-wavy “diffusion LMs are parallel” claim into an analyzable computational-statistical distinction.  
   **Why you should care:** This may become a reference point for deciding which discrete diffusion interface is theoretically worth scaling.

2. **Learn Your Own Thoughts: Abstract Token Curriculum**  
   **Authors:** Khashayar Gatmiry, Avrajit Ghosh, Parsa Mirtaheri, Jason D. Lee, Nika Haghtalab, Emmanuel Abbe, Peter Bartlett  
   **Venue/source:** arXiv  
   **Release date:** September 18, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/list/stat.ML/new))  
   This paper attacks the supervision bottleneck in chain-of-thought by training models to develop continuous intermediate “thought” representations through a curriculum rather than explicit scratchpad labels. The theoretical core studies parity learning with single-layer softmax attention and shows how a curriculum can make attention concentrate on intermediate tokens that give the easiest path to prediction. Experiments on graph reachability and arithmetic are still controlled rather than frontier-scale, but the idea is clean: induce latent reasoning structure from distributional progression, not annotated rationales.  
   **Why you should care:** It is a plausible bridge between representation-learning theory, latent reasoning, and post-CoT training methods.

3. **Efficiently Linking Unstructured Data for Multi-step Reasoning**  
   **Authors:** Jiaming Liang, Haydn Jones, Jacob R. Gardner, Mark Yatskar, Zachary Ives  
   **Venue/source:** arXiv / cs.DB  
   **Release date:** September 18, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/list/cs.DB/new))  
   DASE is a database-system response to a real bottleneck in data-agent and scientific-discovery workflows: retrieving evidence tuples that jointly satisfy structured predicates, relational joins, multiple vector similarities, and thresholded semantic joins. The system introduces a multi-step reasoning query model, SemJI sparse materialized embedding-similarity joins for rare near-neighbor pairs, and predicate-aware ANN traversal with threshold-based aggregation. The reported scientific-discovery workloads show 6–46× faster evidence retrieval at comparable recall, and in semantic-operator settings DASE acts as a high-recall prefilter that can improve quality while cutting LLM evaluation cost.  
   **Why you should care:** This is exactly the kind of hybrid relational/vector/semantic execution substrate that data agents will need if they are to move beyond toy tables.

4. **Null importance: Disentangling relevance for interpretable machine learning**  
   **Authors:** Garvesh Raskutti, Kris Sankaran, Jiaxin Ye  
   **Venue/source:** arXiv / submitted to *Statistical Science*  
   **Release date:** September 18, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/list/stat.ML/new))  
   The paper proposes “null importance” as a unifying language for feature relevance, distinguishing marginal relevance, conditional relevance, predictive-risk relevance, functional invariance, and causal-effect relevance. The contribution is not another attribution score; it is a taxonomy and set of equivalence/counterexample results clarifying which scientific questions different feature-importance procedures answer. The applications to fairness and genomic perturbation modeling are well chosen because both domains routinely conflate predictive, structural, and causal relevance. For interpretability work on tabular, biological, and multimodal models, this is a useful corrective to feature-attribution overclaiming.  
   **Why you should care:** It gives a statistical vocabulary for saying what an “important feature” actually means before choosing an explanation method.

5. **Prediction-Powered Smoothing and Validation for Disaggregated AI Evaluation**  
   **Authors:** Sho Kawano, Zehang Richard Li, Paul A. Parker  
   **Venue/source:** arXiv  
   **Release date:** September 18, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/list/stat.ML/new))  
   This paper treats AI-system evaluation as finite-population estimation with many low-sample domains—task types, conversation types, agent traffic slices—where direct estimates and standard prediction-powered inference are noisy. The proposed prediction-powered smoothing workflow borrows strength across domains using a Bayesian small-area model, with a taxonomy-aware extension, and introduces an approximately unbiased design-based cross-validation score for choosing between direct and smoothed estimators. The evaluation includes both a verifiable benchmark and deployed agent traffic graded by humans, with near-nominal coverage and better domain-level intervals.  
   **Why you should care:** It is a statistically mature answer to a practical problem: how to audit heterogeneous AI performance without labeling everything.

## Section 2: Venue Watch

- **arXiv Sep. 18 stream: unusually dense in theory, agent systems, and data infrastructure.** The cs.LG new-submission page listed 107 new submissions out of 304 total entries; stat.ML listed 9 new submissions out of 46; cs.DB listed 3 new submissions out of 12. The most relevant clusters were diffusion-LM theory, latent reasoning curricula, context/memory audits, Bayesian and policy-evaluation statistics, semantic/vector/relational query engines, and machine-readable dataset-policy semantics. Notable non–Top-5 items include EPIG-Tree for compute-optimal rollout branching in RL, Compressed Active Subspaces for scalable Bayesian inference, Stable Policy Learning, and the Croissant policy-profile paper. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **TMLR September 2026 incremental update.** The top of the TMLR accepted-papers page has a fresh batch beyond the Sep. 17 snapshot. The strongest Adam-relevant items are **Benchmarking Tabular Foundation Models for Conditional Density Estimation in Regression**, **MiloNet: A Framework for Traceable and Verified RAG**, **LLMs Can Leverage Graph Structural Information in Text-Attributed Graphs**, and **Few-Shot Closed-Loop Neural System Identification via Meta-Learning**. Also worth noting: **RESIST** received a Featured certification, and the batch includes clustering model selection, time-series augmentation, GPU attention kernels, Gaussian-input-masking theory, and sample-efficient test-time scaling. ([jmlr.org](https://jmlr.org/tmlr/papers/))

- **cs.DB signal: retrieval systems are converging on certified hybrid semantics.** Today’s cs.DB submissions are not just “vector search plus filters”; they emphasize completeness, freshness, and multi-step evidence assembly. DASE is the strongest systems paper, while **FRESH-GEORANGE** explores certified semantic-spatial range retrieval with deterministic recall lower bounds, and **Resolution limits for process comparison from event data** argues that some concurrency/sequentiality distinctions are unrecoverable from ordinary event-log stochastic languages unless different evidence is recorded. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

## Section 3: Emerging Trends

- **Theoretical diffusion-language-model work is moving from “parallel generation” slogans to complexity separations.** Recent papers are formalizing which diffusion interface buys what kind of parallelism, and today’s Chen–Wang result is the clearest separation so far. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **Data-agent infrastructure is becoming database-native again.** DASE, MiloNet, Croissant policy profiles, and FRESH-GEORANGE all point toward a stack where retrieval, policy, provenance, verification, and freshness are typed execution concerns, not prompt-engineering conventions. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

- **Evaluation is becoming a statistical estimation problem under budget, heterogeneity, and interaction.** Prediction-powered smoothing, fixed-rollout/pass@k identifiability work from recent briefs, and today’s candidate-generation/system-cost study all push against single aggregate benchmark scores. ([arxiv.org](https://arxiv.org/list/stat.ML/new))

- **Interpretability is broadening from attribution artifacts to relevance semantics.** Null importance is especially useful because it separates predictive, conditional, invariant, and causal notions of importance before a method is chosen. ([arxiv.org](https://arxiv.org/list/stat.ML/new))

- **Context/memory audits are probing future-sufficiency, not just current correctness.** The “Correct Now, Insufficient Later” paper is a useful warning: a compressed memory may answer today’s query while discarding distinctions needed after a future update. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

## Section 4: Worth Watching

- **A Policy Profile for Croissant: Refusal as a Property of the Dataset** — a concrete decision-procedure layer for dataset-use conditions in Croissant descriptors, with conformance corpora and microsecond-scale gate checks. This is worth tracking because dataset-policy semantics will matter for automated data pipelines and AI agents. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

- **FRESH-GEORANGE** — a small but conceptually sharp pilot for certified freshness-aware semantic-spatial range retrieval; exact mode gets full set recall, while certified early stopping reports deterministic query-specific lower bounds. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

- **EPIG-Tree** — allocates rollout branches where they most reduce policy-gradient uncertainty per compute unit, with law-of-total-variance allocation rules and agent/RL experiments. It is a useful counterpoint to entropy-based branching heuristics. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **Compressed Active Subspaces for Scalable Bayesian Inference** — compresses parameter space with structured isometric embeddings before active-subspace construction, targeting Bayesian uncertainty for large models where storing gradients is prohibitive. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **Benchmarking Tabular Foundation Models for Conditional Density Estimation in Regression** — newly visible TMLR September item with code; useful because most tabular-FM evaluation still overemphasizes point prediction rather than calibrated conditional distributions. ([jmlr.org](https://jmlr.org/tmlr/papers/))

## Section 5: Discord Highlights

**Sep. 18 brief — Top 5 papers**

1. **Parallelism, critical windows, and separations among diffusion language models** — first-principles separation of masked vs uniform/Gaussian diffusion LM parallelism.  
2. **Learn Your Own Thoughts: Abstract Token Curriculum** — curriculum-induced continuous latent “thoughts” without CoT supervision.  
3. **Efficiently Linking Unstructured Data for Multi-step Reasoning** — DASE hybrid relational/vector/semantic engine for evidence retrieval.  
4. **Null importance: Disentangling relevance for interpretable machine learning** — statistical taxonomy of what feature “importance” can mean.  
5. **Prediction-Powered Smoothing and Validation for Disaggregated AI Evaluation** — small-area/PPI workflow for domain-level AI evaluation under labeling budgets.  

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-09-18","type":"paper","title":"Parallelism, critical windows, and separations among diffusion language models","authors_or_org":"Sitan Chen, Liye Wang","url":"https://arxiv.org/abs/2609.20539","memory":"Top 5 paper. Covered Sep 18 2026 arXiv theory paper comparing masked, uniform, and Gaussian diffusion language models; dual total correlation forward-pass scaling; sqrt(d) vs Omega(d) separation due to narrower masked-diffusion critical windows. Suppress future arXiv/code/venue/social reposts unless theory materially changes."}
{"date_delivered":"2026-09-18","type":"paper","title":"Learn Your Own Thoughts: Abstract Token Curriculum","authors_or_org":"Khashayar Gatmiry, Avrajit Ghosh, Parsa Mirtaheri, Jason D. Lee, Nika Haghtalab, Emmanuel Abbe, Peter Bartlett","url":"https://arxiv.org/abs/2609.19717","memory":"Top 5 paper. Covered Sep 18 2026 arXiv paper on Abstract Token Curriculum for eliciting continuous latent reasoning/thought representations without explicit chain-of-thought supervision; theory for parity with softmax attention and experiments on graph reachability/arithmetic. Suppress future arXiv/code/venue reposts unless objective, theory, or evidence materially expands."}
{"date_delivered":"2026-09-18","type":"paper","title":"Efficiently Linking Unstructured Data for Multi-step Reasoning","authors_or_org":"Jiaming Liang, Haydn Jones, Jacob R. Gardner, Mark Yatskar, Zachary Ives","url":"https://arxiv.org/abs/2609.19491","memory":"Top 5 paper and cs.DB item. Covered DASE query engine for multi-step reasoning over structured predicates, multiple vectors, relational links, thresholded semantic joins, SemJI sparse materialized embedding-similarity join index, and predicate-aware ANN execution. Suppress future arXiv/venue/code/social repeats unless system or evaluation materially changes."}
{"date_delivered":"2026-09-18","type":"paper","title":"Null importance: Disentangling relevance for interpretable machine learning","authors_or_org":"Garvesh Raskutti, Kris Sankaran, Jiaxin Ye","url":"https://arxiv.org/abs/2609.19511","memory":"Top 5 paper. Covered null-importance framework separating marginal, conditional, predictive-risk, functional-invariance, and causal-effect notions of feature relevance; applications to fairness and genomic perturbation modeling. Suppress future arXiv/Statistical Science/code/venue reposts unless framework or results materially change."}
{"date_delivered":"2026-09-18","type":"paper","title":"Prediction-Powered Smoothing and Validation for Disaggregated AI Evaluation","authors_or_org":"Sho Kawano, Zehang Richard Li, Paul A. Parker","url":"https://arxiv.org/abs/2609.20758","memory":"Top 5 paper. Covered finite-population/small-area evaluation workflow combining prediction-powered inference with Bayesian smoothing and design-based cross-validation for disaggregated AI/agent evaluation under label budgets. Suppress future arXiv/code/venue reposts unless theory or evaluation evidence materially expands."}
{"date_delivered":"2026-09-18","type":"proceedings","title":"arXiv cs.LG/stat.ML/cs.DB new-submission stream for September 18 2026","authors_or_org":"arXiv cs.LG, stat.ML, cs.DB","url":"https://arxiv.org/list/cs.LG/new","memory":"Venue Watch. Covered Sep 18 2026 arXiv streams: cs.LG 107 new submissions out of 304 entries, stat.ML 9 new out of 46, cs.DB 3 new out of 12; themes in diffusion-LM theory, latent reasoning curricula, context/memory audits, Bayesian and policy-evaluation statistics, semantic/vector/relational query engines, and dataset-policy semantics. Suppress repeat daily broad stream summary."}
{"date_delivered":"2026-09-18","type":"proceedings","title":"TMLR September 2026 accepted papers incremental update as of September 18","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered visible Sep 18 TMLR September top-of-page additions beyond Sep 17 snapshot: Efficient Multi-Scale Deformable Attention on GPUs; LLMs Can Leverage Graph Structural Information in Text-Attributed Graphs; Few-Shot Closed-Loop Neural System Identification; RESIST Featured; Meta-Learned Surrogates for Clustering Model Selection; MiloNet; Benchmarking Tabular Foundation Models for Conditional Density Estimation; ASCENSION and related items. Suppress repeat Sep 18 incremental snapshot."}
{"date_delivered":"2026-09-18","type":"paper","title":"A Policy Profile for Croissant: Refusal as a Property of the Dataset","authors_or_org":"Alexander Chernov","url":"https://arxiv.org/abs/2609.19640","memory":"Worth Watching and cs.DB cross-list. Covered additive Croissant dataset-policy profile specifying decision procedures for permitted operations and data-use conditions, conformance corpora, nf-core pipeline gate examples, and ODRL-aligned usageInfo evidence. Suppress future arXiv/Zenodo/venue reposts unless policy semantics or implementation materially expands."}
{"date_delivered":"2026-09-18","type":"paper","title":"A Functional Pilot for Certified Freshness-Aware Semantic--Spatial Range Retrieval","authors_or_org":"Taimoor Ahmad","url":"https://arxiv.org/abs/2609.19855","memory":"Worth Watching and cs.DB item. Covered FRESH-GEORANGE pilot for semantic-spatial range retrieval with source-watermark freshness, semantic microblock pruning bounds, exact and certified modes, deterministic recall lower bounds, and OpenFlights CPU pilot. Suppress future arXiv/code/venue mentions unless benchmark, system, or certification materially changes."}
{"date_delivered":"2026-09-18","type":"paper","title":"EPIG-Tree: Compute-Optimal Branching for Gradient-Efficient Reinforcement Learning","authors_or_org":"Nikita Khomich, Leopold Hermansson, Ido Hakimi","url":"https://arxiv.org/abs/2609.20004","memory":"Worth Watching. Covered rollout-branch allocation for policy-gradient estimation using law-of-total-variance decomposition and EPIG-Tree uncertainty-per-compute scores; includes cloned-state control, frozen-LLM gradient calibration, online math, and multi-turn Wordle. Suppress future arXiv/code/venue reposts unless method or empirical evidence materially expands."}
{"date_delivered":"2026-09-18","type":"paper","title":"Compressed Active Subspaces for Scalable Bayesian Inference","authors_or_org":"Thomas Flynn, Sanket Jantre, Byung-Jun Yoon, Kibaek Kim","url":"https://arxiv.org/abs/2609.19539","memory":"Worth Watching. Covered CAS, which constructs active subspaces in compressed parameter coordinates using structured isometric embeddings to reduce memory for Bayesian uncertainty in large models. Suppress future arXiv/code/venue mentions unless inference method or scalability evidence materially changes."}
{"date_delivered":"2026-09-18","type":"benchmark","title":"Benchmarking Tabular Foundation Models for Conditional Density Estimation in Regression","authors_or_org":"Rafael Izbicki, Pedro L. C. Rodrigues; TMLR","url":"https://jmlr.org/tmlr/papers/","memory":"Worth Watching and TMLR September 2026 item. Covered newly visible TMLR accepted paper with code on evaluating tabular foundation models for conditional density estimation in regression, shifting TFM evaluation beyond point prediction. Suppress future TMLR/OpenReview/code reposts unless selected for deeper Top 5 coverage or benchmark materially expands."}
{"date_delivered":"2026-09-18","type":"software","title":"MiloNet: A Framework for Traceable and Verified RAG","authors_or_org":"Yangfan Jiang, Richard M. Bailey; TMLR","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch / Worth Watching TMLR September 2026 item. Covered as newly visible framework for traceable and verified retrieval-augmented generation, adjacent to provenance and data-agent reliability. Suppress future TMLR/OpenReview/code mentions unless artifact or method materially expands."}
```