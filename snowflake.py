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

def draw_snowflake(size):
    penup()
    forward(20 * size)
    right(120)
    pendown()

    for _ in range(6):
        left(60)
        forward(20 * size)
        right(120)
        forward(20 * size)

    left(120)
    backward(20 * size)

    for _ in range(6):
        forward(40 * size)
        backward(10 * size)
        right(60)
        forward(10 * size)
        backward(10 * size)
        left(120)
        forward(10 * size)
        backward(10 * size)
        right(60)
        backward(30 * size)
        right(60)

def main():
    window = Screen()
    window.bgcolor("white")
    draw_snowflake(10)
    window.exitonclick()

if __name__ == "__main__":
    main()