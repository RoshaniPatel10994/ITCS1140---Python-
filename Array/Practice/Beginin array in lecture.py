# Create a program that will allow the user to keep track of snowfall over the course 5 months.
# The program will ask what the snowfall was for each week of each month ans produce a total number
# of inches and average. It will also print out the snowfall values and list the highest amount of snow and the lowest amount of snow.

# Declare variables
snowfall = [0,0,0,0,0]
index = int()
one_month = float()
total_inches = float()
ave_inches =  float()
highest_inches = float()
lowest_inches = float()
##
#For loop
##for index in range(0, 5):
##    #ask use for months snowfall
##    one_month = float(input("Enter months of snowfall: "))
##    snowfall[index] = one_month
##print()

snowfall = [10, 12, 14, 16, 18]

for index in range(0, len(snowfall)):
    one_month = snowfall[index]
    print("Monthly snow fall : ", one_month)
print()
# Determin the total inches of snow fall
for index in range(0, len(snowfall)):
    one_month = snowfall[index]
    total_inches = total_inches + one_month
    
print(" total snowfall : ",  total_inches)

# average snowfall
ave_inches = total_inches / (index + 1)
print("Average snowfall: - " , ave_inches )

# Determine heighest value
highest_inches = snowfall[0]
for index in range(0, len(snowfall)):
    one_month = snowfall[index]
    if one_month > highest_inches :
        highest_inches = one_month
    #endif
print("highest snowfall: - " , highest_inches )


# Determine Lowest value
lowest_inches = snowfall[0]
for index in range(0, len(snowfall)):
    one_month = snowfall[index]
    if one_month < lowest_inches :
        lowest_inches = one_month
print("lowest snowfall: - " , lowest_inches )

































    


















    

