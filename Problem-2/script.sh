declare -A number

echo "Parsing File..."
while read line;
do 
    # echo $line;
    country="$(cut -d',' -f3 <<< $line)"
    number[$country]=$(( number[$country] + 1))
done < './teams.csv'

echo "Writing results..."
for K in "${!number[@]}"; 
do 
    echo ${K},${number[$K]} >> summary.csv
done

echo "Done"