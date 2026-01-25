# Authentication & Telemetry Schema

## Purpose
This schema represents authentication and access telemetry used to detect
credential misuse, brute force activity, and anomalous login behavior.

The design prioritizes **entity-based baselining and contextual reasoning**
over raw event volume.

---

## Event Identity

| Field | Description |
|------|-------------|
| event_type | Fixed value: `auth_event` |
| event_time | Timestamp of authentication attempt |
| event_id | Unique identifier for the log event |

---

## User Context

| Field | Description |
|------|-------------|
| user_id | Normalized user identifier |
| user_role | User privilege level (normal/admin/service) |
| authentication_result | Success or failure |

---

## Source Context

| Field | Description |
|------|-------------|
| source_ip | IP address of authentication attempt |
| geo_country | Country derived from source IP |
| geo_region | Region or ASN (if available) |
| device_type | Known / unknown device indicator |

---

## Authentication Characteristics

| Field | Description |
|------|-------------|
| auth_method | Password / MFA / token-based |
| failure_reason | Reason for failure (if applicable) |
| mfa_used | Boolean flag indicating MFA presence |

---

## Derived Security Signals

| Field | Description |
|------|-------------|
| is_new_location | Indicates login from previously unseen geography |
| is_impossible_travel | Indicates travel speed anomaly |
| failure_burst | Indicates multiple failures in short window |
| login_after_email | Indicates login occurring after suspicious email |

---

## Design Rationale
- Authentication is treated as **behavior**, not identity alone.
- Schema supports correlation with email telemetry.
- Derived signals are computed downstream, not hard-coded.

This schema enables:
- brute force detection
- credential compromise investigation
- identity-centric baselining
- cross-domain correlation

