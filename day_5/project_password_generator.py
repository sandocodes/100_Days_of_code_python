"""
Day 5 Project: PyPassword Generator
Written By: Justin Sando Kollie
Description: Generate passwords
Date: January 10, 2024
Project Source: The source of this project is from a Udemy Course: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
"""
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Generate Random Letters
random_letters = ""
for letter in range(1, nr_letters + 1):
    random_letters += random.choice(letters)

# Generate Random Symbols
random_symbols = ""
for symbol in range(1, nr_symbols + 1):
    random_symbols += random.choice(symbols)

# Generate Random Numbers
random_numbers = ""
for number in range(1, nr_numbers + 1):
    random_numbers += random.choice(numbers)

# Print Password in Specific order (Letters Symbols Numbers)
password = str(f"{random_letters}{random_symbols}{random_numbers}")
print(f"Your password is: {password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Randomise the order of characters in the password
list_password = list(password)
random.shuffle(list_password)

# Convert password list to string
password_string = ""
for items in list_password:
    password_string += items

print(f"Password shuffled: {password_string}")