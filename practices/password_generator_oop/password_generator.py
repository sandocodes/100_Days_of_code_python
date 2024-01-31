from password import Password
import random


# User inputs
num_of_letters = int(input("How many letters?: "))
num_of_symbols = int(input("How many symbols?: "))
number_amount = int(input("How many numbers?: "))

# Generate List each of Letters, Symbols and Numbers
random_letters = Password(num_of_letters, num_of_symbols, number_amount).generate_letters()
random_symbols = Password(num_of_letters, num_of_symbols, number_amount).generate_symbols()
random_numbers = Password(num_of_letters, num_of_symbols, number_amount).generate_numbers()

# Turn Letters, Symbols and Numbers to Strings
letters = ""
for letter in random_letters:
    letters += letter

symbols = ""
for symbol in random_symbols:
    symbols += symbol

numbers = ""
for number in random_numbers:
    numbers += number

# Generated Password
generated_password = f"{letters}{symbols}{numbers}"

# Randomize the positions of the Letters, Symbols and Numbers in our password
# 1. Transform password into list
list_password = list(generated_password)
# 2. Shuffle letters, numbers and symbols
random.shuffle(list_password)

# Turn Password Back to Strings
password = ""
for item in list_password:
    password += item

# Password Output
print(f"Your Password: {password}")
