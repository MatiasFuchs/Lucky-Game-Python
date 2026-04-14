import os
import random
from random import choice
from time import sleep

#BASE CODE
totalRounds = 5 #The amount of rounds
round = 1 #round going on
print("\nPosible numbers:\n")
posibleNumbers = [1,2,3,4,5,6]
print(posibleNumbers)
selectedNumber = int(input("\nSelect a number from the list above\n\n")) #USER SELECT NUMBER

#ROUNDS CODE
while round <= totalRounds:
    sleep(2)
    print("\n\nRound ", round)
    
    sleep(1)
    print("Posible numbers:")
    print(posibleNumbers)
    
    sleep(1)
    print("Selected number:", selectedNumber)
    
    sleep(2)
    randomNumber = random.choice(posibleNumbers) #tHE CODE SELECTS A RANDOM NUMBER TO DELETE IT FROM THE LIST
    print("Losing number", randomNumber)

    sleep(0.5)
    
    #WIN AND LOOSE CODE
    if selectedNumber == randomNumber: #IF THE NUMBER SELECTED RANDOMLY EQUALS TO THE NUMBER THAT THE USER SELECTED...
        print("\nYou lost\n")
        sleep(4)
        break
    else: #IF NOT
        #PASS TO THE NEXT ROUND
        posibleNumbers.remove(randomNumber)
        round += 1

if round == 6:
    print("YOU WON")
    
print("You made it to round ", round)
