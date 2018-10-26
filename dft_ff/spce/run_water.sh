#!/bin/bash
cp calc_pe_water.in calc_pe_water_$1.in; sed -i s/'NN'/$1/g calc_pe_water_$1.in; lmp_icc_serial < calc_pe_water_$1.in
rm calc_pe_water_$1.in
