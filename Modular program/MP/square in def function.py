import turtle

def drawSquare(turtle, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        turtle.begin_fill()
        
        turtle.pencolor('blue')
        turtle.fillcolor("red")
        turtle.forward(100)
        turtle.left(90)
        turtle.end_fill()
##wn = turtle.Screen()              # Set up the window and its attributes
##wn.bgcolor("lightgreen")

alex = turtle.Turtle()            # create alex
drawSquare(alex, 50)             # Call the function to draw the square passing the actual turtle and the actual side size

