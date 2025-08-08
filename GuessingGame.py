import random

print("Let's play a guessing game. You have three attempts.")

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
correct_number = random.choice(number_list)

attempts = 3

while attempts > 0:

    if attempts == 3:
        guess = int(input("\nInput first guess: (1-10)"))

        if guess == correct_number:
            print(f"\nYou won! The correct number was: {correct_number}")

            attempts = 0

        elif guess > correct_number:
            print("\nIncorrect! To high. Try again.")

        elif guess < correct_number:
            print("\nIncorrect! To low. Try again.")

    elif attempts == 2:
        guess = int(input("\nInput second guess: (1-10)"))

        if guess == correct_number:
            print(f"\nYou won! The correct number was: {correct_number}")

            attempts = 0

        elif guess > correct_number:
            print("\nIncorrect! To high. Try again.")

        elif guess < correct_number:
            print("\nIncorrect! To low. Try again.")

    elif attempts == 1:
        guess = int(input("\nInput third guess: (1-10)"))

        if guess == correct_number:
            print(f"\nYou won! The correct number was: {correct_number}")

            attempts = 0

        elif guess > correct_number:
            
            print(f"\nGame over! You ran out of guesses. The correct number was: {correct_number}")
                        
        else:
            print(f"\nGame over! You ran out of guesses. The correct number was: {correct_number}")
                        

    attempts -= 1
                        
                        
