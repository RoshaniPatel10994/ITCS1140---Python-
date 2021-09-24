# 3/30/20
# Steve Christ
# GeometricAreas
# Calculate the areas of geometric figures

# Define Main
def main():
    # Declare variables
    Choice = ""
    Area = 0.0
    Choice = GetChoice()
    while Choice != "4":
        if Choice == "1":
            Area = CalcRectangle()
        elif Choice == "2":
            Area = CalcTriangle()
        else:
            Area = CalcCircle()
        PrintArea(Area)
        Choice = GetChoice()
# Define GetChoice
def GetChoice():
    print("\n1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Quit")
    Choice = input("Enter the number of your choice: ")
    return Choice
# Define CalcRectangle
def CalcRectangle():
    Length = float(input("Enter length: "))
    Width = float(input("Enter width: "))
    Area = Length * Width
    return Area
# Define CalcTriangle
def CalcTriangle():
    Base = float(input("Enter base: "))
    Height = float(input("Enter Height: "))
    Area = 0.5 * Base * Height
    return Area
# Define CalcCircle
def CalcCircle():
    Pi = 3.14
    Radius = float(input("Enter radius: "))
    Area = Pi * Radius **2
    return Area
# Define PrintArea
def PrintArea(inArea):
    print("Area: ", inArea)
    return


# Call Main
main()

    
           
