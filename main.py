import time

import car
import player
import screen

SCREEN_REFRESH_TIME_S = 0.02
CAR_APPEND_TIME_S = SCREEN_REFRESH_TIME_S * car.CAR_WIDTH_PX / car.CAR_MOVING_DISTANCE_PX


def initialize_controls():
    jaywalking_screen.listen()
    jaywalking_screen.onkey(jaywalker.move_up, "space")


def add_car():
    cars.append(car.Car())


def move_cars():
    for every_car in cars:
        every_car.move()


def screen_refresh_needed(refresh_time_s=SCREEN_REFRESH_TIME_S):
    if current_time - screen_refresh_start_time > refresh_time_s:
        return True
    return False


def latest_car_ahead_by(distance_px):
    latest_car_added = cars[len(cars) - 1]
    print(screen.SCREEN_WIDTH_PX/2 - latest_car_added.xcor())
    if screen.SCREEN_WIDTH_PX/2 - latest_car_added.xcor() > distance_px:
        return True
    return False


def collision_with_car():
    for this_car in cars:
        delta_x = round(abs(this_car.xcor() - jaywalker.xcor()))
        delta_y = round(abs(this_car.ycor() - jaywalker.ycor()))
        x_collision_threshold = jaywalker.width_px / 2 + this_car.width_px / 2
        y_collision_threshold = jaywalker.height_px / 2 + this_car.height_px / 2
        if delta_x < x_collision_threshold and delta_y < y_collision_threshold:
            return True
    return False


def reached_other_side():
    if jaywalker.ycor() > screen.SCREEN_HEIGHT_PX / 2:
        return True
    return False


if __name__ == '__main__':
    jaywalking_screen = screen.setup_screen(title="Jaywalking")
    jaywalker = player.Player()
    initialize_controls()
    cars = []
    add_car()
    game_is_on = True
    screen_refresh_start_time = time.time()
    while game_is_on:
        current_time = time.time()
        if screen_refresh_needed(refresh_time_s=SCREEN_REFRESH_TIME_S):
            screen_refresh_start_time = current_time
            if latest_car_ahead_by(distance_px=car.CAR_WIDTH_PX):
                add_car()
            move_cars()
            jaywalking_screen.update()

        elif collision_with_car():
            game_is_on = False
        elif reached_other_side():
            print("yippie")
            game_is_on = False

jaywalking_screen.exitonclick()
