class CPerson:
	def __init__(self, surname, name, ptr, num, month, year, gender):
		self.surname = surname
		self.name = name
		self.ptr = ptr
		self.num = num
		self.month = month
		self.year = year
		self.gender = gender

	def __del__(self):
		print(f'\nКласс CPerson ничтожен')

	def person(self):

		print(f'ФИО: {self.surname} {self.name} {self.ptr}\nДата рождения: {self.num}.{self.month}.{self.year}\nПол: {self.gender}')

John = CPerson('Surn', 'Name', 'Ptr', '12', '02', '2005', 'male')
John.person()
del CPerson