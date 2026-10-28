# Lessons Learned

## 2026-10-27 Workflow был невалидным YAML — CI не запускался вообще
**Что произошло:** в `automerge.yml` встроенный Python в `run: |` начинался с нулевого отступа и ломал YAML. GitHub не мог разобрать файл, поэтому ни проверки, ни автомерж не работали. Плюс consistency check требовал `claude/**` в фильтре веток, которого не было — он падал бы всегда.
**Правило:** после правки workflow прогонять `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/automerge.yml'))"` и сам `scripts/check_consistency.py --root .`. Многострочный Python в `run:` — через heredoc с отступом блока.

## Формат записи
```
## [дата] [краткое название ситуации]
**Что произошло:** ...
**Правило:** ...
```
