# 🛡️ SOC Dashboard Suite

## Email + Telemetry Threat Monitoring

> A security analytics engineering project that designs and implements a **mini-SOC monitoring system** for email-borne threats and authentication telemetry, focusing on detection reliability, false-positive control, and analyst-ready investigation workflows.

---

## 📌 Project Motivation

Modern SOC failures are rarely caused by a lack of data or models.
They fail because of:

* excessive false positives
* weak context enrichment
* alert fatigue
* poor correlation across telemetry
* dashboards optimized for visuals instead of decisions

This project intentionally **does not start with machine learning**.

Instead, it focuses on:

* defining reliable security signals
* designing a defensible detection pipeline
* enforcing evidence-first alerting
* building dashboards that support **triage and investigation**, not vanity metrics

The goal is to simulate how a **real enterprise SOC** designs, evaluates, and operates its monitoring systems.

---

## 🧠 Design Philosophy

This project follows the same discipline used in production SOC environments:

* Detection > Classification
* Alerts > Metrics
* Context > Volume
* Explainability > Accuracy
* Governance > Speed
* ML is *supporting*, never central

If a component increases alert noise, reduces analyst trust, or hides reasoning, it is rejected by design.

---

## 🏗️ System Overview

The SOC Dashboard Suite models an end-to-end monitoring pipeline:

```
Telemetry Sources
   ↓
Ingestion & Normalization
   ↓
Context Enrichment & Baselining
   ↓
Detection Engineering
   ↓
Alerting & Governance
   ↓
Dashboards & Investigation Views
```

### Telemetry Domains

* **Email telemetry**

  * sender identity
  * authentication signals (SPF/DKIM/DMARC)
  * attachment and URL metadata
* **Authentication telemetry**

  * login successes/failures
  * geographic and temporal context
  * device and identity attributes

---

## 🔍 What This Project Explicitly Does

✔ Defines SOC-grade schemas for email and authentication telemetry
✔ Implements ingestion and normalization with data quality guarantees
✔ Adds identity, domain, temporal, and baseline context
✔ Engineers explainable detection logic with tuning knobs
✔ Controls alert volume through gating, deduplication, and severity scoring
✔ Produces analyst-centric dashboards for triage and investigation
✔ Threat-models the SOC system itself
✔ Maps the architecture to real cloud SIEM platforms

---

## 🚫 What This Project Intentionally Does NOT Do

❌ No deep learning models
❌ No accuracy / F1 / ROC-driven claims
❌ No feature ranking for its own sake
❌ No “AI SOC” marketing narratives
❌ No unrealistic assumptions about perfect data

Any machine learning used is **minimal, interpretable, and subordinate** to SOC constraints.

---

## 📁 Repository Structure

```
soc-dashboard-suite/
│
├── README.md
│
├── architecture/
│   ├── soc_system_overview.md
│   ├── soc_system_diagram.png
│   └── threat_model.md
│
├── schema/
│   ├── email_schema.md
│   ├── telemetry_schema.md
│   └── unified_event_schema.md
│
├── data/
│   ├── raw/
│   │   ├── email/
│   │   └── telemetry/
│   ├── normalized/
│   └── enriched/
│
├── ingestion/
│   ├── email_ingestion.ipynb
│   └── telemetry_ingestion.ipynb
│
├── enrichment/
│   ├── domain_context.ipynb
│   ├── identity_context.ipynb
│   └── baseline_context.ipynb
│
├── detections/
│   ├── phishing_suspected_sender.md
│   ├── malicious_domain_first_seen.md
│   ├── bulk_failed_logins.md
│   ├── impossible_travel.md
│   ├── anomalous_login_after_email.md
│   └── README.md
│
├── alerting/
│   ├── alert_schema.json
│   ├── severity_scoring.md
│   └── alert_gating.md
│
├── dashboards/
│   ├── executive_overview.md
│   ├── analyst_triage.md
│   └── investigation_view.md
│
├── playbooks/
│   ├── phishing_response.md
│   └── credential_compromise.md
│
├── evaluation/
│   ├── soc_metrics.md
│   └── false_positive_stress_test.ipynb
│
└── cloud_mapping/
    ├── azure_sentinel_mapping.md
    └── aws_opensearch_mapping.md
```

---

## 🧪 Evaluation Philosophy

System effectiveness is evaluated using **SOC-relevant metrics**, not ML benchmarks:

* alerts per day
* false positives per day
* analyst workload estimates
* alert stability over time
* investigation completeness

This reflects real operational constraints rather than academic performance.

---

## ☁️ Cloud Mapping

The architecture is intentionally **vendor-neutral**, with mappings provided for:

* Microsoft Sentinel (KQL-centric SIEM)
* AWS OpenSearch / Data Lake-centric pipelines

This allows the same detection and governance logic to be reasoned about across platforms.

---

## 🧠 Intended Audience

This project is designed for:

* SOC analysts and detection engineers
* security analytics engineers
* cloud security practitioners
* security architects
* interviewers evaluating real-world security thinking

It is **not** designed as a beginner tutorial or a data science demo.

---

## 🏁 Status

* Phase 1 — Schema & Contracts ✅
* Phase 2 — Ingestion & Normalization ⏳
* Phase 3 — Context & Enrichment ⏳
* Phase 4 — Detection Engineering ⏳
* Phase 5 — Alerting & Governance ⏳
* Phase 6 — Dashboards & Investigation ⏳
* Phase 7 — Evaluation & Threat Modeling ⏳

Progress is intentionally incremental and review-driven.

---

## 🔐 Final Note

This repository prioritizes **credibility over flash**.

The goal is not to impress with tools or models,
but to demonstrate how **real SOC systems are reasoned about, built, and defended**.
