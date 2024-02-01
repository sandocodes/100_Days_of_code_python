from password import Password


# User inputs
letters_count = int(input("How many letters?: "))
symbols_count = int(input("How many symbols?: "))
numbers_count = int(input("How many numbers?: "))

# New Password Instance
new_password = Password().generate_password(letters_count, symbols_count, numbers_count)

# Print the new password
print(f"Your new password is: {new_password}")
