class Reader:
	def __init__(self, name):
		self.name = name
		self.num = 1
		self.faculty = 1
		self.dob = 1
		self.tel = 1

	def takeBook(self):
		booksTake = input('Сколько книг хотите взять?\n\n')

		if int(booksTake) == 1:
			print(f'{self.name} взял {booksTake} книгу')
		else:
			print(f'{self.name} взял {booksTake} книги')


	def returnBook(self):
		booksReturn = input('Сколько книг хотите вернуть?\n\n')

		if int(booksReturn) == 1:
			print(f'{self.name} вернул {booksReturn} книгу')
		else:
			print(f'{self.name} вернул {booksReturn} книги')


John = Reader('Джон')
John.num = '17'
John.faculty = 'random faculty'
John.dob = '12.02.2005'
John.tel = '+19251522847'
res = input('Взять книгу - 1\nВернуть книгу - 2\n\n')

if res == '1':
	John.takeBook()

elif res == '2':
	John.returnBook()

else:
	print('Error!')
