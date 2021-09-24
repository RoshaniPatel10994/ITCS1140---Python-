# Variables
inches = float()
total_inches = float()
# For loop
for months in range(1, 5):
    inches = float(input("How many inches of snow fell this month:  "))
    
    total_inches = total_inches + inches
#end for
print("Total inches of snow this winter:  ", total_inches)
