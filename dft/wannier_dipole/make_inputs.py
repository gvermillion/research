import numpy as np
import sys,os

for i in np.arange(50):
	dest_xyz = "tmp/beryl_wet_{}.xyz".format(i)
	os.system("cp beryl_wet_def.xyz {}".format(dest_xyz))
	with open("water_pos/{}.xyz".format(i)) as f:
		j =0
		for line in f:
			x,y,z = line.split()
			if j == 0:
				os.system("sed -i s/'O_X'/{}/g {}".format(x,dest_xyz))
				os.system("sed -i s/'O_Y'/{}/g {}".format(y,dest_xyz))
				os.system("sed -i s/'O_Z'/{}/g {}".format(z,dest_xyz))
			elif j == 1:
				os.system("sed -i s/'H1_X'/{}/g {}".format(x,dest_xyz))
				os.system("sed -i s/'H1_Y'/{}/g {}".format(y,dest_xyz))
				os.system("sed -i s/'H1_Z'/{}/g {}".format(z,dest_xyz))
			elif j == 2:
				os.system("sed -i s/'H2_X'/{}/g {}".format(x,dest_xyz))
				os.system("sed -i s/'H2_Y'/{}/g {}".format(y,dest_xyz))
				os.system("sed -i s/'H2_Z'/{}/g {}".format(z,dest_xyz))
			j+=1
	
