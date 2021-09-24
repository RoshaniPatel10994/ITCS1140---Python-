#Write a program that will price and order after allowing the user to select
#an item from a name.

#Means:

#1. Hamburger = 9.99
#2. Cobb Salad = 5.99
#3. Steak = 12.99

# Declare Variables
Item = int()
price = float()
Cost = float()
#Print
print("1 = hamburger $9.99")
print("2 = cobb salad $5.99")
print("3 = steak $12.99")
# Ask the user
Item = int(input(" Enter a Item List: "))

# If and else statement 
if Item == 1:
    price = 9.99
elif Item == 2:
    price = 5.99
elif Item == 3:
    price = 12.99
else:
    print("wrong selected")

# Calculation
Cost = price * 1.06
#Print
print("Cost: $",format(Cost, '.2f'))













