class Phone:
	def __init__(self, name):
		self.name = name
		self.number = 1
		self.model = 1
		self.weight = 1

	def receiveCall(self):
		print(f'Звонит {self.name}')
		print(f'Номер: {self.number}')
		print(f'Модель: {self.model}')
		print(f'Вес: {self.weight}\n')

	def getNumber(self):
		return self.number

alex = Phone('Алекс')
alex.number = '+79876543210'
alex.model = 'Samsung'
alex.weight = '186g'
alex.receiveCall()

mark = Phone('Марк')
mark.number = '+79991234567'
mark.model = 'iPhone'
mark.weight = '172g'
mark.receiveCall()