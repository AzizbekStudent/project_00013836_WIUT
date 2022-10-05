import math
import turtle
import math
import random

bob = turtle.Turtle()
bob.color("red", "yellow")
def drawm():
    for i in range(200):
        bob.forward(10)
        bob.left(math.sin(i/10)*25)
        bob.left(20)

bob.begin_fill()
drawm()

bob.penup()
bob.backward(300)
bob.pendown()
drawm()


bob.end_fill()


turtle.done()