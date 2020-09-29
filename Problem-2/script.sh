while read line;
do 
    echo $line;
    country="$(cut -d',' -f3 <<< $line)"
    echo $country
done < './teams.csv'