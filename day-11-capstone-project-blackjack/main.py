# The Blackjack Capstone Project

from art import logo
import random
import replit

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(sum_user_scores, sum_dealer_scores):
    if sum_user_scores > 21:
        if sum_dealer_scores > 21:
            print("You and the dealer both went over. It's a draw.")
        elif sum_dealer_scores <= 21:
            print("You went over. You lose.")
    elif sum_user_scores <= 21:
        if sum_dealer_scores > 21:
            print("The dealer went over. You win!")
        if sum_dealer_scores <= 21:
            if sum_user_scores == sum_dealer_scores:
                print("It's a draw.")
            elif sum_user_scores > sum_dealer_scores:
                print("You win!")
            else:
                print("You lose!")

def play_blackjack():
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = [random.choice(cards), random.choice(cards)]
    dealer_cards = [random.choice(cards), random.choice(cards)]

    should_continue = True
    while should_continue:
        sum_user_scores = calculate_score(user_cards)
        sum_dealer_scores = calculate_score(dealer_cards)

        print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"    Computer's first card: {dealer_cards[0]}")

        if sum_user_scores == 0 or sum_dealer_scores == 0 or sum_user_scores > 21:
            should_continue = False
        else:
            # 
            # should_continue = False
            if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                user_cards.append(random.choice(cards))
            else:
                should_continue = False
        
    while sum_dealer_scores != 0 and sum_dealer_scores < 17:
        dealer_cards.append(random.choice(cards))
        sum_dealer_scores = calculate_score(dealer_cards)

    print(f"    Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"    Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")    

    compare_scores(sum(user_cards), sum(dealer_cards))

    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        replit.clear()
        play_blackjack()

play_blackjack()
