# Hangman Game

import random

# STEP 1

word_list = ["ardvark", "baboon", "camel", "superfluous", "redundant"]

# Todo-1 - Randomly choose a word from the word_list and assign it a vairable called chosen_word.
word_list_length = len(word_list)
chosen_word = word_list[random.randint(0, word_list_length - 1)]
print(chosen_word)

# Todo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = str(input("Guess a letter: ")).lower()

# Todo-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letters in chosen_word:
    if guess == letters:
        print("Right")
    else:
        print("Wrong")


# STEP 2