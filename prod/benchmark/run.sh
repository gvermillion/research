#!/bin/bash
lmp_icc_serial < run_temp_$1_ppn_$2.in
rm run_temp_$1_ppn_$2.in
rm run_temp_$1_ppn_$2.moab
