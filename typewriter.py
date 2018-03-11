#!/usr/bin/env python3

import math
import os
import sys
import turtle

PADDING = 50
SCREEN_WIDTH = 1200
LINE_HEIGHT = 150
SCREEN_HEIGHT = LINE_HEIGHT * 4 + PADDING * 5

screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
t = turtle.Turtle()

input = sys.argv[1]

letter_width = (SCREEN_WIDTH - PADDING * 2) / len(input)

letter_spacing = letter_width * 2/5
letter_width = letter_width * 3/5
if letter_width > LINE_HEIGHT:
    letter_width = LINE_HEIGHT
letter_height = letter_width

def line(size):
    for i in range(2):
        t.forward(size)
        t.left(180)

def skip(size):
    t.penup()
    t.forward(size)
    t.pendown()

def a(depth, size):
    if depth == 0:
        return

    hypotenuse = math.hypot(size, size / 2)
    angle = math.degrees(math.atan2(size, size / 2))

    # /
    t.right(90 - angle)
    t.forward(hypotenuse)

    # \
    t.right(2 * angle)
    t.forward(hypotenuse)

    # Bottom-right descent
    t.right(180 - angle)
    skip(size / 2)
    t.right(90)
    a(depth - 1, size / 2)

    # -
    t.right(90 - angle)
    skip(hypotenuse / 2)
    t.left(180 - angle)
    t.forward(size / 2)
    t.right(90)

    # Top descent
    a(depth - 1, size / 2)

    # Return
    t.left(90 + angle)
    t.forward(hypotenuse / 2)
    t.right(90 + angle)

    # Bottom- left descent
    a(depth - 1, size / 2)


def k(depth, size):
    if depth == 0:
        line(size)
        return

    hypotenuse = math.hypot(size / 2, size / 2)

    # Mast
    t.forward(size)
    t.left(180)
    t.forward(size / 2)

    # Bottom leg
    t.left(45)
    k(depth - 1, hypotenuse)

    # Top leg
    t.left(90)
    k(depth - 1, hypotenuse)

    # Back to start
    t.right(135)
    t.forward(size / 2)
    t.left(180)

def m(depth, size):
    peak_angle = math.degrees(math.atan(0.5))
    hypotenuse = math.hypot(size, size / 2)

                                 # |\/|
    m_line(depth, size)          # |
    t.right(180 - peak_angle)
    m_line(depth, hypotenuse)    #  \
    t.left(180 - 2 * peak_angle)
    m_line(depth, hypotenuse)    #   /
    t.right(180 - peak_angle)
    m_line(depth, size)          #    |

# The line segment bottoms out one level sooner than the M itself, so we unwind
# at depth 1 instead of 0. In other words,
def m_line(depth, size):
    if depth == 1 or size <=1:
        t.forward(size)
        return
    segment = size / 3
    m_line(depth - 1, segment)
    t.left(90)
    m(depth - 1, segment) # A full M
    t.left(90)
    m_line(depth - 1, segment)


def m_helper(depth, size):
    m(depth, size)
    # Reset to bottom left
    t.penup()
    t.right(90)
    t.forward(size)
    t.right(90)

def x(depth, size):
    if depth == 0 or size <= 1:
        return

    # /
    x_leg(depth, size)

    t.right(90)
    skip(size)
    t.right(180)

    # \
    x_leg(depth, size)

    skip(size)
    t.right(90)

def x_leg(depth, size):
    hypotenuse = math.hypot(size, size)
    t.right(45)
    t.forward(hypotenuse)

    t.right(180)
    skip(hypotenuse / 4)

    t.right(90)
    x(depth - 1, hypotenuse / 4)
    t.left(90)

    skip(hypotenuse / 2)

    t.left(90)
    x(depth - 1, hypotenuse / 4)
    t.right(90)

    skip(hypotenuse / 4)
    t.right(135)

def nextchar():
    t.right(90)
    t.penup()
    t.forward(letter_width + letter_spacing)
    t.pendown()
    t.left(90) # Up again

def nextline():
    t.penup()
    t.right(180)
    t.forward(letter_height + PADDING)
    t.right(90)
    t.forward((letter_width + letter_spacing) * len(input))
    t.right(90)
    t.pendown()

def initposition():
    t.penup()
    t.left(180)
    t.forward(SCREEN_WIDTH / 2 - PADDING)
    t.right(90)
    t.forward(SCREEN_HEIGHT / 2 - PADDING - letter_height)
    t.pendown()

t.speed(0)

alphabet = {
        'a': a,
        'k': k,
        'm': m_helper,
        'x': x
        }

initposition()
for i in range(4):
    for letter in input:
        alphabet[letter](2 ** i, letter_width)
        nextchar()
    nextline()

t.hideturtle()
filename = 'renders/' + input
eps = filename + '.eps'
png = filename + '.png'
t.getscreen().getcanvas().postscript(file=eps)
os.system(
    'which convert &&' +
    ' convert -colorspace RGB ' + eps +
    ' -flatten -background white PNG32:' + png
)

screen.exitonclick()
