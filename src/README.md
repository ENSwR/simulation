# **Overview**
The src directory contains the source code for the ENSwR simulation used in Papale 
et al. (2025) depicted in Figure A1. Files, classes and important methods, 
functions,and parameters are described below.

### Table of Contents
* [run_sim.py](#run_simpy)
* [Dials.py](#dialspy)
    - [Class: Model](#class-model)
        + [Parameter: species_X](#parameter-species_x)
        + [Parameter: output_file](#parameter-output_file)
        + [Parameter: timesteps](#parameter-timesteps)
        + [Parameter: extinction_gap](#parameter-extinction_gap)
        + [Parameter: env_x/y](#parameter-env_xy)
        + [Parameter: decay](#parameter-decay)
        + [Parameter: diffusion](#parameter-diffusion)
        + [Parameter: infinite_resources](#parameter-infinite_resources)
        + [Parameter: seed](#parameter-seed)
* [sim.py](#simpy)<br\>
        + [Function: main](#function-main)
        + [Function: timeStep](#function-timestep)
        + [Function: extinctionTimeStep](#function-extinctiontimestep)
* [SimEngine.py](#simenginepy)
* [Environment.py](#environmentpy)
    - [Class: GridCell](#class-gridcell)
    - [Class: Grid](#class-grid)
* [Population.py](#populationpy)
    - [Class: Particle](#class-particle)

## run_sim.py
Initial launch point for the simulation.

This script is responsible for parsing the configuration file and 
initializing the [Model](#class-model). The initialized [Model](#class-model) 
instance is then passed to the [sim](#simpy).

## Dials.py
Contains the [Model](#class-model) Class.

### Class: Model
This class defines the model details and associated parameters and settings for
the simulation. 

See [configs/README.md](https://github.com/ENSwR/simulation/tree/main/configs) 
for additional details about parameters.

#### *Parameter: species_X*
Species and their associated settings are stored as dictionaries with their
attributes as keys with associated values.

#### *Parameter: output_file*
Filepath as a string to direct output for results .csv and .seed files.

#### *Parameter: timesteps*
Integer value for how many timesteps the simulation will run.

#### *Parameter: extinction_gap*
Integer value for how many timesteps will occur in between extinction timesteps.

#### *Parameter: env_x/y*
Integer value for dimensions of the environment dimensions in units of 
[GridCells](#class-gridcell). 

#### *Parameter: decay*
Boolean (True/False) setting to enable/disable decay of particles in the model.

#### *Parameter: diffusion*
Boolean (True/False) setting to enable/disable diffusion of particles in the model.

#### *Parameter: infinite_resources*
Boolean (True/False) setting to enable/disable infinite resources in the model.
If True, model populations will grow using [productionBiasLimited](#method-productionbiaslimited).
If False, model populations will grow using [binomialDraw](#method-binomialdraw).

#### *Parameter: seed*
Integer value to set seed value for pseudo-randomly generating numbers.

## sim.py
Handles parsing of configuration file to initialize [Model](#class-model) and 
[Environment](#environmentpy). Coordinates logistics of moving through timesteps and
produces output results.

#### *Function: main*

The [main](#function-main) function is responsible for parsing the [Model](#class-model)
and initializing the [Environment](#environmentpy). This method drives the simulation
by iterating through timesteps and book-keeping logic around [timesteps](#parameter-timesteps) 
and [extinction gaps](#parameter-extinction-gap), trigggering invoking 
[extinction](#method-extinctiongrid) when required. 

This function invokes the [SimEngine](#simengine) to perform [diffusion](#function-diffusion) functions.


This function invokes [timeStep](#function-timestep) and 
[extinctionTimestep](function-extinctiontimestep), and compiles their returned results
to produce the output .csv results, and the simulation's .seed file.

#### *Function: timeStep*
Invokes the [SimEngine](#simenginepy) [binomialDraw](#function-binomialdraw) or 
[productionBiasLimited](#function-productionbiaslimited) depending on the [model's](#class-model)
[infinite resource](#paramater-infinite_resources) settings.

Also invokes the [SimEngine](#simenginepy) to [tally results](#function-tallyresults), returning
results to [main](#function-main).

#### *Function: extinctionTimeStep*
Performs a non-generative timestep where an extinction has happened.

Similar to [timeStep](#function-timestep), invokes the [SimEngine](#simenginepy) to 
[tally results](#function-tallyresults), returning results to [main](#function-main).

## SimEngine.py
Handles core functionalities and computations for the simulation.

Responsible for calculating how many of each [Particle](#class-particle) 
species is produced by the environment in a timestep 
(**productionBiasLimited** for infinite resource simulations and 
**binomialDraw** for limited resource simulations).

Invokes the [Environment](#environmentpy) to replenish resources 
(**createResourceDoses**).

Invokes Particles to decay (**decay**).

Handles logic for diffusion processes 
(**diffusion** and **resetDiffusionStatus**).

Counts populations and fetches niche property data from 
[Environment](#environmentpy) to return to [sim](#simpy) (**tallyResults**).

## Environment.py
Represents an environment of *n*x*m* micro-environments. Contains the 
[Grid](#class-grid) and [GridCell](#class-gridcell) classes.

### Class: GridCell
Represents a micro-environment. This class stores niche properties (*niche_X*), 
available resources (*resource_doses*), and stores its population as a list 
(*population*) of [Particle](#class-particle) object instances.

This class is responsible for replenishing resources (**resourceDosesInflux**), 
adding new [Particles](#class-particle) to its population (**growPopulation**), 
removing [Particles](#class-particle) from population (**remove**), and 
inflicting extinctions on its population (**extinction**).

### Class: Grid
Represents the environment as a collection of [GridCells](#class-gridcell).

This class creates the environment by initializing an array of 
[GridCell](#class-gridcell) objects (**initializeLandscape**). It is also 
responsible for performing mass-extinctions (**extinction**) by invoking the 
extinction method of the [GridCells](#class-gridcell) in its array.

## Population.py
Contains the [Particle](#class-particle) class. 

### Class: Particle
Each instance of this class represents an individual particle.

Particles have a species (*species*), niche construction effect 
(*X_niche_construction*), remaining lifespan (*lifespan*) for decay models,
production bias (*production_bias*), and a boolean flag to signal if a particle
has diffused during a timestep for diffusion models (*diffused*).

Particles are responsible for decaying (**decay**) and reporting their movement
to the [SimEngine](#simenginepy) during a diffusion event (**diffuse**).

