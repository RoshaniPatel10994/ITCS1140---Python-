DogDay class():
Class DogDay:
    #initialize DogDay object
    def __init__(self, quantity, size):
           self.quantity = quantity
           self.size = size
      #Determine price of each bone based on size
  def DeterminePrice(self):
    if (self.size == 'A'):
      self.price = 2.29
    elif (self.size == 'B'):
      self.price = 3.50
    elif (self.size == 'C'):
      self.price = 4.95
    elif (self.size == 'D'):
      self.price = 7.00
    else:
      self.price = 9.95
      
    #determine the total cost
    def DetermineTotal(self):
      self.total = round(self.quantity*self.price, 2)
  
    #return the total cost
    def ReturnTotal(self):
      return self.total


# Testing class
myDog = DogDay(6, 'C')
myDog.DeterminePrice()
myDog.DetermineTotal()
print(str(myDog.ReturnTotal()))
