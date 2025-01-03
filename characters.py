from turtle import *
import sys

# Set up screen and key listeners
screen = Screen()

def exit_on_key():
    screen.bye()
    sys.exit(0)

# Bind both Enter and Escape keys to exit
screen.onkey(exit_on_key, "Return")  # Enter key
screen.onkey(exit_on_key, "Escape")  # Escape key
screen.listen()  # Start listening for key events

def setup():
  penup()
  left(90)
  forward(300)
  left(90)
  forward(325)
  right(180)

def next_line(size):
  penup()
  right(90)
  forward(16 * size)
  right(90)
  forward(16 * 8 * size)
  right(180)

def draw_héng(size):
  for _ in range(8):
    pendown()
    forward(12 * size)
    penup()
    forward(4 * size)

def draw_shù(size):
  for _ in range(8):
    # Draw down
    pendown()
    right(90)
    forward(12 * size)

    # Reposition
    left(180)
    penup()
    forward(12 * size)
    right(90)
    forward(16 * size)

def main():
    window = Screen()
    window.bgcolor("white")
    speed(3)

    size = 5
    setup()

    draw_héng(size)
    next_line(size)

    draw_shù(size)
    next_line(size)

    window.exitonclick()


if __name__ == "__main__":
    main()