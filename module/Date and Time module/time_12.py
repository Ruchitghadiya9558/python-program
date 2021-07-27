from dateutile.parser import parse

# 12 - 24
time_12 = "2:15:30 PM"
datetime_12 = parse(time_12)
time_24 = datetime_12.strftime("%H : %M : %S")
print(time_24)

# 24 - 12
time_24 = "13:15:30 PM"
datetime_24 = parse(time_24)
time_12 = datetime_24.strftime("%I : %M : %S : %P")
print(time_12)