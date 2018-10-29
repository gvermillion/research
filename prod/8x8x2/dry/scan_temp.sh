for i in {501..570}
	do
		cp def/run_def.in run_${i}.in
		sed -i s/'PROBETEMP'/${i}/g run_${i}.in	
		cp def/run_def.moab run_${i}.moab
		sed -i s/'PROBETEMP'/${i}/g run_${i}.moab	
		msub run_${i}.moab	
	done
