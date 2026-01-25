# Email Telemetry Schema

## Purpose
This schema defines the normalized representation of email telemetry used for security monitoring.
The goal is not full email reconstruction, but extraction of **security-relevant signals**
that support phishing detection, campaign analysis, and incident investigation.

This schema is intentionally minimal and explainable to support SOC workflows.

---

## Event Identity
Each email is treated as a discrete security event.

| Field | Description |
|------|-------------|
| event_type | Fixed value: `email_event` |
| event_time | Timestamp when the email was received |
| message_id | Unique email message identifier |

---

## Sender Context

| Field | Description |
|------|-------------|
| sender_email | Full sender email address |
| sender_domain | Domain extracted from sender_email |
| sender_display_name | Display name used by sender (if present) |
| sender_ip | IP address of sending mail server |

---

## Authentication Signals

| Field | Description |
|------|-------------|
| spf_result | SPF evaluation result (pass/fail/softfail/neutral) |
| dkim_result | DKIM verification result |
| dmarc_result | DMARC alignment result |

---

## Recipient Context

| Field | Description |
|------|-------------|
| recipient_email | Recipient email address |
| recipient_domain | Recipient domain |
| recipient_user_type | User classification (e.g., normal, admin, executive) |

---

## Content Indicators (Metadata Only)

| Field | Description |
|------|-------------|
| subject | Email subject line |
| has_attachment | Boolean flag indicating attachment presence |
| attachment_type | File extension or MIME type (if present) |
| has_url | Boolean flag indicating presence of URLs |
| url_domains | Extracted domains from embedded URLs |

---

## Derived Security Signals

| Field | Description |
|------|-------------|
| first_seen_sender | Boolean indicating sender not previously observed |
| first_seen_domain | Boolean indicating domain not previously observed |
| external_sender | Boolean indicating sender is external |
| suspicious_auth_combo | Boolean flag for SPF/DKIM/DMARC mismatch patterns |

---

## Design Rationale
- Content body is intentionally excluded to avoid payload-level inspection complexity.
- Schema focuses on **identity, provenance, and trust indicators**.
- Fields are chosen to support explainable alerting rather than black-box scoring.

This schema enables:
- phishing detection
- sender reputation tracking
- campaign correlation
- analyst investigation context

