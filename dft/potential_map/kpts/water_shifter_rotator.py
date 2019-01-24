#!/usr/bin/python
import sys
from math import *

def rotateAxisX(alpha):
    '''
    Rotation about x axis
    :param alpha: plane altitude angle in rad
    :return: x-axis rotation matrix
    '''
    rotX = [[1, 0, 0],
	    [0, cos(alpha), sin(alpha)],
	    [0, -sin(alpha), cos(alpha)]]
    return rotX
  
def rotateAxisY(alpha):
    '''
    Rotation about y axis
    :param alpha: plane altitude angle in rad
    :return: x-axis rotation matrix
    '''
    rotY = [[cos(alpha), 0, sin(alpha)],
	    [0, 1, 0],
	    [-sin(alpha), 0, cos(alpha)]]
    return rotY

def rotateAxisZ(alpha):
    '''
    Rotation about z axis
    :param alpha: plane azimuth angle in rad
    :return: z-axis rotation matrix
    '''
    rotZ = [[cos(alpha), sin(alpha), 0],
	    [-sin(alpha), cos(alpha), 0],
	    [0, 0, 1]]
    return rotZ


H_1 = [0.5861738408076631, 0.0, 0.7566992670491973]
H_2 = [0.5861738408076631, 0.0, -0.7566992670491973]
O = [0.0, 0.0, 0.0]

H_1_y = [0.0, 0.0, 0.0]
H_2_y = [0.0, 0.0, 0.0]
O_y = [0.0, 0.0, 0.0]

H_1_z = [0.0, 0.0, 0.0]
H_2_z = [0.0, 0.0, 0.0]
O_z = [0.0, 0.0, 0.0]


if len(sys.argv) == 3:
	theta = float(sys.argv[1])
	phi = float(sys.argv[2])
else:
	if len(sys.argv) == 4:
		shift = float(sys.argv[1])
		theta = float(sys.argv[2])
		phi = float(sys.argv[3])
	else:
		sys.exit("ERROR: number of arguments")

H_1[0] += shift 
H_2[0] += shift 
O[0] += shift

for i in range(3):
  for j in range(3):
    H_1_y[i] = H_1_y[i] + H_1[j]*rotateAxisY(theta)[j][i]
    H_2_y[i] = H_2_y[i] + H_2[j]*rotateAxisY(theta)[j][i]
    O_y[i] = O_y[i] + O[j]*rotateAxisY(theta)[j][i]

for i in range(3):
  for j in range(3):
    H_1_z[i] = H_1_z[i] + H_1_y[j]*rotateAxisZ(phi)[j][i]
    H_2_z[i] = H_2_z[i] + H_2_y[j]*rotateAxisZ(phi)[j][i]
    O_z[i] = O_z[i] + O_y[j]*rotateAxisZ(phi)[j][i]
    
O_z[2] += 2.296999931
H_1_z[2] += 2.296999931
H_2_z[2] += 2.296999931

print ("%.9f,%.9f,%.9f" % (O_z[0], O_z[1], O_z[2]))
print ("%.9f,%.9f,%.9f" % (H_1_z[0], H_1_z[1], H_1_z[2]))
print ("%.9f,%.9f,%.9f" % (H_2_z[0], H_2_z[1], H_2_z[2]))


