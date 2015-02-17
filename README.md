CSV Bar
=======

Draw bar charts from CSV files in the terminal.

Requires either version 2 or 3 of [Python] (https://www.python.org/).


Usage
-----

Say you have a CSV file such as:

```csv
Donor,Value
Friendly Society,49428.84
Limited Liability Partnership,96122.93
Other,233016.58
Registered Political Party,333058.01
Unincorporated Association,2656919.98
Company,3266514.88
Individual,10191197.0
Trade Union,42328877.05
```

You can then:

```bash
$ ./csvbar.py data.csv

Friendly Society               ▌ 49,428.84
Limited Liability Partnership  ▌ 96,122.93
Other                          ▌ 233,016.58
Registered Political Party     ▌ 333,058.01
Unincorporated Association     ███ 2,656,919.98
Company                        ███ 3,266,514.88
Individual                     ████████████ 10,191,197.00
Trade Union                    ██████████████████████████████████████████████████ 42,328,877.05

```


Inspiration
-----------

There are similar tools:

 * [data_hacks] (https://github.com/bitly/data_hacks), by [Bitly] (https://bitly.com/)
 * [termgraph] (https://github.com/mkaz/termgraph), by [Marcus Kazmierczak] (https://twitter.com/mkaz)
 * [spark] (https://github.com/holman/spark), by [Zach Holman] (https://twitter.com/holman)
