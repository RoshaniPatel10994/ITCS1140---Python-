#Variables
user_months = int()
user_weeks = int()
money = float()
month_total = float()
total_money = float()

for months in range(1, 6):
    for weeks in range(1, 4):
        money = float(input("Enter your weekly savings:  $"))
        month_total = month_total + money
    #end loop
    print("Total saved this month:  $", month_total)
    total_money = total_money + month_total
    print("Your saved overall:  $", total_money)
    month_total = 0
#end 
