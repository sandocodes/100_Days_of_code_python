"""
Day4 Project: Blackjack, also known as 21
Written By: Justin Sando Kollie
Description/Rule: Add up your card or number (in our case) without going over 21. If you go over 21, it's an automatic BUST or you Lose immediately. When your score, if under 21, EQUALS the dealer's score, it's a DRAW. In such case, you can choose to HIT/request another card or STAND. If you choose to draw another card, your newly drawn card, added to your already existing cards EQUALS 21, You WIN. Also, if your cards total is GREATER than the dealer's cards total, You also WIN. If the dealer's cards total is LESS THAN 17, the dealer must draw another card. 
Date: January 19, 2024
Project Source: The source of this project is from a Udemy Course: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
"""
import random
from art import logo

# Display Project Logo
print(logo)


user_cards = []
computer_cards = []

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """ Returns a random card from a deck """
    card = random.choice(cards)
    return card


for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# For testing purpose
print(f"user cards: {user_cards}")
print(f"computer cards: {computer_cards}")


# Calculate Scores
def calculate_score(cards):
    """ Takes a list of cards and return the score calculated from the cards """


    if sum(cards) == 21 and len(cards) == 2:
        return 0

















# user_score = calculate_score(user_cards)
# computer_score = calculate_score(computer_cards)

# print(f"user score: {user_score}")
# print(f"computer score: {computer_score}")