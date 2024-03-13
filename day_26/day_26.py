# List and Dictionary Comprehension

# List Comprehension

# Without List Comprehension, add 1 to each item in a my_list = [1, 2, 3]
numbers = [1, 2, 3]
# new_list = []
# for item in numbers:
#     add_1 = item + 1
#     new_list.append(add_1)
# print(new_list)

# List Comprehension Syntax: new_list = [new_item for item in list [condition - optional]]
second_list = [n + 1 for n in numbers]
# print(second_list)


# Square:
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
# print(squared_numbers)


# Dictionary Comprehension
# Syntax: {new_key:new_value for item in list}
import random, pandas

# Example: Let's generate random numbers for each item in a list
# names = ["Alex", "James", "Jarso", "Martina", "Prinecss", "Chris", "Daniel"]
# stu_scores = {student:random.randint(60, 100) for student in names}
# print(f"All Scores: {stu_scores}")

# passed_students = {student:stu_scores[student] for student in stu_scores if stu_scores[student] >= 70}
# failed_students = {student:stu_scores[student] for student in stu_scores if stu_scores[student] <= 69}
# print(f"Failed: {failed_students}")
# print(f"Passed: {passed_students}")


weather_c = {
    "Monday": 12, 
    "Tuesday": 14, 
    "Wednesday": 15, 
    "Thursday": 14, 
    "Friday": 21, 
    "Saturday": 22, 
    "Sunday": 24
}

# Write your Weather temperature in Farenheight
# Celcius to Farenheight: (temp * 9/5) + 32

weather_f = {temp:(weather_c[temp] * 9/5) + 32 for temp in weather_c}
print(weather_f)