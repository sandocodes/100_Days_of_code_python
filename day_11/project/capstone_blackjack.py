"""
Day4 Project: Blackjack / 21
Written By: Justin Sando Kollie
Description/Rule: Add up your card or number (in our case) without going over 21. If you go over 21, it's an automatic BUST or you Lose immediately. When your score, if under 21, EQUALS the dealer's score, it's a DRAW. In such case, you can choose to HIT/request another card or STAND. If you choose to draw another card, your newly drawn card, added to your already existing cards EQUALS 21, You WIN. Also, if your cards total is GREATER than the dealer's cards total, You also WIN. If the dealer's cards total is LESS THAN 17, the dealer must draw another card. cards = [a=11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
Date: January 19, 2024
Project Source: The source of this project is from a Udemy Course: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
"""

from art import logo
print(logo)