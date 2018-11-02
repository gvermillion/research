for k in {4..6}
	do
		for i in {0..9}
			do
				echo RUNNING FOR 0.${k}${i}
				./calc_pe.sh 50 0.${k}${i} 0.001
			done
	done
