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


def plot_alpha(data,epsilon,label):
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
	print("{}:".format(label))
	print("Slope: {}".format(m))
	print("Intercept: {}".format(b))

	plt.plot([i[0] for i in alpha_fcd],[i[1] for i in alpha_fcd],label=label,ls="None",marker="x")
	plt.plot(x,m*x+b,label="{} fit".format(label))

# Load and organize data
datafile_dry = "../prod/8x8x2/dry/data/run_07/analyzedData.dat"
datafile_025 = "../prod/8x8x2/wet_025/data/run_01/analyzedData.dat"
datafile_050 = "../prod/8x8x2/wet_050/data/run_01/analyzedData.dat"
datafile_100 = "../prod/8x8x2/wet_100/data/run_01/analyzedData.dat"
label_dry = "Dry"
label_025 = "Wet-25"
label_050 = "Wet-50"
label_100 = "Wet-100"
epsilon = 100.

data_dry = pickle.load(open(datafile_dry,"r"))
data_025 = pickle.load(open(datafile_025,"r"))
data_050 = pickle.load(open(datafile_050,"r"))
data_100 = pickle.load(open(datafile_100,"r"))
# Plot
plt.figure()
plt.title("Specific Heat Comparison\nCenter FD Method")
plot_alpha(data_dry,epsilon,label_dry)
plot_alpha(data_025,epsilon,label_025)
plot_alpha(data_050,epsilon,label_050)
plot_alpha(data_100,epsilon,label_100)
plt.legend()
plt.show()


