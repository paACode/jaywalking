import turtle
import random

import car
from screen import SCREEN_WIDTH_PX, SCREEN_HEIGHT_PX
import player

DEFAULT_TURTLE_SIZE_PX = 20
HEADING_WEST = 180
CAR_WIDTH_PX = 40
CAR_HEIGHT_PX = 20
DEFAULT_MOVING_SPEED_PX = 4


class Car(turtle.Turtle):
    moving_speed_px = DEFAULT_MOVING_SPEED_PX
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

    def move(self):
        self.forward(car.Car.moving_speed_px)

    @staticmethod
    def get_random_color():
        return random.random(), random.random(), random.random()

    def get_random_start_coordinate(self):
        x_start = SCREEN_WIDTH_PX / 2
        avatar_width_px, avatar_height_px = player.Player.get_image_boundaries(player.AVATAR_FILEPATH)
        # With static method get_image_boundaries , method can be accessed without creating an instance of class player
        y_start = random.randrange(start=-SCREEN_HEIGHT_PX / 2 + avatar_height_px + CAR_HEIGHT_PX / 2,
                                   stop=+SCREEN_HEIGHT_PX / 2 - CAR_HEIGHT_PX / 2,
                                   step=self.height_px)
        return x_start, y_start

    @staticmethod
    def increase_speed():
        Car.moving_speed_px += 1
