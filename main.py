import time

import car
import player
import screen

COLLISION_THRESHOLD = car.CAR_WIDTH_PX/2


def initialize_controls():
    jaywalking_screen.listen()
    jaywalking_screen.onkey(jaywalker.move_up, "space")


def timer_reached(seconds):
    time_passed = timer_current_time - timer_start_time

    if time_passed > seconds:
        return True
    return False


def add_car():
    cars.append(car.Car())


def move_cars():
    for every_car in cars:
        every_car.move()


# def collision_with_car():
#     for every_car in cars:
#         for line in jaywalker.boundaries.rectangle:
#             for element in line:
#                 if element.distance(every_car) < COLLISION_THRESHOLD:
#                     print(element.distance(every_car))
#                     return True
#     return False


# def reached_other_side():
#     if jaywalker.y_coordinate > screen.SCREEN_HEIGHT_PX / 2:
#         return True
#     return False


if __name__ == '__main__':
    jaywalking_screen = screen.setup_screen(title="Jaywalking")
    jaywalker = player.Player()
    initialize_controls()
    cars = []
    game_is_on = True
    timer_start_time = time.time()
    while game_is_on:
        timer_current_time = time.time()
        if timer_reached(seconds=0.5):
            timer_start_time = time.time()
            add_car()
            move_cars()
        # elif collision_with_car():
        #     game_is_on = False
        # elif reached_other_side():
        #     print("yippie")
        #     game_is_on = False

        time.sleep(0.1)
        jaywalking_screen.update()

jaywalking_screen.exitonclick()
