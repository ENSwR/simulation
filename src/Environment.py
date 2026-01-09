import numpy as np
import random
import Population

#An individual micro-environment within the Grid

class GridCell:
	def __init__ (self, niche_A = 0, niche_B = 0, niche_C = 0, \
		niche_D =0, resource_doses = 0):
		self.niche_A = niche_A
		self.niche_B = niche_B
		self.niche_C = niche_C
		self.niche_D = niche_D
		self.population = []
		self.resource_doses = resource_doses

	def growPopulation(self, unit):
		self.population.append(unit)
		
		#A limit is imposed on niche effect to prevent exponential ratchet effect.
		#As a type's niche gets better, each new individual's contribution
		#becomes smaller.

		#This design is intended to flexibly accommodate units which destroy
		#niches of other units, or units which build niches for other units.
		if self.getNicheA() == 0: self.niche_A += unit.getNicheConstructionA()
		else:
			self.niche_A += unit.getNicheConstructionA()/self.getNicheA()
		if self.getNicheB() == 0: self.niche_B += unit.getNicheConstructionB()
		else:
			self.niche_B += unit.getNicheConstructionB()/self.getNicheB()
		if self.getNicheC() == 0: self.niche_C += unit.getNicheConstructionC()
		else:
			self.niche_C += unit.getNicheConstructionC()/self.getNicheC()
		if self.getNicheD() == 0: self.niche_D += unit.getNicheConstructionD()
		else:
			self.niche_D += unit.getNicheConstructionD()/self.getNicheD()
	
	def remove(self, unit):
		self.population.remove(unit)

	def extinction(self, model):
		if model.isDiffusion():

			#1% chance of individuals surviving extinction to diffuse
			indices = random.choices([True,False],
				weights=[0.01,0.99], 
				k=len(self.population))
			self.population = np.array(self.population)[indices].tolist()		
		
		else:				
			self.population = []

	def extinctionA(self):
		for i in self.population: 
			if i.getType() == 'A': 
				self.population.remove(i)

	def extinctionB(self):
		for i in self.population: 
			if i.getType() == 'B': 
				self.population.remove(i)

	def setNicheA(self, niche_A = 0):
		self.niche_A = niche_A

	def setNicheB(self, niche_B = 0):
		self.niche_B = niche_B

	def setNicheC(self, niche_C = 0):
		self.niche_C = niche_C

	def setNicheD(self, niche_D = 0):
		self.niche_D = niche_D


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

	def resourceDosesInflux(self):
		self.resource_doses = 5	#Hard coded at 5

	def getResourceDoses(self):
		return self.resource_doses

# nxn grid of micro-environments

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
	
	def extinctionC(self):
		for n in range(self.row):
			for m in range(self.col):
				self.landscape[n][m].extinctionC()

	def extinctionD(self):
		for n in range(self.row):
			for m in range(self.col):
				self.landscape[n][m].extinctionD()

	def getGridCell(self,n,m):
		return self.landscape[n][m]

	def getLandscape(self):
		return self.landscape
