def addn(n):
    box=0
    for i in range(1,n+1):
        box=box+i
        print(box)

num=int(input("enter the number:"))
addn(num)