## Section 1: Top 5 Papers

1. **AutoGrable: What Is a Good Graph for a Table?**  
   **Authors:** Tamara Cucumides, Floris Geerts  
   **Venue/source:** arXiv cs.LG  
   **Release date:** August 13, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   **Summary:** AutoGrable attacks a deceptively important question for relational/table learning: when is it worth converting a table or foreign-key schema into a graph, and which graph should be built? The paper gives a model-free criterion based on the partition that a 1-WL-bounded message-passing GNN would induce over rows. Candidate graph constructions are scored by whether they separate rows with different labels without over-fragmenting same-label rows, using a label-alignment risk plus occupancy penalty. The method avoids materializing graphs or training GNNs during search, and can decline graphification when no useful construction exists.  
   **Why you should care:** This is a clean bridge between tabular ML, relational representation learning, and graph foundation-model preprocessing.

2. **Three Tokens Force Exponential Feature Rank in Nonnegative Kernel Attention**  
   **Author:** Vicente Opazo  
   **Venue/source:** arXiv cs.LG  
   **Release date:** August 13, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   **Summary:** This theory paper isolates a sharp limitation of nonnegative kernel-attention sketches. Full attention can expose every token pair, while kernel attention compresses a sequence into a fixed-dimensional summary; the paper shows that even at three tokens this distinction can become exponential. For a Boolean Min-IP task, a single normalized nonnegative kernel-attention head needs \(2^{\Omega(m)}\) features to beat error \(1/2\), while dense softmax solves the same task with \(m\)-dimensional scores. The result also survives position-dependent maps and causal final queries, suggesting a hard separation between exact pairwise access and sketch-based approximations.  
   **Why you should care:** It gives a compact lower-bound story for why some “efficient attention” substitutes may fail on compositional retrieval.

3. **Fine-Tuning Generative Models for Extreme Events via CVaR-Penalized Wasserstein Gradient Flows**  
   **Authors:** Thejani Gamage, Hyemin Gu, Zhizhen Zhang, Ziyu Chen, Markos Katsoulakis, Luc Rey-Bellet  
   **Venue/source:** arXiv stat.ML  
   **Release date:** August 13, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/stat.ML/new))  
   **Summary:** The paper proposes CVaR-GPA, a black-box particle fine-tuning method for moving pretrained generative samples toward heavy-tailed or extreme-event target distributions. The key construction is a Wasserstein gradient flow for Lipschitz-regularized KL penalized by a CVaR discrepancy term; the CVaR component restores velocity in under-sampled tails where standard flows can stall. The algorithm operates on generated samples rather than model internals, uses first-variation subgradients from the Rockafellar–Uryasev representation, and sets its horizon by a kinetic-energy stopping rule. Experiments cover Student-\(t\), Neal’s funnel, and Fama-French portfolio data.  
   **Why you should care:** This is a promising diagnostic/fine-tuning primitive for simulation and synthetic-data regimes where tail fidelity matters more than average fit.

4. **Guided Table Retrieval for Structured Data Search**  
   **Authors:** Alekh Jindal, Jyoti Pandey, Christina Pavlopoulou, Ronith PR, Sharath Prakash, Shi Qiao, Shivani Tripathi, Wangda Zhang  
   **Venue/source:** arXiv cs.DB  
   **Release date:** August 13, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.DB/new))  
   **Summary:** This paper proposes a four-stage pipeline for retrieving relevant tables and join paths from structured databases given natural-language questions. Instead of treating schema linking as a pure LLM problem, it decomposes the task into deterministic grounding, join-graph reachability, LLM disambiguation of sources and targets, and algorithmic merging into minimal topologically ordered join trees. On BIRD-DEV and an enterprise BEAVER benchmark, it reports substantially better precision and F1 than baselines, while returning exact join trees consumable by query compilers.  
   **Why you should care:** The design pattern—symbolic reachability plus selective semantic disambiguation—is likely to matter for data-lake agents and text-to-SQL systems.

5. **Disentangling the Expressivity of RoPE**  
   **Authors:** Selim Jerad, Anej Svete, Jiaoda Li, Ryan Cotterell  
   **Venue/source:** arXiv cs.LG  
   **Release date:** August 13, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   **Summary:** This paper separates two explanations for rotary position embeddings: periodic expressivity and positional/local-offset anchoring. For fully uniform finite-precision soft-attention transformers, it shows that if every rotary component is periodic, RoPE transformers recognize exactly languages definable in past temporal logic with modular predicates. Conventional RoPE differs because its rotations do not repeat; it yields a precision-dependent bounded simulation of fixed-offset look-back operators instead of a clean modular-language characterization. Controlled experiments support the distinction, including cases where conventional RoPE harms position-invariant distant access.  
   **Why you should care:** It refines the current theory of positional encodings and long-context generalization beyond informal “RoPE is periodic” explanations.

## Section 2: Venue Watch

**arXiv cs.LG / stat.ML / cs.DB, August 13 daily stream.** The August 13 cs.LG page lists 96 new submissions out of 261 total entries, stat.ML lists one new submission out of 27 total entries, and cs.DB lists six new submissions out of 12 entries. The strongest clusters for Adam’s interests are: table-to-graph construction, table retrieval and join-path search, attention/RoPE expressivity theory, tail-aware generative fine-tuning, structured financial-statement forecasting, scalable Gaussian-process inference, and DBMS/autonomous resource tuning. The stream is unusually useful for structured-data ML: AutoGrable and Guided Table Retrieval both treat representation construction as a first-class object rather than as an opaque embedding step. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

**TMLR August 2026 accepted-paper stream, incremental update visible August 13.** New top-of-page additions include **A Survey on Behavioral Data Representation Learning**, **Beyond Imitation: A Framework and Benchmark for LLM-Assisted Peer Review**, **Variational Set Operator Networks**, **Few Contrastive Attention Heads Enable Visual Grounding in Large Vision-Language Models** with J2C certification, **Toward Unified Robot Learning** with Survey certification, **Patch-based Memory Gate Model in Time Series Foundation Model**, and **Online Learning and Unlearning**. The batch continues TMLR’s August pattern: broad representation-learning surveys, agent/evaluation benchmarks, uncertainty-aware set/meta-learning, time-series foundation-model variants, and algorithmic unlearning theory. ([jmlr.org](https://jmlr.org/tmlr/papers/))

**KDD 2026 status.** KDD is in its final conference day window in Jeju, with the official site showing the August 9–13 conference and a schedule that included the opening awards session, Data Day, dissertation awards, and Test-of-Time awards earlier in the week. I did not find a stable official winners page in the current crawl, so this briefing avoids recording specific award winners. Watch for the official post-conference awards/proceedings update rather than relying on social or scraped summaries. ([kdd2026.kdd.org](https://kdd2026.kdd.org/?utm_source=openai))

## Section 3: Emerging Trends

- **Representation construction is becoming the object of study.** AutoGrable, Guided Table Retrieval, OADD from yesterday, metadata reconstruction, and table-semantic schema systems all point to a shift from “learn embeddings over whatever representation is handed to us” toward explicitly optimizing the interface between raw structured data and learning systems.

- **Efficient attention theory is getting sharper and more adversarial.** Recent RoPE and kernel-attention papers are no longer just explaining empirical long-context behavior; they are isolating precise expressivity classes and lower bounds that separate dense attention from compressed sketches.

- **Synthetic/generative modeling work is moving toward tail, constraint, and query fidelity.** CVaR-GPA, c-rectified flow, Logit Flow/Diffusion for mixed tabular data, and query-centric synthetic-tabular benchmarks all emphasize that average likelihood or marginal similarity is not enough.

- **Data-management papers are absorbing agentic and semantic-query pressure.** Guided table retrieval, AI query compilation, semantic operator compilation, Baikal, Scout, and metadata reconstruction all treat LLMs as components inside query planners, compilers, provenance systems, or retrieval pipelines—not as monolithic database replacements.

- **TMLR’s August stream is broadening representation learning beyond classic vision/NLP.** Behavioral data, set operators, robot foundation models, time-series memory gates, and unlearning suggest a venue-level appetite for reusable representation principles across interaction logs, sets, trajectories, and systems.

## Section 4: Worth Watching

- **Long-Horizon Forecasting of Complete Financial Statements with Forma / ProForma-20Q.** A structured benchmark and transformer for forecasting 78 financial-statement line items 1–20 quarters ahead, with masked-tuple Gaussian likelihood and accounting-coherence postprocessing. Worth suppressing because it is a rare high-dimensional, economically structured forecasting benchmark with model weights promised. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **A Factor Graph Approach to Scalable Multi-Output Gaussian Process Regression.** Recasts multi-output GP regression as exact Gaussian message passing over a nearest-neighbor chain with linear complexity in candidate-set size after construction. This could matter for probabilistic structured time-series and missing-output settings. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **Weightless Fine-Tuning: Personalizing LLMs via Logit-Space Transport.** A training-free decoding-time approximation to SFT using supervised residuals transported across prefixes via dropout-induced cross-covariance. It is adjacent to black-box adaptation, posterior-prefix tuning, and low-cost personalization. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **MicroTune: Reinforcement Learning based DBMS Buffer Pool Auto-Tuning.** Online RL for DBMS buffer-size adjustment under SLA constraints; incremental relative to prior DBMS-tuning work, but useful to track alongside EvoTune and ScaleSense as the database community’s agentic/autonomic tuning thread. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

## Section 5: Discord Highlights

**Aug 13 research brief**

Top 5 papers:
1. **AutoGrable: What Is a Good Graph for a Table?** — model-free criterion for when and how to graphify tables/relational schemas.
2. **Three Tokens Force Exponential Feature Rank in Nonnegative Kernel Attention** — sharp lower bound separating dense attention from kernel sketches.
3. **Fine-Tuning Generative Models for Extreme Events via CVaR-Penalized Wasserstein Gradient Flows** — black-box generative fine-tuning for heavy tails and rare events.
4. **Guided Table Retrieval for Structured Data Search** — deterministic + LLM-guided retrieval of relevant tables and exact join trees.
5. **Disentangling the Expressivity of RoPE** — finite-precision theory separating periodic RoPE from conventional nonrepeating rotations.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-08-13","type":"paper","title":"AutoGrable: What Is a Good Graph for a Table?","authors_or_org":"Tamara Cucumides, Floris Geerts","url":"https://arxiv.org/abs/2608.11431","memory":"Top 5 paper. Covered Aug 13 2026 arXiv paper on model-free table-to-graph construction for single tables and foreign-key schemas using 1-WL partition quality, label-alignment risk, occupancy penalty, and graph-free greedy search. Suppress future arXiv/code/venue reposts unless method or evidence materially changes."}
{"date_delivered":"2026-08-13","type":"paper","title":"Three Tokens Force Exponential Feature Rank in Nonnegative Kernel Attention","authors_or_org":"Vicente Opazo","url":"https://arxiv.org/abs/2608.11427","memory":"Top 5 paper. Covered Aug 13 2026 arXiv theory paper proving exponential feature-rank lower bounds for normalized nonnegative kernel attention on a three-token Min-IP task, contrasted with dense softmax attention. Suppress future arXiv/venue/social reposts unless theory materially expands."}
{"date_delivered":"2026-08-13","type":"paper","title":"Fine-Tuning Generative Models for Extreme Events via CVaR-Penalized Wasserstein Gradient Flows","authors_or_org":"Thejani Gamage, Hyemin Gu, Zhizhen Zhang, Ziyu Chen, Markos Katsoulakis, Luc Rey-Bellet","url":"https://arxiv.org/abs/2608.11544","memory":"Top 5 paper. Covered CVaR-GPA, Aug 13 2026 stat.ML/cs.LG paper on black-box sample-level fine-tuning of generative models for heavy tails and extreme events using CVaR-penalized Wasserstein gradient flows and adaptive kinetic-energy stopping. Suppress future versions unless theory, implementation, or empirical scope materially changes."}
{"date_delivered":"2026-08-13","type":"paper","title":"Guided Table Retrieval for Structured Data Search","authors_or_org":"Alekh Jindal, Jyoti Pandey, Christina Pavlopoulou, Ronith PR, Sharath Prakash, Shi Qiao, Shivani Tripathi, Wangda Zhang","url":"https://arxiv.org/abs/2608.11644","memory":"Top 5 paper and cs.DB item. Covered four-phase structured-data table retrieval pipeline with deterministic grounding, join-graph reachability, LLM disambiguation, and minimal topologically ordered join-tree construction; evaluated on BIRD-DEV and BEAVER. Suppress future arXiv/venue/tool reposts unless artifact or method materially expands."}
{"date_delivered":"2026-08-13","type":"paper","title":"Disentangling the Expressivity of RoPE","authors_or_org":"Selim Jerad, Anej Svete, Jiaoda Li, Ryan Cotterell","url":"https://arxiv.org/abs/2608.11909","memory":"Top 5 paper. Covered Aug 13 2026 arXiv theory paper separating periodic RoPE expressivity from conventional nonrepeating RoPE finite-precision fixed-offset behavior, with formal-language characterization and controlled experiments. Suppress future arXiv/venue/repost versions unless theory or experiments materially change."}
{"date_delivered":"2026-08-13","type":"proceedings","title":"arXiv cs.LG/stat.ML/cs.DB new-submission stream for August 13 2026","authors_or_org":"arXiv cs.LG, stat.ML, cs.DB","url":"https://arxiv.org/list/cs.LG/new","memory":"Venue Watch. Covered Aug 13 2026 arXiv stream: 96 new cs.LG submissions out of 261 entries, one new stat.ML submission out of 27 entries, and six new cs.DB submissions out of 12 entries; themes in table graphification, table retrieval, attention/RoPE theory, tail-aware generative fine-tuning, financial-statement forecasting, scalable GP inference, and DBMS tuning. Suppress repeat broad daily stream summary."}
{"date_delivered":"2026-08-13","type":"proceedings","title":"TMLR August 2026 accepted papers incremental update as of August 13","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered visible Aug 13 top-of-page additions to TMLR August 2026 accepted stream, including Behavioral Data Representation Learning survey, LLM-assisted peer review benchmark, Variational Set Operator Networks, Few Contrastive Attention Heads with J2C, robot learning survey, time-series FM patch memory gate, and Online Learning and Unlearning. Suppress this incremental snapshot."}
{"date_delivered":"2026-08-13","type":"announcement","title":"KDD 2026 final-day schedule and pending official awards/results watch","authors_or_org":"ACM SIGKDD / KDD 2026","url":"https://kdd2026.kdd.org/schedule-at-a-glance/","memory":"Venue Watch. Noted KDD 2026 Jeju Aug 9-13 final-day status and schedule items including opening awards, dissertation awards, Data Day, and Test-of-Time awards, but did not record specific winners because no stable official winners page was found in the current crawl. Suppress repeat schedule status; cover official awards/proceedings/results only when stable page appears."}
{"date_delivered":"2026-08-13","type":"benchmark","title":"ProForma-20Q / Forma financial statement forecasting benchmark and model","authors_or_org":"Travis L. Johnson, Jiannan Jiang, Soumyabrata Chaudhuri, Yihao Chen, Lauren Falvey, Donal O'Cofaigh","url":"https://arxiv.org/abs/2608.11327","memory":"Worth Watching. Covered benchmark/model for long-horizon forecasting of 78 complete financial-statement line items 1-20 quarters ahead using Forma transformer over account-quarter-value tuples, masked-tuple Gaussian likelihood, accounting-coherence postprocessing, and scenario analysis. Suppress future arXiv/repo/model-card mentions unless benchmark or weights materially change."}
{"date_delivered":"2026-08-13","type":"paper","title":"A Factor Graph Approach to Scalable Multi-Output Gaussian Process Regression","authors_or_org":"Wouter W. L. Nuijten, Esther G. van Pelt, Albert Podusenko, İsmail Şenöz, Wouter M. Kouw","url":"https://arxiv.org/abs/2608.11917","memory":"Worth Watching. Covered Aug 13 2026 arXiv paper recasting multi-output GP regression as exact Gaussian message passing on a nearest-neighbor chain with LMC mixing and missing-output support, for scalable probabilistic time-series/structured outputs. Suppress future versions unless method or artifact materially expands."}
{"date_delivered":"2026-08-13","type":"paper","title":"Weightless Fine-Tuning: Personalizing LLMs via Logit-Space Transport","authors_or_org":"Bohan Zhang, Anqi Ni, Yixin Wang, Paramveer S. Dhillon","url":"https://arxiv.org/abs/2608.11342","memory":"Worth Watching. Covered training-free personalization method approximating SFT by transporting supervised logit residuals across prefixes using dropout-induced cross-covariance; related to black-box adaptation and posterior/logit-space elicitation. Suppress future arXiv/code/venue mentions unless substantially expanded."}
{"date_delivered":"2026-08-13","type":"software","title":"MicroTune: Reinforcement Learning based DBMS Buffer Pool Auto-Tuning for Optimal Memory Utilization","authors_or_org":"Yifan Wang, Patrick Royer, Raphaël Féraud, David Delande","url":"https://arxiv.org/abs/2608.11239","memory":"Worth Watching and cs.DB stream item. Covered online RL-based buffer adjustment system for DBMS memory/SLA tradeoffs, evaluated across workloads with external and internal DBMS metrics. Suppress future arXiv/tool/venue reposts unless system, code, or production evidence materially changes."}
```