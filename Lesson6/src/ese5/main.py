# Exercise 5 Lesson 6 - Recursion
import turtle
from turtle import Turtle, Screen
import math

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

wn = Screen()
bob = Turtle()
bob.shape('turtle')
bob.color('green')

speed = 1

square(bob, lenth)

wn.mainloop()

