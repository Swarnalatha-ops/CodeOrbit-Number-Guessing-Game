import random

print("Welcome to the Number Guessing Game!")

while True:
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the number!")
                print("Number of attempts:", attempts)
                break

        except ValueError:
            print("Invalid input! Please enter a number.")

    play_again = input("Do you want to play another round? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break
