# Tasks

Built from the inside out: skeleton → logic → terminal. Each phase ends with passing tests and a commit.

## Phase 1 · Skeleton
Goal: `pytest` runs, even though there is nothing to test yet.
- [ ] `pyproject.toml` with project name, Python version and pytest settings
- [ ] virtual environment `.venv/` with pytest installed
- [ ] `password_generator/__init__.py` (empty)
- [ ] `tests/` folder with one tiny test that imports the package
- [ ] run `pytest` → 1 test passes
- [ ] commit

## Phase 2 · Password logic (`generator.py`)
Goal: `generate_password()` works and all rules are tested. No terminal yet.
- [ ] character sets as constants: `LOWERCASE`, `UPPERCASE`, `DIGITS`, `SYMBOLS`
- [ ] `PasswordSettings` with the five fields and their defaults
- [ ] `validate_settings(settings)` → raises `ValueError` for:
  - [ ] length below 8 or above 128
  - [ ] all kinds turned off
- [ ] `generate_password(settings) -> str`, using `secrets`:
  - [ ] correct length
  - [ ] only characters from enabled kinds
  - [ ] at least one of each enabled kind
  - [ ] two calls give different passwords
- [ ] tests in `tests/test_generator.py` for every rule above, including the edge cases (8, 128, 7, 129, only one kind on)
- [ ] run `pytest` → all pass
- [ ] commit

## Phase 3 · Terminal (`cli.py`, `__main__.py`)
Goal: `python -m password_generator` prints a password.
- [ ] `argparse` options: `--length N`, `--no-lowercase`, `--no-uppercase`, `--no-digits`, `--no-symbols`
- [ ] `main()`: build the settings, call the generator, print the password
- [ ] errors: print the message, no password, exit with an error code
- [ ] `__main__.py` calls `main()`
- [ ] tests in `tests/test_cli.py`:
  - [ ] no options → 16 characters
  - [ ] `--length 20 --no-symbols` → 20 characters, no symbols
  - [ ] `--length 5`, `--length abc`, all kinds off → error, no password
- [ ] manual test: run a few commands and try one password on a real sign-up form
- [ ] run `pytest` → all pass
- [ ] commit

## Phase 4 · Finish
- [ ] README: "Usage" section with example commands; status → Done
- [ ] CLAUDE.md: how to run the app and the tests
- [ ] check that all docs match the code
- [ ] `docs/notes/learning-notes.md`: what went well, what I learned
- [ ] commit and push

## Stretch goals (not now)
- `--count N` to print several passwords at once
- leave out look-alike characters (`0`/`O`, `l`/`1`/`I`)
- passphrases made of random words (`correct-horse-battery-staple`)
