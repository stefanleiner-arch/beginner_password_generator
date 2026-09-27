import pytest

from password_generator.generator import (
    DIGITS,
    LOWERCASE,
    SYMBOLS,
    UPPERCASE,
    PasswordSettings,
    generate_password,
    validate_settings,
)

# Passwords are random, so rules about their content are checked many times.
REPEATS = 200


# --- Character sets ---

def test_character_sets_have_the_expected_sizes():
    assert len(LOWERCASE) == 26
    assert len(UPPERCASE) == 26
    assert len(DIGITS) == 10
    assert len(SYMBOLS) == 13


def test_symbols_are_exactly_the_agreed_set():
    assert SYMBOLS == "!@#$%^&*-_=+?"


def test_symbols_contain_no_quotes_spaces_or_backslashes():
    for bad in "'\" \\":
        assert bad not in SYMBOLS


# --- Settings ---

def test_default_settings():
    settings = PasswordSettings()
    assert settings.length == 16
    assert settings.use_lowercase
    assert settings.use_uppercase
    assert settings.use_digits
    assert settings.use_symbols


# --- Validation ---

@pytest.mark.parametrize("length", [8, 16, 128])
def test_allowed_lengths_pass_validation(length):
    validate_settings(PasswordSettings(length=length))  # no error


@pytest.mark.parametrize("length", [7, 129, 0, -5])
def test_length_outside_8_to_128_is_rejected(length):
    with pytest.raises(ValueError, match="between 8 and 128"):
        validate_settings(PasswordSettings(length=length))


def test_all_kinds_turned_off_is_rejected():
    settings = PasswordSettings(
        use_lowercase=False, use_uppercase=False, use_digits=False, use_symbols=False
    )
    with pytest.raises(ValueError, match="At least one kind"):
        validate_settings(settings)


def test_generate_password_rejects_invalid_settings():
    with pytest.raises(ValueError):
        generate_password(PasswordSettings(length=7))


# --- Generating ---

def test_default_password_has_16_characters():
    assert len(generate_password(PasswordSettings())) == 16


@pytest.mark.parametrize("length", [8, 20, 128])
def test_password_has_the_requested_length(length):
    assert len(generate_password(PasswordSettings(length=length))) == length


def test_default_password_contains_every_kind():
    # Length 8 is the hardest case: with only 8 characters, a kind
    # would often be missing if it weren't guaranteed.
    for _ in range(REPEATS):
        password = generate_password(PasswordSettings(length=8))
        assert any(c in LOWERCASE for c in password)
        assert any(c in UPPERCASE for c in password)
        assert any(c in DIGITS for c in password)
        assert any(c in SYMBOLS for c in password)


def test_default_password_uses_only_allowed_characters():
    allowed = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS
    for _ in range(REPEATS):
        password = generate_password(PasswordSettings())
        assert all(c in allowed for c in password)


@pytest.mark.parametrize(
    "turned_off, forbidden",
    [
        ("use_lowercase", LOWERCASE),
        ("use_uppercase", UPPERCASE),
        ("use_digits", DIGITS),
        ("use_symbols", SYMBOLS),
    ],
)
def test_turned_off_kind_never_appears(turned_off, forbidden):
    settings = PasswordSettings(**{turned_off: False})
    for _ in range(REPEATS):
        password = generate_password(settings)
        assert not any(c in forbidden for c in password)


@pytest.mark.parametrize(
    "only_on, allowed",
    [
        ("use_lowercase", LOWERCASE),
        ("use_uppercase", UPPERCASE),
        ("use_digits", DIGITS),
        ("use_symbols", SYMBOLS),
    ],
)
def test_only_one_kind_turned_on(only_on, allowed):
    settings = PasswordSettings(
        use_lowercase=False, use_uppercase=False, use_digits=False, use_symbols=False
    )
    setattr(settings, only_on, True)
    password = generate_password(settings)
    assert len(password) == 16
    assert all(c in allowed for c in password)


def test_two_passwords_are_different():
    assert generate_password(PasswordSettings()) != generate_password(PasswordSettings())
