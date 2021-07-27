# multiplaiction number

class Xyz:
    def mul(self,n):
        box = 1
        for i in range(1,n+1):
            box = box * i
        print("multiplaction=",box)
num = int (input("enter the number :"))

object = Xyz()
object.mul(num)