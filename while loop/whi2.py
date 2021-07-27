# 123 = 3*2*1 = 6

n=int(input("enter the number:"))
box=1

while n > 0:
    rem=n % 10
    box=box * rem
    n= int(n/10)
print("mul=",box)