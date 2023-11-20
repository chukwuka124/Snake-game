from random import randint
from turtle import Turtle, Screen, _Screen
from constants import DM


class Food(Turtle):
    def __init__(self, snake):
        super().__init__()  # inheritance from Turtle
        self.shape('circle')
        self.color('purple')
        self.penup()
        self.turtlesize(0.5, 0.5, 0)
        self.generateRandomLocation(snake)

    def generateRandomLocation(self, snake):
        location_x = None
        location_y = None
        restart_main_loop_flag = True
        while restart_main_loop_flag:
            restart_main_loop_flag = False
            location_x = randint(-(DM-50)/2, (DM-50)/2)
            location_y = randint(-(DM-50)/2, (DM-50)/2)
            for n in range(len(snake.body)):
                current_position = list(snake.body[n].position())
                if(location_x == current_position[0] and location_y == current_position[1]):
                    restart_main_loop_flag = True
                    # break

        self.setposition((location_x, location_y))
        snake.screen.update()
        return
