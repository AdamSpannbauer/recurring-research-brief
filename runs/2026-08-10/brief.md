## Section 1: Top 5 Papers

1. **Adversarial Causal Intervention Falsification**  
   **Authors:** Mojtaba Eslami  
   **Venue/source:** arXiv cs.LG / cs.GT / econ.EM / stat.ME  
   **Release date:** submitted August 5, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2608.06427))  
   This is the cleanest causal-methodology paper in the current batch. The paper treats causal generative modeling as a sequential game: a structural generator proposes observational/interventional distributions, while an adversarial experimentalist chooses interventions designed to falsify it. The discriminator is indexed by interventions rather than by “real vs. synthetic” samples, giving a formal separation between observational fit, interventional equivalence, and point identification. The main theory reduces the objective to a worst-intervention IPM, proves identification up to interventional equivalence, gives finite-sample guarantees, and supplies an elimination-style active design result.  
   **Why you should care:** It is a useful conceptual bridge between synthetic causal data generation, active experimental design, and falsification-oriented evaluation.

2. **Bootstrap-Conditioned Action Selection with Tabular Foundation Models**  
   **Authors:** Devansh Gupta, Shiv Tavker, Dmitry Efimov, Suchitra Sathyanarayana, Gitanjali Bhutani, Boris N. Oreshkin  
   **Venue/source:** arXiv cs.LG  
   **Release date:** submitted August 6, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2608.06559))  
   This paper asks whether frozen in-context tabular foundation models can be converted into randomized online decision policies. The proposed BC-ICL policy bootstraps the interaction history each round, conditions the pretrained ICL model on the resample, scores every action, and acts according to the sampled score. The arm-context conditioning architecture is the key design point: instead of treating arms independently, it shares statistical strength across actions and reduces bootstrap pathologies in cold-start contextual bandits. The reported gains are strongest in early-round regret under a strict online protocol.  
   **Why you should care:** It is a concrete step from tabular FMs as predictors to tabular FMs as decision-making primitives.

3. **Target-Weighted Neyman Allocation: Experimental Design for Heterogeneous Treatment Effects under Population Shift**  
   **Authors:** Hoang Dang, Luan Pham, Minh Nguyen  
   **Venue/source:** arXiv cs.LG / stat.ME  
   **Release date:** submitted August 6, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2608.06512))  
   The paper addresses a common deployment mismatch: experiments are run in one population, but treatment-effect decisions are needed in another. Standard allocation by experimental proportions ignores deployment prevalence, while allocation by target proportions can undersample noisy or difficult strata. Target-Weighted Neyman Allocation uses a two-stage stratified design: pilot variance estimates determine final-stage sample sizes and treatment probabilities for target-weighted GATE precision. The oracle rule is closed-form, plug-in estimates converge to it, and variants handle uncertain target composition and contaminated or rare-event outcomes.  
   **Why you should care:** It gives a practical design rule for HTE experiments when the population of scientific interest is not the population you can easily randomize.

4. **Robust Average-Reward Markov Decision Processes: Minimax-Optimal Learning via Plug-in Reductions**  
   **Authors:** Yuepeng Yang, Yuxin Chen, Yuejie Chi  
   **Venue/source:** arXiv cs.LG / stat.ML / math.OC  
   **Release date:** submitted August 6, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2608.06545))  
   This is a theory-heavy robust RL paper with unusually crisp sample-complexity structure. It studies average-reward MDPs under rectangular total-variation uncertainty sets and identifies the perturbation scale separating high- and low-tolerance regimes. The minimax rates have a nominal-looking linear-span term and, only in the low-tolerance regime, an additional robustness-specific term. The algorithms are plug-in reductions that choose between nominal and robust reductions and calibrate discounting either from known span parameters or from data.  
   **Why you should care:** The result clarifies when robust sequential decision-making is statistically “free” and when robustness imposes a real extra sample-complexity tax.

5. **MIRA: Evidence-Verified Repair Memory for Text-to-SQL Correction**  
   **Authors:** Yining Liu, Chenyu Yang, Boyan Li, Rui Mao, Yuyu Luo  
   **Venue/source:** arXiv cs.DB  
   **Release date:** submitted August 7, 2026  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/abs/2608.06950))  
   MIRA targets a failure mode that matters for database agents: executable SQL can still be semantically wrong, and repair mechanisms can corrupt already-correct queries. Instead of storing coarse “experiences,” MIRA decomposes historical corrections into independently reusable repair memory items, retrieves them using the question and SQL, verifies each against database evidence, and adapts only supported repairs. Evaluation covers 1,785 queries from three text-to-SQL agents over 14 BIRD and ScienceBenchmark databases, with reported execution-accuracy gains of 16.53% and 8.78%.  
   **Why you should care:** It is a plausible pattern for agent memory in structured-data systems: store small, evidence-checked repair atoms rather than monolithic traces.

## Section 2: Venue Watch

- **arXiv cs.LG / stat.ML / cs.DB, August 10 new-submission wave.** The Monday batch is unusually relevant: 84 new cs.LG submissions, 2 new stat.ML submissions, and 5 new cs.DB submissions. Clusters include causal falsification and HTE design, tabular-FM bandits, robust MDP theory, multimodal retrieval certification, long-horizon agent context compression, semantic-operator execution, text-to-SQL repair memory, adaptive similarity indexes, and causal data-management infrastructure. This was a good day for “models as data/decision infrastructure,” not just another LLM benchmark dump. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **TMLR August 2026 accepted-paper stream, incremental update.** New visible items broaden the month’s earlier themes: data-science agents over heterogeneous formats, trajectory-geometry predictors for chain-of-thought correctness, efficient quantization, GP optimization, structured set utility, agent memory, tool-agent verification, safe generative sampling, and foundation-model transparency. The items most worth tracking for Adam are **DS-STAR** for heterogeneous-format data-science agents, **Predicting Chain-of-Thought Correctness from Trajectory Geometry** for reasoning diagnostics, and **Learning Structured Set Utility Functions with Contrastive Element Representations** for set-valued preference/utility representation. ([jmlr.org](https://jmlr.org/tmlr/papers/))

- **KDD 2026 is now in conference mode.** As of August 10, workshops/tutorials are underway in Jeju, with the opening session and awards scheduled for the evening of August 10. The main conference begins August 11 with Jeff Dean’s keynote, followed by Data Day, Korea Day, dissertation awards, Test-of-Time awards, oral tracks, KDD Cup sessions, and special days for health, education, and AI reasoning. Wait for official award pages before recording best-paper outcomes; today’s signal is the shift from preconference program awareness to live venue activity. ([kdd2026.kdd.org](https://kdd2026.kdd.org/schedule-at-a-glance/))

- **NeurIPS 2026 workshops: unofficial complete index now useful for scouting.** A third-party OpenReview-derived index reports 73 accepted workshop subgroups across Sydney, Atlanta, and Paris, with deadlines and location metadata, but it explicitly warns that some deadlines are site-reported, stale, or inconsistent. This is worth using as a discovery aid for structured-data, agents, representation, privacy, and systems-adjacent workshops, but not as an official archival venue record. ([danyaljj.github.io](https://danyaljj.github.io/neurips2026-workshops/))

## Section 3: Emerging Trends

- **Tabular FMs are moving from passive predictors to adaptive policies.** BC-ICL’s bootstrapped action selection, SkillTFM’s training-free adaptation from the previous brief, and time-series/tabular transfer work all point toward “frozen structured-data model + inference-time procedure” as the design pattern.

- **Causal ML is becoming more operational.** ACIF, TWNA, unstructured-treatment/outcome causal queries, causal data-management layers, and agentic causal-research tools all treat causality as something to test, deploy, query, or automate—not just estimate offline.

- **Agent memory is converging with database repair and provenance.** MIRA’s repair atoms, AgentTrails, semantic isolation, DS-STAR, and text-to-SQL correction work suggest that useful agent memory will look more like evidence-indexed, schema-aware data management than a generic vector store.

- **Semantic operators are entering their compilation phase.** SemBaker is a material upgrade from the earlier vision paper: the community is now trying to compile natural-language predicates into deterministic executable code, with cost-based routing, instead of invoking LLMs row-by-row.

- **Evaluation work is increasingly “operating-point aware.”** The data-cleaning paper on removal-budget confounding, BayesAME, confidence horizons, and active model evaluation all push against leaderboard-style comparisons that hide budget, threshold, or decision-policy differences.

## Section 4: Worth Watching

- **SemBaker / “From Interpretation to Compilation: A Compilation-Based Execution Engine for Semantic Operator Systems.”** This is materially new relative to the previously covered vision paper: it implements a compilation engine for semantic filters, maps, and joins, invokes an LLM once to generate deterministic Python, routes operators through a cost-based optimizer, and reports 4.8–6.3× speedups plus 5.4–10.7× cost reductions across QA workloads. Suppress future repeats unless code or integration scope changes. ([arxiv.org](https://arxiv.org/abs/2608.06677))

- **DS-STAR: Data Science Agent for Solving Diverse Tasks across Heterogeneous Formats and Open-Ended Queries.** Newly visible in TMLR August 2026, this looks directly relevant to the “agentic data scientist” line connecting DataAgent-Bench, CausalDS, Baikal, and database-agent benchmarks. ([jmlr.org](https://jmlr.org/tmlr/papers/))

- **GPTKB 2.0.** A large LLM-derived, disambiguated knowledge base with 38.4M triples, 1.6M canonical entities, SPARQL access, natural-language-to-SPARQL, provenance auditing, and downloadable data. Worth tracking as a resource for entity resolution, KB construction, and provenance-aware LLM-derived structured data. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

- **NeurIPS 2026 accepted-workshop index.** Not official, but useful for planning submissions and scouting signals. Treat the 73-workshop OpenReview scrape as a mutable discovery resource and suppress repeats until official NeurIPS pages or accepted workshop-paper lists appear. ([danyaljj.github.io](https://danyaljj.github.io/neurips2026-workshops/))

## Section 5: Discord Highlights

**Aug 10 — Research brief highlights**

Top papers:
1. **Adversarial Causal Intervention Falsification** — causal generative models evaluated by adversarially chosen interventions.
2. **Bootstrap-Conditioned Action Selection with Tabular Foundation Models** — turns frozen tabular FMs into randomized contextual-bandit policies.
3. **Target-Weighted Neyman Allocation** — HTE experimental design under deployment-population shift.
4. **Robust Average-Reward Markov Decision Processes** — minimax sample complexity for robust average-reward RL.
5. **MIRA** — evidence-verified repair memory for text-to-SQL agents.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-08-10","type":"paper","title":"Adversarial Causal Intervention Falsification","authors_or_org":"Mojtaba Eslami","url":"https://arxiv.org/abs/2608.06427","memory":"Top 5 paper. Covered Aug 5 2026 arXiv paper on adversarial experimentalist vs structural causal generator, intervention-indexed discriminator, worst-intervention IPM, interventional equivalence, finite-sample guarantees, and active causal design. Suppress arXiv revisions, reposts, code, and venue versions unless materially expanded."}
{"date_delivered":"2026-08-10","type":"paper","title":"Bootstrap-Conditioned Action Selection with Tabular Foundation Models","authors_or_org":"Devansh Gupta, Shiv Tavker, Dmitry Efimov, Suchitra Sathyanarayana, Gitanjali Bhutani, Boris N. Oreshkin","url":"https://arxiv.org/abs/2608.06559","memory":"Top 5 paper. Covered BC-ICL: bootstrap-conditioned in-context tabular foundation models for contextual bandits, arm-context conditioning, randomized action selection, cold-start and early-regret improvements. Suppress future arXiv/code/venue/social repeats unless online decision framework or evidence materially changes."}
{"date_delivered":"2026-08-10","type":"paper","title":"Target-Weighted Neyman Allocation: Experimental Design for Heterogeneous Treatment Effects under Population Shift","authors_or_org":"Hoang Dang, Luan Pham, Minh Nguyen","url":"https://arxiv.org/abs/2608.06512","memory":"Top 5 paper. Covered TWNA, two-stage stratified experimental design for target-weighted GATE precision under population shift, closed-form oracle allocation, plug-in rule, uncertain deployment composition, and rare-event/contamination variants. Suppress future versions unless theory or empirical scope materially changes."}
{"date_delivered":"2026-08-10","type":"paper","title":"Robust Average-Reward Markov Decision Processes: Minimax-Optimal Learning via Plug-in Reductions","authors_or_org":"Yuepeng Yang, Yuxin Chen, Yuejie Chi","url":"https://arxiv.org/abs/2608.06545","memory":"Top 5 paper. Covered minimax sample complexity for average-reward robust MDPs under rectangular TV uncertainty, perturbation-scale regimes, matching upper/lower bounds, and span-informed/span-agnostic plug-in reductions. Suppress future arXiv/venue/code mentions unless rates or scope materially expand."}
{"date_delivered":"2026-08-10","type":"paper","title":"MIRA: Evidence-Verified Repair Memory for Text-to-SQL Correction","authors_or_org":"Yining Liu, Chenyu Yang, Boyan Li, Rui Mao, Yuyu Luo","url":"https://arxiv.org/abs/2608.06950","memory":"Top 5 paper. Covered evidence-verified repair memory for text-to-SQL correction, independently reusable repair memory items, retrieval by question and SQL, database-evidence verification, adaptation, and evaluation on BIRD and ScienceBenchmark. Suppress future arXiv/code/venue/repost versions unless artifact or method materially expands."}
{"date_delivered":"2026-08-10","type":"proceedings","title":"arXiv cs.LG/stat.ML/cs.DB new-submission stream for August 10 2026","authors_or_org":"arXiv cs.LG, stat.ML, cs.DB","url":"https://arxiv.org/list/cs.LG/new","memory":"Venue Watch. Covered Aug 10 2026 arXiv stream: 84 new cs.LG submissions, 2 new stat.ML submissions, 5 new cs.DB submissions; themes in causal falsification, HTE design, tabular-FM bandits, robust MDPs, semantic operators, text-to-SQL repair memory, adaptive similarity indexes, and causal data management. Suppress repeat broad daily stream summary."}
{"date_delivered":"2026-08-10","type":"proceedings","title":"TMLR August 2026 accepted papers incremental update as of August 10","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered visible TMLR August 2026 additions including DS-STAR, chain-of-thought trajectory geometry, EHR2Path, materials discovery agents, structured set utility, quantization, GP optimization, safe generative sampling, tool-agent verification, and other August accepted papers. Suppress repeat Aug 10 incremental snapshot."}
{"date_delivered":"2026-08-10","type":"announcement","title":"KDD 2026 live conference schedule / opening session and awards awareness","authors_or_org":"ACM SIGKDD / KDD 2026","url":"https://kdd2026.kdd.org/schedule-at-a-glance/","memory":"Venue Watch. Covered KDD 2026 in Jeju entering live mode: Aug 9-10 workshops/tutorials, Aug 10 opening session and awards, Aug 11 Jeff Dean keynote, Data Day, Korea Day, dissertation awards, Test-of-Time awards, KDD Cup sessions, health/education/reasoning special days. Suppress repeat schedule awareness; cover official awards/results/proceedings only when released."}
{"date_delivered":"2026-08-10","type":"resource","title":"NeurIPS 2026 Workshops unofficial OpenReview-derived index","authors_or_org":"Third-party OpenReview scrape by danyaljj / NeurIPS workshop metadata","url":"https://danyaljj.github.io/neurips2026-workshops/","memory":"Venue Watch and Worth Watching. Covered unofficial index reporting 73 accepted NeurIPS 2026 workshop subgroups across Sydney, Atlanta, and Paris with deadlines/location metadata and caveats about stale or site-reported deadlines. Suppress repeat index mentions unless official NeurIPS accepted-workshop list, accepted-paper lists, or materially changed metadata appears."}
{"date_delivered":"2026-08-10","type":"software","title":"SemBaker / From Interpretation to Compilation: A Compilation-Based Execution Engine for Semantic Operator Systems","authors_or_org":"Wenkai Dong, Yifan Wang","url":"https://arxiv.org/abs/2608.06677","memory":"Worth Watching. Material expansion of previously delivered vision paper 'From Interpretation to Compilation'. Covered SemBaker engine compiling semantic filters/maps/joins into deterministic Python with cost-based routing, adapters for Palimpzest/LOTUS/Nirvana/DocETL, speedup and cost-reduction claims. Suppress future repeats unless code, benchmark, or system integration materially changes."}
{"date_delivered":"2026-08-10","type":"paper","title":"DS-STAR: Data Science Agent for Solving Diverse Tasks across Heterogeneous Formats and Open-Ended Queries","authors_or_org":"Jaehyun Nam, Jinsung Yoon, Jiefeng Chen, Rajarishi Sinha, Jinwoo Shin, Tomas Pfister","url":"https://jmlr.org/tmlr/papers/","memory":"Worth Watching TMLR August 2026 item. Covered as a data-science agent for heterogeneous formats and open-ended queries, relevant to DataAgent-Bench, CausalDS, Baikal, and database-agent benchmarks. Suppress TMLR/OpenReview/code repeats unless artifact or results materially expand."}
{"date_delivered":"2026-08-10","type":"resource","title":"GPTKB 2.0: Browsing, Querying, and Auditing a Disambiguated LLM-Derived Knowledge Base","authors_or_org":"Yujia Hu, Tuan-Phong Nguyen, Simon Razniewski","url":"https://arxiv.org/abs/2608.06992","memory":"Worth Watching resource. Covered GPTKB 2.0 as LLM-derived disambiguated KB with 38.4M triples, 1.6M canonical entities, relation/class consolidation, SPARQL and NL-to-SPARQL querying, provenance auditing, and downloadable full KB. Suppress future demo/arXiv/site mentions unless KB materially expands or becomes central."}
```