from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.show_scoreboard()


    def add_score(self):
        self.score += 1
        self.clear()
        self.show_scoreboard()


    def show_scoreboard(self):
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)


    def gameover(self):
        self.color("white")
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)