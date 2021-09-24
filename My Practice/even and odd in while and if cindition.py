
# Variables
number = int()
# Get number from the users
number = int(input(" Enter the number (0 to quit ): "))
# Loop to get numbers
while number != 0:
    # Determine if odd and even
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
    number = int(input(" Enter the number (0 to quit ): "))
