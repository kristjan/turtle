import turtle
import sys

# Set up screen and key listeners
screen = turtle.Screen()

def exit_on_key():
    screen.bye()
    sys.exit(0)

# Bind both Enter and Escape keys to exit
screen.onkey(exit_on_key, "Return")  # Enter key
screen.onkey(exit_on_key, "Escape")  # Escape key
screen.listen()  # Start listening for key events


def draw_snowflake(t, size):
  t.penup()
  t.forward(20 * size)
  t.right(120)
  t.pendown()

  for _ in range(6):
    t.left(60)
    t.forward(20 * size)
    t.right(120)
    t.forward(20 * size)

  t.left(120)
  t.backward(20 * size)

  for _ in range(6):
     t.forward(40 * size)
     t.backward(10 * size)
     t.right(60)
     t.forward(10 * size)
     t.backward(10 * size)
     t.left(120)
     t.forward(10 * size)
     t.backward(10 * size)
     t.right(60)
     t.backward(30 * size)
     t.right(60)


def main():
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    draw_snowflake(t, 10)
    window.exitonclick()


if __name__ == "__main__":
    main()