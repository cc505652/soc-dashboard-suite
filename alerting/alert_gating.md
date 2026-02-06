# Alert Gating Strategy

## Objective

Alert gating ensures that the SOC only surfaces alerts that are meaningful, reducing analyst fatigue while preserving detection coverage.

---

## Why Alert Gating Is Necessary

Raw detections often produce noisy outputs. Without prioritization and gating:

- Analysts are overwhelmed
- Important signals are buried
- Trust in detection systems decreases

Alert gating transforms raw detections into a manageable operational queue.

---

## Gating Principles

1. **Severity-Based Prioritization**  
   Alerts are assigned P1–P4 levels based on contextual risk.

2. **Multi-Signal Promotion**  
   Alerts triggered by multiple independent detections are elevated in priority.

3. **Contextual Risk Weighting**  
   Additional risk signals (rare domain, off-hours activity, first-seen sender) increase alert urgency.

4. **Low-Risk Suppression**  
   Alerts with minimal context or weak signals are deprioritized.

---

## Resulting Alert Flow

| Priority | Description |
|----------|-------------|
| **P1** | Multi-signal, high-confidence threat |
| **P2** | Strong contextual risk |
| **P3** | Moderate anomaly |
| **P4** | Low-priority monitoring |

---

## Operational Impact

Alert gating ensures analysts spend time on high-confidence threats first while still retaining lower-priority visibility for trend monitoring.

This approach reflects real SOC operations where alert volume must be controlled to maintain effectiveness.

