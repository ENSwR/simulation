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

#### *<ins>Parameter: species_X</ins>*
Species and their associated settings are stored as dictionaries with their
attributes as keys with associated values.

#### *<ins>Parameter: output_file</ins>*
Filepath as a string to direct output for results .csv and .seed files.

#### *<ins>Parameter: timesteps</ins>*
Integer value for how many timesteps the simulation will run.

#### *<ins>Parameter: extinction_gap</ins>*
Integer value for how many timesteps will occur in between extinction timesteps.

#### *<ins>Parameter: env_x/y</ins>*
Integer value for dimensions of the environment dimensions in units of 
[GridCells](#class-gridcell). 

#### *<ins>Parameter: decay</ins>*
Boolean (True/False) setting to enable/disable decay of particles in the model.

#### *<ins>Parameter: diffusion</ins>*
Boolean (True/False) setting to enable/disable diffusion of particles in the model.

#### *<ins>Parameter: infinite_resources</ins>*
Boolean (True/False) setting to enable/disable infinite resources in the model.
If True, model populations will grow using [productionBiasLimited](#function-productionbiaslimited).
If False, model populations will grow using [binomialDraw](#function-binomialdraw).

#### *<ins>Parameter: seed</ins>*
Integer value to set seed value for pseudo-randomly generating numbers.

## sim.py
Handles parsing of configuration file to initialize [Model](#class-model) and 
[Environment](#environmentpy). Coordinates logistics of moving through timesteps and
produces output results.

#### *<ins>Function: main</ins>*

The [main](#function-main) function is responsible for parsing the [Model](#class-model)
and initializing the [Environment](#environmentpy). This method drives the simulation
by iterating through timesteps and book-keeping logic around [timesteps](#parameter-timesteps) 
and [extinction gaps](#parameter-extinction-gap), trigggering invoking 
[extinction](#method-extinctiongrid) when required. 

This function invokes the [SimEngine](#simengine) to perform [diffusion](#function-diffusion) functions.

This function invokes [timeStep](#function-timestep) and 
[extinctionTimestep](function-extinctiontimestep), and compiles their returned results
to produce the output .csv results, and the simulation's .seed file.

#### *<ins>Function: timeStep</ins>*
Invokes the [SimEngine](#simenginepy) [binomialDraw](#function-binomialdraw) or 
[productionBiasLimited](#function-productionbiaslimited) depending on the [model's](#class-model)
[infinite resource](#paramater-infinite_resources) settings.

Also invokes the [SimEngine](#simenginepy) to [tally results](#function-tallyresults), returning
results to [main](#function-main).

#### *<ins>Function: extinctionTimeStep</ins>*
Performs a non-generative timestep where an extinction has happened.

Similar to [timeStep](#function-timestep), invokes the [SimEngine](#simenginepy) to 
[tally results](#function-tallyresults), returning results to [main](#function-main).

## SimEngine.py
Handles core functionalities and computations for the simulation.

#### *<ins>Function: productionBiasLimited</ins>*
Responsible for calculating how many of each [Particle](#class-particle) 
species is produced by the environment in a timestep when infinite resources
are **enabled** using [appendix](https://github.com/ENSwR/simulation/blob/main/appendix.pdf) 
Equation 1 (Papale et al. 2025).

<p align="center">
<img width="534" height="44" alt="image" src="https://github.com/user-attachments/assets/bbba8370-1c82-4dd5-9c65-37361a192d29" />
</p>

#### *<ins>Function: binomialDraw</ins>*
Responsible for calculating how many of each [Particle](#class-particle) 
species is produced by the environment in a timestep when infinite resources
are **disabled** using Bernoulli trials with probabilities deteremined by
[appendix](https://github.com/ENSwR/simulation/blob/main/appendix.pdf) 
Equation 2 (Papale et al. 2025).

<p align="center">
<img width="579" height="129" alt="image" src="https://github.com/user-attachments/assets/1e979517-5a97-485a-b18d-ae799ddf15f0" />
</p>

#### *<ins>Function: createResourceDoses</ins>*
Invokes [resourceDosesInflux](#method-resourcedosesinflux).

#### *<ins>Function: decay</ins>*
Handles back-end logic for implementing decay functionality on populations
and invokes Particles to [decay](#method-decay).

#### *<ins>Function: diffusion</ins>*
Handles logic for diffusion processes. Receives Particle coordinates, performs
bound-checks, and passes new coordinates to environment to [add individuals](#method-growpopulation) 
to a new population and [remove them](#method-remove) from the old population.

#### *<ins>Function: tallyResults</ins>*
Counts [GridCell](#class-gridcell) populations and niche property data 
to return to [sim](#simpy) (**tallyResults**).

## Environment.py
Represents an environment of *n*x*m* micro-environments. Contains the 
[Grid](#class-grid) and [GridCell](#class-gridcell) classes.

### Class: GridCell
Represents a micro-environment. This class stores [niche properties](#parameter-niche_x), 
[available resources](#parameter-resource_doses), and its [population](#parameter-population).

#### *<ins>Parameter: niche_X</ins>*
Float value for the accumulating niche property of a given species *X*

#### *<ins>Parameter: resource_doses</ins>*
Integer value for the number of resource doses remaining in a [microenvironment](#class-gridcell)
under resource-limited models.

#### *<ins>Parameter: population</ins>*
A list containing [particle](#class-particle) instances representing a population.

#### *<ins>Method: resourceDosesInflux</ins>*
Replenishes [resources](#parameter-resource_doses) for the [microenvironment](#class-gridcell).

#### *<ins>Method: growPopulation</ins>*
Adds a new [particle](#class-particle) instance to the [population](#parameter-population) list.

#### *<ins>Method: remove</ins>*
Removes a specific [particle](#class-particle) instance from the [population](#parameter-population) list.

#### *<ins>Method: extinction (GridCell)</ins>*
Handles logic for rare extinction survival if [diffusion](#parameter-diffusion) is enabled.

Otherwise, replaces its [population](#parameter-population) with an empty list.

### Class: Grid
Represents the environment as a collection of [GridCells](#class-gridcell).

#### *<ins>Parameter: landcsape</ins>*
*n*x*m* numpy array of [GridCell](#class-gridcell) objects

#### *<ins>Method: initializeLandscape</ins>*
Creates the *n*x*m* array of [GricCells](#class-gridcell).

#### *Method: extinction (Grid)</ins>*
Invokes [extinction](#method-extinction-gridcell) in each [GridCell](#class-gridcell) of
the [landscape](#parameter-landscape).

## Population.py
Contains the [Particle](#class-particle) class. 

### Class: Particle
Each instance of this class represents an individual particle.

#### *<ins>Parameter: species</ins>*
Character variable which denotes which species the individual belongs to.

#### *<ins>Parameter: X_niche_construction</ins>*
Integer value representing the niche construction ability of a denoted species *X*

See [configs/README.md](https://github.com/ENSwR/simulation/tree/main/configs#x_niche_construction-required) 
for additional details about this parameters

#### *<ins>Parameter: lifespan</ins>*
Integer value which stores the remaining timesteps for a particle to persist in the
simulation if [decay](#parameter-decay) is enabled.

See [configs/README.md](https://github.com/ENSwR/simulation/tree/main/configs##lifespan-required-for-decay) 
for additional details about this parameters

#### *<ins>Parameter: production_bias</ins>*
Integer value representing strength of inherent bias for a denoted species *X* to be produced.

See [configs/README.md](https://github.com/ENSwR/simulation/tree/main/configs#production_bias-required) 
for additional details about this parameters

#### *<ins>Parameter: diffused</ins>*
Boolean (True/False) variable which flags when a particle has survive an extinction and diffused
in [diffusion](#parameter-diffusion) enabled models. This prevents particles from diffusing
more than once if they land in a new [GridCell](#class-gridcell) where extinction/diffusion has 
not yet been calculted for the timestep.

#### *<ins>Method: decay</ins>*
Reduces the individual's [lifespan](#parameter-lifespan) by 1.

#### *<ins>Method: diffuse</ins>*
Reports a random direction of diffusion to the [diffusion function of the SimEngine](#function-diffusion)

