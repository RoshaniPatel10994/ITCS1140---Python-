def GetTotal(price, pounds, ounces):
    #variables
    total = float()
    
    total = price * (pounds + ounces/16)
    total = round(total, 2)
    return total

Price = float()
Pounds = float()
Ounces = float()

Price = float(input())
Pounds = float(input())
Ounces = float(input())

newgettotal = GetTotal(Price, Pounds, Ounces)
#return total
print(newgettotal)

