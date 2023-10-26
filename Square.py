class Square:

	def __init__(self, a, d):
		self.a = a
		self.d = d

	def s(self):
		sqS = self.a * self.a
		print(f'Площадь 1 метод (Известна сторона квадрата: {self.a}): Площадь квадрата = {self.a} * {self.a} = {sqS}')

	def s2(self):
		sqS2 = self.d * self.d / 2
		print(f'Площадь 2 метод (Известна диагональ квадрата: {self.d}): Площадь квадрата = {self.d} * {self.d} / 2 = {sqS2}')

	def p(self):
		sqP = self.a * 4
		print(f'Периметр 1 метод (Известна сторона квадрата: {self.a}): Периметр квадрата = {self.a} * 4 = {sqP}')

	def p2(self):
		sqP2 = self.d * 2 * (2 ** 0.5)
		print(f'Периметр 2 метод (Известна диагональ квадрата: {self.d}): Периметр квадрата = {self.d} * 2 * √2 = {sqP2}')

squareS = Square(5, 0)
squareS2 = Square(0, 10)
squareS.s()
squareS2.s2()

squareP = Square(7, 0)
squareP2 = Square(0, 25)
squareP.p()
squareP2.p2()