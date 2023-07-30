import random

def get_random_word():
    words = ["apple", "banana", "cherry", "orange", "grape", "lemon", "melon", "strawberry", "watermelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    MAX_TRIES = 6
    word_to_guess = get_random_word()
    guessed_letters = []
    attempts = 0

    print("Welcome to Hangman!")
    print("You need to guess a word. Each '_' represents a letter.")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            attempts += 1
            print("Incorrect guess!")

        print(display_word(word_to_guess, guessed_letters))

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

        if attempts >= MAX_TRIES:
            print("Game over! The word was:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()
