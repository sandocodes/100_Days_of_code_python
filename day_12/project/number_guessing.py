from art import logo
import random, os



random_number = random.randint(1, 101)

# Generate random number between 1 and 100
# for _ in range(1, 101):

def play_game():
    """Start the number guessing game"""

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts_left = 0

    # Set difficulty level
    if difficulty_level == "easy":
        attempts_left = 10
        print(f"You have {attempts_left} attempts to guess the number.")
    else:
        attempts_left = 5
        print(f"You have {attempts_left} attempts to guess the number.")

    
    is_game_over = False
    while not is_game_over and attempts_left != 0:
        user_guess = int(input("Make a guess: "))

        if user_guess == random_number:
            is_game_over = True
            print(f"You got it! The answer was: {random_number}.")
        elif user_guess > random_number:
            attempts_left -= 1
            print("Too high.")
            if attempts_left > 0:
                print("Guess again.")
                print(f"You have {attempts_left} left.")
        else:
            attempts_left -= 1
            print("Too low.")
            if attempts_left > 0:
                print("Guess again.")
                print(f"You have {attempts_left} left.")

    if attempts_left == 0:
        print("You ran out of guesses, you lose.")

    if input("Do you want to continue? Type 'yes' to continue and 'no' to exit: ") == "yes":
        # Clear the screen and run game again
        os.system("clear")
        play_game()


play_game()
