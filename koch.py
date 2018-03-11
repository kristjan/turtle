#!/usr/bin/env python3

import sys
import turtle

screen = turtle.Screen()

t = turtle.Turtle()

def koch(t, depth, size):
    if depth == 0:
        t.forward(size)
        return
    else:
        segment = size / 3
        koch(t, depth - 1, segment)
        t.left(60)
        koch(t, depth - 1, segment)
        t.right(120)
        koch(t, depth - 1, segment)
        t.left(60)
        koch(t, depth - 1, segment)

# Position
t.penup()
t.left(90)
t.forward(300)
t.right(150)
t.pendown()

t.speed(0)

for i in range(3):
    koch(t, int(sys.argv[1]), 500)
    t.right(120)

screen.exitonclick()
