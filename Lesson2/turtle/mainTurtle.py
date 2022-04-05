import turtle
from turtle import Turtle, Screen
import math


# 1 & 2:
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


# 3:
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)


# 4:
def circle(t, radius):
    length = (2 * math.pi * radius) / 360
    polygon(t, length, 360)


wn = Screen()
bob = Turtle()
bob.shape('turtle')
bob.color('green')
#bob.penup()

speed = 1


def travel():
    bob.forward(speed)
    wn.ontimer(travel, 10)


wn.onkey(lambda: bob.setheading(90), 'Up')
wn.onkey(lambda: bob.setheading(180), 'Left')
wn.onkey(lambda: bob.setheading(0), 'Right')
wn.onkey(lambda: bob.setheading(270), 'Down')

wn.listen()

travel()

wn.mainloop()
