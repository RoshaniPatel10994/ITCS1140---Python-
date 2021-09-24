class GymMembership():
  #Constructor
  def __init__(self, n, type):
      self.nos = n
      self.type = type

  #find cost of membership based on type of membership
  def DetermineRate(self):
    if self.type == 'bronze':
      self.cost = 25
    if self.type == 'silver':
      self.cost = 35
    if self.type == 'gold':
      self.cost = 50
    if self.type == 'platinum':
      self.cost = 75

  #Method to determine total cost of nos memberships for a month
  def DetermineTotal(self):
    self.total = self.cost * self.nos

  #Method to return total cost for the membership for one year
  def ReturnTotal(self):
    return self.total*12


#Test above class
a = GymMembership(6, 'silver')
a.DetermineRate()
a.DetermineTotal()
print('Total cost of membership: $' + str(a.ReturnTotal()))
