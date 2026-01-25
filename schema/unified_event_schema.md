# Unified SOC Event Schema

## Purpose
The unified event schema enables correlation across disparate telemetry sources
(email, authentication, endpoint, network) by enforcing a consistent structure.

This abstraction allows detections to operate on **security meaning**
instead of raw log formats.

---

## Core Fields (Present in All Events)

| Field | Description |
|------|-------------|
| event_type | High-level category (email_event, auth_event) |
| event_time | Timestamp of occurrence |
| entity_id | Primary entity (user, account, or domain) |
| source | Original telemetry source |
| confidence | Confidence score assigned post-detection |

---

## Context Fields

| Field | Description |
|------|-------------|
| identity_context | User role, privilege level |
| asset_context | Criticality of affected system |
| temporal_context | Business hours vs off-hours |
| baseline_context | Deviation from historical behavior |

---

## Detection Metadata

| Field | Description |
|------|-------------|
| detection_id | Identifier of detection logic |
| severity | Assigned alert severity |
| alert_reason | Human-readable explanation |
| contributing_signals | List of signals that triggered alert |

---

## Investigation Support Fields

| Field | Description |
|------|-------------|
| related_events | Linked events across telemetry types |
| evidence_summary | Key fields supporting alert |
| recommended_action | Suggested analyst response |

---

## Design Rationale
- Schema is **event-centric**, not log-centric.
- Correlation occurs at the semantic layer.
- Alert explanations are first-class fields.

This schema enables:
- multi-stage attack correlation
- explainable alerts
- analyst-friendly investigation workflows

