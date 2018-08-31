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

executable   = /work/gcates/research/prod/8x8x2/wet_025/run.sh 


arguments = 1100  
Queue
arguments = 1700  
Queue
arguments = 1800  
Queue
arguments = 1900  
Queue
arguments = 2000  
Queue
