# Potential Paramters
pair_style 	hybrid/overlay morse 5.5 buck 5.5 lj/cut/coul/long 5.5 15.0 
pair_coeff    1    1 morse     		  0 	       0           0  # Be Be
pair_coeff    1    1 buck                 0            1           0 
pair_coeff    1    1 lj/cut/coul/long	  0	       0           
pair_coeff    2    2 morse     		  0 	       0           0  # Al Al
pair_coeff    2    2 buck                 0            1           0 
pair_coeff    2    2 lj/cut/coul/long	  0	       0           
pair_coeff    3    3 morse     		  0 	       0           0  # Si Si
pair_coeff    3    3 buck                 0            1           0 
pair_coeff    3    3 lj/cut/coul/long	  0	       0           
pair_coeff    4    4 morse     		  0.042395     1.379316    3.618701  # O O  
pair_coeff    4    4 buck                 0.000000     1.000000   -22.00000 
pair_coeff    4    4 lj/cut/coul/long	  5.500000     1.000000
pair_coeff    1    4 morse 		  0.239919     2.527420    1.815405	#Be O
pair_coeff    1    4 buck                 0.000000     1.000000   -1.000000
pair_coeff    1    4 lj/cut/coul/long     0.250000     1.000000
pair_coeff    2    4 morse 		  0.361581     1.900442    2.164818	#Al O
pair_coeff    2    4 buck                 0.000000     1.000000   -0.900000
pair_coeff    2    4 lj/cut/coul/long     0.225000     1.000000
pair_coeff    3    4 morse 		  0.340554     2.006700    2.100000	#Si O
pair_coeff    3    4 buck                 0.000000     1.000000   -1.000000
pair_coeff    3    4 lj/cut/coul/long     0.250000     1.000000
pair_coeff    1    2 morse     		  0 	       0           0  # Be Al 
pair_coeff    1    2 buck                 0            1           0 
pair_coeff    1    2 lj/cut/coul/long	  0	       0           
pair_coeff    1    3 morse     		  0 	       0           0  # Al Si
pair_coeff    1    3 buck                 0            1           0 
pair_coeff    1    3 lj/cut/coul/long	  0	       0           
pair_coeff    2    3 morse     		  0 	       0           0  # Al si
pair_coeff    2    3 buck                 0            1           0 
pair_coeff    2    3 lj/cut/coul/long	  0	       0           
kspace_style 	pppm 1.0e-4

# Neighbor Style
neighbor	0.3 bin
neigh_modify	delay 0 every 1 check yes

# Minimization style
min_style	cg
 
# Setup Output
thermo		10
thermo_style	custom	step temp vol cella cellb cellc cellgamma pxx pyy pzz pxy pxz pyz lx ly lz press pe #c_eatoms
thermo_modify	norm no
variable 	myVol equal vol
variable	myCella equal cella
variable	myCellb equal cellb
variable	myCellc equal cellc
variable	myCellgamma equal cellgamma
