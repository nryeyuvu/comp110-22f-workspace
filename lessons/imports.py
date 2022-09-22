"""Examples of importing Python."""

# Alias a module / imported name as another name
from lessons import helpers # this was unnecessary considering the other line
from lessons import helpers as hp

# import names defined globally in a module
from lessons.helpers import powerful, THE_ANSWER



def main() -> None:
    """Entrypoint of program."""
    print(hp.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER)")
    print( powerful(2, 4))


if __name__ == "__main__":
    main()