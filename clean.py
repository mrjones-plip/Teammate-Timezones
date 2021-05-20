

import csv
import glob
import os.path

csvFiles = glob.glob('./input/*.csv')

citiesFile = open("./lookups/worldcities.csv")
outputFile = open('./html/outputFinal.csv', 'w', newline='')

cities = csv.reader(citiesFile)
output = csv.writer(outputFile)

if os.path.isfile("./lookups/country.city.timezone.offset.csv"):
    timezonesFile = open("./lookups/country.city.timezone.offset.csv")
    timezones = csv.reader(timezonesFile)
else:
    timezones = False
    timezonesFile = False

header = ["Teammate", "Team", "Title", "City", "Country",
          "Hub", "latitude", "longitude", "iso_a2", "timezone"]
output.writerow(header)

for file in csvFiles:
    reader = csv.reader(open(file, "r"))
    isFirstRow = True
    for teammate in reader:

        # first for has column headers, skip it
        if isFirstRow is True:
            isFirstRow = False
            continue

        # set local vars for city and country. default found to string 'nope'
        teammateCity = teammate[3]
        teammateCountry = teammate[4]

        # rewind citiesFile CSV to beginning. if this isn't here "for city in cities" does nothing on N + 1 run
        citiesFile.seek(0)
        if timezones is not False:
            timezonesFile.seek(0)

        # todo: cache found cities so do avoid this loop on cities we've seen before
        # todo: handle soft matches/more than one match - city names are NOT unique!
        foundCity = False
        for city in cities:
            searchCity = city[0]
            searchCityAdmin = city[7]
            searchCountry = city[4]
            searchISO2 = city[5]
            searchISO3 = city[6]
            lat = city[2]
            lon = city[3]
            if (teammateCountry == searchCountry or teammateCountry == searchISO3) and \
                    (teammateCity == searchCity or teammateCity == searchCityAdmin):
                foundCity = True
                teammate.append(lat)
                teammate.append(lon)
                teammate.append(searchISO2)
                break

        if not foundCity:
            teammate.append('NA')
            teammate.append('NA')
            teammate.append('NA')
            print('Could not resolve this teammate to a lat/lon: ' + str(teammate))

        if timezones is not False:
            foundTimezone = False
            for timezone in timezones:
                searchCity = timezone[2]
                searchISO2 = timezone[0]
                searchTimezone = timezone[3]
                if teammateCity == searchCity:
                    foundTimezone = True
                    teammate.append(searchTimezone)
                    break

            if not foundTimezone:
                teammate.append('NA')
                print('Could not resolve this teammate to a timezone: ' + str(teammate))
        else:
            teammate.append('NA')
            print('"./lookups/country.city.timezone.offset.csv" not present, can\'t resolve '
                  'teammate to timezone: ' + str(teammate))

        output.writerow(teammate)