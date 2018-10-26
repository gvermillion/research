kspace_style 	pppm/tip4p 1.0e-4
pair_style 	hybrid/overlay morse 5.5 buck 5.5 lj/cut/coul/long 5.5 15 lj/cut/tip4p/long 5 6 1 1 0.1546 15    

# Neighbor Style
neighbor	0.3 bin
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
