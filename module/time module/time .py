from datetime import time

#time (hour=0 , minute=0, second=0)

a = time()
print("a=",a)

# time (hour,minute,second)

b = time(10,12,55)
print("b =",b)
print(type(b))

#time (hour , time and minute)
c = time(hour=10, minute=20, second=55)
print("c =",c)
print(type(c))

#time (hour , minute , second , microsecond)

d = time(10,14,47,254685)
print("d=",d)
print(type(d))