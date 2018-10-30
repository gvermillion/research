cp def/run_def.in run_$1.in
sed -i s/'PROBETEMP'/$1/g run_$1.in	
cp def/run_def.moab run_$1.moab
sed -i s/'PROBETEMP'/$1/g run_$1.moab	
msub run_$1.moab	
