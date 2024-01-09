# Day 5: Beginner Level -> for loops with lists [] and range

# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     # print(fruit)
#     print(fruit + " Pie" )

# student_heights = [151, 145, 179]
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
    
# # total heights
# total_heights = 0
# for height in student_heights:
#     total_heights += height
# print(f"Total heights: {total_heights}")

# # number of students
# num_students = 0
# for student in student_heights:
#     num_students += 1
# print(f"Number of students: {num_students}")

# # Average heights
# avarage_height = round(total_heights / num_students)
# print(f"Average height: {avarage_height}")

# Highest Number from a list of numbers
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score

# print(max_score)

# Range Function => 
# Syntax: for number in range(start, end, excluding the end):
#             print(number)
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# Add all Even numbers from a given range of numbers
# target = int(input("Enter a number between 1 and 1000: "))
# even_sum = 0

# for number in range(1, target + 1):
#     if number % 2 == 0:
#         even_sum += number
# print(even_sum)

# FizzBuzz

for number in range(1, 16):
    if number % 3 == 0 and number % 5 == 0:
        number = "FizzBuzz"
    elif number % 3 == 0:
        number = "Fizz"
    elif number % 5 == 0:
        number = "Buzz"
    else:
        print(number)