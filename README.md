# **Overview**
This repository hosts the ENSwR simulation used in Papale et al. (2025)

### Table of Contents
- [Instructions](#instructions)
    * [Inputs](#inputs)
    * [Outputs](#outputs)
    * [Running the simulation](#running-the-simulation)
        - [Navigate to the main directory](#navigate-to-the-main-directory)
        - [Create a virtual environment (venv) for Python](#create-a-virtual-environment-for-python)
        - [Activate the virtual environment](#activate-the-virtual-environment)
        - [Install requirements to the venv](#install-requirements-to-the-venv)
        - [Run the simulation with config file](#running-simulation-with-configuration-file)
        - [Deactivate the venv](#deactivate-the-venv)
- [Directories](#directories)
    * [./configs](#configs)
    * [./src](#src)
    * [./results](#results)
- [requirements.txt](#requirementstxt)

## Instructions

### Inputs
This simulation requires a plain-text configuration file to be provided.

### Outputs
During runtime this simulation prints the actively running timestep to console.
Upon completion, the simulation's seed number will be printed to console. If the 
config file does not specify a seed, then the seed will be randomly generated.

At the end of runtime a .csv file will be output to the filepath specified in
the config file. The seed number and a timestamp will be appended to a .seed file
with the same name.

### Running the Simulation
1. [Navigate to the main directory](#navigate-to-the-main-directory)
1. [Create a virtual environment (venv) for Python](#create-a-virtual-environment-for-python)
1. [Activate the virtual environment](#activate-the-virtual-environment)
1. [Install requirements to the venv](#install-requirements-to-the-venv)
1. [Run the simulation with config file](#running-simulation-with-configuration-file)
1. [Deactivate the venv](#deactivate-the-venv)

### Navigate to the main directory
Extract the compressed .zip or .tar.gz file. Note the name and location of the 
directory that is created.

Using PowerShell (Windows) or a terminal (MacOS/Linux), navigate the working 
directory to the extracted directory that was created.

### Create a virtual environment for python
In your terminal or PowerShell enter:
```
python3 -m venv venv
```
This will create a virtual environment directory called "venv" in the active 
folder.

### Activate the virtual environment
#### Windows
In PowerShell, enter:
```
venv\Scripts\Activate.ps1
```
#### MacOS/Linux
In the terminal, enter:
```
source venv/bin/activate
```
You should now see the environment name in parentheses in your command line.

### Install requirements to the venv
With the venv now activated, enter:
```
pip3 install -r requirements.txt
```
This will begin installing dependencies listed in requirements.txt to the 
virtual environment. These installations will not persist outside of your 
virtual environment. This step will not need to be repeated if you activate the
venv again in the future.

### Running simulation with configuration file
To run the simulation, ensure that the venv is active and dependencies have been
installed, and envoke python3 to run the run_sim.py script:
```
python3 <path/to/run_sim.py> [path/to/config] 

Example:
python3 src/run_sim.py configs/1a.config
```
The console should begin outputting numbers indicating the timestep it is 
computing, followed by a seed value when the simulation has completed.

Results will appear in [./results/](#results).

### Deactivate the venv
When finished running simulations, the venv can be deactived by entering:
```
deactivate
```

## Directories
### ./configs
The configs directory holds ".config" files named for the figures' data they 
produce.

### ./src
The src directory contains the source code for the simulation.

### ./results
The results directory is the output directory for the ".config" files found in 
[./configs](#configs). It contains '.csv' files, where the raw data from each 
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

## requirements.txt
Contains the packages and versions info required to run the simulation.


[![DOI](https://zenodo.org/badge/1054276078.svg)](https://doi.org/10.5281/zenodo.17106872)
