from turtle import Turtle, Screen
import random

screen = Screen()
turtle = Turtle()
turtle.shape("turtle")
screen.colormode(255)


def go_up():
    turtle.penup()
    turtle.left(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(50)
    turtle.pendown()


def random_color():
    rand_r = random.randint(1, 255)
    rand_g = random.randint(1, 255)
    rand_b = random.randint(1, 255)
    return (rand_r, rand_g, rand_b)


def draw_shape(num_sides):
    turtle.pencolor(random_color())
    for i in range(num_sides):
        turtle.right(360/num_sides)
        turtle.forward(100)


go_up()
for i in range(3, 20):
    draw_shape(i)

screen.exitonclick()