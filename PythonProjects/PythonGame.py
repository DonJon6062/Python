import random
#function to get the user's name
userName = input("What is your first name? ")
    #with open("highscore.txt", "a") as file: 
        #file.write(highscore)

#welcome the user
print("Welcome", userName)
print("Please enjoy my game!")

#tells the user how good at gaming they are
def giveScore(wins, losses):
    return (wins*10) - (losses*5)

#how to win/lose
def enemyMove():
    return random.choice([True, False])

#how the game operates
def startGame():
    wins = 0
    losses = 0
    totalRounds = 10

#plays the game until 10 rounds are done
    for _ in range(totalRounds):
        print("Press Enter to play!")
        input()

        if enemyMove():
            print("You win!")
            wins += 1
        else:
            print("You lose! Better luck next time...")
            losses += 1

#gives score
    score = giveScore(wins, losses)
    print("Game Over")
    print(f"Your final score: {score}")
    print("Thanks for playing!")

results = "{userName}: {score}"
#lets player play again or end game
while True:
    startGame()
    response = input("Do you want to play again? (Yes/No) :")

    if response != "Yes":
        print ("Thanks for playing!")
        break

#def highScore(fileName, writeType)
