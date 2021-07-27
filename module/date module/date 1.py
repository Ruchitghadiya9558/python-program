from datetime import date

currentdate = date.today()
print(currentdate)
print(type(currentdate))

month = currentdate.month
print(month)

year = currentdate.year
print(year)

date = currentdate.day
print(date)

# format

Dmy = currentdate.strftime("%d/%m/%Y")
print(Dmy)
print(type(Dmy))