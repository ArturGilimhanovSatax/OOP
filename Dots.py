import math
class Dots:

	def __init__(self, x1, y1, x2, y2, x3, y3):
		self.x1 = x1
		self.x2 = x2
		self.x3 = x3
		self.y1 = y1
		self.y2 = y2
		self.y3 = y3

	def distance(self):
		A = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
		B = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
		C = math.sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2)
		p = A + B + C

		print(f'Периметр треугольника = {p}')


dots = Dots(2, 4, 6, 9, 6, 0)
dots.distance()
