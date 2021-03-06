#This file demos how functions are called and how we get values to return

import random


def GenerateRandomNumbers():
    #Declare local variables to GenerateRandomNumbers
    num1 = int()
    num2 = int()

    #notice the variables names and how they are different from those in main
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    #return both values
    #notice the order --- VERY important
    return num1, num2

def PrintNumbers(rand1, rand2): #notice the names of the parameters being different
                                #from the names of the arguments
    print()
    print("Value of Random Number 1:  ", rand1)
    print("VAlue of Random Number 2:  ", rand2)
    print()

    #notice no return.  Why?  thsi function doesn't return anything.  It just prints.

def GetTotal(rand1, rand2):
    #Declare local variable to GetTotal
    local_total = int()

    #Calculate the total
    local_total = rand1 + rand2

    #return the total
    return local_total

def main():
    #declare local variables to main
    mainRandom1 = int()
    mainRandom2 = int()
    mainTotal = int()

    mainRandomFirst = int()
    mainRandomSecond = int()
    mainTotal2 = int()

    #Calling GenerateRandomNumbers -- notice the order and how this is done
    mainRandom1, mainRandom2 = GenerateRandomNumbers()

    #Calling PrintNumbers
    PrintNumbers(mainRandom1, mainRandom2)

    #Calling GetTotal
    mainTotal = GetTotal(mainRandom1, mainRandom2)
    #Printing mainTotal
    print("The total for both numbers:  ", mainTotal)

    mainRandomFirst, mainRandomSecond = GenerateRandomNumbers()
    PrintNumbers(mainRandomFirst, mainRandomSecond)
    mainTotal2 = GetTotal(mainRandomFirst, mainRandomSecond)
    print("The total for both numbers (a second time):  ", mainTotal2)

    





main()
