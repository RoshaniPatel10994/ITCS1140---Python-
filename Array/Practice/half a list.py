def HalfList(numbers = []):
  total = 0
  length = int(len(numbers)/2)
  for I in range (0,length):
    total = total + numbers[I]
  return(total)

mytotal = int()
def main():
    mynumbers = [0] * 6
    mytotal = int()

    mynumbers = [6, 5, 7, 9, 4, 3,]
    mytotal = HalfList(mynumbers)
    print(mytotal)

main()
