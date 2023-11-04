from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color = "red"
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def start_position(self):
        self.goto(x=0, y=-280)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
