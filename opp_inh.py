class Table:
	def __init__(self, l, w, h):
		self.lenght  = l
		self.width = w
		self.height = h

class KitchenTable(Table):
	def __init__(self, l, w, h, p):
		Table.__init__(self, l, w, h)
		self.place = p

	def setPlaces(self, p):
		self.p = p

class DeskTable(Table):
	def getSquare(self):
		return self.lenght * self.width

class ComputerTable(DeskTable):
	def getSquare(self, e):
		return DeskTable.getSquare(self) - e

hall_table = DeskTable(25, 45, 12)
room_table = ComputerTable(25, 45, 12)

print(room_table.getSquare(3))
print(hall_table.getSquare())