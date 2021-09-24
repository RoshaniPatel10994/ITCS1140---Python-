
Name = ""
DailyCookies = 0
WeeklyCookies = 0
Days = 0
Goal = 0
GoalDifference = 0
price = ""
Name = str(input("Enter your name: "))
Goal = int(input("Enter your goal for selling cookies:  "))

while Days <7:

    DailyCookies = int(input("Enter the amount of cookies you sold today: "))
    WeeklyCookies = WeeklyCookies + DailyCookies
    Days = Days +1

GoalDifference = WeeklyCookies - Goal
                    
if GoalDifference <= 0:
    prize = "nothing"
elif GoalDifference < 5:
    prize = "mouse pad"
elif GoalDifference < 10:
    prize = "Starbucks $10 Gift Card"
elif GoalDifference < 25:
    prize = "iTunes $25 Gift Card"
else:
    prize = "Movie Packet"


print("You sold ", WeeklyCookies, "cookies this week")
print("The difference between what you sold and your goal is ", GoalDifference)
print("Your prize for going over your goal is ", prize)

