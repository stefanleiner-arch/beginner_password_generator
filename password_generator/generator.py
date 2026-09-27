"""Create strong, random passwords. Pure logic: no printing, no input."""

import secrets
import string
from dataclasses import dataclass

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*-_=+?"

MIN_LENGTH = 8
MAX_LENGTH = 128


@dataclass
class PasswordSettings:
    """What kind of password to create."""

    length: int = 16
    use_lowercase: bool = True
    use_uppercase: bool = True
    use_digits: bool = True
    use_symbols: bool = True


def enabled_character_sets(settings):
    """Return the character sets that are turned on, e.g. [LOWERCASE, DIGITS]."""
    character_sets = []
    if settings.use_lowercase:
        character_sets.append(LOWERCASE)
    if settings.use_uppercase:
        character_sets.append(UPPERCASE)
    if settings.use_digits:
        character_sets.append(DIGITS)
    if settings.use_symbols:
        character_sets.append(SYMBOLS)
    return character_sets


def validate_settings(settings):
    """Raise ValueError if the settings break a rule."""
    if not MIN_LENGTH <= settings.length <= MAX_LENGTH:
        raise ValueError(
            f"Length must be between {MIN_LENGTH} and {MAX_LENGTH}, "
            f"not {settings.length}."
        )
    if not enabled_character_sets(settings):
        raise ValueError("At least one kind of character must be turned on.")


def generate_password(settings):
    """Return a random password that follows the settings."""
    validate_settings(settings)
    character_sets = enabled_character_sets(settings)
    all_characters = "".join(character_sets)

    # One character from each enabled kind, so every kind appears at least once.
    characters = [secrets.choice(chars) for chars in character_sets]

    # Fill up to the full length from all enabled kinds together.
    while len(characters) < settings.length:
        characters.append(secrets.choice(all_characters))

    # Shuffle, so the guaranteed characters aren't always at the start.
    secrets.SystemRandom().shuffle(characters)
    return "".join(characters)
