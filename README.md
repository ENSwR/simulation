# ENSwR Simulation
This repository hosts the ENSwR simulation used in Papale et al. (2025)

## Inputs
This simulation requires a plain-text configuration file to be provided.

## Outputs
During runtime this simulation prints the actively running timestep to console.
Upon completion, the simulation's seed number will be printed to console. If the 
config file does not specify a seed, then the seed will be randomly generated.

At the end of runtime a .csv file will be output to the filepath specified in
the config file. The seed number and a timestamp will be appended to a .seed file
with the same name.

# Running the Simulation
PORTABILITY NEEDS REVISION!

# Running simulation with config file
```
python3 <path/to/run_sim.py> [path/to/config] 

Example:
python3 src/run_sim.py configs/1a.config
```

## configs
The configs directory holds ".config" files named for the figures' data they 
produce.

## src
The scr directory contains the source code for the simulation.

## results
The results directory is the output directory for the ".config" files found in 
[configs](#configs). It contains '.csv' files, where the raw data from each 
simulation run gets stored, as well as associated '.seed' files which list a 
history of seed values for previous runs.

All simulation runs report a seed value, whether the value is set by the user
in the configuration file, or whether the program generates its seed value at
run-time.

Results from the runs using the provided configuration files are already 
included, and can be reproduced again by running the simulation with the 
configuration files again.

**Note:** Results for simulation running 4.config are not included due to 
filesize. This simulation config runs 2,100,000 timesteps on a 10x10 
environment. The resulting .csv is approximately 12GB. To obtain these results, 
run the simulation using 4.config and allow considerable time for the simulation
to run through each timestep. Expect a long wait after the final timestep while
the resulting .csv is being created.

## Requirements.txt
Contains the packages and versions info required to run the simulation.


[![DOI](https://zenodo.org/badge/1054276078.svg)](https://doi.org/10.5281/zenodo.17106872)
