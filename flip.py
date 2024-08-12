import random
import sys
import string
#NEED
#main method

#Reads the commandline arguments are directs user to correct flow based on what they want
def readAndDirect():
    if len(sys.argv) < 2:
        print("You need to specify what action you would like in the commandline arguments \n Please use \"Dice\", \"Raffle\", or \"coin\" ")
    elif (sys.argv[1] == "Coin" or sys.argv[1] == "coin"):
        flipCoin()
    elif (sys.argv[1] == "Dice" or sys.argv[1] == "dice"):
        if(len(sys.argv)) < 4:
            checkDiceArg(-1,-1)
        checkDiceArg(sys.argv[2], sys.argv[3])
    elif (sys.argv[1] == "Raffle" or sys.argv[1] == "raffle"):
        if(len(sys.argv) < 3):
            print("Your list argument is empty, please provide a list of choices separated by commas with no spaces")
            exit()
        checkRaffleArg(sys.argv[2])
    elif (sys.argv[1] == "help" or sys.argv[1] == "Help"):
        printHelp()
        exit()
    else:
        print("You need to provide a valid command line argument, Please use \"Dice\", \"Raffle\", or \"coin\"")

def printHelp():
    print("Flip.py is a simple commandline application that allows the user to simulate coin flips, dice rolls, and raffle drawinss")
    print("The program works by passing in commandline arguments when running the application")
    print("The first argument should be a selection, either \"coin\", \"dice\", \"raffle\"")
    print("If you choose dice, then it should be followed by two positive integers representing the number of dice to roll and the number of sides on the dice")
    print("If you choose raffle please follow it with a comma separated list of choices to be in the raffle, make sure to use no spaces")
    print("If you choose coin no further arguments are needed")
    print("For more info please see the readme")
def isInt(someString):
    try:
        int(someString)
    except ValueError:
        return False
    else:
        return True

def checkRaffleArg(listOfChoices):
    if (listOfChoices.isspace()):
        print("The list argument is empty, please provide a list of choices separated by commas and no spaces")
    raffleDraw(listOfChoices.split(","))        

#Checks Dice argument for formatting and calls function if valid
def checkDiceArg(diceArg1, diceArg2):
    #Check if its even an int
    if(not isInt(diceArg1) or not isInt(diceArg2)):
        print("The arguments must be integers")
        exit()
    #Check if args are negative
    if(int(diceArg1) < 0 or int(diceArg2) < 0):
        print("The arguments must be positive")
        exit()
    #Check if args were missing
    if (int(diceArg1) == -1 or int(diceArg2) == -1):
        print("You need to provide two arguments after \"Dice\", the number of dice you wish to roll, and the number of sides you want on the dice")
        exit()
    #Check if either arg = 0
    if (int(diceArg1) == 0 or int(diceArg2) == 0):
        print("Both values must be greater then 0")
        exit()
    #Check if args are too big
    if (int(diceArg1) > 10000 or int(diceArg2) > 10000):
        print("Both values must be under 10,000")
        exit()
    #It it makes it thorugh tests, call the dice function with args
    rollDie(int(diceArg1),int(diceArg2))

#Prints the result of a coin flip
def flipCoin():
    randomValue = random.randint(0,1)
    if (randomValue == 0):
        print("Heads")
    else:
        print("Tails")

#Generates dice rolls according to parameters
def rollDie(diceNum, sideNum):
    results = []
    for x in range(diceNum):
        results.append(random.randint(1,sideNum))
    print("Rolling " + str(diceNum) + " dies with " + str(sideNum) + " sides on each die")
    printDiceResults(results)
    
#Formats and prints results of a dice roll
def printDiceResults(results):
    resultString = ""
    for index in range(len(results)):
        resultString += str(results[index])
        if not index == len(results) - 1:
            resultString += ", "
    print(resultString)

#Takes a list of names and randomly selects and prints one
def raffleDraw(listOfNames):
    winningNum = random.randint(0, len(listOfNames) - 1)
    print("The winner is " + listOfNames[winningNum])

#raffleDraw(["Safari", "Jenny", "Mouse", "Jared", "Tommy"])
readAndDirect()