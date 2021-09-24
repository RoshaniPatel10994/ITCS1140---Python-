# 3/30/20
#Calculate the area of geometric figures


# Define Main
def main():
    #Declare variables
    Choice = ""
    Area = 0.0
    Choice = GetChoice()
    while Choice != "4":
        Choice = GetChoice()
        if Choice == "1":
            Area = CalcRectangle()
        elif  Choice == "2":
            Area = CalcTriangle()
        else:
            Area = CalCircle()
        printArea(Area)
        Choice = GetChoice()
        
# Define GetChoice
def GetChoice():
    print("\n1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Quit")
    Choice = input("Enter the number of your choice:  ")
    return Choice

# Define Calculate
def CalcRectangle():
    Lenth = float(input("Enter Lenth:  "))
    Width = float(input("Enter Width:  " ))
    Area = Lenth * Width
    return Area

# Define Triangle
def CalcTriangle():
    Base = float(input("Enter Base:  "))
    Height = float(input("Enter Height:  " ))
    Area = 0.5 * Base * Height
    return Area
    
# Define Circle
def CalCircle():
    pi = 3.14
    Radius = float(input("Enter Base: "))
    Area = pi * Radius**2
    return Area
    
# Define PrintArea
def printArea(inArea):
    print("Area: ",  inArea)
    return

#Call Main
main()






    
    
