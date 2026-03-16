import random

print("Welcome to the Number Guessing Game!")

playing = True

while playing:
    number_to_guess = random.randint(1, 50)

    print("\nSelect difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")

    level_choice = input("Enter 1, 2, or 3: ")

    if level_choice == "1":
        max_attempts = 10
    elif level_choice == "2":
        max_attempts = 7
    elif level_choice == "3":
        max_attempts = 5
    else:
        print("Invalid choice, defaulting to Easy")
        max_attempts = 10

    print(f"\nI have picked a number between 1 and 50. You have {max_attempts} attempts!")

    attempts = 0
    guessed = False

    while attempts < max_attempts and not guessed:
        guess = input("Enter your guess (or 0 to quit): ")

        if guess == "0":
            print("Quitting the game.")
            break

        if guess.isdigit():
            guess = int(guess)
            attempts += 1

            if guess == number_to_guess:
                print(f" Correct! You guessed it in {attempts} attempts.")
                guessed = True
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        else:
            print("Please enter a valid integer.")

    if not guessed and guess != "0":
        print(f" You ran out of attempts! The number was {number_to_guess}.")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        playing = False

print("Thanks for playing! Goodbye.")