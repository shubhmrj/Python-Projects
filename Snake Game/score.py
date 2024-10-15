from turtle import Turtle, Screen
from snake import Snake
screen = Screen()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score=0
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.generate_score()
        # self.Name = input("Enter your Name: ")

    def generate_score(self):
        self.clear()
        # noinspection PyTypeChecker
        self.write(f'Score : {self.score}  High Score = {self.high_score}', align="center", font=('bold', 15, 'italic'))

    def high_txt(self):
        # a = screen.textinput(title="Game Over", prompt="Name")
        with open("HIGHSCORE.TXT", mode="a") as file:
            file.write(f" : {self.high_score}")

    def high_score1(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.high_txt()
        self.score=0
        self.generate_score()

    def clear_score(self):
        self.score += 1
        self.generate_score()
