print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input(print("Are you ready to embark on this journey? Let's take your first step by choosing which direction to go. Think and then type 'left' or 'right': "))

if left_or_right.lower() == "right":
  print("Oops! Such a hole you fell into! See you again! Bye!")
else:
  swim_or_wait = input(print("Coooool!! Right move! Here you go. Walk and walk, run and run. Oh no! There comes a lake, what should you do now? Type 'wait' or 'swim': "))
  if swim_or_wait.lower() != "swim":
    print("Sorry. Attacked by trout. Your game is OVER!")
  else:
    door =  input(print("Such a ride! You have arrived at the door. Oh wait, but Which door? Pick your door by typing 'red', 'blue', or 'yellow': "))
    if door.lower() == "red":
      print("Burned by fire. Smells good. Game Over.")
    elif door.lower() == "blue":
      print("Eaten by beasts. Such bones! Game over.")
    elif door.lower() == "yellow":
      print("WOW WOW WOW!!! YOU WON!!! HERE IS YOUR MILLION BUCKS! Plus a princess (it's me! ^_^")
    else:
      print("That's no door. You lose!")
