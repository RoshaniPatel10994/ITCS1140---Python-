#Main function with array and call other function
def candy():
  candy = [23,17,18,31,35]
  total = GetTotal(candy)
  print("Total Number of Boxes Sold:", total)
  average = GetAverage(total,len(candy))
  print("Average Number of Boxes Sold:", average)


#Calculate total using loop 
def GetTotal(candy=[]):
  total = 0
  for i in range (0,len(candy)):
    total = total + candy[i]
  return total


#Return average. Total from GetTotal length from len() function
def GetAverage(total,length):
  average = total/length
  return average

#Runs candy program

candy()
