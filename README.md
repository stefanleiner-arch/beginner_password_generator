# Password Generator

A small command-line tool that creates strong, random passwords for me when I sign up for websites. A learning project.

## Goals
- Get a strong, random password with one short command.
- Choose the length of the password.
- Choose which kinds of characters to use (letters, numbers, symbols), because some websites don't accept all of them.

**Success looks like:** I type one command, get a password, and paste it into a sign-up form.

## Non-goals
- Storing or remembering passwords. It is not a password manager.
- Checking how strong an existing password is.
- Copying the password to the clipboard automatically. I copy it from the terminal myself.
- A graphical window or website. The terminal is enough.
- Syncing between devices, or accounts for other people.

## Requirements
- [ ] Generate a password
  - one command prints one password and nothing else
  - by default: 16 characters, using lowercase letters, uppercase letters, digits and symbols
  - running it twice gives two different passwords
  - uses a secure random source (Python's `secrets` module, not `random`)
- [ ] Choose the length
  - any whole number from 8 to 128
  - below 8 or above 128 → clear error, no password
  - not a whole number (`abc`, `12.5`) → clear error, no password
- [ ] Choose the kinds of characters
  - each kind can be turned off: lowercase, uppercase, digits, symbols
  - a turned-off kind never appears in the password
  - every kind that is on appears at least once (many websites require this)
  - all kinds turned off → clear error, no password
- [ ] Symbols
  - the symbol set is `!@#$%^&*-_=+?`
  - no quotes, spaces or backslashes, because some websites reject them or they cause trouble when pasting

## Status
Planning
