import sys, os
import numpy as np

q_O = float(sys.argv[1])
q_H = q_O/2*-1
O = np.array([0.000000000, 0.000000000, 2.296999931])
H1 = np.array([00.586173841, 0.000000000, 3.053699198])
H2 = np.array([00.586173841, 0.000000000, 1.540300664])

p = q_O*O + q_H*H1 + q_H*H2

print(np.linalg.norm(p)/0.21) 
