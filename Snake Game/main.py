import turtle
import time

screen = turtle.Screen()
screen.bgcolor()
screen.setup(600, 600)
screen.tracer(0)
all_snake = []
positions = [(1, 0), (-20, 0), (-40, 0)]
# y_position = [1, 2, 3]

for turtle_index in positions:
    its = turtle.Turtle(shape="square")
    its.penup()
    its.goto(turtle_index)
    all_snake.append(its)
    all_snake.append(its)

game_mode_on = True
while game_mode_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(all_snake)-1, 0, -1):
        new_x = all_snake[i-1].xcor()
        new_y = all_snake[i-1].ycor()
        all_snake[i].goto(new_x, new_y)
    all_snake[0].forward(20)

screen.exitonclick()