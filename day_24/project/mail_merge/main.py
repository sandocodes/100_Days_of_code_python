# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


all_invited = []

with open("./Input/Names/invited_names.txt") as invited_names:
    for name in invited_names:
        all_invited.append(name.strip())

for invited in all_invited:
    with open(f"./Output/ReadyToSend/letter_for_{invited}.txt", "w") as person_invited:
        # Write the contents of the 'starter_letter.txt' to the new files created.
        with open("./Input/Letters/starting_letter.txt") as starter_letter:
            letter_lines = starter_letter.readlines()
            for line in letter_lines:
                formatted_lines = line.replace("[name]", f"{invited}").strip()
                person_invited.write(f"{formatted_lines}\n")
