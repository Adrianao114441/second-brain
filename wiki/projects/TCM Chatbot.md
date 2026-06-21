---
title: TCM Chatbot
type: project
last-updated: 2026-06-21
---

# TCM Chatbot

TCM Chatbot is a Traditional Chinese Medicine chatbot built as a full-stack web application. It is deployed on Vercel and uses Next.js with TypeScript on the frontend.

## Architecture

- **Frontend:** Next.js, TypeScript, React.
- **Styling:** Tailwind CSS (`globals.css`).
- **Authentication:** Custom auth setup via `auth.config.ts` and `auth.ts`.
- **Deployment:** Vercel (`vercel.json`, `vercel-template.json`).
- **Containerisation:** Docker Compose for local development.
- **Testing:** Playwright for end-to-end tests; CI via GitHub Actions (lint and Playwright workflows).

## Key Files

- `next.config.ts`, `package.json`, `tsconfig.json` — project configuration.
- `auth.config.ts`, `auth.ts`, `route.ts` — authentication.
- `docker-compose.yml` — local containerised environment.
- `playwright.config.ts` — E2E test configuration.
- `CLAUDE.md` — project-level Claude Code instructions.

## Status

Active or completed. Deployment-ready with CI configured.
