## Section 1: Top 5 Papers

1. **CausalDS: Benchmarking Causal Reasoning in Data-Science Agents**  
   **Authors:** Andrej Leban, Yuekai Sun  
   **Venue/source:** arXiv; accompanying Hugging Face dataset  
   **Date:** July 9, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2607.08093))  
   **Summary:** CausalDS is a particularly relevant benchmark because it joins three evaluation regimes that are usually separated: symbolic causal reasoning, realistic data-science tool use, and structured synthetic data generation. Each task is generated from a sampled SCM, paired with observational data and a graph-faithful natural-language story, and spans Pearl-style prediction, intervention, and counterfactual tasks. It also scores abstention when no warranted causal answer exists. The released HF artifact includes a frozen 100-task main exam plus seeding/observation-layer variants, making it concrete enough to affect agent evaluation.  
   **Why you should care:** It is a strong candidate for the “causal data-science agent” benchmark people will cite when testing whether agents can do causal inference rather than merely narrate it.

2. **In-Context Time Series Classification with Random Convolutional Features**  
   **Authors:** Joscha Cüppers, Jilles Vreeken  
   **Venue/source:** arXiv  
   **Date:** July 21, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2607.19234))  
   **Summary:** The paper proposes **MASHT**, a deliberately simple bridge between time-series classification and tabular foundation models: transform sequences with MultiRocket/Hydra random convolutional features, then hand the resulting tabular representation to an in-context tabular FM. The key result is not architectural novelty but a useful reframing: time-series foundation modeling can sometimes be decomposed into strong handcrafted/random feature extraction plus zero-shot tabular inference. Reported results match strong univariate baselines and remain competitive in multivariate settings, without task-specific model training.  
   **Why you should care:** It is a clean test of how far tabular FMs can be extended by representation engineering rather than by building modality-specific foundation models.

3. **Provable diffusion-based posterior sampling for linear inverse problems via DDIM**  
   **Authors:** Yuchen Jiao, Na Li, Changxiao Cai, Yuxin Chen, Gen Li  
   **Venue/source:** arXiv  
   **Date:** July 21, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2607.19333))  
   **Summary:** This paper gives a lightweight posterior sampler for noisy linear inverse problems with diffusion priors. The method modifies DDIM updates coordinate-wise along singular directions of the measurement operator: follow the learned diffusion prior when observation SNR is weak, and switch to a calibrated measurement predictor when the observation is strong. The contribution is attractive because it converts a difficult posterior-sampling problem into simple DDIM-style updates while proving convergence to the Bayesian posterior. Empirically, it compares favorably on image restoration tasks.  
   **Why you should care:** It is part of the continuing convergence between generative modeling and statistically principled posterior computation.

4. **Circuit Claims Depend on What Is Extracted and How It Is Compared**  
   **Authors:** Yang Sheng, Jie Fu  
   **Venue/source:** arXiv  
   **Date:** July 21, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2607.18921))  
   **Summary:** This is a useful corrective for mechanistic interpretability. The authors argue that “the circuit” found by extraction is underdetermined: different extraction objects, pruning thresholds, and comparison granularities can preserve behavior but produce low-overlap circuits. They demonstrate this in a synthetic Lean tactic-prediction benchmark with dense and weight-sparse transformer checkpoints. Fine-grained edge overlap can approach random baseline, while coarser summaries such as selected attention heads are more stable. The paper ends with reporting recommendations for circuit-extraction studies.  
   **Why you should care:** It sharpens the standard of evidence for circuit claims, especially as circuit discovery moves from toy settings into automated tooling.

5. **Elicitation without Backpropagation: Steering Model Behavior by Optimizing the Latent Posterior**  
   **Authors:** Garrett Baker, Vinayak Pathak, Daniel Murfet, Susan Wei  
   **Venue/source:** arXiv  
   **Date:** July 21, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2607.18804))  
   **Summary:** In exact Bayes-filtered transformer settings, the paper treats next-token prediction as a posterior mixture over latent predictive models and introduces **Posterior Prefix Tuning**. Instead of backpropagating through the transformer, PPT samples from the prior once, then optimizes a distribution over hard prompts by importance sampling against those utility-independent prior samples. The experiments are stylized—Beta–Bernoulli and reinforced-urn BFTs, plus utility families such as frequency matching and Dyck validity—but the conceptual move is elegant: behavior elicitation as posterior optimization, not model editing.  
   **Why you should care:** It offers a Bayesian lens on prompt optimization and could inspire more principled elicitation methods for in-context learners.

## Section 2: Venue Watch

- **arXiv cs.LG/stat.ML July 22 stream.** The July 22 cs.LG listing is unusually large—177 entries shown for the day—and has several clusters relevant to Adam: diffusion/posterior sampling, tabular-FM extension to time series, mechanistic-interpretability evaluation/tooling, latent-posterior elicitation, probabilistic message passing, and optimizer/model-systems work. The batch is noisy, but the concentration of papers that treat foundation models as statistical objects—posterior mixtures, circuit-extraction artifacts, tabular ICL engines—is notable. ([arxiv.org](https://arxiv.org/list/cs.LG/recent))

- **JMLR Volume 27 tail update.** Since the prior July 20 snapshot, JMLR now visibly extends to papers 136–137. Paper 136 is the already-covered Martin–Biroli–Bach high-dimensional gradient-flow analysis, now appearing in the JMLR stream; do not treat that as a new item. The new noteworthy item is **“Bridging Domain Invariance and Diversity,”** which proposes a tri-space latent representation decomposing features into domain-invariant, spurious invariant, and domain-variant components, then derives a finer target-risk bound explaining why invariance learning and domain augmentation need not be contradictory. ([jmlr.org](https://jmlr.org/papers/v27/))

- **cs.DB / VLDB-adjacent stream: agentic data provenance.** The only new July 22 cs.DB item is **AgentTrails: Towards Trust and Reuse for Agentic Tasks**, a short paper accepted at DASHSys 2026, co-located with VLDB 2026. This fits the database community’s emerging shift from “agents over data” demos toward provenance, trust, reuse, and audit trails for agentic workflows. Prior July 21 cs.DB items—EvoTune, WGLog, SAGA, etc.—were already covered and should remain suppressed. ([arxiv.org](https://arxiv.org/list/cs.DB/recent?show=100&skip=0))

## Section 3: Emerging Trends

- **Tabular FMs are becoming substrate models, not just table classifiers.** MASHT, TabFM-style releases, and prior work extending TabPFN-like machinery to time series all point to a pattern: structured-data FMs are increasingly used as generic in-context inference engines after a modality-specific representation transform.

- **Causal-agent evaluation is moving from text-only reasoning to executable structured workflows.** CausalDS is especially important because it forces agents to combine SCM reasoning, statistical estimation, coding, uncertainty, and abstention.

- **Mechanistic interpretability is entering a measurement-crisis phase.** Recent papers are less about finding one more circuit and more about validating whether extracted circuits are stable, comparable, and reportable.

- **Generative-model theory keeps importing statistical-inference language.** DDIM posterior sampling, signed flows, rare-event estimation, and diffusion sampling theory are all converging on posterior consistency, calibrated risk, exclusion constraints, and finite-sample evaluation.

- **Database venues are absorbing agent infrastructure questions.** The new cs.DB/VLDB-adjacent stream is less about LLMs as query translators and more about metadata access, provenance, auditability, semantic operators, agent memory, and data-system control planes.

## Section 4: Worth Watching

- **CausalDS dataset and benchmark artifact.** The HF release is small but complete enough to matter: a frozen 100-task exam, grading variants, observation-layer tasks, tabular/text modalities, and CC0 licensing. Suppress future reposts unless the benchmark materially expands or gets accepted into a major benchmark track. ([huggingface.co](https://huggingface.co/datasets/andleb/causalds))

- **CircuitKIT: Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability.** Not selected as a top paper, but worth tracking as infrastructure. It provides typed, serializable circuit representations, discovery algorithms, diagnostics, and downstream modules for pruning/editing/steering workflows. ([arxiv.org](https://arxiv.org/abs/2607.19317))

- **RAMP: Recognition parametrisation by Amortised Message Passing.** A ProbML 2026 paper proposing nonlinear amortized message passing for likelihood-based recovery of latent-variable distributions. It looks under-hyped but relevant to probabilistic representation learning. ([arxiv.org](https://arxiv.org/abs/2607.18883))

- **Signed Rectified Flow.** A principled attempt to add “negative information” to flow-based generation via signed measures, with applications to anti-memorization and suppression of undesired generated content. Worth tracking if code or broader evaluations appear. ([arxiv.org](https://arxiv.org/abs/2607.18516))

- **AgentTrails.** Short, early, but directionally important for reusable/auditable traces of agentic data tasks in VLDB-adjacent systems work. ([arxiv.org](https://arxiv.org/list/cs.DB/recent?show=100&skip=0))

## Section 5: Discord Highlights

**Jul 22 research brief**

Top papers:
1. **CausalDS: Benchmarking Causal Reasoning in Data-Science Agents** — executable causal data-science benchmark with SCM-grounded tabular tasks, tool use, uncertainty, and abstention.
2. **In-Context Time Series Classification with Random Convolutional Features** — uses random convolutional features plus tabular FMs for zero-shot time-series classification.
3. **Provable diffusion-based posterior sampling for linear inverse problems via DDIM** — coordinate-wise DDIM sampler with posterior-consistency guarantees.
4. **Circuit Claims Depend on What Is Extracted and How It Is Compared** — shows circuit-extraction conclusions are highly sensitive to reporting and comparison choices.
5. **Elicitation without Backpropagation** — Bayesian prompt elicitation by optimizing latent posterior samples, no transformer backprop required.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-07-22","type":"paper","title":"CausalDS: Benchmarking Causal Reasoning in Data-Science Agents","authors_or_org":"Andrej Leban, Yuekai Sun","url":"https://arxiv.org/abs/2607.08093","memory":"Top 5 paper. Covered July 9 2026 arXiv paper and HF artifact for SCM-generated causal data-science agent benchmark with tabular data, natural-language stories, Pearl-rung tasks, coding/tool use, uncertainty, and abstention. Suppress arXiv, HF, GitHub, benchmark-track, and social reposts unless the benchmark materially expands or results become central."}
{"date_delivered":"2026-07-22","type":"paper","title":"In-Context Time Series Classification with Random Convolutional Features","authors_or_org":"Joscha Cüppers, Jilles Vreeken","url":"https://arxiv.org/abs/2607.19234","memory":"Top 5 paper. Covered MASHT: MultiRocket/Hydra random convolutional features plus in-context tabular foundation models for zero-shot time-series classification. Suppress arXiv revisions, code, venue versions, and TabPFN/TFM social reposts unless materially expanded."}
{"date_delivered":"2026-07-22","type":"paper","title":"Provable diffusion-based posterior sampling for linear inverse problems via DDIM","authors_or_org":"Yuchen Jiao, Na Li, Changxiao Cai, Yuxin Chen, Gen Li","url":"https://arxiv.org/abs/2607.19333","memory":"Top 5 paper. Covered July 21 2026 arXiv paper proposing pDDIM coordinate-wise DDIM updates along singular directions for linear inverse problems with diffusion priors, with posterior consistency proof and image restoration experiments. Suppress future arXiv/code/venue reposts unless theory or empirical scope materially changes."}
{"date_delivered":"2026-07-22","type":"paper","title":"Circuit Claims Depend on What Is Extracted and How It Is Compared","authors_or_org":"Yang Sheng, Jie Fu","url":"https://arxiv.org/abs/2607.18921","memory":"Top 5 paper. Covered July 21 2026 arXiv mechanistic-interpretability paper showing circuit extraction claims are underdetermined by extraction object, pruning threshold, and comparison granularity, using synthetic Lean tactic prediction and dense/weight-sparse transformer checkpoints. Suppress future versions unless reporting recommendations or experiments materially change."}
{"date_delivered":"2026-07-22","type":"paper","title":"Elicitation without Backpropagation: Steering Model Behavior by Optimizing the Latent Posterior","authors_or_org":"Garrett Baker, Vinayak Pathak, Daniel Murfet, Susan Wei","url":"https://arxiv.org/abs/2607.18804","memory":"Top 5 paper. Covered Posterior Prefix Tuning for Bayes-filtered transformers: optimize distributions over hard prompts via prior samples and importance sampling, with no transformer forward passes/backprop during elicitation. Suppress future arXiv/venue/code reposts unless extended beyond stylized BFT settings."}
{"date_delivered":"2026-07-22","type":"proceedings","title":"arXiv cs.LG/stat.ML recent stream snapshot for July 22 2026","authors_or_org":"arXiv cs.LG/stat.ML","url":"https://arxiv.org/list/cs.LG/recent","memory":"Venue Watch. Covered July 22 2026 cs.LG stream with 177 entries and clusters in diffusion posterior sampling, tabular-FM/time-series transfer, mechanistic interpretability, latent-posterior elicitation, probabilistic message passing, and model/optimizer systems. Suppress this broad daily stream snapshot."}
{"date_delivered":"2026-07-22","type":"venue_issue","title":"JMLR Volume 27 latest papers stream as of July 22 2026, papers 136-137 tail","authors_or_org":"Journal of Machine Learning Research","url":"https://jmlr.org/papers/v27/","memory":"Venue Watch. Covered new visible JMLR Volume 27 tail after July 20 snapshot: paper 136 High-Dimensional Analysis of Gradient Flow for Extensive-Width Quadratic Neural Networks was already delivered earlier; paper 137 Bridging Domain Invariance and Diversity introduced tri-space latent representation and fine-grained domain-generalization risk bounds. Suppress this JMLR tail snapshot."}
{"date_delivered":"2026-07-22","type":"paper","title":"Bridging Domain Invariance and Diversity: A Fine-Grained Risk Bound for Domain Generalization","authors_or_org":"Xi Wang, Liang Bai, Xian Yang, Richard Yi Da Xu, Jiye Liang","url":"https://jmlr.org/papers/v27/25-0399.html","memory":"Individually discussed in JMLR Venue Watch. Covered tri-space latent representation decomposing domain-invariant, spurious invariant, and domain-variant components, with target-domain risk bound reconciling invariance learning and domain augmentation. Suppress future JMLR/arXiv/code mentions unless selected for deeper treatment or materially revised."}
{"date_delivered":"2026-07-22","type":"proceedings","title":"cs.DB recent database arXiv stream as of July 22 2026","authors_or_org":"arXiv cs.DB / VLDB-adjacent papers","url":"https://arxiv.org/list/cs.DB/recent","memory":"Venue Watch. Covered only new July 22 cs.DB item AgentTrails, while noting July 21 cs.DB items had already been delivered. Suppress this broad daily cs.DB snapshot."}
{"date_delivered":"2026-07-22","type":"resource","title":"AgentTrails: Towards Trust and Reuse for Agentic Tasks","authors_or_org":"Eden Wu, Sonia Castelo, Yurong Liu, Cláudio T. Silva, Juliana Freire","url":"https://arxiv.org/abs/2607.18816","memory":"Worth Watching and cs.DB Venue Watch. Covered short paper accepted at DASHSys 2026 co-located with VLDB 2026 on trust, provenance, and reuse for agentic tasks. Suppress future arXiv/workshop reposts unless a fuller system, artifact, or VLDB/DASHSys program update materially expands it."}
{"date_delivered":"2026-07-22","type":"software","title":"CircuitKIT: Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability","authors_or_org":"Pratinav Seth, Hem Gosalia, Aditya Kasliwal, Vinay Kumar Sankarapu","url":"https://arxiv.org/abs/2607.19317","memory":"Worth Watching. Covered source-available library for typed/serializable circuit representations, discovery algorithms, diagnostics, and downstream intervention modules for pruning/editing/steering/selective fine-tuning. Suppress future paper/repo/social mentions unless library capabilities or adoption materially change."}
{"date_delivered":"2026-07-22","type":"paper","title":"RAMP: Recognition parametrisation by Amortised Message Passing","authors_or_org":"Lior Fox, Kai Biegun, James Heald, Samo Hromadka, Arielle Rosinski, Maneesh Sahani","url":"https://arxiv.org/abs/2607.18883","memory":"Worth Watching. Covered ProbML 2026 paper proposing nonlinear amortized message passing / recognition-parametrised modeling for likelihood-based recovery of latent-variable distributions. Suppress future arXiv/ProbML/code mentions unless substantially expanded."}
{"date_delivered":"2026-07-22","type":"paper","title":"Signed Rectified Flow: Negativity-Controlled Generation","authors_or_org":"Runlong Liao, Baiyu Su, Lizhang Chen, Qiang Liu","url":"https://arxiv.org/abs/2607.18516","memory":"Worth Watching. Covered signed-measure generalization of rectified flow for promoting positive distributions and suppressing negative ones, with exclusion constraints, anti-memorization, and unsafe-content suppression examples. Suppress future versions unless code, theory, or evaluations materially change."}
{"date_delivered":"2026-07-22","type":"dataset","title":"CausalDS Hugging Face benchmark dataset","authors_or_org":"Andrej Leban, Yuekai Sun / Hugging Face dataset andleb/causalds","url":"https://huggingface.co/datasets/andleb/causalds","memory":"Worth Watching artifact paired with Top 5 paper. Covered frozen 100-task exam, grading variants, observation-layer variants, tabular/text modalities, parquet data, and CC0 license. Suppress repeat dataset-card/repo mentions unless resource materially expands."}
```