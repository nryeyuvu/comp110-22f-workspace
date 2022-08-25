"""EX01 - Chardle - A cure step toward Wordle."""

__author__ = "730552319"

word: str = input("Enter a 5-character word: ")
if(len(word) < 5 or len(word) > 5):
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")
if(len(character) > 1 or len(character < 1)):
    print("Error: Character must be a single character")
    exit()

print("Searching for " + character + " in " + word)

count: int = 0
if(word[0] == character):
    print(character + " found at index 0")
    count = count + 1

if(word[1] == character):
    print(character + " found at index 1")
    count = count + 1

if(word[2] == character):
    print(character + " found at index 2")
    count = count + 1

if(word[3] == character):
    print(character + " found at index 3")
    count = count + 1

if(word[4] == character):
    print(character + " found at index 4")
    count = count + 1

if(count >= 1):
    print(str(count) + " instances of " + character + " found in " + word)
else:
    print("No instances of " + character + " found in " + word)