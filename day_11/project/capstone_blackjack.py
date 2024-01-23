"""
Day4 Project: Blackjack, also known as 21
Written By: Justin Sando Kollie
Description/Rule: Add up your card or number (in our case) without going over 21. If you go over 21, it's an automatic BUST or you Lose immediately. When your score, if under 21, EQUALS the dealer's score, it's a DRAW. In such case, you can choose to HIT/request another card or STAND. If you choose to draw another card, your newly drawn card, added to your already existing cards EQUALS 21, You WIN. Also, if your cards total is GREATER than the dealer's cards total, You also WIN. If the dealer's cards total is LESS THAN 17, the dealer must draw another card. 
Date: January 19, 2024
Project Source: The source of this project is from a Udemy Course: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
"""
import random, os
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """ Returns a random card from a deck """
    card = random.choice(cards)
    return card

# Deal the user and computer 2 cards each using deal_card()
#6 Calculate Scores
def calculate_score(cards):
    """Takes a list of cards and return the score calculated from the cards"""
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    """Compare the user score with the computer score to determine who wins"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent wen over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    """Play the Blackjack (21) Game"""

    # Display Project Logo
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is: {user_cards}, final score: {user_score}")
    print(f"Computer 's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("clear")
    play_game()