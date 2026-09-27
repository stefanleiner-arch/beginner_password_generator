# Learning notes: password generator

*Draft written by Claude from our session. Edit it into my own words.*

## What went well
- **Planning before code, in the order from my guide.** Goals → requirements → data model → architecture → decisions → tasks. Every doc was short, and each one answered the questions the next one needed.
- **No surprises while coding.** All the real choices (length 8–128, the symbol set, `secrets`, at least one of each kind, options instead of a menu) were already made. Phases 2 and 3 were mostly "turn the docs into code".
- **Requirements became tests almost word for word.** "Length 7 → error" became `test_length_outside_8_to_128_is_rejected[7]`.
- **Inside out worked.** The logic was fully tested before the terminal part existed.

## What surprised me
- **Testing something random.** You can't check for an exact password, so tests check *properties* (length, allowed characters, each kind present) and repeat 200 times so a bug can't pass by luck.
- **Testing the tests.** Claude broke the "one of each kind" rule on purpose: the right test failed. A test that never fails proves nothing.
- **Claude makes mistakes too.** Twice a quick edit ticked or unticked the wrong boxes in `tasks.md`. It was caught by checking the result. Lesson: look at what changed (`git diff`, `git status`), no matter who made the change.
- **The chat isn't a private terminal.** Output of `!` commands lands in the conversation. Real passwords should be generated in my own terminal.
- **`&amp;` in the output** wasn't from my program; the chat display changed `&` for web display.

## Concepts
| Concept | In one line |
|---|---|
| `secrets` vs `random` | `random` is for games and can be predicted; `secrets` is for security. |
| Virtual environment (`.venv`) | A private Python setup for one project; installs don't touch the rest of the computer. |
| `pyproject.toml` | The project's settings file (name, Python version, pytest settings). |
| Dataclass | A short way to write a class that mainly holds values, like `PasswordSettings`. |
| `argparse` | Python's built-in tool for command-line options; builds `--help` automatically. |
| stdout vs stderr | Two output channels: normal output (the password) and errors. Kept separate so an error is never mistaken for a password. |
| Exit code | A number a program returns when it ends: 0 = success, anything else = error (ours: 2). |
| `@pytest.mark.parametrize` | Run the same test once per value, e.g. lengths 7, 129, 0 and -5. |
| Core vs edges | Pure logic (`generator.py`) in the middle, terminal (`cli.py`) at the edge. The core is easy to test. |

## Git commands I used
| Command | What it does |
|---|---|
| `git init -b main` | Turn a folder into a repository. |
| `git status` | What's changed, staged, or untracked. |
| `git add <files>` / `git add .` | Stage specific files / everything that changed. Check `git status` first when using `.`. |
| `git commit -m "…"` | Save a snapshot locally. |
| `git remote add origin <url>` | Connect to GitHub. No upload yet. |
| `git push -u origin main` | First upload; `-u` remembers the link so later a plain `git push` is enough. |
| `git log --oneline` | Short history, one line per commit. |

Things I learned about the output:
- `root-commit` = the very first commit.
- A changed line counts as one deletion plus one insertion.
- "LF will be replaced by CRLF" is a harmless line-ending warning on Windows.
- Git commands that succeed often print nothing.

## Open ends
- Try a generated password on a real sign-up form.
- Maybe: a friendlier message for `--length abc` (now: "invalid int value").
- Maybe: a `.gitattributes` file to stop the line-ending warnings.
- Stretch goals in `tasks.md`: `--count`, no look-alike characters, passphrases.
