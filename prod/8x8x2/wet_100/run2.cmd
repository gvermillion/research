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

executable   = /work/gcates/research/prod/8x8x2/wet_100/run.sh 


arguments = 2000  
Queue
