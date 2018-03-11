#!/usr/bin/env python3

import math
import sys
import turtle

screen = turtle.Screen()

t = turtle.Turtle()

def serpinski(t, depth, size):
    for i in range(3):
        t.forward(size)
        t.left(120)
    if depth == 0:
        return

    segment = size / 2

    serpinski(t, depth - 1, segment)
    t.forward(segment)
    serpinski(t, depth - 1, segment)
    t.left(120)
    t.forward(segment)
    t.right(120)
    serpinski(t, depth - 1, segment)
    t.right(120)
    t.forward(segment)
    t.left(120)


# Position
t.penup()
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(180)
t.pendown()

t.speed(0)

serpinski(t, int(sys.argv[1]), 400)

screen.exitonclick()
