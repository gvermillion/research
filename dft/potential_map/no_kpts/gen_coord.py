import numpy as np
import sys, os

num_meas = sys.argv[1] # Number of measurements between 0:2pi
#shift = sys.argv[2] # Amount to shift along c-axis
angles = np.linspace(0,2*np.pi,num_meas)
#dest = "mod/q_def/"
#`os.system("cp -r mod/def_q_def/ {}".format(dest))

i = 0  
for angle in angles:
#	os.system("python water_shifter_rotator.py {} 0 {} >> water_pos/{}.xyz".format(shift,angle,i))
	os.system("python water_shifter_rotator.py 0 0 {} >> water_pos/{}.xyz".format(angle,i))
	i +=1
os.system("sed -i s/','/' '/g water_pos/*xyz")
