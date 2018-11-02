# Calls floating arithmatic stuff
. float.sh

for j in {0..9};
	do
		cp -r q_def/ q_${j}/
		cd q_${j}/
		sed -i s/'def'/${j}/g calc_pe.in
		sed -i s/'def'/${j}/g calc_pe_water.in

		let i=0
		while [ $i -lt $1 ]
			do
				mv beryl_water_${i}_q_def.mod beryl_water_${i}_q_${j}.mod
				sed -i s/'Q_H'/$(float_eval "$2 * 1 + ${j} * $3")/g beryl_water_${i}_q_${j}.mod 
				sed -i s/'Q_O'/$(float_eval "($2 * 1 + ${j} * $3) * 2")/g beryl_water_${i}_q_${j}.mod
				i=$[$i+1]
			done

		cd ../
	done
