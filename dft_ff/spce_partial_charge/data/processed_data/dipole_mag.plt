set title "Dipole Magnitude vs Oxygen Charge"
set xlabel "Oxygen charge [|e|]"
set ylabel "Dipole [Debye]"
plot "dipole_mag.dat" u 1:2 w lp title "SPCE"
