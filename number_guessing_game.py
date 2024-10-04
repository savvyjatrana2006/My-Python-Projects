import random

# Constants
LOWER_LIMIT = 1
UPPER_LIMIT = 100
MAX_TRIES = 10

def number_guessing_game():
    # Generate a random number between LOWER_LIMIT and UPPER_LIMIT
    secret_number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    
    print(f"Welcome to the Number Guessing Game! I'm thinking of a number between {LOWER_LIMIT} and {UPPER_LIMIT}.")
    print(f"You have {MAX_TRIES} attempts to guess it correctly.\n")
    
    attempts = 0
    
    # Game loop
    while attempts < MAX_TRIES:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        attempts += 1
        
        if guess < LOWER_LIMIT or guess > UPPER_LIMIT:
            print(f"Your guess must be between {LOWER_LIMIT} and {UPPER_LIMIT}. Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.")
            break
    else:
        print(f"Sorry! You've used all {MAX_TRIES} attempts. The number was {secret_number}.")

# Run the game
number_guessing_game()
