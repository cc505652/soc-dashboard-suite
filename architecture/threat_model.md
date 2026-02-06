# Threat Model — SOC Detection System

## Objective

This document outlines how an adversary might attempt to evade or degrade the SOC detection pipeline and the architectural controls designed to mitigate those risks.

---

## Assets to Protect

- Detection logic and rule integrity  
- Enrichment baselines (domain, identity, behavior)  
- Alert prioritization pipeline  
- Analyst visibility and trust in alerts  

---

## Potential Adversary Goals

### 1. Detection Evasion
Attackers may attempt to blend into normal activity by:
- Using legitimate domains or compromised accounts
- Operating within normal business hours
- Mimicking typical user behavior

**Mitigation:** Multi-signal detection combining identity, domain, and temporal context.

---

### 2. Baseline Poisoning
An attacker could slowly introduce malicious behavior to influence rarity or behavioral baselines.

**Mitigation:**  
- Use of first-seen logic alongside historical rarity  
- Context layers separated from detection logic to avoid silent drift  
- Emphasis on identity sensitivity, not only behavioral norms

---

### 3. Alert Flooding (SOC DoS)
Attackers may generate large volumes of low-quality alerts to overwhelm analysts.

**Mitigation:**  
- Risk scoring and prioritization (P1–P4)  
- Alert gating to suppress low-value signals  
- Multi-signal requirement for high-severity alerts

---

### 4. Signal Suppression
If telemetry is incomplete or delayed, detection coverage weakens.

**Mitigation:**  
- Layered detection logic that does not rely on a single signal  
- Clear separation between ingestion and detection components

---

## Architectural Defenses

| Risk | Defense |
|------|---------|
| Evasion via normal-looking activity | Context layering (identity + time + domain) |
| Alert overload | Scoring and gating mechanisms |
| Baseline manipulation | Multi-factor risk modeling |
| Over-reliance on a single signal | Correlated detections |

---

## Conclusion

The detection system is designed under the assumption that attackers will attempt to hide within normal activity. Therefore, the architecture prioritizes contextual reasoning, signal correlation, and operational safeguards rather than relying on simplistic thresholds.
