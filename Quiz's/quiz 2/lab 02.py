#payroll
#Calculate Gross Pay given pay rate and time.


# Declare Variables
Interest = str()
Rate = float()
Principal = str()
Time = str()
FinalValue = ()


# Get Input
Principal = int(input("Enter principal: "))
Rate = float(input("Enter interesr rate: $"))
Time = int(input("Enter time of the years: "))

# Calculate Gross pay
Interest = Principal*Rate*Time
FinalValue = Principal+Interest

# Display Output
print("Interest: ", Interest)
print("FinalValue: $", format(FinalValue, '.2f'))
