import turtle
import screen

FONT_TYPE = "Courier"
FONT_SIZE = 20
FONT_STYLE = "normal"


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.x_position = -screen.SCREEN_WIDTH_PX / 2 + FONT_SIZE / 2
        self.y_position = screen.SCREEN_HEIGHT_PX / 2 - 2 * FONT_SIZE
        self.goto(self.x_position, self.y_position)
        self.level = 1
        self.update_level()

    def increase_level(self):
        self.level += 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=(FONT_STYLE, FONT_SIZE, FONT_STYLE))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font=(FONT_STYLE, FONT_SIZE, FONT_STYLE))
