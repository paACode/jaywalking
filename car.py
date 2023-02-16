import turtle
import random
from screen import SCREEN_WIDTH_PX, SCREEN_HEIGHT_PX

DEFAULT_TURTLE_SIZE_PX = 20
HEADING_WEST = 180


class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.width_px = 40
        self.height_px = 20
        self.shape("square")
        self.penup()
        self.color(self.get_random_color())
        self.shapesize(self.height_px / DEFAULT_TURTLE_SIZE_PX, self.width_px / DEFAULT_TURTLE_SIZE_PX, 1)
        self.goto(self.get_random_start_coordinate())
        self.setheading(HEADING_WEST)
        self.moving_distance = self.width_px/4

    def move(self):
        self.forward(self.moving_distance)

    @staticmethod
    def get_random_color():
        return random.random(), random.random(), random.random()


    def get_random_start_coordinate(self):
        x_start = SCREEN_WIDTH_PX / 2 - self.width_px / 2
        y_start = random.randrange(start=-SCREEN_HEIGHT_PX / 2 + DEFAULT_TURTLE_SIZE_PX / 2,
                                   stop=+SCREEN_HEIGHT_PX / 2 - DEFAULT_TURTLE_SIZE_PX / 2,
                                   step=self.height_px)
        return x_start, y_start
