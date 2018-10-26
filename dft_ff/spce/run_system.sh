#!/bin/bash
cp calc_pe.in calc_pe_$1.in; sed -i s/'NN'/$1/g calc_pe_$1.in; lmp_icc_serial < calc_pe_$1.in
rm calc_pe_$1.in
