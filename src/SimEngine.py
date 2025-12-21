import numpy as np
import Population
import random

def binomialDraw(sim_environment,model,n,m):
		
	createResourceDoses(sim_environment,n,m)
	
	if model.isDecay():
		decay(sim_environment,n,m)

	#Calculate weights for the Bernoulli experiment
	if model.isDiffusion():

		#Only GridCell(1,1) supports production_rate for A's.
		#In order to populate other GridCell spaces A must
		#diffuse and construct a niche.
		if (n == 1 and m == 1):
			weights = [model.getTypeA()['production_rate']+
			sim_environment.getLandscape()[n][m].getNicheA(),
			model.getTypeB()['production_rate']+
			sim_environment.getLandscape()[n][m].getNicheB(),
			model.getTypeC()['production_rate']+
			sim_environment.getLandscape()[n][m].getNicheC(),
			model.getTypeD()['production_rate']+
			sim_environment.getLandscape()[n][m].getNicheD()]
		else:
			weights = [0+sim_environment.getLandscape()[n][m].getNicheA(),
			model.getTypeB()['production_rate']+
			sim_environment.getLandscape()[n][m].getNicheB(),
			model.getTypeC()['production_rate']+
			sim_environment.getLandscape()[n][m].getNicheC(),
			model.getTypeD()['production_rate']+
			sim_environment.getLandscape()[n][m].getNicheD()]
	else:		

		weights = [model.getTypeA()['production_rate']+
		sim_environment.getLandscape()[n][m].getNicheA(),
		model.getTypeB()['production_rate']+
		sim_environment.getLandscape()[n][m].getNicheB(),
		model.getTypeC()['production_rate']+
		sim_environment.getLandscape()[n][m].getNicheC(),
		model.getTypeD()['production_rate']+
		sim_environment.getLandscape()[n][m].getNicheD()]

	#Implementation of the draws
	spawn = random.choices(['A','B','C','D'],
		weights=weights, 
		k=sim_environment.getLandscape()[n][m].getResourceDoses())
	for product in spawn:
		if product == "A": 
			sim_environment.getLandscape()[n][m]\
			.growPopulation(Population.Unit(**model.getTypeA()))
		elif product == "B": 
			sim_environment.getLandscape()[n][m]\
			.growPopulation(Population.Unit(**model.getTypeB()))
		elif product == "C": 
			sim_environment.getLandscape()[n][m]\
			.growPopulation(Population.Unit(**model.getTypeC()))
		elif product == "D": 
			sim_environment.getLandscape()[n][m]\
			.growPopulation(Population.Unit(**model.getTypeD()))
	
#Assigns resource doses to each micro-environment
def createResourceDoses(sim_environment,n,m):
	sim_environment.getLandscape()[n][m].resourceDosesInflux()

#Production is calculated as a sum of production_rate and niche
def productionRateLimited(sim_environment, model, n, m):
	if model.isDecay():
		decay(sim_environment,n,m)

	for i in range(model.getTypeA()['production_rate']+
		int(sim_environment.getLandscape()[n][m].getNicheA())):
		sim_environment.getLandscape()[n][m]\
		.growPopulation(Population.Unit(**model.getTypeA()))	
	for i in range(model.getTypeB()['production_rate']+
		int(sim_environment.getLandscape()[n][m].getNicheB())):
		sim_environment.getLandscape()[n][m]\
		.growPopulation(Population.Unit(**model.getTypeB()))
	for i in range(model.getTypeC()['production_rate']+
		int(sim_environment.getLandscape()[n][m].getNicheC())):
		sim_environment.getLandscape()[n][m]\
		.growPopulation(Population.Unit(**model.getTypeC()))	
	for i in range(model.getTypeD()['production_rate']+
		int(sim_environment.getLandscape()[n][m].getNicheD())):
		sim_environment.getLandscape()[n][m]\
		.growPopulation(Population.Unit(**model.getTypeD()))

#Invoke decay on all individuals
#If an individual's lifespan is 0 then it will not
#be in the surviving population list
def decay(sim_environment,n,m):
	surviving_population=[]
	for individual in sim_environment.getLandscape()[n][m].getPopulation():
		if individual.getLifespan() > 0:
			individual.decay()
			surviving_population.append(individual)
	sim_environment.getLandscape()[n][m].setPopulation(surviving_population)

def diffusion(sim_environment,model,n,m):
	if sim_environment.countRow() > 1 or sim_environment.countRow() > 1:
		for individual in sim_environment.getLandscape()[n][m].getPopulation():
			#Individuals should only be able to diffuse once per timestep
			#This check is set up so that if an individual diffuses to a gridcell
			#whose individuals have not been diffused yet, the individual cannot 
			#diffuse a second time when individuals from its new cell start
			#being distributed
			if not individual.getDiffused():
				new_n,new_m = individual.diffuse(n,m)
				#Note that diffusion treats the grid edges as if
				#they wrap-around. This ensures that each GridCell
				#has the same probability of receiving a diffuser
				#since each GridCell has the same number of neighbours
				if new_n > sim_environment.countRow()-1:
					new_n = new_n - sim_environment.countRow()
				if new_m > sim_environment.countCol()-1:
					new_m = new_m - sim_environment.countCol()

				#The population at the destination GridCell adds the individual
				#to the population and the old GridCell removes the individual from
				#the population
				sim_environment.getLandscape()[new_n][new_m].growPopulation(individual)
				
				sim_environment.getLandscape()[n][m].remove(individual)

	else: print ("Cannot diffuse on a 1x1 environment")

def resetDiffusionStatus(sim_environment):
	row, col = np.shape(sim_environment.getLandscape())
	if sim_environment.countRow() > 1 or sim_environment.countRow() > 1:
		for n in range(row):
			for m in range(col):
				for individual in sim_environment.getLandscape()[n][m].getPopulation():
					individual.setDiffused(False)

def tallyResults(sim_environment, model, n, m, 
	population, pop_A, pop_B, pop_C, pop_D, 
	niche_A, niche_B, niche_C, niche_D):
	count_A = 0
	count_B = 0
	count_C = 0
	count_D = 0

	for individual in sim_environment.getLandscape()[n][m].getPopulation():
		if individual.getType() == 'A':
			count_A += 1
		elif individual.getType() == 'B':
			count_B += 1
		elif individual.getType() == 'C':
			count_C += 1
		elif individual.getType() == 'D':
			count_D += 1

	population[n][m] = count_A+count_B+count_C+count_D
	pop_A[n][m] = count_A
	pop_B[n][m] = count_B
	pop_C[n][m] = count_C
	pop_D[n][m] = count_D
	niche_A[n][m] = sim_environment.getLandscape()[n][m].getNicheA()
	niche_B[n][m] = sim_environment.getLandscape()[n][m].getNicheB()
	niche_C[n][m] = sim_environment.getLandscape()[n][m].getNicheC()
	niche_D[n][m] = sim_environment.getLandscape()[n][m].getNicheD()

	return population, pop_A, pop_B, pop_C, pop_D, niche_A, niche_B, niche_C, niche_D
