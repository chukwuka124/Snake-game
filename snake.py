import time
from turtle import Turtle, _Screen
from scoreboard import ScoreBoard
from constants import DM, TURTLE_SIZE, FOOD_BUFFER, UP, DOWN, LEFT, RIGHT


class Snake:
    def __init__(self, screen: _Screen):
        body = []

        for n in range(-1, 2):
            temp_turtle = Turtle()
            temp_turtle.hideturtle()
            temp_turtle.penup()
            temp_turtle.color('white')
            temp_turtle.shape('square')
            temp_turtle.turtlesize(1, 1, 0)
            temp_turtle.setposition(-n*TURTLE_SIZE, 0)
            temp_turtle.showturtle()
            temp_turtle.speed(0.1)
            body.append(temp_turtle)

        temp = Turtle()
        temp.hideturtle()
        temp.penup()

        self.body = body
        self.screen = screen
        self.temp_turtle = temp
        self.scoreboard = ScoreBoard(screen)
        self.gameOver = False
        self.crash = False
        self.food_reference = None

    def initScreen(self):
        self.screen.setup(width=DM, height=DM)
        self.screen.bgcolor('black')
        self.screen.title('Divine\'s Snake Game')

    def moveBody(self, past_position):
        for n in range(1, len(self.body)):
            temp_position = self.body[n].position()
            self.body[n].setposition(past_position)
            past_position = temp_position
        self.screen.update()

    def moveForward(self, food):
        if self.crash:
            return
        food_position = (food.position())
        past_position = list(self.body[0].position())
        not_on_food = True
        self.temp_turtle.setheading(self.body[0].heading())
        self.temp_turtle.setposition(self.body[0].position())
        self.temp_turtle.forward(TURTLE_SIZE)
        if(self.temp_turtle.distance(food_position) <= FOOD_BUFFER):
            not_on_food = False
        else:
            if (DM/2)-abs(self.temp_turtle.position()[0]) < 10 or (DM/2)-abs(self.temp_turtle.position()[1]) < 10:
                self.crash = True
                self.scoreboard.writeText(
                    f'GAME OVER.\nYou collided with the wall.\nYour score was {self.scoreboard.score}. Your high score is {self.scoreboard.high_score}.\nPress "r" to restart or "q" to quit game')
                return True
            for n in range(len(self.body)):
                current_turtle: Turtle = self.body[n]
                if(current_turtle.distance(self.temp_turtle) == 0):
                    self.crash = True
                    self.scoreboard.writeText(
                        f'GAME OVER.\nYou collided with your body.\nYour score was {self.scoreboard.score}. Your high score is {self.scoreboard.high_score}.\nPress "r" to restart or "q" to quit game')
                    return True

        if(not not_on_food):
            food.generateRandomLocation(self)
            self.scoreboard.increaseScore()
            self.add_cell()

        self.body[0].forward(TURTLE_SIZE)
        self.moveBody(past_position)
        return False

    def moveRight(self):
        if self.crash:
            return
        if(int(self.body[0].heading()) == LEFT):
            return
        self.body[0].setheading(RIGHT)

    def moveUp(self):
        if self.crash:
            return
        if(int(self.body[0].heading()) == DOWN):
            return
        self.body[0].setheading(UP)

    def moveDown(self):
        if self.crash:
            return
        if(int(self.body[0].heading()) == UP):
            return
        self.body[0].setheading(DOWN)

    def moveLeft(self):
        if self.crash:
            return
        if(int(self.body[0].heading()) == RIGHT):
            return
        self.body[0].setheading(LEFT)

    def add_cell(self):
        temp_turtle = Turtle()
        temp_turtle.penup()
        temp_turtle.color('white')
        temp_turtle.shape('square')
        temp_turtle.turtlesize(1, 1, 0)
        length_of_snake = len(self.body)
        last_cell = self.body[length_of_snake-1]
        last_cell_position = list(self.body[length_of_snake-1].position())
        if(int(last_cell.heading()) == LEFT):
            temp_turtle.setposition(
                (last_cell_position[0]+TURTLE_SIZE, last_cell_position[1]))
            self.body.append(temp_turtle)
            return
        elif (int(last_cell.heading()) == RIGHT):
            temp_turtle.setposition(
                (last_cell_position[0]-TURTLE_SIZE, last_cell_position[1]))
            self.body.append(temp_turtle)
            return
        elif (int(last_cell.heading()) == UP):
            temp_turtle.setposition(
                (last_cell_position[0], last_cell_position[1]-TURTLE_SIZE))
            self.body.append(temp_turtle)
            return
        elif (int(last_cell.heading()) == DOWN):
            temp_turtle.setposition(
                (last_cell_position[0], last_cell_position[1]+TURTLE_SIZE))
            self.body.append(temp_turtle)
            return

    def restartGame(self):

        body = []
        for n in range(len(self.body)):
            self.body[n].reset()

        for n in range(-1, 2):
            temp_turtle = Turtle()
            temp_turtle.hideturtle()
            temp_turtle.penup()
            temp_turtle.color('white')
            temp_turtle.shape('square')
            temp_turtle.turtlesize(1, 1, 0)
            temp_turtle.setposition(-n*TURTLE_SIZE, 0)
            temp_turtle.showturtle()
            temp_turtle.speed(0.1)
            body.append(temp_turtle)

        temp = Turtle()
        temp.hideturtle()
        temp.penup()

        self.body = body
        self.temp_turtle = temp
        self.scoreboard.resetScore()
        self.gameOver = False
        self.crash = False
        self.runGame()

    def quit(self):
        self.scoreboard.writeText(
            f'You quit, thanks for playing Divine\'s snake game.\nYour score was {self.scoreboard.score}')
        self.gameOver = True

    def runGame(self):
        while not self.crash and not self.gameOver:
            self.moveForward(self.food_reference)
            time.sleep(0.1)

    def setFoodRef(self, food):
        self.food_reference = food

    def initializeListeners(self):
        self.screen.listen()
        self.screen.onkey(self.moveRight, "Right")
        self.screen.onkey(self.moveLeft, "Left")
        self.screen.onkey(self.moveUp, "Up")
        self.screen.onkey(self.moveDown, "Down")
        self.screen.onkey(self.restartGame, "r")
        self.screen.onkey(self.quit, "q")
