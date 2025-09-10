class Model:
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls)

	def __init__ (self, output_file = "",
						timesteps = 0, 
						extinction_gap = 0, 
						species_A = {}, 
						species_B = {}, 
						species_C = {}, 
						species_D = {},
						env_x = 0,
						env_y = 0,
						decay = False,
						diffusion = False,
						infinite_resources = False,
						seed = 0):
		self.output_file = output_file
		self.timesteps = timesteps
		self.extinction_gap = extinction_gap
		self.species_A = species_A
		self.species_B = species_B
		self.species_C = species_C
		self.species_D = species_D
		self.env_x = env_x
		self.env_y = env_y
		self.decay = bool(decay)
		self.diffusion = bool(diffusion)
		self.infinite_resources = bool(infinite_resources)
		self.seed = seed


	def isInfiniteResources(self):
		return self.infinite_resources
	def isDecay(self):
		return self.decay
	def getEnvX(self):
		return self.env_x
	def getEnvY(self):
		return self.env_y
	def setTimesteps(self, timesteps = 0):
		self.timesteps = timesteps
	def setDiffusion(self, diffusion = False):
		self.diffusion = diffusion
	def isDiffusion(self):
		return self.diffusion
	def setExtinctionGap(self, extinction_gap = 0):
		self.extinction_gap = extinction_gap
	def setSeed(self, seed = 0):
		self.seed = seed

	#Note: this simulation supports, or has partially developed
	#machinery for a range of functions such a toxin/antidote
	#interactions between species, or impacts of one species
	#on other niches.

	def initSpecies(self, species = "",
					niche_construction = 0,
					A_niche_construction = 0, 
					B_niche_construction = 0,
					C_niche_construction = 0,
					D_niche_construction = 0,
					toxin_str = 0,
					toxin_rad = 0,
					antidote_str = 0,
					antidote_rad = 0,
					lifespan = 0,
					production_bias = 0):

		if species == "A":
			self.species_A = {"species":species, 
						"niche_construction":niche_construction,
						"A_niche_construction":A_niche_construction,
						"B_niche_construction":B_niche_construction,
						"C_niche_construction":C_niche_construction,
						"D_niche_construction":D_niche_construction, 
						"toxin_str":toxin_str, 
						"toxin_rad":toxin_rad, 
						"antidote_str":antidote_str, 
						"antidote_rad":antidote_rad,
						"lifespan":lifespan,
						"production_bias":production_bias}

		elif species == "B":
			self.species_B = {"species":species, 
						"niche_construction":niche_construction,
						"A_niche_construction":A_niche_construction,
						"B_niche_construction":B_niche_construction,
						"C_niche_construction":C_niche_construction,
						"D_niche_construction":D_niche_construction, 
						"toxin_str":toxin_str, 
						"toxin_rad":toxin_rad, 
						"antidote_str":antidote_str, 
						"antidote_rad":antidote_rad,
						"lifespan":lifespan,
						"production_bias":production_bias}

		elif species == "C":
			self.species_C = {"species":species, 
						"niche_construction":niche_construction,
						"A_niche_construction":A_niche_construction,
						"B_niche_construction":B_niche_construction,
						"C_niche_construction":C_niche_construction,
						"D_niche_construction":D_niche_construction, 
						"toxin_str":toxin_str, 
						"toxin_rad":toxin_rad, 
						"antidote_str":antidote_str, 
						"antidote_rad":antidote_rad,
						"lifespan":lifespan,
						"production_bias":production_bias}

		elif species == "D":
			self.species_D = {"species":species, 
						"niche_construction":niche_construction,
						"A_niche_construction":A_niche_construction,
						"B_niche_construction":B_niche_construction,
						"C_niche_construction":C_niche_construction,
						"D_niche_construction":D_niche_construction, 
						"toxin_str":toxin_str, 
						"toxin_rad":toxin_rad, 
						"antidote_str":antidote_str, 
						"antidote_rad":antidote_rad,
						"lifespan":lifespan,
						"production_bias":production_bias}
		else:
			print ("Unrecognized species: " + str(species))
	
	def getTimesteps(self):
		return self.timesteps
	def getExtinctionGap(self):
		return self.extinction_gap
	def getSeed(self):
		return self.seed
	def getSpeciesA(self):
		return self.species_A
	def getSpeciesB(self):
		return self.species_B
	def getSpeciesC(self):
		return self.species_C
	def getSpeciesD(self):
		return self.species_D
	def getOutputFile(self):
		return self.output_file
	
	def toString(self):
		message = "[Dials]\n"\
		+"seed = " + str(self.seed)+"\n"
		+"timesteps = " + str(self.timesteps)+"\n"\
		+"extinction_gap = " + str(self.extinction_gap)+"\n"\
		+"environment_x = " + str(self.env_x)+"\n"\
		+"environment_y = " + str(self.env_y)+"\n"\
		+"output_file = " + str(self.output_file)+"\n"\
		+"decay = " + str(self.decay)+"\n"\
		+"diffusion = " + str(self.diffusion)+"\n"\
		+"infinite_resources = " + str(self.infinite_resources)+"\n"\
		+"\n[Species_A]\n"
		temp_str = str(self.species_A).replace(', ','\n').replace(': ', ' = ').replace('{','').replace('}','').replace("'",'')+"\n"
		message += temp_str
		message += "\n[Species_B]\n"
		temp_str = str(self.species_B).replace(', ','\n').replace(': ', ' = ').replace('{','').replace('}','').replace("'",'')+"\n"
		message += temp_str
		message +="\n[Species_C]\n"
		temp_str = str(self.species_C).replace(', ','\n').replace(': ', ' = ').replace('{','').replace('}','').replace("'",'')+"\n"
		message += temp_str
		message += "\n[Species_D]\n"
		temp_str = str(self.species_D).replace(', ','\n').replace(': ', ' = ').replace('{','').replace('}','').replace("'",'')+"\n"
		message += temp_str

		return message