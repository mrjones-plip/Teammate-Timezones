#!/bin/bash

# clean up from prior runs
cat /dev/null > output.csv
cat /dev/null > ./html/outputFinal.csv

# clean up files and concat to one single file
for file in ./input/*.csv; do
    if [ -f "$file" ]; then
        tail -n +2 $file >> output.csv
        echo -e "\n" >> output.csv
    fi
done

if [[ -f "./lookups/sub-cleanse.sh" && -x "./lookups/sub-cleanse.sh" ]]
then
    ./lookups/sub-cleanse.sh
else
  echo "Skipping './lookups/sub-cleanse.sh' - not found or not executable";
fi

# download
# https://simplemaps.com/static/data/world-cities/basic/simplemaps_worldcities_basicv1.73.zip
# extract worldcities.csv into ./lookups/
#
# create file with unique ISO,country,city,timezone from
# official timezone list: https://en.wikipedia.org/wiki/Zone.tab

# inject lat lon and timezone
echo "Teammate,Team,Title,City,Country,ISO,Hub,latitude,longitude,timezone" > ./html/outputFinal.csv
while read p; do
  if [ "$p" != "" ]; then
    countryISO=$( echo "$p"|cut -d"," -f2 )
    countryFUll=$( echo "$p"|cut -d"," -f3 )
    city=$( echo "$p"|cut -d"," -f4 )
    latLonLine=$( grep "^\"$city" ./lookups/worldcities.csv | grep "\"$countryISO\"" | head -1 )

    if [[ -f "./lookups/country.city.timezone.offset.csv"  ]]
    then
      timezoneLine=$( grep "^$countryISO,$countryFUll,$city" ./lookups/country.city.timezone.offset.csv )
    else
      timezoneLine='NA'
    fi

    lat=$( echo "$latLonLine"|cut -d"\"" -f6)
    lon=$( echo "$latLonLine"|cut -d"\"" -f8 )
    tz=$( echo "$timezoneLine"|cut -d"," -f4 )
    echo "$p,$lat,$lon,$tz" >> ./html/outputFinal.csv
  fi
done < output.csv

rm output.csv