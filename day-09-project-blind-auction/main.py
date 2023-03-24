# Dictionaries and Nesting

from replit import clear

from art import logo
print(logo)

bid_list = {}

def find_highest_bid(bidding_record):
    highest_bid_price = 0
    highest_bid_name = ""
    for bid in bid_list:
        if bid_list[bid] > highest_bid_price:
            highest_bid_price = bid_list[bid]
            highest_bid_name = bid
    print(f"The winner is {highest_bid_name} with the bid of ${highest_bid_price}")

restart = True
while restart:
    name = input("What is your name? ")
    price = int(input("What is your bid price? $"))
    bid_list[name] = price
    # print(bid_list)
    should_restart = input("Is there anyone else who wants to bid? Type 'yes' or 'no': ")
    if should_restart == "no":
        restart = False
        find_highest_bid(bid_list)
    else:
        clear()
