from  datetime import  datetime
from  pytz import timezone
south_africa = ("Africa/Johannesburg")

currentedatetime = datetime.today()
print(currentedatetime)
print(type(currentedatetime))

print(currentedatetime.day)
print(currentedatetime.month)
print(currentedatetime.year)

print("----------------------------")

print(currentedatetime.hour)
print(currentedatetime.minute)
print(currentedatetime.second)

# current time

currentetime = currentedatetime.strftime("%H : %M : %S")
print(currentetime)

# south

currentetime1 =  datetime.now(south_africa)
print(currentetime1)