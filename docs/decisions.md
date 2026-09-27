# Decisions

## 2026-09-27 · Use `secrets`, not `random`
**Context:** passwords must be unpredictable. Python's `random` module is made for games and simulations, and its output can in principle be predicted.
**Options:** `random` · `secrets`
**Decision:** `secrets`. It is built for security and is part of the standard library.
**Consequences:** safe passwords, no extra install. Tests can't predict exact passwords, so they check properties instead (length, which characters appear).

## 2026-09-27 · Every enabled kind of character appears at least once
**Context:** many websites demand "at least one digit / uppercase letter / symbol".
**Options:** pure random choice (might miss a kind) · guarantee each enabled kind
**Decision:** guarantee it.
**Consequences:** passwords are accepted more often; the code is slightly more involved (pick one of each kind, fill the rest, then shuffle).

## 2026-09-27 · No clipboard copy
**Context:** copying automatically would save a step.
**Options:** copy automatically · print only
**Decision:** print only.
**Consequences:** standard library only, no Windows-specific code; I select and copy the password myself.
