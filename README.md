# Skincare Guide

Статический HTML-проект (PWA-совместимый) по уходу за кожей.

## С чего начать

| Я хочу… | Открыть |
|---------|---------|
| Понять правила работы ИИ в репо | [CLAUDE.md](CLAUDE.md) |
| Увидеть текущие задачи | [tasks/todo.md](tasks/todo.md) |
| Посмотреть накопленные уроки | [tasks/lessons.md](tasks/lessons.md) |
| Запустить аудит репо | [docs/AUDIT_PROMPT.md](docs/AUDIT_PROMPT.md) |

## Стек

- HTML + CSS + JavaScript (без фреймворков)
- PWA: `icon-192.png`, `icon-512.png`, `apple-touch-icon.png`
- Автомерж: `.github/workflows/automerge.yml`

## Структура

```
index.html            — точка входа
docs/                 — документация проекта
scripts/              — вспомогательные скрипты (check_consistency.py и т.д.)
tasks/                — todo/lessons
```

## Инфраструктура

- Репо: `github.com/Arsid0305/Skincare-Guide`
- Деплой: статический хостинг / GitHub Pages
- CI: `automerge.yml` — валидация + автомерж `claude/*` PR через GitHub API
- 
Pages restart: 17.08.2026
