class LinearFunction():
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def ycor(self, x): 
		# y = ax + b
		return self.a * x + self.b # The value of our y coordinate

	def xcor(self, y):
		# y = ax + b
		y -= self.b
		return y / self.a # The value of the x coordinate
