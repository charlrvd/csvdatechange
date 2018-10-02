# csvdatechange

This is small script that I have used to convert datetime on csv files.

This is more modular that a bash or perl script to me and allowed me to work more with python

## Example

For the [file](Sacramentorealestatetransactions.csv)
```
street,city,zip,state,beds,baths,sq__ft,type,sale_date,price,latitude,longitude
3526 HIGH ST,SACRAMENTO,95838,CA,2,1,836,Residential,Wed May 21 00:00:00 EDT 2008,59222,38.631913,-121.434879
```
The date format originaly is `%a %b %d %H:%M:%S %Z %Y` ex:`Wed May 21 00:00:00 EDT 2008`

The changed dateformat would be `%Y/%m/%d-%H.%M.%S(%Z)` ex:`2008/05/21-00.00.00(EDT)`

![](diff.png?raw=true)

The settings file used to make this transformation is [here](settingstest.py)

The list of config to do in settings is as follow:
- `in_format` is a datetime format as defined in a below link
- `out_format` is the desired output format
- `in_file` and out_file are the name of the file input and output to write to
- `date_index` is a list of integer to specify the date column (start at index 0)
  This could be removed in a future version with a re.match on the first line of data
- `split_char` is the column delimiting character
- `timezone` is the input timezone is there is any. Can be set to `None`
  Script could later need out_timezone to output the time on another timezone

### How to use

For every type of csv you will need to new settings file containing a `class Settings`

In a main file ([example](main.py)) you can import the settings and the function
```python
import csvdate
from sacramento_settings import Settings as Sacramento
[...]
  settings = Sacramento()
  csvdate.rewrite(settings)
```

If is possible to loop over a list of csv of same format to modify all of them a the same time

It would require to update the settings of out_file inside the loop after each file to avoir rewrite over the same file over and over.
 

## Datetime format syntax
[Documentation link](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior)

## Tips to convert csv
convert windows generated csv with ^M newline character
```
:%s/<Ctrl-V><Ctrl-M>/\r/g
```
