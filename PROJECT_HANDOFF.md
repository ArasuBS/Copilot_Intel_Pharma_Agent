# AI-Driven Pharma Intelligence Agent

## Purpose

Build an ontology-driven pharma intelligence platform for CSO-office technology scouting.

The goal is not literature search.

The goal is continuous monitoring, classification, signal accumulation, trend detection, and strategic intelligence generation.

---

# Vision

Sources
↓
Collection
↓
Classification
↓
Reporting
↓
Historical Signal Storage
↓
Trend Analysis
↓
Strategic Insights

Target Users:
- CSO Office
- R&D Leadership
- Strategy Teams
- Business Development
- Technology Scouting Teams

---

# Current Development Stage

STATUS: Phase 1 Complete

Completed:

✅ Source Collection

✅ Ontology Layer

✅ Classification Layer

✅ GitHub Workflow Automation

✅ Multi-Modality Classification

Not Yet Built:

❌ Human Readable Reporting

❌ Trend History

❌ Historical Signal Memory

❌ Strategic Insight Engine

❌ Abstract Analysis

❌ Azure OpenAI Signal Extraction

---

# Strategic Positioning

This project is different from Gemini, ChatGPT, or search engines.

Those tools answer questions.

This agent continuously monitors predefined scientific and business domains, classifies signals, stores historical evidence, identifies trends, and generates strategic intelligence.

---

# Architecture

Sources
↓
Collectors
↓
Raw Records
↓
Classifier
↓
Structured Signals
↓
Reports
↓
Trend Memory
↓
Insights

---

# Current Sources

Operational

✅ PubMed

✅ Fierce Pharma RSS

Planned

- Fierce Biotech
- BioPharma Dive
- Contract Pharma
- GEN
- Nature Biotechnology
- Europe PMC
- ClinicalTrials.gov
- NIH Reporter
- FDA
- EMA
- OECD
- NC3Rs
- AACR
- ASCO
- Company Websites

---

# Current Modalities

## ADC

Ontology Sections

- keywords
- targets
- payloads
- technologies
- antibody_formats
- indications
- watch_companies
- products
- competitor_cros
- competitor_cdmos
- manufacturing
- deal_types
- strategic_questions

Classification Uses

- keywords
- targets
- products
- payloads
- technologies

Current ADC Classification Vocabulary

78 terms

---

## NAMS

Ontology Sections

- keywords
- organoid_models
- organ_on_chip
- advanced_models
- manufacturing_and_scaleup
- dmpk_applications
- tox_applications
- efficacy_applications
- adoption_stage
- watch_companies
- computational_nams_companies
- computational_technologies
- pharma_adopters
- competitor_cros
- competitor_cdmos
- deal_types
- regulatory_and_validation
- strategic_questions

Classification Uses

keywords only

Current Classification Vocabulary

25 terms

Priority Retrieval Keywords

- Spheroid
- Patient Derived Organoid
- Tumor Organoid
- Organ Chip
- Liver Organoid
- Liver On Chip
- Microphysiological Systems

---

## Bispecifics

Ontology Sections

- keywords
- targets
- products
- companies
- deal_types
- strategic_questions

Classification Uses

keywords only

Current Classification Vocabulary

14 terms

---

## Cell Line Development

Ontology Exists

Current State

keywords only

Current Classification Vocabulary

10 terms

---

# Collector Design Philosophy

Important Rule

Collectors Collect

Classifier Classifies

There should be no modality-specific logic inside collectors.

---

# PubMed Collector

File

ingest_pubmed.py

Function

- Load topic ontology
- Build query
- Retrieve PubMed IDs
- Retrieve summaries
- Save results

Current Query Structure

ADC Keywords (first 2)

+

NAMS Keywords (first 7)

+

Bispecific Keywords (first 5)

+

CLD Keywords (first 5)

Current Retmax

30

Output

data/pubmed_results.json

Current Fields

- pubmed_id
- title
- pubdate
- source

Current Limitation

Reads titles only.

Does not read abstracts.

---

# RSS Collector

File

ingest_rss.py

Current Source

Fierce Pharma RSS

Current Fields

- title
- link
- date
- source

Output

data/rss_results.json

Current Limitation

Generic collection only.

No signal extraction.

No modality logic.

---

# Classifier

File

classify_records.py

Current Method

Case-insensitive title matching.

Current Logic

if keyword.lower() in title.lower()

Classification is title-based only.

No abstract analysis.

No AI reasoning.

No semantic matching.

---

# Current Classification Outputs

## classified_records.json

Example

{
  "title": "...",
  "topics": ["ADC"]
}

Output contains classified records.

---

## classification_summary.json

Example

{
  "total_records": 35,
  "classified_records": 13,
  "topic_counts": {
    "ADC": 6,
    "NAMS": 1,
    "Bispecifics": 5,
    "Cell Line Development": 1
  }
}

---

# GitHub Workflow

File

.github/workflows/pubmed-test.yml

Execution Sequence

Checkout Repository
↓
Setup Python 3.11
↓
Install Requirements
↓
Run ingest_pubmed.py
↓
Run ingest_rss.py
↓
Run classify_records.py
↓
Upload Output Artifact

Workflow Trigger

workflow_dispatch

Run manually via:

Actions
→ PubMed Test
→ Run Workflow

---

# Artifact Output

Current

Single downloadable artifact

pharma-intelligence-output.zip

Contains

- pubmed_results.json
- rss_results.json
- classified_records.json
- classification_summary.json

---

# Current Database Vision

Every article/news item should eventually become a signal.

Core Fields

- signal_id
- date
- source
- url
- title

Organizations

- company
- partner
- competitor
- pharma_adopter

Scientific Attributes

- modality
- target
- technology
- platform
- product
- indication

Business Attributes

- event_type
- deal_type

Manufacturing Attributes

- manufacturing_area
- capability

Regulatory Attributes

- regulatory_body
- validation_stage

Intelligence Attributes

- impact_score
- confidence_level
- strategic_relevance

Evidence

- summary
- extracted_entities

---

# Important Design Decision

The future system should learn from structured historical signals.

It should NOT learn from previous narrative reports.

Wrong

Report
↓
Read Old Report
↓
Generate New Report

Correct

Signals
↓
Store Historical Data
↓
Trend Detection
↓
Generate Reports

---

# Future Trend Memory Layer

Proposed File

trend_history.json

Example

[
  {
    "month": "2026-08",
    "ADC": 6,
    "NAMS": 1,
    "Bispecifics": 5,
    "Cell Line Development": 1
  }
]

Purpose

Store historical counts across runs.

Enable trend analysis.

---

# Future Reporting Layers

## Level 1 Report

Human-readable summary.

Example

ADC (6)

• Paper 1
• Paper 2

NAMS (1)

• Paper 1

---

## Level 2 Report

Trend Analysis

Examples

- Most active modality
- Rising targets
- Active companies
- Partnership activity
- Technology momentum

---

## Level 3 Report

Strategic Insights

Examples

- Which ADC targets are gaining momentum?
- Which NAM technologies are approaching adoption?
- Which CRO/CDMO capabilities are expanding?
- What strategic implications exist for outsourcing?

---

# Future Intelligence Layer

Collector
↓
Classifier
↓
Abstract Retrieval
↓
Entity Extraction
↓
Signal Store
↓
Trend Memory
↓
Reporting
↓
Strategic Insights

---

# Current Constraints

Current Agent Reads

✅ Title

✅ Date

✅ Source

Current Agent Does Not Read

❌ PubMed Abstract

❌ Full Article

❌ Company Press Releases

❌ Regulatory Documents

---

# Coding Support Requirements

Project owner is not a software developer.

All coding instructions should be given as:

- exact file name
- exact code block to find
- exact code block to replace
- exact code block to insert

Avoid high-level programming instructions.

Provide step-by-step implementation guidance.
