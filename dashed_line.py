from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()
turtle.shape("turtle")
turtle.color("green")


def dashed_line(distance):
    while distance >= 20:
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
        distance -= 20
    if distance < 20:
        turtle.forward(distance)


dashed_line(200)
screen.exitonclick()

