echo Generating partial charge geometries
cd mod/
./gen_qs.sh $1 $2
cd ../

echo Measuring partial charge:
echo Water:
for i in {0..9};
	do
		echo $i
		cd mod/q_$i

		for j in {0..19}; 
			do 
				../../run_water.sh $j 
			done | grep '^       0' | tee ../../data/current_run/pe_water_q_$i.dat 
		cd ../../
	done
echo System:
for ii in {0..9};
	do
		echo $ii
		cd mod/q_$ii

		for jj in {0..19}; 
			do 
				../../run_system.sh $jj 
			done | grep '^       0' | tee ../../data/current_run/pe_system_q_$i.dat 
		cd ../../
	done

echo Cleaning up
mkdir data/$1N
mv data/current_run/* data/$1N
for k in {0..9}; 
	do
		rm -r mod/q_$k
	done
