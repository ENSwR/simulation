import Environment, Population, Dials, SimEngine, random, numpy as np
from numpy import random as nprandom
import matplotlib.pyplot as plt
import pandas as pd
import os

sim_environment = Environment.Grid(10,10)
sim_environment.initializeLandscape()

species_A = {"variant": "A",
					"buffer_effect" : 0,
					"A_buffer_effect" : 1, 
					"B_buffer_effect" : 0,
					"C_buffer_effect" : 0,
					"D_buffer_effect" : 0,
					"toxin_str" : 0,
					"toxin_rad" : 0,
					"antidote_str" : 0,
					"antidote_rad" : 0,
					"lifespan" : 0,
					"prod_capacity" : 2}
species_B = {"variant": "B",
					"buffer_effect" : 0,
					"A_buffer_effect" : 1, 
					"B_buffer_effect" : 0,
					"C_buffer_effect" : 0,
					"D_buffer_effect" : 0,
					"toxin_str" : 0,
					"toxin_rad" : 0,
					"antidote_str" : 0,
					"antidote_rad" : 0,
					"lifespan" : 0,
					"prod_capacity" : 2}

sim_environment.getLandscape()[1][0].growPopulation(Population.Particle(**species_A))
sim_environment.getLandscape()[1][0].growPopulation(Population.Particle(**species_B))
sim_environment.getLandscape()[1][0].growPopulation(Population.Particle(**species_A))
sim_environment.getLandscape()[1][0].growPopulation(Population.Particle(**species_B))
print (sim_environment.getLandscape()[1][0].getPopulation())
print()
for individual in sim_environment.getLandscape()[1][0].getPopulation():
	new_n,new_m = individual.migrate(1,0)
	sim_environment.getLandscape()[new_n][new_m].growPopulation(individual)
	sim_environment.getLandscape()[1][0].remove(individual)
print (sim_environment.getLandscape()[1][0].getPopulation())
print()
print (sim_environment.getLandscape()[new_n][new_m].getPopulation())