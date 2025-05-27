import turtle

positions = [(1, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.all_snake = []
        self.body()
        self.head = self.all_snake[0]

    def body(self):
        for turtle_index in positions:
            self.structure(turtle_index)

    def structure(self, turtle_index):
        its = turtle.Turtle(shape="square")
        its.color("DarkOliveGreen")
        its.penup()
        its.goto(turtle_index)
        self.all_snake.append(its)

    def increase_size(self):
        self.structure(self.all_snake[-1].position())

    def move(self):
        for i in range(len(self.all_snake) - 1, 0, -1):
            new_x = self.all_snake[i - 1].xcor()
            new_y = self.all_snake[i - 1].ycor()
            self.all_snake[i].goto(new_x, new_y)
        self.head.forward(20)

    def restart(self):
        for all_ in self.all_snake:
            all_.goto(1000, 1000)
        self.all_snake.clear()
        self.body()
        self.head = self.all_snake[0]
        self.move()
        self.increase_size()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)