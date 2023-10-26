class CPerson:

	def __del__():
		print(f'\nКласс CPerson ничтожен')

	def person():
		surname = input()
		name = input()
		ptr = input()
		num = input()
		month = input()
		year = input()
		gender = input()

		print(f'ФИО: {surname} {name} {ptr}\nДата рождения: {num}.{month}.{year}\nПол: {gender}')

CPerson.person()
CPerson.__del__()
del CPerson