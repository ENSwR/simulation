import sys
import Dials
import configparser
import sim
import random

config = configparser.ConfigParser(allow_no_value=True)
config.read(sys.argv[1])

dials = config['Dials']

#This model supports up to 4 species.
#This allows unused species to be omitted from config
try:
	species_A = config['Species_A']
except:
	species_A = None
try:
	species_B = config['Species_B']
except:
	species_B = None
try:
	species_C = config['Species_C']
except:
	species_C = None
try:
	species_D = config['Species_D']
except:
	species_D = None


############################################################################
#Initialize Model
############################################################################


try: 
	set_seed = int(dials['seed'])
	print(set_seed)
except:
	set_seed = random.randrange(1,9999)

#Allows simulation to run with a random seed if seed is configured as a non-numerical
if not isinstance(set_seed,int):
	set_seed = random.randrange(1,9999)

random.seed(set_seed)

model = Dials.Model(output_file = dials['output_file'],
	timesteps = int(dials['timesteps']),
	extinction_gap = int(dials['extinction_gap']),
	env_x = int(dials['environment_x']),
	env_y = int(dials['environment_y']),
	decay = dials.getboolean('decay'),
	diffusion = dials.getboolean('diffusion'),
	infinite_resources = dials.getboolean('infinite_resources'),
	seed = set_seed)

############################################################################
#Initialize Species
############################################################################


def initEmptySpecies(model, type):
	model.initSpecies(species = str(type),
						A_niche_construction = 0,
						B_niche_construction = 0,
						C_niche_construction = 0,
						D_niche_construction = 0,
						production_bias = 0,
						lifespan = 0)


#Note this model supports species which are not used.
#This section has had some functionality commented 
#out to emphasize what is being used in the simulation.

if species_A is not None:
	if model.isDecay():	
		model.initSpecies(species = "A",
							A_niche_construction = int(species_A['A_niche_construction']),
							#B_niche_construction = int(species_A['B_niche_construction']),
							#C_niche_construction = int(species_A['C_niche_construction']),
							#D_niche_construction = int(species_A['D_niche_construction']),
							production_bias = int(species_A['production_bias']),
							lifespan = int(species_A['lifespan']))
	else:
		model.initSpecies(species = "A",
							A_niche_construction = int(species_A['A_niche_construction']),
							#B_niche_construction = int(species_A['B_niche_construction']),
							#C_niche_construction = int(species_A['C_niche_construction']),
							#D_niche_construction = int(species_A['D_niche_construction']),
							production_bias = int(species_A['production_bias']))
else:
	initEmptySpecies(model,"A")

if species_B is not None:
	if model.isDecay():
		model.initSpecies(species = "B",
							#A_niche_construction = int(species_B['A_niche_construction']),
							B_niche_construction = int(species_B['B_niche_construction']),
							#C_niche_construction = int(species_B['C_niche_construction']),
							#D_niche_construction = int(species_B['D_niche_construction']),
							production_bias = int(species_B['production_bias']),
							lifespan = int(species_B['lifespan']))
	else:
		model.initSpecies(species = "B",
							#A_niche_construction = int(species_B['A_niche_construction']),
							B_niche_construction = int(species_B['B_niche_construction']),
							#C_niche_construction = int(species_B['C_niche_construction']),
							#D_niche_construction = int(species_B['D_niche_construction']),
							production_bias = int(species_B['production_bias']))
else:
	initEmptySpecies(model,"B")

if species_C is not None:
	model.initSpecies(species = "C")#,
						#A_niche_construction = int(species_C['A_niche_construction']),
						#B_niche_construction = int(species_C['B_niche_construction']),
						#C_niche_construction = int(species_C['C_niche_construction']),
						#D_niche_construction = int(species_C['D_niche_construction']),
						#production_bias = int(species_C['production_bias']))

else:
	initEmptySpecies(model,"C")

if species_D is not None:
	model.initSpecies(species = "D")#,
						#A_niche_construction = int(species_D['A_niche_construction']),
						#B_niche_construction = int(species_D['B_niche_construction']),
						#C_niche_construction = int(species_D['C_niche_construction']),
						#D_niche_construction = int(species_D['D_niche_construction']),
						#production_bias = int(species_D['production_bias']))

else:
	initEmptySpecies(model,"D")

sim.main(model,model.getOutputFile())