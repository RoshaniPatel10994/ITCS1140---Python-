#write your function here
def GetAverage(num1, num2, num3):
    average = float()
    average = (num1 + num2 + num3) / 3
    return average;

#delcare variables
sales1 = float()
sales2 = float()
sales3 = float()
average = float()

#Get sales from the user
sales1 = float(input())
sales2 = float(input())
sales3 = float(input())

#write your code to call your function here
average = GetAverage(sales1, sales2, sales3)

#print out the average
print(str(average))
