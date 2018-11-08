#!/bin/bash

mpirun --bind-to core --map-by core lmp_icc_openmpi < tmp/run_$1.in
rm tmp/run_$1.in
rm tmp/run_$1.moab
mv data/current_run/cp_rawTemp$1.dat data/current_run/rawTemp$1.dat
