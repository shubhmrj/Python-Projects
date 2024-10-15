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