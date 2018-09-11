class Warrior:
	def __init__(self, health:int, damage:int, name:str):
		self.health = health
		self.damage = damage
		self.name   = name

	def attack(self, enemy):
		enemy.health -= self.damage
		print(self.name + ' атакует '+ enemy.name + '. '+ enemy.name + ' теряет ' + str(self.damage) + ' очков здроровья.')

	def get_health(self):
		if self.health <= 0:
			print(self.name + ' убит. Выпьем за него.')
		else:
			print('У {0} остается {1} очков здоровья.'.format(self.name, str(self.health)))




garret = Warrior(200, 50, 'Garret')
koegorn = Warrior(210, 45, 'Koegorn')

garret.attack(koegorn)
koegorn.get_health()

koegorn.attack(garret)
garret.get_health()

garret.attack(koegorn)
koegorn.get_health()

koegorn.attack(garret)
garret.get_health()

garret.attack(koegorn)
koegorn.get_health()

koegorn.attack(garret)
garret.get_health()

garret.attack(koegorn)
koegorn.get_health()

garret.attack(koegorn)
koegorn.get_health()