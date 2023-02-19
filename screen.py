import turtle

SCREEN_WIDTH_PX = 600
SCREEN_HEIGHT_PX = 600


def setup_screen(title):
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH_PX, SCREEN_HEIGHT_PX)
    turn_off_animation(screen)
    add_custom_avatars(screen)
    screen.title(title)
    return screen


def turn_off_animation(screen):
    screen.tracer(0)


def add_custom_avatars(screen):
    """Only avatars added to screen can be used. Reason: Implementation of Turtle-Library"""
    screen.addshape("granny.gif")
