from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    elif snake.snakes[0].xcor() > 280 or snake.snakes[0].xcor() < -280 or snake.snakes[0].ycor() > 280 or snake.snakes[0].ycor() < -280:
        scoreboard.goto(0, 0)
        print(scoreboard.write("GAME OVER", align= "center", font=("courier", 12, "normal")))
        game_is_on = False

    for head in snake.snakes:
        if head == snake.snakes[0]:
            pass
        elif snake.snakes[0].distance(head) < 10:
            game_is_on = False





screen.exitonclick()