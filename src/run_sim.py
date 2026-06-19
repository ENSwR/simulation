import sys
import Dials
import configparser
import sim
import random

############################################################################
#This script is the starting point of the simulation
############################################################################

config = configparser.ConfigParser(allow_no_value=True)
config.read(sys.argv[1])

dials = config['Dials']

#This model supports up to 4 types.
#This allows unused types to be omitted from config
try:
	type_A = config['Type_A']
except:
	type_A = None
try:
	type_B = config['Type_B']
except:
	type_B = None
try:
	type_C = config['Type_C']
except:
	type_C = None
try:
	type_D = config['Type_D']
except:
	type_D = None


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
#Initialize Types
############################################################################


def initEmptyType(model, type):
	model.initType(type = str(type),
						A_niche_construction = 0,
						B_niche_construction = 0,
						C_niche_construction = 0,
						D_niche_construction = 0,
						production_rate = 0,
						residence_time = 0)


#Note this model supports types which are not used.
#This section has had some functionality commented 
#out to emphasize what is being used in the simulation.

if type_A is not None:
	if model.isDecay():	
		model.initType(type = "A",
							A_niche_construction = int(type_A['A_niche_construction']),
							#B_niche_construction = int(type_A['B_niche_construction']),
							#C_niche_construction = int(type_A['C_niche_construction']),
							#D_niche_construction = int(type_A['D_niche_construction']),
							production_rate = int(type_A['production_rate']),
							residence_time = int(type_A['residence_time']))
	else:
		model.initType(type = "A",
							A_niche_construction = int(type_A['A_niche_construction']),
							#B_niche_construction = int(type_A['B_niche_construction']),
							#C_niche_construction = int(type_A['C_niche_construction']),
							#D_niche_construction = int(type_A['D_niche_construction']),
							production_rate = int(type_A['production_rate']))
else:
	initEmptyType(model,"A")

if type_B is not None:
	if model.isDecay():
		model.initType(type = "B",
							#A_niche_construction = int(type_B['A_niche_construction']),
							B_niche_construction = int(type_B['B_niche_construction']),
							#C_niche_construction = int(type_B['C_niche_construction']),
							#D_niche_construction = int(type_B['D_niche_construction']),
							production_rate = int(type_B['production_rate']),
							residence_time = int(type_B['residence_time']))
	else:
		model.initType(type = "B",
							#A_niche_construction = int(type_B['A_niche_construction']),
							B_niche_construction = int(type_B['B_niche_construction']),
							#C_niche_construction = int(type_B['C_niche_construction']),
							#D_niche_construction = int(type_B['D_niche_construction']),
							production_rate = int(type_B['production_rate']))
else:
	initEmptyType(model,"B")

if type_C is not None:
	model.initType(type = "C")#,
						#A_niche_construction = int(type_C['A_niche_construction']),
						#B_niche_construction = int(type_C['B_niche_construction']),
						#C_niche_construction = int(type_C['C_niche_construction']),
						#D_niche_construction = int(type_C['D_niche_construction']),
						#production_rate = int(type_C['production_rate']))

else:
	initEmptyType(model,"C")

if type_D is not None:
	model.initType(type = "D")#,
						#A_niche_construction = int(type_D['A_niche_construction']),
						#B_niche_construction = int(type_D['B_niche_construction']),
						#C_niche_construction = int(type_D['C_niche_construction']),
						#D_niche_construction = int(type_D['D_niche_construction']),
						#production_rate = int(type_D['production_rate']))

else:
	initEmptyType(model,"D")

sim.main(model,model.getOutputFile())