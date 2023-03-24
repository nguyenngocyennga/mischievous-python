# Scope and Number Guessing Game

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from replit import clear
import random

def play_game():
    print(logo)

    print("I'm thinking of a number betwwen 1 and 100.")
    level = input("   Type 'easy' or 'hard' to choose your battle level: ")
    guess_times = 0

    if level == "easy":
        guess_times = 10
    else:
        guess_times = 5

    computer_number = random.randint(1, 100)
    user_number = int(input("   Guess a number between 1 and 100: "))

    while guess_times >= 0:
        guess_times -= 1
        if computer_number == user_number:
            print("Yay you guessed right!")
            guess_times = 0
        elif guess_times >= 1:
            if computer_number > user_number:
                print(f"You guessed too low. You have {guess_times} guesses left.")
            else:
                print(f"You guessed too high. You have {guess_times} guesses left.")
            user_number = int(input("   Pick a new number: "))
        else:
            "No more attempt. You lose."
    while input("Wanna guess a new number? Type 'yes' or 'no': ") == "yes":
        clear()
        play_game()

play_game()
