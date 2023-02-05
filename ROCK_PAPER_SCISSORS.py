char = ["Rock","Paper","Scissors"]
import time
from random import randint
computer = char[randint(0,2)]
print(computer)
player = True
while player == True:
    playerc = input("Select one of the options- Rock, Paper or Scissors?")

    if playerc == computer:
        time.sleep(2)
        print("Its a Tie!!")

    elif playerc == "Rock":
        if computer == "Scissors":
            print("computer chooses ",computer)
            time.sleep(2)
            print("You WIN!!! ",playerc,"SMASHES ", computer)
        else:
            print("computer chooses", computer)
            time.sleep(2)
            print("You lose!" , computer,"Covers ",playerc)

    elif playerc == "Paper":
        if computer == "Rock":
            print("Computer chooses ", computer)
            time.sleep(2)#this tells the computer to wait for 2 seconds
            print("You WIN!!! ", playerc, "Covers ", computer)
        else:
            print("Computer chooses ", computer)
            time.sleep(2)
            print("You lose ", computer,"Cuts ",playerc)

    elif playerc == "Scissors":
        if computer == "Paper":
            print("Computer chooses ", computer)
            time.sleep(2)
            print("You WIN!!! ", playerc, "Cuts ", computer)
        else:
            print("Computer chooses ", computer)
            time.sleep(2)
            print("You lose ", computer,"Smashes ",playerc)
    else:
        print("Kindly enter a valid character, in the proper format also check your spelling!")

    player = True
    computer = char[randint(0,2)]


    


    



