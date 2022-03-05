from turtle import Turtle   
import random 

COLOURS = ['blue', 'red', 'green', 'yellow', 'magenta', 'cyan', '']

class Cars(Turtle):
    def __init__(self):
        self.all_cars = []
        self.speed = 1

    def create_cars(self):
        random_chance =  random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLOURS))
            new_car.penup()
            new_car.goto(300, random.randint(-250,250 ) )
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(5)

    def level_up(self):
        self.speed *= 0.9
    