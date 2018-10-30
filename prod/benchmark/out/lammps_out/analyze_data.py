import numpy as np


f = open("dat.no_processors","r")
no_processors = []
for line in f:
	tmp = line.split(" ")
	no_processors.append(int(tmp[-1]))
f.close()


f = open("dat.ns_day","r")
ns_day= []
for line in f:
	tmp = line.split(" ")
	ns_day.append(float(tmp[1]))
f.close()
np.savetxt('dat.analyzed.ns_day', np.c_[no_processors,ns_day])
