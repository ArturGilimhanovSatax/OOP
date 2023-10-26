class Triangle:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def s(self):
		tS = (self.a * self.b) / 2
		print(f'Площадь (Известны катеты треугольника: {self.a} и {self.b}): Площадь треугольника = {self.a} * {self.b} / 2 = {tS}')

	def p(self):
		tP = (self.a ** 2 + self.b ** 2) ** 0.5
		print(
			f'Периметр (Известны катеты треугольника: {self.a} и {self.b}): Периметр треугольника = √{self.a}² + {self.b}² = {tP}')

triangleS = Triangle(3, 5)
triangleP = Triangle(3, 5)
triangleS.s()
triangleP.p()