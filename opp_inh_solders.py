from random import randint

class Unit:
	count = 0
	def __init__(self, t):
		Unit.count += 1
		self.unit_id = Unit.count
		self.team_id = t


class Solder(Unit):
	def __init__(self, t):
		Unit.__init__(self, t)
		self.herro = None

	def folow_herro(self, herro):
		self.herro = herro.unit_id


class Herro(Unit):
	def __init__(self, t):
		Unit.__init__(self, t)
		self.level = 1

	def level_up(self):
		self.level += 1

albus = Herro(1)
geralt = Herro(2)

print(albus.unit_id)
print(geralt.unit_id)

team_alpha = []
team_beta  = []

for i in range(30):
	n = randint(1, 2)
	if n == 1:		
		team_alpha.append(Solder(n))	
	elif n == 2:
		team_beta.append(Solder(n))

team_alpha[2].folow_herro(albus)

print(team_alpha[2].herro, albus.unit_id )