# Randomisation and Python Lists

import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

all_options = [rock, paper, scissors]

player_choice_as_number = input("Type 0 for rock, 1 for paper, 2 for scissors: ")

if player_choice_as_number.isdigit() == False or int(player_choice_as_number) > 2:
  print("You typed invalid number! You lose.")
else:
  player_choice = all_options[int(player_choice_as_number)]
  print("Your choice is: \n" + player_choice)

  computer_choice = random.choice(all_options)
  print("Your invisible player's choice is: \n" + computer_choice)

  if player_choice == computer_choice:
    print("It's a draw.")
  elif (player_choice == rock and computer_choice == scissors) or (player_choice == scissors and computer_choice == paper) or (player_choice == paper and computer_choice == rock):
    print("You win!")
  else:
    print("You lose!")

  # if player_choice == computer_choice:
  #   print("It's a draw!")
  # elif player_choice == rock and computer_choice == scissors:
  #   print("You win!")
  # elif player_choice == scissors and computer_choice == paper:
  #   print("You win!")
  # elif player_choice == paper and computer_choice == rock:
  #   print("You win!")
  # else:
  #   print("You lose!")
