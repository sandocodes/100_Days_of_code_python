# Day 24 - 100DaysOfPython
# Working with Files

# Read-only mode
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Write a number (70) at the end of a file
with open("my_file.txt", 'a') as file:
    file.write("\n70")
    # print(file.read())
