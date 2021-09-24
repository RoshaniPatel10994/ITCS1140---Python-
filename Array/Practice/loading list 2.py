#Declare variables
Index = 0
OneScore = 0.0
#Declare the list to have 5 items in it
Scores=[0, 0, 0, 0, 0]
#Load the list with scores
for Index in range(0, 5):
    OneScore = float(input("Enter a test score:  "))
    Scores[Index] = OneScore
#end for
