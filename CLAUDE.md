# Claude Adapter — Skincare-Guide

> Тонкий адаптер. Универсальные правила экосистемы — в `AI_OS/docs/rules/core/*.md` (SSOT, копий в этом репо нет).
> Специфика проекта — в `docs/rules/scoped/skincare-guide-specific.md`.
> Читай этот файл и `tasks/lessons.md` в начале каждого чата. В конце — обновляй «Открытые баги» и `tasks/lessons.md`.

---

## ⛔ ГЛАВНОЕ ПРАВИЛО

Внутри согласованной задачи — работать без остановок, баги в её скоупе чинить сам, сообщать после.
Заметил баг или улучшение вне задачи — не трогать: записать в блок «Нужно от вас» и продолжать работу. Разбираем вместе с владелицей.

Канон — `AI_OS/docs/rules/core/communication-style.md` §«Доводить до конца» (решение владелицы, 2026-10-08).

---

## LLM_Wiki — контекст экосистемы

В начале каждой сессии прочитать из `arsid0305/llm_wiki` (main):
- `wiki/lessons.md`, `wiki/decisions.md` — кросс-проектные уроки и решения
- `wiki/rules-architecture.md` — canon rules-архитектуры (если ещё не читал)

---

## Каноны (rules как атомы)

Универсальные правила — в `AI_OS/docs/rules/core/*.md` (SSOT, копий в этом репо нет). Если AI_OS не подключён к сессии — попросить подключить, по памяти не работать:

- Начало / конец сессии — [`AI_OS/docs/rules/core/session-lifecycle.md`](https://github.com/Arsid0305/AI_OS/blob/main/docs/rules/core/session-lifecycle.md)
- Стиль общения / краткость — [`AI_OS/docs/rules/core/communication-style.md`](https://github.com/Arsid0305/AI_OS/blob/main/docs/rules/core/communication-style.md)
- Git flow, запрет флагов — [`AI_OS/docs/rules/core/git-flow.md`](https://github.com/Arsid0305/AI_OS/blob/main/docs/rules/core/git-flow.md)
- GitHub anti-abuse — [`AI_OS/docs/rules/core/github-anti-abuse.md`](https://github.com/Arsid0305/AI_OS/blob/main/docs/rules/core/github-anti-abuse.md)
- BIG / SMALL — [`AI_OS/docs/rules/core/task-classification.md`](https://github.com/Arsid0305/AI_OS/blob/main/docs/rules/core/task-classification.md)
- Принципы работы с кодом — [`AI_OS/docs/rules/core/code-principles.md`](https://github.com/Arsid0305/AI_OS/blob/main/docs/rules/core/code-principles.md)
- Subagents — [`AI_OS/docs/rules/core/subagents.md`](https://github.com/Arsid0305/AI_OS/blob/main/docs/rules/core/subagents.md)
- Audit-триггер — [`AI_OS/docs/rules/core/audit-trigger.md`](https://github.com/Arsid0305/AI_OS/blob/main/docs/rules/core/audit-trigger.md)
- Разрешения веб-сессий — [`AI_OS/docs/rules/core/web-permissions.md`](https://github.com/Arsid0305/AI_OS/blob/main/docs/rules/core/web-permissions.md)
- Context Mode — `llm_wiki/wiki/context-mode.md`
- Выбор модели `haiku`/`sonnet`/`opus` — `llm_wiki/wiki/workflow.md`

**Специфика Skincare-Guide** (scoped): [`docs/rules/scoped/skincare-guide-specific.md`](docs/rules/scoped/skincare-guide-specific.md) — HTML/JS review, безопасность (XSS/SRI), стек, среда.

Архитектура rules — [`AI_OS/docs/rules/README.md`](https://github.com/Arsid0305/AI_OS/blob/main/docs/rules/README.md).

---

## TEMPLATE репо — автодоступ

```bash
git clone https://github.com/Arsid0305/TEMPLATE /tmp/arsid-template
```

---

## Task Management

- `tasks/todo.md` — план с чекбоксами до начала любой BIG задачи. Отмечать выполненное по ходу.
- `tasks/lessons.md` — паттерны ошибок (формат — в [`AI_OS/docs/rules/core/session-lifecycle.md`](https://github.com/Arsid0305/AI_OS/blob/main/docs/rules/core/session-lifecycle.md) §«Формат lessons.md»).

## Предложение улучшений в стандарт

Если в проекте появился новый паттерн лучше существующего:
1. Не применять молча — сначала предложить пользователю
2. Описать: что это, почему лучше, какой трейдофф
3. Ждать решения: принять в стандарт / использовать только в этом проекте / отклонить
4. После одобрения — внести в `~/.claude/CLAUDE.md` (или в `AI_OS/docs/rules/core/*.md`, SSOT)

---

## Инфраструктура

_Проверено: 2026-08-19._

- Репо: github.com/Arsid0305/Skincare-Guide
- Тип: статический HTML-проект (PWA)
- Деплой: GitHub Pages или прямой хостинг (проверить: где реально живёт прод на дату проверки)
- Workflows:
  - `automerge.yml` (имя историческое) — только CI: PR из `claude/...` или `cursor/...` → validate (consistency check + HTML). Автомержа нет (удалён 2026-10-27) — PR мержит владелица кнопкой, мерж через API запрещён (`AI_OS/docs/rules/core/github-anti-abuse.md`).

## Структура

```
.github/workflows/automerge.yml
.gitignore
CLAUDE.md
README.md
tasks/{todo.md,lessons.md}
docs/{AUDIT_PROMPT.md, rules/}
scripts/check_consistency.py
index.html
```

## Рабочий процесс
Ветка `claude/...` → PR в `main` (не draft) → validate. Автомержа нет — мержит владелица кнопкой. Никогда не пушить в `main` напрямую.

---

## Открытые баги

- 2026-10-26: `scripts/check_consistency.py` падает на `main`: ищет `claude/**` и `cursor/**` в `automerge.yml`, а workflow фильтрует через `startsWith(github.head_ref, ...)`. Шаг validate в CI красный на любом PR. Не чинится без решения владелицы (вне задачи).
