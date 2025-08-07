import random

print("Let's play a guessing game. You have three attempts")
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
correct_number = random.choice(number_list)

attempt1 = int(input("\nInput first guess: (1-10)"))
if attempt1 == correct_number:
    print(f"\nYou won! The correct number was: {correct_number}")

elif attempt1 > correct_number:
    print("\nIncorrect! To high. Try again.")
    attempt2 = int(input("\nInput second guess: (1-10)"))

    if attempt2 == correct_number:
        print(f"\nYou won! The correct number was: {correct_number}")

    elif attempt2 > correct_number:
        print("\nIncorrect! To high. Try again.")
        attempt3 = int(input("\nInput third guess: (1-10"))

        if attempt3 == correct_number:
            print(f"\nYou won! The correct number was: {correct_number}")

        elif attempt3 > correct_number:
            print(f"\nIncorrect! Game over. You ran out of guesses. The number was: {correct_number}")

        elif attempt3 < correct_number:
            print(f"\nIncorrect! Game over. You ran out of guesses. The number was: {correct_number}")



                

        elif attempt2 < correct_number:
            print("\nIncorrect! To low. Try again.")
            attempt3 = int(input("\nInput third guess: (1-10"))

            if attempt3 == correct_number:
                print(f"\nYou won! The correct number was: {correct_number}")
                    
            elif attempt3 > correct_number:
                print(f"\nIncorrect! Game over. You ran out of guesses. The number was: {correct_number}")

            elif attempt3 < correct_number:
                print(f"\nIncorrect! Game over. You ran out of guesses. The number was: {correct_number}")


                
                

               




elif attempt1 < correct_number:
    print("\nIncorrect! To low. Try again.")
    attempt2 = int(input("\nInput second guess: (1-10)"))

    if attempt2 == correct_number:
        print(f"\nYou won! The correct number was: {correct_number}")

    elif attempt2 > correct_number:
        print("\nIncorrect! To high. Try again.")
        attempt3 = int(input("\nInput third guess: (1-10"))
        if attempt3 == correct_number:
            print(f"\nYou won! The correct number was: {correct_number}")

        elif attempt3 > correct_number:
            print("f\nIncorrect! Game over. You ran out of guesses. The number was: {correct_number}")




        elif attempt2 < correct_number:
            print("\nIncorrect! To low. Try again.")
            attempt3 = int(input("\nInput third guess: (1-10"))
            if attempt3 == correct_number:
                print(f"\nYou won! The correct number was: {correct_number}")

            elif attempt3 > correct_number:
                print("f\nIncorrect! Game over. You ran out of guesses. The number was:{correct_number}")
            else:
                print("f\nIncorrect! Game over. You ran out of guesses. The number was:{correct_number}")





            
            
