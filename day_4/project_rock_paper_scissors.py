"""
Day4 Project: Rock, Paper, Scissors
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

Description: 
        Rules: Rock beats Scissors, Scissors beats Paper and Paper beats Rock
Date: January 9, 2024
Project Source: The source of this project is from a Udemy Course: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
"""
import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice >= 3 or computer_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(f"You chose:\n{game_images[user_choice]}")
    print(f"Computer chose:\n{game_images[computer_choice]}")

    # you win
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    # computer wins - if computer choice is greater than user choice
    elif computer_choice > user_choice:
        print("You loose!")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
    