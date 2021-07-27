# armstrong number

class Abc:
    def arm(self,n):
        box = 0
        while n > 0:
            rem = n % 10
            box = box + (rem * rem * rem)
            n = int (n/10)
        print("armstrong number=",box)
num = int (input("enter the number :"))

object = Abc()
object . arm (num)