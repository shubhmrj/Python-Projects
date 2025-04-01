from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.shapesize(3, 3)
        self.penup()
        self.bounce_x = 10
        self.bounce_y = 10
    def move(self):
        new_xcor = self.xcor() + self.bounce_x
        new_ycor = self.ycor() + self.bounce_y
        self.goto(new_xcor, new_ycor)

    def bounce(self):
        self.bounce_y *= -1

    def bounce1(self):
        self.bounce_x *= -1