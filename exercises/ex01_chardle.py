"""EX01 - Chardle - A cure step toward Wordle."""

__author__ = "730552319"


# Responsible for user input
five_char_word: str = input("Enter a 5-character word: ")
if len(five_char_word) < 5 or len(five_char_word) > 5:
    print("Error: Word must contain 5 characters")
    exit()

one_character: str = input("Enter a single character: ")
if len(one_character) > 1 or len(one_character) < 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + one_character + " in " + five_char_word)

# checks inputed character to see if its part of the five character word
char_count: int = 0

if five_char_word[0] == one_character:
    print(one_character + " found at index 0")
    char_count = char_count + 1
if five_char_word[1] == one_character:
    print(one_character + " found at index 1")
    char_count = char_count + 1
if five_char_word[2] == one_character:
    print(one_character + " found at index 2")
    char_count = char_count + 1
if five_char_word[3] == one_character:
    print(one_character + " found at index 3")
    char_count = char_count + 1
if five_char_word[4] == one_character:
    print(one_character + " found at index 4")
    char_count = char_count + 1

# print character count in word
if char_count > 1:
    print(str(char_count) + " instances of " + one_character + " found in " + five_char_word)
if char_count == 1:
    print("1 instance of " + one_character + " found in " + five_char_word)
else:
    print("No instances of " + one_character + " found in " + five_char_word)