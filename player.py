from turtle import Turtle
STARTING_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.left(90)
        self.goto_start()
        self.shape("turtle")
        self.speed("fastest")

    def player_move(self):
        if self.ycor() != FINISH_LINE_Y:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def check_finishline(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(STARTING_POS)

