import random

# Function to check the guess against the target word and provide feedback

#on request to fix the first code, gave a far more accurate right/wrong code
def check_guess(target, guess):
    feedback = ''
    for i in range(len(target)):
        if guess[i] == target[i]:
            feedback += guess[i].upper()  # Correct letter in correct position
        elif guess[i] in target:
            feedback += '+'  # Correct letter, wrong position
        else:
            feedback += '-'  # Incorrect letter
    return feedback

# Main function to run the game
def wordle():
    words = ["hello", "world", "tiger", "stoat", "apple", "crane", "sweet", "table", "chair", "house"]
    target_word = random.choice(words)
    guesses_left = 6
    guessed_words = []

    print("Welcome to Wordle!")
    #some custom print statements to explain how the game works
    print("Guess a five letter word. ")
    print("A plus means right letter, wrong placement. ")
    print("A minus is wrong letter overall. ")
    print("A letter being displayed means right letter, right placement. ")
    #end of my code
    print("Guess the word in 6 attempts. Good luck!")

    while guesses_left > 0:
        print("\nGuesses left:", guesses_left)
        guess = input("Enter your guess: ").lower()

        if guess == target_word:
            print("Congratulations! You've guessed the word:", target_word)
            break

        if guess in guessed_words:
            print("You already guessed that word. Try another one.")
            continue

        feedback = check_guess(target_word, guess)
        guessed_words.append(guess)

        print("Feedback:", feedback)

        guesses_left -= 1

    if guesses_left == 0:
        print("You're out of guesses! The word was:", target_word)

# Run the game
if __name__ == "__main__":
    wordle()

("Original starter code, placed wrong letters as right or wrong while guessing. ")
#def check_guess(target, guess):
    #feedback = ''
    #for i in range(len(target)):
        #if guess[i] == target[i]:
            #feedback += guess[i].upper()  # Correct letter in correct position
        #elif guess[i] in target:
            #feedback += guess[i]  # Correct letter, wrong position
        #else:
            #feedback += '-'  # Incorrect letter
    #return feedback