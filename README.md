# ENSwR Simulation
This repository hosts the ENSwR simulation used in Papale et al. (2025)

## Inputs
This simulation requires a plain-text configuration file to be provided.

## Outputs
During runtime this simulation prints the current running timestep to console.
Upon completion, the simulation's seed number will be printed to console. If the 
config file does not specify a seed, then the seed will be randomly generated.

At the end of runtime a .csv file will be output to the filepath specified in
the config file. The seed number and a timestamp will be appended to a .seed file
with the same name.

# Running the Simulation
It is recommended to run this simulation using the included virtual environment 
for Python, which has all dependencies pre-installed.

Files associated with this virtual environment are found in the [venv](#venv) directory.

To run this simulation:

1. [Activate the virtual environment](#activating-the-virtual-environment)
2. [Run simulation with a config file](#running-simulation-with-config-file)
3. Result output paths are set by the config files. In the provided configs,
resulting output will be sent to the [results](#results) directory.

## Activating the virtual environment
### MacOS/Linux
```
source venv/bin/activate
```
### Windows (PowerShell)
```
venv\bin\Activate.ps1
```

# Running simulation with config file
```
python3 <path/to/run_sim.py> [path/to/config] 
Example:
python3 src/run_sim.py configs/1a.config
```

## venv
The venv directory contains all files associated with a virtual environment
for Python with all package requirements pre-installed to run the simulation.

## configs
The configs directory holds ".config" files named for the figures' data they 
produce.

## src
The scr directory contains the source code for the simulation.

## results
The results directory is the output directory for the ".config" files found in 
[configs](#configs). It contains '.csv' files, where the raw data from each simulation run 
gets stored, as well as associated '.seed' files which list a history of seed
values for previous runs.

Results from the runs using the provided config files are already included, and 
can be reproduced again by running the simulation with the config files again.

**Note:** Results for simulation with 4.config are not included due to filesize. 
This simulation config runs 2,100,000 timesteps on a 10x10 environment. 
The resulting .csv is approximately 12GB. To obtain these results, please
run the simulation using 4.config and allow considerable time for the simulation
to run through each timestep. Expect a long wait after the final timestep while
the resulting .csv is being created.