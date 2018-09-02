import numpy as np
import matplotlib.pyplot as plt
import sys,os
import pickle
import csv

# PREAMBLE
def validate_input():
	if len(sys.argv) != 3:
    		print("Usage: python {} ANALYZED_DATA_FILE EPSILON".format(sys.argv[0]))
    		sys.exit(2)
	return sys.argv[1], float(sys.argv[2])

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
datafile, epsilon = validate_input()
data = pickle.load(open(datafile,"r"))

Ts = [i[0] for i in data] 

V = np.array([i[12] for i in data]) # [angstrom**3]

# Center Finite-Difference Method
alpha_data = zip(Ts,[perform_binning_analysis(i) for i in V])
alpha_fcd = []

for i in np.arange(len(alpha_data)-1):
	T2 = alpha_data[i+1][0]
	T1 = alpha_data[i-1][0]
	V2 = alpha_data[i+1][1][0]
	V1 = alpha_data[i-1][1][0]
	V0 = alpha_data[i][1][0]
	if T2-T1 == 2*epsilon:
		alpha_fcd.append([T2-epsilon,(V2-V1)/(2*epsilon*V0)])

m,b = np.polyfit([i[0] for i in alpha_fcd],[i[1] for i in alpha_fcd],1)
x = np.linspace(Ts[0],Ts[-1],100)

# Print
print("\nSlope: {}".format(m))
print("Intercept: {}".format(b))

# Plot
plt.figure()
plt.title("Thermal Expansion Coefficient\nCenter FD Method")
plt.plot([i[0] for i in alpha_fcd],[i[1] for i in alpha_fcd],ls="None",marker="x")
plt.plot(x,m*x+b)
plt.show()


