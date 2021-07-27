# revers number
def revers(n):
    box=0
    while n>0:
        rem= n % 10
        box=(box*10) + rem
        n=n//10
    print("revers=",box)
num = int(input("enter the number:"))
revers(num)

