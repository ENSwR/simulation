import random

#Units which can comprise a population 
#stored in population parameter of 
#Environment.GridCell

class Unit:
	__slots__ = ['type', 
				'A_niche_construction', 
				'B_niche_construction',
				'C_niche_construction',
				'D_niche_construction',
				'lifespan',
				'production_rate',
				'diffused']

	def __new__(cls, *args, **kwargs):
		return super().__new__(cls)

	def __init__ (self, type = None, 
						A_niche_construction = 0, 
						B_niche_construction = 0,
						C_niche_construction = 0,
						D_niche_construction = 0,
						lifespan = 1,
						production_rate = 0,
						diffused = False):
		self.type = type
		self.A_niche_construction = A_niche_construction
		self.B_niche_construction = B_niche_construction
		self.C_niche_construction = C_niche_construction
		self.D_niche_construction = D_niche_construction
		self.lifespan = lifespan
		self.production_rate = production_rate
		self.diffused = diffused

	def diffuse(self,n,m):
		self.diffused = True
		new_n = n
		new_m = m
		#While condition ensures that the unit moves
		#to a new location
		while new_n == n and new_m == m:
			new_n = random.choice([n+1,n-1,n])
			new_m = random.choice([m+1,m-1,m])
		return new_n, new_m

	def getDiffused(self):
		return self.diffused

	def setDiffused(self,diffused):
		self.diffused = diffused

	def setType(self, type):
		self.type = type

	def setNicheConstructionA(self, A_niche_construction):
		self.A_niche_construction = A_niche_construction

	def setNicheConstructionB(self, B_niche_construction):
		self.B_niche_construction = B_niche_construction

	def setNicheConstructionC(self, C_niche_construction):
		self.C_niche_construction = C_niche_construction

	def setNicheConstructionD(self, D_niche_construction):
		self.D_niche_construction = D_niche_construction

	def setProductionRate(self, production_rate):
		self.production_rate = production_rate	

	def getType(self):
		return self.type

	def getNicheConstructionA(self):
		return self.A_niche_construction

	def getNicheConstructionB(self):
		return self.B_niche_construction

	def getNicheConstructionC(self):
		return self.C_niche_construction

	def getNicheConstructionD(self):
		return self.D_niche_construction

	def getLifespan(self):
		return self.lifespan

	def getProductionRate(self):
		return self.production_rate

	def decay(self):
		self.lifespan = self.lifespan-1

	#Currently unused in the simulation.
	#Partially implemented concept of types
	#being able to catalyze self-production
	#or production of other types
	
	"""
	def catalytic_production(self):
		products = []
		if self.getType() == "A":
			#if random.random() < 0.2:
			#	products.append("A")
			if random.random() < 0.5:
				products.append("B")
		elif self.getType() == "B":
			#if random.random() < 0.2:
			#	products.append("B")
			if random.random() < 0.5:
				products.append("A")
		elif self.getType() == "C":
			products.append(self.getNicheConstruction())
		elif self.getType() == "D":
			#if random.random() < 0.2:
			#	products.append("D")
			if random.random() < 0.5:
				products.append("C")
		return products
	"""

