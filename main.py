import time
from turtle import Screen
from food import Food
from snake import Snake

screen = Screen()
screen.tracer(0)
my_snake = Snake(screen)
food = Food(my_snake)
my_snake.setFoodRef(food)
my_snake.initScreen()
my_snake.initializeListeners()
my_snake.runGame()
screen.exitonclick()
