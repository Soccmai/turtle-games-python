from turtle import Turtle, Screen
import random

screen = Screen()
turtle = Turtle()
turtle.pensize(15)
turtle.speed("fastest")
screen.colormode(255)


angles = [0, 90, 180, 270]


def random_color():
    rand_r = random.randint(1, 255)
    rand_g = random.randint(1, 255)
    rand_b = random.randint(1, 255)
    return (rand_r, rand_g, rand_b)


def random_walk(times):
    for i in range(times):
        turtle.color(random_color())
        turtle.pencolor(random_color())
        turtle.forward(30)
        turtle.setheading(random.choice(angles))


random_walk(200)
screen.exitonclick()
