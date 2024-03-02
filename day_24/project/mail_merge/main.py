# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# invited names
invite_names = []

with open("./Output/ReadyToSend/example.txt", "w") as example_file:
    # Write the contents of the 'starter_letter.txt' to example file
    with open("./Input/Letters/starting_letter.txt") as starter_letter:
        letter_lines = starter_letter.readlines()
        for line in letter_lines:
            line.replace("[name]", replacement_txt)
            example_file.write(f"{line.strip()}\n")
