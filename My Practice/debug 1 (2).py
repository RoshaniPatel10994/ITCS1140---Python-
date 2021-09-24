# Program:Debug #01# Due Date:     10/3/18# Programmer:   <your name># Description:  This program will track the number of calories burned after #               10, 15, 20, 25, and 30 minutes given that you burn 4.2 calories#               per minute.#               Note: It should not print calories burned after 5 minutes.
# Declare variables and constants
Counter = 5
CaloriesPerMinute = 4.2
TotalCalories = 0
# Get user input
Name = input("Enter your name: ")
# Calculate and display calories burned
print("\nHere are the calories burned for ", Name)
print("\nMinutes","Total Calories")
TotalCalories = TotalCalories + CaloriesPerMinute *10
print(Counter, "\t")
Counter = Counter
while Counter <= 30:
    TotalCalories = TotalCalories + CaloriesPerMinute * 5
    print(Counter, "\t", TotalCalories)
    Counter = Counter + 5
