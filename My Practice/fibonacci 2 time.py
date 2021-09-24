
# Variables
N = 10
count = 0
fib = 0
Next = 1
current = 0

# For loop
for i in range(0, N+1):
    print(fib)
    fib = Next + current
    Next = current
    current = fib
    count = count+1
    
    
    
