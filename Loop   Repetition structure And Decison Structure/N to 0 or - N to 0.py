#N to 0 or -N to 0
# This is a tricky challenge for you.

#We will pass in a value N. N can be positive or negative.

    #If N is positive then output all values from N down to and excluding 0.
    #If N is negative, then output every value from N up to and excluding 0.



N = 6
counter = 0
if N > 0:
    while counter < N:
        print(N - counter)
        counter = counter + 1
else:
    if N < 0:
        while counter < N:
            print(N - counter)
        couner = counter + 1
    
