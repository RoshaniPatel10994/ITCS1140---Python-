#variables
numtriangles = int()
trianglesize = int()

# Ask the user
numtriangles = int(input("Enter the number of triangles:  "))
trianglesize = int(input("Enter the size of the triangles:  "))
# For loop
for triangles in range(0, numtriangles):
    for size in range(0, trianglesize):
        # print
        print('*' * size)
