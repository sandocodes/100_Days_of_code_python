"""
Project: Band Name
Written By: Justin Sando Kollie
Description: This program combines two inputs: the name of the user's city
            and their pet's name. The program then combines the two inputs to generate 
            the user's band name.
Date: January 5, 2024
Project Source: The source of this project is from a Udemy Course: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
"""

# 1. Create a greeting for your program.
print("Welcome to the Brand Name Generator.")

# 2. Ask the user for the city they grew up in.
city = str(input("What's the name of the city you grew up in?\n"))

# 3. Ask the user for the name of a pet.
pet = str(input("What's the name of your pet?\n")) 

# 4. Combine the name of the city and pet and show them their band name.
band_name = f"{city} {pet}"
print(f"The name of your band could be {band_name}.")
