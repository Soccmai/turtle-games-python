from turtle import Turtle, Screen
import random

is_game_on = False
screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


colors = ["red", "orange", "yellow", "green", "blue", "violet"]
turtles = []


if user_bet:
    is_game_on = True
    y = -100
    for i in range(0, 6):
        turtle = Turtle(shape="turtle")
        turtle.color(colors[i])
        turtle.penup()
        turtle.goto(-280, y)
        y += 40
        turtles.append(turtle)

while is_game_on:
    for turtle in turtles:
        if turtle.xcor() > 280:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
                is_game_on = False
            else:
                print(f"You've lost! The {winning_color} turtle the winner")
                is_game_on = False
        random_distance = random.randint(0, 20)
        turtle.forward(random_distance)


