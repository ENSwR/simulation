# **Overview**
This directory contains the configuration files used to produce the figures for
Papale et al. (2025). Files are named for the figure data and output results
they correspond to.

The order of the parameters is not important, but parameters must be set
under their correct headings (eg. [Dials]). Parameters which are not included
will take on default values.

### Table of Contents
* [Dials](#dials)
    + [seed](#seed)
    + [timesteps](#timesteps)
    + [extinction_gap](#extinction_gap)
    + [environment_x/y](#envirionment_xy)
    + [output_file](#output_file)
    + [decay](#decay)
    + [diffusion](#diffusion)
    + [infinite_resources](#infinite_resources)
* [Type_X](#type_x)
    + [X_niche_construction](#x_niche_construction-required)
    + [lifespan](#lifespan-required-for-decay)
    + [production_rate](#production_rate-required)

## [Dials]
Sets the simulation and environment parameters.

### <ins>seed</ins>
Integer value for the random seed, which allows pseudo-random number generation
to be reproducible.

**Default: A number will be generated.**

### <ins>timesteps</ins>
Integer value for the number of timesteps the simulation will run for.

**Default: 0**

**Note:** The simulation starts counting from timestep 0, so the last timestep
of the simulation will be *timesteps*-1.

### <ins>extinction_gap</ins>
Integer value for the number of timesteps between extinctions.

**Default: 0**

**Note:** An extinction occupies a timestep, so if *extinction_gap*=2 the
simulation will start at *t=0*, populations will grow for *t=1* and *t=2*, an
extinction occurs at *t=3* and population growth begins again at *t=4*.

### <ins>environment_x/y</ins>
Integer values for dimensions of environment's x and y dimensions. 
Each unit represents a GridCell micro-environment, so a 10x10 environment will 
contain 100 GridCell micro-environments.

**Default x: 0**
**Default y: 0**

### <ins>output_file</ins>
String filepath where resulting '.csv' and '.seed' files will be written to.

**Default: Current working directory**

**Note:** Relative filepaths are supported, but the current working directory
will be the working directory that initiated the simulation.

### <ins>decay</ins>
Boolean (True/False) which toggles whether the model will include decay 
functionality.

**Default: False**

**Note:** If decay is enabled then a [lifespan](#lifespan-(required-for-decay)) parameter must be
configured for both types, otherwise an error will be produced.

### <ins>diffusion</ins>
Boolean (True/False) which toggles whether the model will include diffusion 
functionality.

**Default: False**

**Note:** If diffusion is enabled then an environment larger than 1x1 is 
required.

### <ins>infinite_resources</ins>
Boolean (True/False) which toggles whether the model will include resource 
limitation.

**Default: False**

## [Type_X]
Sets the type-specific parameters.

While Type A and Type B are used throughout Papale et al. (2025), the
simulation supports a Type C and Type D for a maximum of 4 types in a
simulated run.

If a type is not configured it is not included in the simulation.

### <ins>X_niche_construction</ins> (required)
Integer value for the niche construction value of the indicated type. 
In this release, this parameter name must explicitly indicate the same type 
associated with its header's type. This parameter must be
correctly configured to run the simulation.

Eg:<br/>
```
[Type_A]
B_niche_construction = 2
```
Will produce an error.

Eg:<br/>
```
[Type_A]
A_niche_construction = 2
B_niche_construction = 1
```
Will be accepted to correctly configure Type A, but will not implement any 
effects to Type B or its niche.

Negative values are not explicitly prevented, but may result in a invalid negative
weight error when [infinite_resources](#infinite_resources) is *False*.

**Note:** This simulation can support types affecting each other's
niches. However, [u]this has been disabled for this release[/u]. It can be enabled by 
uncommenting the lines noted in [../src/Dials.py](https://github.com/ENSwR/simulation/blob/main/src/Dials.py)
although it may not be fully developed and may not function as expected. In this
case, the second example above will allow Type A to impact Type B's niche as well as
its own when it is created.

### <ins>lifespan</ins> (required for decay)
Integer value specifying the number of timesteps a unit of the type 
will persist in the population after it has been created. Units created
at timestep *t* will be removed at timestep *t+1+lifespan*

Eg:<br/>
```
[Type_A]
A_niche_construction = 0
lifespan = 0
production_rate = 1
```

Each timestep 1 unit will be produced, and any units produced in the
previous timestep will be be removed. In this example, only 1 unit can be
produced in any timestep, so the population will always be 1 for all 
non-extinction timesteps.

### <ins>production_rate</ins> (required)
Integer value specifying the rate for production of a type by the 
environment. This value is interpreted differently depending on how
[infinite_resources](#infinite_resources) is configured.

Negative values are not explicitly prevented, but may result in a invalid negative
weight error when [infinite_resources](#infinite_resources) is *False*. Otherwise
it is treated as ```production_rate = 0```.

**[infinite_resources](#infinite_resources) = True**
*production_rate* is the baseline number of units that will be created before
niche effects are calculated, as described in the [appendix](https://github.com/ENSwR/simulation/blob/main/appendix.pdf) 
Equation 1 of Papale et al (2025).

<p align="center">
<img width="534" height="44" alt="image" src="https://github.com/user-attachments/assets/bbba8370-1c82-4dd5-9c65-37361a192d29" />
</p>

See [src/SimEngine#productionRateLimited](https://github.com/ENSwR/simulation/tree/main/src#function-productionratelimited)
for more details

**[infinite_resources](#infinite_resources) = False**
*production_rate* is a factor of the weighting in Bernoulli trials, as described
in the [appendix](https://github.com/ENSwR/simulation/blob/main/appendix.pdf) 
Equation 2 of Papale et al. (2025).

<p align="center">
<img width="579" height="129" alt="image" src="https://github.com/user-attachments/assets/1e979517-5a97-485a-b18d-ae799ddf15f0" />
</p>

See [src/SimEngine#binomialDraw](https://github.com/ENSwR/simulation/tree/main/src#function-binomialdraw)
for more details

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

[Type_A]
A_niche_construction = *integer value*
lifespan = *integer value*
production_rate = *integer value*

[Type_B]
B_niche_construction = *integer value*
lifespan = *integer value*
production_rate = *integer value*

[Type_C]
C_niche_construction = *integer value*
lifespan = *integer value*
production_rate = *integer value*

[Type_D]
D_niche_construction = *integer value*
lifespan = *integer value*
production_rate = *integer value*
```
