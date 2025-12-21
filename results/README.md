# **Overview**
This directory contains simulation outputs for the simulations used in
Papale et al. (2025). Files are named for the figure data and configuration file
they correspond to.

**Note:** 4.csv is not included with this release due to filesize (11.6GB), but can be 
produced by running the simulation using the [4.config](https://github.com/ENSwR/simulation/blob/main/configs/4.config)
configuration. Please see [4-resources.txt](https://github.com/ENSwR/simulation/blob/main/results/4-resources.txt)
first, for example of ```/usr/bin/time -v``` time and resources required to produce 4.csv

The program will appear to stall for a long period after the final timestep. Do not interrupt
or perform memory intensive operations that might trigger SIGKILL at this stage.

## .csv
Comma Separated Value files with a header row.

The first column (unnamed) contains the timestep.

#### <ins>Extinctions</ins>
The number of previous extinctions which have occurred in the simulation.

#### <ins>Tot_Pop(_X)</ins>
A population tally combined across all GridCells of total populations, or 
specific type's populations, as indicated under the corresponding column headers.

#### <ins>Pop(_X)</ins>
Population tallies of each GridCell for all type populations, or specific 
type populations.

#### <ins>niche_X</ins>
Niche property tallies of each GridCell for a given type.

## .seed
Plain-text file which records a timestep of when a simulation was run and
its seed value. Each time the simulation is run, these values will be appended
to the end of a .seed file which shares the same filename prefix as the 
corresponding .csv output.

## 4-resources.txt
Summarizes the time and computational resources required for the run that 
produced data for 4.csv using [4.config](https://github.com/ENSwR/simulation/blob/main/configs/4.config)
