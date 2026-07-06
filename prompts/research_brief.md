# Recurring Research Brief Prompt

Prepare a concise research briefing tailored to Adam's research interests.

Goal: maximize the probability of discovering important new ideas, papers,
research directions, and venue activity while minimizing noise and avoiding
items already covered in prior briefings. Write like an expert research
librarian with strong judgment about machine learning, statistics, data
management, and adjacent research communities.

## Inputs

Use the current date and any provided history of previously delivered items.
The target freshness window is roughly the last month, but do not repeat items
from prior briefings even if they are newly reposted, newly published in another
venue, newly discussed, or available at a different URL.

Previously delivered history may be provided inline under a heading such as:

```text
Already Delivered History
...
```

Treat that history as memory for duplicate suppression.

## Research Interests

Prioritize foundation models for structured/tabular data; self-supervised
learning and representation learning; synthetic data generation and simulation
for machine learning; entity resolution, record linkage, identity resolution,
and data integration; causal machine learning and heterogeneous treatment
effects; probabilistic machine learning and Bayesian methods; interpretability
and understanding learned representations; general ML theory, especially
representation learning, objective functions, optimization, and generalization;
databases, data management, and ML systems where relevant. Adjacent work is
encouraged if likely to influence these areas.

## Duplicate And Staleness Rules

Do not include items already delivered in prior briefings.

Treat an item as already seen when it has the same or substantially similar
title, overlapping authors or organization, same underlying artifact, or the
same venue issue/release already covered. This applies even when the new item
has a different URL, a new publication stage, a code release, a revised arXiv
version, or renewed social attention.

For papers, treat preprint, conference, workshop, journal, camera-ready, code,
and project-page versions as the same item unless the newer version materially
changes the contribution. If mentioning a changed version, explicitly say what
is materially new.

For venue watch, do not repeat the same issue, proceedings release,
accepted-paper batch, award, or announcement once it has been covered.

## Output Structure

Write the human-readable brief in Markdown.

### Section 1: Top 5 Papers

Select the five most interesting papers published, released, or gaining
significant attention within roughly the last month, after applying duplicate
suppression. Do not balance research areas; optimize for overall importance.
Prioritize significant new methods, strong theory, elegant ideas, high
potential impact, rapid community traction, respected research groups, and
papers likely to influence future research.

For each paper include:

- title
- authors
- venue or source
- publication or release date
- link when available
- about a 100-word summary covering the problem, core idea, key findings, and
  why it matters
- one sentence labeled `Why you should care:`

Prefer papers with genuinely new ideas over incremental benchmark improvements.
Among similar papers, favor those most likely to shape future research rather
than those with the best reported metrics.

### Section 2: Venue Watch

Use this section to maintain awareness of what selected research communities
are publishing, not only to filter for Adam's current interests. Monitor new
issues, accepted-paper lists, proceedings, editorial highlights, conference
announcements, and awards from the venues below. When a watched journal or venue
publishes a new issue, proceedings batch, accepted-paper batch, or similarly
bounded release, include a compact summary of the release's contents and themes,
even if some themes are outside the core interests above.

For each included venue or release, summarize the main topical clusters,
notable methodological directions, and any papers/items that look especially
important, surprising, or relevant. Keep the summary compact; the goal is venue
awareness, not exhaustive article-by-article coverage.

Watch venues including NeurIPS, ICML, ICLR, AISTATS, UAI, TMLR, JMLR, KDD,
SIGMOD, VLDB, ICDE, ICDM, SDM, AAAI, IJCAI, Management Science, MSOM, ISR,
Organization Science, Decision Sciences, INFORMS Journal on Computing,
Operations Research, JRSS B, JASA, Annals of Statistics, and Bayesian Analysis.

Do not summarize every venue every time. Include a venue when there is a new
issue, proceedings release, accepted-paper batch, announcement, award, or
editorial item worth tracking. For management science, operations, statistics,
information systems, and database venues, preserve a broad view of the issue's
themes rather than only extracting ML-adjacent papers.

Do not let Venue Watch become a feedback loop around the primary interests. Its
job is to expose adjacent and shifting research-community activity that may
change future topic priorities.

### Section 3: Emerging Trends

In 3-6 bullets, summarize recurring themes across recent publications and venue
activity, such as synthetic pretraining, new benchmarks, evaluation standards,
diffusion models, Bayesian methods, foundation-model architectures,
interpretability, causal ML, or unexpected shifts in watched venues.

Emphasize synthesis and judgment. Do not merely restate paper titles.

### Section 4: Worth Watching

Briefly mention promising new arXiv papers, datasets, benchmark competitions,
open-source repositories, software libraries, reproducibility resources, or
community artifacts likely to become influential.

Include only items that are specific enough to be useful and worth suppressing
from future repeat briefings if they appear again.

### Section 5: Discord Highlights

Provide a short Discord-ready highlights message. It should include:

- brief date
- the five Top 5 paper titles
- one short highlight line for each paper
- a placeholder line: `Full brief: <link inserted by workflow>`

Keep this compact. The Discord message is a pointer to the full Markdown brief,
not a replacement for it.

## Delivered Items Memory

At the end of the brief, include a fenced block labeled
`delivered_items_jsonl`. Each line must be one JSON object for a concrete item
that should be suppressed from future repeat briefings.

Do not record every named entity or broad trend. Record concrete delivered
items that would be annoying or misleading to repeat later, including:

- Top 5 papers
- specific venue issues, proceedings releases, accepted-paper batches, awards,
  or announcements covered in Venue Watch
- specific papers called out in Venue Watch when they are individually
  discussed
- specific datasets, benchmarks, repositories, software libraries, or resources
  in Worth Watching

Each JSON object should use this shape:

```json
{
  "date_delivered": "YYYY-MM-DD",
  "type": "paper | venue_issue | proceedings | announcement | dataset | benchmark | repository | software | resource | other",
  "title": "Human-readable item title",
  "authors_or_org": "Authors, organization, venue, or publisher",
  "url": "Canonical URL if available",
  "memory": "Brief free-text memory of what was covered and what future runs should suppress."
}
```

The `memory` field is important. Write it for future duplicate detection by an
LLM, not for a database. Mention aliases, publication-stage relationships, issue
dates, release names, or other clues that would help identify repeats.

## Style

Target approximately 1,000-1,500 words for the human-readable brief, excluding
the delivered-items memory block. Prefer insight over exhaustiveness. Assume the
reader is an ML researcher and avoid basic explanations. Emphasize why something
is interesting, not just what it does.
