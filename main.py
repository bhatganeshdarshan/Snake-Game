from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
is_game_on = True
screen = Screen()
screen.bgcolor("green")
screen.setup(width=600, height=600)
screen.title("SNAKE GAME")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
while is_game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.reset()
        food.hideturtle()
        food = Food()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()
    for seg_pos in snake.snake[1:]:
        # if seg_pos == snake.head:
        #     continue
        if snake.head.distance(seg_pos) < 10:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()
