## Section 1: Top 5 Papers

1. **CIDER-FM: Foundation Models for Causal Inference from Diverse Experimental Regimes**  
   **Authors:** Yuche Gao, Arik Reuter, Siyuan Guo, Anish Dhir, Bernhard Schölkopf, Adrian Weller  
   **Venue/source:** arXiv  
   **Release date:** October 1, 2026 arXiv new listing  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   **Summary:** CIDER-FM targets a gap in causal foundation models: observational data alone often leaves the target causal effect underidentified, while interventions on the exact target variable are rarely available. The paper formalizes how *surrogate* experiments—interventions on related variables or regimes—can improve prediction of a target conditional interventional distribution. Architecturally, CIDER-FM uses intervention-aware representations plus hierarchical attention across variables, samples, and experimental regimes. The evaluation spans synthetic SCM families and Causal Chambers data, positioning the work as a practical step from “causal PFN over observational tables” toward amortized multi-regime experimental reasoning.  
   **Why you should care:** This is one of the clearest moves toward causal foundation models that use realistic experimental fragments rather than pretending every deployment is purely observational or perfectly randomized.

2. **Which Tasks Survive Self-Supervised Learning?**  
   **Authors:** Achleshwar Luthra, Lucas Bryant, Tracy Zhu, Tomer Galanti  
   **Venue/source:** arXiv  
   **Release date:** October 1, 2026 arXiv new listing  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   **Summary:** This paper gives a task-level account of what information same-instance SSL preserves. It introduces “semantic recoverability,” measuring how much of a downstream task’s posterior score lies in the learned representation function space. For centered/whitened representations, recoverability exactly characterizes directional class-distance-normalized variance, controls few-shot nearest-centroid classification, and predicts semantic direction strength. For a canonical two-view SSL objective, the population optimum spans leading cross-view-stable spectral modes, so task survival depends on whether the task posterior lies in that selected subspace. The empirical validation connects recoverability, geometry, spectra, and few-shot transfer.  
   **Why you should care:** It offers a useful language for representation-learning evaluation: not “is the embedding good?” but “which downstream task posteriors did the objective make linearly/geometrically available?”

3. **CDMD: A Cross-Dataset Mixed-Type Diffusion Model for Tabular Data**  
   **Authors:** Mohamed Amine Ketata, Maximilian Schambach, Stephan Günnemann  
   **Venue/source:** arXiv; accepted at BeNTo workshop, NeurIPS 2026  
   **Release date:** October 1, 2026 arXiv new listing  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   **Summary:** CDMD tackles transferable tabular generation across heterogeneous schemas. Rather than embedding all tables into a generic continuous representation, it defines diffusion directly over mixed numerical/categorical feature spaces and uses schema-restricted reverse-process parameterization so categorical outputs respect each feature’s vocabulary. Feature-level diffusion processes are composed into schema-dependent row-level processes, and a shared schema-aware Transformer denoiser learns dependencies across variable feature sets. This is an important design point for tabular generative foundation models: cross-dataset transfer without losing mixed-type semantics to a continuous latent bottleneck.  
   **Why you should care:** If tabular synthesis is moving from per-dataset generators to pretrained generators, schema-aware mixed-type diffusion is likely to become a central design axis.

4. **Revisiting scaling laws for reward optimization**  
   **Authors:** Ali Aouad, Aymane El Gadarri, Vivek F. Farias  
   **Venue/source:** arXiv  
   **Release date:** October 1, 2026 arXiv new listing  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   **Summary:** This paper studies how reward-optimization performance scales jointly with preference-data size and KL-divergence budget. It proposes a simple law: performance scales like roughly \(\sqrt{\min\{\log(M),K\}}\), where \(M\) is the number of preference comparisons and \(K\) is the policy’s divergence budget. The authors give an information-theoretic model and constructive achievability result, then fit the law using a real annotation setup with a 70B gold reward model and proxy reward models in the 0.6B–4B range. It reframes reward optimization as selection from noisy Gaussian-like feedback.  
   **Why you should care:** It links post-training compute, data collection, and overoptimization in a way that could influence practical RLHF/RLAIF budgeting.

5. **EHR2Trace: Auditable EHR Data Infrastructure for Patient World Models and Clinical Agents**  
   **Authors:** Xinye Yang, Yuli Wang, Cheng Ting Lin, Harrison Bai  
   **Venue/source:** arXiv; cross-listed cs.LG/cs.DB/q-bio.QM  
   **Release date:** October 1, 2026 arXiv new listing  
   **Link:** arXiv. ([arxiv.org](https://arxiv.org/list/cs.LG/new))  
   **Summary:** EHR2Trace is a data-infrastructure paper for patient world models and clinical agents. It converts heterogeneous EHRs into traceable patient events, records source provenance, separates event time from information availability, and distinguishes orders, dispensing, and administration. The authors report conversion of 846.4M events across three clinical datasets and show that assigning later diagnoses to admission time inflates measured performance, while availability-filtered deployment histories degrade such models. The paper is less about a new model than about making temporal clinical data usable for world-model training and evaluation.  
   **Why you should care:** It is a concrete example of the data-management layer that structured-data foundation models and clinical agents will need before their evaluations are trustworthy.

## Section 2: Venue Watch

**arXiv cs.LG/stat.ML/cs.DB, October 1 new-listing wave.** The October 1 cs.LG page is unusually large, with 256 new submissions and 638 total entries, while cs.DB lists five new submissions plus cross-lists. The strongest clusters for Adam’s interests are: causal foundation models and multi-regime causal inference; cross-dataset tabular generation; representation-survival theory for SSL; reward-optimization scaling laws; agent harness and context-control systems; EHR/data-provenance infrastructure; and database support for document extraction, exploratory data tasks, and object-graph prefetching. The most directly relevant items are the five Top Papers above, plus O-Funnel, Temporal Trace Graph prefetching, MIND, PEG-Tab, MILO, and Hermes. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

**TMLR September 2026 tail visible on October 1.** TMLR’s top-of-page additions include *Data-Driven Priors for Uncertainty-Aware Risk Prediction of Clinical Deterioration using Multimodal Data*, a reproducibility study of weight-based mechanistic interpretability in bilinear MLPs, *SMART: A Modular Two-Stage Framework for Structural Representation Attribution*, and a hybrid-LM routing-specialization paper. The interesting signal is a convergence between uncertainty-aware clinical prediction, mechanistic interpretability reproducibility, and structural attribution tools—less flashy than the arXiv stream but useful as a peer-reviewed counterweight. ([jmlr.org](https://jmlr.org/tmlr/papers/))

**NeurIPS 2026 status.** The official accepted-papers page still renders “Accepted Papers 0,” so broad accepted-paper coverage should continue to wait. The blog did add the affinity-events announcement on September 25: events span Sydney, Paris, and Atlanta, including Africa in AI, GlobalSouthAI, LatinX in AI, Muslims in ML, New in ML, Queer in AI, and WiML. This is mainly venue-awareness rather than research content, but it matters for workshop/community activity tracking. ([nips.cc](https://nips.cc/Conferences/2026/AcceptedPapersInitial))

**JMLR Volume 27 status.** The visible JMLR Volume 27 tail remains at article 205, *A Library for Learning Neural Operators*, with no new post-205 entries visible in the current crawl. No new JMLR item should be repeated until the volume tail moves. ([jmlr.org](https://www.jmlr.org/papers/v27/))

## Section 3: Emerging Trends

- **Causal foundation models are becoming multi-regime models.** CIDER-FM and recent causal-tabular work shift from amortizing observational adjustment to integrating observational, surrogate-interventional, and target-experimental fragments.

- **Tabular generation is bifurcating into semantic-control and schema-native diffusion.** CDMD, MIND, PEG-Tab, and prior semantic-rule tabular diffusion all point to generators that preserve type, schema, marginal constraints, dependency structure, and release-time safety.

- **Representation evaluation is getting more task-conditional.** “Which tasks survive SSL?” and Rashomon-representation prediction both argue that representation quality is not scalar; it is a map from objectives to recoverable downstream semantics.

- **Agent performance is increasingly treated as harness-and-data-system co-design.** Hermes, MILO, EHR2Trace, TTG prefetching, O-Funnel, and recent BI/data-agent papers all emphasize that the model is only one layer in a reasoning system.

- **Post-training theory is being put on a scaling-law footing.** Reward-optimization scaling, TailSFT-like filtering, low-rank post-training, and RL outcome prediction are converging on a more quantitative account of what post-training can buy per unit data/compute.

## Section 4: Worth Watching

- **MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution.** A full-harness evolutionary search system with lineage memory, mutator agents, and orchestrator-level adaptation, reporting gains on Terminal-Bench, PaperBench, and DeepSWE. Worth suppressing as a concrete agent-harness artifact. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **Hermes / Hermes-Learn.** A configurable context-allocation and reuse harness for test-time scaling, plus a training method that teaches contextual reasoning strategies. Relevant to multi-context agents and adaptive inference-time compute. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **O-Funnel.** A schema-drift-resistant document extraction library that converts heterogeneous XML/JSON/CSV/HTML/key-value documents into a typed tree, verifies lossless capture, and fuses key/path/value/synonym evidence for extraction. ([arxiv.org](https://arxiv.org/list/cs.DB/new))

- **MIND: Marginal-Invariant Neural Dependency Diffusion for Mixed-Type Tabular Generation.** Separates column-wise marginal transport from latent dependency diffusion, then rank-projects samples to reduce marginal shift. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

- **PEG-Tab: Sampling-Time Record Repair and Release Control for Tabular Synthesis.** A post-training repair/release-control layer for frozen tabular generators aimed at reducing record reproduction without retraining. ([arxiv.org](https://arxiv.org/list/cs.LG/new))

## Section 5: Discord Highlights

**Oct 1 brief**

Top papers:
1. **CIDER-FM** — causal foundation model that combines observational and surrogate-interventional regimes.
2. **Which Tasks Survive Self-Supervised Learning?** — spectral/task-level theory of what SSL representations preserve.
3. **CDMD** — cross-dataset mixed-type tabular diffusion with schema-restricted categorical generation.
4. **Revisiting scaling laws for reward optimization** — joint law for preference-data size and KL budget.
5. **EHR2Trace** — auditable EHR event infrastructure for patient world models and clinical agents.

Full brief: <link inserted by workflow>

```delivered_items_jsonl
{"date_delivered":"2026-10-01","type":"paper","title":"CIDER-FM: Foundation Models for Causal Inference from Diverse Experimental Regimes","authors_or_org":"Yuche Gao, Arik Reuter, Siyuan Guo, Anish Dhir, Bernhard Schölkopf, Adrian Weller","url":"https://arxiv.org/abs/2609.39523","memory":"Top 5 paper. Covered causal foundation model using observational plus surrogate-interventional datasets, intervention-aware representations, hierarchical attention across variables/samples/regimes, and Causal Chambers evaluation. Suppress future arXiv/code/venue/social reposts unless architecture, theory, or empirical scope materially changes."}
{"date_delivered":"2026-10-01","type":"paper","title":"Which Tasks Survive Self-Supervised Learning?","authors_or_org":"Achleshwar Luthra, Lucas Bryant, Tracy Zhu, Tomer Galanti","url":"https://arxiv.org/abs/2609.38393","memory":"Top 5 paper. Covered semantic recoverability theory for same-instance SSL, spectral characterization of which downstream task posteriors survive, CDNV/few-shot geometry links, and synthetic/real validation. Suppress future arXiv/code/venue versions unless theory or empirical scope materially expands."}
{"date_delivered":"2026-10-01","type":"paper","title":"CDMD: A Cross-Dataset Mixed-Type Diffusion Model for Tabular Data","authors_or_org":"Mohamed Amine Ketata, Maximilian Schambach, Stephan Günnemann","url":"https://arxiv.org/abs/2609.39124","memory":"Top 5 paper. Covered NeurIPS 2026 BeNTo workshop paper on cross-dataset schema-aware mixed-type tabular diffusion, schema-restricted categorical reverse process, row-level composed diffusion, and shared Transformer denoiser. Suppress future arXiv/workshop/code reposts unless generator or benchmark materially expands."}
{"date_delivered":"2026-10-01","type":"paper","title":"Revisiting scaling laws for reward optimization","authors_or_org":"Ali Aouad, Aymane El Gadarri, Vivek F. Farias","url":"https://arxiv.org/abs/2609.38526","memory":"Top 5 paper. Covered scaling law for reward optimization as roughly sqrt(min{log(M),K}) in preference-data size and KL budget, information-theoretic model, constructive achievability, and 70B gold reward model experiments. Suppress future versions unless theory or empirical scope materially changes."}
{"date_delivered":"2026-10-01","type":"paper","title":"EHR2Trace: Auditable EHR Data Infrastructure for Patient World Models and Clinical Agents","authors_or_org":"Xinye Yang, Yuli Wang, Cheng Ting Lin, Harrison Bai","url":"https://arxiv.org/abs/2609.38193","memory":"Top 5 paper. Covered EHR-to-trace infrastructure separating event time from information availability, OMOP/MEDS export, provenance, validation, 846.4M converted events, injected-fault detection, and leakage from assigning later diagnoses to admission time. Suppress future arXiv/code/clinical-agent reposts unless system or datasets materially expand."}
{"date_delivered":"2026-10-01","type":"proceedings","title":"arXiv cs.LG/stat.ML/cs.DB new-submission stream for October 1 2026","authors_or_org":"arXiv cs.LG, stat.ML, cs.DB","url":"https://arxiv.org/list/cs.LG/new","memory":"Venue Watch. Covered Oct 1 2026 arXiv streams: cs.LG 256 new submissions out of 638 entries, cs.DB five new submissions plus cross-lists; themes included causal FMs, tabular diffusion/synthesis, SSL representation theory, reward scaling laws, EHR data infrastructure, agent harness discovery, document extraction, and exploratory-data-task recommendation. Suppress repeat broad daily stream summary."}
{"date_delivered":"2026-10-01","type":"proceedings","title":"TMLR September 2026 accepted papers tail visible as of October 1","authors_or_org":"Transactions on Machine Learning Research","url":"https://jmlr.org/tmlr/papers/","memory":"Venue Watch. Covered visible Oct 1 top-of-page TMLR September tail: Data-Driven Priors for multimodal clinical deterioration risk, reproduction study of weight-based mechanistic interpretability in bilinear MLPs, SMART structural representation attribution, and genre-associated routing specialization. Suppress repeat Oct 1 TMLR tail snapshot."}
{"date_delivered":"2026-10-01","type":"announcement","title":"NeurIPS 2026 Affinity Events announcement","authors_or_org":"NeurIPS 2026 Communication Chairs / affinity-event organizers","url":"https://blog.neurips.cc/2026/09/25/announcing-the-neurips-2026-affinity-events/","memory":"Venue Watch. Covered Sep 25 2026 NeurIPS affinity-events announcement spanning Sydney, Paris, and Atlanta, including Africa in AI, GlobalSouthAI, LatinX in AI, Muslims in ML, New in ML, Queer in AI, and WiML. Suppress repeat announcement summaries."}
{"date_delivered":"2026-10-01","type":"announcement","title":"NeurIPS 2026 accepted-paper page still shows Accepted Papers 0 as of October 1","authors_or_org":"NeurIPS 2026","url":"https://nips.cc/Conferences/2026/AcceptedPapersInitial","memory":"Venue Watch status. Checked official accepted-papers page and it still rendered Accepted Papers 0. Suppress repeat status note; cover official accepted-paper list once populated."}
{"date_delivered":"2026-10-01","type":"venue_issue","title":"JMLR Volume 27 latest papers stream status as of October 1 2026","authors_or_org":"Journal of Machine Learning Research","url":"https://www.jmlr.org/papers/v27/","memory":"Venue Watch no-new-tail status. Checked JMLR Volume 27 and noted latest visible entry remains article 205, A Library for Learning Neural Operators, already covered previously. Suppress repeat no-change status unless new JMLR papers appear."}
{"date_delivered":"2026-10-01","type":"paper","title":"MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution","authors_or_org":"Prithwish Jana, Mononito Goswami, Hao Liu, Xinyu Li, Langlin Huang, Zhehui Huang, Zhishen Huang, Patrick Blöbaum, Anoop Deoras, Purak Jain, Nikos Kanakaris, Sahika Genc","url":"https://arxiv.org/abs/2609.38349","memory":"Worth Watching. Covered automated co-evolution of agent harnesses and search strategy with lineage memory, mutator agents, and orchestrator; reported gains on Terminal-Bench, PaperBench, DeepSWE, and EinsteinArena. Suppress future arXiv/code/social/venue repeats unless harness framework or evaluation materially expands."}
{"date_delivered":"2026-10-01","type":"paper","title":"Hermes: Learning Contextual Reasoning Unlocks Test-Time Scaling","authors_or_org":"Xinyu Li, Mononito Goswami, Hao Liu, Nikos Kanakaris, Langlin Huang, Prithwish Jana, Patrick Blöbaum, Purak Jain","url":"https://arxiv.org/abs/2609.38332","memory":"Worth Watching. Covered Hermes configurable test-time scaling harnesses and Hermes-Learn framework for teaching context allocation/reuse across multiple context windows. Suppress future arXiv/code/social reposts unless method or benchmark materially changes."}
{"date_delivered":"2026-10-01","type":"software","title":"O-Funnel: Lossless Structural Capture and Requirement-Driven Extraction from Drifting, Heterogeneous Documents","authors_or_org":"Osama Mustafa","url":"https://arxiv.org/abs/2609.39209","memory":"Worth Watching and cs.DB item. Covered dependency-free document extraction library converting XML/JSON/CSV/HTML/key-value text into verified typed trees and fusing structural/value evidence for drift-resistant extraction. Suppress future arXiv/GitHub/venue mentions unless library or benchmark materially expands."}
{"date_delivered":"2026-10-01","type":"paper","title":"MIND: Marginal-Invariant Neural Dependency Diffusion for Mixed-Type Tabular Generation","authors_or_org":"Pengfei Li, Mohammad Khalil","url":"https://arxiv.org/abs/2609.39628","memory":"Worth Watching. Covered mixed-type tabular generation method separating column-wise marginal transport from latent dependency diffusion, with copula-tangent denoising and rank projection. Suppress future arXiv/code/venue reposts unless method or benchmark materially changes."}
{"date_delivered":"2026-10-01","type":"paper","title":"PEG-Tab: Sampling-Time Record Repair and Release Control for Tabular Synthesis","authors_or_org":"Pengfei Li, QinYi Liu, Mohammad Khalil","url":"https://arxiv.org/abs/2609.39630","memory":"Worth Watching. Covered post-training repair and release-control framework for frozen tabular generators to reduce record reproduction at sampling/release time. Suppress future arXiv/code/venue repeats unless framework or privacy evidence materially expands."}
```