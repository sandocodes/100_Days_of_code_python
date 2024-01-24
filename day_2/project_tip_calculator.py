"""
Project: Tip Calculator
Written By: 
  ██████  ▄▄▄       ███▄    █ ▓█████▄  ▒█████   ▄████▄   ▒█████  ▓█████▄ ▓█████   ██████ 
▒██    ▒ ▒████▄     ██ ▀█   █ ▒██▀ ██▌▒██▒  ██▒▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▒██    ▒ 
░ ▓██▄   ▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌▒██░  ██▒▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   ░ ▓██▄   
  ▒   ██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌▒██   ██░▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄   ▒   ██▒
▒██████▒▒ ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░ ████▓▒░▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒▒██████▒▒
▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░   ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░
░  ░  ░    ░   ▒      ░   ░ ░  ░ ░  ░ ░ ░ ░ ▒  ░        ░ ░ ░ ▒   ░ ░  ░    ░   ░  ░  ░  
      ░        ░  ░         ░    ░        ░ ░  ░ ░          ░ ░     ░       ░  ░      ░  
                               ░               ░                  ░                       

Description: 
Date: January 6, 2024
Project Source: The source of this project is from a Udemy Course: 100 Days of Code: The Complete Python Pro Bootcamp for 2023
"""

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = round(total_bill / num_of_people, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")