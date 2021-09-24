# Patel Roshani
# InClassLabLists

# Def Main Module
def main():
    # Declare Variables
    NumHomes = 0
    AvgPrice = 0.0
    NumAbove = 0
    NumBelow = 0
    Prices  = [0.0]

    # Call GetInput
    NumHomes, Prices = GetInput()
    #Call CalAvg
    AvgPrice = CalcAvg(NumHomes, Prices)
    # Call CountAboveBelow
    NumAbove, NumBelow = CountAboveBelow(NumHomes, AvgPrice, Prices)
    # Call Display output
    DisplayOutput(AvgPrice, NumAbove, NumBelow)

# Define GetInput
def GetInput():
    NumHomes = int(input("Enter Number of homes sold:"))
    Prices =[0.0]* NumHomes
    for Index in range(0, NumHomes):
        Prices[Index] = float(input("Enter Prices: "))
        return NumHomes, Prices
    
# Define CalAvg
def CalcAvg(NumHomes, Prices):
    Total = 0.0
    for Index in range(0, NumHomes):
        Total = Total + Prices[Index]
    AvgPrice = Total/NumHomes
    return AvgPrice

# Define CountAboveBelow
def CountAboveBelow(NumHomes, AvgPrice, Prices):
    NumAbove = 0
    NumBelow = 0
    for Index in range(0, NumHomes):
        if Prices[Index] < AvgPrice:
            NumBelow = NumBelow + 1
        elif Prices[Index] > AvgPrice:
            NumAbove = NumAbove + 1
        return NumAbove, NumBelow

# Define Display Output
def DisplayOutput(AvgPrice, NumAbove, NumBelow):
    print("Average: $ ", format(AvgPrice, '.2f'))
    print("Number above : ", NumAbove)
    print("Number Below: ", NumBelow)

# Call main
main()
   
