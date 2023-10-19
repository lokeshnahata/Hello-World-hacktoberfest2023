import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Set the range for the random number
    lower_limit = 1
    upper_limit = 100
    secret_number = random.randint(lower_limit, upper_limit)
    
    attempts = 0

    while True:
        # Get the player's guess
        guess = int(input(f"Guess the number between {lower_limit} and {upper_limit}: "))
        
        # Increment the attempts
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    number_guessing_game()
