# Repository Audit — Skincare-Guide

Универсальные проверки — см. **`llm_wiki/wiki/audit-universal.md`** (canon для всех репо).

Этот файл — тонкий overlay с проектной спецификой Skincare-Guide.

---

## Контекст проекта

```
Тип: статический PWA-сайт (гид по уходу за кожей)
Стек: HTML + CSS + JavaScript, PWA (icon-192, icon-512, apple-touch-icon)
Бэкенд: нет
Внешние API: нет
CI/CD: automerge.yml (validate HTML → merge через GitHub API)
Деплой: GitHub Pages / статический хостинг
```

## Проектные проверки (в дополнение к universal)

**HTML / PWA:**
- [ ] Валидный HTML в `index.html` — проходит парсер без ошибок (validate job в `automerge.yml`)
- [ ] Нет `innerHTML` без санитизации пользовательских данных
- [ ] Внешние скрипты (если есть) — с `integrity` (SRI)
- [ ] PWA-иконки все три существуют: `icon-192.png`, `icon-512.png`, `apple-touch-icon.png`
- [ ] `manifest.json` (если есть) ссылается на реально существующие иконки

**Assets / производительность:**
- [ ] Размер изображений оптимизирован (нет 5MB PNG где хватит 100KB)
- [ ] CSS в одном файле или inline — нет 20+ маленьких `.css`
- [ ] Нет `console.log` в проде-JS

## Формат отчёта

Как в `llm_wiki/wiki/audit-universal.md`.
