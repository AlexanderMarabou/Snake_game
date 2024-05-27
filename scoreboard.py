from turtle import Turtle

TOP_Y_SCREEN = 275
TOP_X_SCREEN = 0
ALIGNMENT = "center"
FONT = 'Courier', 20, 'normal'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(TOP_X_SCREEN, TOP_Y_SCREEN)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as new_data:
                new_data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
