import turtle
import time
from snake import Snake
from food import Food
from score import Score

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(600, 600)
screen.tracer(0)
snake = Snake()

hungry = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food_score = Score()

game_mode_on = True
while game_mode_on:
    screen.update()
    time.sleep(0.2)
    for turtle in snake.all_snake:
        if turtle.xcor() > 270 or turtle.ycor() > 270 or turtle.xcor() < -270 or turtle.ycor() < -270:
            game_mode_on = False
            turtle.screen.textinput(title="Game Over", prompt="Name")

    snake.move()

    if snake.head.distance(hungry) < 20:
        hungry.generate_food()
        food_score.clear_score()


screen.exitonclick()