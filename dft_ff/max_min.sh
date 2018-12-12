

n=$2 

sort -k${n}n $1 | awk -v n=$n 'NR==1{print $n} END{print $n}' | paste -sd- - | bc 

