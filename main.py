import time
import car
import player
import scoreboard
import screen

SCREEN_REFRESH_TIME_S = 0.02


def initialize_controls():
    jaywalking_screen.listen()
    jaywalking_screen.onkey(jaywalker.move_up, "space")


def add_car():
    cars.append(car.Car())


def move_all_cars():
    for every_car in cars:
        every_car.move()


def screen_refresh_needed(refresh_time_s=SCREEN_REFRESH_TIME_S):
    if current_time - screen_refresh_start_time > refresh_time_s:
        return True
    return False


def latest_car_ahead_by(distance_px):
    latest_car_added = cars[len(cars) - 1]
    if screen.SCREEN_WIDTH_PX / 2 - latest_car_added.xcor() > distance_px:
        return True
    return False


def collision_with_car():
    if len(cars) > 0:
        for this_car in cars:
            delta_x = round(abs(this_car.xcor() - jaywalker.xcor()))
            delta_y = round(abs(this_car.ycor() - jaywalker.ycor()))
            x_collision_threshold = jaywalker.width_px / 2 + this_car.width_px / 2
            y_collision_threshold = jaywalker.height_px / 2 + this_car.height_px / 2
            if delta_x < x_collision_threshold and delta_y < y_collision_threshold:
                return True
    return False


if __name__ == '__main__':
    jaywalking_screen = screen.setup_screen(title="Jaywalking")
    jaywalker = player.Player()
    initialize_controls()
    jaywalking_scoreboard = scoreboard.Scoreboard()
    cars = []
    add_car()  # Making sure there is already an instance of class car, when starting the game
    game_is_on = True
    screen_refresh_start_time = time.time()
    while game_is_on:
        current_time = time.time()
        if screen_refresh_needed(refresh_time_s=SCREEN_REFRESH_TIME_S):
            screen_refresh_start_time = current_time
            if collision_with_car():
                game_is_on = False
            elif jaywalker.reached_other_side():
                print("yippie")
                jaywalker.goto_start()
                car.Car.increase_speed()
                jaywalking_scoreboard.increase_level()
            elif latest_car_ahead_by(distance_px=jaywalker.width_px * 3):  # Makes sure player can pass between 2 cars
                add_car()
            move_all_cars()
            jaywalking_screen.update()
    jaywalking_scoreboard.game_over()
    jaywalking_screen.exitonclick()
