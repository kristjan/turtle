#!/usr/bin/env python3

import math
import random
import sys
import turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
TRIANGLE_SIZE = 10

screen = turtle.Screen()
screen.setup(SCREEN_WIDTH + TRIANGLE_SIZE*4, SCREEN_HEIGHT + TRIANGLE_SIZE*4)
t = turtle.Turtle()

def halfway(a, b):
    return (
            (a[0] + b[0]) / 2,
            (a[1] + b[1]) / 2,
           )

def random_point():
    return (
            random.randint(-SCREEN_WIDTH / 2, SCREEN_WIDTH / 2),
            random.randint(-SCREEN_HEIGHT / 2, SCREEN_HEIGHT / 2)
           )

def triangle(fill = False):
    t.pendown()
    if fill:
        t.begin_fill()
    for i in range(3):
        t.forward(TRIANGLE_SIZE)
        t.right(120)
    if fill:
        t.end_fill()
    t.penup()

def triangle_at(p, fill = False):
    t.goto(p[0], p[1])
    triangle(fill)

t.speed(0)
t.left(60)
t.penup()

points = [random_point() for i in range(3)]
for p in points:
    triangle_at(p, True)

current = random_point()
triangle_at(current)

for i in range(int(sys.argv[1])):
    next = random.choice(points)
    current = halfway(current, next)
    triangle_at(current)

screen.exitonclick()
