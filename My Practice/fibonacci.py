
# Variables
N = 10
counter = 0
Next = 1
current = 0
fib = 0
# Forloop
for i in range(0, N+1):
    print(fib)
    fib = Next + current
    Next = current
    current = fib
    counter= counter + 1
