from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREENSIZE = {"width": 600, "height": 600}
INITIAL_SNAKE_SIZE = 3
MOVE_DISTANCE = 20

def pause():
    global running
    if running:
        running = False
    else:
        running = True


screen = Screen()
screen.setup(width=SCREENSIZE["width"], height=SCREENSIZE["height"])
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake(move_distance=MOVE_DISTANCE,
              initial_snake_size=INITIAL_SNAKE_SIZE)

food = Food()

scoreboard = Scoreboard()


screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_right, "Right")
screen.onkey(pause, "space")

running = True
game_over = False

screen.update()

i = 0
while not game_over:
    screen.update()
    if running:

        time.sleep(0.1)
        snake.move_snake()

        # Detect food collision
        if snake.head.distance(food) <= 15:
            print("mnom, mnom")
            snake.add_to_snake_body()
            food.collision()
            scoreboard.add_score()

        # Detect wall collision
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
           snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_over = True

        # Detect snake collision
        if snake.collision() == True:
            game_over = True

scoreboard.gameover()

screen.exitonclick()
