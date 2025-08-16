import random
print("-Hangman-")

word_list = ["katchy", "python", "minecraft", "technoblade", "evit", "java", "c++", "c#", "hypixel"]
word = random.choice(word_list)

word_length = len(word)

correct_letters = []
incorrect_letters = []

guesses = 1

guess = "placeholder"

while guess != word and guesses < 21:
    print(f"\nWord Length: {word_length}")
    print(f"Correct Letters: {correct_letters}")
    print(f"Incorrect Leters: {incorrect_letters}")
    
    guess = input(f"\nInput Guess {guesses}: (Lowercase)")


    if guess in word:
        if guess != word:
            print(f"\n{guess} is in the Word")
            correct_letters.append(guess)
        elif guess == word:
            print(f"\nYou Guessed Correctly. Word Was: {word}")

    else:
        print(f"\n{guess} is not in the Word")
        incorrect_letters.append(guess)

    guesses += 1

if guesses == 20:
    print("\nGAME OVER You ran out of Guesses")
          
