CSV Bar
=======

Draw bar charts from CSV files in the terminal.

Tested on Python 2.7 and 3.5.


Installing
----------

    pip install csvbar


Usage
-----

Say you have a CSV file such as:

```
Donor,Value
Trust,93167.74
Limited Liability Partnership,100522.93
Friendly Society,111428.84
Registered Political Party,382227.01
Unincorporated Association,2846016.31
Company,3696180.22
Individual,11021726.04
Trade Union,44483505.54
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
