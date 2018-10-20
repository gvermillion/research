#!/bin/bash

cp run.in $1+run.in
sed -i s/'PROBETEMP'/$1/g $1+run.in
/home/gcates/bin/lammps/build/lmp < $1+run.in
rm $1+run.in
mv data/current_run/cp_rawTemp$1.dat data/current_run/rawTemp$1.dat
