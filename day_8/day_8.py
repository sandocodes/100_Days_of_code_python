# Function Parameters & Project: Caesar Cipher
# def greet():
#     print("Hello")
#     print("How are you?")
#     print("Have a nice day!")
# greet()

# def greet_with_name(name):
#     print(f"Hello, {name}")
#     print(f"How are you, {name}?")
#     print(f"Have a nice day, {name}!")
# greet_with_name("Billie")

# In programming, when we give a function a parameter, we are essentially creating a variable with the name of the parameter, with the value set to the argument that's passed to the function call. For example, in the greet_with_name function, the function has a parameter called name and an argument called "Billie". This is essentially equivalent to name = "Billie".

# Multiple Parameters to a function: A function can take any amount of parameters
def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")

# greet_with("Jack Bauer", "Boston") # ==> This is the default


# Keyword Arguments:
# greet_with(location="Boston", name="Jack Bauer")


# Test Code:
for i, j in enumerate(['bar', 'foo', 'bar', 'baz', 'bar']):
    if j == 'bar':
        print(i)