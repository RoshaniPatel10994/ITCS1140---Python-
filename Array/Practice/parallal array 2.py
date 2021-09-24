
def FindHighest(names, calls):
  maxIndex = 0
  for i in range (1, len(calls)):
    if calls[maxIndex] < calls[i]:
      maxIndex = i
      return names[maxIndex], calls[maxIndex]
  

def main():
    #variables
    names = ["Bob", "Mary", "Sue", "John", "Mike", "Becky"]
    calls = [20, 11, 15, 32, 17, 28]
  
    highest_name = str()
    highest_calls = int()

    highest_name, highest_calls = FindHighest(names, calls)
    print(highest_name, "\t", highest_calls)
main()
