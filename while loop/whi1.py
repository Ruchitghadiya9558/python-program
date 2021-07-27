#123 = 3+2+1=6 sum

x=int(input("enter the number:"))
box=0

while x>0:
    rem=x % 10          #last digit
    box=box+rem         #store
    x = int (x / 10)    #remove last digit
print("sum=",box)


