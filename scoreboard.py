from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=FONT)
