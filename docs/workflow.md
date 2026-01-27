# PulseManager – Workflow

This document defines the daily operational workflow for PulseManager.
The system is manual-first and human-in-the-loop.

---

## Daily Flow

### 1. Content Preparation
- User prepares post content manually.
- Select target platform(s).
- Content is queued as a draft.

---

### 2. Posting (Assisted)
- Posts are reviewed before scheduling.
- Platform-specific formatting is applied.
- Posts are published via official APIs.

---

### 3. Inbox Review
- System fetches comments, mentions, and messages.
- All incoming items appear in a unified inbox.
- Each item is marked as:
  - Pending
  - Ignored
  - Replied

---

### 4. Reply Drafting
- System generates a reply draft using the defined persona.
- Drafts respect platform tone and safety rules.

---

### 5. Manual Approval
- User reviews each draft.
- User may edit, approve, or discard.
- Only approved replies are sent.

---

## Safety Rules
- No automated replies without approval.
- Rate limits enforced per platform.
- NSFW and spam content are ignored.

---

## Scaling Rule
Automation is increased only after consistent safe behavior
and platform compliance is confirmed.
