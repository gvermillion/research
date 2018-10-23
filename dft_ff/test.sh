# Calls floating arithmatic stuff
. mod/float.sh

for i in {0..19};
	do 	
		echo "3" >> water_pos/${i}.xyz
		echo "" >> water_pos/${i}.xyz
		python water_shifter_rotator.py 0. 0. $(float_eval "3.14 / 20 * ${i}") >> water_pos/${i}.xyz
	done






#for j in {0..9};
#	do
#		cp -r q_def/ q_${j}/
#		cd q_${j}/
#		sed -i s/'def'/${j}/g calc_pe.in
#		sed -i s/'def'/${j}/g calc_pe_water.in
#
#		for i in {0..19};
#			do
#				mv beryl_water_${i}_q_def.mod beryl_water_${i}_q_${j}.mod
#				sed -i s/'Q_O'/$(float_eval "$1 * 1 + ${j} * $2")/g beryl_water_${i}_q_${j}.mod 
#				sed -i s/'Q_H'/$(float_eval "($1 * 1 + ${j} * $2) / 2")/g beryl_water_${i}_q_${j}.mod
#			done
#
#		cd ../
#	done
