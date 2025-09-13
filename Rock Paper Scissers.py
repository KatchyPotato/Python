import random

print("Rock, Paper, Scissors")

choices = ["Rock", "Paper", "Scissors"]

play = "Yes"

while play == "Yes":

    choice = input("\nInput Choice: (Rock, Paper, Scissors)")

    com_choice = random.choice(choices)

    if choice == com_choice:
        print(f"\nDRAW {choice}, {com_choice}")

    elif choice == "Rock":
        if com_choice == "Scissors":
            print(f"\nWIN {choice}, {com_choice}")
        elif com_choice == "Paper":
            print(f"\nLOSS {choice}, {com_choice}")

    elif choice == "Paper":
        if com_choice == "Rock":
            print(f"\nWIN {choice}, {com_choice}")
        elif com_choice == "Scissors":
            print(f"\nLOSS {choice}, {com_choice}")

    elif choice == "Scissors":
        if com_choice == "Paper":
            print(f"\nWIN {choice}, {com_choice}")
        elif com_choice == "Rock":
            print(f"\nLOSS {choice}, {com_choice}")
            
    play = input("\nWould you like to play again? (Yes, No)")
        


