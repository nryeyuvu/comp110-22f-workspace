"""Program to guess the letters of an inputted word"""

__author__ = 730552319

secret: str = "python"
guess: str = str(input(f"What is your { len(secret) }-letter guess? "))

if len(guess) != 6:
    print(str(input(f"That was not { len(secret) } letters! Try again: ")))

counter: int = 0
i: int = 0
color_code: str = ""

while counter < len(secret):
    if secret[i] == guess[i]:
        color_code = color_code + "\U0001F7E9 "
    else:
       check_guess: bool = False
       checking_counter: int = 0
       while not check_guess and counter < (len(secret) - 1):
            if secret[checking_counter] == guess[counter]:
                check_guess = True
            else:
                checking_counter += 1  
       if check_guess == True:
            color_code = color_code + "\U0001F7E8 "
       else:
            color_code = color_code + "\U00002B1C "
    counter += 1
    i += 1

print(color_code)

if guess != secret:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
                