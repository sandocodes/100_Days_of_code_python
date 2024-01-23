from art import logo
import random, os



def guess_number():
    """Generates a random number for user to guess."""

    print(logo)
    print("Welcome to the Number Guesz")
    print("I'm thinking of a number between 1 and 100.")

    # Generate random number between 1 and 100:
    answer = random.randint(1, 101)
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts_left = 0

    # Set the game difficulty level
    if difficulty_level == "easy":
        attempts_left = 10
        print(f"You have {attempts_left} attempts to guess the number.")
    else:
        attempts_left = 5
        print(f"You have {attempts_left} attempts to guess the number.")

    
    is_game_over = False
    while not is_game_over and attempts_left != 0:
        user_guess = int(input("Make a guess: "))

        if user_guess == answer:
            is_game_over = True
            print(f"You got it! The answer was: {answer}.")
        elif user_guess > answer:
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

    # If the attempts left reaches 0, the user has run out of guesses
    if attempts_left == 0:
        print("You ran out of guesses, you lose.")

    # Ask the user if they want to play again. If yes, clear the screen and rerun the guess_number() function
    if input("Do you want to play again? Type 'yes' to continue and 'no' to exit: ") == "yes":
        # Clear the screen and run game again
        os.system("clear")
        guess_number()


guess_number()
