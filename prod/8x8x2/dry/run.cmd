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


arguments = 606   
Queue
arguments = 618   
Queue
arguments = 619   
Queue
arguments = 620   
Queue
arguments = 621   
Queue
arguments = 622   
Queue
arguments = 623   
Queue
arguments = 624   
Queue
arguments = 625   
Queue
arguments = 626 
Queue
arguments = 627   
Queue
arguments = 628   
Queue
arguments = 629   
Queue
arguments = 630   
Queue
arguments = 631   
Queue
arguments = 632   
Queue
arguments = 633   
Queue
arguments = 634   
Queue
arguments = 635   
Queue
arguments = 636   
Queue
arguments = 637   
Queue
arguments = 638   
Queue
arguments = 639   
Queue
