from datetime import  datetime,timedelta

currentdatetime = datetime.today()
print(currentdatetime)
print(type(currentdatetime))

one_week_before_day = currentdatetime + timedelta(days=15)
print(one_week_before_day)
print(type(one_week_before_day))

one_week_before_day =one_week_before_day.strftime("%d/%m/%y")
print(one_week_before_day)