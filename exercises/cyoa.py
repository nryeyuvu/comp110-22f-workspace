"""This game is a recreation of rock, paper, scissors."""

__author__ = "730552319"


import random

points: int = 0
player: str = ""


def greet() -> None:
    """Creates an initial message that greets the user at start of game."""
    global player
    player = input("Enter your name: ")
    print(f"Hello {player}! Get ready to play Rock, Paper, Scissors!")
    print("You will be playing this game against a computer and, each time you win, you get one point.")
    print("Basic rules are rock wins against scissors, paper wins against rock and scissors win against paper.")
    print(f"Good luck {player}!")


def definitions(player, computer) -> bool:
    """Defines what it means to win."""
    if player == "rock" and computer == "scissors":
        return True
    if player == "scissors" and computer == "paper":
        return True
    if player == "paper" and computer == "rock":
        return True
    return False


def game() -> str:
    """Sets the play for user and computer."""
    global points
    user_play: str = input("Choose your play (rock, paper, scissors): ")
    while user_play != "rock" and user_play != "paper" and user_play != "scissors":
        user_play = input("You may only choose one out of these three (rock, paper, scissors). Try again: ")
    computer_play: str = random.choice(["rock", "paper", "scissors"])
    if definitions(user_play, computer_play):
        points += 1
        return f"Computer played {computer_play}. Congrats! You won! Your total points are: {points}"
    if user_play == computer_play:
        points += 1
        return f"It's a tie, but we will give you the point \U0001f600. Your total points are: {points}"
    return f"Computer played {computer_play}. Sorry. You did not win. Your total points are {points}"


def exit_message() -> bool:
    """Checks to see if user wants to continue the game and returns points."""
    global points
    global player
    print(f"Right now, you have {points} point(s).")
    continue_game: str = input("Would you like to continue the game (y/n)? ")
    while continue_game != "y" and continue_game != "n":
        continue_game = input("Try again! Would you like to continue the game (y/n)? ")
    if continue_game == "y":
        print(game())
        return True
    print(f"{player}, you ended the game with a total of {points} point(s).")
    return False
    exit()


def main() -> None:
    """Bringing everything together."""
    global points
    global player
    points = 0
    player = ""
    greet()
    print(game())
    exit_message()
    while exit_message:
        print(game())
        exit_message()


if __name__ == "__main__":
    main()