#!/bin/bash

for i in {1..16}; 
	do
		cp run_def.in run_temp_$1_ppn_${i}.in
		sed -i s/'PPN'/${i}/g run_temp_$1_ppn_${i}.in
		sed -i s/'PROBETEMP'/$1/g run_temp_$1_ppn_${i}.in
		cp run_def.moab run_temp_$1_ppn_${i}.moab
		sed -i s/'PPN'/${i}/g run_temp_$1_ppn_${i}.moab
		sed -i s/'PROBETEMP'/$1/g run_temp_$1_ppn_${i}.moab
		msub run_temp_$1_ppn_${i}.moab
	done

