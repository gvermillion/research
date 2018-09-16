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


def calc_var(U, p, V):
	k = 6.24*10**(-7) # [bar*angstrom**3] --> [eV]
	var_Hs = []
	for i in np.arange(len(U)):
		var_H = np.var(U[i]) + 2*k**2*np.cov(U[i],p[i]*V[i])[0][1] +k**2*((np.var(p[i])+np.mean(p[i])**2)*(np.var(V[i]) +np.mean(V[i])**2)-(np.cov(p[i],V[i])[0][1]+np.mean(p[i])*np.mean(V[i]))**2 + np.cov(p[i]**2,V[i]**2)[0][1])
		var_Hs.append(var_H)
	return var_Hs


def plot_Cp(data,epsilon,label):	
	Ts = [i[0] for i in data] 

	U = np.array([i[10] for i in data]) # [eV]
	p = np.array([i[11] for i in data]) # [bar]
	V = np.array([i[12] for i in data]) # [angstrom**3]

	conversion = 6.24*10**(-7) # [bar*angstrom**3] --> [eV]

	H = U + conversion*p*V  # [eV]
	var_Hs = calc_var(U,p,V)

	# Center Finite-Difference Method
	Cp_data = zip(Ts,[perform_binning_analysis(i) for i in H])
	Cps_fcd = []
	err = []
	
	for i in np.arange(len(Cp_data)-1):
		T2 = Cp_data[i+1][0]
		T1 = Cp_data[i-1][0]
		H2 = Cp_data[i+1][1][0]
		H1 = Cp_data[i-1][1][0]
		var_H2 = var_Hs[i+1]
		var_H1 = var_Hs[i-1]

		if T2-T1 == 2*epsilon:
			Cps_fcd.append([T2-epsilon,(H2-H1)/(2*epsilon)])
			error = np.sqrt(var_H2+var_H1-2*np.cov(H[i+1],H[i-1])[0][1])
			err.append(error)

	m,b = np.polyfit([i[0] for i in Cps_fcd],[i[1] for i in Cps_fcd],1)
	x = np.linspace(Ts[0],Ts[-1],100)

	# Print
	print("\n{}:".format(label))
	print("Slope: {}".format(m))
	print("Intercept: {}".format(b))
	#plt.errorbar([i[0] for i in Cps_fcd],[i[1] for i in Cps_fcd], yerr=err,label=label,fmt="-o")
	plt.plot([i[0] for i in Cps_fcd],[i[1] for i in Cps_fcd],label=label)
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
plot_Cp(data_dry,epsilon,label_dry)
plot_Cp(data_025,epsilon,label_025)
plot_Cp(data_050,epsilon,label_050)
plot_Cp(data_100,epsilon,label_100)
plt.legend()
plt.show()


