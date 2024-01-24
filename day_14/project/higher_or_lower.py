"""
Day4 Project: Higher or Lower
Written By: 
  ██████  ▄▄▄       ███▄    █ ▓█████▄  ▒█████   ▄████▄   ▒█████  ▓█████▄ ▓█████   ██████ 
▒██    ▒ ▒████▄     ██ ▀█   █ ▒██▀ ██▌▒██▒  ██▒▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▒██    ▒ 
░ ▓██▄   ▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌▒██░  ██▒▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   ░ ▓██▄   
  ▒   ██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌▒██   ██░▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄   ▒   ██▒
▒██████▒▒ ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░ ████▓▒░▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒▒██████▒▒
▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░   ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░
░  ░  ░    ░   ▒      ░   ░ ░  ░ ░  ░ ░ ░ ░ ▒  ░        ░ ░ ░ ▒   ░ ░  ░    ░   ░  ░  ░  
      ░        ░  ░         ░    ░        ░ ░  ░ ░          ░ ░     ░       ░  ░      ░  
                               ░               ░                  ░                       
Description: User inputs 'A' or 'B' to guess which celebrity has the most followers. If the user guesses right, the celebrity in 'B' position gets put in the 'A' position and a random celebrity is selected for the 'B' position. A feedback and the current score also get printed. If the user guesses wrong, the final score, along with a message is printed to the console. Moreover, if the user inputs anything other than 'A' or 'B', a message: 'Wrong input' gets printed and the final score is also printed.
Date: January 24, 2024
Project Source: The source of this project is from a Udemy Course: 100 Days of Code: The Complete Python Pro Bootcamp for 2023.
"""


# Modules Imports
from os import system
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

# Start Game
def play_game():
    # Print project logo and project introduction
    print(logo)

    # variables to be modified in the function
    global is_game_over, score, index_personB, index_personA

    # While game is not over:
    while not is_game_over:

        # Random Data For Person A
        personA = data[index_personA]["name"]
        personA_Description = data[index_personA]["description"]
        personA_Country = data[index_personA]["country"]
        personA_followerCount = int(data[index_personA]["follower_count"])
        # print(personA_followerCount) #For testing purpose, will delete later

        # Random Data For Person B:
        personB = data[index_personB]["name"]
        personB_Description = data[index_personB]["description"]
        personB_Country = data[index_personB]["country"]
        personB_followerCount = int(data[index_personB]["follower_count"])
        # print(personB_followerCount) #For testing purpose, will delete later

        print(f"Compare A: {personA}, a {personA_Description}, from {personA_Country}.\n{vs}\nAgainst B: {personB}, a {personB_Description}, from {personB_Country}.")

        # Compare who has more followers based on user input
        # Take user input and return UpperCase version
        whos_higher = str(input("Who has more followers? Type 'A' or 'B': "))

        if whos_higher.upper() == "A": #If user inputs "A"
            #if personA follower count is greater than or equal to personB follower count
            if personA_followerCount >= personB_followerCount:
                score += 1 #Add 1 to the score
                system("clear") #clear the screen
                print(logo) #print Game logo
                print(f"You're right! Current score: {score}") #Output the current score
                index_personA = index_personB #Set variable index_personA to the index of the previous personB
                index_personB = randint(0, len(data) -1) #Generate random index for personB
            else: #if personA follower count is less than personB follower count
                is_game_over = True #End the game or Game Over
                system("clear") #Clear the screen
                print(logo) #Print Game logo
                print(f"Sorry, that's wrong. Final Score: {score}") #Output the final score #Run the wrong_guess() function Line26
        elif whos_higher.upper() == "B": #If the user inputs "B"
            #If personB follower count is GREATER THAN or EQUAL to personA follower count
            if personB_followerCount >= personA_followerCount:
                score += 1 #Add 1 to the score
                system("clear") #clear the screen
                print(logo) #Print Game logo
                print(f"You're right! Current score: {score}") #Output the current score
                index_personA = index_personB #Set variable index_personA to the index of the previous personB
                index_personB = randint(0, len(data) -1) #Generate random index for personB
            else: #If personB follower count is LESS THAN personA follower count
                is_game_over = True #End the game or Game Over
                system("clear") #Clear the screen
                print(logo) #Print Game logo
                print(f"Sorry, that's wrong. Final Score: {score}") #Output the final score
        else: #If the user inputs anything other than "A" or "B"
            is_game_over = True #End the game or Game Over
            system("clear") #Clear the screen
            print(logo) #Print Game logo
            print(f"Wrong input: '{whos_higher}'") #Inform user of input
            print(f"Final Score: {score}") #Output final score

play_game() #End Game