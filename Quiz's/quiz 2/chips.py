# Roshani Patel
# 2/10/20
# Chips
# This program Calculate the cost of an order of chips.

# Display program that will ask user how many bags of chips they want to buy.
#In addition ask the user what size of bag.
#If the bag is 8 oz the cost is 1.29 dollar if the bag is 16 oz then the cost is 3.59 dollars.
#If bag is 32 oz then cost is $5.50. calculate the total cost of the order including tax at 6%.

## Declare Variable
Size = 0
Qty = 0
Price = 0.0
Cost = 0.0

# Display Menu
print("1 - 8 oz\t$1.29")
print("2 - 16 oz\t$3.59")
print("3 - 32 0z\t$5.50")


# Bet Input
Size = int(input("Enter size: "))
if Size == 1 or Size == 2 or Size == 3:
    Qty = int(input("Enter quantity: "))


# Calculate the COst
if Size == 1:
    Price = 1.29
elif Size == 2:
    Price = 3.59
elif Size == 3:
    Price = 5.50
else:
    print("Enter 1, 2, or 3")


Cost = Price * Qty * 1.06

# Display Cost
print("Cost = $",format(Cost, '.2f'))








          
