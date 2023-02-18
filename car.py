import turtle
import random

import screen
from screen import SCREEN_WIDTH_PX, SCREEN_HEIGHT_PX
import player

DEFAULT_TURTLE_SIZE_PX = 20
HEADING_WEST = 180
CAR_WIDTH_PX = 40
CAR_HEIGHT_PX = 20
CAR_MOVING_DISTANCE_PX = 4


class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.width_px = CAR_WIDTH_PX
        self.height_px = CAR_HEIGHT_PX
        self.shape("square")
        self.penup()
        self.color(self.get_random_color())
        self.shapesize(self.height_px / DEFAULT_TURTLE_SIZE_PX, self.width_px / DEFAULT_TURTLE_SIZE_PX, 1)
        self.goto(self.get_random_start_coordinate())
        self.setheading(HEADING_WEST)
        self.moving_speed_px = CAR_MOVING_DISTANCE_PX

    def move(self):
        self.forward(self.moving_speed_px)

    @staticmethod
    def get_random_color():
        return random.random(), random.random(), random.random()

    def get_random_start_coordinate(self):
        x_start = SCREEN_WIDTH_PX / 2
        avatar_height_px = screen.get_boundaries(player.AVATAR)[1]
        y_start = random.randrange(start=-SCREEN_HEIGHT_PX / 2 + avatar_height_px + CAR_HEIGHT_PX / 2,
                                   stop=+SCREEN_HEIGHT_PX / 2 - CAR_HEIGHT_PX / 2,
                                   step=self.height_px)
        return x_start, y_start
