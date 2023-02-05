from turtle import Turtle
FONT = ("Courier", 18, "normal")
FONT2 = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-310, 250)
        self.update_scoreboard()

    def level_up(self):
        self.level = self.level + 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT2)
