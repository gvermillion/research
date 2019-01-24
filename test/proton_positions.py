# IPython log file

from ase import Atoms
import numpy as np
from ase.visualize import view
from ase.io import read

def return_wyckoff_positions(x,y,z):
	pos = [(x,y,z),(-y,x-y,z),(-x+y,-x,z),(-x,-y,z),(y,-x+y,z),(x-y,x,z),(y,x,-z+1./2.),(x-y,-y,-z+1./2.),(-x,-x+y,-z+1./2.),(-y,-x,-z+1./2.),(-x+y,y,-z+1./2.),(x,x-y,-z+1./2.),(-x,-y,-z),(y,-x+y,-z),(x-y,x,-z),(x,y,-z),(-y,x-y,-z),(-x+y,-x,-z),(-y,-x,z+1./2.),(-x+y,y,z+1./2.),(x,x-y,z+1./2.),(y,x,z+1./2.),(x-y,-y,z+1./2.),(-x,-x+y,z+1./2.)]
	return pos
pos = return_wyckoff_positions(-0.0257,-0.0709,0.3327)
atoms = read("/work/gcates/research/dft/wannier_dipole/no_kpts/tmp/beryl_wet_0.xyz")

a = 9.21
b = 9.21
c = 9.19
alpha = np.radians(90)
beta = np.radians(90)
gamma = np.radians(120)
vol = a*b*c*np.sqrt(1-np.cos(alpha)**2-np.cos(beta)**2-np.cos(gamma)**2+2*np.cos(alpha)*np.cos(beta)*np.cos(gamma))
T = np.zeros((3,3))
T[0][0] = a
T[0][1] = b*np.cos(gamma)
T[1][1] = b*np.sin(gamma)
T[0][2] = c*np.cos(beta)
T[1][2] = c*(np.cos(alpha)-np.cos(beta)*np.cos(gamma))/(np.sin(gamma))
T[2][2] = vol/(a*b*np.sin(gamma))

pos2 =[np.matmul(T,pos[i]) for i in range(0,12)]
test2 = atoms.copy()
protons2 = Atoms("H"*12,positions=pos2)
test2.extend(protons2)
view(test2)
