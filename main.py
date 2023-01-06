from turtle import Screen
from move_Snake import Snake
from food import Food
from Scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Kevin's Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detecting collision with food
    if snake.head.distance(food)< 15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        scoreboard.game_over()
        is_game_on = False

    #detecting collision with tail
    for segments in snake.segment[1::]:
        if snake.head.distance(segments)< 10:
            scoreboard.game_over()
            is_game_on = False


screen.exitonclick()