"""
Day4 Project: Caesar Cipher
Written By: Justin Sando Kollie
Description: 
Date: January 9, 2024
Project Source: The source of this project is from a Udemy Course: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
"""


from art import logo


# Display Caesar Cipher Logo
print(logo)



alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar_cipher(start_text, shift_amount, cipher_direction):
        end_text = ""
        
        if cipher_direction == "decode":
            shift_amount *= -1

        for char in start_text:
            if char in alphabets:
                position = alphabets.index(char) 
                new_position = position + shift_amount
                end_text += alphabets[new_position]
            else:
                end_text += char
        print(f"The {cipher_direction}d text is: {end_text}")

    shift = round(shift & len(alphabets))
    caesar_cipher(start_text=text, shift_amount=shift, cipher_direction=direction)

    question = str(input("Type 'yes' if you want to continue. Otherwise type 'no'.\n")).lower()
    if question == "no":
        should_continue = False
        print("Goodbye")