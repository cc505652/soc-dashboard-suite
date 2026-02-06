# SOC System Overview

## Objective

The SOC Dashboard Suite models a realistic Security Operations Center (SOC) detection and monitoring pipeline. The system demonstrates how raw telemetry is transformed into actionable, prioritized alerts for security analysts while minimizing noise and preserving explainability.

This project emphasizes detection engineering discipline, context enrichment, and operational usability over raw model accuracy.

---

## System Purpose

The system is designed to answer three core SOC questions:

1. **What is happening?**  
   (Telemetry ingestion and normalization)

2. **Is it risky?**  
   (Context enrichment and detection logic)

3. **What should analysts look at first?**  
   (Alert correlation, scoring, and prioritization)

---

## High-Level Data Flow

**Email Telemetry → Normalization → Context Enrichment → Detection Rules → Alert Correlation → Risk Scoring → Dashboard Analytics**

### 1. Ingestion
Raw email data is ingested and transformed into a structured event format aligned with a unified schema. This ensures downstream detection logic operates on consistent, clean telemetry.

### 2. Enrichment Layers
Detection quality is improved through layered contextual enrichment:

- **Domain Context** — rarity and first-seen tracking  
- **Identity Context** — user role sensitivity (admin, executive, user)  
- **Temporal Context** — off-hours and unusual activity detection  

These layers convert raw events into **security-relevant signals**.

### 3. Detection Engineering
Detection rules are intentionally explainable and context-driven. Rather than relying on single features, detections combine:

- Identity sensitivity  
- Behavioral anomalies  
- Domain reputation or novelty  

This reduces false positives and mirrors real SOC detection practices.

### 4. Alert Correlation
Multiple detections can trigger on the same event. Alerts are merged into a unified stream to prevent duplicate analyst workload and to capture multi-signal risk convergence.

### 5. Risk Scoring & Prioritization
Alerts are assigned risk scores based on:

- Severity of triggered detections  
- Number of contributing rules  
- Contextual risk signals  

This produces SOC-style priority levels (P1–P4), allowing analysts to focus on high-impact threats first.

### 6. Dashboard Analytics
Aggregated metrics power a SOC dashboard that provides:

- Alert volume trends  
- Severity distribution  
- Detection rule effectiveness  
- Exposure of sensitive user roles  
- High-risk domains  

The dashboard supports operational monitoring, not just visualization.

---

## Design Principles

- **Explainability over black-box models**
- **Context before classification**
- **Analyst workload reduction**
- **Separation of detection logic and visualization**
- **Architecture-first thinking**

---

## Why This Matters

The system demonstrates how detection engineering integrates with SOC operations, bridging the gap between raw telemetry and analyst decision-making. It reflects real-world constraints such as alert fatigue, false positives, and operational prioritization.
