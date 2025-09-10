import Dials

A_niche = 0
B_niche = 0
A_prod = 1
B_prod = 2
isDecay = True

for infinite_resources in [True,False]:
	#Uncomment to toggle between decays
	for A_decay in range(1):
		A_decay = 21
	#for A_decay in range(1,45,5):
		for B_decay in range(1):
			B_decay = 47
		#for B_decay in range(A_decay+1,50,5):
			for A_niche in range(1):
				A_niche = 5
			#for A_niche in range(1,12,4):
				for B_niche in range(1):
					B_niche = 2
				#for B_niche in range(0,A_niche+1):
					output_file = "resource:"+str(infinite_resources)+"_decay:"+str(isDecay)+"_A_lifespan:"+str(A_decay)+"_buffer:"+str(A_niche)+"_prod:"+str(A_prod)+"_B_lifespan:"+str(B_decay)+"_buffer:"+str(B_niche)+"_prod:"+str(B_prod)
					
					model = Dials.Model(output_file = output_file+'.csv',
						timesteps = int(200),
						gen_length = int(50),
						env_x = int(1),
						env_y = int(1),
						decay = isDecay,
						migration = False,
						infinite_resources = infinite_resources)

					model.initSpecies(variant = "A",
										A_buffer_effect = int(A_niche),
										B_buffer_effect = int(0),
										C_buffer_effect = int(0),
										D_buffer_effect = int(0),
										prod_capacity = A_prod,
										lifespan = int(A_decay))
					model.initSpecies(variant = "B",
										A_buffer_effect = int(0),
										B_buffer_effect = int(B_niche),
										C_buffer_effect = int(0),
										D_buffer_effect = int(0),
										prod_capacity = B_prod,
										lifespan = int(B_decay))
					model.initSpecies(variant = "C",
										A_buffer_effect = int(0),
										B_buffer_effect = int(0),
										C_buffer_effect = int(0),
										D_buffer_effect = int(0),
										prod_capacity = int(0),
										lifespan = int(0))
					model.initSpecies(variant = "D",
										A_buffer_effect = int(0),
										B_buffer_effect = int(0),
										C_buffer_effect = int(0),
										D_buffer_effect = int(0),
										prod_capacity = int(0),
										lifespan = int(0))
					with open(output_file+'.config','w') as file:
						file.write(model.toString())