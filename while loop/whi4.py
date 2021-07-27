# reverse number
# 123 = 321
i=int (input("enter the number:"))
box=0

while i > 0:
    box = (box*10) + i%10
    i= int (i/10)
print("reverse number=",box)