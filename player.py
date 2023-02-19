import turtle
import screen
from PIL import Image

DEFAULT_TURTLE_SIZE_PX = 20
DIRECTION_UP = 90
AVATAR_FILEPATH = "grandpa.gif"


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(AVATAR_FILEPATH)
        self.width_px, self.height_px = self.get_image_boundaries(AVATAR_FILEPATH)
        self.goto_start()
        self.moving_distance_px = self.height_px / 2

    def move_up(self):
        self.setheading(DIRECTION_UP)
        self.forward(self.moving_distance_px)

    def goto_start(self):
        self.goto(0, -screen.SCREEN_HEIGHT_PX / 2 + self.height_px / 2)

    def reached_other_side(self):
        if self.ycor() > screen.SCREEN_HEIGHT_PX / 2:
            return True
        return False

    @staticmethod
    def get_image_boundaries(filepath):
        img = Image.open(filepath)
        return img.width, img.height
