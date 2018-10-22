#!/bin/bash
for i in {1..20}:
do ./calc_pe.sh ${i}
done

grep '^       0' | tee pe.dat
