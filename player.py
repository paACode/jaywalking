import turtle
import permanentbrush
from PIL import Image

from screen import SCREEN_HEIGHT_PX

CHARACTER_WIDTH_PX = 40
CHARACTER_HEIGHT_PX = 80
DEFAULT_TURTLE_SIZE_PX = 20
STEP = CHARACTER_HEIGHT_PX / 2
STARTING_POSITION = (0, -SCREEN_HEIGHT_PX / 2 + CHARACTER_HEIGHT_PX / 2)
DIRECTION_UP = 90


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("granny.gif")
        self.width_px,  self.height_px = self.get_boundaries()
        self.goto(STARTING_POSITION)

    def get_boundaries(self):
        filepath = "granny.gif"
        img = Image.open(filepath)
        return img.width, img.height

    def move_up(self):
        self.setheading(DIRECTION_UP)
        self.forward(STEP)

