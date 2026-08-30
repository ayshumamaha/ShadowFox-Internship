import random

words = ["python", "shadow", "internship", "coding"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    print("Guessed letters:", guessed_letters)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct guess!")
    else:
        attempts -= 1
        print("Incorrect guess!")

if "_" not in guessed:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
