from datetime import datetime,timedelta

currentdatetime = datetime.today()
print(currentdatetime)
print(type(currentdatetime))

three_hours_before_time = currentdatetime + timedelta(hours=3)
print(three_hours_before_time)
print(type(three_hours_before_time))

mytime = three_hours_before_time.strftime("%H : %M : %S : %p")
print(mytime)