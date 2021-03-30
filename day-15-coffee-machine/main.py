MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    # "latte": {
    #     "ingredients": {
    #         "water": 500,
    #         "milk": 550,
    #         "coffee": 524,
    #     },
    #     "cost": 2.5,
    # },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: [v] 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# TODO: [v] 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: [v] 3. Print report.
# TODO: [v] 4. Check resources sufficient?
# TODO: [v] 5. Process coins.
# TODO: [v] 6. Check transaction successful?
# TODO: [v] 7. Make Coffee.


def report():
    print(f"""> Currently, we have:
    Water: {resources['water']}ml
    Milk: {resources['milk']}ml
    Coffee: {resources['coffee']}g
    Money: ${money}
    """)


def check_resources(drink_ordered):
    # print(MENU[drink_ordered]["ingredients"])
    global enough_resource
    for ingredient in MENU[drink_ordered]["ingredients"]:
        # print(ingredient)
        if MENU[drink_ordered]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            enough_resource = False


def process_coins():
    print("> Insert money:")
    pennies = int(input("   Pennies: "))
    nickles = int(input("   Nickles: "))
    dimes = int(input("   Dimes: "))
    quarters = int(input("   Quarters: "))
    return round((pennies * 0.01 + nickles * 0.05 + dimes * 0.1 + quarters * 0.25), 2)


def check_transaction(drink, money_amount):
    drink_cost = MENU[drink]["cost"]
    global money
    global enough_money
    if money_amount < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
    elif money_amount == drink_cost:
        money += drink_cost
        enough_money = True
        round(money, 2)
    else:
        money += drink_cost
        enough_money = True
        print(f"Here is ${round((money_inserted - drink_cost), 2)} dollars in change.")


def make_coffee(drink):
    # global resources => don't need this because we only call 'resources' without changing its value.
    for i in MENU[drink]["ingredients"]:
        resources[i] -= MENU[drink]["ingredients"][i]
    print(f"🥤 Here is your cup of {drink}. Enjoy!")


is_on = True
money = 0.0
while is_on:
    # report()
    user_action = input(f"> What would you like? (espresso $1.5/latte $2.5/cappuccino $3.0): ")
    enough_money = False
    enough_resource = True
    if user_action == "off":
        is_on = False
        print("Coffee machine has been successfully turned off. Until next time!")
    elif user_action == "report":
        report()
    else:
        check_resources(user_action)
        if enough_resource:
            while not enough_money:
                money_inserted = process_coins()
                check_transaction(user_action, money_inserted)
            make_coffee(user_action)
            # report()
