
# 3/9/2020
# Product
# Multiply 2 number together using python fuctions


# Define Main module
def main():
    # Declare variables
    x = 0.0
    y = 0.0
    Answer = 0.0
    # Call GetInput function
    X, Y = GetInput()
    # Call CalProduct function
    Answer = CalcProduct(X, Y)
    # Calculate DisplayProduct function
    DisplayProduct(Answer)
# Define GetInput function
def GetInput():
    X = float(input("Enter 1st number: "))
    Y = float(input("Enter 2st number: "))
    return X, Y
# Define CalProduct function
def CalcProduct(inX, inY):
    Answer = inX * inY
    return Answer
# Define DisplayProduct function
def DisplayProduct(inAnswer):
    print("Product is: ", inAnswer)
    return
# Call main
main()
              
    

