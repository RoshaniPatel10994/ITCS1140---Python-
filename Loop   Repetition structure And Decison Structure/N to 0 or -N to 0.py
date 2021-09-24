N = 6
count = 0

count = 0 


if N>0:
  while count<=N:
    if (N-count)>0:
      print(N-count)
    count = count+1
else:
  while count>=N:
    if (N-count)<0:
      print(N-count)
    count = count-1
