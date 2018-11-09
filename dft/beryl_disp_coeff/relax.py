import numpy as np
from ase import *
from ase.io import read, write
from ase.optimize.bfgs import BFGS
from gpaw import GPAW


beryl = read("beryl_unrelaxed.xyz") # 1x1x2 of true unit cell
calc = GPAW(xc='PBE',txt="calc.out")
beryl.set_calculator(calc)

dyn = BFGS(beryl,trajectory="beryl.traj")
dyn.run(fmax=0.1)

