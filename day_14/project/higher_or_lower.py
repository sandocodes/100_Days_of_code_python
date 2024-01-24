"""Day4 Project: Higher or Lower
Written By:
██████  ▄▄▄       ███▄    █ ▓█████▄  ▒█████   ▄████▄   ▒█████  ▓█████▄
▓█████   ██████ ▒██    ▒ ▒████▄     ██ ▀█   █ ▒██▀ ██▌▒██▒  ██▒▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▒██    ▒ ░ ▓██▄   ▒██
 ▀█▄  ▓██  ▀█ ██▒░██   █▌▒██░  ██▒▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   ░ ▓██▄ ▒   ██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌▒██
 ██░▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄   ▒   ██▒ ▒██████▒▒ ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░ ████▓▒░▒ ▓███▀ ░░
 ████▓▒░░▒████▓ ░▒████▒▒██████▒▒ ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░▒
 ▒▓▒ ▒ ░ ░ ░▒  ░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░   ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░ ░  ░  ░    ░   ▒
    ░   ░ ░  ░ ░  ░ ░ ░ ░ ▒  ░        ░ ░ ░ ▒   ░ ░  ░    ░   ░  ░  ░ ░        ░  ░         ░    ░        ░ ░  ░ ░
          ░ ░     ░       ░  ░      ░ ░               ░                  ░
Description: User inputs 'A' or 'B' to
          guess which celebrity has the most followers. If the user guesses right, the celebrity in 'B' position gets
          put in the 'A' position and a random celebrity is selected for the 'B' position. A feedback and the current
          score also get printed. If the user guesses wrong, the final score, along with a message is printed to the
          console. Moreover, if the user inputs anything other than 'A' or 'B', a message: 'Wrong input' gets printed
          and the final score is also printed.
Date: January 24, 2024
Project Source: The source of this project is
          from a Udemy Course: 100 Days of Code: The Complete Python Pro Bootcamp for 2023."""

# Modules Imports

from random import randint
from art import logo, vs
from game_data import data

# Global Variables
is_game_over = False
score = 0

#  Generate 2 random indices, which are used to generate random data
# Use randint to generate random indices
index_personA = randint(0, len(data) - 1)
index_personB = randint(0, len(data) - 1)

if index_personA == index_personB:
    index_personB = randint(0, len(data) - 1)


# Start Game
def play_game():
    # Print project logo and project introduction
    print(logo)

    # variables to be modified in the function
    global is_game_over, score, index_personB, index_personA

    # While game is not over:
    while not is_game_over:

        # Random Data For Person A
        person_a = data[index_personA]["name"]
        person_a_description = data[index_personA]["description"]
        person_a_country = data[index_personA]["country"]
        person_a_follower_count = int(data[index_personA]["follower_count"])
        # print(personA_followerCount) #For testing purpose, will delete later

        # Random Data For Person B:
        person_b = data[index_personB]["name"]
        person_b_description = data[index_personB]["description"]
        person_b_country = data[index_personB]["country"]
        person_b_follower_count = int(data[index_personB]["follower_count"])
        # print(personB_followerCount) #For testing purpose, will delete later

        print(
            f"Compare A: {person_a}, a {person_a_description}, from {person_a_country}.\n{vs}\nAgainst B: "
            f"{person_b}, a {person_b_description}, from {person_b_country}."
        )

        # Compare who has more followers based on user input
        # Take user input and return UpperCase version
        user_input = str(input("Who has more followers? Type 'A' or 'B': "))

        if user_input.upper() == "A":  # If user inputs "A"
            if person_a_follower_count > person_b_follower_count:
                is_game_over = True  # End the game or Game Over
                # system("clear") #Clear the screen
                print(logo)  # Print Game logo
                print(f"Sorry, that's wrong. Final Score: {score}")
            else:
                score += 1  # Add 1 to the score
                # system("clear") #clear the screen
                print(logo)  # print Game logo
                print(f"You're right! Current score: {score}")  # Output the current score
                index_personA = index_personB  # Set variable index_personA to the index of the previous personB
                index_personB = randint(0, len(data) - 1)  # Generate random index for personB
        # If the user inputs "B"
        elif user_input.upper() == "B":
            if person_b_follower_count > person_a_follower_count:
                # Add 1 to the score
                score += 1
                print(logo)
                # Output the current score
                print(f"You're right! Current score: {score}")
                # Set variable index_personA to the index of the previous personB
                index_personA = index_personB
                # Generate random index for personB
                index_personB = randint(0, len(data) - 1)
            # If personB follower count is LESS THAN personA follower count
            else:
                # End the game or Game Over
                is_game_over = True
                # system("clear") #Clear the screen
                # Print Game logo
                print(logo)
                # Output the final score
                print(f"Sorry, that's wrong. Final Score: {score}")
        # If the user inputs anything other than "A" or "B"
        else:
            # End the game or Game Over
            is_game_over = True
            # Print Game logo
            print(logo)
            # Inform user of input
            print(f"Wrong input: '{user_input}'")
            # Output final score
            print(f"Final Score: {score}")


play_game()

