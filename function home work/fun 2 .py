# multiplication digit number
def mul(n):
    box=1
    while n>0:
        rem= n % 10
        box = box * rem
        n= n//10
    print("mul=",box)
num=int(input("enter the number:"))
mul(num)
