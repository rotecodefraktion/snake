from turtle import Turtle
import random
import time

BORDER = 20

class Food(Turtle):
    def __init__(self, screen_width=600, screen_height=600):
        super().__init__()
        self.screen_width = int(screen_width / 2) - BORDER
        self.screen_height = int(screen_height / 2) - BORDER
        self.shape("turtle")
        self.color("red")
        self.fillcolor("pink")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.setpos(self.rand_pos())


    def rand_pos(self):
        x = [*range(self.screen_width * -1, self.screen_width + 1, 5)]
        y = [*range(self.screen_width * -1, self.screen_width + 1, 5)]
        random_position = (random.choice(x), random.choice(y))
        return random_position

    def collision(self):
        # head_x_low = int(snake_pos[0] - 10)
        # head_x_high = int(snake_pos[0] + 10)
        # head_y_low = int(snake_pos[1] - 10)
        # head_y_high = int(snake_pos[1] + 10)
        # food_pos_x = int(self.position()[0])
        # food_pos_y = int(self.position()[1])
        #
        # print(head_x_low, snake_pos[0], head_x_high, head_y_low, snake_pos[1], head_y_high, food_pos_x, food_pos_y)
        # if (food_pos_x >= head_x_low and food_pos_x <= head_x_high) and \
        #    (food_pos_y >= head_y_low and food_pos_y <= head_y_high) :
        #     print(f"Collision at x:{snake_pos[0]} y:{snake_pos[1]}")
        #     print(f"Food x between {head_x_low} [ {self.position()[0]} ] and [ {head_x_high} ]  ")
        #     print(f"Food y between {head_y_low} [ {self.position()[1]} ] and [ {head_y_high} ]  ")
        #     print("Search new position")
        self.setpos(self.rand_pos())
