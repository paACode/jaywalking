import time

import car
import player
import screen


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


def collision_with_car():
    for this_car in cars:
        delta_x = round(abs(this_car.xcor() - jaywalker.xcor()))
        delta_y = round(abs(this_car.ycor() - jaywalker.ycor()))
        print(delta_y,delta_x)
        x_collision_threshold = jaywalker.width_px / 2 + this_car.width_px / 2
        y_collision_threshold = jaywalker.height_px / 2 + this_car.height_px / 2
        if delta_x < x_collision_threshold and delta_y < y_collision_threshold:
            return True
    return False


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
        if timer_reached(seconds=0.05):
            timer_start_time = time.time()
            add_car()
            move_cars()
        elif collision_with_car():
            game_is_on = False
        # elif reached_other_side():
        #     print("yippie")
        #     game_is_on = False

        # time.sleep(0.05)
        jaywalking_screen.update()

jaywalking_screen.exitonclick()
