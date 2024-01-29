from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def move_left():
    turtle.left(10)

def move_right():
    turtle.right(10)


def clear():
    turtle.clear()


screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(clear, "c")
screen.exitonclick()
