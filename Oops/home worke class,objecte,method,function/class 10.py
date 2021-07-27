# (1-10) number 3 divisible

class Abc:
    def div(self):
        box = 0
        for i in range(1,11):
            if (i % 3==0):
                box = box + 1
        print("count=",box)

object = Abc()
object.div()

