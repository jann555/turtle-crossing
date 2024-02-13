from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-250, 280)
        self.write(f"Level: {self.level} ", align="center", font=("Courier", 14, "normal"))


    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", font=FONT, align="center")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} ", align="center", font=("Courier", 14, "normal"))

