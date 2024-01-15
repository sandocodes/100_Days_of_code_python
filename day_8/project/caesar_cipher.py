"""
Day4 Project: Caesar Cipher
Written By: Justin Sando Kollie
Description: 
Date: January 9, 2024
Project Source: The source of this project is from a Udemy Course: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
"""


from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Create a function that has two parameters: plain_text and shift_amount
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    # Shift each letter of the 'plain_text' forwards in the alphabet list by the shift_amount and print the encrypted text
    for letter in plain_text:
        position = alphabet.index(letter) #Get the position of each of the letters in 'plain_text' in correspondence to the alphabet list
        new_position = position + shift_amount #Shift each letter in the 'plain_text' to a new position in the 'alphabet' list using the value of the shift amount
        new_letter = alphabet[new_position] #Using the new position just generated, get it's corresponding letter in the 'alphabet' list
        cipher_text += new_letter

    print(f"The encrypted text is: {cipher_text}")

# Write the decrypted verson
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        real_letter = alphabet[new_position]
        plain_text += real_letter

    print(f"The plain text is: {plain_text}")


if direction == "encode":
    encrypt(shift_amount=shift, plain_text=text)
elif direction == "decode":
    decrypt(shift_amount=shift, cipher_text=text)