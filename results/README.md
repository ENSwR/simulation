# **Overview**
This directory contains simulation outputs for the simulations used in
Papale et al. (2025). Files are named for the figure data and configuration file
they correspond to.

**Note:** 4.csv is not included with this release due to filesize, but can be 
produced by running the simulation using the 4.config configuration.

## .csv
Comma Separated Value files with a header row.

The first column (unnamed) contains the timestep.

### Extinctions
The number of previous extinctions which have occurred in the simulation.

### Tot_Pop(_X)
A population tally combined across all GridCells of total populations, or 
specific speciespopulations, as indicated under the corresponding column headers.

### Pop(_X)
Population tallies of each GridCell for all species populations, or specific 
species populations.

### niche_X
Niche property tallies of each GridCell for a given species.

## .seed
Plain-text file which records a timestep of when a simulation was run and
its seed value. Each time the simulation is run, these values will be appended
to the end of a .seed file which shares the same filename prefix as the 
corresponding .csv output.
