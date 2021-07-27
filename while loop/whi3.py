# armstrong number
# 123 =1*1*1 + 2*2*2 +3*3*3 = 1 + 8 + 27 =36
#153  =1*1*1 + 5*5*5 +3*3*3* =1 + 125 + 27 =153

n=int(input("enter the number:"))
box=0
x=n

while n > 0:
    rem=n % 10
    box = box + (rem * rem * rem)
    n= int(n/10)
if (box==x):
    print("armstrong ")
else:
    print("not armstrong ")


