# Playbook — Phishing / Suspicious Email Response

## Trigger

Alert generated from detections involving rare domains, unusual timing, or multi-signal risk associated with email events.

---

## Step 1 — Validate Email Source
- Review sender domain reputation
- Check if the domain is newly observed
- Inspect email headers if available

---

## Step 2 — Assess Scope
- Identify if multiple users received similar emails
- Check if sensitive roles (admin/executive) are targeted

---

## Step 3 — User Activity Review
- Review recent login activity for the recipient
- Check for suspicious sign-ins after the email timestamp

---

## Step 4 — Containment (if necessary)
- Temporarily restrict mailbox access if compromise suspected
- Block sender domain if confirmed malicious

---

## Step 5 — Escalation
Escalate to incident response if:
- Credentials appear compromised
- Lateral movement is suspected
- Multiple privileged accounts are involved

---

## Objective

This playbook ensures suspicious email detections are investigated systematically and consistently, reducing response time and improving containment outcomes.

