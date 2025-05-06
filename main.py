import random

# List of 5-letter words
word_list = ["apple", "brick", "crane", "flame", "grape", "plant", "spear", "light"]

# Choose a random word from the list
word = random.choice(word_list)
attempts = 6

print("Welcome to Wordle!")
print("Guess the 5-letter word. You have 6 tries.\n")

def check_guess(secret, guess):
    result = ""
    for i in range(5):
        if guess[i] == secret[i]:
            result += guess[i].upper()  # Correct letter & position
        elif guess[i] in secret:
            result += guess[i].lower()  # Correct letter, wrong position
        else:
            result += "_"              # Wrong letter
    return result

for attempt in range(attempts):
    guess = input(f"Attempt {attempt + 1}: ").lower()
    
    if len(guess) != 5:
        print("Please enter a 5-letter word.\n")
        continue

    result = check_guess(word, guess)
    print("Result:", result)

    if guess == word:
        print("🎉 Congratulations! You guessed the word!")
        break
else:
    print(f"❌ Game over! The word was: {word}")
