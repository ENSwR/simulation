class Model:
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls)

	def __init__ (self, output_file = ".",
						timesteps = 0, 
						extinction_gap = 0, 
						type_A = {}, 
						type_B = {}, 
						type_C = {}, 
						type_D = {},
						env_x = 0,
						env_y = 0,
						decay = False,
						diffusion = False,
						infinite_resources = False,
						seed = 0):
		self.output_file = output_file
		self.timesteps = timesteps
		self.extinction_gap = extinction_gap
		self.type_A = type_A
		self.type_B = type_B
		self.type_C = type_C
		self.type_D = type_D
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
	#interactions between types, or impacts of one type
	#on other niches.

	def initType(self, type = "",
					A_niche_construction = 0, 
					B_niche_construction = 0,
					C_niche_construction = 0,
					D_niche_construction = 0,
					lifespan = 0,
					production_rate = 0):

		#Uncommenting the lines allows for units to construct niches
		#for other units, or destroy each other's niches.
		#This has been removed for this release to simplify configuration. 
		if type == "A":
			self.type_A = {"type":type, 
						"A_niche_construction":A_niche_construction,
						#"B_niche_construction":B_niche_construction,
						#"C_niche_construction":C_niche_construction,
						#"D_niche_construction":D_niche_construction, 
						"lifespan":lifespan,
						"production_rate":production_rate}

		elif type == "B":
			self.type_B = {"type":type, 
						#"A_niche_construction":A_niche_construction,
						"B_niche_construction":B_niche_construction,
						#"C_niche_construction":C_niche_construction,
						#"D_niche_construction":D_niche_construction,
						"lifespan":lifespan,
						"production_rate":production_rate}

		elif type == "C":
			self.type_C = {"type":type, 
						#"A_niche_construction":A_niche_construction,
						#"B_niche_construction":B_niche_construction,
						"C_niche_construction":C_niche_construction,
						#"D_niche_construction":D_niche_construction,
						"lifespan":lifespan,
						"production_rate":production_rate}

		elif type == "D":
			self.type_D = {"type":type, 
						#"A_niche_construction":A_niche_construction,
						#"B_niche_construction":B_niche_construction,
						#"C_niche_construction":C_niche_construction,
						"D_niche_construction":D_niche_construction,
						"lifespan":lifespan,
						"production_rate":production_rate}
		else:
			print ("Unrecognized type: " + str(type))
	
	def getTimesteps(self):
		return self.timesteps
	def getExtinctionGap(self):
		return self.extinction_gap
	def getSeed(self):
		return self.seed
	def getTypeA(self):
		return self.type_A
	def getTypeB(self):
		return self.type_B
	def getTypeC(self):
		return self.type_C
	def getTypeD(self):
		return self.type_D
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
		+"\n[Type_A]\n"
		temp_str = str(self.type_A).replace(', ','\n').replace(': ', ' = ').replace('{','').replace('}','').replace("'",'')+"\n"
		message += temp_str
		message += "\n[Type_B]\n"
		temp_str = str(self.type_B).replace(', ','\n').replace(': ', ' = ').replace('{','').replace('}','').replace("'",'')+"\n"
		message += temp_str
		message +="\n[Type_C]\n"
		temp_str = str(self.type_C).replace(', ','\n').replace(': ', ' = ').replace('{','').replace('}','').replace("'",'')+"\n"
		message += temp_str
		message += "\n[Type_D]\n"
		temp_str = str(self.type_D).replace(', ','\n').replace(': ', ' = ').replace('{','').replace('}','').replace("'",'')+"\n"
		message += temp_str

		return message