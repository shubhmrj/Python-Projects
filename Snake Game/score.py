from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("orchid")

        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.generate_score()

    def generate_score(self):
        # noinspection PyTypeChecker
        self.write(f'Score : {self.score}', align="center", font=('bold', 15, 'italic', 'underline'))

    def clear_score(self):
        self.score += 1
        self.clear()
        self.generate_score()
