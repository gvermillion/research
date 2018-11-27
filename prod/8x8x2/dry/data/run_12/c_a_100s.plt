#!/bin/bash/gnuplot --persist
files = system("ls -1 rawTemp*00.dat")
set xlabel "Timesteps"
set ylabel "c/a"
set key bottom left
plot for [f in files] f u 1:(($8/4)/($6/8)) w lp title f


