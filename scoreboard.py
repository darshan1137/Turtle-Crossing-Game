from turtle import Turtle  

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1 
        self.penup()
        self.goto(-240, -280)
        self.color("black")
        self.hideturtle()
        self.update()


    def update(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", align="center",font= ("Courier", 15, "normal"))

    def add_point(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", align="center",font= ("Courier", 20, "normal"))