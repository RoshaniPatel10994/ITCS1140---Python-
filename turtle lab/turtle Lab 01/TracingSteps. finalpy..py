#Roshani Patel
#import Turtle library
import turtle

#retracing steps
turtle.write("starting our walk")

#Change Shape To Turtle
turtle.shape("turtle")
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.write("oops wrong direction")
turtle.left(180)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

#Back where we started
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.write("all done")

#Keeps program open and stops it from crashing
turtle.done()
