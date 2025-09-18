import Environment, Population, Dials, SimEngine, datetime, numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

def extinctionTimestep(sim_environment,model):

	row, col = np.shape(sim_environment.getLandscape())
	
	#Configure fields to hold data for timestep
	results = np.empty((10),dtype=object)
	population = np.empty((row,col),dtype=float)
	pop_A = np.empty((row,col),dtype=float)
	pop_B = np.empty((row,col),dtype=float)
	pop_C = np.empty((row,col),dtype=float)
	pop_D = np.empty((row,col),dtype=float)
	niche = np.empty((row,col),dtype=float)
	niche_A = np.empty((row,col),dtype=float)
	niche_B = np.empty((row,col),dtype=float)
	niche_C = np.empty((row,col),dtype=float)
	niche_D = np.empty((row,col),dtype=float)
	
	#Retrieve data from the SimEngine for each grid square
	for n in range(row):
		for m in range(col):
			result_handle = SimEngine.tallyResults(sim_environment, model, n, m, 
				population, pop_A, pop_B, pop_C, pop_D, 
				niche, niche_A, niche_B, niche_C, niche_D)	

	#Compile results from timestep data
	results[0] = result_handle[0] #population
	results[1] = result_handle[1] #pop_A
	results[2] = result_handle[2] #pop_B
	results[3] = result_handle[3] #pop_C
	results[4] = result_handle[4] #pop_D
	results[5] = result_handle[5] #niche
	results[6] = result_handle[6] #niche_A
	results[7] = result_handle[7] #niche_B
	results[8] = result_handle[8] #niche_C
	results[9] = result_handle[9] #niche_D

	return results

def timeStep(sim_environment,model):

	row, col = np.shape(sim_environment.getLandscape())
	
	#Configure fields to hold data for timestep
	results = np.empty((10),dtype=object)
	population = np.empty((row,col),dtype=float)
	pop_A = np.empty((row,col),dtype=float)
	pop_B = np.empty((row,col),dtype=float)
	pop_C = np.empty((row,col),dtype=float)
	pop_D = np.empty((row,col),dtype=float)
	niche = np.empty((row,col),dtype=float)
	niche_A = np.empty((row,col),dtype=float)
	niche_B = np.empty((row,col),dtype=float)
	niche_C = np.empty((row,col),dtype=float)
	niche_D = np.empty((row,col),dtype=float)
	
	#Run sim for timestep
	for n in range(row):
		for m in range(col):
			#Determines whether to implement resource limitation			
			if model.isInfiniteResources(): 
				SimEngine.productionBiasLimited(sim_environment,model,n,m)
			else: 
				SimEngine.binomialDraw(sim_environment,model,n,m)
	
	#Retrieve results from the SimEngine for each grid suqare
	for n in range(row):
		for m in range(col):
			result_handle = SimEngine.tallyResults(sim_environment, model, n, m, 
				population, pop_A, pop_B, pop_C, pop_D, 
				niche, niche_A, niche_B, niche_C, niche_D)


	#Compile results from timestep data
	results[0] = result_handle[0] #population
	results[1] = result_handle[1] #pop_A
	results[2] = result_handle[2] #pop_B
	results[3] = result_handle[3] #pop_C
	results[4] = result_handle[4] #pop_D
	results[5] = result_handle[5] #niche
	results[6] = result_handle[6] #niche_A
	results[7] = result_handle[7] #niche_B
	results[8] = result_handle[8] #niche_C
	results[9] = result_handle[9] #niche_D

	return results


def main(model,output_file):
	#Create the environment
	sim_environment = Environment.Grid(model.getEnvX(),model.getEnvY())
	sim_environment.initializeLandscape()

	#configure parameters from moddle settings
	extinction_gap = model.getExtinctionGap()
	timesteps = model.getTimesteps()
	row, col = np.shape(sim_environment.getLandscape())

	#Set up results tracker for each timestep
	results = np.empty((timesteps,11),dtype=object)

	t_since_extinction = 0
	extinction_count = 0
	
	for t in range(timesteps): 

		results[t,0] = extinction_count
		
		#Timestep 0 is handled internally as an extinction timestep
		#at beginning of the simultation
		if t == 0:
			results[t,1:] = extinctionTimestep(sim_environment,model)
		else:
			t_since_extinction += 1

			#Executes extinction processes
			if t_since_extinction > extinction_gap:
				extinction_count+=1
				sim_environment.extinction(model)
				if model.isDiffusion():
					for n in range(row):
						for m in range(col):		
							SimEngine.diffusion(sim_environment,model,n,m)
					SimEngine.resetDiffusionStatus(sim_environment)
				results[t,1:] = extinctionTimestep(sim_environment,model)
				t_since_extinction = 0
			
			#Executes normal timestep
			else:
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

	#Calculated populations and results are formatted to
	#dataframe and output to .csv
	data = {
		'Extinctions' : results[:,0],
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
		'Niche' : results[:,6],
		'niche_A' : results[:,7],
		'niche_B' : results[:,8],
		'niche_C' : results[:,9],
		'niche_D' : results[:,10],
	}

	data = pd.DataFrame(data)
	data.to_csv(str(output_file),sep=',')

	#appends the seed value for the run to a .seed file 
	#This provides a history of run seeds so results can be reproduced
	with open(str(output_file.replace('.csv','.seed')),'a') as seed_output:
		seed_output.write(str(datetime.datetime.now()) + "\t" + str(model.getSeed())+"\n")
	print("Seed: " + str(model.getSeed()))
