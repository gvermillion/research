import numpy as np
import os,sys

root_dir = '.' 
for directory, subdirectories, files in os.walk(root_dir):
        if directory.find('N_') != -1 and directory.find('water') != -1: 
                #print directory
                #print subdirectories
                #print files
                for filename in files:
                        num_meas = int(directory[directory.find('N_')+2:directory.rfind('/')])
                        angles = np.linspace(0,2*np.pi,num_meas)
                        q_prefix = directory[:directory.find('N_')]
                        q_suffix = filename[filename.find('q_')+2:filename.find('.dat')]
                        q = q_prefix[2:]+q_suffix
                        f = open(directory+'/'+filename,"r")
                        data = []
                        for line in f:
                                line = float(line[9:-1].replace(" ",""))
                                data.append(line)
                        f.close()
                        output = open("processed_data/"+q+".dat","w")
                        data_dump = zip(angles,data)
                        for datum in data_dump:
                                output.write(str(datum)[1:-1].replace(",","    "))
                                output.write('\n')
                        output.close()
