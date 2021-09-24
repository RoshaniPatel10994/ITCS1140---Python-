# Import Turtle Library

import turtle
import time

# Define main function
def main():
    turtle.setup(800,600)
    climb('red',5)
    time.sleep(1)
    turtle.reset()
    turtle.setup(800,600)
    turtle.shape('classic')
    swim('green',4)
    time.sleep(1)
    turtle.reset()
    turtle.setup(800,600)
    turtle.shape('classic')
    eat()
    time.sleep(1)
    turtle.reset()
    turtle.setup(800,600)
    turtle.shape('classic')
    sleep()

def write(asdf):
        string = str(asdf)
        turtle.write(string, move = False,align = "right", font = ("Arial", 16, "bold"))


    
# Climb a Mountain
def climb (colored, sizer):
    turtle.reset()
    turtle.shape('turtle')
    size = int()
    size = sizer
    color = str(colored)
    turtle.pensize(size)
    turtle.pencolor(color)
    counter = 0
    turtle.pendown()
    # Loop
    for counter in range (0,4):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
    turtle.forward(50)
    turtle.color('black')
    turtle.write("Hurray! Made it to the top!", move = False,align = "right", font = ("Arial", 16, "bold"))

# Swiming in Pond
def swim (colored2, sizer2):
    size2 = int()
    size2 = sizer2
    color2 = str(colored2)
    
    turtle.penup()
    turtle.goto(-160, 70)
    turtle.pendown()
    turtle.shape('triangle')
    turtle.pencolor('blue')
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()
    turtle.shape('turtle')
    turtle.pensize(size2)
    turtle.pencolor(color2)
    turtle.penup()
    turtle.goto(-172, 60)
    turtle.pendown()
    turtle.circle(100)
    turtle.fillcolor('green')
    turtle.pencolor('blue')
    turtle.left(90)
    turtle.forward(70)
    turtle.pencolor('black')
    turtle.write("Yeah! I'm swimming!", move = False,align = "right", font = ("Arial", 16, "bold"))

# Eating 
def eat():
    turtle.fillcolor('green')
    turtle.shape('turtle')
    colors = ["red", "blue", "yellow", "green"]
    randomcolor = int()
    turtle.penup()
    turtle.goto(-150,-150)
    horizontal = -150
    vertical = -150
    # Loop for circle
    for count in range (0,4):
        turtle.shape('classic')
        turtle.pendown()
        colors = ["red", "blue", "yellow", "green"]
        turtle.fillcolor(colors[count])
        turtle.pencolor(colors[count])
        turtle.pensize(5)
        turtle.begin_fill()
        turtle.circle(10)
        turtle.penup()
        horizontal = horizontal + 7
        vertical = vertical + 7
        turtle.goto(horizontal,vertical)
        turtle.end_fill()        
    turtle.goto(-150,-150)
    horizontal = -150
    vertical = -150
    turtle.shape('turtle')
    # Loop for eat turtle
    for count in range (0,4):
        turtle.pendown()
        turtle.fillcolor('white')
        turtle.pencolor('white')
        turtle.pensize(5)
        turtle.begin_fill()
        turtle.circle(10)
        turtle.penup()
        horizontal = horizontal + 7
        vertical = vertical + 7
        turtle.goto(horizontal,vertical)
        turtle.end_fill()
        turtle.fillcolor('green')
        time.sleep(3)
    turtle.pencolor('black')
    turtle.write("Wow! What a great meal!", move = False,align = "right", font = ("Arial", 16, "bold"))

# Sleeping
def sleep():
    turtle.penup()
    turtle.goto(100, -100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.shape('classic')
    turtle.fillcolor('brown')
    turtle.pencolor('brown')
    #Loop for bed
    for counter in range (0,4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

    turtle.pencolor('pink')
    turtle.penup()
    turtle.goto(140,-110)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('pink')
    
    # Loop for pillow
    for counter in range (0,4):
        turtle.pendown()
        turtle.forward(25)
        turtle.right(90)
    turtle.end_fill()
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(153, -153)
    turtle.left(90)
    turtle.forward(15)
    turtle.setheading(90)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor('green')
    turtle.pencolor('black')
    turtle.write("Good Night!", move = False, align = "right", font = ("Arial", 16, "bold"))

main()
