#!/usr/bin/env bash

cp lookups/country.city.timezone.offset_dist.csv lookups/country.city.timezone.offset.csv
cp input/Team-A.csv-dist input/Team-A.csv

python3 ./clean.py