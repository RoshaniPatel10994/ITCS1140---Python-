# Roshani Patel
# 2/10/20
# Chips


#Create small program that will determine how much money you will pay in taxes this year.
#If you earn less than $20,000 your tax is 0.
#Over $20,000 but under $100,000 your tax is 25% of your income.
#Over $100,000 but under $250,000 your tax is 35%.
#If you are over $250,000 your taxes are 45% of your total income.
#Make sure the program will prompt the user for their total income.
#It will then output the total tax (Income * Percentage)

# 
# Declare Variable
Rate = 0.0
TotalTax = 0.0
Income = 0.0

# Display Income
Income = float(input("Enter income: "))
              
# Calculate the COst
if Income < 20000:
    Rate = 0
elif Income < 100000:
    Rate= 0.25
elif Income < 250000:
    Rate = 0.35
else:
    Rate = 0.45

TotalTax = Income * Rate
    
# Display Total Taxes
print("Total Taxes: $",format(TotalTax, '.2f'))
























