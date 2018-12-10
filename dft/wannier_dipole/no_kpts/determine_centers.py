import sys, os
from gpaw import GPAW, restart
from ase import Atoms
from ase.io import write
from ase.dft import wannier
import numpy as np

scwf = sys.argv[1] # <path_to_data/prefix+seed.gpw
path_to_data = scwf[:scwf.find('/')+1]
prefix = scwf[scwf.find('/')+1:scwf.find('.')-3]
#prefix = ''
seed = scwf[-7:-4]


def minimum_image(r_i,r_j,atoms):
	h = np.array([atoms.get_cell()[0],atoms.get_cell()[1],atoms.get_cell()[2]])
	h_inv = np.linalg.inv(h)

	# Determine fractional transformations
	s_i = h_inv.dot(r_i)
	s_j = h_inv.dot(r_j)
	s_ij = s_i - s_j

	# General Minimum Image Convention
	s_ij -= np.rint(s_ij)

	# Transform back
	r_ij = h.dot(s_ij)
	
	return r_ij
	
print("Working on {}".format(seed))
print("\tLoading SCWF")
atoms, calc = restart(scwf,txt=None)

print("\tDeterminingg MLWF")
path_to_mlwf = path_to_data+prefix+seed+'.wan'
if os.path.isfile(path_to_mlwf):
	#print("{} does exist".format(path_to_mlwf))
	w = wannier.Wannier(nwannier=148,calc=calc,file=path_to_mlwf)
else:
	#print("{} does not exist".format(path_to_mlwf))
	w = wannier.Wannier(nwannier=148,calc=calc)
	w.localize()
	w.save(path_to_mlwf)

print("\tDetermining Centers")
O_pos = np.array([0., 0., 2.296999931]) # Oxygen atom position is constant through rotation
centers = w.get_centers()

atoms_centers = atoms.copy()
cat = Atoms('X'*len(centers),positions=centers)
atoms_centers.extend(cat)
distances = list(atoms_centers.get_all_distances(mic=True)[58])
dist_O_centers = atoms_centers.get_all_distances(mic=True)[58][61:]
select = list(np.sort(dist_O_centers))[0:4] 
closest = [distances.index(select[i]) for i in np.arange(len(select))] 
atoms.extend(atoms_centers[closest])

# Write file that includes all Wannier centers
path_to_center_verification = path_to_data+'center_verification/'+prefix+seed+'TEST.xyz'
write(path_to_center_verification,atoms)

