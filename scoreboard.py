from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 170)
        self.write(f"Score:{self.score}", align="center", font=("Arial",24,"normal"))
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write("Game Over", align="center",font=("Arial", 24, "normal"))

