from turtle import Screen, _Screen, Turtle
from constants import DM
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class ScoreBoard(Turtle):
    def __init__(self, screen: _Screen):
        super().__init__()

        self.score = 0
        self.screen = screen
        self.high_score = 0
        self.writeText(f'Score: {self.score}')
        with open(os.path.join(__location__, 'data.txt')) as file:
            content = file.read()
            self.high_score = int(content)

    def increaseScore(self):
        if(self.high_score < self.score+1):
            self.high_score = self.score+1
            with open(os.path.join(__location__, 'data.txt'), mode='w') as file:
                file.write(str(self.score))

        self.score += 1
        self.writeText(f'Score: {self.score}. High Score: {self.high_score}')

    def writeText(self, to_write: str):
        self.reset()
        self.penup()
        self.goto((0, (DM/2)-60))
        self.color('white')
        self.hideturtle()
        style = ('Courier', 13, 'normal')
        self.write(to_write, font=style, align='center')

    def resetScore(self):
        self.score = 0
        self.writeText(f'Score: {self.score}. High Score: {self.high_score}')
