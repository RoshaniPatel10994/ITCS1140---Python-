#Parallal array list

colors = ["red", "blue", "yellow", "black", "green", "brown"]
index = int()

search_item = str()
found = False

# Ask the user for an item to search on
search_item = input("Enter the color to search for : ")
months = [" Dec", "Jan", "Feb", "Mar"]
snowfall = [7, 13, 15, 6]
highest = float()
highest_index = int()
index = int()
lowest = float()
lowest_index = int()

lowest = snowfall[0]
highest = snowfall[0]
for index in range(0, len(months)):
    if snowfall[index] > highest:
        highest = snowfall[index]
        highest_index = index
    # end if
# end for
print()
print(" Highest snowfall : ", highest)
print(" Highest month : ", months[highest_index])

for index in range(0, len(months)):
    if snowfall[index] < lowest:
        lowest = snowfall[index]
        lowest_index = index
    #end if
#end for
print()
print("Lowest snowfall; ", lowest)
print("lowest months : " ,months[lowest_index])

 #Using python function and methodes
 #Searching

if search_item in colors:
    print("We found your item: ")
else:
    print("Sorry we did not found your item : " )
    
 #Sorting (), reverse(), sort(reverse - true)

print()
print(" List before any sorting : " )
print(colors)
colors.sort()
print(" Listafter any sorting : " )
print(colors)
colors = ["red", "blue", "yellow", "black", "green", "brown"]
print()
print("using reverse: ")
colors.reverse()
print("after reverse: ")
print(colors)

 #Reset colors
colors = colors = ["red", "blue", "yellow", "black", "green", "brown"]
print()
print(" Using sort with reverse = True ")
colors.sort(reverse = True)
print(colors)



















