from datetime import datetime

mydate = "2011/06/15"  #y/m/d  to  d/m/y

mydatetimeobj = datetime.strptime(mydate,"%Y/%m/%d")
print(mydatetimeobj)
print(type(mydatetimeobj))

dmy = mydatetimeobj.strftime("%d/%m/%Y")
print(dmy)
print(type(dmy))