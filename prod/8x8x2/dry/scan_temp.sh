for i in {12..100}
	do
		cp def/run_def.in tmp/run_${i}.in
		sed -i s/'PROBETEMP'/${i}/g tmp/run_${i}.in	
		cp def/run_def.moab tmp/run_${i}.moab
		sed -i s/'PROBETEMP'/${i}/g tmp/run_${i}.moab	
		msub tmp/run_${i}.moab	
	done
