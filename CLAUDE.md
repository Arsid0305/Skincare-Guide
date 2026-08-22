# Claude Adapter — Skincare-Guide

> Тонкий адаптер. Универсальные правила экосистемы — в `docs/rules/core/*.md` (синкается из AI_OS SSOT).
> Специфика проекта — в `docs/rules/scoped/skincare-guide-specific.md`.
> Читай этот файл и `tasks/lessons.md` в начале каждого чата. В конце — обновляй «Открытые баги» и `tasks/lessons.md`.

---

## ⛔ ГЛАВНОЕ ПРАВИЛО

Никаких изменений без явного согласования с пользователем.
Заметил баг или улучшение — сообщи и жди разрешения. Не трогай.

**Исключение:** баг внутри уже согласованного скоупа задачи — чини сам, сообщи после.

---

## LLM_Wiki — контекст экосистемы

В начале каждой сессии прочитать из `arsid0305/llm_wiki` (main):
- `wiki/lessons.md`, `wiki/decisions.md` — кросс-проектные уроки и решения
- `wiki/rules-architecture.md` — canon rules-архитектуры (если ещё не читал)

---

## Каноны (rules как атомы)

Универсальные правила — в `docs/rules/core/*.md` (SSOT в AI_OS, синкается автоматически):

- Начало / конец сессии — [`docs/rules/core/session-lifecycle.md`](docs/rules/core/session-lifecycle.md)
- Стиль общения / краткость — [`docs/rules/core/communication-style.md`](docs/rules/core/communication-style.md)
- Git flow, запрет флагов — [`docs/rules/core/git-flow.md`](docs/rules/core/git-flow.md)
- GitHub anti-abuse — [`docs/rules/core/github-anti-abuse.md`](docs/rules/core/github-anti-abuse.md)
- BIG / SMALL — [`docs/rules/core/task-classification.md`](docs/rules/core/task-classification.md)
- Принципы работы с кодом — [`docs/rules/core/code-principles.md`](docs/rules/core/code-principles.md)
- Subagents — [`docs/rules/core/subagents.md`](docs/rules/core/subagents.md)
- Audit-триггер — [`docs/rules/core/audit-trigger.md`](docs/rules/core/audit-trigger.md)
- Context Mode — `llm_wiki/wiki/context-mode.md`
- Выбор модели `haiku`/`sonnet`/`opus` — `llm_wiki/wiki/workflow.md`

**Специфика Skincare-Guide** (scoped): [`docs/rules/scoped/skincare-guide-specific.md`](docs/rules/scoped/skincare-guide-specific.md) — HTML/JS review, безопасность (XSS/SRI), стек, среда.

Архитектура rules и правила синка — [`docs/rules/README.md`](docs/rules/README.md).

---

## TEMPLATE репо — автодоступ

```bash
git clone https://github.com/Arsid0305/TEMPLATE /tmp/arsid-template
```

---

## Task Management

- `tasks/todo.md` — план с чекбоксами до начала любой BIG задачи. Отмечать выполненное по ходу.
- `tasks/lessons.md` — паттерны ошибок (формат — в [`docs/rules/core/session-lifecycle.md`](docs/rules/core/session-lifecycle.md) §«Формат lessons.md»).

## Предложение улучшений в стандарт

Если в проекте появился новый паттерн лучше существующего:
1. Не применять молча — сначала предложить пользователю
2. Описать: что это, почему лучше, какой трейдофф
3. Ждать решения: принять в стандарт / использовать только в этом проекте / отклонить
4. После одобрения — внести в `~/.claude/CLAUDE.md` (или в `docs/rules/core/*.md` через AI_OS SSOT)

---

## Инфраструктура

- Репо: github.com/Arsid0305/Skincare-Guide
- Тип: статический HTML-проект (PWA)
- Деплой: GitHub Pages или прямой хостинг
- Workflows: `automerge.yml` — PR из `claude/...` или `cursor/...` → validate → автомерж в `main` через GitHub API (squash)

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
Ветка `claude/...` → PR в `main` (не draft) → validate → `automerge.yml` через GitHub API (squash). Никогда не пушить в `main` напрямую.

---

## Открытые баги

_(пусто)_
