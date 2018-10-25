# Potential Paramters

pair_coeff    1    5 morse     		  0. 	       0.           0.  	# Ow Be 
pair_coeff    1    5 buck                 0            1           -354.5 
pair_coeff    1    5 lj/cut/tip4p/long	  39.637	1.1435          
pair_coeff    2    5 morse     		  0 	       0           0  		# Ow Al 
pair_coeff    2    5 buck                 0            1           -554.6 
pair_coeff    2    5 lj/cut/tip4p/long	  96.854	1.0616           
pair_coeff    3    5 morse     		  0 	       0           0  		# Ow Si 
pair_coeff    3    5 buck                 0            1           -419.9 
pair_coeff    3    5 lj/cut/tip4p/long	  55.345	1.1126           
pair_coeff    4    5 morse     		  0 	       0           0  		# Ow O 
pair_coeff    4    5 buck                 0            1           -102.9 
pair_coeff    4    5 lj/cut/tip4p/long	  0.70042	1.8233           
pair_coeff    5    6 morse     		  0 	       0           0  		# Ow Hw
pair_coeff    5    6 buck                 0            1           0 
pair_coeff    5    6 lj/cut/tip4p/long	  0.000	      0.0	           

pair_coeff    5    5 morse     		  0 	       0           0  		# Ow Ow
pair_coeff    5    5 buck                 0            1           -625.4 
pair_coeff    5    5 lj/cut/tip4p/long	  0.008038276	3.1589
pair_coeff    1    6 morse     		  0 	       0           0  		# Hw Be
pair_coeff    1    6 buck                 0            1           0 
pair_coeff    1    6 lj/cut/tip4p/long	  0.000	      0.0	           
pair_coeff    2    6 morse     		  0 	       0           0  		# Hw Al
pair_coeff    2    6 buck                 0            1           0 
pair_coeff    2    6 lj/cut/tip4p/long	  0.000	      0.0	           
pair_coeff    3    6 morse     		  0 	       0           0  		# Hw Si
pair_coeff    3    6 buck                 0            1           0 
pair_coeff    3    6 lj/cut/tip4p/long	  0.000	      0.0	           
pair_coeff    4    6 morse     		  0 	       0           0  		# Hw O 
pair_coeff    4    6 buck                 0            1           0 
pair_coeff    4    6 lj/cut/tip4p/long	  0.000	      0.0	           
pair_coeff    6    6 morse     		  0 	       0           0  		# Hw Hw
pair_coeff    6    6 buck                 0            1           0 
pair_coeff    6    6 lj/cut/tip4p/long	  0.000	      0.0	           



bond_style	harmonic
angle_style	harmonic
dihedral_style	none
improper_style	none

bond_coeff	1 35.756   	0.95720
angle_coeff	1 3.969		104.520
group		water type 5 6

