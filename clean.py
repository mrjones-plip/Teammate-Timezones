

import re, csv, glob

csvFiles = glob.glob('./input/*.csv')
citiesFile = open("./lookups/worldcities.csv")
# countryData = countryFile.read();
cities = csv.reader(citiesFile)

#   0       1           2      3    4         5     6       7             8         9           10
# "city","city_ascii","lat","lng","country","iso2","iso3","admin_name","capital","population","id"


for file in csvFiles:
    reader = csv.reader(open(file, "r"))
    for teammate in reader:

        foundCity = 'nope'
        for city in cities:

            foundCity = 'nope'
            # if teammate[4] == city[4] and teammate[3] == city[0]:
            # print(teammate[3] + ' match ' + city[0])
            if teammate[3] == city[0]:
                foundCity = str(city)
                break
        citiesFile.seek(0)
            # else:
            #     foundCity = 'nope :('
        #     for col in row:
        #         print(col)

        if foundCity == 'nope':
            print(teammate[3] + ' ' + teammate[4] + ': ' + foundCity)


# #!/bin/bash
#
# # clean up from prior runs
# cat /dev/null > output.csv
# cat /dev/null > ./html/outputFinal.csv
#
# # clean up files and concat to one single file
# for file in ./input/*.csv; do
#     if [ -f "$file" ]; then
#         tail -n +2 $file >> output.csv
#         echo -e "\n" >> output.csv
#     fi
# done
#
# if [[ -f "./lookups/sub-cleanse.sh" && -x "./lookups/sub-cleanse.sh" ]]
# then
#     ./lookups/sub-cleanse.sh
# else
#   echo "Skipping './lookups/sub-cleanse.sh' - not found or not executable";
# fi
#
# # download
# # https://simplemaps.com/static/data/world-cities/basic/simplemaps_worldcities_basicv1.73.zip
# # extract worldcities.csv into ./lookups/
# #
# # create file with unique ISO,country,city,timezone from
# # official timezone list: https://en.wikipedia.org/wiki/Zone.tab
#
# # inject lat lon and timezone
# echo "Teammate,Team,Title,City,Country,ISO,Hub,latitude,longitude,timezone" > ./html/outputFinal.csv
# while read p; do
#   if [ "$p" != "" ]; then
#     countryISO=$( echo "$p"|cut -d"," -f2 )
#     countryFUll=$( echo "$p"|cut -d"," -f3 )
#     city=$( echo "$p"|cut -d"," -f4 )
#     latLonLine=$( grep "^\"$city" ./lookups/worldcities.csv | grep "\"$countryISO\"" | head -1 )
#
#     if [[ -f "./lookups/country.city.timezone.offset.csv"  ]]
#     then
#       timezoneLine=$( grep "^$countryISO,$countryFUll,$city" ./lookups/country.city.timezone.offset.csv )
#     else
#       timezoneLine='NA'
#     fi
#
#     lat=$( echo "$latLonLine"|cut -d"\"" -f6)
#     lon=$( echo "$latLonLine"|cut -d"\"" -f8 )
#     tz=$( echo "$timezoneLine"|cut -d"," -f4 )
#     echo "$p,$lat,$lon,$tz" >> ./html/outputFinal.csv
#   fi
# done < output.csv
#
# rm output.csv