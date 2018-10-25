let t=$2\*60\*60+$3\*60+$4
sed -i s/'N'$1/$t/g processor_results.dat
