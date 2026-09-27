# Tasks

Built from the inside out: skeleton → logic → terminal. Each phase ends with passing tests and a commit.

## Phase 1 · Skeleton
Goal: `pytest` runs, even though there is nothing to test yet.
- [x] `pyproject.toml` with project name, Python version and pytest settings
- [x] virtual environment `.venv/` with pytest installed
- [x] `password_generator/__init__.py` (empty)
- [x] `tests/` folder with one tiny test that imports the package
- [x] run `pytest` → 1 test passes
- [x] commit

## Phase 2 · Password logic (`generator.py`)
Goal: `generate_password()` works and all rules are tested. No terminal yet.
- [x] character sets as constants: `LOWERCASE`, `UPPERCASE`, `DIGITS`, `SYMBOLS`
- [x] `PasswordSettings` with the five fields and their defaults
- [x] `validate_settings(settings)` → raises `ValueError` for:
  - [x] length below 8 or above 128
  - [x] all kinds turned off
- [x] `generate_password(settings) -> str`, using `secrets`:
  - [x] correct length
  - [x] only characters from enabled kinds
  - [x] at least one of each enabled kind
  - [x] two calls give different passwords
- [x] tests in `tests/test_generator.py` for every rule above, including the edge cases (8, 128, 7, 129, only one kind on)
- [x] run `pytest` → all pass
- [x] commit

## Phase 3 · Terminal (`cli.py`, `__main__.py`)
Goal: `python -m password_generator` prints a password.
- [x] `argparse` options: `--length N`, `--no-lowercase`, `--no-uppercase`, `--no-digits`, `--no-symbols`
- [x] `main()`: build the settings, call the generator, print the password
- [x] errors: print the message, no password, exit with an error code
- [x] `__main__.py` calls `main()`
- [x] tests in `tests/test_cli.py`:
  - [x] no options → 16 characters
  - [x] `--length 20 --no-symbols` → 20 characters, no symbols
  - [x] `--length 5`, `--length abc`, all kinds off → error, no password
- [x] manual test in the terminal: default, `--length 34`, `--length 120`, `--help`, `--length 3`
- [x] optional: try one password on a real sign-up form
- [x] run `pytest` → all pass
- [x] commit

## Phase 4 · Finish
- [x] README: "Usage" section with example commands; status → Done
- [x] CLAUDE.md: how to run the app and the tests
- [x] check that all docs match the code
- [x] `docs/notes/learning-notes password_generator.md`: what went well, what I learned
- [x] commit and push

## Stretch goals (not now)
- `--count N` to print several passwords at once
- leave out look-alike characters (`0`/`O`, `l`/`1`/`I`)
- passphrases made of random words (`correct-horse-battery-staple`)
