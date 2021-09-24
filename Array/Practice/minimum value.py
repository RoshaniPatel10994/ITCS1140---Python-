def FindMin(numbers):
  Lowest = int()
  LowestIndex = int()
  Lowest = numbers[0]
  LowestIndex = 0
  for Index in range(len(numbers)):
    if numbers[Index] < Lowest:
      Lowest = numbers[Index]
      LowestIndex = Index
  return Lowest, LowestIndex
    
  

def main():
    #variables
    my_numbers = [22, 46, 78, 15, 98, 101]
    smallest_int = int()
    smallest_index = int()
    smallest_int, smallest_index = FindMin(my_numbers)
    print(smallest_int, "\t", smallest_index)

main()
