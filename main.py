from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
#tim=Turtle()
screen=Screen()
screen.bgcolor("black")
screen.screensize(600,600)
screen.tracer(0)
screen.title("Snake Game")
screen.setup(width=600,height=600,startx=150,starty=-100)

snake=Snake()
food=Food()
score= Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # detect collisions..........

    if snake.head.distance(food.snake_food) <15 :
        food.refresh()
        snake.extend()

    #scoreboard..................
        score.increase_score()

    # control the turtle...........

    # if  snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280 :
    #     is_game_on=False
    #     score.game_over()

    if snake.head.xcor()>280:
        snake.head.goto(-280,0)

    if snake.head.ycor()>280:
        snake.head.goto(0,-280)

    if snake.head.xcor()<-280:
        snake.head.goto(280,0)

    if snake.head.ycor()<-280:
        snake.head.goto(0,280)



    #detect colloision with tail........
    for all_turtles in snake.number_of_turtles[2:]:
        # if all_turtles==snake.head:
        #     pass
        if snake.head.distance(all_turtles)<10:
            is_game_on = False
            score.game_over()


screen.exitonclick()