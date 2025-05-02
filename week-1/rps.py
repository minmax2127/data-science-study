### RPS GAME ###

import random

print("Rock, Paper, Scissors Game")
print("For this game, you will be playing against the computer. Race to 3!")

winner = ""  # will store the winner of the game
playerScore = 0
computerScore = 0

while winner == "":
    # make player input their answer
    playerChoice = input("\n[r]ock, [p]aper, [s]cissors : ")

    if playerChoice == 'r':
        playerChoice = "Rock"
    elif playerChoice == 'p':
        playerChoice = "Paper"
    elif playerChoice == 's':
        playerChoice = "Scissors"

    # get random choice for the computer
    computerChoiceInt = random.randint(0, 2)
    computerChoice = ""

    if computerChoiceInt == 0:
        computerChoice = "Rock"
    elif computerChoiceInt == 1:
        computerChoice = "Paper"
    elif computerChoiceInt == 2:
        computerChoice = "Scissors"

    # decide who wins
    if playerChoice == computerChoice: # if same
        print("Both of you chose " + playerChoice + ". It's a tie!")
        continue
    else: # if different
        print("Player chose " + playerChoice + ". Computer chose " + computerChoice)
        if playerChoice == "Rock":
            if computerChoice == "Paper":
                print("You lose for this round!")
                computerScore += 1
            elif computerChoice == "Scissors":
                print("You win for this round!")
                playerScore += 1

        elif playerChoice == "Paper":
            if computerChoice == "Scissors":
                print("You lose for this round!")
                computerScore += 1
            elif computerChoice == "Rock":
                print("You win for this round!")
                playerScore += 1

        elif playerChoice == "Scissors":
            if computerChoice == "Rock":
                print("You lose for this round!")
                computerScore += 1
            elif computerChoice == "Paper":
                print("You win for this round!")
                playerScore += 1
            
    # display player and computer score per round
    print("Player: " + str(playerScore))
    print("Computer: " + str(computerScore))

    # determine if someone has already won
    if playerScore == 3 or computerScore == 3:
        if playerScore == 3:
            winner = "Player"
        else:
            winner = "Computer"

if winner == "Computer":
    print("\nSorry, you lost!")
else:
    print("\nCongratulations! You won!")
