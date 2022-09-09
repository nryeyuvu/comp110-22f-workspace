"""Program to guess the letters of an inputted word."""

__author__ = "730552319"

# defines initial variables that are being later compared with one another
secret: str = "python"  # Can be changed to any string of any size
guess: str = str(input(f"What is your { len(secret) }-letter guess? "))

# Checks to make sure the length of both variables match
while len(guess) != len(secret):
    guess = str(input(f"That was not { len(secret) } letters! Try again: "))

# variables to keep count of when below loop should end
counter: int = 0
i: int = 0
color_code: str = ""  # Stores the final color combination

# Builds the color code combination for which letters are wrong and right (the body of wordle)
while counter < len(secret):
    if secret[i] == guess[i]:
        color_code = color_code + "\U0001F7E9"
    else:
        check_guess: bool = False
        checking_counter: int = 0
        while not check_guess and checking_counter < len(secret):
            if secret[checking_counter] == guess[counter]:
                check_guess = True
            else:
                checking_counter += 1  
        if check_guess:
            color_code = color_code + "\U0001F7E8"
        else:
            color_code = color_code + "\U00002B1C"
    counter += 1
    i += 1

print(color_code)

# Checking guess with secret and giving user output on their guess
if guess != secret:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
                