import turtle
import time
from snake import Snake
from food import Food
from score import Score

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(600, 600)
screen.tracer(0)

# Here inherit the Snake class
snake = Snake()

# Here inherit the Food class
hungry = Food()

# here we control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food_score = Score()

# food_score.high_score()
game_mode_on = True
while game_mode_on:
    screen.update()
    time.sleep(0.2)
    for turtle in snake.all_snake:
        if turtle.xcor() > 290 or turtle.ycor() > 290 or turtle.xcor() < -290 or turtle.ycor() < -290:
            food_score.high_score1()
            # turtle.screen.textinput(title="Game Over", prompt="Name")
            snake.restart()

    snake.move()

    if snake.head.distance(hungry) < 20:
        hungry.generate_food()
        food_score.clear_score()
        snake.increase_size()
        # food_score.high_score1()

    for snake_body in snake.all_snake:
        if snake_body==snake.head:
            pass
        elif snake.head.distance(snake_body) < 10:
            food_score.high_score1()
            # turtle.screen.textinput(title="Game Over", prompt="Name")

screen.exitonclick()
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