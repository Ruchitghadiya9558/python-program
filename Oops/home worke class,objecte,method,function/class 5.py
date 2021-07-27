# revers number

class Abc:
    def revers(self,n):
        box = 0
        while n > 0:
            rem = n % 10
            box = (box*10) + rem
            n = n//10
        print("revers number=",box)
num = int (input("enter the number :"))

object = Abc()
object . revers(num)