#2/17/2020


# Accumulate 7 days worth of bug counts.

# Declare Variables

Bugs = 0
Days = 1
Total = 0

# Loop to accumulate 7 Days of bug Counts

while Days <= 7:
    Bugs = int(input(" Enter today's bug count: "))
    Total = Total + Bugs
    #print(locals())
    Days = Days + 1
    

# Display Total

print("Total: ", Total)
