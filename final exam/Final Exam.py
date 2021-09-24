#Define main
def main():
    #sales array from Professor
    SalesData=[2010.45,5500.00,1170.65, 550.25, 50.95,3650.45]
    #Print space
    print()
    #Call PrintSales
    sales = PrintSales(SalesData)
    print()
    #Find profit
    profit = DetermineProfits(SalesData)
   #Print space
    print()
    #Find lowest sale
    lowestsale = FindLowestSale(SalesData)
    print("Lowest Sales: $","{:,.2f}".format(lowestsale))

#Define PrintSales function
def PrintSales(sales = []):
    #Print wording and star
    print("Sales by Store")
    print("**************************")
    #Loop to print sales data and format
    SalesData=sales
    for i in range(0,len(SalesData)):
        print("$", "{:,.2f}".format(SalesData[i]))
        
#Define DetermineProfits function
def DetermineProfits(sales2 = []):
    #Print word and star
    print("Store Profit Amounts")
    print("**************************")
    salesdata2=sales2
    #Loop to print sale * 0.2
    for i in range(0,len(salesdata2)):
        profit = salesdata2[i]*0.2
        print("$", "{:,.2f}".format(profit))

#Define FindLowest Sale
def FindLowestSale(sales3 = []):
    salesdata3=sales3
    #Define lowest variable
    lowest = salesdata3[0]
    #Loop to compare lowest to next element and find lowest
    for i in range(0,len(salesdata3)):
        if lowest > salesdata3[i]:
            lowest = salesdata3[i]
    return lowest
    
#Call main function
main()

