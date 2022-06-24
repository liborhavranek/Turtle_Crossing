import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player_turtle = Player()
car = CarManager()
score_board = Scoreboard()


screen.listen()
screen.onkey(player_turtle.move_up, "w")

game_is_on = True

while game_is_on:
	time.sleep(0.1)
	screen.update()
	car.add_car()
	car.move_of_car()

	#collision turtle with car
	for cars in car.all_cars:
		if player_turtle.distance(cars) < 20:
			score_board.game_over()
			game_is_on = False

	#detect turtle is in second site
	if player_turtle.ycor() > 280:
		score_board.increase_score()
		player_turtle.go_to_start()
		car.level_up()


screen.exitonclick()
