import os,sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

def return_wyckoff_positions(x,y,z):
	pos = [[x,y,z],[-y,x-y,z],[-x+y,-x,z],[-x,-y,z],[y,-x+y,z],[x-y,x,z],[y,x,-z+1./2.],[x-y,-y,-z+1./2.],[-x,-x+y,-z+1./2.],[-y,-x,-z+1./2.],[-x+y,y,-z+1./2.],[x,x-y,-z+1./2.],[-x,-y,-z],[y,-x+y,-z],[x-y,x,-z],[x,y,-z],[-y,x-y,-z],[-x+y,-x,-z],[-y,-x,z+1./2.],[-x+y,y,z+1./2.],[x,x-y,z+1./2.],[y,x,z+1./2.],[x-y,-y,z+1./2.],[-x,-x+y,z+1./2.]]
	return pos



		
return_wyckoff_positions(x,y,z)
