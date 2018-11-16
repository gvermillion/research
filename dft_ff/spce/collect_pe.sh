cd mod/q_spce
for i in {0..299} 
	do
		../../run_system.sh ${i}
	done | grep '^       0' | awk '{print $2}'| tee ../../data/potential_energy.dat
