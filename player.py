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

    def is_at_finish_line(self):
        return self.ycor() == FINISH_LINE_Y

    def got_to_start_line(self):
        self.goto(STARTING_POSITION)
