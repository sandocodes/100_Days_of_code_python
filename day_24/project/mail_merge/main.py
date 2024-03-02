# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import os


invite_names = []  # invited names
replacement_txt = "[Test]"

with open('./Input/Names/invited_names.txt') as invites:
    for name in invites:
        invite_names.append(name.strip())

for inv_name in invite_names:
    with open(f'./Output/ReadyToSend/letter_for_{inv_name.strip()}.txt', 'w') as example_file:
        # Write the contents of the 'starter_letter.txt' to example file
        with open("./Input/Letters/starting_letter.txt") as starter_letter:
            letter_lines = starter_letter.readlines()
            print(letter_lines)
            for line in letter_lines:
                formatted_lines = line.replace('[name]', f"{inv_name}").rstrip()
                print(formatted_lines)
                example_file.write(f"{formatted_lines}\n")
                