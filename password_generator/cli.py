"""Command-line interface: read the options, print a password or an error."""

import argparse

from password_generator.generator import PasswordSettings, generate_password


def build_parser():
    """Describe the command-line options."""
    parser = argparse.ArgumentParser(
        prog="password_generator",
        description="Create a strong, random password.",
    )
    parser.add_argument(
        "--length",
        type=int,
        default=PasswordSettings().length,
        help="number of characters, 8-128 (default: %(default)s)",
    )
    parser.add_argument("--no-lowercase", action="store_true", help="leave out a-z")
    parser.add_argument("--no-uppercase", action="store_true", help="leave out A-Z")
    parser.add_argument("--no-digits", action="store_true", help="leave out 0-9")
    parser.add_argument("--no-symbols", action="store_true", help="leave out symbols")
    return parser


def main(argv=None):
    """Run the program. argv is the list of options (None means: the real command line)."""
    parser = build_parser()
    args = parser.parse_args(argv)
    settings = PasswordSettings(
        length=args.length,
        use_lowercase=not args.no_lowercase,
        use_uppercase=not args.no_uppercase,
        use_digits=not args.no_digits,
        use_symbols=not args.no_symbols,
    )
    try:
        password = generate_password(settings)
    except ValueError as error:
        # Same style as argparse's own errors: message on stderr, exit code 2.
        parser.error(str(error))
    print(password)
