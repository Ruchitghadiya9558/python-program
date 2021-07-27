# user thi val and multiplication number

class Abc:
    def mul(self,n):
        box = 1
        while n > 0:
            rem = n % 10
            box = box * rem
            n = int(n/10)
        print("multiplication=",box)
num = int (input("enter the number:"))

object = Abc()
object.mul(num)