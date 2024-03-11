# List Comprehension

# Without List Comprehension, add 1 to each item in a my_list = [1, 2, 3]
numbers = [1, 2, 3]
# new_list = []
# for item in numbers:
#     add_1 = item + 1
#     new_list.append(add_1)

# print(new_list)


# List Comprehension Syntax: new_list = [new_item for item in list]
second_list = [n + 1 for n in numbers]
# print(second_list)


# Square:
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)
