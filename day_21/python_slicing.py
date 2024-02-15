piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5])
# Answer: ['c', 'd', 'e'] ---> Find everything from index 2 to 5(not included)

print(piano_keys[2:])
# Answer: ['c', 'd', 'e', 'f', 'g'] ---> Find everything from index 2

print(piano_keys[-2:])
# Answer: ['f', 'g']

print(piano_keys[:-2])
# Answer: ['a', 'b', 'c', 'd', 'e'] ---> Find everything from the beginning index (0) to -2 index ("f" - not included)


# In Python, we can also specify the number of increment in the slicing. E.g. [2:5:2]
# The 2nd "2" is the number of increment
# For example:
print(piano_keys[2:5:2])
# Answer: ['c', 'e'] ---> Find everything from index 2 to 5(not included) but increment by 2. Meaning,
# start from index 2, count two indices and print the next ['c', skip 'd', and 'e']

print(piano_keys[::2])
# Answer: ["a", "c", "e", "g"] ---> Find everything in the list but skip every second item

print(piano_keys[::-1])
# Answer: ['g', 'f', 'e', 'd', 'c', 'b', 'a'] ---> Find everything in the list starting from the end

