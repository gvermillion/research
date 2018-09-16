
import numpy as np
import matplotlib.pyplot as plt
import sys,os
import pickle
import csv

# PREAMBLE
def validate_input():
	if len(sys.argv) < 4:
    		print("Usage: python {} ANALYZED_DATA_FILE EPSILON LABEL ERROR_BARS(1: YES/0: NO [default])".format(sys.argv[0]))
    		sys.exit(2)
	elif len(sys.argv) == 4:
		return sys.argv[1], float(sys.argv[2]), sys.argv[3], int(0)
	else:
		return sys.argv[1], float(sys.argv[2]), sys.argv[3], int(sys.argv[4])
datafile, epsilon, label, error = validate_input()
