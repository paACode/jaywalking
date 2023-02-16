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


class Player:

    def __init__(self):
        self.character = self.Character()
        width_px, height_px = self.character.get_boundaries()
        self.boundaries = self.Boundaries(width_px, height_px)
        self.y_coordinate = STARTING_POSITION[1]

    class Character(turtle.Turtle):
        def __init__(self):
            super().__init__()
            self.filepath = "granny.gif"
            self.shape("granny.gif")
            self.img = Image.open(self.filepath)
            self.penup()
            self.goto(STARTING_POSITION)

        def get_boundaries(self):
            return self.img.width, self.img.height

        def move_up(self):
            self.setheading(DIRECTION_UP)
            self.forward(STEP)

    class Boundaries:
        def __init__(self, width_px, height_px):
            my_brush = permanentbrush.PermanentBrush()
            self.rectangle = my_brush.draw_rectangle(STARTING_POSITION, width_px, height_px)

        def move_up(self):
            for line in self.rectangle:
                for element in line:
                    element.setheading(DIRECTION_UP)
                    element.forward(STEP)

    def move_up(self):
        self.y_coordinate += STEP
        self.character.move_up()
        self.boundaries.move_up()
