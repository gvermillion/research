#!/bin/bash

mpirun lmp_icc_openmpi < run_$1.in
rm run_$1.in
rm run_$1.moab
mv data/current_run/cp_rawTemp$1.dat data/current_run/rawTemp$1.dat
