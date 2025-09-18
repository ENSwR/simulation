import random
class Particle:
	__slots__ = ['species', 
				'niche_construction',
				'A_niche_construction', 
				'B_niche_construction',
				'C_niche_construction',
				'D_niche_construction',
				'toxin_str', 
				'toxin_rad', 
				'antidote_str', 
				'antidote_rad',
				'lifespan',
				'production_bias',
				'diffused']

	def __new__(cls, *args, **kwargs):
		return super().__new__(cls)

	def __init__ (self, species = None, 
						niche_construction = 0,
						A_niche_construction = 0, 
						B_niche_construction = 0,
						C_niche_construction = 0,
						D_niche_construction = 0,
						toxin_str = 0, 
						toxin_rad = 0, 
						antidote_str = 0, 
						antidote_rad = 0,
						lifespan = 1,
						production_bias = 0,
						diffused = False):
		self.species = species
		self.niche_construction = niche_construction
		self.A_niche_construction = A_niche_construction
		self.B_niche_construction = B_niche_construction
		self.C_niche_construction = C_niche_construction
		self.D_niche_construction = D_niche_construction
		self.toxin_str = toxin_str
		self.toxin_rad = toxin_rad
		self.antidote_str = antidote_str
		self.antidote_rad = antidote_rad
		self.lifespan = lifespan
		self.production_bias = production_bias
		self.diffused = diffused

	def diffuse(self,n,m):
		self.diffused = True
		new_n = n
		new_m = m
		while new_n == n and new_m == m:
			new_n = random.choice([n+1,n-1,n])
			new_m = random.choice([m+1,m-1,m])
		#print ("n: " + str(n) + " m: " + str(m))
		#print ("new n: " + str(new_n) + " new m:" + str(new_m))
		return new_n, new_m

	def getDiffused(self):
		return self.diffused

	def setDiffused(self,diffused):
		self.diffused = diffused

	def setSpecies(self, species):
		self.species = species

	def setNicheConstruction(self, niche_construction):
		self.niche_construction = niche_construction

	def setNicheConstructionA(self, A_niche_construction):
		self.A_niche_construction = A_niche_construction

	def setNicheConstructionB(self, B_niche_construction):
		self.B_niche_construction = B_niche_construction

	def setNicheConstructionC(self, C_niche_construction):
		self.C_niche_construction = C_niche_construction

	def setNicheConstructionD(self, D_niche_construction):
		self.D_niche_construction = D_niche_construction

	def setToxinStrength(self, toxin_str):
		self.toxin_str = toxin_str

	def setToxinRadius(self, toxin_rad):
		self.toxin_rad = toxin_rad

	def setAntidoteStrength(self, antidote_str):
		self.antidote_str = antidote_str

	def setAntidoteRadius(self, antidote_rad):
		self.antidote_rad = antidote_rad

	def setProductionBias(self, production_bias):
		self.production_bias = production_bias	

	def getSpecies(self):
		return self.species

	def getNicheConstruction(self):
		return self.niche_construction
	def getNicheConstructionA(self):
		return self.A_niche_construction
	def getNicheConstructionB(self):
		return self.B_niche_construction
	def getNicheConstructionC(self):
		return self.C_niche_construction
	def getNicheConstructionD(self):
		return self.D_niche_construction

	def getToxinStrength(self):
		return self.toxin_str

	def getToxinRadius(self):
		return self.toxin_rad

	def getAntidoteStrength(self):
		return self.antidote_str

	def getAntidoteRadius(self):
		return self.antidote_rad

	def getLifespan(self):
		return self.lifespan

	def getProductionBias(self):
		return self.production_bias

	def decay(self):
		self.lifespan = self.lifespan-1

	#Currently unused in the simulation.
	#Partially implemented concept of species
	#being able to catalyze self-production
	#or production of other species
	
	"""
	def catalytic_production(self):
		products = []
		if self.getSpecies() == "A":
			#if random.random() < 0.2:
			#	products.append("A")
			if random.random() < 0.5:
				products.append("B")
		elif self.getSpecies() == "B":
			#if random.random() < 0.2:
			#	products.append("B")
			if random.random() < 0.5:
				products.append("A")
		elif self.getSpecies() == "C":
			products.append(self.getNicheConstruction())
		elif self.getSpecies() == "D":
			#if random.random() < 0.2:
			#	products.append("D")
			if random.random() < 0.5:
				products.append("C")
		return products
	"""

	def setSpecies(self, species):
		self.species = species

	def setNicheConstruction(self, niche_construction):
		self.niche_construction = niche_construction

	def setToxinStrength(self, toxin_str):
		self.toxin_str = toxin_str

	def setToxinRadius(self, toxin_rad):
		self.toxin_rad = toxin_rad

	def setAntidoteStrength(self, antidote_str):
		self.antidote_str = antidote_str

	def setAntidoteRadius(self, antidote_rad):
		self.antidote_rad = antidote_rad

	def getSpecies(self):
		return self.species

	def getNicheConstruction(self):
		return self.niche_construction

	def getToxinStrength(self):
		return self.toxin_str

	def getToxinRadius(self):
		return self.toxin_rad

	def getAntidoteStrength(self):
		return self.antidote_str

	def getAntidoteRadius(self):
		return self.antidote_rad