from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
	def __init__(self):
		super().__init__()
		self.color("black")
		self.setheading(90)
		self.shape("turtle")
		self.penup()
		self.go_to_start()

	def go_to_start(self):
		self.goto(STARTING_POSITION)

	def move_up(self):
		new_y = self.ycor() + 20
		self.goto(self.xcor(), new_y)

	def is_in_the_end(self):
		self.go_to_start()


