class Person:
	def __init__(self, name, qualify = 1):
		self.name = name
		self.qualify = qualify

	def get_info (self):
		print('Person name:{1}, Person qualify:{1}.'.format(self.name, str(self.qualify)))

	def __del__(self):
		print(self.name + ' Dismissed')

garry = Person('Garry')
jerry = Person('Jerry', 3)
gordon = Person('Gordon', 2)

print(garry.get_info())
print(jerry.get_info())
print(gordon.get_info())

del(garry)
input()
