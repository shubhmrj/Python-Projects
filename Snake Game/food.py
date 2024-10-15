import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5 , 0.5)
        self.speed("fastest")
        goto_x = random.randint(-280, 280)
        goto_y = random.randint(-280, 280)
        self.goto(goto_x, goto_y)
        self.generate_food()

    def generate_food(self):
        goto_x = random.randint(-280, 280)
        goto_y = random.randint(-280, 280)
        self.goto(goto_x, goto_y)


