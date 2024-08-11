import random
#Ideas
#Coin flips, Dice rolls (Multiple dice whatever num of sides)
#Enter names and draw like a raffle

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

raffleDraw(["Safari", "Jenny", "Mouse", "Jared", "Tommy"])
