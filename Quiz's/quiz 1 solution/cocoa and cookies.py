# Declare Variables
firstname = str()
lastname = str()
namecocoa = int()
numcookies = int()
total = float()

# Get the name and Quantities from user
firstname = input("Enter the first name: ")
lastname = input("Enter the last name: ")
namecocoa = int(input("Enter the number of the hot cocoas: "))
namecokies = int(input("Enter the number of cookies: "))

# Calculate the total and concatenate the name

name = firstname + " " + lastname
total = (numcookies * 2.00) + (namecocoa * 2.50)

# print out name total to the user
print(" Customer Name: " , name)
print(" Order Total: " , total)
