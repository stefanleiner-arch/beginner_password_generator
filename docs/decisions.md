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

## 2026-09-28 · Command-line options, not an interactive menu
**Context:** the goal is "one short command gives a password".
**Options:** command-line options (`--length 20 --no-symbols`) · interactive menu (the program asks questions one by one)
**Decision:** command-line options, read with Python's built-in `argparse`.
**Consequences:** fast once learned, and the defaults need no typing at all; `--help` lists the options. Same approach as the expense tracker.

## 2026-09-28 · pytest for tests
**Context:** tests are part of every phase. pytest is not in the standard library.
**Options:** `unittest` (built in, wordier) · `pytest` (installed, short `assert` tests)
**Decision:** pytest, installed only in this project's `.venv/`.
**Consequences:** readable tests and the same tool as the expense tracker; the finished tool itself still needs only the standard library.
