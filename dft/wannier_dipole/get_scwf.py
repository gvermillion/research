import numpy as np
from ase import *
from ase.io import read, write
from ase.optimize.bfgs import BFGS
from gpaw import GPAW
from ase.visualize import view
import sys,os

i = sys.argv[1]
k_dens = "3.9"
dest_xyz = "tmp/beryl_wet_{}.xyz".format(i)
#os.system("cp beryl_wet_def.xyz {}".format(dest_xyz))
#with open("water_pos/{}.xyz".format(i)) as f:
#	j =0
#	for line in f:
#		x,y,z = line.split()
#		if j == 0:
#			os.system("sed -i s/'O_X'/{}/g {}".format(x,dest_xyz))
#			os.system("sed -i s/'O_Y'/{}/g {}".format(y,dest_xyz))
#			os.system("sed -i s/'O_Z'/{}/g {}".format(z,dest_xyz))
#		elif j == 1:
#			os.system("sed -i s/'H1_X'/{}/g {}".format(x,dest_xyz))
#			os.system("sed -i s/'H1_Y'/{}/g {}".format(y,dest_xyz))
#			os.system("sed -i s/'H1_Z'/{}/g {}".format(z,dest_xyz))
#		elif j == 2:
#			os.system("sed -i s/'H2_X'/{}/g {}".format(x,dest_xyz))
#			os.system("sed -i s/'H2_Y'/{}/g {}".format(y,dest_xyz))
#			os.system("sed -i s/'H2_Z'/{}/g {}".format(z,dest_xyz))
#		j+=1

beryl = read(dest_xyz)
calc = GPAW(xc='PBE',kpts={'density':float(k_dens)},h=0.2,txt="data/current_run/{}.calc".format(i)) 
beryl.set_calculator(calc)
#os.system("echo {}".format(i))
energy = beryl.get_potential_energy()
calc.write('data/current_run/{}.gpw'.format(i), mode='all')
