

n=$2 

sort =k${n}n $1 | awk -v n=$n 'NR==1{print "min ("n"):"i,$n} END{print "max("n"):", $n}' 
