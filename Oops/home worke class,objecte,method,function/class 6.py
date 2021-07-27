# palindrong number
class Abc:
 def palin(self,i):
    box = 0
    x=i
    while i > 0:
        rem = i % 10
        box = (box * 10) + rem
        i = int (i/10)
    if (box==i):
        print("palindrong number ")
    else:
        print("not palindrong number")

num = int (input("enter the number :"))

object = Abc()
object.palin(num)