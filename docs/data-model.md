# Data model

The program has one "thing": the **settings** for the password to create. The result is the password itself, which is plain text.

## PasswordSettings
| Field | Type | Default | Example | Notes |
|---|---|---|---|---|
| `length` | whole number (`int`) | `16` | `20` | allowed range: 8–128 |
| `use_lowercase` | yes/no (`bool`) | `True` | `True` | `a`–`z` |
| `use_uppercase` | yes/no (`bool`) | `True` | `True` | `A`–`Z` |
| `use_digits` | yes/no (`bool`) | `True` | `False` | `0`–`9` |
| `use_symbols` | yes/no (`bool`) | `True` | `False` | `!@#$%^&*-_=+?` |

Example: `length=20, use_digits=False, use_symbols=False` gives something like `qWbTzkRmPaLxUvNcHsYe`.

### Validation rules
- `length` is a whole number from 8 to 128.
- At least one of the four `use_…` fields is `True`.
- Invalid settings produce a clear error and no password.

## Character sets
Fixed values that never change while the program runs:

| Kind | Characters | Count |
|---|---|---|
| lowercase | `abcdefghijklmnopqrstuvwxyz` | 26 |
| uppercase | `ABCDEFGHIJKLMNOPQRSTUVWXYZ` | 26 |
| digits | `0123456789` | 10 |
| symbols | `!@#$%^&*-_=+?` | 13 |

## Result
The password is a text (`str`) of exactly `length` characters. It:
- contains only characters from the enabled kinds
- contains at least one character of each enabled kind

## Storage
None. Nothing is saved to a file, and passwords are never written anywhere except the terminal. This is on purpose: a password tool that keeps copies of passwords is a security risk.

## Edge cases
| Situation | Behaviour |
|---|---|
| No settings given | 16 characters, all four kinds |
| `length` = 8 or 128 | allowed (the limits are included) |
| `length` = 7 or 129 | error |
| Only one kind enabled | allowed; the password uses only that kind |
| All kinds disabled | error |
