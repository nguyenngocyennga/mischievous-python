# import turtle
#
# # initialize, construct an object from the Turtle blueprint,
# # and save it into an object called timmy
# timmy = turtle.Turtle()
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

my_table = PrettyTable()
my_table.add_column("Student Name", ["Nga", "Son", "Tung"])
my_table.add_column("IELTS", ["7.5", "7.5", "6.0"])
# my_table.align = "l"

print(my_table)

