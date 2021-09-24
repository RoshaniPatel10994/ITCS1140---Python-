
#2/24/2020
# Gaming
#Declare variable
import random

Number = int()
Guess = str()
UserContinue = "Yes"

# Loop to play a Game
while UserContinue == "Yes":
    Number = random.randint(1, 50)
    # Loop to get 3 Guesses
    for Counter in range(3):
        Guess = int(input("Enter your guess"))
        if Guess == Number:
            print("Congratulation you won")
            break
        elif Guess < Number:
            print("TOO Low")
        else:
            print("too high")
    print("The Number Was: " , Number)
    UserContinue = input(" Do you Play again? (yes/no)")
                
    
    

