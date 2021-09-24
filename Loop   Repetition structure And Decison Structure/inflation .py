#Variables
inflated_price = float()
price = float()
years = int()

#Setting the inflation rate
inflation = 0.0223

#Getting inputs
price = float(input())
years = int(input())
inflated_price = float(intput())

#Your code goes here
for i in range(0,5):
    
  inflated_price = inflated_price * (1+inflation)
  
  print("inflated_price", inflated_price)
  
#Print out the inflated price
print(inflated_price)
