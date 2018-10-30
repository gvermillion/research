#!/bin/bash
mpirun lmp_icc_openmpi < run_temp_$1_ppn_$2.in
rm run_temp_$1_ppn_$2.in
rm run_temp_$1_ppn_$2.moab
