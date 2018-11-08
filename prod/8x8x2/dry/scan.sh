cp def/run_def.in tmp/run_$1.in
sed -i s/'PROBETEMP'/$1/g tmp/run_$1.in	
cp def/run_def.moab tmp/run_$1.moab
sed -i s/'PROBETEMP'/$1/g tmp/run_$1.moab	
msub tmp/run_$1.moab	
