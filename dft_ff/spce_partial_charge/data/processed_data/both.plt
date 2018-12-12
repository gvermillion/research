set title "Potential Depth and Dipole Moment vs Oxygen Partial Charge"
set ytics nomirror
set y2tics
set ylabel "Potential Depth [eV]"
set y2label "Dipole Moment [D]"
set xlabel "Oxygen Partial Charge [|e|]"
plot 'depth.dat' u 1:2 w lp axis x1y1 title "Depth", 'dipole_mag.dat' u 1:2 w lp axis x1y2 title "Dipole"
