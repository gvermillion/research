set title "Potential Depth vs Oxygen Charge"
set xlabel "Oxygen charge [|e|]"
set ylabel "Potential Depth [ev]"
plot "depth.dat" u 1:2 w lp title "SPCE"
