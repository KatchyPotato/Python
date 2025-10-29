import random
print("-Hangman-")

word_list = [
    "apple", "banana", "orange", "grape", "peach", "cherry", "lemon", "lime", "mango", "pear",
    "table", "chair", "window", "door", "floor", "ceiling", "wall", "roof", "garden", "fence",
    "river", "mountain", "ocean", "desert", "forest", "valley", "island", "beach", "hill", "cave",
    "dog", "cat", "horse", "tiger", "lion", "bear", "snake", "rabbit", "mouse", "sheep",
    "school", "teacher", "student", "pencil", "paper", "book", "eraser", "desk", "backpack", "ruler",
    "car", "truck", "bus", "train", "airplane", "bicycle", "boat", "scooter", "subway", "taxi",
    "music", "guitar", "piano", "violin", "drum", "trumpet", "flute", "song", "dance", "movie",
    "summer", "winter", "spring", "autumn", "rain", "snow", "wind", "storm", "cloud", "sun",
    "computer", "phone", "camera", "television", "radio", "light", "clock", "watch", "mirror", "bottle",
    "bread", "cheese", "butter", "milk", "coffee", "tea", "sugar", "salt", "pepper", "honey"
]

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
          
