from turtle import Turtle
import random
from snake import Snake
class Food():
    def __init__(self):
        #super().__init__(self)
        self.is_find_food = True
        self.snake_food = Turtle(shape="circle")
        self.snake_food.color("yellow")
        self.snake_food.penup()
        self.snake_food.speed("fastest")
        self.snake_food.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        self.x = random.randint(-280, 280)
        self.y = random.randint(-280, 280)
        self.snake_food.goto(self.x, self.y)
