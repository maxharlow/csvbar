CSV Bar
=======

Draw bar charts from CSV files in the terminal.

Requires either version 2 or 3 of [Python] (https://www.python.org/), including `pip`.


Installing
----------

Install with Pip: `pip install csvbar`.


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
$ csvbar data.csv

Trust                          ▌ 93,167.74 (0.15%)
Limited Liability Partnership  ▌ 100,522.93 (0.16%)
Friendly Society               ▌ 111,428.84 (0.18%)
Registered Political Party     ▌ 382,227.01 (0.61%)
Unincorporated Association     ███ 2,846,016.31 (4.54%)
Company                        ████ 3,696,180.22 (5.89%)
Individual                     ████████████ 11,021,726.04 (17.57%)
Trade Union                    ██████████████████████████████████████████████████ 44,483,505.54 (70.91%)

Total: 62,734,774.63
```

It also accepts data on STDIN, useful if you're using something like [CSV Kit] (https://github.com/onyxfish/csvkit) or [Q] (https://github.com/harelba/q).


Inspiration
-----------

There are similar tools:

 * [data_hacks] (https://github.com/bitly/data_hacks), by [Bitly] (https://bitly.com/)
 * [termgraph] (https://github.com/mkaz/termgraph), by [Marcus Kazmierczak] (https://twitter.com/mkaz)
 * [spark] (https://github.com/holman/spark), by [Zach Holman] (https://twitter.com/holman)
