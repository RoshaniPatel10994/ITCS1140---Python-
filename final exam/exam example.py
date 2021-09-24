

# For loop
def LoadLists():
    sales = [0]*12
    one_sale = float()
    for index in range (0, len(sales)):
        one_sale = float(input("Enter monthly sales: "))
        sales[index]=one_sale
    return sales

#Determine Total
def DetermineTotal(sales):
    one_sale = float()
    total  = float()
    for index in range (0, len(sales)):
        one_sale = sales[index]
        total = total + one_sale
    return total

#Determine Average
def DetermineAverage(total):
    average = float()
    average = total/12
    return average

#FindHighest
def FindHighest(sales):
    high = float()
    one_sale = float()
    for index in range (0, len(sales)):
        one_sale = sales[index]
        if one_sale >high:
            high = one_sale
    return high

def FindLowest(sales):
    low = float()
    one_sale = float()
    low = sales[0]
    for index in range (0, len(sales)):
        one_sale = sales[index]
        if one_sale < low:
            low = one_sale
    return low

# Call main
def main():
    monthly_sales = [0]*12
    total_sales = float()
    average_sales = float()
    high_sales = float()
    low_sales = float()
    monthly_sales = LoadLists()
    total_sales = DetermineTotal(monthly_sales)
    average_sales = DetermineAverage(total_sales)
    high_sales = FindHighest(monthly_sales)
    low_sales = FindLowest(monthly_sales)

    #Print
    print("Total sales: ", total_sales)
    print("Average sales: ", average_sales)
    print("Highest sales: ", high_sales)
    print("Lowest sales: ", low_sales)

main()
