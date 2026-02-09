# Authentication Event Schema

## Objective

Define the structure of normalized login/authentication events ingested into the SOC telemetry pipeline.

---

## Core Fields

| Field | Description |
|------|-------------|
| event_time | Timestamp of login attempt |
| user_id | Unique user identifier |
| user_role | Role of the user (admin, executive, user) |
| source_ip | IP address of login attempt |
| source_country | Country derived from IP (if available) |
| device_id | Identifier of device used (if available) |
| login_status | Success or failure |
| event_type | "authentication" |

---

## Design Principles

- Align with unified event schema used by email telemetry
- Include identity context for risk modeling
- Include location/device fields for anomaly detection
- Keep schema minimal and detection-focused

---

## Why This Matters

Authentication events are critical for detecting account compromise, lateral movement, and post-phishing exploitation. Integrating identity telemetry enables cross-signal correlation in later phases.
