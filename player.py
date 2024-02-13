from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.fd(MOVE_DISTANCE)
        if self.ycor() == FINISH_LINE_Y:
            self. __start_line()

    def __start_line(self):
        self.clear()
        self.goto(STARTING_POSITION)

