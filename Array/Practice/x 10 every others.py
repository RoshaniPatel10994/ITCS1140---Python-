list = [1,  2, 3 ,4 , 5, 6, 2, 7]
n = 7
m = 2

for i in range (n-1 , len(list) , n):
    list[i] = list[i] *m
print(list)
    
