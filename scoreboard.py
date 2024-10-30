from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()

    def game_over(self):
        self.hideturtle()
        self.goto(-100, 0)
        self.write("Game Over", font=FONT)

    def write_level(self):
        self.hideturtle()
        self.goto(-280, 250)
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)
