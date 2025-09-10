import Environment, Population, Dials, SimEngine, random, numpy as np
from numpy import random as nprandom
import matplotlib.pyplot as plt
import pandas as pd
import os

def timeStep(sim_environment,model):
	#Configure 
	row, col = np.shape(sim_environment.getLandscape())
	results = np.empty((10),dtype=object)
	population = np.empty((row,col),dtype=float)
	pop_A = np.empty((row,col),dtype=float)
	pop_B = np.empty((row,col),dtype=float)
	pop_C = np.empty((row,col),dtype=float)
	pop_D = np.empty((row,col),dtype=float)
	buffer = np.empty((row,col),dtype=float)
	buffer_A = np.empty((row,col),dtype=float)
	buffer_B = np.empty((row,col),dtype=float)
	buffer_C = np.empty((row,col),dtype=float)
	buffer_D = np.empty((row,col),dtype=float)

	for n in range(row):
		for m in range(col):
			population, pop_A, pop_B, pop_C, pop_D, buffer,buffer_A, buffer_B, buffer_C, buffer_D = SimEngine.tallyResults(sim_environment, model, n, m, population, pop_A, pop_B, pop_C, pop_D, buffer, buffer_A, buffer_B, buffer_C, buffer_D)

	#Compile Results
	results[0] = population
	results[1] = pop_A
	results[2] = pop_B
	results[3] = pop_C
	results[4] = pop_D
	results[5] = buffer
	results[6] = buffer_A
	results[7] = buffer_B
	results[8] = buffer_C
	results[9] = buffer_D

	return results

output_file = "unit_test_migration.csv"
model = Dials.Model(output_file = output_file,
						timesteps = 50, 
						gen_length = 0, 
						variant_A = {}, 
						variant_B = {}, 
						variant_C = {}, 
						variant_D = {},
						env_x = 10,
						env_y = 10,
						decay = True,
						migration = True,
						infinite_resources = True)

model.initSpecies(variant = "A",
					buffer_effect = 0,
					A_buffer_effect = 2, 
					B_buffer_effect = 0,
					C_buffer_effect = 0,
					D_buffer_effect = 0,
					toxin_str = 0,
					toxin_rad = 0,
					antidote_str = 0,
					antidote_rad = 0,
					lifespan = 5,
					prod_capacity = 0)
model.initSpecies(variant = "B",
					buffer_effect = 0,
					A_buffer_effect = 0, 
					B_buffer_effect = 0,
					C_buffer_effect = 0,
					D_buffer_effect = 0,
					toxin_str = 0,
					toxin_rad = 0,
					antidote_str = 0,
					antidote_rad = 0,
					lifespan = 10,
					prod_capacity = 0)


sim_environment = Environment.Grid(model.getEnvX(),model.getEnvY())
sim_environment.initializeLandscape()
row, col = np.shape(sim_environment.getLandscape())
gen_length = model.getGenLength()
timesteps = model.getTimesteps()
results = np.empty((timesteps,11),dtype=object)



t_count = 0
n = 0 #Generation count

sim_environment.getLandscape()[0][1].growPopulation(Population.Particle(**model.getSpeciesA()))
sim_environment.getLandscape()[5][5].growPopulation(Population.Particle(**model.getSpeciesB()))
#You need a way to report the purge as a timestep
for t in range(timesteps): 
	results[t,0] = n
	#results[t,1:] = timeStep(sim_environment)
	for n in range(row):
		for m in range(col):
			SimEngine.decay(sim_environment,n,m)
	if t > 0:
		if model.isMigration():			
			for n in range(row):
				for m in range(col):		
					SimEngine.migration(sim_environment,model,n,m)
			SimEngine.resetMigrationStatus(sim_environment)
	#results[t,1:] = purgedTimestep(sim_environment,model)

	results[t,1:] = timeStep(sim_environment,model)
	print(t)

#Calculates total populations of each chemical species
#over the whole environment
sum_Pop = []
sum_A = []
sum_B = []
sum_C = []
sum_D = []
for i in range(timesteps):
	sum_Pop.append(sum(sum(results[i,1])))
	sum_A.append(sum(sum(results[i,2])))
	sum_B.append(sum(sum(results[i,3])))
	sum_C.append(sum(sum(results[i,4])))
	sum_D.append(sum(sum(results[i,5])))

data = {
	'Generation' : results[:,0],
	'Tot_Pop' : sum_Pop,
	'Tot_Pop_A' : sum_A,
	'Tot_Pop_B' : sum_B,
	'Tot_Pop_C' : sum_C,
	'Tot_Pop_D' : sum_D,
	'Pop' : results[:,1],
	'Pop_A' : results[:,2],
	'Pop_B' : results[:,3],
	'Pop_C' : results[:,4],
	'Pop_D' : results[:,5],
	'Buffer' : results[:,6],
	'Buffer_A' : results[:,7],
	'Buffer_B' : results[:,8],
	'Buffer_C' : results[:,9],
	'Buffer_D' : results[:,10],
}

data = pd.DataFrame(data)
data.to_csv(str(output_file),sep=',')
