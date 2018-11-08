for i in {0..49}
 do 
  sed -i -e '1,27d' beryl_water_${i}_q_def.mod
  awk '{print $5,$6,$7,$8,$9}' beryl_water_${i}_q_def.mod > ${i}.mod
  sed -i -e '62,70d' ${i}.mod 
 done
