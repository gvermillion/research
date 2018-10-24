echo Loading necessary JUSTUS modules
module load chem/lammps
module load devel/python
module load numlib/python_numpy
echo Determining water rotation coordinates
python gen_coord.py $1
echo Generating partial charge geometries
cd mod/
./gen_qs.sh $1 $2 $3
cd ../


echo Measuring partial charge:
echo Water:
for i in {0..9};
	do
		echo $i
		cd mod/q_$i

		let x=0
		while [ $x -lt $1 ] 
			do	
				echo ${x} 
				../../run_water.sh $x 
				x=$[$x+1]
			done | grep '^       0' | tee ../../data/current_run/pe_water_q_$i.dat 
		cd ../../
		unset x
	done
echo System:
for ii in {0..9};
	do
		echo $ii
		cd mod/q_$ii

		let x=0
		while [ $x -lt $1 ] 
			do 
				../../run_system.sh $x 
				x=$[$x+1]
			done | grep '^       0' | tee ../../data/current_run/pe_system_q_$ii.dat 
		cd ../../
	done

echo Cleaning up
mkdir data/$2N_$1
mkdir data/$2N_$1/water
mkdir data/$2N_$1/system
mv data/current_run/*water* data/$2N_$1/water
mv data/current_run/*system* data/$2N_$1/system
rm -r mod/q_def/
for k in {0..9}; 
	do
		rm -r mod/q_$k
	done
