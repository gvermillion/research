import numpy as np
import matplotlib.pyplot as plt
import sys,os
import pickle
import csv

# PREAMBLE
def validate_input():
	if len(sys.argv) != 4:
    		print("Usage: python {} ANALYZED_DATA_FILE EPSILON LABEL".format(sys.argv[0]))
    		sys.exit(2)
	return sys.argv[1], float(sys.argv[2]), sys.argv[3]

def binning_analysis(O,k):
	# determine number of blocks
        noBlocks = len(O)//k
        N = k*noBlocks
        
        # Compute block averages
        O = np.array(O)
        Osplit = np.split(O[0:N],noBlocks)
        bas = np.mean(Osplit,axis=1)
 
        # Calculate block average and variance
        blockAvg = np.mean(bas)
        blockVar = np.var(bas)
        # Calculate block error
        blockError = np.sqrt(blockVar/noBlocks)

      	# Calculate average and variance of measurements
        Oavg = np.mean(O)
        Ovar = np.var(O)

      	# Calculate estimated autocorrelation time and effective statistics
        if Ovar > 0:
               	tINTo = k*blockVar/(2*Ovar)
        else:
                tINTo = float('nan') 
        if tINTo > 0:
                Neff = N/(2*tINTo)
        else:
                Neff = float("nan")
        return Oavg, tINTo, Neff, blockError

def perform_binning_analysis(O):
    N = len(O)      
    
    # Initialize variables for tracking data
    Neff = 0.0
    blockError = 0.0
    tINTo = 0.0     

    for i in range(N//10):
        k = i+1
        Oavg, tINToNew, NeffNew, blockErrorNew = binning_analysis(O,k)
        if tINToNew > tINTo:
            Neff = NeffNew
            blockError = blockErrorNew
            tINTo = tINToNew
    data = [Oavg,tINTo,Neff,blockError]
    return data

# Load and organize data
datafile, epsilon, label = validate_input()
data = pickle.load(open(datafile,"r"))

def plot_ac(data,epsilon,label):
	Ts = [i[0] for i in data] 

	a = np.array([i[5][0] for i in data])/8 # [angstrom]
	c = np.array([i[7][0] for i in data])/4 # [angstrom]
	a_err = np.array([i[5][3] for i in data])/8 # [angstrom]
	c_err = np.array([i[7][3] for i in data])/4 # [angstrom]


	m_a,b_a = np.polyfit(Ts,a,1)
	m_c,b_c = np.polyfit(Ts,c,1)
	x = np.linspace(Ts[0],Ts[-1],100)

	# Print
	print("a:")
	print("Slope: {}".format(m_a))
	print("Intercept: {}".format(b_a))
	print("c:")
	print("Slope: {}".format(m_c))
	print("Intercept: {}".format(b_c))

	plt.errorbar(Ts,a,yerr=a_err,fmt='-o',label="a")
	plt.errorbar(Ts,c,yerr=c_err,fmt='-o',label="c")
	plt.plot(x,m_a*x+b_a,label="a fit")
	plt.plot(x,m_c*x+b_c,label="c fit")
# Plot
plt.figure()
plt.title("Lattice Constants")
plot_ac(data,epsilon,label)
plt.legend()
plt.show()


