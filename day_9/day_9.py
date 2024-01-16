# Day 9: Dictionaries, Nesting and Secret Auction
# Dictionary Syntax:
#  =======> dict_name = {"key": value}
# To have more than one entries in a dictionary, separate each entry with a comma(,)
# Example: dict_name = {"Bug": "An error in a program that prevents the program from running.", "Function": "A piece of code that you can easily call over and over again."}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Accessing Items fro a Dictionary:
# Syntax ===> dict_name["key"]
# print(programming_dictionary["Bug"])

# WARNING: If we try to access a key that doesn't exist in a dictionary, we get a KeyError warning.

# Adding new items to dictionary.
# Syntax: dict_name["key"] = value
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)


# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary["Bug"])


# Looping through a dictionary
# for i in programming_dictionary:
#     print(f"{i}: {programming_dictionary[i]}")

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# # TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#   score = student_scores[key]
#   if score >= 91:
#     student_grades[key] = "Outstanding"
#   elif score >= 81:
#     student_grades[key] = "Exceeds Expectations"
#   elif score >= 71:
#     student_grades[key] = "Acceptable"
#   else:
#     student_grades[key] = "Fail"

# # 🚨 Don't change the code below 👇
# print(student_grades)

############################## NESTING ##############################

#simple dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

################ NESTING Lists inside a Dictionary ################
# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"], 
#         "total_visits": 12
#     },
#     "German": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
#         "total_visits": 4
#     },
# }


############### NESTING Dictionaries inside a List ###############
# travel_log = [
#     {
#         "country": "France", 
#         "cities_visited": ["Paris", "Lille", "Dijon"], 
#         "total_visits": 12
#     },
#     {
#         "country": "German", 
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
#         "total_visits": 4
#     },
# ]




# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# # Do NOT change the code above 👆

# #TODO: Write the function that will allow new countries
# # to be added to the travel_log. 
# def add_new_country(name, times_visited, cities_visited):
#         # Add the country and it's data to the travel_log
#     travel_log.append({
#         "country": name,
#         "visits": times_visited,
#         "cities": cities_visited
#     })

# # Do not change the code below 👇
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")


# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# dict["c"] = [1, 2, 3]
# # dict[1] = 4
# print(dict[1])