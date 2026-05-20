# Project Context

> Skincare-Guide — PWA-гид по уходу за кожей. Статический сайт без бэкенда.

---

## 1. Tech Stack
- Frontend: HTML + CSS + JS (без фреймворков), PWA (manifest, иконки)
- Animations: CSS transitions
- Backend: none
- DB & Auth: none
- Design System: none

---

## 2. Infrastructure & CI/CD
- Frontend deploy: GitHub Pages / ручной
- Repo: github.com/Arsid0305/Skincare-Guide

Workflows:
- `automerge.yml` — `claude/** | cursor/**` → `main` авто ✅
- `promote.yml` — удалён ❌
- `deploy.yml` — не используется ❌

---

## 3. AI Environment

| Tool | Status | Note |
|------|--------|------|
| Node.js / npm | ❌ | не используется |
| Python | ❌ | не используется |
| Supabase CLI | ❌ | нет |
| .env (real keys) | ❌ | нет секретов |

---

## 4. Design System

Не используется. Весь UI — в `index.html`.

---

## 5. Project Structure

```
.github/workflows/
  automerge.yml        — авто-мерж ветки в main
docs/
  AUDIT_PROMPT.md      — контекст для аудита
scripts/
  check_consistency.py — CI-проверки консистентности
tasks/
  todo.md              — активные задачи
  lessons.md           — уроки из ошибок
index.html             — SSOT: весь контент и логика
apple-touch-icon.png
icon-192.png
icon-512.png
```

---

## 6. Standard Packages

Зависимостей нет — чистый HTML/CSS/JS.

---

## 7. Auth (Supabase OTP)

Не используется — нет Supabase.

---

## 8. Open Bugs

_(empty)_
