# ENSwR Simulation
This repository hosts the ENSwR simulation used in Papale et al. (2025)

# Running the Simulation
It is recommended to run this simulation using the included virtual environment 
for Python, which has all dependencies pre-installed.

Files associated with this virtual environment are found in the [venv](#venv) directory.

1. [Activate the virtual environment](#Activating-the-virtual-environment)
2. ```python3 src/run_sim.py [path-to-config] 
Example:
python3 src/run_sim.py configs/1a.config```

## Activating the virtual environment
### MacOS/Linux
```
source venv/bin/activate
```
### Windows (PowerShell)
```
venv\bin\Activate.ps1
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