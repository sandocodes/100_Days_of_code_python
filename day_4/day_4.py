# Day 4: Beginner Level -> Radomisation and Python Lists

# Python Random Module
# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)

# love_score = random.randint(1, 100)
# print(F"Your love score is {love_score}")


# Python Lists:
    # - List Syntax: fruits = ["item1", "item2"]
    # Each item in a list has an index beginning with 0. This means the first item in a list has index 0

# import random
# names = ["James", "Martina", "Daniel", "Samuel", "Jarso"]

# # Get the total numbers of items in list
# num_names = len(names)
# # Generate the random numbers between 0 and the last index
# random_choice = random.randint(0, num_names)
# # Pick out random person from the list of names using the random number
# person_who_pays = names[random_choice]
# print(f"{person_who_pays} is going to buy drinks today")

# labels = ["A", "B", "C"]
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"
# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{labels}\n{line1}\n{line2}\n{line3}")