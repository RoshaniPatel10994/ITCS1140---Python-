import turtle




#Moving the pen For Circle
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()

# Draw Circle

turtle.pensize(3)
turtle.pencolor("Red")
turtle.fillcolor("Yellow")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

#Moving the pen for square
turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()


# Draw square

turtle.pensize(3)
turtle.pencolor("Blue")
turtle.fillcolor("Red")
turtle.begin_fill()


turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)

turtle.end_fill()

#Moving the pen for Triangle
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()

# Draw Triangle

turtle.pensize(3)
turtle.pencolor("Yellow")
turtle.fillcolor("Green")
turtle.begin_fill()


turtle.right(35)
turtle.forward(125)
turtle.right(235)
turtle.forward(150)
turtle.left(127)
turtle.forward(130)

turtle.end_fill()




#Moving the pen For Circle at the second Coordinate
turtle.penup()
turtle.goto(-200, 250)
turtle.pendown()

# Draw Circle

turtle.pensize(3)
turtle.pencolor("Red")
turtle.fillcolor("Cyan")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

#Moving the pen for square for first Coordinates
turtle.penup()
turtle.goto(250, 200)
turtle.pendown()


# Draw square

turtle.pensize(3)
turtle.pencolor("Green")
turtle.fillcolor("Yellow")
turtle.begin_fill()


turtle.right(37)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)

turtle.end_fill()


# Draw Sqare in 4th coordinate
turtle.penup()
turtle.goto(250, -300)
turtle.pendown()


# Draw square

turtle.pensize(3)
turtle.pencolor("Green")
turtle.fillcolor("Yellow")
turtle.begin_fill()


turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)

turtle.end_fill()

# Draw Circle in 3 Coordinate
turtle.penup()
turtle.goto(-200, -300)
turtle.pendown()



turtle.pensize(3)
turtle.pencolor("Blue")
turtle.fillcolor("Orange")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()





