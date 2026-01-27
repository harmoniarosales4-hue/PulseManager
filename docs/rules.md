# PulseManager – Safety & Moderation Rules

This document defines global safety rules, moderation logic, and rate limits.
These rules apply across all platforms.

---

## Content Safety (SFW)

PulseManager operates strictly as Safe-For-Work (SFW).

### Disallowed Content
- Explicit sexual content
- Nudity or pornographic language
- Escorting or adult services
- Personal phone numbers or emails
- Financial promises or guarantees
- Hate speech or harassment

Any detected disallowed content must be ignored or flagged.

---

## Reply Rules

- No automated replies without manual approval
- Replies must follow the defined persona
- Arguments, hostility, or debates are avoided
- When in doubt, do not reply

---

## Moderation Logic

Incoming messages are classified as:
- Valid (can reply)
- Neutral (optional reply)
- Spam (ignore)
- NSFW (ignore + flag)

Only “Valid” messages generate reply drafts.

---

## Rate Limits (Initial)

These limits are conservative and may be adjusted later.

### Meta (Facebook / Instagram / Threads)
- Max 20 replies per hour per account
- Cooldown: 2–3 minutes between replies

### Reddit
- Max 10 replies per hour per account
- Cooldown: 5–10 minutes between replies

### TikTok
- Max 5 replies per hour
- Posting only, minimal engagement

### Discord
- Max 30 messages per hour per server
- Follow server-specific rules

---

## Escalation Rules

- Repeated spam → ignore
- Aggressive users → ignore
- Rule violations → log only, no reply

---

## Automation Policy

Automation increases only after:
- Stable account health
- No warnings or restrictions
- Consistent manual approval history

PulseManager prioritizes account longevity over speed.
