"""This game is a recreation of rock, paper, scissors."""

__author__ = "730552319"


import random

points: int = 0

def greet() -> None:
    """Creates an initial message that greets the user at start of game."""
    name: str = input("Enter your name: ")
    print(f"Hello {name}! Get ready to play Rock, Paper, Scissors!")
    print("You will be playing this game against a computer and, each time you win, you get one point.")
    print("Basic rules are rock wins against scissors, paper wins against rock and scissors win against paper.")
    print(f"Good luck {name}!")

def definitions(player, computer) -> bool:
    """Defines what it means to win."""
    if player == "rock" and computer == "scissors":
        return True
    if player == "scissors" and computer == "paper":
        return True
    if player == "paper" and computer == "rock":
        return True
    return False


def game() -> int:
    """Sets the play for user and computer."""
    global points
    user_play: str = input("Choose your play (rock, paper, scissors): ")
    while user_play != "rock" or user_play != "paper" or user_play != "scissors":
        user_play = input("You may only choose one out of these three (rock, paper, scissors). Try again: ")
    computer_play: str = random.choice(["rock", "paper", "scissors"])
    if definitions(user_play, computer_play):
        points += 1
        return f"Congrats! You won! Your total points are: {points}"
    if user_play == computer_play:
        points += 1
        return f"It's a tie, but we will give you the point \U0001f600. Your total points are: {points}"
    return f"Sorry. You did not win. Your total points are {points}"


def main() -> None:
    global points
    greet()
    game()
    continue_game: str = input("Would you like to continue the game (y/n)? ")
    while continue_game != "y" or continue_game != "n":
        continue_game = input("Try again! Would you like to continue the game (y/n)? ")
    if continue_game == "y":
        game()
    elif continue_game == "n":
        print(f"You ended the game with a total of {points} points.")

main()

if __name__ == "__main__":
    main()