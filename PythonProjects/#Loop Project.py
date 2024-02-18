#Loop Project
#import random library
import random

#create function for the game
def theGame():
    #get a random #
    secretNum = random.randint(1, 50)

    #var to hold user's guess
    guess = 0

    #var for # of tries
    attempts = 0

    while guess != secretNum:
        guess = int(input("Pick a number between 1 and 50: "))  
        attempts += 1

        if guess < secretNum: 
            print("Try higher! ")

        elif guess > secretNum:
            print("Close! try going lower. ")
        
        else:
            print(f"Great job! You guessed {secretNum} in {attempts} tries!")

while True:
    #the game function
    theGame()

    #ask user to play again
    playAgain = input("Play Again? (Y or N?) ")

    #go back
    if playAgain == 'Y':
        continue

    #end game
    elif playAgain == 'N':
        print("Thanks for playing! ")
        break

    #catchall
    else:
        print("Please type one of those nifty letters in the parenthases! ")