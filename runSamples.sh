#!/usr/bin/env bash

cp lookups/country.city.timezone.offset_dist.csv lookups/country.city.timezone.offset.csv
cp lookups/sub-cleanse_dist.sh lookups/sub-cleanse.sh
chmod +x lookups/sub-cleanse.sh
cp input/Team-A.csv-dist input/Team-A.csv
cp input/Team-B.csv-dist input/Team-B.csv

./clean.sh