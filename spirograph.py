from turtle import Turtle, Screen
import random

screen = Screen()
turtle = Turtle()
turtle.speed("fastest")
screen.colormode(255)


def random_color():
    rand_r = random.randint(1, 255)
    rand_g = random.randint(1, 255)
    rand_b = random.randint(1, 255)
    return (rand_r, rand_g, rand_b)


def circle():
    turtle.color(random_color())
    turtle.pencolor(random_color())
    turtle.circle(100)


def draw_spirograph(size):
    for i in range(int(360 / size)):
        circle()
        turtle.setheading(turtle.heading() + size)


draw_spirograph(5)
screen.exitonclick()
