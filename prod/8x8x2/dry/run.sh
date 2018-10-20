#!/bin/bash

cp run.in $1+run.in
sed -i s/'PROBETEMP'/$1/g $1+run.in
lmp_icc_serial < $1+run.in
rm $1+run.in
mv data/current_run/cp_rawTemp$1.dat data/current_run/rawTemp$1.dat
