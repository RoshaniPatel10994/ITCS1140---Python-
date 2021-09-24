# Roshani Patel
# ITCS 1140
# 2/29/2020


#Using the Turtle for loops
#drawing circles across the screenimport turtleimport timeimport random


import turtle
import time
import random



#variables
horizontal = int()
radius = int()
colors = ["red", "blue", "yellow", "green"]
pensize = int()
randomcolor = int()
x = int()
y = int()

#initializing the location and size of the circles
horizontal = -200
radius = 25
pensize = 2


#moving the turtle
turtle.penup()
turtle.goto(horizontal, 0)
turtle.pendown()
#setting the pen size, and fill color
turtle.pensize(5)

# Loop to draw the circles
for count in range(0, 4):
    # set the fill color, pensize and fill color
    turtle.fillcolor(colors[count])
    turtle.pensize(pensize)
    turtle.begin_fill()
    # draw circle
    turtle.circle(radius)
    #reset location, radius and pensize
    horizontal = horizontal + 75
    radius = radius + 20
    pensize = pensize + 2
    #Moving the turtle
    turtle.penup()
    turtle.goto(horizontal, 0)
    turtle.pendown()
    turtle.end_fill()
#Sets up the size of the window
time.sleep(3)
turtle.reset()
turtle.setup(600, 600)

turtle.write("Ready for more circles?",move=False, align="center", font=("Arial", 16, "bold"))

#Sets up the size of the window for more circle
time.sleep(3)
turtle.reset()
turtle.setup(600, 600)

# Ready for more circle

for counter in range(0, 20):
    # Randomize the variables
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    randomcolor = random.randint(0, 3)
    pensize = random.randint(0, 10)
    radius = random.randint(25,125)
    #Moving the turtle
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    # set the fill color & pensize
    turtle.fillcolor(colors[randomcolor])
    turtle.pensize(pensize)
    # draw circle
    turtle.circle(radius)
    turtle.end_fill()





    























