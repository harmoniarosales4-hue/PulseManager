# PulseManager – Platforms & APIs

This document outlines platform-specific APIs, capabilities, and limitations.
PulseManager uses only official APIs and follows platform compliance rules.

---

## Facebook (Meta)

**API**
- Meta Graph API

**Requirements**
- Facebook Developer Account
- Facebook App
- Facebook Page

**Supported Actions**
- Page posting
- Comment reading
- Comment replies
- Engagement metrics (limited)

**Notes**
- Rate limits enforced by Meta
- Personal profiles are not supported (Pages only)

---

## Instagram (Meta)

**API**
- Meta Graph API (Instagram Business / Creator)

**Requirements**
- Instagram Business or Creator account
- Linked Facebook Page

**Supported Actions**
- Media posting
- Comment reading
- Comment replies
- Mentions

**Restrictions**
- DM automation is limited
- No personal account automation

---

## Threads (Meta)

**API**
- Meta Graph API (Threads endpoints)

**Supported Actions**
- Text posting
- Comment reading (limited)
- Engagement tracking

**Notes**
- Still evolving
- Automation must be conservative

---

## Reddit

**API**
- Reddit API (OAuth2)

**Supported Actions**
- Post submissions
- Comment replies
- Inbox message reading

**Restrictions**
- Strict rate limits
- Subreddit rules must be respected
- No spam or bulk automation

**Notes**
- Human-like pacing is mandatory

---

## TikTok

**API**
- TikTok Content Posting API

**Supported Actions**
- Video posting
- Comment reading (limited)

**Restrictions**
- DM automation not supported
- Heavy automation may trigger bans

**Notes**
- Manual-first engagement required

---

## Discord

**API**
- Discord Bot API

**Supported Actions**
- Read messages
- Send replies
- Manage channels (if permitted)

**Notes**
- Best suited for community engagement
- Bots must clearly follow server rules

---

## Global Rules
- All platforms use official APIs only
- Manual approval required for replies
- Rate limits enforced per platform
- SFW content only
