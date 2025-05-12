from turtle import Screen
import time
from score_board import Scoreboard
from snake import Snake
from food import Food


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


    # Collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or  snake.head.xcor() < -280:
        scoreboard.reset()
        snake.reset()




    # Detect collision with the tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    #if head collides with any segment in the tail:
    #trigger game_over

































screen.exitonclick()