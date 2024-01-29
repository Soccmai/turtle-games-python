import colorgram
from turtle import Turtle, Screen
import random

img_colors = colorgram.extract("image.jpg", 30)
colors = []

for img_color in img_colors:
    color_tuple = ((img_color.rgb.r), (img_color.rgb.g), (img_color.rgb.b))
    colors.append(color_tuple)

print(colors)

screen = Screen()
turtle = Turtle()
turtle.speed("fast")
screen.colormode(255)


y = -225
def new_row():
    turtle.goto(-225, y)


def go_to_right():
    turtle.dot(20, random.choice(colors))
    turtle.forward(50)


turtle.penup()
for i in range(10):
    new_row()
    for j in range(10):
        go_to_right()
    y += 50

screen.exitonclick()
