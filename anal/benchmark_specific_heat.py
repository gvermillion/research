import numpy as np
import matplotlib.pyplot as plt
import sys,os
import pickle
import csv

# PREAMBLE
def validate_input():
	if len(sys.argv) < 4:
    		print("Usage: python {} ANALYZED_DATA_FILE EPSILON LABEL".format(sys.argv[0]))
    		sys.exit(2)
	return sys.argv[1], float(sys.argv[2]), sys.argv[3]

#def validate_input():
#	if len(sys.argv) < 4:
#    		print("Usage: python {} ANALYZED_DATA_FILE EPSILON LABEL ERROR_BARS(1: YES/0: NO [default])".format(sys.argv[0]))
#    		sys.exit(2)
#	elif len(sys.argv) == 4:
#		return sys.argv[1], float(sys.argv[2]), sys.argv[3], int(0)
#	else:
#		return sys.argv[1], float(sys.argv[2]), sys.argv[3], int(sys.argv[4])
def same_length(a,b):
	if len(a) < len(b):
		return a, b[:len(a)]
	elif len(b) < len(a):
		return a[:len(b)], b
	else:
		return a,b
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
U = np.array([i[10] for i in data]) # [eV]
p = np.array([i[11] for i in data]) # [bar]
V = np.array([i[12] for i in data]) # [angstrom**3]

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
			H2s, H1s = same_length(H[i+1],H[i-1])
			error = np.sqrt(var_H2+var_H1-2*np.cov(H2s,H1s)[0][1])
			err.append(error)

	m,b = np.polyfit([i[0] for i in Cps_fcd],[i[1] for i in Cps_fcd],1)
	x = np.linspace(Ts[0],Ts[-1],100)
	
	# Benchmark (American Mineralogist, Volume 76, pages 557-568, 1986)
	C1 = 1625.842
	C2 = -0.425206
	C3 = 12.0318*10**(-5)
	C4 = -20180.94
	C5 = 6.82544*10**(6)
	bench_Ts = np.linspace(200,1800,1000)
	bench_Cps = C1 + C2*bench_Ts + C3*bench_Ts**2 + C4*bench_Ts**(-0.5) + C5*bench_Ts**(-2) # [J/mol/K]
	#convert = 1.037*10**(-5) # [J/mol/K] -> [eV/K]
	#convert = 1#6.242 # [J/mol/K] -> [eV/mol/K] E-18
  	convert = 188.36 # [ev/K] -> [J/mol/K]

	# Print
	print("\n{}:".format(label))
	print("Slope: {}".format(m))
	print("Intercept: {}".format(b))
	#plt.errorbar([i[0] for i in Cps_fcd],[i[1] for i in Cps_fcd], yerr=err,label=label,fmt="-o")
	plt.plot(x,(m*x+b)*convert,label="{} fit".format(label))
	plt.plot(bench_Ts,bench_Cps,label="Exp")

	
# Plot
plt.figure()
plt.title("Specific Heat: {}\nCenter FD Method".format(label))
plot_Cp(data,epsilon,label)
plt.xlabel("Temperature [K]")
plt.ylabel("Cp [J/mol/K]")
plt.legend()
plt.show()
