# csvdatechange

This is small script that I have used to convert datetime on csv files.

This is more modular that a bash or perl script to me and allowed me to work more with python

## example

For the [file](Sacramentorealestatetransactions.csv)
```
street,city,zip,state,beds,baths,sq__ft,type,sale_date,price,latitude,longitude
3526 HIGH ST,SACRAMENTO,95838,CA,2,1,836,Residential,Wed May 21 00:00:00 EDT 2008,59222,38.631913,-121.434879
```
The date format originaly is `%a %b %d %H:%M:%S %Z %Y` ex:`Wed May 21 00:00:00 EDT 2008`

The changed dateformat would be `%Y/%m/%d-%H.%M.%S(%Z)` ex:`2008/05/21-00.00.00()`

Will need to further work on timezone as it is not getting it into accout right now.

## datetime format syntax
[Documentation link](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior)

## Tips to convert csv
convert windows generated csv with ^M newline character
```
:%s/<Ctrl-V><Ctrl-M>/\r/g
```
