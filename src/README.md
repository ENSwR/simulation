# src
This directory contains the source code for the ENSwR simulation used in Papale 
et al. (2025) depicted in Figure A1. Important class methods are given in bold 
parentheses, while important parameters are given in italicized parantheses.

## run_sim
Initial launch point for the simulation.

This script is responsible for parsing the configuration file and 
initializing the [Model](#class:-model). The initialized [Model](#class:-model) 
instance is then passed to the [sim](#sim).

## Dials
Contains the [Model](#class:-model) Class.

### Class: Model
This class defines the model details and associated parameters and settings for
the simulation (*output_file*, *timesteps*, *extinction_gap*, *env_x*, *env_y*,
*decay*, *diffusion*, *infinite_resources*, *seed*) and each species 
(*species_X*). Species are stored as dictionaries where each of their parameters 
are a key with an associated value.

## sim
The main method (**main**) is responsible for parsing the [Model](#class:-model)
, initializing the [Environment](#environment), counting timestep (*t*), and 
invoking the [SimEngine](#simengine) to perform functions in sequence for 
timesteps (**timestep**), extinction timesteps (**extinctionTimestep**), and
additional diffusion if specified in the [Model](#class:-model).

The **timestep** and **extinctionTimestep** functions return tallied results
for the timestep produced by the [SimEngine](#simengine).

At the end of the simulation, **main** compiles all timestep results and 
outputs the .csv file, along with an associated .seed file.

## SimEngine
Handles core functionalities and computations for the simulation.

Responsible for calculating how many of each [Particle](#class:-particle) 
species is produced by the environment in a timestep 
(**productionBiasLimited** for infinite resource simulations and 
**binomialDraw** for limited resource simulations).

Invokes the [Environment](#environment) to replenish resources 
(**createResourceDoses**).

Invokes Particles to decay (**decay**).

Handles logic for diffusion processes 
(**diffusion** and **resetDiffusionStatus**).

Counts populations and fetches niche property data from 
[Environment](#environment) to return to [sim](#sim) (**tallyResults**).

## Environment
Represents an environment of *n*x*m* micro-environments. Contains the 
[Grid](#class:-grid) and [GridCell](#class:-gridcell) classes.

### Class: GridCell
Represents a micro-environment. This class stores niche properties (*niche_X*), 
available resources (*resource_doses*), and stores its population as a list 
(*population*) of [Particle](#class:-particle) object instances.

This class is responsible for replenishing resources (**resourceDosesInflux**), 
adding new [Particles](#class:-particle) to its population (**growPopulation**), 
removing [Particles](#class:-particle) from population (**remove**), and 
inflicting extinctions on its population (**extinction**).

### Class: Grid
Represents the environment as a collection of [GridCells](#class:-gridcell).

This class creates the environment by initializing an array of 
[GridCell](#class:-gridcell) objects (**initializeLandscape**). It is also 
responsible for performing mass-extinctions (**extinction**) by invoking the 
extinction method of the [GridCells](#class:-gridcell) in its array.

## Population
Contains the [Particle](#class:-particle) class. 

### Class: Particle
Each instance of this class represents an individual particle.

Particles have a species (*species*), niche construction effect 
(*X_niche_construction*), remaining lifespan (*lifespan*) for decay models,
production bias (*production_bias*), and a boolean flag to signal if a particle
has diffused during a timestep for diffusion models (*diffused*).

Particles are responsible for decaying (**decay**) and reporting their movement
to the [SimEngine](#simengine) during a diffusion event (**diffuse**).

