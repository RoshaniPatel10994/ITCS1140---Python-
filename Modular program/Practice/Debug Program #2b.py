# Program:      Debug #03

# Programmer:   <Roshani Patel>
# Description:  This program will calculate the total sales for a week(7 days) using a list.

# Declare variables and constants
Index = int()
Sales = [0.0] * 7
Total = float()
Index = 0

# Get the sales from the user
for Index in range(0,7):
    Sales[Index] = float(input("Enter day's sales: "))

# Calculate the total sales
for Index in range(0,7):
    Index = 3
    Total = Total + Sales[Index]

# Display the total sales
print("Total sales: $", format(Total, '.2f'))

