
# Neighbor Style
neighbor	2.0 bin
neigh_modify	delay 0 every 1 check yes

# Minimization style
min_style	cg
 
# Setup Output
thermo_style	custom	step temp vol cella cellb cellc cellgamma pxx pyy pzz pxy pxz pyz lx ly lz press pe #c_eatoms
thermo_modify	norm no
variable 	myVol equal vol
variable	myCella equal cella
variable	myCellb equal cellb
variable	myCellc equal cellc
variable	myCellgamma equal cellgamma
