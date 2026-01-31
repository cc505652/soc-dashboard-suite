# Detection: Suspicious Sender Domain

## Detection ID
DET_01_SUSPICIOUS_SENDER_DOMAIN

## Objective
Identify emails originating from rare or first-seen external domains,
which may indicate phishing or newly introduced attacker infrastructure.

## Logic
Trigger when:
- sender_domain is classified as "rare"
  OR
- domain is observed for the first time
AND
- sender is external to the organization

## Severity Logic
Severity is influenced by recipient identity:
- admin → high
- executive → high
- normal → medium

## False Positive Risks
- Legitimate first-time vendors
- New business partners
- Marketing platforms using rotating domains

## Tuning Knobs
- Adjust rarity threshold
- Require additional signals (e.g., off-hours activity)
- Suppress known safe domains

## Analyst Response Guidance
- Inspect domain reputation
- Review email content for phishing indicators
- Check for follow-up authentication anomalies
