import turtle
from PIL import Image

from screen import SCREEN_HEIGHT_PX

DEFAULT_TURTLE_SIZE_PX = 20
DIRECTION_UP = 90


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("granny.gif")
        self.width_px,  self.height_px = self.get_boundaries()
        self.goto(0, -SCREEN_HEIGHT_PX / 2 + self.height_px / 2)
        self.moving_distance = self.height_px/2

    @staticmethod
    def get_boundaries():
        filepath = "granny.gif"
        img = Image.open(filepath)
        return img.width, img.height

    def move_up(self):
        self.setheading(DIRECTION_UP)
        self.forward(self.moving_distance)

