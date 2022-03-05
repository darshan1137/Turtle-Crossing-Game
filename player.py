from turtle import Turtle 

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -280)
        self.left(90)

    def move(self):
        self.forward(10)

    def restart(self):
        self.goto(0, -280)

    def is_at_finish(self):
        if self.ycor() > 280:
            return True
        else:
            return False
