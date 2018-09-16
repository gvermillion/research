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

executable   = /work/gcates/research/prod/8x8x2/dry/run.sh 


arguments = 539   
Queue
arguments = 540   
Queue
arguments = 541   
Queue
arguments = 542   
Queue
arguments = 543   
Queue
arguments = 544   
Queue
arguments = 545   
Queue
arguments = 546   
Queue
arguments = 547 
Queue
arguments = 548   
Queue
arguments = 549   
Queue
arguments = 550   
Queue
arguments = 551   
Queue
arguments = 552   
Queue
arguments = 553   
Queue
arguments = 554   
Queue
arguments = 555   
Queue
arguments = 556   
Queue
arguments = 557   
Queue
arguments = 558   
Queue
arguments = 559   
Queue
arguments = 560   
Queue
