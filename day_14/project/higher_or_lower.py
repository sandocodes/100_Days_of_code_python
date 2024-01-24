"""
Day4 Project: Higher or Lower
Written By: Justin Sando Kollie
Description: 
Date: January 24, 2024
Project Source: The source of this project is from a Udemy Course: 100 Days of Code: The Complete Python Pro Bootcamp for 2023.
"""

import random
from art import logo, vs
from game_data import data

# Print Logo
print(logo)

# Print VS.
# print(vs)

# print(random_index_A)
# print(random_index_B)


# def compare_followers():
    
is_game_over = False
score = 0

   

while not is_game_over:
    # Task1: Generate 2 random names from [data] list
    random_index_A = random.randint(0, len(data) - 1)
    random_index_B = random.randint(0, len(data) - 1)

    # name
    nameA = data[random_index_A]["name"]
    # description
    descriptionA = data[random_index_A]["description"]
    # country
    countryA = data[random_index_A]["country"]
    # num_of_followers
    follower_countA = int(data[random_index_A]["follower_count"])
    print(follower_countA)

    # Get random data B:
    # name
    nameB = data[random_index_B]["name"]
    # description
    descriptionB = data[random_index_B]["description"]
    # country
    countryB = data[random_index_B]["country"]
    # num_of_followers
    follower_countB = int(data[random_index_B]["follower_count"])
    print(follower_countB)

    #   (b) Compare who has more followers
    # Print Comparison
    print(f"Compare A: {nameA}, a {descriptionA}, from {countryA}.\n{vs}\nAgainst B: {nameB}, a {descriptionB}, from {countryB}")
    whos_higher = str(input("Who has more followers? Type 'A' or 'B': ")).upper()
    if whos_higher == "A":
        # global score
        if follower_countA >= follower_countB:
            score += 1
            print(f"You're right! Current score: {score}")
            # compare_followers()
        else:
            is_game_over = True
            print(f"Sorry, that's wrong. Final Score: {score}")

    elif whos_higher == "B":
        if follower_countB >= follower_countA:
            score += 1
            print(f"You're right! Current score: {score}")
            # compare_followers()
        else:
            is_game_over = True
            print(f"Sorry, that's wrong. Final Score: {score}")

    else:
        is_game_over = True
        print(f"Wrong input")
        print(f"Final Score: {score}")



# compare_followers()