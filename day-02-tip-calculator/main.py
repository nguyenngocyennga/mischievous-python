# Understanding Data Types and How to Manipulate Strings

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

each_person = (bill / people) * (1 + tip / 100)
each_person = "{:.2f}".format(each_person)

print(f"Each person should pay: ${each_person}")
