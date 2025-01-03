from turtle import *
import sys

# Set up screen and key listeners
screen = Screen()

def exit_on_key():
    bye()
    sys.exit(0)

# Bind both Enter and Escape keys to exit
screen.onkey(exit_on_key, "Return")  # Enter key
screen.onkey(exit_on_key, "Escape")  # Escape key
screen.listen()  # Start listening for key events

def draw_rock(size):
    penup()
    forward(size)
    right(90)
    forward(size)
    left(180)

    pendown()
    circle(size, 180)

def main():
    window = Screen()
    window.bgcolor("white")
    window.setup(400, 400)
    window.setworldcoordinates(-200, -200, 200, 200)

    draw_rock(200)

    window.exitonclick()

if __name__ == "__main__":
    main()