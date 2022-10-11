"""Integrated wordle game allowing users six tries to guess the right secret word."""

__author__ = "730552319"


# Function that will check if character is in secret word
# Reduces work! :)
def contains_char(searched_word: str, char_to_search: str) -> bool:
    """Checks to see if the one character is found anywhere in the word."""
    assert len(char_to_search) == 1
    check_guess: bool = False
    func_counter: int = 0

    # Checks if letter appears anywhere in searched word
    while not check_guess and func_counter < len(searched_word):
        if searched_word[func_counter] == char_to_search:
            check_guess = True
        else:
            func_counter += 1
    return check_guess


def emojified(guess: str, secret: str) -> str:
    """Tests user guess with secret word and returns corresponding color emoji."""
    assert len(guess) == len(secret)
    # variables to keep count of when below loop should end
    i: int = 0
    color_code: str = ""  # Stores the final color combination

    # Builds the color code combination for which letters are wrong and right (the body of wordle)
    while i < len(secret):
        if secret[i] == guess[i]:
            color_code = color_code + "\U0001F7E9"
        else:
            if contains_char(secret, guess[i]):
                color_code = color_code + "\U0001F7E8"
            else:
                color_code = color_code + "\U00002B1C"
        i += 1
    return color_code


def input_guess(expected_len: int) -> str:
    """Has the user pick a guess word based on a user-determined length."""
    # Makes user guess word
    inputted_guess: str = str(input(f"Enter a {expected_len} character word: "))

    # Checks to make sure the length of both variables match
    while len(inputted_guess) != expected_len:
        inputted_guess = str(input(f"That wasn't {expected_len} chars! Try again: "))
    return inputted_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    num_of_tries: int = 1
    five_green: str = "\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9" + "\U0001F7E9"

    # Bringing everything together
    while num_of_tries < 7:
        print(f"=== Turn {num_of_tries}/6 === ")
        test: str = emojified(input_guess(5), "codes")
        print(test)
        if test == five_green:
            print(f"You won in {num_of_tries}/6 turns!")
            return
        else:
            num_of_tries += 1
    print("X/6 = Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()