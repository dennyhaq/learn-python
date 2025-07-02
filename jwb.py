import random

def get_chances(difficulty):
    if difficulty == '1':
        return 10  # Easy
    elif difficulty == '2':
        return 5   # Medium
    elif difficulty == '3':
        return 3   # Hard
    else:
        return None

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    difficulty = input("Enter your choice (1/2/3): ").strip()
    chances = get_chances(difficulty)

    if chances is None:
        print("Invalid difficulty level selected. Exiting the game.")
        return

    print(f"\nGreat! You have selected the {'Easy' if difficulty == '1' else 'Medium' if difficulty == '2' else 'Hard'} difficulty level.")
    print("Let's start the game!")

    target_number = random.randint(1, 100)
    attempts = 0

    while chances > 0:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess == target_number:
                print(f"🎉 Congratulations! You guessed the correct number in {attempts} attempts.")
                break
            elif guess < target_number:
                print("Incorrect! The number is greater than your guess.")
            else:
                print("Incorrect! The number is less than your guess.")
            
            chances -= 1
            if chances > 0:
                print(f"You have {chances} chance{'s' if chances != 1 else ''} left.")
            else:
                print(f"❌ You've run out of chances. The correct number was {target_number}. Better luck next time!")

        except ValueError:
            print("Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
