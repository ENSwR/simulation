import numpy as np
import random
import Population


class GridCell:
	def __init__ (self, niche = 0, niche_A = 0, niche_B = 0, niche_C = 0, \
		niche_D =0, local_effect = 0, resource_doses = 0):
		self.niche = niche
		self.niche_A = niche_A
		self.niche_B = niche_B
		self.niche_C = niche_C
		self.niche_D = niche_D
		self.population = []
		self.local_effect = local_effect #Currently unused
		self.resource_doses = resource_doses

	def growPopulation(self, particle):
		self.population.append(particle)
		
		#Note: "niche" is currently unused. Particles all have
		#niche_construction = 0, so self.niche remains 0 and is not
		#an active component of the simulation at this time.
		self.niche += particle.getNicheConstruction()
		
		#Imposed a limit on niche effect to prevent exponential ratchet effect.
		#As a species's niche gets better, each new individual's contribution
		#becomes smaller
		if self.getNicheA() == 0: self.niche_A += particle.getNicheConstructionA()
		else:
			self.niche_A += particle.getNicheConstructionA()/self.getNicheA()
		if self.getNicheB() == 0: self.niche_B += particle.getNicheConstructionB()
		else:
			self.niche_B += particle.getNicheConstructionB()/self.getNicheB()
		
		self.niche_C += particle.getNicheConstructionC()
		self.niche_D += particle.getNicheConstructionD()
	
	"""
	def migration(self):
		new_coords = []
		for i in self.population:
			new_coords.appends(i.migrate())
			print(new_coords)
	"""
	
	def remove(self, particle):
		self.population.remove(particle)

	def extinction(self, model):
		if model.isDiffusion():

			#1% chance of individuals surviving extinction to diffuse
			indices = (np.random.uniform(size=len(self.population)) < 0.01).astype(bool)
			self.population = np.array(self.population)[indices].tolist()
		
		else:			
		
			self.population = []

	def extinctionA(self):
		for i in self.population: 
			if i.getSpecies() == 'A': 
				self.population.remove(i)

	def extinctionB(self):
		for i in self.population: 
			if i.getSpecies() == 'B': 
				self.population.remove(i)

	def setNiche(self, niche = 0):
		self.niche = niche

	def setNicheA(self, niche_A = 0):
		self.niche_A = niche_A

	def setNicheB(self, niche_B = 0):
		self.niche_B = niche_B

	def setNicheC(self, niche_C = 0):
		self.niche_C = niche_C

	def setNicheD(self, niche_D = 0):
		self.niche_D = niche_D

	def getNiche(self):
		return self.niche

	def getNicheA(self):
		return self.niche_A

	def getNicheB(self):
		return self.niche_B

	def getNicheC(self):
		return self.niche_C

	def getNicheD(self):
		return self.niche_D

	def getPopulation(self):
		return self.population

	def setPopulation(self, population = []):
		self.population = population

	def setLocalEffect(self, flux_param):
		self.local_effect = flux_param - (self.niche*flux_param)

	def getLocalEffect(self):
		return self.local_effect

	def resourceDosesInflux(self):
		self.resource_doses = 5

	def getResourceDoses(self):
		return self.resource_doses

class Grid:
	def __init__ (self,n = 0, m = 0):
		self.row = n
		self.col = m
		self.landscape = np.empty((n,m),dtype = object)
		
	def initializeLandscape(self, niche = 0):
		row, col = np.shape(self.landscape)
		for n in range(row):
			for m in range(col):
				self.landscape[n][m]=GridCell(niche)
	
	def countRow(self):
		return self.row
	def countCol(self):
		return self.col		

	def extinction(self,model):
		for n in range(self.row):
			for m in range(self.col):
				self.landscape[n][m].extinction(model)

	def extinctionA(self):
		for n in range(self.row):
			for m in range(self.col):
				self.landscape[n][m].extinctionA()

	def extinctionB(self):
		for n in range(self.row):
			for m in range(self.col):
				self.landscape[n][m].extinctionB()

	def getGridCell(self,n,m):
		return self.landscape[n][m]

	def getLandscape(self):
		return self.landscape
