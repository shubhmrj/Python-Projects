from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed(20000)
        self.shape("square")
        self.shapesize(4, 1)
        self.penup()
        self.goto(position)


    def fow(self):
        new_y = self.ycor() + 15
        self.goto(self.xcor(), new_y)

    def bow(self):
        new_y = self.ycor() - 15
        self.goto(self.xcor(), new_y)




    # def paddle2(self):
    #     self.arcade.shape("square")
    #     self.arcade.shapesize(4, 1)
    #     self.arcade.penup()
    #     self.arcade.goto(-370, 0)
    #
    # def paddle1(self):
    #     self.arcade1.shape("square")
    #     self.arcade1.shapesize(4, 1)
    #     self.arcade1.penup()
    #     self.arcade1.goto(370, 0)
