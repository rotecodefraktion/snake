from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

PAUSE_KEYPRESSED = 10

class Snake:
    def __init__(self, move_distance=20, initial_snake_size=3):
        self.snake: [Turtle] = []
        self.initial_items = initial_snake_size
        self.move_distance = move_distance
        self.create_snake()
        self.head = self.snake[0]
        self.time_last_key_pressed = 0

    def create_snake(self):
        for _ in range(self.initial_items):
            self.add_to_snake_body()


    def add_to_snake_body(self):
        snake_item = Turtle()
        snake_item.shape("square")
        snake_item.color("white")
        snake_item.penup()

        if len(self.snake) > 0:
            x_offset = 0
            y_offset = 0
            last_item: Turtle = self.snake[-1]
            heading = last_item.heading()

            if heading == RIGHT:
                x_offset = - 20
            elif heading == UP:
                y_offset = - 20
            elif heading == LEFT:
                x_offset = 20
            elif heading == DOWN:
                y_offset = 20

            x = last_item.position()[0] + x_offset
            y = last_item.position()[1] + y_offset
            snake_item.setpos(x, y)


        self.snake.append(snake_item)

    def move_snake(self):
        # range (start <- included, stop <-- not included, step)
        for index in range(len(self.snake) - 1, -1, -1):
            current_snake_item = self.snake[index]
            if index == 0:
                current_snake_item.forward(20)
            else:
                new_pos: (float, float) = (self.snake[index - 1].pos()[0], self.snake[index - 1].pos()[1])
                current_snake_item.setpos(new_pos)

    def collision(self):
        for snake_item in self.snake[1:]:
            return self.head.distance(snake_item) <= 10
        return False

    def key_pressed_distance(self):
        return int(time.time() * 1000) - self.time_last_key_pressed

    def set_last_keypressed_time(self):
        self.time_last_key_pressed = int(time.time() * 1000)

    def turn_up(self):
        if self.head.heading() == DOWN:
            return
        if self.key_pressed_distance() < PAUSE_KEYPRESSED:
            return
        self.set_last_keypressed_time()
        self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() == UP:
            return
        if self.key_pressed_distance() < PAUSE_KEYPRESSED:
            return
        self.set_last_keypressed_time()
        self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() == RIGHT:
            return
        if self.key_pressed_distance() < PAUSE_KEYPRESSED:
            return
        self.set_last_keypressed_time()
        self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() == LEFT:
            return
        if self.key_pressed_distance() < PAUSE_KEYPRESSED:
            return
        self.set_last_keypressed_time()
        self.head.setheading(RIGHT)

    def head_position(self):
        return self.head.position()