#Variables
wing_type = str()
user = str()
quantity = int()
rate = float()
discount = float()
subtotal = float()
total = float()

#Loop to begin program
while user != 'Q':
    #ask user for quantity and type
    wing_type = input("Type:  ")
    quantity = int(input("Quantity:  "))
    #determining the rate
    if wing_type == "hot":
        if quantity <= 6:
            rate = 0
        elif quantity <= 12:
            rate = .1
        elif quantity <= 24:
            rate = .2
        else:
            rate = .25
    elif wing_type == "sour":
        if quantity <= 6:
            rate = .05
        elif quantity <= 12:
            rate = .1
        elif quantity <= 24:
            rate = .15
        else:
            rate = .25
    #end if
    #determine subtotal
    subtotal = quantity * .5
    discount = subtotal * rate
    total = subtotal - discount
    #print out values to the user
    print("Total:", total)
    #ask the user if they want another order
    user = input("Continue:  ")



    

#end loop

                        

