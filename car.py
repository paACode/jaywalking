import turtle
import random
from screen import SCREEN_WIDTH_PX, SCREEN_HEIGHT_PX

CAR_WIDTH_PX = 40
CAR_HEIGHT_PX = 20
DEFAULT_TURTLE_SIZE_PX = 20
HEADING_WEST = 180


class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(self.get_random_color())
        self.shapesize(CAR_HEIGHT_PX / DEFAULT_TURTLE_SIZE_PX, CAR_WIDTH_PX / DEFAULT_TURTLE_SIZE_PX, 1)
        self.goto(self.get_random_start_coordinate())
        self.setheading(HEADING_WEST)

    def move(self):
        self.forward(CAR_WIDTH_PX)

    @staticmethod
    def get_random_color():
        return random.random(), random.random(), random.random()

    @staticmethod
    def get_random_start_coordinate():
        x_start = SCREEN_WIDTH_PX / 2 - CAR_WIDTH_PX / 2
        y_start = random.randrange(start=-SCREEN_HEIGHT_PX / 2 + DEFAULT_TURTLE_SIZE_PX / 2,
                                   stop=+SCREEN_HEIGHT_PX / 2 - DEFAULT_TURTLE_SIZE_PX / 2,
                                   step=CAR_HEIGHT_PX)
        return x_start, y_start
