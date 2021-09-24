
#  Declare variables
week_total = 0.0
month_total = 0.0
daily_sales = 0.0



#For loop to get 4 weeks of days
for week in range(1, 5):
    #Loop to get 7 days of data
    for days in range(1, 8):
        daily_sales = float(input("Enter sals amount: "))
        week_total = week_total+daily_sales
    print("Week_total - $", format(week_total, '.2f'))
    month_total += week_total
    week_total = 0.0
print("Month Total - $", month_total)


                
    
