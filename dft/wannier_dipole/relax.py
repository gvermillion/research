import numpy as np
from ase import *
from ase.io import read, write
from ase.optimize.bfgs import BFGS
from gpaw import GPAW
from ase.visualize import view

beryl = read("beryl_test.xyz") # 1x1x2 of true unit cell
view(beryl)
#calc = GPAW(xc='PBE',txt="calc.out")
#beryl.set_calculator(calc)
#
#dyn = BFGS(beryl,trajectory="beryl.traj")
#dyn.run(fmax=0.1)
#
