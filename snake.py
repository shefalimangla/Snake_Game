import random
from turtle import Turtle,Screen
starting_positions=[(0,0),(-20,0),(-40,0)]
end_positions=[300,300]
move_distance=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
turtle_color=["white","red","yellow","pink","cyan"]


class Snake:
    def __init__(self):
        self.number_of_turtles = []
        self.create_snake()
        self.head=self.number_of_turtles[0]
        self.tail=self.number_of_turtles[-1]

    def create_snake(self):
        for positions in starting_positions:
            self.add_Turtle(positions)

    def add_Turtle(self,positions):
        all_turtles = Turtle(shape="square")
        all_turtles.color(random.choice(turtle_color))
        all_turtles.penup()
        all_turtles.goto(positions)
        self.number_of_turtles.append((all_turtles))

    def extend(self):
        self.add_Turtle(self.tail.position())


    def move(self):
        for all_turtles in range(len(self.number_of_turtles) - 1, 0, -1):
            self.new_x = self.number_of_turtles[all_turtles - 1].xcor()
            self.new_y = self.number_of_turtles[all_turtles - 1].ycor()
            self.number_of_turtles[all_turtles].goto(self.new_x, self.new_y)
        self.head.forward(move_distance)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

