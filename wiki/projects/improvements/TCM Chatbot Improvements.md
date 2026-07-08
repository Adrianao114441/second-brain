---
title: TCM Chatbot Improvements
type: improvements
last-updated: 2026-07-06
---

# TCM Chatbot Improvements

Suggested improvements for [[TCM Chatbot]]. These are agent suggestions, not commitments; move an item into `priorities.md` when Adrian decides to act on it.

## Knowledge Gaps

- The project page documents the frontend and deployment but not the backend: record where the TCM knowledge comes from (LLM, database, or static content) and how `route.ts` serves it.
- Record the live deployment URL and whether the Vercel deployment is still up.
- Confirm the status: the page says "active or completed".

## Technical

- Keep the GitHub Actions lint and Playwright workflows green; a failing CI on a dormant project hides real regressions if the project is revived.
- Review the custom auth setup (`auth.config.ts`, `auth.ts`): custom authentication is the highest risk part of the stack and worth a security pass if the app is public.
