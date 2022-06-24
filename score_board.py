from turtle import Turtle
FONT = ("courier", 24, "normal")

class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 1
		self.penup()
		self.goto(-250, 250)
		self.color("black")
		self.hideturtle()
		self.update_score_board()

	def update_score_board(self):
		self.write(f"Level: {self.score}", align='left', font=('Arial', 20, 'normal'))

	def increase_score(self):
		self.score += 1
		self.clear()
		self.update_score_board()


	def game_over(self):
		self.goto(-80, 0)
		self.write(f"GAME OVER! In level: {self.score}", align='left', font=('Arial', 20, 'normal'))