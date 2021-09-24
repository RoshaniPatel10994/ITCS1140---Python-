

#3/23/20

# CALCULATE area of circle and sqaure fuction

# Define math

def main():
    # Declare variables
    Radius = 0.0
    Side = 0.0
    AreaCircle = 0.0
    AreaSquare = 0.0
    
    # Call the function = Radius, Side = GetInput()/ Argument pass here ()
    Radius, Side = GetInput()
    AreaCircle, AreaSquare = CalcAreas(Radius, Side)
    DisplayAreas(AreaCircle, AreaSquare)

# Define Getinput function (inradius because its is different variables, return will radius)
def GetInput():
    inRadius = float(input("Enter radius: "))
    inSide = float(input("Enter square side: "))
    return inRadius, inSide

# Define CalArea function (input RadiusIn, SideIn)

def CalcAreas(RadiusIn, SideIn):
    pi = 3.14
    CircleArea = pi * RadiusIn **2
    SquareArea = SideIn **2
    # Will return call function
    return CircleArea, SquareArea


# Define Display Areas
def DisplayAreas (disCircleArea, disSquareArea):
    print("Area of Circle: ", disCircleArea)
    print("Area of Square: ", disSquareArea)
    return

# call Main()
main()













    
    
    


















    
