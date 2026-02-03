# Detection: Multi-Signal Email Risk

## Detection ID
DET_03_MULTI_SIGNAL_EMAIL_RISK

## Objective
Detect high-confidence phishing or targeted intrusion attempts by correlating
multiple contextual risk factors in a single email event.

## Logic
Trigger when ALL conditions are true:
- Sender domain is rare OR first-seen
- Email occurs during off-hours OR unusual user activity time
- Recipient role is admin OR executive
- Sender is external

## Severity Logic
All alerts are marked critical due to multi-signal convergence.

## False Positive Risks
- Newly onboarded vendor communicating after hours
- Executive travel across time zones
- Emergency off-hours communications

## Tuning Knobs
- Require domain rarity only (exclude first-seen if noisy)
- Require off-hours only (exclude unusual-hour if noisy)
- Exclude known safe domains
- Add email volume or campaign pattern checks

## Analyst Response Guidance
- Immediately validate sender authenticity
- Check for similar emails sent to other privileged users
- Review recent authentication or endpoint activity for recipient
- Consider temporary mailbox isolation if phishing suspected
