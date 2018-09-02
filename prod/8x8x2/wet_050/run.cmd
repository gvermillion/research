#!/bin/bash

universe     = vanilla
requirements = OpSys == "Ubuntu16" && (CUDA0Capability >= 3.5) && CUDA0Capability >= 3.0
Rank         = CUDA0GlobalMemoryMb
request_GPUs = 1
request_CPUs = 1

dir          = log
Log          = $(dir)/$(Cluster)_condor_run.log
Error        = $(dir)/$(Cluster)_$(Process).error
Output       = $(dir)/$(Cluster)_$(Process).out

executable   = /work/gcates/research/prod/8x8x2/wet_050/run.sh 


arguments = 100  
Queue
arguments = 200  
Queue
arguments = 300  
Queue
arguments = 400  
Queue
arguments = 500  
Queue
arguments = 600  
Queue
arguments = 700  
Queue
arguments = 800  
Queue
arguments = 900  
Queue
arguments = 1000  
Queue
arguments = 1100  
Queue
arguments = 1200  
Queue
arguments = 1300  
Queue
arguments = 1400  
Queue
arguments = 1500  
Queue
arguments = 1600  
Queue
arguments = 1700  
Queue
arguments = 1800  
Queue
arguments = 1900  
Queue
arguments = 2000  
Queue
