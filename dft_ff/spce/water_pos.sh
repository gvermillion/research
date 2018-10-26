# Calls floating arithmatic stuff
. mod/float.sh

for j in {0..19};
	do 	
#		echo "3" >> water_pos/${i}.xyz
#		echo "" >> water_pos/${i}.xyz
		python water_shifter_rotator.py 0.0 0.0 $(float_eval "3.14 / 20 * ${j}") >> water_pos/${j}.xyz
		cd water_pos/
		let i==1
		echo "3" >> tmp
		echo "" >> tmp
		while read line;
			do
				let i++
				if [ "${i}" = "1" ]; 
					then
						echo "O "$line >> tmp
					else
						echo "H "$line >> tmp
				fi
			done < ${j}.xyz

		rm ${j}.xyz
		mv tmp ${j}.xyz
		cd ../
		unset i
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
