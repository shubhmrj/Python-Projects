import turtle

import score
from paddle import Paddle
from generateball import Ball
import time

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Arcade")
screen.tracer(0)
# paddle_class = Paddle(position)

l_paddle = Paddle((380, 0))
r_paddle = Paddle((-385, 0))

ball = Ball()

screen.listen()
screen.onkeypress(fun=l_paddle.fow, key="Up")
screen.onkeypress(fun=l_paddle.bow, key="Down")

screen.onkeypress(fun=r_paddle.fow, key="w")
screen.onkeypress(fun=r_paddle.bow, key="s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() < -270 or ball.ycor() > 270:
        ball.bounce()

    if ball.xcor() > 300 and ball.distance(l_paddle) < 25 or ball.xcor() < -300 and ball.distance(r_paddle) < 25:
        ball.bounce1()
        score.Score()
    # elif ball.distance(r_paddle) < 25 and ball.xcor() < -290:
    #     ball.bounce1()

    if ball.xcor() > 375 or ball.xcor() < -385:
        game_is_on = False
screen.exitonclick()
