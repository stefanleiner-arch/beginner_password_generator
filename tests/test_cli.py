import subprocess
import sys
from pathlib import Path

import pytest

from password_generator.cli import main
from password_generator.generator import DIGITS, LOWERCASE, SYMBOLS, UPPERCASE

PROJECT_FOLDER = Path(__file__).parent.parent


def run(capsys, *options):
    """Run main() with the given options and return (output, error output)."""
    main(list(options))
    captured = capsys.readouterr()
    return captured.out, captured.err


def run_expecting_error(capsys, *options):
    """Run main(), check that it stops with exit code 2, return (output, error output)."""
    with pytest.raises(SystemExit) as exit_info:
        main(list(options))
    assert exit_info.value.code == 2
    captured = capsys.readouterr()
    return captured.out, captured.err


# --- Working commands ---

def test_no_options_prints_one_16_character_password(capsys):
    out, err = run(capsys)
    lines = out.splitlines()
    assert len(lines) == 1
    assert len(lines[0]) == 16
    assert err == ""


def test_length_and_no_symbols(capsys):
    out, _ = run(capsys, "--length", "20", "--no-symbols")
    password = out.strip()
    assert len(password) == 20
    assert not any(c in SYMBOLS for c in password)


@pytest.mark.parametrize(
    "option, forbidden",
    [
        ("--no-lowercase", LOWERCASE),
        ("--no-uppercase", UPPERCASE),
        ("--no-digits", DIGITS),
        ("--no-symbols", SYMBOLS),
    ],
)
def test_each_no_option_leaves_out_its_kind(capsys, option, forbidden):
    out, _ = run(capsys, option)
    assert not any(c in forbidden for c in out.strip())


# --- Errors: clear message, no password ---

@pytest.mark.parametrize("length", ["5", "129"])
def test_length_out_of_range_is_an_error(capsys, length):
    out, err = run_expecting_error(capsys, "--length", length)
    assert out == ""
    assert "between 8 and 128" in err


@pytest.mark.parametrize("length", ["abc", "12.5"])
def test_length_not_a_whole_number_is_an_error(capsys, length):
    out, err = run_expecting_error(capsys, "--length", length)
    assert out == ""
    assert "invalid int value" in err


def test_all_kinds_turned_off_is_an_error(capsys):
    out, err = run_expecting_error(
        capsys, "--no-lowercase", "--no-uppercase", "--no-digits", "--no-symbols"
    )
    assert out == ""
    assert "At least one kind" in err


# --- The real command ---

def test_python_dash_m_prints_a_password():
    result = subprocess.run(
        [sys.executable, "-m", "password_generator", "--length", "12"],
        capture_output=True,
        text=True,
        cwd=PROJECT_FOLDER,
    )
    assert result.returncode == 0
    assert len(result.stdout.strip()) == 12
