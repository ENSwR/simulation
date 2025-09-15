# **Overview**
The src directory contains the source code for the ENSwR simulation used in Papale 
et al. (2025) depicted in Figure A1. Files, classes and important methods, 
functions,and parameters are described below.

### Table of Contents
* [Software Map](#softwaremap)
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
* [sim.py](#simpy)
    + [Function: main](#function-main)
    + [Function: timeStep](#function-timestep)
    + [Function: extinctionTimeStep](#function-extinctiontimestep)
* [SimEngine.py](#simenginepy)
    + [Function: productionBiasLimited](#function-productionbiaslimited)
    + [Function: binomialDraw](#function-binomialdraw)
    + [Function: createResourceDoses](#function-createresourcedoses)
    + [Function: decay](#function-decay)
    + [Function: diffusion](#function-diffusion)
    + [Function: tallyResults](#function-tallyresults)
* [Environment.py](#environmentpy)
    - [Class: GridCell](#class-gridcell)
        + [Parameter: niche_X](#parameter-niche_x)
        + [Parameter: resource_doses](#parameter-resource_doses)
        + [Parameter: population](#parameter-population)
        + [Method: resourceDosesInflux](#method-resourcedosesinflux)
        + [Method: growPopulation](#method-growpopulation)
        + [Method: remove](#method-remove)
        + [Method: extinction](#method-extinction-gridcell)
    - [Class: Grid](#class-grid)
        + [Parameter: landcsape](#parameter-landscape)
        + [Method: initializeLandscape](#method-initializelandscape)
        + [Method: extinction](#method-extinction-grid)
* [Population.py](#populationpy)
    - [Class: Particle](#class-particle)
        + [Parameter: species](#parameter-species)
        + [Parameter: X_niche_construction](#parameter-X_niche_construction)
        + [Parameter: lifespan](#parameter-lifespan)
        + [Parameter: production_bias](#parameter-production_bias)
        + [Parameter: diffused](#parameter-diffused)
        + [Method: decay](#method-decay)
        + [Method: diffuse](#method-diffuse)

# Software Map
Figure A1 (Papale et al. 2025).

<p align="center">
    <img width="592" height="566" alt="image" src="https://github.com/user-attachments/assets/61d7f3bf-5569-455b-b518-d9f6c05cdd67" />
</p>


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

#### *Function: productionBiasLimited*
Responsible for calculating how many of each [Particle](#class-particle) 
species is produced by the environment in a timestep when infinite resources
are **enabled** using Appendix Equation 1 (Papale et al. 2025).

<p align="center">
<img width="534" height="44" alt="image" src="https://github.com/user-attachments/assets/bbba8370-1c82-4dd5-9c65-37361a192d29" />
</p>

#### *Function: binomialDraw*
Responsible for calculating how many of each [Particle](#class-particle) 
species is produced by the environment in a timestep when infinite resources
are **disabled** using Appendix Equation 2 (Papale et al. 2025).

<p align="center">
<img width="579" height="129" alt="image" src="https://github.com/user-attachments/assets/1e979517-5a97-485a-b18d-ae799ddf15f0" />
</p>

#### *Function: createResourceDoses*
Invokes [resourceDosesInflux](#method-resourcedosesinflux).

#### *Function: decay*
Handles back-end logic for implementing decay functionality on populations
and invokes Particles to [decay](#method-decay).

#### *Function: diffusion*
Handles logic for diffusion processes. Receives Particle coordinates, performs
bound-checks, and passes new coordinates to environment to [add individuals](#method-growpopulation) 
to a new population and [remove them](#method-remove) from the old population.

#### *Function: tallyResults*
Counts [GridCell](#class-gridcell) populations and niche property data 
to return to [sim](#simpy) (**tallyResults**).

## Environment.py
Represents an environment of *n*x*m* micro-environments. Contains the 
[Grid](#class-grid) and [GridCell](#class-gridcell) classes.

### Class: GridCell
Represents a micro-environment. This class stores [niche properties](#parameter-niche_x), 
[available resources](#parameter-resource_doses), and its [population](#parameter-population).

#### *Parameter: niche_X*
Float value for the accumulating niche property of a given species *X*

#### *Parameter: resource_doses*
Integer value for the number of resource doses remaining in a [microenvironment](#class-gridcell)
under resource-limited models.

#### *Parameter: population*
A list containing [particle](#class-particle) instances representing a population.

#### *Method: resourceDosesInflux*
Replenishes [resources](#parameter-resource_doses) for the [microenvironment](#class-gridcell).

#### *Method: growPopulation*
Adds a new [particle](#class-particle) instance to the [population](#parameter-population) list.

#### *Method: remove*
Removes a specific [particle](#class-particle) instance from the [population](#parameter-population) list.

#### *Method: extinction (GridCell)*
Handles logic for rare extinction survival if [diffusion](#parameter-diffusion) is enabled.

Otherwise, replaces its [population](#parameter-population) with an empty list.

### Class: Grid
Represents the environment as a collection of [GridCells](#class-gridcell).

#### *Parameter: landcsape*
*n*x*m* numpy array of [GridCell](#class-gridcell) objects

#### *Method: initializeLandscape*
Creates the *n*x*m* array of [GricCells](#class-gridcell).

#### *Method: extinction (Grid)*
Invokes [extinction](#method-extinction-gridcell) in each [GridCell](#class-gridcell) of
the [landscape](#parameter-landscape).

## Population.py
Contains the [Particle](#class-particle) class. 

### Class: Particle
Each instance of this class represents an individual particle.

#### *Parameter: species*
Character variable which denotes which species the individual belongs to.

#### *Parameter: X_niche_construction*
Integer value representing the niche construction ability of a denoted species *X*

#### *Parameter: lifespan*
Integer value which stores the remaining timesteps for a particle to persist in the
simulation if [decay](#parameter-decay) is enabled.

#### *Parameter: production_bias*
Integer value representing strength of inherent bias for a denoted species *X* to be produced.

#### *Parameter: diffused*
Boolean (True/False) variable which flags when a particle has survive an extinction and diffused
in [diffusion](#parameter-diffusion) enabled models. This prevents particles from diffusing
more than once if they land in a new [GridCell](#class-gridcell) where extinction/diffusion has 
not yet been calculted for the timestep.

#### *Method: decay*
Reduces the individual's [lifespan](#parameter-lifespan) by 1.

#### *Method: diffuse*
Reports a random direction of diffusion to the [diffusion function of the SimEngine](#function-diffusion)

