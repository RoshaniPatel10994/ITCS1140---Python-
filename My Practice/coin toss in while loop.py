

import random

# Variable
coin = int()
heads = 1
tails = 1
Continue = int()
Toss = str()

# While loop with if and else stament
while Continue != "Q":
    Toss = str(input("Enter the type of coin (heads or tails):"))
    if Toss == 'heads':
        heads = heads + 1
        print("Toss:heads")
        print("Heads Win!")
        print("Continue:")
       
    else:
        tails = tails + 1
        print("Toss:tails")
        print("Tails Win!")
        print("Continue")
        
        # ask user to quit
    Continue = input("Continue: Q")
    
    #end loop
print("Heads score:", heads)
print("Tails score:", tails)







