from dateutil.parser import parse

mydate = "24 november 2016"  #2016-11-24
mydate1 = parse(mydate)

ymd = mydate.strftime("%Y/%m/%d")
print(ymd)
