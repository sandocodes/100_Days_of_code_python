"""
Day4 Project: Hangman Game
Written By: Justin Sando Kollie
Description: A random word is generated in a series of _'s and the user has to guess the letters in the word. If the user guess a letter    right, that letter is placed in the position of the _ in the random word. If the user guesses wrong, a man begins to hang while the user lives decreases by 1. When the user has no lives left, the game is over.
Date: January 9, 2024
Project Source: The source of this project is from a Udemy Course: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
"""

import random
from hangman_words import word_list
from hangman_art import logo, stages

# Display Hangman Logo
print(f"{logo}")

lives = 6
game_over = False

# Generate a random word from the word list and store in variable word_list
chosen_word = random.choice(word_list)

# Generate as many blanks as the letters in the random word
display = []
for i in chosen_word:
    display += "_"

print(f"Your word: {' '.join(display)}\n")

while not game_over:
    # Ask the user to guess a letter and store in the variable called guess
    guess = str(input("Guess a letter: ")).lower()

    # Is the guessed letter in the chosen_word?
    # If yes, replace the "_" in the 'display' list of the chosen word with the guessed word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess

    # If the guessed word is not in the chosen_word, reduce the user's lives by 1
    if guess not in chosen_word:
        lives -= 1
        # If user have no lives left, Game Over
        if lives == 0:
            # End the game
            game_over = True
            print("Game over, you lose.")
            print(f"The word is: {chosen_word}")

    # Join all the elements in the 'display' list and turn it into a string
    print(f"{' '.join(display)}")

    # If there are no _'s in the display list, after guessing the word, the user wins.
    if "_" not in display:
        # End the game
        game_over = True
        print("You win.")

    print(f"{stages[lives]}")