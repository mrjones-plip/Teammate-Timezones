# Teammate Timezones

## Intro

Teammate Timezones is an interactive choropleth map showing where your teammates work in the world. It shows the local time in each location. It uses the open source [MapTable library](https://github.com/Packet-Clearing-House/maptable) to render the map which may be zoomed and filtered. 

![](./map.sample.png)

To get started, generate a CSV file called `outputFinal.csv` using the format below. Put it into the `html` directory and copy all the files in that directory to your website.

## CSV Format

Teammate Timezones needs a file called `outputFinal.csv` in the `./html/` directory with the following fields:

| Field | Description | Example |
--- | --- | ---
| Teammate | name of the person | Shaffan Fares |
| ISO | 2 letter name in [ISO_3166-1_alpha-2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) | CA |
| Mailing Country | Full name of country | Canada |
| Mailing City | City! | Victoria |
| Title | Title at Company | Director of App Services |
| Team | Team! | App Services |
| Hub | Office the teammate is based out of | Dakar |
| latitude | latitude! | 14.7319 |
| longitude | longitude! | -17.4572 |
| timezone | Official entry from [Zone.tab](https://en.wikipedia.org/wiki/Zone.tab) | Africa/Abidjan |

The CSV must have at least the `Teammate` and `ISO` columns to render the choropleth.  It must have the `latitude` and `longitude` to generate a marker.  It must have `timezone` to generate the local time.
 
## CSV Example

| Teammate | ISO | Mailing Country | Mailing City  | Title | Team |  Hub | latitude | longitude | timezone |
--- | --- | --- | --- | --- | --- | --- | --- | ---  | ---  
| Shaffan Fares | CA | Canada | Victoria | Director of App Services | Team A | Distributed | 48.4283 | -123.3647 | America/Vancouver |
| Majid Saber | SN | Senegal | Dakar | App Developer Manager | Team A  | Dakar | 14.7319 | -17.4572 | Africa/Abidjan |
| Ghatiya Iman | SN | Senegal | Dakar | Sr App Developer | Team A | Dakar |14.7319 | -17.4572 | Africa/Abidjan |

## CSV Generation 

If you don't have a fully formed CSV file already there's a `clean.sh` script to help you out.  It was developed for a very specific use case which may not apply to you. In order to use it you need:

1. At least one file ending in `.csv` in the `./input/` directory.  `Mailing Country` and `Mailing City`  will be used to search for a lat lon.
1. Optionally have a `sub-cleanse.sh` bash script in `./lookups/` where you can do any manual clean up needed. 
1. Have a `country.city.timezone.offset.csv` file to lookup timezones in

**WARNING** - `clean.sh`  will overwrite the `outputFinal.csv` file.  Use this script with caution!

The `worldcities.csv` file is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) from [Simplemaps.com](https://simplemaps.com).  Thanks to them for providing a free version of their [world cities data](https://simplemaps.com/data/world-cities) with a permissive license!

## Sample map 

You can can run sample data through the CSV Generation `clean.sh` script by running the `runSamples.sh` script. It can be good way to get up and running with the lookup files and a map. You can then edit these in place and re-run the `clean.sh` script to re-compile the `outputFinal.csv` file.

**WARNING** - `runSamples.sh`  will overwrite the `outputFinal.csv` , `sub-cleanse.sh` and `country.city.timezone.offset.csv` files.  Use this script with caution!

