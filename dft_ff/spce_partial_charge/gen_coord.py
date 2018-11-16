import numpy as np
import sys, os

num_meas = sys.argv[1] # Number of measurements between 0:2pi
angles = np.linspace(0,2*np.pi,num_meas)
dest = "mod/q_def/"
os.system("cp -r mod/def_q_def/ {}".format(dest))

i = 0  
for angle in angles:
	os.system("python water_shifter_rotator.py 0 0 {} >> tmp".format(angle))
	with open("tmp","r") as f:
		lines = f.read().splitlines()
		O = lines[0].split(",")
		H1 = lines[1].split(",")
		H2 = lines[2].split(",")
		filename = "{}beryl_water_{}_q_def.mod".format(dest,i)
		os.system("cp mod/beryl_water_def.mod {}".format(filename))
		os.system("sed -i s/'X_O'/'{}'/g {}".format(O[0],filename))
		os.system("sed -i s/'Y_O'/'{}'/g {}".format(O[1],filename))
		os.system("sed -i s/'Z_O'/'{}'/g {}".format(O[2],filename))
		os.system("sed -i s/'X_H1'/'{}'/g {}".format(H1[0],filename))
		os.system("sed -i s/'Y_H1'/'{}'/g {}".format(H1[1],filename))
		os.system("sed -i s/'Z_H1'/'{}'/g {}".format(H1[2],filename))
		os.system("sed -i s/'X_H2'/'{}'/g {}".format(H2[0],filename))
		os.system("sed -i s/'Y_H2'/'{}'/g {}".format(H2[1],filename))
		os.system("sed -i s/'Z_H2'/'{}'/g {}".format(H2[2],filename))
	os.system("rm tmp")
	i += 1
#	for line in f:
#		if i == 1:
#			X_O, Y_O, Z_O = line.split(",")
#			print(X_O, Y_O, Z_O)	
