# configs
This directory contains the configuration files used to produce the figures for
Papale et al. (2025). Files are named for the figure data and output results
they correspond to.

The order of the parameters is not important, but parameters must be set
under their correct headings (eg. [Dials]). Parameters which are not included
will take on default values.

## [Dials]
Sets the simulation and environment parameters.

### seed
Integer value for the random seed, which allows pseudo-random number generation
to be reproducible.

**Default: A number will be generated.**

### timesteps
Integer value for the number of timesteps the simulation will run for.

**Default: 0**

**Note:** The simulation starts counting from timestep 0, so the last timestep
of the simulation will be *timesteps*-1.

### extinction_gap
Integer value for the number of timesteps between extinctions.

**Default: 0**

**Note:** An extinction occupies a timestep, so if *extinction_gap*=2 the
simulation will start at *t=0*, populations will grow for *t=1* and *t=2*, an
extinction occurs at *t=3* and population growth begins again at *t=4*.

### environment_x/y
Integer values for dimensions of environment's x and y dimensions. 
Each unit represents a GridCell micro-environment, so a 10x10 environment will 
contain 100 GridCell micro-environments.

**Default x: 0**
**Default y: 0**

### output_file
String filepath where resulting '.csv' and '.seed' files will be written to.

**Default: Current working directory**

**Note:** Relative filepaths are supported, but the current working directory
will be the working directory that initiated the simulation.

### decay
Boolean (True/False) which toggles whether the model will include decay 
functionality.

**Default: False**

**Note:** If decay is enabled then a [lifespan](#lifespan-(required-for-decay)) parameter must be
configured for both species, otherwise an error will be produced.

### diffusion
Boolean (True/False) which toggles whether the model will include diffusion 
functionality.

**Default: False**

**Note:** If diffusion is enabled then an environment larger than 1x1 is 
required.

### infinite_resources
Boolean (True/False) which toggles whether the model will include resource 
limitation.

**Default: False**

## [Species_X]
Sets the species-specific parameters.

While Species A and Species B are used throughout Papale et al. (2025), the
simulation supports a Species C and Species D for a maximum of 4 species in a
simulated run.

If a species is not configured it is not included in the simulation.

### X_niche_construction (required)
Integer value for the niche construction value of the indicated species. 
In this release, the parameter name must explicitly indicate the same species 
associated with the species of its associated header. This parameter must be
correctly configured to run the simulation.

Eg:<br/>
[Species_**A**]<br/>
**B**_niche_construction = 2

Will produce an error.

Eg:<br/>
[Species_**A**]<br/>
**A**_niche_construction = 2<br/>
**B**_niche_construction = 1

Will be accepted to correctly configure Species A, but will not apply any 
effects to Species B or its niche.

### lifespan (required for decay)
Integer value specifying the number of timesteps a particle of the species 
will persist in the population after it has been created. Particles created
at timestep *t* will be removed at timestep *t+1+lifespan*

Eg:<br/>
[Species_A]<br/>
A_niche_construction = 0<br/>
lifespan = 0<br/> 
production_bias = 1

Each timestep 1 particle will be produced, and any particles produced in the
previous timestep will be be removed. In this example, only 1 particle can be
produced in any timestep, so the population will always be 1 for all 
non-extinction timesteps.

### production_bias (required)
Integer value specifying the bias for production of a species by the 
environment. This value is interpreted differently depending on how
[infinite_resources](#infinite_resources) is configured.

**[infinite_resources](#infinite_resources) = True**
*production_bias* is the baseline number of particles that will be created before
niche effects are calculated.

**[infinite_resources](#infinite_resources) = False**
*production_bias* is a factor of the weighting in Bernoulli trials, as described
in the appendix Equation 2 of Papale et al. (2025).

# Template
Below is a blank sample template which can be configured to run your own 
simulations.
```
[Dials]
seed = *integer value*
timesteps = *integer value*
extinction_gap = *integer value*
environment_x = *integer value*
environment_y = *integer value*
output_file = *Filepath (do not surround in quotes)*
decay = *True/False*
diffusion = *True/False*
infinite_resources = *True/False*

[Species_A]
A_niche_construction = *integer value*
lifespan = *integer value*
production_bias = *integer value*

[Species_B]
B_niche_construction = *integer value*
lifespan = *integer value*
production_bias = *integer value*

[Species_C]
C_niche_construction = *integer value*
lifespan = *integer value*
production_bias = *integer value*

[Species_D]
D_niche_construction = *integer value*
lifespan = *integer value*
production_bias = *integer value*
```
