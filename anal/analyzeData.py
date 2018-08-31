import numpy as np
import matplotlib.pyplot as plt
import sys,os
import pickle
import csv

def validateInput():
	if len(sys.argv) != 2:
    		print("Usage: python {} DATA_DIR".format(sys.argv[0]))
    		sys.exit(2)
	return sys.argv[1]

def readFile(filename):
	if os.path.exists(filename):
		print("\t Reading data from {}.".format(filename))
		ts = []
		temps = []
		pes = []
		presss = []
		vols = []
		cellas = []
		cellbs = []
		cellcs = []
		cellgammas = []
		with open(filename,'r') as file:
			i = 1
			for row in file:
				if i > 2:
					t, temp, pe, press, vol, cella, cellb, cellc, cellgamma = row.split()
					ts.append(float(t))
					temps.append(float(temp))
					pes.append(float(pe))
					presss.append(float(press))
					vols.append(float(vol))
					cellas.append(float(cella))
					cellbs.append(float(cellb))
					cellcs.append(float(cellc))
					cellgammas.append(float(cellgamma))
				i += 1
		ts = np.asarray(ts)
		temps = np.asarray(temps)
		pes = np.asarray(pes)
		presss = np.asarray(presss)	
		vols = np.asarray(vols)	
		cellas = np.asarray(cellas)	
		cellbs = np.asarray(cellbs)	
		cellcs = np.asarray(cellcs)	
		cellgammas = np.asarray(cellgammas)	
	else:
    		print("ERROR: Files not found.")
    		sys.exit(3)
	return ts, temps, pes, presss, vols, cellas, cellbs, cellcs, cellgammas 

def writeToFile(data):
	with open("{}/analyzedData.dat".format(data_dir), "wb") as dataFile:
		print("\t Writing data to {}".format(dataFile))
		pickle.dump(data,dataFile)
		

def binningAnalysis(O,k):
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

def performBinningAnalysis(O):
    N = len(O)      
    
    # Initialize variables for tracking data
    Neff = 0.0
    blockError = 0.0
    tINTo = 0.0     

    for i in range(N//10):
        k = i+1
        Oavg, tINToNew, NeffNew, blockErrorNew = binningAnalysis(O,k)
        if tINToNew > tINTo:
            Neff = NeffNew
            blockError = blockErrorNew
            tINTo = tINToNew
    data = [Oavg,tINTo,Neff,blockError]
    return data
      	#return Oavg, tINTo, Neff, blockError

# MAIN

data_dir = validateInput()
data = []
# Cycle through files in /data dir
for root, dirs, files in os.walk(data_dir):
	for fil in files:
		start = fil.find("Temp") + 4
		end = fil.find(".dat") + 1
		if start>4: # If a valid data file name
			print("Processing data for: {}".format(fil))
			targetTemp = float(fil[start:end])
			ts, temps, pes, presss, vols, cellas, cellbs, cellcs, cellgammas = readFile("{}/{}".format(data_dir,fil))
			tempData = performBinningAnalysis(temps)
			peData = performBinningAnalysis(pes)
			pressData = performBinningAnalysis(presss)
			volData = performBinningAnalysis(vols)
			cellaData = performBinningAnalysis(cellas)
			cellbData = performBinningAnalysis(cellbs)
			cellcData = performBinningAnalysis(cellcs)
			cellgammaData = performBinningAnalysis(cellgammas)
			#writeToFile([targetTemp,tempData,peData,pressData,volData,cellaData,cellbData,cellcData,cellgammaData])
			data.append([targetTemp,tempData,peData,pressData,volData,cellaData,cellbData,cellcData,cellgammaData,temps,pes,presss,vols])
			
		else:
			print("Skip")
data.sort()
writeToFile(data)
