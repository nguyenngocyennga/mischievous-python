# ------------------------ PSEUDO-CODE ------------------------
# [v] import art.py and game_data, import random
# [v] print the game logo
# [v] create an empty list A = {}, and list B = {}
# [v] create a interger variable score = 0
# [ ] create a function play_game() which will loop until end_game = True
# [v] assign a random person from the data to list A, and to list B
# [ ] MAYBE I SHOULD RANDOM.CHOICE INDEX :-?
# [v] print the A random from the list of game_data with the 'name', 'description', 'country' (not showing 'follower_count')
# [v] print the B random from the list of game_data with the 'name', 'description', 'country' (not showing 'follower_count')
# [v] create a function to compare 'follower_count' between A and B, return A or B as the higher count person, save the function as a variable computer_answer
# [v] ask user to guess which one has more followers, type 'A' or 'B', use lower() to lower the text input, save the answer to the variable user_guess
# [v] compare computer_answer vs user_guess, if not the same, print("Sorry you're wrong. Final score = {score}"), exit the game
# [v] else: score += 1, print(f"You're right! Current score: {score}"), update list A to B, assign a new random person from the list, loop back to the print() A and B
# [ ] remove the selected dictionary from the list, random.choice from the list, if end_game = False, append the dictionary to the list, etc.,

from art import logo
from art import vs
from replit import clear
from game_data import data
import random

print(logo)

A = {}
B = {}
score = 0

end_game = False

def compare(option_a, option_b):
    if option_a["follower_count"] > option_b["follower_count"]:
        return "A"
    else:
        return "B"

def remove_data(person, data_list):
    return [i for i in data_list if not (i['name'] == person['name'])]

def add_data(person, data_list):
    return data_list.append(person)

A = random.choice(data)
remove_data(A, data)

while not end_game:
    B = random.choice(data)
    remove_data(B, data)

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    winner = compare(A, B)

    clear()
    print(logo)

    if winner != user_guess:
        end_game = True
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print(f"SORRY YOU'RE WRONG. FINAL SCORE: {score}")
    else:
        score += 1
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print(f"YOU'RE RIGHT! CURRENT SCORE: {score}")
        if winner == "A":
            add_data(B, data)
        else:
            add_data(A, data)
            A = B
