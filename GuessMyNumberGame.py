#This programm lets you guess a random number

import random
import sys

def guessMyNumber():
    secretNumber = random.randint (1,20)

    print("I have chosen a random number between 1 and 20. Can you guess it?")

    for userTry in range(1,7):
        userGuess = int(input("Guess number " +str(userTry) +"/6: " ))

        if userGuess < secretNumber:
            print("That's too low.")
        elif userGuess > secretNumber:
            print("That's too much.")
        else:
            break

    if userGuess == secretNumber: #The loop has ended.
        print ("Correct!. The random number is " + str(secretNumber)+".")
    else :
        print ("Sorry. The correct answer would have been " + str(secretNumber)+".")

#Programmteil
endStatement = "continue"
while endStatement == "continue":
    guessMyNumber()
    endStatement = input('Type "continue" to play again or anything else to quit.')
    
    if endStatement == "anything else":
        print("Very funny. Goodbye.")
        break
        sys.exit

    elif endStatement == "continue":
        continue

    else:
        break
        sys.exit
