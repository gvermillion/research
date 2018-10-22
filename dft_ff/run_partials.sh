#!/bin/bash
for i in {0..9}; 
do 
cd mod/q_${i}
for j in {0..19}; 
do 
../../run.sh beryl_water_${j}_q_${i}.mod 
done | grep '^       0' | pe.dat
cd ../../
done
