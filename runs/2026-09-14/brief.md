## Section 1: Top 5 Papers

1. **FINESSE: An Agent-Based Simulator and Benchmark Dataset for Multimodal Financial Event Sequences**  
   **Authors:** Tyler Farnan, Benjamin Eng, Adam Abate, Xirui Hou, Rizal Fathony, Nam H. Nguyen, Senthil Kumar  
   **Venue/source:** arXiv  
   **Release date:** September 9, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2609.11993))  
   FINESSE is one of the more useful structured-data artifacts this week: an agent-based simulator for financial event streams coupled through latent evolving agent states. It generates multiple interdependent schemas—transactions, payments, account-status changes, interventions—and releases FINESSE-Bench for balance forecasting, fraud detection, missed-payment prediction, and next-event prediction. This is not just another tabular dataset; it is a controllable simulation environment for temporally structured, multi-table, policy-influenced data. That makes it relevant to synthetic data, causal simulation, temporal graphs, event-sequence modeling, and foundation models for financial/enterprise structured data.  
   **Why you should care:** It could become a rare public testbed for structured-data models that need temporal, relational, and policy-intervention realism.

2. **Attention Quantization for Tabular Foundation Models**  
   **Authors:** Jonas M. Kübler, Benjamin Jäger, Klemens Flöge, Noah Hollmann, Frank Hutter  
   **Venue/source:** arXiv new listing  
   **Release/listing date:** September 14, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   This paper targets a practical bottleneck that will matter if TabPFN-style models become routine infrastructure: inference speed. The key observation is that tabular foundation models have transformer-like attention, but not LLM-like serving patterns, so standard weight/KV-cache quantization is not necessarily the right target. The authors quantize queries, keys, and values to FP8 and use explicit FP8 matrix multiplication, while carefully aligning quantization error between test rows and training/context rows. They report up to 1.7× attention-kernel speedup on TabPFN-v3 and TabICLv2 with no relevant accuracy loss across TabArena and BeyondArena.  
   **Why you should care:** This is a concrete step toward treating tabular foundation models as deployable systems rather than leaderboard curiosities.

3. **Amortized Low-Rank Adaptation for Model-Based Reinforcement Learning**  
   **Authors:** Fernando Palafox, David Fridovich-Keil  
   **Venue/source:** arXiv  
   **Release date:** September 10, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/abs/2609.12278))  
   CLAW studies fast test-time adaptation of world models when the environment comes from a known family but differs at deployment. Instead of choosing between cheap but limited in-context learning and expressive but expensive gradient adaptation, it trains a hypernetwork to emit LoRA adapters from a small batch of test-time transitions. The base model is frozen at deployment; a single forward pass generates the adaptation. In locomotion and manipulation families, the method reportedly adapts within seconds of data, outperforms gradient-based adaptation and ICL, and avoids overfitting in data-scarce regimes.  
   **Why you should care:** It is a clean “model emits adaptation” pattern that may transfer to tabular, relational, and simulator-conditioned foundation models.

4. **Rank-Efficient LoRA via Joint Tangent-Space Optimization under Isotropic Curvature**  
   **Authors:** Zihan Zhu, Zhehang Du, Xuyang Chen, Tim Tsz-Kit Lau, Jiayuan Wu, X. Y. Han, Qi Long, Weijie Su  
   **Venue/source:** arXiv new listing  
   **Release/listing date:** September 14, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   This paper argues that LoRA’s nominal rank is a poor proxy for the effective rank of the induced update: AdamW can concentrate per-step updates into low-rank singular spectra even when the adapter rank is larger. ISO-LoRA instead couples the two LoRA factors through spectral descent on the induced tangent perturbation in weight space, encouraging more even use of available singular directions. The authors give a one-step analysis under a spiked-gradient model and evaluate adaptation from 0.1B to 7B parameters, with strongest gains at moderate-to-large LoRA ranks.  
   **Why you should care:** It connects optimizer geometry, parameter-efficient adaptation, and rank-utilization diagnostics—useful for both practical fine-tuning and representation-theoretic analysis.

5. **Membership Inference via Pairwise Likelihood Ratios**  
   **Authors:** Shengjie Niu, Zebin Yun, Yeheng Ge, Jian Huang  
   **Venue/source:** arXiv  
   **Release/listing date:** September 14, 2026  
   **Link:** ([arxiv.org](https://arxiv.org/list/stat.ML/new))  
   PL-MIA reframes membership inference as calibrated statistical evidence aggregation rather than thresholding one confidence-like score. The method forms pairwise likelihood-ratio comparisons between a query and non-training reference points, derives p-values, and combines them with the Cauchy combination test. The motivation is strong: modern privacy audits often discard continuous evidence by reducing pairwise signals to votes or scores, losing power in low-false-positive regimes. The paper reports over 25% TPR improvement in the critical low-FPR region and gives conditions under which GLR, population calibration, and Cauchy aggregation improve attack power.  
   **Why you should care:** It is a statistically principled privacy-audit method that should be considered alongside the recent wave of memorization, extraction, and tabular-FM privacy work.

## Section 2: Venue Watch

- **arXiv cs.LG/stat.ML/cs.DB, September 14 stream.** The Monday batch was unusually broad: cs.LG listed 260 total entries with 99 new submissions, stat.ML listed 34 total with 4 new submissions, and cs.DB listed 7 total with 3 new submissions. The most relevant clusters were structured-data simulation, tabular-FM systems, LoRA/optimizer geometry, privacy auditing, world-model adaptation, conformal/UQ methods, and database learning systems. Notable adjacent items include physics-informed conformal prediction for neural operators, FINESSE, diffusion-conditioned representation alignment for time series, QEmbed for cardinality estimation, and kernel-I/O bottleneck analysis for cloud OLTP systems. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **TMLR September 2026 additions.** The visible September stream added a mix of retrieval/context sizing, foundation-model optimization, agentic reasoning, diffusion, interpretability, and world-model memory. Especially relevant: **Ricci-Filtration** for adaptive RAG context sizing, **Low-rank orthogonalization for large-scale matrix optimization**, **LLM Probability Concentration**, **On Memory: A Comparison of Memory Mechanisms in World Models**, **Tags for DAGs**, **Attention by Synchronization**, **Choosing the right basis for interpretability**, **WaveletDiff**, **multi-layer SSM expressivity**, **Subspace Inference for Active Reward Learning**, and **Compressibility Measures Complexity**. This is a good month for representation/objective-function work, but also a signal that TMLR is continuing to absorb survey, systems, and agent-evaluation work even after recent survey-policy changes. ([jmlr.org](https://jmlr.org/tmlr/papers/))

- **JMLR Volume 27 tail remains unchanged since the last snapshot.** The latest visible tail still runs through article 205, including **Robustness Against Weak or Invalid Instruments**, **A Theoretical Framework for Masked Pretraining**, **Unveiling the Statistical Foundations of Chain-of-Thought Prompting Methods**, **OptunaHub**, **MarkDiffusion**, and **A Library for Learning Neural Operators**. No new post-205 JMLR items were visible in the current crawl, so this is mainly a “no new bounded release” note rather than a repeat issue summary. ([jmlr.org](https://www.jmlr.org/papers/v27/))

## Section 3: Emerging Trends

- **Structured-data foundation models are moving from modeling to serving.** Attention quantization, prototype/context compression, relational context construction, and deployment-aware evaluations are converging on the same question: can tabular/relational FMs be made cheap, stable, and auditable enough for production?

- **Simulation is becoming a first-class benchmark substrate.** FINESSE, recent causal simulators, verified code-world models, and structured financial/clinical event generators all point toward benchmark design where interventions, latent states, and distribution shifts are controllable rather than merely observed.

- **Rank and geometry are now practical diagnostics, not just theory.** ISO-LoRA, Muon/Musec-style optimizer work, shared SAE dictionaries, Fisher/output geometry, and superposition theory are all probing whether learned representations and updates use their nominal capacity.

- **Privacy auditing is getting more statistical.** PL-MIA fits a broader shift from ad hoc extraction/memorization scores toward calibrated tests, likelihood ratios, conformal-style guarantees, and low-FPR operating points.

- **World-model adaptation is drifting toward amortized parameter generation.** CLAW’s “context → LoRA adapter” approach is a close cousin of emitted-specialist models and may become a general pattern for adapting models to small task-specific structured datasets.

## Section 4: Worth Watching

- **QEmbed: A Deep Learning Based Cardinality Estimator for Efficient Query Processing.** A MADE-based learned cardinality estimator using hybrid one-hot/embedding encodings for mixed-cardinality attributes, with emphasis on reducing catastrophic maximum Q-errors. Worth tracking for learned query optimization, especially if artifacts appear. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

- **GUIDE: Generative Utility Inference and Decision Engine.** Combines LLM-driven conversational preference elicitation, Bayesian adaptive sampling, and symbolic representation learning; the investment-portfolio setup is narrow, but the architecture is relevant to preference learning and decision-aware user modeling. ([arxiv.org](https://arxiv.org/abs/2609.12137))

- **Granularity-Adaptive Credit Assignment for Long-Horizon LLM Agent RL.** GACA uses uncertainty/negative-log-likelihood to decide when to use fine-grained versus episode-level advantage signals, reporting gains on ALFWorld and WebShop. This is worth suppressing now because agent-RL credit assignment is becoming crowded and repetitive. ([arxiv.org](https://arxiv.org/abs/2609.12424))

- **Learning Interaction Kernels from Collective Steady States.** A stat.ML system-identification paper learning interaction laws from single-snapshot collective steady states rather than trajectories. Relevant to inverse problems, simulation, and mechanistic representation learning. ([arxiv.org](https://arxiv.org/list/stat.ML/new))

## Section 5: Discord Highlights

**Sep 14 research brief**

Top papers:
1. **FINESSE** — agent-based simulator and benchmark for multimodal financial event sequences.
2. **Attention Quantization for Tabular Foundation Models** — FP8 Q/K/V attention acceleration for TabPFN-style models.
3. **Amortized Low-Rank Adaptation for Model-Based RL** — hypernetwork-generated LoRA adapters for fast world-model adaptation.
4. **Rank-Efficient LoRA** — optimizer-aware LoRA rank utilization via tangent-space spectral descent.
5. **Membership Inference via Pairwise Likelihood Ratios** — calibrated likelihood-ratio aggregation for stronger privacy audits.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-09-14","type":"paper","title":"FINESSE: An Agent-Based Simulator and Benchmark Dataset for Multimodal Financial Event Sequences","authors_or_org":"Tyler Farnan, Benjamin Eng, Adam Abate, Xirui Hou, Rizal Fathony, Nam H. Nguyen, Senthil Kumar","url":"https://arxiv.org/abs/2609.11993","memory":"Top 5 paper. Covered FINESSE agent-based simulator and FINESSE-Bench for multimodal structured financial event sequences with transactions, payments, account status, policy interventions, latent evolving states, and four benchmark tasks. Suppress future arXiv, dataset, simulator, code, benchmark, and repost mentions unless the framework or benchmark materially expands."}
{"date_delivered":"2026-09-14","type":"paper","title":"Attention Quantization for Tabular Foundation Models","authors_or_org":"Jonas M. Kübler, Benjamin Jäger, Klemens Flöge, Noah Hollmann, Frank Hutter","url":"https://arxiv.org/abs/2609.13031","memory":"Top 5 paper. Covered FP8 query/key/value attention quantization for tabular foundation models including TabPFN-v3 and TabICLv2, explicit FP8 matmul kernels, train/test row quantization-error alignment, TabArena/BeyondArena evaluation, and up to 1.7x attention speedup. Suppress arXiv/code/social/venue repeats unless implementation, model scope, or deployment evidence materially changes."}
{"date_delivered":"2026-09-14","type":"paper","title":"Amortized Low-Rank Adaptation for Model-Based Reinforcement Learning","authors_or_org":"Fernando Palafox, David Fridovich-Keil","url":"https://arxiv.org/abs/2609.12278","memory":"Top 5 paper. Covered CLAW, context-conditioned low-rank adaptation of world models via a hypernetwork that emits LoRA adapters from a small batch of test-time transitions; compared with ICL and gradient adaptation in locomotion/manipulation families. Suppress future arXiv/code/venue/project mentions unless method or empirical scope materially expands."}
{"date_delivered":"2026-09-14","type":"paper","title":"Rank-Efficient LoRA via Joint Tangent-Space Optimization under Isotropic Curvature","authors_or_org":"Zihan Zhu, Zhehang Du, Xuyang Chen, Tim Tsz-Kit Lau, Jiayuan Wu, X. Y. Han, Qi Long, Weijie Su","url":"https://arxiv.org/abs/2609.12137","memory":"Top 5 paper. Covered ISO-LoRA and the claim that optimizer geometry controls effective rank utilization of nominal-rank LoRA adapters; AdamW concentrates singular spectra while Muon/ISO-LoRA use rank more evenly, with 0.1B-7B adaptation experiments. Suppress arXiv/code/social/venue repeats unless theory or evidence materially changes."}
{"date_delivered":"2026-09-14","type":"paper","title":"Membership Inference via Pairwise Likelihood Ratios","authors_or_org":"Shengjie Niu, Zebin Yun, Yeheng Ge, Jian Huang","url":"https://arxiv.org/abs/2609.12367","memory":"Top 5 paper. Covered Pairwise Likelihood MIA / PL-MIA using Gaussian likelihood-ratio statistics, population calibration, pairwise p-values against reference points, and Cauchy combination for stronger low-FPR membership inference auditing. Suppress future arXiv/code/venue/social mentions unless attack model, calibration theory, or empirical scope materially changes."}
{"date_delivered":"2026-09-14","type":"proceedings","title":"arXiv cs.LG/stat.ML/cs.DB new-submission stream for September 14 2026","authors_or_org":"arXiv cs.LG, stat.ML, cs.DB","url":"https://arxiv.org/list/cs.LG/new","memory":"Venue Watch. Covered Sep 14 2026 streams: cs.LG 99 new submissions out of 260 total entries, stat.ML 4 new out of 34, cs.DB 3 new out of 7; themes in structured-data simulation, tabular-FM systems, LoRA and optimizer geometry, privacy audits, world-model adaptation, conformal/UQ, and database learning systems. Suppress repeat daily stream summary."}
{"date_delivered":"2026-09-14","type":"proceedings","title":"TMLR September 2026 accepted papers incremental update as of September 14","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered visible Sep 14 TMLR September additions/top-of-page activity including Ricci-Filtration, low-rank orthogonalization for foundation-model training, ENIGMA, LLM-driven algorithm design for quantum circuits, WISE, MV-RAG, ProteinZero, LLM Probability Concentration, On Memory in World Models, Tags for DAGs, synchronization attention, interpretability basis comparison, WaveletDiff, SSM expressivity, active reward learning, and compressibility/MDL/singular-learning-theory. Suppress repeat Sep 14 incremental snapshot."}
{"date_delivered":"2026-09-14","type":"venue_issue","title":"JMLR Volume 27 latest papers stream status as of September 14 2026","authors_or_org":"Journal of Machine Learning Research","url":"https://www.jmlr.org/papers/v27/","memory":"Venue Watch no-new-tail status. Checked JMLR Volume 27 and noted latest visible tail remains through article 205, already covered previously; no new post-205 JMLR items visible in current crawl. Suppress repeating this no-change status unless new JMLR papers appear."}
{"date_delivered":"2026-09-14","type":"paper","title":"QEmbed: A Deep Learning Based Cardinality Estimator for Efficient Query Processing","authors_or_org":"Pooja Rajput, Suman Banerjee","url":"https://arxiv.org/abs/2609.12535","memory":"Worth Watching. Covered QEmbed learned cardinality estimator using MADE-style autoregressive joint distribution modeling, hybrid one-hot and embedding encodings for mixed-cardinality attributes, and emphasis on reducing maximum Q-error tail failures. Suppress future arXiv/code/venue mentions unless system or benchmark evidence materially expands."}
{"date_delivered":"2026-09-14","type":"paper","title":"GUIDE: Generative Utility Inference and Decision Engine","authors_or_org":"Anagha Tiwari, Alexander G. Gray, Nick Feamster, Brian Jabarian, Alex Imas, Alex Kale","url":"https://arxiv.org/abs/2609.12137","memory":"Worth Watching. Covered LLM-driven conversational preference elicitation using Bayesian adaptive sampling and symbolic representation learning for domain-specific priors, with investment-portfolio in silico experiments. Suppress arXiv/code/project/venue repeats unless preference-learning framework or empirical scope materially expands."}
{"date_delivered":"2026-09-14","type":"paper","title":"Granularity-Adaptive Credit Assignment for Long-Horizon LLM Agent Reinforcement Learning","authors_or_org":"Taoran Liang, Yang Liu, Shang Luo, Yingguang Yang, Rongrong Zhang, Yingzong Min, Yulin Huang, Jianshen Zhang, Yongzhi Qi, Kefu Xu, Congjing Ran, Bin Chong","url":"https://arxiv.org/abs/2609.12424","memory":"Worth Watching. Covered GACA for critic-free long-horizon LLM agent RL, using per-step NLL/uncertainty to mix fine-grained and episode-level advantage signals; evaluated on ALFWorld and WebShop. Suppress future arXiv/code/social/venue repeats unless method or results materially expand."}
{"date_delivered":"2026-09-14","type":"paper","title":"Learning Interaction Kernels from Collective Steady States","authors_or_org":"Baoli Hao, Mauro Maggioni, Ming Zhong","url":"https://arxiv.org/abs/2609.12004","memory":"Worth Watching. Covered stat.ML system-identification paper learning interaction kernels in interacting-particle systems from single-snapshot collective steady-state or quasi-stationary observations rather than trajectories. Suppress future arXiv/code/venue reposts unless theory, solver, or empirical scope materially changes."}
```