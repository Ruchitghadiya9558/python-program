# palindrome number 525 = 525 yes
#123 = 123 no

i=int (input("enter the number:"))
box=0
rem=i
while i>0:
    box= (box*10) + i%10
    i=int(i/10)
if(rem==box):
    print("palindrome")
else:
    print("not palindrome")
