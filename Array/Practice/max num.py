numbers = [1, 1,  1, 1,  2, 4, 1, 10]

# Your code goes here

largest = numbers[0]

for I in range (0,len(numbers)):
  if numbers[I] > largest:
      largest= I
  print(largest)
