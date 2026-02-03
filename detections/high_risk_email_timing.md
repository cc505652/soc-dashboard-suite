# Detection: High-Risk Email Timing

## Detection ID
DET_02_HIGH_RISK_EMAIL_TIMING

## Objective
Detect emails delivered to privileged or sensitive users during unusual or off-hours periods.

## Logic
Trigger when:
- recipient role is admin or executive
AND
- time_behavior is off_hours or unusual_hour

## Severity Logic
All alerts are high severity due to identity sensitivity.

## False Positive Risks
- Executives working across time zones
- After-hours legitimate work
- Automated system-generated emails

## Tuning Knobs
- Restrict to external senders only
- Require domain rarity as additional signal
- Exclude known bulk/internal domains

## Analyst Response Guidance
- Validate sender legitimacy
- Check for similar emails to other privileged users
- Review recent login or authentication activity
