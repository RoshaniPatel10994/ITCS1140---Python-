#Roshani patel
 # Variables
total = float()
bars = 1.5
gum = 0.75
licorice = 1.25
total = 0
answer = str()
C=str()
G=str()
L=str()

 # Start Loop
while answer != 'quit':
    candy = str(input("What kind of candy did you sell (C = Candy Bar, G = Gum, L = Licorice: "))
    amt = int(input("How many did you sell: "))
    if candy == 'C':
        subtotal = amt * bars
    elif candy == 'G':
        subtotal = amt * gum
    else:
        subtotal = amt * licorice
    # End loop
    # print out subtotal
    print("Your subtotal is: $", subtotal)
    total = total + subtotal
    
# Ask the user for Quit
    answer = input("Enter 'quit' to end the program: ")
# Print Out total
print("Your total is: $", total)

        
