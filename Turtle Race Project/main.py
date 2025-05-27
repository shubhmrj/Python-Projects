from turtle import Turtle, Screen
import random

screen = Screen()

# def factor():
#     its.forward(50)
# def backward():
#     its.backward(50)
# def left_turn():
#     head_direction= its.heading() + 10
#     its.setheading(head_direction)
# def right_turn():
#     head_direction = its.heading() - 10
#     its.setheading(head_direction)

# screen.listen()
# screen.onkey(key="space", fun=factor)
# screen.onkey(key="q", fun=backward)
# screen.onkey(key="w", fun=left_turn)
# screen.onkey(key="e",fun=right_turn)
is_race_on = False
screen.setup(height=400, width=600)
user_bet = screen.textinput(title="who will win the race", prompt="which color you choose")
rainbow_color = ["red", "yellow", "green", "blue", "purple", "orange"]
y_position = [0, -62, -124, 62, 124, 180]
all_turtles = []
for turtle_index in range(0, 6):
    its = Turtle(shape="turtle")
    its.color(rainbow_color[turtle_index])
    its.penup()
    its.goto(x=-270, y=y_position[turtle_index])
    all_turtles.append(its)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 270:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won the {winning_color} turtle won ")
            else:
                print(f"you lost ! The {winning_color} turtle won")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()