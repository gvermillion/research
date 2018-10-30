import numpy as np


f = open("dat.wall_time","r")
wall_time = []
for line in f:
	tmp = line.split(" ")
	tmp =tmp[-3].split(":")
	time = int(tmp[0])*60*60 + int(tmp[1])*60 + int(tmp[2])
	wall_time.append(time)
f.close()


f = open("dat.wait_time","r")
wait_time = []
for line in f:
	tmp = line.split(" ")
	tmp = tmp[35]
	tmp = tmp.split(":")
	time = int(tmp[0])*60*60 + int(tmp[1])*60 + int(tmp[2])
	wait_time.append(time)
f.close()

f = open("dat.no_nodes","r")
no_nodes = []
for line in f:
	tmp = line.split(" ")
	tmp = tmp[-1]
	tmp = tmp.split(":")
	no_nodes.append(int(tmp[1]))
f.close()

f = open("dat.task_mem","r")
task_mem = []
for line in f:
	tmp = line.split(" ")
	task_mem.append(int(tmp[32]))
f.close()


np.savetxt('dat.analyzed.wait_time', np.c_[no_nodes,wait_time])
np.savetxt('dat.analyzed.wall_time', np.c_[no_nodes,wall_time])
np.savetxt('dat.analyzed.task_mem', np.c_[no_nodes,task_mem])
